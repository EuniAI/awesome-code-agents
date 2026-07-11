"""Tests for sources parsing/filtering and the review command protocol (no network)."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from automation import reviewflow, sources, storage

_FEED = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2601.12345v2</id>
    <title>Test Paper:
      A Coding Agent</title>
    <summary>  An abstract   about agents. </summary>
    <published>2026-01-15T12:00:00Z</published>
    <author><name>Alice A</name></author>
    <author><name>Bob B</name></author>
  </entry>
</feed>"""


def test_feed_parsing_builds_ready_paper():
    (paper, abstract), = sources._feed_entries(_FEED)
    assert paper.id == "2601.12345"
    assert paper.title == "Test Paper: A Coding Agent"
    assert paper.authors == ["Alice A", "Bob B"]
    assert paper.published == "2026-01-15"
    assert paper.venue == "arXiv 2026/01"
    assert paper.links["paper"] == "https://arxiv.org/abs/2601.12345"
    assert abstract == "An abstract about agents."


def test_keyword_hit_respects_word_boundaries():
    kws = ["CAD program", "code agent", "SWE-bench"]
    assert sources.keyword_hit("A Code Agent for X", kws)
    assert sources.keyword_hit("evaluated on swe-bench verified", kws)
    assert not sources.keyword_hit("decade programs are cascaded", kws)


def test_seen_roundtrip():
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        assert storage.load_seen(d) == set()
        storage.save_seen({"2601.00001", "x"}, d)
        assert storage.load_seen(d) == {"2601.00001", "x"}


def _entries(n=3):
    return [
        {"paper": {"id": f"260{i}.0000{i}", "title": f"P{i}", "authors": ["A"],
                   "venue": "arXiv 2026/01", "links": {"paper": "u"}},
         "category": "software_debugging", "tags": [], "summary": "S.", "reason": "R."}
        for i in range(1, n + 1)
    ]


def test_issue_body_payload_roundtrip():
    body = reviewflow.build_issue_body(_entries(), note="test note")
    m = reviewflow._PAYLOAD_RE.search(body)
    assert m
    import json
    assert json.loads(m.group(1)) == _entries()
    assert "### 2. P2" in body


def _comment(login, body):
    return {"user": {"login": login}, "body": body}


def test_parse_decisions_protocol():
    comments = [
        _comment("stranger", "/approve all"),  # ignored: not the reviewer
        _comment("owner", "/approve 1,3"),
        _comment("owner", "/edit 2 category=web tags=benchmark,model"),
        _comment("owner", "/reject 3"),  # later command overrides the earlier approve
    ]
    d = reviewflow.parse_decisions(comments, "owner", 3)
    assert d[1] == ("approve", {})
    assert d[2] == ("approve", {"category": "web", "tags": ["benchmark", "model"]})
    assert d[3] == ("reject", {})


def test_parse_decisions_ranges_and_all():
    d = reviewflow.parse_decisions([_comment("o", "/approve 1-2")], "o", 3)
    assert set(d) == {1, 2}
    d = reviewflow.parse_decisions([_comment("o", "/reject all")], "o", 3)
    assert all(v[0] == "reject" for v in d.values()) and len(d) == 3
    d = reviewflow.parse_decisions([_comment("o", "/edit 2 tags=-")], "o", 3)
    assert d[2] == ("approve", {"tags": []})
    d = reviewflow.parse_decisions([_comment("o", "no commands here")], "o", 3)
    assert d == {}
