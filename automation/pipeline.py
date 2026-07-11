"""
The two pipeline entrypoints, wired to GitHub Actions:

  crawl   (cron)            arXiv + inbox -> classify -> one review issue.
                            Writes only data/seen.json and the abstracts sidecar;
                            never touches the curated data files.
  decide  (issue_comment)   apply the reviewer's commands from a review issue to
                            data/, re-render, and close the issue when done.

State is GitHub-native: curated papers in data/*.yaml, handled ids in
data/seen.json, pending proposals in the open review issue (whose body carries
its own payload). The workflows commit whatever these entrypoints write.

Learning loop: every `/edit category=` correction is appended to calibration.json
as an owner-labeled example (templated why), so the classifier improves with each
review. Rejects add no example: a reject can mean low quality, not out of scope.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path

from automation import badges, classify, config, render, reviewflow, sources, storage, taxonomy
from automation.models import Paper

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[1]
CALIBRATION_PATH = _REPO_ROOT / "calibration.json"


# ── intake: classify candidates and propose them into the pool ────────────────

MAX_PER_ISSUE = 25  # large intakes are chunked into several review issues


def classify_and_propose(candidates: list[Paper], dry_run: bool = False,
                         origin: dict[str, str] | None = None) -> None:
    """Shared tail of every intake path (daily crawl, inbox, backlog): classify,
    mark handled ids seen, and open chunked review issues (the pool). Unreviewed
    issues simply stay open; nothing is ever dropped. `origin` maps paper id to
    its source (inbox/backlog/backfill) for the issue's source markers."""
    if not candidates:
        logger.info("nothing new to propose")
        return
    logger.info("classifying %d new candidates", len(candidates))

    cache = storage.load_abstracts()
    items = [
        {"id": p.id, "title": p.title,
         "abstract": cache.get(p.id, "(abstract unavailable; judge from the title alone)")}
        for p in candidates
    ]
    verdicts = classify.classify(items)

    entries: list[dict] = []
    skipped = 0
    failed_ids: list[str] = []
    seen = storage.load_seen()
    for p, v in zip(candidates, verdicts):
        if v.failed:
            failed_ids.append(p.id)  # persisted below; retried on the next intake
            continue
        seen.add(p.id)
        if not v.relevant:
            skipped += 1
            continue
        # The classifier reads the full abstract and may spot an acceptance note
        # the regex extractor missed; fill-only, never overwrite a real venue.
        if v.venue_hint and len(v.venue_hint) <= 40 and p.venue.startswith("arXiv"):
            p.venue = v.venue_hint
        entries.append({
            "paper": p.to_dict(),
            "category": v.category, "tags": v.tags,
            "summary": v.summary, "reason": v.reason,
            "source": (origin or {}).get(p.id, "crawl"),
        })

    note = f"Auto-skipped {skipped} out-of-scope; {len(failed_ids)} failed (retried next run)."
    if dry_run:  # a dry run must leave no trace in the pipeline state
        print(json.dumps(entries, indent=2, ensure_ascii=False))
        print(note)
        return
    # Failures survive the crawl window, but not forever: after three failed
    # attempts a paper is given up on (marked seen) so it cannot clog the queue.
    counts = storage.load_retry_counts()
    for p, v in zip(candidates, verdicts):
        if not v.failed:
            counts.pop(p.id, None)
    for pid in failed_ids:
        counts[pid] = counts.get(pid, 0) + 1
        if counts[pid] >= 3:
            counts.pop(pid)
            seen.add(pid)
            logger.warning("giving up on %s after 3 failed classification attempts", pid)
    storage.save_retry_counts(counts)
    storage.save_seen(seen)
    if not entries:
        logger.info("no relevant papers in this intake (%s)", note)
        return
    # Sort by taxonomy tree order before chunking: same-category papers sit
    # together (outliers stand out), and large intakes chunk into near-uniform
    # category runs, without fragmenting issues per category.
    order = {k: i for i, k in enumerate(taxonomy.load().leaf_keys())}
    entries.sort(key=lambda e: order.get(e["category"], len(order)))
    for start in range(0, len(entries), MAX_PER_ISSUE):
        chunk = entries[start:start + MAX_PER_ISSUE]
        number = reviewflow.create_issue(chunk, note=note if start == 0 else "")
        logger.info("review issue #%d: %d papers proposed", number, len(chunk))


