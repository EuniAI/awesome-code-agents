#!/usr/bin/env python3
"""
Generate badges for GitHub repositories in the Acknowledgements section of README.md.

Behavior (no CLI parameters needed):
- Reads fixed YAML at data/ack_repos.yaml (relative to repo root)
- Replaces the Acknowledgements nested repo list in README.md with items
  including Stars and Last Commit badges
- Writes changes in-place to README.md

Usage:
  python scripts/generate_ack_badges.py

Notes:
- Only modifies the nested bullets under "## 🙏 Acknowledgements".
- Skips lines that already contain shields.io badges to avoid duplication (legacy mode only).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple, Optional

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None


ACK_HEADING_PATTERN = re.compile(r"^##\s+🙏\s+Acknowledgements\s*$")
NEXT_HEADING_PATTERN = re.compile(r"^##\s+\S")
GITHUB_URL_PATTERN = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)(?:[\)/]|$)")


def extract_ack_block(lines: List[str]) -> Tuple[int, int]:
    """Return (start_index, end_index) for the Acknowledgements block.

    The end_index is exclusive.
    """
    start = -1
    for i, line in enumerate(lines):
        if ACK_HEADING_PATTERN.match(line.rstrip("\n")):
            start = i
            break
    if start == -1:
        raise RuntimeError("Acknowledgements heading not found.")

    end = len(lines)
    for j in range(start + 1, len(lines)):
        if NEXT_HEADING_PATTERN.match(lines[j].rstrip("\n")):
            end = j
            break
    return start, end


def already_has_badge(line: str) -> bool:
    return "img.shields.io/github/" in line


def append_badges_to_line(line: str) -> str:
    """Append stars and last-commit badges to a nested bullet line with a GitHub link.

    Preserves existing indentation and trailing newline.
    """
    newline = "\n" if line.endswith("\n") else ""
    content = line.rstrip("\n")

    match = GITHUB_URL_PATTERN.search(content)
    if not match:
        return line

    owner, repo = match.group(1), match.group(2)

    if already_has_badge(content):
        return line

    # Construct badges
    stars_badge = (
        f"[![Stars](https://img.shields.io/github/stars/{owner}/{repo}?label=stars)](https://github.com/{owner}/{repo}/stargazers)"
    )
    last_commit_badge = (
        f"<a href=\"https://img.shields.io/github/last-commit/{owner}/{repo}?color=green\">"
        f"<img src=\"https://img.shields.io/github/last-commit/{owner}/{repo}?color=green\" alt=\"Last Commit\"></a>"
    )

    # Append with two spaces between items to keep inline spacing readable
    updated = f"{content}  {stars_badge}  {last_commit_badge}{newline}"
    return updated


def transform_ack_block(lines: List[str], start: int, end: int) -> List[str]:
    updated = lines[:]

    # Only modify nested bullets that are likely the repo list items, e.g., lines starting with two spaces then '- ['
    for idx in range(start + 1, end):
        line = updated[idx]
        # Preserve non-list and top-level bullets; focus on nested bullets under acknowledgements
        if line.startswith("  - ") and "github.com" in line:
            updated[idx] = append_badges_to_line(line)

    return updated


def detect_repo_list_range(lines: List[str], start: int, end: int) -> Optional[Tuple[int, int]]:
    """Detect the contiguous range of nested repo list items to replace.

    Returns (s, e) indices [s, e) or None if not found.
    """
    s = None
    e = None
    for idx in range(start + 1, end):
        line = lines[idx]
        if line.startswith("  - ") and "github.com" in line:
            s = idx
            break
    if s is None:
        return None
    e = s
    for idx in range(s, end):
        line = lines[idx]
        if line.startswith("  - ") and "github.com" in line:
            e = idx + 1
        else:
            break
    return (s, e)


def parse_github_url(url: str) -> Optional[Tuple[str, str]]:
    m = GITHUB_URL_PATTERN.search(url)
    if not m:
        return None
    return m.group(1), m.group(2)


def load_repo_urls_from_yaml(yaml_path: Path) -> List[str]:
    if yaml is None:
        raise SystemExit("PyYAML is required. Install with: pip install pyyaml")
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    urls: List[str] = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                urls.append(item)
            elif isinstance(item, dict) and "url" in item:
                urls.append(str(item["url"]))
    elif isinstance(data, dict) and "repos" in data and isinstance(data["repos"], list):
        for item in data["repos"]:
            if isinstance(item, str):
                urls.append(item)
            elif isinstance(item, dict) and "url" in item:
                urls.append(str(item["url"]))
    else:
        raise SystemExit("YAML must be a list of URLs or {repos: [ ... ]}")
    # De-duplicate while preserving order
    seen = set()
    deduped: List[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


def format_repo_list_items(urls: List[str]) -> List[str]:
    items: List[str] = []
    for url in urls:
        parsed = parse_github_url(url)
        if not parsed:
            continue
        owner, repo = parsed
        name = repo  # Use repo name as display text by default
        # allow nicer display if the repo name in URL has uppercase (keep as-is)
        display_text = name
        stars_badge = (
            f"[![Stars](https://img.shields.io/github/stars/{owner}/{repo}?label=stars)](https://github.com/{owner}/{repo}/stargazers)"
        )
        last_commit_badge = (
            f"<a href=\"https://img.shields.io/github/last-commit/{owner}/{repo}?color=green\">"
            f"<img src=\"https://img.shields.io/github/last-commit/{owner}/{repo}?color=green\" alt=\"Last Commit\"></a>"
        )
        line = (
            f"  - [{display_text}]({url})  {stars_badge}  {last_commit_badge}\n"
        )
        items.append(line)
    return items


def replace_repo_list_with_yaml(lines: List[str], start: int, end: int, urls: List[str]) -> List[str]:
    rng = detect_repo_list_range(lines, start, end)
    if rng is None:
        # Insert after the second bullet (intro line), preserving a blank line if any
        insert_at = start + 2
        before = lines[:insert_at]
        after = lines[insert_at:end]
        rest = lines[end:]
        items = format_repo_list_items(urls)
        return before + items + after + rest
    s, e = rng
    before = lines[:s]
    after = lines[e:]
    items = format_repo_list_items(urls)
    return before + items + after


def process_readme(path: Path, inplace: bool, yaml_path: Optional[Path]) -> str:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)

    start, end = extract_ack_block(lines)
    if yaml_path is not None:
        urls = load_repo_urls_from_yaml(yaml_path)
        updated_lines = replace_repo_list_with_yaml(lines, start, end, urls)
    else:
        updated_lines = transform_ack_block(lines, start, end)
    updated_text = "".join(updated_lines)

    if inplace:
        if updated_text != original:
            path.write_text(updated_text, encoding="utf-8")
        return ""
    return updated_text


def main() -> None:
    # Operate from repository root inferred by script location
    repo_root = Path(__file__).resolve().parents[1]
    readme = repo_root / "README.md"
    yaml_path = repo_root / "data" / "ack_repos.yaml"

    if not readme.exists():
        raise SystemExit(f"README not found: {readme}")
    if not yaml_path.exists():
        raise SystemExit(f"YAML not found: {yaml_path}")

    # Always YAML-driven replacement, always write in place
    process_readme(readme, inplace=True, yaml_path=yaml_path)


if __name__ == "__main__":
    main()
