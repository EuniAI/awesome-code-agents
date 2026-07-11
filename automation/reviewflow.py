"""
Review issues: the pipeline proposes classified papers as one GitHub issue per
crawl; the owner replies with commands; the decide step applies them.

The issue body ends with a fenced JSON payload carrying every proposed paper and
its proposal, so deciding needs nothing but the issue itself. Decide is stateless
and safe to re-run: it recomputes the full decision set from the complete comment
history, and every data write is dedup-safe.

Command protocol (comments by the configured reviewer only; one command per line):
  /approve all          /approve 1,3-5
  /reject all           /reject 2,4
  /edit 3 category=web tags=benchmark,model   (implies approval; tags= optional,
                                               tags=- clears the tags)
Later commands override earlier ones for the same paper.
"""

from __future__ import annotations

import json
import logging
import re
import subprocess

from automation import config

logger = logging.getLogger(__name__)

_PAYLOAD_RE = re.compile(r"```json\n(.*?)\n```", re.DOTALL)
# Index spec captured up front; any trailing free text ("/reject 2 wrong topic")
# is tolerated and ignored.
_APPROVE_RE = re.compile(r"^/approve\s+(all|[\d,\s\-]+)", re.IGNORECASE)
_REJECT_RE = re.compile(r"^/reject\s+(all|[\d,\s\-]+)", re.IGNORECASE)
_EDIT_RE = re.compile(r"^/edit\s+(\d+)\s+(\S.*)$", re.IGNORECASE)
# key=value pairs where the value may contain spaces (venue=ICSE 2026): a value
# runs until the next key= or the end of the line.
_KV_RE = re.compile(r"(\w+)=(.+?)(?=\s+\w+=|\s*$)")


# ── gh plumbing ───────────────────────────────────────────────────────────────

def _repo() -> str:
    cfg = config.load()["repo"]
    return f"{cfg['owner']}/{cfg['name']}"


def _gh_json(args: list[str], payload: dict | None = None):
    cmd = ["gh", "api"] + args
    kwargs: dict = {"capture_output": True, "text": True, "timeout": 120}
    if payload is not None:
        cmd += ["--method", "POST", "--input", "-"]
        kwargs["input"] = json.dumps(payload)
    proc = subprocess.run(cmd, **kwargs)
    if proc.returncode != 0:
        raise RuntimeError(f"gh api {args[0]} failed: {proc.stderr[:300]}")
    return json.loads(proc.stdout) if proc.stdout.strip() else {}


# ── Issue creation ────────────────────────────────────────────────────────────

def _entry_block(i: int, e: dict) -> str:
    p = e["paper"]
    authors = ", ".join(p.get("authors", [])[:3])
    if len(p.get("authors", [])) > 3:
        authors += ", et al."
    tags = " ".join(f"`{t}`" for t in e.get("tags", [])) or "none"
    lines = [
        f"### {i}. {p['title']}",
        f"_{authors}_ · {p.get('venue', '')} · [paper]({p['links'].get('paper', '')})",
        f"**proposed: `{e['category']}`** · tags: {tags}",
    ]
    if e.get("summary"):
        lines.append(f"> {e['summary']}")
    if e.get("reason"):
        lines.append(f"<sub>{e['reason']}</sub>")
    return "\n".join(lines)


def build_issue_body(entries: list[dict], note: str = "") -> str:
    head = [
        "Reply with commands, one per line:",
        "`/approve all` · `/approve 1,3-5` · `/reject 2` · "
        "`/edit 3 category=world_terminal tags=benchmark` (edit implies approve; "
        "`tags=-` clears tags). Valid category keys: see taxonomy.json.",
    ]
    if note:
        head.append(f"\n_{note}_")
    blocks = [_entry_block(i + 1, e) for i, e in enumerate(entries)]
    payload = json.dumps(entries, ensure_ascii=False)
    tail = (
        "<details><summary>machine payload (do not edit)</summary>\n\n"
        f"```json\n{payload}\n```\n\n</details>"
    )
    return "\n\n".join(["\n".join(head)] + blocks + [tail])