# ── crawl ─────────────────────────────────────────────────────────────────────

def crawl(since: str | None = None, dry_run: bool = False) -> None:
    """Daily intake: everything ANNOUNCED since the last successful run (harvest
    cursor), plus retries and the inbox. A failed run leaves the cursor untouched,
    so missed days self-heal on the next run."""
    from datetime import date, timedelta

    leaves = taxonomy.load().leaf_keys()
    stored: dict[str, str] = {}  # id -> leaf, for the update stream below
    for k in leaves:
        for p in storage.load(k):
            stored[p.id] = k
    known = set(stored) | storage.load_seen() | reviewflow.pending_ids()

    cursor = since or storage.load_harvest_cursor() or str(date.today() - timedelta(days=2))
    retry_papers = list(sources.fetch_arxiv_papers(sorted(storage.load_retry_counts())).values())
    fresh, day_counts = sources.harvest_announced(cursor)
    inbox_papers = sources.read_inbox()
    updates = [p for p in fresh if p.id in stored]  # v2+ of papers we already curate
    origin = {p.id: "inbox" for p in inbox_papers}
    candidates: list[Paper] = []
    for p in retry_papers + fresh + inbox_papers:
        if p.id not in known:
            known.add(p.id)  # also dedups retry vs harvest vs inbox within this run
            candidates.append(p)
    logger.info("harvest: %d new candidates, %d updates of stored papers",
                len(candidates), len(updates))
    if candidates:
        classify_and_propose(candidates, dry_run=dry_run, origin=origin)
    else:
        logger.info("nothing new today")
    if not dry_run:
        _refresh_venues(updates, stored)
        _distill_feedback()  # owner reasons queued by decide -> calibration examples
        # The run succeeded end to end: ledger the swept days, advance the cursor.
        storage.record_harvest(day_counts, cursor=str(date.today()))
        # Thumbs-up inbox comments whose links are now all handled.
        sources.ack_inbox(storage.all_ids(leaves) | storage.load_seen() | reviewflow.pending_ids())
        # Weekends are arXiv's quiet days, and an idle weekday costs nothing:
        # both advance the historical sweep by one slice (old pipeline's intent).
        from datetime import datetime, timezone
        if datetime.now(timezone.utc).weekday() >= 5 or not candidates:
            _weekend_backfill()


def _refresh_venues(updates: list[Paper], stored: dict[str, str]) -> None:
    """Mine the announcement-update stream (v2+ of papers already in the corpus):
    authors often add an acceptance note to the abstract after publication, so an
    update can upgrade our arXiv-default venue to the real one. Never overwrites
    a venue that is already real (set by a conference note or by the owner)."""
    upgraded = False
    for p in updates:
        if p.venue.startswith("arXiv"):
            continue  # the update carries no venue signal
        leaf = stored[p.id]
        papers = storage.load(leaf)
        cur = next(x for x in papers if x.id == p.id)
        if not cur.venue.startswith("arXiv"):
            continue  # already a real venue; not ours to overwrite
        logger.info("venue upgraded from announcement update: %s: %s -> %s",
                    p.title[:55], cur.venue, p.venue)
        cur.venue = p.venue
        storage.save(leaf, papers)
        upgraded = True
    if upgraded:
        render.main()
        badges.refresh()


# ── backfill ──────────────────────────────────────────────────────────────────

def backfill(from_date: str, to_date: str, dry_run: bool = False) -> None:
    """Historical sweep of an ANNOUNCEMENT-date range into the pool; same source
    and same intake tail as the daily crawl, and the same ledger records the
    coverage. Also usable manually to accelerate past the weekend cursor."""
    leaves = taxonomy.load().leaf_keys()
    known = storage.all_ids(leaves) | storage.load_seen() | reviewflow.pending_ids()
    fresh, day_counts = sources.harvest_announced(from_date, until=to_date)
    candidates = [p for p in fresh if p.id not in known]
    logger.info("backfill %s..%s: %d new candidates", from_date, to_date, len(candidates))
    classify_and_propose(candidates, dry_run=dry_run,
                         origin={p.id: "backfill" for p in candidates})
    if not dry_run:
        storage.record_harvest(day_counts)


