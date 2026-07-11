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
from automation.models import Paper

_REPO_ROOT = Path(__file__).resolve().parents[1]
README = _REPO_ROOT / "README.md"
FULL_LIST = _REPO_ROOT / "automation" / "PAPERS.md"

NAV_BEGIN, NAV_END = "<!-- NAV:BEGIN -->", "<!-- NAV:END -->"
PAPERS_BEGIN, PAPERS_END = "<!-- PAPERS:BEGIN -->", "<!-- PAPERS:END -->"

# The README is a VIEW: papers from the last N days, keeping the front page
# focused on the frontier. PAPERS.md is the complete collection (recent papers
# included), fully generated with the same tree.
FRESH_DAYS = 365

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
    "benchmark":     ("Benchmark",       "F4A261"),
    "survey":        ("Survey",          "2A9D8F"),
    "position":      ("Position_Paper",  "9B59B6"),
    "empirical":     ("Empirical_Study", "4A90D9"),
    "model":         ("Model",           "E76F51"),
    "training-data": ("Training_Data",   "8AB17D"),
}


def _repo_slug(github_url: str) -> str:
    if not github_url:
        return ""
    parts = urlparse(github_url).path.strip("/").split("/")
    return "/".join(parts[:2]) if len(parts) >= 2 else ""


def _badge_paper(url: str) -> str:
    """Paper badge; the arXiv logo only for actual arXiv links."""
    if not url:
        return ""
    logo = "&logo=arxiv&logoColor=white" if "arxiv.org" in url.lower() else ""
    return f"[![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge{logo})]({url})"


def _badge_github(url: str) -> str:
    slug = _repo_slug(url)
    return (
        f"[![GitHub Stars](https://img.shields.io/github/stars/{slug}?style=for-the-badge&logo=github&label=GitHub&color=black)]({url})"
        if slug else ""
    )


def _website_label(url: str) -> str:
    parsed = urlparse(url)
    if parsed.path.strip("/"):
        label = parsed.path.strip("/").split("/")[-1]
        label = re.sub(r"\.(html|md)$", "", label)
    else:
        domain = re.sub(r"^www\.", "", parsed.netloc.lower())
        label = re.sub(r"\.(com|org|net|co|gov|edu|github|dev)(\.[a-z]{2})?$", "", domain)
    return label.replace("_", "-").upper() or "WEBSITE"


def _badge_website(url: str) -> str:
    """Static badge (no liveness ping) labeled from the site's domain or page name."""
    if not url:
        return ""
    label = _website_label(url).replace("-", "--").replace(" ", "_")
    return f"[![Website](https://img.shields.io/badge/{label}-blue?style=for-the-badge)]({url})"


def _badge_tag(tag: str) -> str:
    key = tag.lower().strip()
    if key in TAG_STYLES:
        label, color = TAG_STYLES[key]
    else:
        label, color = re.sub(r"[^A-Za-z0-9_]", "_", tag), "808080"
    display = label.replace("_", " ").replace("%26", "&")
    return f"![{display}](https://img.shields.io/badge/{label}-{color}?style=for-the-badge)"


def _format_authors(names: list[str]) -> str:
    names = [n for n in names if n.strip()]
    if len(names) > 10:
        return ", ".join(names[:10]) + ", et al."
    return ", ".join(names)


def render_entry(p: Paper) -> str:
    title = p.title.rstrip(".")
    authors = _format_authors(p.authors)
    venue = p.venue

    link_badges = " ".join(
        x for x in [
            _badge_paper(p.links.get("paper", "")),
            _badge_github(p.links.get("github", "")),
            _badge_website(p.links.get("website", "")),
        ] if x
    )
    tag_badges = " ".join(_badge_tag(t) for t in p.tags if t)
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


def _fresh_cutoff() -> str:
    import datetime

    return str(datetime.date.today() - datetime.timedelta(days=FRESH_DAYS))


def render_papers(tax: taxonomy.Taxonomy) -> str:
    """The README papers chapter: fresh papers only, with per-leaf archive links."""
    cutoff = _fresh_cutoff()
    blocks: list[str] = []
    for node, depth in tax.walk():
        blocks.append(_heading(node, depth))
        blocks.append(f"> {node.blurb or _first_sentence(node.definition)}")
        if node.is_leaf:
            papers = storage.load(node.key)
            fresh = [p for p in papers if storage.date_key(p) >= cutoff]
            older = len(papers) - len(fresh)
            if fresh:
                blocks.append("\n\n".join(render_entry(p) for p in fresh))
            elif not older:
                blocks.append("*No papers yet.*")
            if older:
                anchor = gh_slug(f"{node.emoji} {node.title}".strip())
                blocks.append(f"<sub>… plus {older} earlier paper(s): see the "
                              f"[full list](automation/PAPERS.md#{anchor}).</sub>")
    return "\n\n".join(blocks)


def render_full_list(tax: taxonomy.Taxonomy) -> str:
    """PAPERS.md: the COMPLETE collection (recent papers included), same tree.
    The README is just this document's last-twelve-months view."""
    blocks: list[str] = [
        "# Full Paper List\n\n"
        "> The complete collection, every paper ever curated, newest first. The "
        "README shows only the last twelve months of this list. Auto-generated; "
        "do not edit by hand.",
    ]
    for node, depth in tax.walk():
        blocks.append(_heading(node, depth))
        if not node.is_leaf:
            continue
        papers = storage.load(node.key)
        if papers:
            blocks.append("\n\n".join(render_entry(p) for p in papers))
        else:
            blocks.append("*No papers yet.*")
    return "\n\n".join(blocks) + "\n"


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
    full = render_full_list(tax)
    if not FULL_LIST.exists() or FULL_LIST.read_text(encoding="utf-8") != full:
        FULL_LIST.write_text(full, encoding="utf-8")
        print("[OK] PAPERS.md regenerated.")


if __name__ == "__main__":
    main()
