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


# ── crawl ─────────────────────────────────────────────────────────────────────

def crawl(days_back: int | None = None, dry_run: bool = False) -> None:
    leaves = taxonomy.load().leaf_keys()
    known = storage.all_ids(leaves) | storage.load_seen() | reviewflow.pending_ids()

    candidates: list[Paper] = []
    for p in sources.crawl(days_back) + sources.read_inbox():
        if p.id not in known:
            known.add(p.id)  # also dedups crawl vs inbox within this run
            candidates.append(p)
    if not candidates:
        logger.info("nothing new today")
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
    skipped = failed = 0
    seen = storage.load_seen()
    for p, v in zip(candidates, verdicts):
        if v.failed:
            failed += 1  # not marked seen: retried on the next crawl
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

    note = f"Auto-skipped {skipped} out-of-scope; {failed} failed (retried next run)."
    if dry_run:  # a dry run must leave no trace in the pipeline state
        print(json.dumps(entries, indent=2, ensure_ascii=False))
        print(note)
        return
    storage.save_seen(seen)
    if entries:
        number = reviewflow.create_issue(entries, note=note)
        logger.info("review issue #%d: %d papers proposed", number, len(entries))
    else:
        logger.info("no relevant papers today (%s)", note)


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
    parser.add_argument("command", choices=["crawl", "decide"])
    parser.add_argument("--issue", type=int, help="review issue number (decide)")
    parser.add_argument("--days-back", type=int, default=None, help="crawl window override")
    parser.add_argument("--dry-run", action="store_true", help="crawl: print instead of creating an issue")
    args = parser.parse_args()
    if args.command == "crawl":
        crawl(days_back=args.days_back, dry_run=args.dry_run)
    else:
        if not args.issue:
            parser.error("decide requires --issue")
        decide(args.issue)


if __name__ == "__main__":
    main()
