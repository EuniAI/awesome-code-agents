"""
The one schema for a paper record. Every stage of the pipeline passes Paper
objects; YAML files store their dict form. Nothing else defines these fields.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)


@dataclass
class Classification:
    """The classifier's verdict for one paper."""
    relevant: bool
    category: str = ""            # a taxonomy leaf key; empty when not relevant / failed
    tags: list[str] = field(default_factory=list)
    summary: str = ""
    reason: str = ""              # one-line why (kept for review issues and debugging)
    failed: bool = False          # classification could not be obtained/validated


@dataclass
class Paper:
    id: str                      # arxiv id when available, else the paper URL
    title: str
    authors: list[str] = field(default_factory=list)
    venue: str = ""
    published: str = ""          # first-publication date, YYYY-MM-DD (drives curation)
    links: dict[str, str] = field(default_factory=dict)   # paper / github / website
    category: str = ""           # a taxonomy leaf key
    tags: list[str] = field(default_factory=list)          # paper_type + released_artifact values
    summary: str = ""

    # ── identity ──────────────────────────────────────────────────────────────

    @staticmethod
    def id_from_url(url: str) -> str:
        """Stable identity: the arxiv id if the URL is an arxiv link, else the URL."""
        m = _ARXIV_ID_RE.search(url or "")
        return m.group(1) if m else (url or "").strip()

    # ── (de)serialization ─────────────────────────────────────────────────────

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Paper":
        links = {k: (v or "").strip() for k, v in (d.get("links") or {}).items()}
        authors = d.get("authors") or []
        if isinstance(authors, str):
            authors = [a.strip() for a in authors.split(",") if a.strip()]
        tags = d.get("tags") or []
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]
        pid = (d.get("id") or "").strip() or cls.id_from_url(links.get("paper", ""))
        return cls(
            id=pid,
            title=(d.get("title") or "").strip(),
            authors=authors,
            venue=(d.get("venue") or "").strip(),
            published=(d.get("published") or "").strip(),
            links=links,
            category=(d.get("category") or "").strip(),
            tags=tags,
            summary=(d.get("summary") or "").strip(),
        )

    def to_dict(self) -> dict[str, Any]:
        """Stable field order; empty optionals omitted to keep YAML lean."""
        d: dict[str, Any] = {
            "id": self.id,
            "title": self.title,
            "authors": self.authors,
            "venue": self.venue,
            "category": self.category,
        }
        if self.published:
            d["published"] = self.published
        if self.tags:
            d["tags"] = self.tags
        if self.summary:
            d["summary"] = self.summary
        d["links"] = {
            "paper": self.links.get("paper", ""),
            "github": self.links.get("github", ""),
            "website": self.links.get("website", ""),
        }
        return d
