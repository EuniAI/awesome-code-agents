#!/usr/bin/env python3
"""
Main orchestrator for the awesome-code-agents automation pipeline.

Modes:
  --mode daily      Crawl arXiv + process inbox → classify → create GitHub Issues
  --mode finalize   Poll pending Issues for /approve → write YAML → git push
  --mode setup      Create the inbox GitHub Issue and persist its number to config.yaml
  --mode backfill   Crawl a specific date range (use with --from and --to)

Usage:
  python automation/main.py --mode daily
  python automation/main.py --mode finalize
  python automation/main.py --mode setup
  python automation/main.py --mode backfill --from 2025-05-20 --to 2025-05-25

Cron suggestions:
  0 9 * * *   cd /path/to/repo && python automation/main.py --mode daily
  0 * * * *   cd /path/to/repo && python automation/main.py --mode finalize
"""

from __future__ import annotations

import argparse
import logging
import sys
from datetime import date, timedelta
from pathlib import Path

from dotenv import load_dotenv

# ── Bootstrap ─────────────────────────────────────────────────────────────────
_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT))
load_dotenv(_REPO_ROOT / "automation" / ".env", override=False)
load_dotenv(_REPO_ROOT / ".env", override=False)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("main")

from automation.config_loader import load_config, save_config
import automation.state_manager as state_mgr

# ── Mode: setup ───────────────────────────────────────────────────────────────

def run_setup() -> None:
    """Create the pinned inbox GitHub Issue if it doesn't exist yet."""
    from automation.review import github as gh

    cfg    = load_config()
    owner  = cfg["repo"]["owner"]
    repo   = cfg["repo"]["name"]

    if cfg["inbox"].get("issue_number"):
        logger.info("Inbox issue already exists: #%d", cfg["inbox"]["issue_number"])
        logger.info("  https://github.com/%s/%s/issues/%d", owner, repo, cfg["inbox"]["issue_number"])
        return

    logger.info("Creating inbox issue on %s/%s…", owner, repo)
    body = (
        "## 📥 Paper Inbox\n\n"
        "Drop arXiv links here as comments — the automation pipeline will pick them up daily.\n\n"
        "**Format:** Just paste the arXiv URL anywhere in your comment, e.g.:\n"
        "```\n"
        "https://arxiv.org/abs/2501.12345\n"
        "```\n"
        "You can add multiple links per comment. "
        "A ✅ reaction will appear once the bot has processed your comment.\n\n"
        "---\n"
        "_This issue is managed by the automation pipeline. Do not close it._"
    )
    issue = gh.create_issue(owner, repo, "📥 Paper Inbox", body, labels=[])
    number = issue.get("number")
    logger.info("Created inbox issue #%d", number)

    # Persist to config.yaml
    cfg["inbox"]["issue_number"] = number
    save_config(cfg)
    logger.info("Saved inbox issue number to config.yaml")


# ── Mode: daily ───────────────────────────────────────────────────────────────

def run_daily() -> None:
    """Full pipeline: crawl → enrich → classify → create review Issues."""
    from automation.crawler.arxiv import fetch_papers, fetch_date_range
    from automation.enricher import papers_with_code as pwc
    from automation.enricher import metadata as meta_enricher
    from automation.classifier.llm import classify_papers
    from automation.review.create_issues import create_review_issues
    from automation.inbox.reader import read_inbox

    cfg    = load_config()
    owner  = cfg["repo"]["owner"]
    repo   = cfg["repo"]["name"]
    arxiv_cfg = cfg["arxiv"]
    state  = state_mgr.load()

    today       = date.today()
    backfill    = int(arxiv_cfg.get("backfill_days", 3))
    categories  = arxiv_cfg["categories"]
    keywords    = arxiv_cfg["keywords"]
    max_results = int(arxiv_cfg.get("max_results_per_category", 200))

    # ── 1. Crawl arXiv ──────────────────────────────────────────────────────
    logger.info("=== Step 1: arXiv crawl (today + %d backfill days) ===", backfill)
    start_date = today - timedelta(days=backfill)
    raw_papers = fetch_date_range(start_date, today, categories, keywords, max_results)
    logger.info("Raw crawl: %d papers", len(raw_papers))

    # ── 2. Read inbox ───────────────────────────────────────────────────────
    inbox_number = cfg["inbox"].get("issue_number")
    if inbox_number:
        logger.info("=== Step 2: Reading inbox issue #%d ===", inbox_number)
        processed_set = set(state["processed_ids"]) | set(state["rejected_ids"])
        inbox_papers = read_inbox(owner, repo, inbox_number, processed_set)
        logger.info("Inbox: %d new papers", len(inbox_papers))
    else:
        logger.warning("No inbox issue configured — skipping inbox. Run --mode=setup first.")
        inbox_papers = []

    # ── 3. Merge + deduplicate ──────────────────────────────────────────────
    all_papers = raw_papers + inbox_papers
    processed_set = set(state["processed_ids"]) | set(state["rejected_ids"])
    new_papers = [p for p in all_papers if p.get("arxiv_id") not in processed_set]
    logger.info("After dedup: %d new papers to process", len(new_papers))

    if not new_papers:
        logger.info("Nothing new to process today.")
        return

    # Mark as processed immediately so re-runs don't double-process
    state_mgr.mark_processed(state, [p["arxiv_id"] for p in new_papers])
    state_mgr.save(state)

    # ── 4. Enrich ───────────────────────────────────────────────────────────
    logger.info("=== Step 3: Enriching %d papers ===", len(new_papers))
    pwc.enrich_papers(new_papers)
    meta_enricher.enrich_papers(new_papers)

    # ── 5. Classify ─────────────────────────────────────────────────────────
    logger.info("=== Step 4: Classifying with LLM ===")
    relevant = classify_papers(
        new_papers,
        categories=cfg["categories"],
        tags=cfg["tags"],
        temperature=cfg.get("llm", {}).get("temperature", 0.1),
    )
    logger.info("Relevant papers: %d / %d", len(relevant), len(new_papers))

    if not relevant:
        logger.info("No relevant papers found.")
        return

    # ── 6. Create GitHub review Issues ──────────────────────────────────────
    logger.info("=== Step 5: Creating GitHub review Issues ===")
    new_issues = create_review_issues(
        relevant, owner, repo, batch_date=str(today)
    )

    for issue_meta in new_issues:
        state_mgr.add_pending_issue(state, issue_meta)

    state_mgr.save(state)
    logger.info("Daily run complete. Created %d review issue(s).", len(new_issues))


