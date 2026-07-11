"""Tests for taxonomy loading and README rendering. Run: python -m pytest automation/tests/"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from automation import taxonomy
from automation.render import (
    NAV_BEGIN, NAV_END, PAPERS_BEGIN, PAPERS_END,
    gh_slug, render_nav, render_papers, render_readme,
)


def test_real_taxonomy_loads_and_validates():
    tax = taxonomy.load(force=True)
    leaves = tax.leaves()
    assert len(leaves) == 24
    keys = tax.leaf_keys()
    assert len(keys) == len(set(keys))
    assert tax.by_key("agency").axis
    assert tax.by_key("software_debugging").is_leaf


def test_gh_slug_matches_github_behavior():
    # Reference anchors observed in GitHub's own rendering of this README.
    assert gh_slug("📚 Papers") == "-papers"
    assert gh_slug("🚀 Products & Tools") == "-products--tools"
    assert gh_slug("Environment Setup & CI/CD") == "environment-setup--cicd"
    assert gh_slug("🧊 3D & CAD") == "-3d--cad"
    assert gh_slug("Code as Artifact: Building the Digital World") == \
        "code-as-artifact-building-the-digital-world"


def _tiny_tax() -> taxonomy.Taxonomy:
    raw = {
        "nodes": [
            {
                "key": "artifact", "emoji": "🧱", "title": "Code as Artifact",
                "definition": "Builds things. More detail here.",
                "axis": "domain",
                "children": [
                    {"key": "software", "emoji": "💻", "title": "General Software",
                     "definition": "Software work."},
                ],
            },
        ]
    }
    tax = taxonomy.Taxonomy(raw=raw, nodes=[taxonomy._parse_node(n) for n in raw["nodes"]])
    return tax


def test_render_nav_structure():
    nav = render_nav(_tiny_tax())
    assert nav.splitlines() == [
        "- [🧱 Code as Artifact](#-code-as-artifact)",
        "  * [💻 General Software](#-general-software)",
    ]


def test_render_papers_headings_and_empty_note():
    papers = render_papers(_tiny_tax())
    assert "## 🧱 Code as Artifact" in papers
    assert "### 💻 General Software" in papers
    assert "> Builds things." in papers
    assert "*No papers yet.*" in papers


def test_render_readme_idempotent_and_strict():
    tax = _tiny_tax()
    doc = f"header\n{NAV_BEGIN}\nstale\n{NAV_END}\nmiddle\n{PAPERS_BEGIN}\nstale\n{PAPERS_END}\ntail\n"
    once = render_readme(doc, tax)
    twice = render_readme(once, tax)
    assert once == twice
    assert "stale" not in once
    assert once.startswith("header") and once.rstrip().endswith("tail")

    try:
        render_readme("no markers here", tax)
        raised = False
    except ValueError:
        raised = True
    assert raised
