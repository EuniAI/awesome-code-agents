"""Tests for sources parsing/filtering and the review command protocol (no network)."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from automation import config, reviewflow, sources, storage

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


_OAI_FEED = b"""<?xml version="1.0" encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/">
  <ListRecords>
    <record>
      <header><datestamp>2026-07-10</datestamp></header>
      <metadata>
        <arXiv xmlns="http://arxiv.org/OAI/arXiv/">
          <id>2607.05432</id>
          <created>2026-07-08</created>
          <authors><author><keyname>Doe</keyname><forenames>Jane</forenames></author></authors>
          <title>An Agent
            that Codes</title>
          <categories>cs.SE cs.AI</categories>
          <abstract> Abstract body. Accepted at ICSE 2027. </abstract>
        </arXiv>
      </metadata>
    </record>
    <resumptionToken>tok123</resumptionToken>
  </ListRecords>
</OAI-PMH>"""


def test_oai_feed_parsing():
    root_records, token = sources._oai_parse(_OAI_FEED)
    (paper, abstract, cats, announced), = root_records
    assert paper.id == "2607.05432"
    assert paper.title == "An Agent that Codes"
    assert paper.authors == ["Jane Doe"]
    assert paper.published == "2026-07-08"
    assert paper.venue == "ICSE 2027"  # extracted from the acceptance phrase
    assert cats == {"cs.SE", "cs.AI"}
    assert abstract.startswith("Abstract body.")
    assert announced == "2026-07-10"  # datestamp = announcement day
    assert token == "tok123"


def test_harvest_ledger_roundtrip():
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        assert storage.load_harvest_cursor(d) == ""
        storage.record_harvest({"2026-07-10": 861, "2026-07-11": 0}, cursor="2026-07-12", data_dir=d)
        storage.record_harvest({"2026-07-12": 40}, data_dir=d)  # merge, cursor kept
        ledger = storage.load_harvest(d)
        assert ledger["cursor"] == "2026-07-12"
        assert ledger["days"] == {"2026-07-10": 861, "2026-07-11": 0, "2026-07-12": 40}


def test_keyword_hit_respects_word_boundaries():
    kws = ["CAD program", "code agent", "SWE-bench"]
    assert sources.keyword_hit("A Code Agent for X", kws)
    assert sources.keyword_hit("evaluated on swe-bench verified", kws)
    assert not sources.keyword_hit("decade programs are cascaded", kws)


def test_keyword_hit_is_plural_tolerant():
    kws = ["code agent", "language model"]
    assert sources.keyword_hit("a study of code agents", kws)
    assert sources.keyword_hit("large language models are used", kws)


def test_recall_gate_signal_times_domain():
    recall = {
        "strong": ["SWE-bench", "program synthesis"],
        "signal": ["agent", "LLM", "language model"],
        "domain": ["terminal environment", "operating system", "web browser"],
    }
    # strong phrase alone passes
    assert sources.recall_hit("Evaluated on SWE-bench Verified", recall)
    # signal x domain passes, including the exact variant that used to be missed
    assert sources.recall_hit("An LLM agent acting in a terminal environment", recall)
    assert sources.recall_hit("Agents operating across terminal environments", recall)
    # domain without a signal does NOT pass (no agent/model context)
    assert not sources.recall_hit("A survey of terminal environments for HPC", recall)
    # signal without a domain does NOT pass
    assert not sources.recall_hit("An autonomous LLM agent for planning", recall)
    # a non-code sense of a domain word never passes (no signal, wrong phrase)
    assert not sources.recall_hit("Prognosis of terminal illness in patients", recall)


def test_repo_recall_config_covers_the_gate():
    recall = config.load()["arxiv"]["recall"]
    assert recall["strong"] and recall["signal"] and recall["domain"]
    # the owner's motivating case now recalls end to end through the real config
    assert sources.recall_hit(
        "A coding agent that navigates terminal environments", recall)
    assert not sources.recall_hit("Managing a patient's terminal illness", recall)


def test_seen_roundtrip():
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        assert storage.load_seen(d) == set()
        storage.save_seen({"2601.00001", "x"}, d)
        assert storage.load_seen(d) == {"2601.00001", "x"}


def test_retry_counts_roundtrip():
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        assert storage.load_retry_counts(d) == {}
        storage.save_retry_counts({"2601.00002": 2, "2601.00001": 1}, d)
        assert storage.load_retry_counts(d) == {"2601.00001": 1, "2601.00002": 2}


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


def test_parse_decisions_trailing_reason_and_venue():
    # A free-text reason after the indices must not swallow the command.
    d = reviewflow.parse_decisions([_comment("o", "/reject 2 wrong topic")], "o", 3)
    assert d == {2: ("reject", {"reason": "wrong topic"})}
    # Venue values may contain spaces; a following key= ends the value.
    d = reviewflow.parse_decisions(
        [_comment("o", "/edit 1 venue=ICSE 2026 tags=benchmark")], "o", 3)
    assert d[1] == ("approve", {"venue": "ICSE 2026", "tags": ["benchmark"]})


def test_parse_decisions_mixed_line_and_case_insensitive_login():
    # Several commands on one line, applied in positional order (legacy protocol).
    d = reviewflow.parse_decisions(
        [_comment("Owner", "/approve 1,3 /reject 2 wrong topic /edit 3 venue=FSE 2027")],
        "owner", 3)
    assert d[1] == ("approve", {})
    assert d[2] == ("reject", {"reason": "wrong topic"})
    assert d[3] == ("approve", {"venue": "FSE 2027"})
    # An edit followed by a newline command keeps its value bounded to the line.
    d = reviewflow.parse_decisions(
        [_comment("OWNER", "/edit 2 venue=ICSE 2026\n/approve 1")], "owner", 3)
    assert d[2] == ("approve", {"venue": "ICSE 2026"})
    assert d[1] == ("approve", {})


def test_inbox_id_extraction_handles_bare_ids():
    text = ("see https://arxiv.org/abs/2601.11111v2 and also 2602.22222 please, "
            "but not version digits like 1.5 or 2601.11111 again")
    assert sources._extract_inbox_ids(text) == ["2601.11111", "2602.22222"]


def test_extract_venue():
    assert sources.extract_venue(
        "We do X. Accepted at ICSE 2026.", "arXiv 2026/01") == "ICSE 2026"
    assert sources.extract_venue(
        "This paper will appear in NeurIPS 2025 proceedings... wait no.",
        "arXiv 2026/01").startswith("NeurIPS")
    assert sources.extract_venue("No acceptance mentioned.", "arXiv 2026/01") == "arXiv 2026/01"
