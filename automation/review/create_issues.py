"""
Formats and creates GitHub review Issues for batches of classified papers.

One Issue per (date, category) batch.
Each paper is a numbered checklist item — user replies with:
    /approve 1,3   /reject 2   /approve all
"""

from __future__ import annotations

import logging
from collections import defaultdict
from datetime import date
from typing import Any

from automation.review import github as gh

logger = logging.getLogger(__name__)

# GitHub label definitions
_LABELS = [
    {"name": "pending-review", "color": "fbca04", "description": "Paper batch awaiting review"},
    {"name": "auto-discovered", "color": "0075ca", "description": "Found by arXiv crawler"},
    {"name": "user-submitted",  "color": "e4e669", "description": "Submitted via inbox"},
    {"name": "unknown-category","color": "d93f0b", "description": "No matching category found"},
]


def _format_paper_item(idx: int, paper: dict[str, Any]) -> str:
    """Format one paper as a Markdown checklist item."""
    title   = paper.get("title", "Untitled")
    authors = paper.get("authors", [])
    if isinstance(authors, list):
        if len(authors) > 5:
            author_str = ", ".join(authors[:5]) + ", et al."
        else:
            author_str = ", ".join(authors)
    else:
        author_str = str(authors)

    venue   = paper.get("venue", "")
    summary = paper.get("summary", "")
    tags    = paper.get("tags", [])
    links   = paper.get("links", {})
    paper_url  = links.get("paper", "")
    github_url = links.get("github", "")
    website_url = links.get("website", "")

    tag_str = ""
    if tags:
        tag_str = " | " + " ".join(f"`{t}`" for t in tags)

    link_parts = []
    if paper_url:
        link_parts.append(f"[📄 Paper]({paper_url})")
    if github_url:
        link_parts.append(f"[💻 GitHub]({github_url})")
    if website_url:
        link_parts.append(f"[🌐 Website]({website_url})")
    link_str = " · ".join(link_parts) if link_parts else "_(no links)_"

    lines = [
        f"### {idx}. {title}",
        f"**Authors:** {author_str}  ",
        f"**Venue:** {venue}{tag_str}  ",
        f"> {summary}" if summary else "",
        f"{link_str}",
    ]
    return "\n".join(l for l in lines if l)


def _format_issue_body(
    batch_date: str,
    category: str,
    papers: list[dict[str, Any]],
) -> str:
    cat_display = category.replace("_", " ").title()
    items = "\n\n---\n\n".join(
        _format_paper_item(i + 1, p) for i, p in enumerate(papers)
    )

    commands_help = (
        "**Review commands** (comment on this issue):\n"
        "- `/approve all` — accept all papers\n"
        "- `/approve 1,3` — accept papers 1 and 3\n"
        "- `/reject 2` — discard paper 2\n"
        "- `/approve 1,3 /reject 2` — mixed\n"
        "- `/edit 1 category=code_generation` — change category before approving\n"
        "- `/edit 1 venue=ICSE 2026` — fix venue\n"
    )

    return (
        f"## 📋 {batch_date} · {cat_display} — {len(papers)} paper(s)\n\n"
        f"> Auto-processed by the arXiv crawler pipeline. "
        f"Review each paper and reply with the commands below.\n\n"
        f"---\n\n"
        f"{items}\n\n"
        f"---\n\n"
        f"{commands_help}"
    )


def create_review_issues(
    papers: list[dict[str, Any]],
    owner: str,
    repo: str,
    batch_date: str | None = None,
) -> list[dict[str, Any]]:
    """
    Group papers by category and create one GitHub Issue per group.

    Returns list of issue metadata dicts (for state tracking):
        [{issue_number, category, arxiv_ids, batch_date}, ...]
    """
    if batch_date is None:
        batch_date = str(date.today())

    # Ensure labels exist (idempotent)
    try:
        gh.ensure_labels_exist(owner, repo, _LABELS)
    except Exception as exc:
        logger.warning("Could not ensure labels: %s", exc)

    # Separate unknown-category papers
    unknown = [p for p in papers if not p.get("category")]
    categorised: dict[str, list] = defaultdict(list)
    for p in papers:
        if p.get("category"):
            categorised[p["category"]].append(p)

    created_issues: list[dict[str, Any]] = []

    # Create one issue per category batch
    for category, batch in sorted(categorised.items()):
        cat_display = category.replace("_", " ").title()
        title = f"[{batch_date}] {cat_display} — {len(batch)} paper(s)"
        body  = _format_issue_body(batch_date, category, batch)

        source_labels = set()
        for p in batch:
            source_labels.add("auto-discovered" if p.get("source") == "arxiv" else "user-submitted")

        issue = gh.create_issue(
            owner, repo, title, body,
            labels=["pending-review"] + list(source_labels),
        )
        issue_number = issue["issue_number"] if "issue_number" in issue else issue.get("number")
        logger.info("Created Issue #%s: %s", issue_number, title)

        created_issues.append({
            "issue_number": issue_number,
            "issue_url":    issue.get("html_url", ""),
            "category":     category,
            "arxiv_ids":    [p["arxiv_id"] for p in batch],
            "papers":       batch,
            "batch_date":   batch_date,
        })

    # Unknown category — single triage issue
    if unknown:
        title = f"[{batch_date}] ⚠️ Unknown Category — {len(unknown)} paper(s) need triage"
        body = (
            f"## ⚠️ Papers with No Matching Category\n\n"
            f"The classifier could not assign these papers to an existing category.\n"
            f"Please decide: create a new category, assign to an existing one, or reject.\n\n"
            f"**Reply format:** `/triage <number> category=<key>` or `/reject <number>`\n\n"
            f"---\n\n"
        ) + "\n\n---\n\n".join(_format_paper_item(i + 1, p) for i, p in enumerate(unknown))

        issue = gh.create_issue(
            owner, repo, title, body,
            labels=["pending-review", "unknown-category"],
        )
        issue_number = issue.get("number")
        logger.info("Created triage Issue #%s for %d unknown-category papers", issue_number, len(unknown))

        created_issues.append({
            "issue_number": issue_number,
            "issue_url":    issue.get("html_url", ""),
            "category":     "__unknown__",
            "arxiv_ids":    [p.get("arxiv_id", "") for p in unknown],
            "papers":       unknown,
            "batch_date":   batch_date,
        })

    return created_issues
