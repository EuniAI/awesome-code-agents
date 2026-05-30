#!/usr/bin/env python3
"""
Migrate papers from deprecated categories (benchmarks, surveys, empirical_studies)
into appropriate functional categories, using the LLM classifier.
Skips papers already present in any other category file.
"""

from __future__ import annotations
import re
import sys
import logging
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO))

from dotenv import load_dotenv
load_dotenv(_REPO / "automation" / ".env")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)

import yaml
from automation.config_loader import load_config
from automation.classifier.llm import classify_paper
from automation.crawler.arxiv import fetch_single_paper
from automation.finalizer.yaml_writer import append_paper

DEPRECATED = ["benchmarks", "surveys", "empirical_studies"]
_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.IGNORECASE)

LEGACY_TAG = {
    "benchmarks":       "benchmark",
    "surveys":          "survey",
    "empirical_studies":"empirical",
}


def load_existing(data_dir: Path) -> tuple[set[str], set[str]]:
    """All paper URLs and titles already recorded in non-deprecated files."""
    urls, titles = set(), set()
    for f in data_dir.glob("papers_*.yaml"):
        if any(f.name == f"papers_{d}.yaml" for d in DEPRECATED):
            continue   # don't count deprecated files as "existing"
        try:
            for e in (yaml.safe_load(f.read_text()) or []):
                if isinstance(e, dict):
                    u = (e.get("links") or {}).get("paper", "").strip()
                    t = e.get("title", "").strip()
                    if u: urls.add(u)
                    if t: titles.add(t)
        except Exception:
            pass
    return urls, titles


def fetch_abstract(paper: dict) -> str:
    """Try to get abstract via arXiv API; fall back to title."""
    url = (paper.get("links") or {}).get("paper", "")
    m = _ARXIV_ID_RE.search(url)
    if m:
        fetched = fetch_single_paper(m.group(1))
        if fetched and fetched.get("abstract"):
            return fetched["abstract"]
    return paper.get("title", "")


def main():
    cfg      = load_config()
    data_dir = _REPO / "data"
    existing_urls, existing_titles = load_existing(data_dir)

    logger.info("Non-deprecated existing papers: %d urls, %d titles",
                len(existing_urls), len(existing_titles))

    migrated = skipped_dup = skipped_irrel = 0

    for cat in DEPRECATED:
        src = data_dir / f"papers_{cat}.yaml"
        if not src.exists():
            continue
        papers = yaml.safe_load(src.read_text()) or []
        logger.info("\n=== %s (%d papers) ===", cat, len(papers))

        for paper in papers:
            title = paper.get("title", "").strip()
            url   = (paper.get("links") or {}).get("paper", "").strip()

            # Dedup against non-deprecated files
            if (url and url in existing_urls) or (title and title in existing_titles):
                logger.info("  SKIP dup: %s", title[:70])
                skipped_dup += 1
                continue

            # Fetch abstract for better classification
            logger.info("  Fetching: %s", title[:70])
            abstract = fetch_abstract(paper)

            result = classify_paper(
                {"title": title, "abstract": abstract, "arxiv_id": ""},
                categories=cfg["categories"],
                tags=cfg["tags"],
            )

            if not result.get("relevant") or not result.get("category"):
                logger.info("  SKIP not relevant: %s", title[:70])
                skipped_irrel += 1
                continue

            paper["category"] = result["category"]
            # Merge tags: original + classifier + legacy tag, deduped
            orig_tags   = paper.get("tags") or []
            new_tags    = result.get("tags") or []
            legacy      = LEGACY_TAG.get(cat, "")
            paper["tags"] = list(dict.fromkeys(
                [t for t in orig_tags + new_tags + ([legacy] if legacy else []) if t]
            ))

            if append_paper(paper, data_dir):
                existing_urls.add(url)
                existing_titles.add(title)
                migrated += 1
                logger.info("  ✓ → %s %s", result["category"], paper["tags"])
            else:
                skipped_dup += 1
                logger.info("  SKIP append dedup: %s", title[:70])

    logger.info("\n=== Result: migrated=%d  dup=%d  irrelevant=%d ===",
                migrated, skipped_dup, skipped_irrel)


if __name__ == "__main__":
    main()
