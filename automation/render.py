"""
Tree-driven README renderer.

The README has two generated zones, each delimited by one marker pair:

    <!-- NAV:BEGIN -->    ... Quick Navigation for the papers tree ...    <!-- NAV:END -->
    <!-- PAPERS:BEGIN --> ... the whole Papers chapter ...                <!-- PAPERS:END -->

Everything inside the markers is derived from taxonomy.json + data/*.yaml and
must never be edited by hand. Missing or duplicated markers are a hard error.
Running the renderer twice produces zero diff.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from automation import storage, taxonomy

_REPO_ROOT = Path(__file__).resolve().parents[1]
README = _REPO_ROOT / "README.md"

NAV_BEGIN, NAV_END = "<!-- NAV:BEGIN -->", "<!-- NAV:END -->"
PAPERS_BEGIN, PAPERS_END = "<!-- PAPERS:BEGIN -->", "<!-- PAPERS:END -->"

# Heading level of L1 nodes; L2 = +1, L3 = +2.
_L1_HEADING = "##"
_NAV_INDENT = {0: "- ", 1: "  * ", 2: "    + "}


# ── GitHub heading anchors ────────────────────────────────────────────────────

def gh_slug(heading: str) -> str:
    """Replicate GitHub's heading-to-anchor slug (emoji drop out, spaces
    become hyphens, so '🧱 Title' yields '-title')."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s", "-", s)
    return s


# ── Paper entry rendering (badges) ────────────────────────────────────────────

TAG_STYLES: dict[str, tuple[str, str]] = {
    "benchmark":     ("Benchmark_%26_Dataset", "F4A261"),
    "survey":        ("Survey",                "2A9D8F"),
    "position":      ("Position_Paper",        "9B59B6"),
    "empirical":     ("Empirical_Study",       "4A90D9"),
    "model":         ("Model_Release",         "E76F51"),
    "training-data": ("Training_Data",         "8AB17D"),
}


def _repo_slug(github_url: str) -> str:
    if not github_url:
        return ""
    parts = urlparse(github_url).path.strip("/").split("/")
    return "/".join(parts[:2]) if len(parts) >= 2 else ""


def _badge_paper(url: str) -> str:
    return (
        f"[![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)]({url})"
        if url else ""
    )


def _badge_github(url: str) -> str:
    slug = _repo_slug(url)
    return (
        f"[![GitHub Stars](https://img.shields.io/github/stars/{slug}?style=for-the-badge&logo=github&label=GitHub&color=black)]({url})"
        if slug else ""
    )


def _badge_website(url: str) -> str:
    if not url:
        return ""
    parsed = urlparse(url)
    if parsed.path.strip("/"):
        label = parsed.path.strip("/").split("/")[-1]
        label = re.sub(r"\.(html|md)$", "", label)
    else:
        domain = re.sub(r"^www\.", "", parsed.netloc.lower())
        label = re.sub(r"\.(com|org|net|co|gov|edu|github|dev)(\.[a-z]{2})?$", "", domain)
    label = label.replace("_", "-").upper()
    return (
        f"[![Website](https://img.shields.io/website?url={url}"
        f"&up_message={label}&up_color=blue&down_message={label}&down_color=blue"
        f"&style=for-the-badge)]({url})"
    )


def _badge_tag(tag: str) -> str:
    key = tag.lower().strip()
    if key in TAG_STYLES:
        label, color = TAG_STYLES[key]
    else:
        label, color = re.sub(r"[^A-Za-z0-9_]", "_", tag), "808080"
    display = label.replace("_", " ").replace("%26", "&")
    return f"![{display}](https://img.shields.io/badge/{label}-{color}?style=for-the-badge)"


def _format_authors(authors_field) -> str:
    if not authors_field:
        return ""
    if isinstance(authors_field, list):
        names = [str(a).strip() for a in authors_field if str(a).strip()]
    else:
        names = [s.strip() for s in str(authors_field).split(",") if s.strip()]
    if len(names) > 10:
        return ", ".join(names[:10]) + ", et al."
    return ", ".join(names)


def render_entry(e: dict) -> str:
    title = e.get("title", "").rstrip(".")
    authors = _format_authors(e.get("authors", ""))
    venue = e.get("venue", "")
    links = e.get("links", {}) or {}

    link_badges = " ".join(
        x for x in [
            _badge_paper(links.get("paper", "")),
            _badge_github(links.get("github", "")),
            _badge_website(links.get("website", "")),
        ] if x
    )
    tags = e.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    tag_badges = " ".join(_badge_tag(t) for t in tags if t)
    badges = " ".join(x for x in [link_badges, tag_badges] if x)

    lines = [f"- **{title}**  " if title and title[-1] in "?!" else f"- **{title}.**  "]
    lines.append(f"  _{authors.rstrip(' .')}._ {venue}.  ")
    if badges:
        lines.append(f"  {badges}")
    return "\n".join(lines)


# ── Zone generation ───────────────────────────────────────────────────────────

def _heading(node: taxonomy.Node, depth: int) -> str:
    prefix = _L1_HEADING + "#" * depth
    label = f"{node.emoji} {node.title}".strip()
    return f"{prefix} {label}"


def _first_sentence(text: str) -> str:
    sentence = text.strip().split(". ")[0].strip()
    return sentence if sentence.endswith(".") else sentence + "."


def render_nav(tax: taxonomy.Taxonomy) -> str:
    lines = []
    for node, depth in tax.walk():
        label = f"{node.emoji} {node.title}".strip()
        anchor = gh_slug(f"{node.emoji} {node.title}".strip())
        lines.append(f"{_NAV_INDENT[depth]}[{label}](#{anchor})")
    return "\n".join(lines)


def render_papers(tax: taxonomy.Taxonomy) -> str:
    blocks: list[str] = []
    for node, depth in tax.walk():
        blocks.append(_heading(node, depth))
        blocks.append(f"> {node.blurb or _first_sentence(node.definition)}")
        if node.is_leaf:
            entries = storage.load_entries(node.key)
            if entries:
                blocks.append("\n\n".join(render_entry(e) for e in entries))
            else:
                blocks.append("*No papers yet.*")
    return "\n\n".join(blocks)


# ── README assembly ───────────────────────────────────────────────────────────

def _replace_zone(content: str, begin: str, end: str, body: str) -> str:
    if content.count(begin) != 1 or content.count(end) != 1:
        raise ValueError(f"README must contain exactly one {begin} / {end} pair")
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(f"{begin}\n{body}\n{end}", content)


def render_readme(content: str, tax: taxonomy.Taxonomy) -> str:
    content = _replace_zone(content, NAV_BEGIN, NAV_END, render_nav(tax))
    content = _replace_zone(content, PAPERS_BEGIN, PAPERS_END, render_papers(tax))
    return content


def main() -> None:
    tax = taxonomy.load()
    content = README.read_text(encoding="utf-8")
    try:
        new_content = render_readme(content, tax)
    except ValueError as exc:
        print(f"[ERR] {exc}", file=sys.stderr)
        sys.exit(2)
    if new_content != content:
        README.write_text(new_content, encoding="utf-8")
        print("[OK] README regenerated from taxonomy.")
    else:
        print("[OK] README unchanged.")


if __name__ == "__main__":
    main()
