"""
Manages automation/state/processed.json.

Schema:
{
  "processed_ids":  ["2501.12345", ...],   // IDs that have been through the pipeline
  "rejected_ids":   ["2501.99999", ...],   // User-rejected, never re-surface
  "pending_issues": [                      // Issues awaiting approval
    {
      "issue_number": 42,
      "issue_url":    "https://github.com/...",
      "category":     "issue_resolution",
      "arxiv_ids":    ["2501.12345"],
      "papers":       [{...}],
      "batch_date":   "2025-05-29",
      "last_checked": "2025-05-29T10:00:00Z",
      "decided":      {"0": "approve"}     // persisted decisions (idx → action)
    },
    ...
  ]
}
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

_STATE_PATH = Path(__file__).parent / "state" / "processed.json"

_DEFAULT: dict[str, Any] = {
    "processed_ids":  [],
    "rejected_ids":   [],
    "pending_issues": [],
}


def load() -> dict[str, Any]:
    if not _STATE_PATH.exists():
        return {k: list(v) if isinstance(v, list) else v for k, v in _DEFAULT.items()}
    try:
        data = json.loads(_STATE_PATH.read_text(encoding="utf-8"))
        # Ensure all keys present
        for k, default in _DEFAULT.items():
            data.setdefault(k, list(default) if isinstance(default, list) else default)
        return data
    except Exception as exc:
        logger.warning("Could not load state, starting fresh: %s", exc)
        return {k: list(v) if isinstance(v, list) else v for k, v in _DEFAULT.items()}


def save(state: dict[str, Any]) -> None:
    _STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def mark_processed(state: dict[str, Any], arxiv_ids: list[str]) -> None:
    existing = set(state["processed_ids"])
    for aid in arxiv_ids:
        if aid not in existing:
            state["processed_ids"].append(aid)
            existing.add(aid)


def mark_rejected(state: dict[str, Any], arxiv_ids: list[str]) -> None:
    existing = set(state["rejected_ids"])
    for aid in arxiv_ids:
        if aid not in existing:
            state["rejected_ids"].append(aid)
            existing.add(aid)


def is_processed(state: dict[str, Any], arxiv_id: str) -> bool:
    return arxiv_id in state["processed_ids"] or arxiv_id in state["rejected_ids"]


def add_pending_issue(state: dict[str, Any], issue_meta: dict[str, Any]) -> None:
    state["pending_issues"].append(issue_meta)


def update_pending_issues(state: dict[str, Any], updated: list[dict[str, Any]]) -> None:
    state["pending_issues"] = updated