def create_issue(entries: list[dict], note: str = "") -> int:
    from datetime import datetime, timezone

    cfg = config.load()
    label = cfg["review"]["label"]
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    title = f"Paper review {date}: {len(entries)} candidates"
    issue = _gh_json(
        [f"repos/{_repo()}/issues"],
        payload={"title": title, "body": build_issue_body(entries, note), "labels": [label]},
    )
    logger.info("created review issue #%s with %d papers", issue.get("number"), len(entries))
    return issue["number"]


# ── Issue reading ─────────────────────────────────────────────────────────────

def fetch_issue(number: int) -> tuple[list[dict], list[dict], dict]:
    """(payload entries, comments, issue) for a review issue."""
    issue = _gh_json([f"repos/{_repo()}/issues/{number}"])
    m = _PAYLOAD_RE.search(issue.get("body", ""))
    if not m:
        raise ValueError(f"issue #{number} has no machine payload")
    entries = json.loads(m.group(1))
    proc = subprocess.run(
        ["gh", "api", "--paginate", f"repos/{_repo()}/issues/{number}/comments"],
        capture_output=True, text=True, timeout=120,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh api comments failed: {proc.stderr[:300]}")
    comments = json.loads(proc.stdout)
    return entries, comments, issue


def pending_ids() -> set[str]:
    """Paper ids proposed in currently open review issues (still awaiting a verdict)."""
    cfg = config.load()
    label = cfg["review"]["label"]
    proc = subprocess.run(
        ["gh", "api", "--paginate", f"repos/{_repo()}/issues?labels={label}&state=open"],
        capture_output=True, text=True, timeout=120,
    )
    if proc.returncode != 0:
        logger.warning("could not list open review issues: %s", proc.stderr[:200])
        return set()
    ids: set[str] = set()
    for issue in json.loads(proc.stdout):
        m = _PAYLOAD_RE.search(issue.get("body", ""))
        if m:
            ids.update(e["paper"]["id"] for e in json.loads(m.group(1)))
    return ids


# ── Decision parsing ──────────────────────────────────────────────────────────

def _indices(spec: str, n: int) -> list[int]:
    """Parse 'all' or '1,3-5' into valid 1-based indices."""
    spec = spec.strip().rstrip(".")
    if spec.lower() == "all":
        return list(range(1, n + 1))
    out: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        m = re.fullmatch(r"(\d+)-(\d+)", part)
        if m:
            out.extend(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.isdigit():
            out.append(int(part))
    return [i for i in out if 1 <= i <= n]


def parse_decisions(comments: list[dict], reviewer: str, n: int) -> dict[int, tuple[str, dict]]:
    """index -> ('approve' | 'reject', overrides). Cumulative across the reviewer's
    comments in order; later commands override earlier ones."""
    decisions: dict[int, tuple[str, dict]] = {}
    for c in comments:
        if c.get("user", {}).get("login") != reviewer:
            continue
        for line in (c.get("body") or "").splitlines():
            line = line.strip()
            m = _APPROVE_RE.match(line)
            if m:
                for i in _indices(m.group(1), n):
                    decisions[i] = ("approve", {})
                continue
            m = _REJECT_RE.match(line)
            if m:
                for i in _indices(m.group(1), n):
                    decisions[i] = ("reject", {})
                continue
            m = _EDIT_RE.match(line)
            if m:
                i = int(m.group(1))
                if not 1 <= i <= n:
                    continue
                overrides: dict = {}
                for key, value in _KV_RE.findall(m.group(2)):
                    value = value.strip().strip("`")
                    if key == "category":
                        overrides["category"] = value
                    elif key == "tags":
                        overrides["tags"] = [] if value == "-" else value.split(",")
                    elif key == "venue":
                        overrides["venue"] = value
                decisions[i] = ("approve", overrides)
    return decisions


# ── Issue actions ─────────────────────────────────────────────────────────────

def post_comment(number: int, body: str) -> None:
    _gh_json([f"repos/{_repo()}/issues/{number}/comments"], payload={"body": body})


def close_issue(number: int) -> None:
    proc = subprocess.run(
        ["gh", "api", "--method", "PATCH", f"repos/{_repo()}/issues/{number}",
         "-f", "state=closed"],
        capture_output=True, text=True, timeout=60,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"closing issue #{number} failed: {proc.stderr[:200]}")
