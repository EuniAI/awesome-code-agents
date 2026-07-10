"""
arXiv crawler — fetches papers by category and date, applies keyword pre-filter.

Usage (standalone test):
    python -m automation.crawler.arxiv --date 2025-05-28
"""

from __future__ import annotations

import logging
import re
import time
from datetime import date, timedelta
from typing import Any

import arxiv

logger = logging.getLogger(__name__)

# arXiv API allows ~1 req / 3s without getting rate-limited
_REQUEST_DELAY = 3.0


def _arxiv_id(result: arxiv.Result) -> str:
    """Extract bare arXiv ID (e.g. '2501.12345') from a Result."""
    return result.entry_id.split("/abs/")[-1].split("v")[0]


def _paper_url(result: arxiv.Result) -> str:
    return f"https://arxiv.org/abs/{_arxiv_id(result)}"


def _matches_keywords(result: arxiv.Result, keywords: list[str]) -> bool:
    """Return True if the title or abstract contains ANY keyword (case-insensitive)."""
    haystack = (result.title + " " + result.summary).lower()
    return any(kw.lower() in haystack for kw in keywords)


def fetch_papers(
    target_date: date,
    categories: list[str],
    keywords: list[str],
    max_results_per_category: int = 200,
) -> list[dict[str, Any]]:
    """
    Fetch arXiv papers submitted on *target_date* from each category,
    returning only those that match at least one keyword.

    Returns a list of normalised paper dicts (no GitHub/venue enrichment yet).
    """
    client = arxiv.Client(num_retries=3, delay_seconds=_REQUEST_DELAY)

    # arXiv date format for submittedDate filter
    date_str = target_date.strftime("%Y%m%d")
    next_date_str = (target_date + timedelta(days=1)).strftime("%Y%m%d")

    seen_ids: set[str] = set()
    papers: list[dict[str, Any]] = []

    for cat in categories:
        query = (
            f"cat:{cat} AND submittedDate:[{date_str}0000 TO {next_date_str}0000]"
        )
        logger.info("Querying arXiv: %s (max %d)", query, max_results_per_category)

        search = arxiv.Search(
            query=query,
            max_results=max_results_per_category,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        try:
            results = list(client.results(search))
        except Exception as exc:
            logger.warning("arXiv query failed for %s: %s", cat, exc)
            time.sleep(_REQUEST_DELAY)
            continue

        logger.info("  Got %d results from %s", len(results), cat)

        for r in results:
            arxiv_id = _arxiv_id(r)
            if arxiv_id in seen_ids:
                continue
            if not _matches_keywords(r, keywords):
                continue
            seen_ids.add(arxiv_id)

            authors = [str(a) for a in r.authors]
            papers.append({
                "arxiv_id":   arxiv_id,
                "title":      r.title.strip(),
                "authors":    authors,
                "abstract":   r.summary.strip().replace("\n", " "),
                "submitted":  r.published.strftime("%Y-%m-%d") if r.published else str(target_date),
                "categories": r.categories,
                "links": {
                    "paper":   _paper_url(r),
                    "github":  "",   # filled by enricher
                    "website": "",
                },
                "venue":   "",       # filled by enricher / classifier
                "summary": "",       # filled by classifier
                "tags":    [],       # filled by classifier
                "source":  "arxiv",
            })

        time.sleep(_REQUEST_DELAY)

    logger.info("Crawler found %d unique relevant papers for %s", len(papers), target_date)
    return papers


def fetch_date_range(
    start_date: date,
    end_date: date,
    categories: list[str],
    keywords: list[str],
    max_results_per_category: int = 200,
) -> list[dict[str, Any]]:
    """Fetch papers for each day in [start_date, end_date] inclusive."""
    all_papers: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    current = start_date
    while current <= end_date:
        day_papers = fetch_papers(current, categories, keywords, max_results_per_category)
        for p in day_papers:
            if p["arxiv_id"] not in seen_ids:
                seen_ids.add(p["arxiv_id"])
                all_papers.append(p)
        current += timedelta(days=1)

    return all_papers


def fetch_single_paper(arxiv_id: str) -> dict[str, Any] | None:
    """
    Fetch a single paper by arXiv ID (used by inbox processor).
    arxiv_id can be bare '2501.12345' or full URL.
    """
    # Normalise URL to bare ID
    arxiv_id = re.sub(r"https?://arxiv\.org/(abs|pdf)/", "", arxiv_id)
    arxiv_id = arxiv_id.split("v")[0].strip().rstrip("/")

    client = arxiv.Client(num_retries=3, delay_seconds=_REQUEST_DELAY)
    search = arxiv.Search(id_list=[arxiv_id])

    try:
        results = list(client.results(search))
    except Exception as exc:
        logger.warning("Failed to fetch arXiv paper %s: %s", arxiv_id, exc)
        return None

    if not results:
        logger.warning("arXiv paper not found: %s", arxiv_id)
        return None

    r = results[0]
    authors = [str(a) for a in r.authors]
    return {
        "arxiv_id":   arxiv_id,
        "title":      r.title.strip(),
        "authors":    authors,
        "abstract":   r.summary.strip().replace("\n", " "),
        "submitted":  r.published.strftime("%Y-%m-%d") if r.published else "",
        "categories": r.categories,
        "links": {
            "paper":   f"https://arxiv.org/abs/{arxiv_id}",
            "github":  "",
            "website": "",
        },
        "venue":   "",
        "summary": "",
        "tags":    [],
        "source":  "inbox",
    }


# ── CLI quick-test ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse, json
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=str(date.today()), help="YYYY-MM-DD")
    args = parser.parse_args()

    from automation.config_loader import load_config
    cfg = load_config()
    target = date.fromisoformat(args.date)
    papers = fetch_papers(
        target,
        cfg["arxiv"]["categories"],
        cfg["arxiv"]["keywords"],
        cfg["arxiv"]["max_results_per_category"],
    )
    print(json.dumps(papers, indent=2, ensure_ascii=False))
