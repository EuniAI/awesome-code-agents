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
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

# ── Bootstrap ─────────────────────────────────────────────────────────────────
_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT))
load_dotenv(_REPO_ROOT / "automation" / ".env", override=False)
load_dotenv(_REPO_ROOT / ".env", override=False)

_LOG_FORMAT = "%(asctime)s %(levelname)-8s %(name)s — %(message)s"
_LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"
_LOG_DIR = _REPO_ROOT / "automation" / "logs"

logging.basicConfig(level=logging.INFO, format=_LOG_FORMAT, datefmt=_LOG_DATEFMT)
logger = logging.getLogger("main")


def _attach_file_logging(mode: str) -> None:
    """Add a size-capped rotating file handler for this run's mode.

    Logs are local-only (gitignored). Rotation keeps the last few runs while
    bounding disk usage — the durable state lives in state/processed.json, not here.
    """
    _LOG_DIR.mkdir(parents=True, exist_ok=True)
    handler = RotatingFileHandler(
        _LOG_DIR / f"{mode}.log",
        maxBytes=5 * 1024 * 1024,  # 5 MB per file
        backupCount=3,             # keep 3 rotations (~20 MB max per mode)
        encoding="utf-8",
    )
    handler.setFormatter(logging.Formatter(_LOG_FORMAT, datefmt=_LOG_DATEFMT))
    logging.getLogger().addHandler(handler)

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

    # Dedup 1: filter already processed
    new_papers = [p for p in all_papers if p.get("arxiv_id") not in processed_set]

    # Dedup 2: within this batch, keep first occurrence by arxiv_id
    # (arXiv crawl and inbox may contain the same paper)
    seen: dict[str, bool] = {}
    deduped = []
    for p in new_papers:
        aid = p.get("arxiv_id", "")
        if aid and aid not in seen:
            seen[aid] = True
            deduped.append(p)
    new_papers = deduped

    # ── 3b. Add papers pending retry (LLM failed last time) ─────────────────
    retry_ids = state_mgr.get_retry_ids(state)
    if retry_ids:
        logger.info("=== Retrying %d previously failed classification(s) ===", len(retry_ids))
        already = {p["arxiv_id"] for p in new_papers}
        from automation.crawler.arxiv import fetch_single_paper
        for aid in retry_ids:
            if aid not in already:
                p = fetch_single_paper(aid)
                if p:
                    new_papers.append(p)
                    already.add(aid)

    logger.info("After dedup: %d new papers to process", len(new_papers))

    if not new_papers:
        logger.info("Nothing new to process today — running historical backfill instead.")
        _run_incremental_backfill(cfg, state, owner, repo)
        return

    # ── 4. Enrich ───────────────────────────────────────────────────────────
    logger.info("=== Step 3: Enriching %d papers ===", len(new_papers))
    meta_enricher.enrich_papers(new_papers)

    # ── 5. Classify ─────────────────────────────────────────────────────────
    logger.info("=== Step 4: Classifying with LLM ===")
    learned_rules = state_mgr.maybe_refresh_learned_rules(state)
    relevant, failed_ids = classify_papers(
        new_papers,
        categories=cfg["categories"],
        tags=cfg["tags"],
        temperature=cfg.get("llm", {}).get("temperature", 0.1),
        learned_rules=learned_rules,
    )
    logger.info("Relevant papers: %d / %d (failed: %d)", len(relevant), len(new_papers), len(failed_ids))

    # Mark successfully classified papers as processed (failed ones stay out)
    succeeded_ids = [p["arxiv_id"] for p in new_papers if p.get("arxiv_id") not in failed_ids]
    state_mgr.mark_processed(state, succeeded_ids)

    # Track failures — give up after MAX_RETRIES, mark as processed to stop retrying
    if failed_ids:
        _, give_up_ids = state_mgr.add_failed_classifications(state, failed_ids)
        if give_up_ids:
            state_mgr.mark_processed(state, give_up_ids)
    state_mgr.save(state)

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

    # ── 7. Incremental historical backfill ──────────────────────────────────
    _run_incremental_backfill(cfg, state, owner, repo)


