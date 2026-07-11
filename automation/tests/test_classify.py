"""Tests for prompt compilation and classification validation (no LLM calls)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from automation import classify, taxonomy


def _items(n=2):
    return [{"id": f"260{i}.0000{i}", "title": f"Paper {i}", "abstract": f"Abstract {i}"} for i in range(n)]


def test_prompt_contains_full_taxonomy_contract():
    prompt = classify.build_prompt(_items())
    tax = taxonomy.load()
    for key in tax.leaf_keys():
        assert f"[{key}]" in prompt, key
    assert "MASTER TEST" in prompt
    assert "PAL/PoT" in prompt                       # scope excludes made it in
    assert "playing the game is agency" in prompt    # boundary lines made it in
    assert "training-data" in prompt
    assert "--- paper 1 ---" in prompt


def _valid_payload(n=2, category="software_debugging"):
    return [
        {"index": i, "relevant": True, "category": category, "tags": ["benchmark"],
         "summary": "S.", "reason": "R."}
        for i in range(n)
    ]


def test_classify_happy_path_with_fake_runner():
    calls = []
    def runner(prompt, schema, model):
        calls.append(model)
        return _valid_payload()
    out = classify.classify(_items(), runner=runner)
    assert len(out) == 2
    assert all(c.category == "software_debugging" and not c.failed for c in out)
    assert calls == [classify.MODEL]


def test_invalid_category_retries_then_marks_failed():
    attempts = []
    def runner(prompt, schema, model):
        attempts.append(1)
        bad = _valid_payload()
        bad[0]["category"] = "not_a_leaf"
        return bad
    out = classify.classify(_items(), runner=runner)
    assert len(attempts) == 2            # one retry
    assert all(c.failed for c in out)


def test_retry_recovers_on_second_attempt():
    attempts = []
    def runner(prompt, schema, model):
        attempts.append(1)
        if len(attempts) == 1:
            raise RuntimeError("transient")
        return _valid_payload()
    out = classify.classify(_items(), runner=runner)
    assert len(attempts) == 2
    assert all(not c.failed for c in out)


def test_tag_rules_enforced():
    # two paper_type tags on one paper is invalid
    def runner(prompt, schema, model):
        bad = _valid_payload()
        bad[1]["tags"] = ["survey", "position"]
        return bad
    out = classify.classify(_items(), runner=runner)
    assert all(c.failed for c in out)


def test_irrelevant_paper_has_no_category():
    def runner(prompt, schema, model):
        return [{"index": 0, "relevant": False, "category": None, "tags": [],
                 "summary": "", "reason": "pure LLM reasoning, out of scope"}]
    out = classify.classify(_items(1), runner=runner)
    assert out[0].relevant is False and out[0].category == "" and not out[0].failed
