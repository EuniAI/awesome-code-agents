"""
Appends approved papers to the appropriate data/papers_<category>.yaml files.

YAML format (new fields added, old entries untouched):
  - title: "..."
    authors: "..."          # comma-separated string
    venue: "..."
    summary: "..."          # 2-sentence summary (not rendered yet)
    tags: []                # list of tag keys
    links:
      paper: "..."
      github: "..."
      website: ""
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)


def _authors_to_string(authors: list[str] | str) -> str:
    if isinstance(authors, list):
        return ", ".join(authors)
    return str(authors)


def _build_yaml_entry(paper: dict[str, Any]) -> dict[str, Any]:
    """Convert a pipeline paper dict to the canonical YAML entry format."""
    links = paper.get("links", {}) or {}
    entry: dict[str, Any] = {
        "title":   paper.get("title", "").strip(),
        "authors": _authors_to_string(paper.get("authors", "")),
        "venue":   paper.get("venue", "").strip(),
    }
    # Only include summary if non-empty
    summary = paper.get("summary", "").strip()
    if summary:
        entry["summary"] = summary
    # Only include tags if non-empty
    tags = [t for t in (paper.get("tags") or []) if t]
    if tags:
        entry["tags"] = tags

    entry["links"] = {
        "paper":   links.get("paper", "").strip(),
        "github":  links.get("github", "").strip(),
        "website": links.get("website", "").strip(),
    }
    return entry


def append_paper(paper: dict[str, Any], data_dir: Path) -> tuple[bool, str]:
    """
    Append one paper to the appropriate YAML file.
    Returns (written, duplicate_arxiv_id):
      - written=True  → paper was added
      - written=False → skipped; duplicate_arxiv_id is the paper's arxiv_id
        so the caller can add it to processed_ids and avoid re-processing.
    """
    arxiv_id = paper.get("arxiv_id", "")
    category = paper.get("category", "")
    if not category:
        logger.warning("Paper has no category, skipping: %s", paper.get("title"))
        return False, arxiv_id

    yaml_path = data_dir / f"papers_{category}.yaml"
    if not yaml_path.exists():
        logger.warning("Category file not found: %s — skipping", yaml_path)
        return False, arxiv_id

    # Load existing entries
    existing_text = yaml_path.read_text(encoding="utf-8")
    try:
        existing: list[dict] = yaml.safe_load(existing_text) or []
    except yaml.YAMLError as exc:
        logger.error("YAML parse error in %s: %s", yaml_path, exc)
        return False, arxiv_id

    # Dedup by paper URL or title
    paper_url = paper.get("links", {}).get("paper", "")
    title     = paper.get("title", "")
    for e in existing:
        e_url   = (e.get("links") or {}).get("paper", "")
        e_title = e.get("title", "")
        if (paper_url and e_url and e_url == paper_url) or (title and e_title == title):
            logger.info("Already exists in %s, skipping: %s", yaml_path.name, title[:60])
            return False, arxiv_id   # return arxiv_id so caller marks it processed

    new_entry = _build_yaml_entry(paper)

    # Prepend to the top of the list (newest first, matching existing convention)
    updated = [new_entry] + existing

    # Serialise with nice formatting
    new_text = yaml.dump(
        updated,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    )

    yaml_path.write_text(new_text, encoding="utf-8")
    logger.info("Written to %s: %s", yaml_path.name, title[:60])
    return True, ""


def append_papers(papers: list[dict[str, Any]], data_dir: Path) -> tuple[int, list[str]]:
    """
    Append multiple papers.
    Returns (written_count, duplicate_arxiv_ids) so callers can mark
    duplicates in processed_ids and avoid re-processing them next time.
    """
    count = 0
    duplicate_ids: list[str] = []
    for paper in papers:
        written, dup_id = append_paper(paper, data_dir)
        if written:
            count += 1
        elif dup_id:
            duplicate_ids.append(dup_id)
    return count, duplicate_ids
