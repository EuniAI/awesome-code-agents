"""Tests for the Paper model and storage layer."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from automation import storage
from automation.models import Paper
from automation.render import render_entry


def _paper(pid="2605.22535", cat="world_terminal") -> Paper:
    return Paper(
        id=pid,
        title="TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks",
        authors=["Zhaoyang Chu", "Jiarui Hu"],
        venue="arXiv 2026/05",
        links={"paper": f"https://arxiv.org/abs/{pid}", "github": "https://github.com/EuniAI/TerminalWorld", "website": ""},
        category=cat,
        tags=["benchmark"],
        summary="A benchmark of real terminal tasks.",
    )


def test_paper_id_from_url():
    assert Paper.id_from_url("https://arxiv.org/abs/2605.22535") == "2605.22535"
    assert Paper.id_from_url("https://arxiv.org/pdf/2605.22535v2") == "2605.22535"
    url = "https://openreview.net/forum?id=RuLsq4LSZK"
    assert Paper.id_from_url(url) == url


def test_paper_dict_round_trip_and_legacy_tolerance():
    p = _paper()
    q = Paper.from_dict(p.to_dict())
    assert q == p
    # legacy shapes: authors as comma string, no id field, tags as string
    legacy = {
        "title": "X",
        "authors": "A One, B Two",
        "venue": "ICSE 2026",
        "tags": "benchmark, survey",
        "links": {"paper": "https://arxiv.org/abs/2601.00001", "github": "", "website": ""},
    }
    r = Paper.from_dict(legacy)
    assert r.authors == ["A One", "B Two"]
    assert r.tags == ["benchmark", "survey"]
    assert r.id == "2601.00001"


def test_storage_round_trip_add_dedup_and_all_ids():
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        p = _paper()
        assert storage.load("world_terminal", d) == []
        assert storage.add(p, d) is True
        assert storage.add(p, d) is False          # dedup by id
        loaded = storage.load("world_terminal", d)
        assert loaded == [p]
        p2 = _paper(pid="2605.99999")
        assert storage.add(p2, d) is True
        assert storage.load("world_terminal", d)[0] == p2   # newest first
        assert storage.all_ids(["world_terminal", "web"], d) == {p.id, p2.id}


def test_render_entry_with_paper():
    md = render_entry(_paper())
    assert "**TerminalWorld" in md
    assert "Zhaoyang Chu, Jiarui Hu" in md
    assert "img.shields.io/github/stars/EuniAI/TerminalWorld" in md
    assert "Benchmark" in md
