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


def append_paper(paper: dict[str, Any], data_dir: Path) -> bool:
    """
    Append one paper to the appropriate YAML file.
    Returns True if written, False if skipped (already exists).
    """
    category = paper.get("category", "")
    if not category:
        logger.warning("Paper has no category, skipping: %s", paper.get("title"))
        return False

    yaml_path = data_dir / f"papers_{category}.yaml"
    if not yaml_path.exists():
        logger.warning("Category file not found: %s — skipping", yaml_path)
        return False

    # Load existing entries
    existing_text = yaml_path.read_text(encoding="utf-8")
    try:
        existing: list[dict] = yaml.safe_load(existing_text) or []
    except yaml.YAMLError as exc:
        logger.error("YAML parse error in %s: %s", yaml_path, exc)
        return False

    # Dedup by paper URL or title
    paper_url = paper.get("links", {}).get("paper", "")
    title     = paper.get("title", "")
    for e in existing:
        e_url   = (e.get("links") or {}).get("paper", "")
        e_title = e.get("title", "")
        if (paper_url and e_url and e_url == paper_url) or (title and e_title == title):
            logger.info("Already exists in %s, skipping: %s", yaml_path.name, title[:60])
            return False

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
    return True


def append_papers(papers: list[dict[str, Any]], data_dir: Path) -> int:
    """Append multiple papers. Returns count of successfully written papers."""
    count = 0
    for paper in papers:
        if append_paper(paper, data_dir):
            count += 1
    return count
