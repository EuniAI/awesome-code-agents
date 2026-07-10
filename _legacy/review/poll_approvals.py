"""
Polls pending GitHub Issues for /approve and /reject commands.

Command syntax (case-insensitive, from the designated reviewer only):
    /approve all
    /approve 1,3,5
    /reject 2
    /reject 2 not related to code agents
    /approve 1,3 /reject 2 wrong topic
    /edit 2 category=code_generation
    /edit 2 venue=ICSE 2026
    /triage 1 category=code_generation      (for unknown-category issues)

Reject reasons (text after the numbers) are recorded in state and used
periodically to improve the classifier via learned_rules.

After processing, the bot:
    - Comments a summary of what was actioned
    - Closes the issue when all items have been decided
"""

from __future__ import annotations

import logging
import re
from typing import Any

from automation.review import github as gh

logger = logging.getLogger(__name__)

# ── Command parsing ───────────────────────────────────────────────────────────

_APPROVE_RE = re.compile(r"/approve\s+(all|\d[\d,\s]*)", re.IGNORECASE)
# Captures: numbers + optional reason text until the next command or end of line
_REJECT_RE  = re.compile(r"/reject\s+(all|\d[\d,\s]*)([^/\n]*)?", re.IGNORECASE)
_EDIT_RE    = re.compile(r"/(?:edit|triage)\s+(\d+)\s+(\w+)=(.+?)(?=\s*/|$)", re.IGNORECASE)


def _parse_indices(raw: str, total: int) -> set[int]:
    """Parse '1,3,5' or 'all' into a set of 0-based indices."""
    raw = raw.strip()
    if raw.lower() == "all":
        return set(range(total))
    indices: set[int] = set()
    for part in re.split(r"[\s,]+", raw):
        part = part.strip()
        if part.isdigit():
            idx = int(part) - 1   # 1-based → 0-based
            if 0 <= idx < total:
                indices.add(idx)
    return indices


def parse_commands(
    comment_body: str,
    total_papers: int,
) -> dict[str, Any]:
    """
    Parse a comment body into a commands dict:
    {
        "approve": {0, 2, ...},           # 0-based paper indices
        "reject":  {1, ...},
        "reject_reasons": {1: "not code-related", ...},
        "edits":   {0: {"category": "code_generation"}, ...},
    }
    """
    approved: set[int] = set()
    rejected: set[int] = set()
    reject_reasons: dict[int, str] = {}
    edits: dict[int, dict[str, str]] = {}

    for m in _APPROVE_RE.finditer(comment_body):
        approved |= _parse_indices(m.group(1), total_papers)

    for m in _REJECT_RE.finditer(comment_body):
        indices = _parse_indices(m.group(1), total_papers)
        reason = (m.group(2) or "").strip()
        rejected |= indices
        if reason:
            for idx in indices:
                reject_reasons[idx] = reason

    # Rejected takes precedence if same index appears in both
    approved -= rejected

    for m in _EDIT_RE.finditer(comment_body):
        idx = int(m.group(1)) - 1   # 1-based → 0-based
        field = m.group(2).strip().lower()
        value = m.group(3).strip()
        if 0 <= idx < total_papers:
            edits.setdefault(idx, {})[field] = value

    return {"approve": approved, "reject": rejected, "reject_reasons": reject_reasons, "edits": edits}


# ── Poll ──────────────────────────────────────────────────────────────────────

def poll_issue(
    issue_meta: dict[str, Any],
    owner: str,
    repo: str,
    reviewer: str,
    last_checked: str | None = None,
) -> dict[str, Any]:
    """
    Poll a single issue for reviewer commands.

    Returns an action dict:
    {
        "issue_number": int,
        "approved_papers": [paper_dict, ...],   # with any edits applied
        "rejected_ids":    [arxiv_id, ...],
        "fully_resolved":  bool,
        "new_last_checked": str,                # ISO timestamp of latest comment seen
    }
    """
    issue_number = issue_meta["issue_number"]
    papers = list(issue_meta.get("papers", []))   # shallow copy
    total = len(papers)

    if total == 0:
        return {
            "issue_number":  issue_number,
            "approved_papers": [],
            "rejected_ids":    [],
            "fully_resolved":  True,
            "new_last_checked": last_checked or "",
        }

    comments = gh.get_issue_comments(owner, repo, issue_number, since=last_checked)

    # Track which indices have been decided (persisted in issue_meta["decided"]).
    # JSON round-trips turn int keys into strings, so normalise to int here.
    decided: dict[int, str] = {int(k): v for k, v in issue_meta.get("decided", {}).items()}
    reject_reasons: dict[int, str] = {int(k): v for k, v in issue_meta.get("reject_reasons", {}).items()}
    pending_edits: dict[int, dict[str, str]] = {}
    latest_ts = last_checked or ""

    for comment in comments:
        author = comment.get("user", {}).get("login", "")
        if author.lower() != reviewer.lower():
            continue  # only trust the reviewer

        body = comment.get("body", "")
        ts   = comment.get("updated_at") or comment.get("created_at") or ""
        if ts > latest_ts:
            latest_ts = ts

        cmds = parse_commands(body, total)

        for idx in cmds["approve"]:
            decided[idx] = "approve"
        for idx in cmds["reject"]:
            decided[idx] = "reject"
        for idx, reason in cmds["reject_reasons"].items():
            reject_reasons[idx] = reason
        for idx, fields in cmds["edits"].items():
            pending_edits.setdefault(idx, {}).update(fields)

    # Apply edits to paper dicts
    for idx, fields in pending_edits.items():
        if 0 <= idx < total:
            for field, value in fields.items():
                if field in ("category", "venue", "tags"):
                    if field == "tags":
                        papers[idx]["tags"] = [t.strip() for t in value.split(",")]
                    else:
                        papers[idx][field] = value

    approved_papers = [papers[i] for i in sorted(decided) if decided[i] == "approve"]
    rejected_ids    = [papers[i].get("arxiv_id", "") for i in sorted(decided) if decided[i] == "reject"]
    # Attach reject reason and paper title for learning purposes
    rejected_with_reasons = [
        {
            "arxiv_id": papers[i].get("arxiv_id", ""),
            "title":    papers[i].get("title", ""),
            "reason":   reject_reasons.get(i, ""),
        }
        for i in sorted(decided) if decided[i] == "reject"
    ]
    fully_resolved  = len(decided) == total

    return {
        "issue_number":         issue_number,
        "approved_papers":      approved_papers,
        "rejected_ids":         rejected_ids,
        "rejected_with_reasons": rejected_with_reasons,
        "fully_resolved":       fully_resolved,
        "new_last_checked":     latest_ts,
        "decided":              decided,
        "reject_reasons":       reject_reasons,
    }