# ── Mode: finalize ────────────────────────────────────────────────────────────

def run_finalize() -> None:
    """Poll pending Issues for /approve commands, write YAML, push."""
    from automation.review.poll_approvals import poll_all_pending
    from automation.finalizer.yaml_writer import append_papers
    from automation.finalizer.git_push import render_and_push

    cfg   = load_config()
    owner = cfg["repo"]["owner"]
    repo  = cfg["repo"]["name"]
    reviewer = cfg["repo"]["reviewer"]
    state = state_mgr.load()

    pending = state.get("pending_issues", [])
    if not pending:
        logger.info("No pending issues to check.")
        return

    logger.info("=== Polling %d pending issue(s) ===", len(pending))
    approved_papers, still_pending = poll_all_pending(pending, owner, repo, reviewer)

    state_mgr.update_pending_issues(state, still_pending)

    if not approved_papers:
        state_mgr.save(state)
        logger.info("No approvals found yet.")
        return

    logger.info("=== Writing %d approved paper(s) to YAML ===", len(approved_papers))
    data_dir = _REPO_ROOT / "data"
    written = append_papers(approved_papers, data_dir)

    # Mark rejected IDs
    rejected = []
    for issue_meta in pending:
        # rejected_ids are present in poll result but we need to gather from all issues
        pass
    # (Rejection tracking happens inside poll_all_pending via state updates)

    state_mgr.save(state)

    if written > 0:
        commit_msg = (
            f"chore(bot): add {written} paper(s) from review pipeline\n\n"
            + "\n".join(f"- {p.get('title', p.get('arxiv_id', ''))[:80]}" for p in approved_papers[:10])
        )
        logger.info("=== Rendering and pushing ===")
        render_and_push(_REPO_ROOT, commit_msg)
    else:
        logger.info("No new papers written (all duplicates?)")


# ── Mode: backfill ────────────────────────────────────────────────────────────

def run_backfill(from_date: date, to_date: date) -> None:
    """Crawl a specific historical date range."""
    from automation.crawler.arxiv import fetch_date_range
    from automation.enricher import papers_with_code as pwc
    from automation.enricher import metadata as meta_enricher
    from automation.classifier.llm import classify_papers
    from automation.review.create_issues import create_review_issues

    cfg   = load_config()
    owner = cfg["repo"]["owner"]
    repo  = cfg["repo"]["name"]
    state = state_mgr.load()

    logger.info("=== Backfill: %s → %s ===", from_date, to_date)
    papers = fetch_date_range(
        from_date, to_date,
        cfg["arxiv"]["categories"],
        cfg["arxiv"]["keywords"],
        cfg["arxiv"]["max_results_per_category"],
    )

    processed_set = set(state["processed_ids"]) | set(state["rejected_ids"])
    new_papers = [p for p in papers if p.get("arxiv_id") not in processed_set]
    logger.info("New (unprocessed) papers: %d", len(new_papers))

    if not new_papers:
        logger.info("Nothing new in this date range.")
        return

    state_mgr.mark_processed(state, [p["arxiv_id"] for p in new_papers])
    state_mgr.save(state)

    pwc.enrich_papers(new_papers)
    meta_enricher.enrich_papers(new_papers)

    relevant = classify_papers(
        new_papers,
        categories=cfg["categories"],
        tags=cfg["tags"],
    )

    if relevant:
        new_issues = create_review_issues(
            relevant, owner, repo,
            batch_date=f"{from_date}..{to_date}",
        )
        for issue_meta in new_issues:
            state_mgr.add_pending_issue(state, issue_meta)
        state_mgr.save(state)
        logger.info("Backfill created %d review issue(s).", len(new_issues))


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Awesome Code Agents automation pipeline")
    parser.add_argument(
        "--mode",
        choices=["daily", "finalize", "setup", "backfill"],
        required=True,
        help="Pipeline mode",
    )
    parser.add_argument("--from", dest="from_date", help="Start date for backfill (YYYY-MM-DD)")
    parser.add_argument("--to",   dest="to_date",   help="End date for backfill (YYYY-MM-DD)")
    args = parser.parse_args()

    if args.mode == "setup":
        run_setup()
    elif args.mode == "daily":
        run_daily()
    elif args.mode == "finalize":
        run_finalize()
    elif args.mode == "backfill":
        if not args.from_date or not args.to_date:
            parser.error("--mode=backfill requires --from and --to")
        run_backfill(
            date.fromisoformat(args.from_date),
            date.fromisoformat(args.to_date),
        )


if __name__ == "__main__":
    main()
