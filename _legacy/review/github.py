"""
Thin GitHub REST API wrapper (Issues only).

Uses GITHUB_TOKEN from .env. All requests go to api.github.com.
"""

from __future__ import annotations

import logging
import os
import time
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

_BASE = "https://api.github.com"
_TIMEOUT = 15
_RETRY_DELAY = 5.0


def _headers() -> dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        raise EnvironmentError("GITHUB_TOKEN not set in environment / .env")
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _request(method: str, path: str, **kwargs) -> requests.Response:
    url = f"{_BASE}{path}"
    for attempt in range(1, 4):
        try:
            resp = requests.request(method, url, headers=_headers(), timeout=_TIMEOUT, **kwargs)
            if resp.status_code == 403 and "rate limit" in resp.text.lower():
                logger.warning("GitHub rate limit hit, sleeping 60s…")
                time.sleep(60)
                continue
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            logger.warning("GitHub API attempt %d failed: %s", attempt, exc)
            if attempt < 3:
                time.sleep(_RETRY_DELAY)
    raise RuntimeError(f"GitHub API request failed after 3 attempts: {method} {path}")


# ── Issue CRUD ────────────────────────────────────────────────────────────────

def create_issue(
    owner: str,
    repo: str,
    title: str,
    body: str,
    labels: list[str] | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {"title": title, "body": body}
    if labels:
        payload["labels"] = labels
    resp = _request("POST", f"/repos/{owner}/{repo}/issues", json=payload)
    return resp.json()


def update_issue(
    owner: str,
    repo: str,
    issue_number: int,
    *,
    state: str | None = None,
    body: str | None = None,
    title: str | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    if state is not None:
        payload["state"] = state
    if body is not None:
        payload["body"] = body
    if title is not None:
        payload["title"] = title
    resp = _request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)
    return resp.json()


def close_issue(owner: str, repo: str, issue_number: int) -> None:
    update_issue(owner, repo, issue_number, state="closed")
    logger.info("Closed issue #%d", issue_number)


def get_issue_comments(
    owner: str, repo: str, issue_number: int, since: str | None = None
) -> list[dict[str, Any]]:
    """Return all comments on an issue. `since` is an ISO 8601 timestamp."""
    params: dict[str, Any] = {"per_page": 100}
    if since:
        params["since"] = since

    comments: list[dict[str, Any]] = []
    page = 1
    while True:
        params["page"] = page
        resp = _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params=params)
        batch = resp.json()
        if not batch:
            break
        comments.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    return comments


def add_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> dict[str, Any]:
    resp = _request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})
    return resp.json()


def add_reaction(
    owner: str, repo: str, issue_number: int, comment_id: int, reaction: str = "+1"
) -> None:
    """Add a reaction to a comment. reaction ∈ {+1,-1,laugh,confused,heart,hooray,rocket,eyes}"""
    _request(
        "POST",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions",
        json={"content": reaction},
    )


def add_issue_reaction(
    owner: str, repo: str, issue_number: int, reaction: str = "+1"
) -> None:
    """Add a reaction directly to an issue."""
    _request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/reactions",
        json={"content": reaction},
    )


def ensure_labels_exist(owner: str, repo: str, labels: list[dict[str, str]]) -> None:
    """
    Create labels that don't already exist.
    Each label dict: {"name": "...", "color": "rrggbb", "description": "..."}
    """
    existing_resp = _request("GET", f"/repos/{owner}/{repo}/labels", params={"per_page": 100})
    existing = {l["name"] for l in existing_resp.json()}
    for label in labels:
        if label["name"] not in existing:
            try:
                _request("POST", f"/repos/{owner}/{repo}/labels", json=label)
                logger.info("Created label: %s", label["name"])
            except Exception as exc:
                logger.warning("Could not create label %s: %s", label["name"], exc)
