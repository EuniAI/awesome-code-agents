"""
Papers with Code enricher — looks up GitHub repository links by arXiv ID.

API docs: https://paperswithcode.com/api/v1/docs/
Rate limit: generous for reasonable usage, no auth required.
"""

from __future__ import annotations

import logging
import time
from typing import Any

import requests

logger = logging.getLogger(__name__)

_BASE_URL = "https://paperswithcode.com/api/v1"
_TIMEOUT = 10
_DELAY = 1.0   # seconds between requests


def _get(url: str, params: dict | None = None) -> dict | None:
    try:
        resp = requests.get(url, params=params, timeout=_TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as exc:
        logger.debug("PapersWithCode request failed: %s", exc)
        return None


def find_github_url(arxiv_id: str) -> str:
    """
    Return the best GitHub repo URL for a paper, or '' if not found.

    Strategy:
    1. Search PapersWithCode by arXiv ID
    2. Among returned repos, prefer the one with the most stars
    """
    data = _get(f"{_BASE_URL}/papers/", params={"arxiv_id": arxiv_id})
    time.sleep(_DELAY)

    if not data or not data.get("results"):
        return ""

    paper_id = data["results"][0].get("id", "")
    if not paper_id:
        return ""

    # Get repos linked to this paper
    repos_data = _get(f"{_BASE_URL}/papers/{paper_id}/repositories/")
    time.sleep(_DELAY)

    if not repos_data or not repos_data.get("results"):
        return ""

    repos = repos_data["results"]

    # Filter to GitHub URLs only, sort by stars descending
    github_repos = [
        r for r in repos
        if r.get("url", "").startswith("https://github.com/")
    ]
    if not github_repos:
        return ""

    github_repos.sort(key=lambda r: r.get("stars", 0) or 0, reverse=True)
    return github_repos[0]["url"]


def enrich_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Fill in links.github for each paper that doesn't already have one.
    Mutates in place and returns the list.
    """
    for p in papers:
        if p.get("links", {}).get("github"):
            continue   # already filled
        arxiv_id = p.get("arxiv_id", "")
        if not arxiv_id:
            continue
        url = find_github_url(arxiv_id)
        if url:
            p["links"]["github"] = url
            logger.info("  PwC: %s → %s", arxiv_id, url)
        else:
            logger.debug("  PwC: no repo found for %s", arxiv_id)
    return papers