def poll_all_pending(
    pending_issues: list[dict[str, Any]],
    owner: str,
    repo: str,
    reviewer: str,
) -> tuple[list[dict[str, Any]], list[str], list[dict[str, Any]]]:
    """
    Poll all pending issues.

    Returns:
        (approved_papers, all_rejected_ids, rejected_with_reasons, updated_pending_issues)
        - approved_papers: flat list of newly approved paper dicts
        - all_rejected_ids: flat list of newly rejected arXiv IDs
        - rejected_with_reasons: list of {arxiv_id, title, reason} for feedback learning
        - updated_pending_issues: issues not yet fully resolved (for state persistence)
    """
    all_approved: list[dict[str, Any]] = []
    all_rejected_ids: list[str] = []
    all_rejected_with_reasons: list[dict[str, Any]] = []
    still_pending: list[dict[str, Any]] = []

    for issue_meta in pending_issues:
        prev_decided: dict[int, str] = {int(k): v for k, v in issue_meta.get("decided", {}).items()}

        result = poll_issue(
            issue_meta, owner, repo, reviewer,
            last_checked=issue_meta.get("last_checked"),
        )

        # Only surface decisions that are NEW since last poll
        new_decided = {
            k: v for k, v in result["decided"].items()
            if k not in prev_decided
        }
        papers = list(issue_meta.get("papers", []))

        newly_approved = [papers[i] for i in sorted(new_decided) if new_decided[i] == "approve"]
        newly_rejected_ids = [papers[i].get("arxiv_id", "") for i in sorted(new_decided) if new_decided[i] == "reject"]
        newly_rejected_with_reasons = [
            r for r in result["rejected_with_reasons"]
            if r["arxiv_id"] in newly_rejected_ids
        ]

        all_approved.extend(newly_approved)
        all_rejected_ids.extend(rid for rid in newly_rejected_ids if rid)
        all_rejected_with_reasons.extend(newly_rejected_with_reasons)

        # Post confirmation only when there are new decisions this cycle
        if newly_approved or newly_rejected_ids:
            _post_confirmation(owner, repo, issue_meta, {
                "approved_papers":       newly_approved,
                "rejected_ids":          newly_rejected_ids,
                "rejected_with_reasons": newly_rejected_with_reasons,
                "fully_resolved":        result["fully_resolved"],
            })

        if result["fully_resolved"]:
            gh.close_issue(owner, repo, issue_meta["issue_number"])
            logger.info("Issue #%d fully resolved and closed", issue_meta["issue_number"])
        else:
            updated = dict(issue_meta)
            updated["last_checked"]  = result["new_last_checked"]
            updated["decided"]       = result["decided"]
            updated["reject_reasons"] = result["reject_reasons"]
            still_pending.append(updated)

    return all_approved, all_rejected_ids, all_rejected_with_reasons, still_pending


def _post_confirmation(
    owner: str,
    repo: str,
    issue_meta: dict[str, Any],
    result: dict[str, Any],
) -> None:
    """Post a bot comment summarising what was approved/rejected this cycle."""
    lines = ["**🤖 Pipeline update:**\n"]

    if result["approved_papers"]:
        lines.append(f"✅ **Approved {len(result['approved_papers'])} paper(s)** — will be added to the repo in the next finalize run.")
        for p in result["approved_papers"]:
            lines.append(f"  - {p.get('title', p.get('arxiv_id', ''))}")

    if result["rejected_ids"]:
        lines.append(f"\n❌ **Rejected {len(result['rejected_ids'])} paper(s)** — blacklisted.")
        for r in result.get("rejected_with_reasons", []):
            reason_str = f" — _{r['reason']}_" if r.get("reason") else ""
            lines.append(f"  - {r.get('title', r.get('arxiv_id', ''))}{reason_str}")

    if result["fully_resolved"]:
        lines.append("\n_All items decided — closing this issue._")

    body = "\n".join(lines)
    try:
        gh.add_issue_comment(owner, repo, issue_meta["issue_number"], body)
    except Exception as exc:
        logger.warning("Could not post confirmation comment: %s", exc)
