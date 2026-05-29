"""
Metadata enricher — extracts venue from arXiv abstract/comments.

arXiv papers often include acceptance info in their abstract as phrases like:
  "Accepted at ICSE 2026"
  "To appear in NeurIPS 2025"
  "Published in ICML 2025"
  "Accepted to ACL 2026"

If none found, we fall back to "arXiv YYYY/MM" derived from the submission date.
"""

from __future__ import annotations

import logging
import re
from typing import Any

logger = logging.getLogger(__name__)

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


def enrich_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Fill in the `venue` field for papers that don't already have one.
    Mutates in place and returns the list.
    """
    for p in papers:
        if p.get("venue"):
            continue
        venue = extract_venue(p.get("abstract", ""), p.get("submitted", ""))
        p["venue"] = venue
        logger.debug("Venue for %s: %s", p.get("arxiv_id"), venue)
    return papers