def _run_incremental_backfill(cfg, state, owner: str, repo: str) -> None:
    """
    Each daily run, advance the historical backfill cursor by CHUNK_DAYS.
    Backfill range: backfill_cursor → min(cursor + CHUNK_DAYS, yesterday).
    Stops automatically once the cursor reaches today.
    """
    from automation.crawler.arxiv import fetch_date_range
    from automation.enricher import metadata as meta_enricher
    from automation.classifier.llm import classify_papers
    from automation.review.create_issues import create_review_issues

    CHUNK_DAYS = 1  # days of history to process per daily run

    cursor_str = state.get("backfill_cursor")
    if cursor_str is None:
        logger.info("No historical backfill configured (backfill_cursor not set).")
        return

    cursor = date.fromisoformat(cursor_str)
    today  = date.today()

    if cursor >= today:
        logger.info("Historical backfill complete — cursor has reached today.")
        state["backfill_cursor"] = None
        state_mgr.save(state)
        return

    chunk_end = min(cursor + timedelta(days=CHUNK_DAYS - 1), today - timedelta(days=1))
    logger.info("=== Historical backfill: %s → %s ===", cursor, chunk_end)

    papers = fetch_date_range(
        cursor, chunk_end,
        cfg["arxiv"]["categories"],
        cfg["arxiv"]["keywords"],
        cfg["arxiv"]["max_results_per_category"],
    )

    processed_set = set(state["processed_ids"]) | set(state["rejected_ids"])
    new_papers = [p for p in papers if p.get("arxiv_id") not in processed_set]
    logger.info("Backfill new papers: %d", len(new_papers))

    if new_papers:
        meta_enricher.enrich_papers(new_papers)
        relevant, failed_ids = classify_papers(
            new_papers,
            categories=cfg["categories"],
            tags=cfg["tags"],
        )
        # Mark successfully classified as processed; failed ones stay out for retry
        succeeded_ids = [p["arxiv_id"] for p in new_papers if p.get("arxiv_id") not in failed_ids]
        state_mgr.mark_processed(state, succeeded_ids)
        if failed_ids:
            _, give_up_ids = state_mgr.add_failed_classifications(state, failed_ids)
            if give_up_ids:
                state_mgr.mark_processed(state, give_up_ids)

        if relevant:
            batch_label = f"backfill:{cursor}..{chunk_end}"
            new_issues = create_review_issues(relevant, owner, repo, batch_date=batch_label)
            for issue_meta in new_issues:
                state_mgr.add_pending_issue(state, issue_meta)
            logger.info("Backfill created %d review issue(s).", len(new_issues))

    # Advance cursor
    state["backfill_cursor"] = str(chunk_end + timedelta(days=1))
    state_mgr.save(state)
    logger.info("Backfill cursor advanced to %s", state["backfill_cursor"])


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
    approved_papers, rejected_ids, rejected_with_reasons, still_pending = poll_all_pending(
        pending, owner, repo, reviewer
    )

    state_mgr.update_pending_issues(state, still_pending)

    # Persist rejected IDs so they are never re-surfaced
    if rejected_ids:
        state_mgr.mark_rejected(state, rejected_ids)
        logger.info("Blacklisted %d rejected paper(s)", len(rejected_ids))

    # Accumulate reject reasons for classifier learning
    if rejected_with_reasons:
        state_mgr.add_reject_feedback(state, rejected_with_reasons)
        logger.info("Recorded %d reject reason(s) for classifier learning", len(rejected_with_reasons))

    if not approved_papers:
        state_mgr.save(state)
        logger.info("No approvals found yet.")
        return

    logger.info("=== Writing %d approved paper(s) to YAML ===", len(approved_papers))
    data_dir = _REPO_ROOT / "data"
    written, duplicate_ids = append_papers(approved_papers, data_dir)

    # Papers detected as duplicates by yaml_writer were manually added before
    # the pipeline started and have no arxiv_id in processed_ids yet.
    # Mark them now so the pipeline never re-processes them.
    if duplicate_ids:
        state_mgr.mark_processed(state, duplicate_ids)
        logger.info("Marked %d duplicate arxiv_id(s) as processed", len(duplicate_ids))

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

    meta_enricher.enrich_papers(new_papers)

    relevant = classify_papers(
        new_papers,
        categories=cfg["categories"],
        tags=cfg["tags"],
    )

    state_mgr.mark_processed(state, [p["arxiv_id"] for p in new_papers])
    state_mgr.save(state)

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
    _attach_file_logging(args.mode)

    try:
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
    except Exception:
        # Land uncaught crashes in the rotating file too, so cron can redirect
        # to /dev/null without losing tracebacks.
        logger.exception("Pipeline run failed (mode=%s)", args.mode)
        raise


if __name__ == "__main__":
    main()
