"""
Inbox reader — reads user-submitted arXiv links from a pinned GitHub Issue.

Protocol:
  - User comments any text containing arXiv URLs on the inbox issue.
  - Deduplication is handled via the pipeline state (processed_ids).
  - For each unprocessed comment, extracts arXiv IDs, fetches paper metadata.
  - After processing, adds a 👍 (+1) reaction as a visual acknowledgement.
"""

from __future__ import annotations

import logging
import re
from typing import Any

from automation.review import github as gh
from automation.crawler.arxiv import fetch_single_paper

logger = logging.getLogger(__name__)

# Matches arxiv.org/abs/XXXX.XXXXX or arxiv.org/pdf/XXXX.XXXXX (with optional vN)
_ARXIV_URL_RE = re.compile(
    r"https?://arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?",
    re.IGNORECASE,
)
# Also match bare IDs like "2501.12345"
_ARXIV_ID_RE = re.compile(r"\b(\d{4}\.\d{4,5})\b")


def _extract_arxiv_ids(text: str) -> list[str]:
    ids: list[str] = []
    for m in _ARXIV_URL_RE.finditer(text):
        ids.append(m.group(1))
    # Only pick up bare IDs that aren't already captured
    found_urls = set(ids)
    for m in _ARXIV_ID_RE.finditer(text):
        if m.group(1) not in found_urls:
            ids.append(m.group(1))
    return list(dict.fromkeys(ids))   # deduplicate preserving order


def read_inbox(
    owner: str,
    repo: str,
    inbox_issue_number: int,
    processed_ids: set[str],
) -> list[dict[str, Any]]:
    """
    Fetch unprocessed papers from the inbox issue.

    processed_ids: set of arXiv IDs already in the pipeline (from state).
    Returns list of paper dicts (same format as crawler output).
    """
    comments = gh.get_issue_comments(owner, repo, inbox_issue_number)
    papers: list[dict[str, Any]] = []
    new_processed: list[str] = []

    for comment in comments:
        comment_id = comment["id"]
        body = comment.get("body", "")
        arxiv_ids = _extract_arxiv_ids(body)
        if not arxiv_ids:
            continue

        # Check if all IDs in this comment are already processed
        new_ids = [aid for aid in arxiv_ids if aid not in processed_ids]
        if not new_ids:
            continue

        # Fetch metadata for each new arXiv ID
        fetched_any = False
        for aid in new_ids:
            logger.info("Inbox: fetching %s", aid)
            paper = fetch_single_paper(aid)
            if paper:
                paper["source"] = "inbox"
                papers.append(paper)
                new_processed.append(aid)
                fetched_any = True
            else:
                logger.warning("Inbox: could not fetch %s", aid)

        # Mark comment as processed with ✅ reaction
        if fetched_any:
            try:
                gh.add_reaction(owner, repo, inbox_issue_number, comment_id, reaction="+1")
            except Exception as exc:
                logger.warning("Could not add reaction to comment %d: %s", comment_id, exc)

    logger.info("Inbox: fetched %d new papers from %d comments", len(papers), len(comments))
    return papers