def pool_has_room() -> bool:
    """Backpressure: historical intakes run only while the review pool is below
    the cap. The owner's review capacity is the system's real bottleneck; the
    pool must never grow past what feels comfortable to clear."""
    cap = int(config.load()["review"].get("pool_cap", 50))
    pending = len(reviewflow.pending_ids())
    if pending >= cap:
        logger.info("review pool at %d papers (cap %d): historical intake paused", pending, cap)
        return False
    return True


def _weekend_backfill() -> None:
    """arXiv announces nothing on weekends, so weekend crawl runs advance the
    historical sweep by one slice instead. Cursor survives in data/backfill.json;
    a failed slice is retried next weekend (the cursor only advances on success)."""
    from datetime import date, timedelta

    cfg = config.load().get("backfill")
    if not cfg:
        return
    cursor = storage.load_backfill_cursor() or cfg["start"]
    if cursor >= cfg["until"]:
        logger.info("historical backfill complete (cursor %s)", cursor)
        return
    if not pool_has_room():
        return
    start = date.fromisoformat(cursor)
    end = min(start + timedelta(days=int(cfg.get("slice_days", 7)) - 1),
              date.fromisoformat(cfg["until"]))
    logger.info("weekend backfill slice: %s..%s", start, end)
    backfill(str(start), str(end))
    storage.save_backfill_cursor(str(end + timedelta(days=1)))


# ── decide ────────────────────────────────────────────────────────────────────

def _distill_feedback() -> None:
    """Turn the owner's terse review feedback (queued by decide) into durable
    calibration examples via one LLM pass. Runs in crawl, which holds the Claude
    token; decide stays token-free. The queue survives a failed distillation."""
    items = storage.load_feedback()
    if not items:
        return
    leaves = taxonomy.load().leaf_keys()
    prompt = (
        "You maintain the calibration examples of a paper classifier for a curated "
        "list of code-agent research. Below are review-feedback items from the list's "
        "owner: category corrections (action=edit, proposed -> final) and rejections "
        "(action=reject) with the owner's terse reasons. For EACH item, draft a "
        "durable classification example: a `why` of 1-2 sentences that turns the "
        "owner's reason into a reusable rule-of-thumb the classifier can apply to "
        "similar papers.\n"
        "- action=edit: category is the corrected leaf; the why explains why it beats "
        "the proposed one.\n"
        "- action=reject: decide from the reason whether the paper is OUT OF SCOPE "
        "(include=true, category=null) or merely low quality / a duplicate "
        "(include=false: quality judgments are not scope rules and must not become "
        "examples).\n"
        f"Valid category keys: {', '.join(leaves)}\n\n"
        "FEEDBACK ITEMS (JSON, one per line):\n"
        + "\n".join(json.dumps(it, ensure_ascii=False) for it in items)
        + "\n\nOUTPUT: an object {results: [...]} with one entry per item, in order: "
        "{id, title, include, category (key or null), tags (list, [] if none), why}."
    )
    schema = {
        "type": "object",
        "properties": {"results": {
            "type": "array", "minItems": len(items), "maxItems": len(items),
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"}, "title": {"type": "string"},
                    "include": {"type": "boolean"},
                    "category": {"anyOf": [{"type": "string", "enum": leaves},
                                           {"type": "null"}]},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "why": {"type": "string"},
                },
                "required": ["id", "title", "include", "category", "tags", "why"],
                "additionalProperties": False,
            },
        }},
        "required": ["results"], "additionalProperties": False,
    }
    try:
        results = classify._run_claude(prompt, schema, classify.MODEL)
    except Exception as exc:
        logger.warning("feedback distillation failed, queue kept: %s", exc)
        return
    data = json.loads(CALIBRATION_PATH.read_text(encoding="utf-8"))
    existing = {e["id"] for e in data["examples"]}
    added = 0
    for ex in results:
        if not ex.get("include") or ex["id"] in existing:
            continue
        data["examples"].append({
            "id": ex["id"], "title": ex["title"], "category": ex["category"],
            "tags": ex.get("tags", []), "why": ex["why"],
        })
        added += 1
    if added:
        CALIBRATION_PATH.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
    storage.save_feedback([])
    logger.info("feedback distilled: %d items -> %d calibration examples", len(items), added)


