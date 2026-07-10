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
  ],
  "backfill_cursor": "2025-10-01"          // next historical date to backfill (null = done)
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
    "processed_ids":   [],
    "rejected_ids":    [],
    "pending_issues":  [],
    "backfill_cursor": None,   # ISO date string, e.g. "2025-10-01"; None = no backfill pending
    "reject_feedback": [],     # [{arxiv_id, title, reason}, ...] — curator reject reasons
    "learned_rules":   "",     # LLM-synthesised rules injected into classifier prompt
    "rules_last_updated": "",  # ISO date when learned_rules was last generated
    "retry_counts":    {},     # {arxiv_id: int} — LLM failure retry count
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


_MAX_RETRIES = 3


def add_failed_classifications(state: dict[str, Any], arxiv_ids: list[str]) -> tuple[list[str], list[str]]:
    """
    Record LLM classification failures. Increment retry count for each ID.
    Returns (retry_later, give_up):
      - retry_later: IDs that haven't hit the retry limit yet (keep out of processed_ids)
      - give_up: IDs that have failed too many times (mark as processed to stop retrying)
    """
    counts: dict[str, int] = state.setdefault("retry_counts", {})
    retry_later: list[str] = []
    give_up: list[str] = []

    for aid in arxiv_ids:
        counts[aid] = counts.get(aid, 0) + 1
        if counts[aid] >= _MAX_RETRIES:
            logger.warning("Giving up on %s after %d failed attempts", aid, counts[aid])
            give_up.append(aid)
        else:
            logger.info("Will retry %s (attempt %d/%d)", aid, counts[aid], _MAX_RETRIES)
            retry_later.append(aid)

    return retry_later, give_up


def get_retry_ids(state: dict[str, Any]) -> list[str]:
    """Return IDs that failed classification and should be retried."""
    counts: dict[str, int] = state.get("retry_counts", {})
    processed = set(state.get("processed_ids", [])) | set(state.get("rejected_ids", []))
    return [aid for aid, cnt in counts.items()
            if cnt < _MAX_RETRIES and aid not in processed]


def add_reject_feedback(state: dict[str, Any], items: list[dict[str, Any]]) -> None:
    """Append curator reject reasons for classifier learning."""
    state.setdefault("reject_feedback", []).extend(items)


def maybe_refresh_learned_rules(state: dict[str, Any], min_new_items: int = 10) -> str:
    """
    If enough new reject feedback has accumulated since the last refresh,
    call the LLM to synthesise updated learned_rules and store them in state.
    Returns the current learned_rules string.
    """
    import os
    from datetime import date
    from openai import OpenAI

    feedback = state.get("reject_feedback", [])
    last_updated = state.get("rules_last_updated", "")

    # Count items added since last update
    new_items = [f for f in feedback if f.get("date", "9999") >= last_updated] if last_updated else feedback
    if len(new_items) < min_new_items:
        return state.get("learned_rules", "")

    logger.info("Refreshing learned_rules from %d reject feedback items…", len(feedback))

    feedback_text = "\n".join(
        f"- [{f.get('arxiv_id','')}] {f.get('title','')} | reason: {f.get('reason','(no reason given)')}"
        for f in feedback[-100:]  # use last 100 at most
    )

    prompt = f"""You are helping curate "Awesome Code Agents", a list of papers about AI agents
that work with source code (writing, fixing, reviewing, executing, or testing code).

Below are papers the curator REJECTED and their reasons:
{feedback_text}

Based on these rejections, write 3-7 concise bullet-point rules to help the classifier
avoid similar mistakes in the future. Be specific. Focus on patterns you see in the reasons.
Format: a plain bulleted list, each item starting with "- ".
Do not repeat the base rules (those already say: must involve source code, not general agents, etc.)
Only add NEW nuances discovered from these rejections."""

    try:
        client = OpenAI(
            base_url=os.environ.get("LITELLM_BASE_URL", "http://localhost:4000"),
            api_key=os.environ.get("LITELLM_API_KEY", "anything"),
        )
        model = os.environ.get("LITELLM_MODEL", "gemini/gemini-2.5-flash")
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=512,
        )
        rules = resp.choices[0].message.content.strip()
        state["learned_rules"] = rules
        state["rules_last_updated"] = str(date.today())
        logger.info("Learned rules updated:\n%s", rules)
    except Exception as exc:
        logger.warning("Could not refresh learned_rules: %s", exc)

    return state.get("learned_rules", "")
