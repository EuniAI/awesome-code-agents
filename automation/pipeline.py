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


def classify_and_propose(candidates: list[Paper], dry_run: bool = False) -> None:
    """Shared tail of every intake path (daily crawl, inbox, backlog): classify,
    mark handled ids seen, and open chunked review issues (the pool). Unreviewed
    issues simply stay open; nothing is ever dropped."""
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
        entries.append({
            "paper": p.to_dict(),
            "category": v.category, "tags": v.tags,
            "summary": v.summary, "reason": v.reason,
        })

    note = f"Auto-skipped {skipped} out-of-scope; {len(failed_ids)} failed (retried next run)."
    if dry_run:  # a dry run must leave no trace in the pipeline state
        print(json.dumps(entries, indent=2, ensure_ascii=False))
        print(note)
        return
    storage.save_seen(seen)
    # Failures survive the crawl window: successfully classified ids leave the
    # retry list, fresh failures join it, and crawl() feeds the list back in.
    classified = {p.id for p, v in zip(candidates, verdicts) if not v.failed}
    storage.save_retry(sorted((set(storage.load_retry()) - classified) | set(failed_ids)))
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

def crawl(days_back: int | None = None, dry_run: bool = False) -> None:
    leaves = taxonomy.load().leaf_keys()
    known = storage.all_ids(leaves) | storage.load_seen() | reviewflow.pending_ids()

    retry_papers = list(sources.fetch_arxiv_papers(storage.load_retry()).values())
    candidates: list[Paper] = []
    for p in retry_papers + sources.crawl(days_back) + sources.read_inbox():
        if p.id not in known:
            known.add(p.id)  # also dedups retry vs crawl vs inbox within this run
            candidates.append(p)
    if candidates:
        classify_and_propose(candidates, dry_run=dry_run)
    else:
        logger.info("nothing new today")
    if not dry_run:
        # Thumbs-up inbox comments whose links are now all handled.
        sources.ack_inbox(storage.all_ids(leaves) | storage.load_seen() | reviewflow.pending_ids())


# ── backfill ──────────────────────────────────────────────────────────────────

def backfill(from_date: str, to_date: str, dry_run: bool = False) -> None:
    """Historical sweep of a date range into the pool; same intake tail as crawl.
    Useful for categories added after the fact (cs.RO/AR/OS/DC/DB were never
    crawled by the old pipeline). Sweep long ranges month by month."""
    leaves = taxonomy.load().leaf_keys()
    known = storage.all_ids(leaves) | storage.load_seen() | reviewflow.pending_ids()
    candidates = [p for p in sources.crawl_range(from_date, to_date) if p.id not in known]
    logger.info("backfill %s..%s: %d new candidates", from_date, to_date, len(candidates))
    classify_and_propose(candidates, dry_run=dry_run)


# ── decide ────────────────────────────────────────────────────────────────────

def _append_calibration(corrections: list[tuple[Paper, str, str]]) -> None:
    """Feed each category correction back to the classifier as an owner example."""
    data = json.loads(CALIBRATION_PATH.read_text(encoding="utf-8"))
    existing = {e["id"] for e in data["examples"]}
    added = 0
    for p, proposed, corrected in corrections:
        if p.id in existing:
            continue
        data["examples"].append({
            "id": p.id, "title": p.title, "category": corrected, "tags": p.tags,
            "why": (f"Owner correction during review: the classifier proposed "
                    f"`{proposed}`; the owner filed it under `{corrected}`."),
        })
        added += 1
    if added:
        CALIBRATION_PATH.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        logger.info("calibration.json: %d owner examples appended", added)


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
    corrections: list[tuple[Paper, str, str]] = []

    for idx in sorted(decisions):
        action, overrides = decisions[idx]
        e = entries[idx - 1]
        if action == "reject":
            rejected.append(idx)
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
            corrections.append((p, e["category"], overrides["category"]))

    if corrections:
        _append_calibration(corrections)
    if added_new:
        render.main()
        badges.refresh()
    logger.info("issue #%d: %d approved (%d newly added), %d rejected, %d errors",
                issue_number, len(approved), added_new, len(rejected), len(errors))

    if errors:
        reviewflow.post_comment(issue_number, "Some commands failed:\n- " + "\n- ".join(errors))
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
    parser.add_argument("--days-back", type=int, default=None, help="crawl window override")
    parser.add_argument("--from", dest="from_date", help="backfill start date (YYYY-MM-DD)")
    parser.add_argument("--to", dest="to_date", help="backfill end date (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true",
                        help="crawl/backfill: print instead of creating issues")
    args = parser.parse_args()
    if args.command == "crawl":
        crawl(days_back=args.days_back, dry_run=args.dry_run)
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