def decide(issue_number: int) -> None:
    entries, comments, _ = reviewflow.fetch_issue(issue_number)
    reviewer = config.load()["repo"]["reviewer"]
    decisions = reviewflow.parse_decisions(comments, reviewer, len(entries))
    if not decisions:
        logger.info("issue #%d: no commands from %s yet", issue_number, reviewer)
        return

    leaves = set(taxonomy.load().leaf_keys())
    approved, rejected, errors = [], [], []
    added_new = 0
    feedback: list[dict] = []  # owner reasons, distilled into calibration by crawl

    for idx in sorted(decisions):
        action, overrides = decisions[idx]
        e = entries[idx - 1]
        if action == "reject":
            rejected.append(idx)
            if overrides.get("reason"):
                feedback.append({
                    "action": "reject", "id": e["paper"]["id"],
                    "title": e["paper"]["title"], "proposed": e["category"],
                    "reason": overrides["reason"],
                })
            continue
        category = overrides.get("category", e["category"])
        tags = overrides.get("tags", e["tags"])
        if category not in leaves:
            errors.append(f"paper {idx}: unknown category `{category}`")
            continue
        if bad := [t for t in tags if t not in classify.PAPER_TYPES + classify.ARTIFACT_TAGS]:
            errors.append(f"paper {idx}: unknown tags {bad}")
            continue
        p = Paper.from_dict(e["paper"])
        p.category, p.tags, p.summary = category, tags, e.get("summary", "")
        if overrides.get("venue"):
            p.venue = overrides["venue"]
        sources.enrich_links(p)
        if storage.add(p):  # dedup-safe: False when already stored (e.g. a re-run)
            storage.save(category, storage.newest_first(storage.load(category)))
            added_new += 1
        approved.append(idx)
        if "category" in overrides and overrides["category"] != e["category"]:
            feedback.append({
                "action": "edit", "id": p.id, "title": p.title,
                "proposed": e["category"], "final": overrides["category"],
                "reason": overrides.get("reason", ""),
            })

    if feedback:
        storage.save_feedback(storage.load_feedback() + feedback)
        logger.info("queued %d feedback items for distillation", len(feedback))
    if added_new:
        render.main()
        badges.refresh()
    logger.info("issue #%d: %d approved (%d newly added), %d rejected, %d errors",
                issue_number, len(approved), added_new, len(rejected), len(errors))

    if errors:
        reviewflow.post_comment(issue_number, "Some commands failed:\n- " + "\n- ".join(errors))
    # Thumbs-up each processed command comment so the owner sees decide ran.
    reviewflow.ack_command_comments(comments, reviewer)
    if len(set(approved) | set(rejected)) >= len(entries):
        reviewflow.post_comment(
            issue_number,
            f"All {len(entries)} papers decided: {len(approved)} approved, "
            f"{len(rejected)} rejected. Closing.",
        )
        reviewflow.close_issue(issue_number)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-7s %(message)s")
    parser = argparse.ArgumentParser(description="Daily paper pipeline")
    parser.add_argument("command", choices=["crawl", "decide", "backfill"])
    parser.add_argument("--issue", type=int, help="review issue number (decide)")
    parser.add_argument("--since", help="crawl: harvest-cursor override (YYYY-MM-DD)")
    parser.add_argument("--from", dest="from_date", help="backfill start date (YYYY-MM-DD)")
    parser.add_argument("--to", dest="to_date", help="backfill end date (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true",
                        help="crawl/backfill: print instead of creating issues")
    args = parser.parse_args()
    if args.command == "crawl":
        crawl(since=args.since, dry_run=args.dry_run)
    elif args.command == "backfill":
        if not (args.from_date and args.to_date):
            parser.error("backfill requires --from and --to")
        backfill(args.from_date, args.to_date, dry_run=args.dry_run)
    else:
        if not args.issue:
            parser.error("decide requires --issue")
        decide(args.issue)


if __name__ == "__main__":
    main()
