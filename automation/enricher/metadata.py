"""
Metadata enricher — extracts venue and GitHub links from arXiv abstracts.

arXiv papers often include acceptance info in their abstract as phrases like:
  "Accepted at ICSE 2026"
  "To appear in NeurIPS 2025"
  "Published in ICML 2025"
  "Accepted to ACL 2026"

Authors also frequently share code links in the abstract:
  "Code is available at https://github.com/..."
  "Our implementation: https://github.com/..."

If no venue found, we fall back to "arXiv YYYY/MM" derived from the submission date.
"""

from __future__ import annotations

import logging
import re
from typing import Any

logger = logging.getLogger(__name__)

# Extract GitHub URLs from abstract text
_GITHUB_RE = re.compile(
    r"https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+",
    re.IGNORECASE,
)

# Patterns to extract venue mentions from abstract text
_VENUE_PATTERNS = [
    # "Accepted at/to/in VENUE YEAR" / "to appear in VENUE YEAR"
    r"(?:accepted (?:at|to|in|by)|to appear in|published (?:at|in)|appears? in|presented at)\s+"
    r"((?:the\s+)?[\w\s\-\+\/&]+?(?:\d{4}))",
    # "VENUE YEAR paper" / "VENUE'25"
    r"\b((?:ICSE|FSE|ASE|ISSTA|PLDI|POPL|OOPSLA|SOSP|OSDI|ASPLOS|MICRO|ISCA"
    r"|NeurIPS|ICML|ICLR|ACL|EMNLP|NAACL|CVPR|ICCV|ECCV|AAAI|IJCAI"
    r"|CCS|USENIX|Oakland|NDSS|CHI|CSCW|VLDB|SIGMOD|ICDE|KDD|WWW"
    r"|SOUPS|EuroSP|RAID|ACSAC|DSN|ISSRE|MSR|ICST|SANER|ICSME|WCRE"
    r"|TOSEM|TSE|JSS|IST|EMSE|JMLR|TPAMI)\s*(?:\'?\d{2,4})\b)",
]

_COMPILED = [re.compile(p, re.IGNORECASE) for p in _VENUE_PATTERNS]


def extract_venue(abstract: str, submitted: str) -> str:
    """
    Try to extract the publication venue from the abstract.
    Falls back to 'arXiv YYYY/MM' from the submission date.
    """
    for pattern in _COMPILED:
        m = pattern.search(abstract)
        if m:
            raw = m.group(1).strip().rstrip(".,;:")
            # Normalise whitespace
            venue = re.sub(r"\s+", " ", raw)
            # Trim trailing filler words
            venue = re.sub(r"\s+(?:proceedings|workshop|conference|journal)$", "", venue, flags=re.I)
            logger.debug("Extracted venue: %r", venue)
            return venue

    # Fallback: arXiv YYYY/MM
    if submitted and len(submitted) >= 7:
        year_month = submitted[:7].replace("-", "/")
        return f"arXiv {year_month}"
    return "arXiv"


def extract_github_url(abstract: str) -> str:
    """Extract the first GitHub URL mentioned in the abstract, or ''."""
    m = _GITHUB_RE.search(abstract)
    return m.group(0).rstrip(".,;:)>\"'") if m else ""


def enrich_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Fill in `venue` and `links.github` for papers that don't already have them.
    Mutates in place and returns the list.
    """
    for p in papers:
        abstract = p.get("abstract", "")

        # Venue
        if not p.get("venue"):
            venue = extract_venue(abstract, p.get("submitted", ""))
            p["venue"] = venue
            logger.debug("Venue for %s: %s", p.get("arxiv_id"), venue)

        # GitHub link — fallback from abstract if Papers With Code didn't find one
        if not p.get("links", {}).get("github"):
            url = extract_github_url(abstract)
            if url:
                p.setdefault("links", {})["github"] = url
                logger.info("  Abstract GitHub: %s → %s", p.get("arxiv_id"), url)

    return papers
