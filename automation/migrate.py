"""
Migration tooling: re-classify the legacy corpus into the new taxonomy.

Reads paper facts (title/authors/venue/links) from `_legacy/data/`, fetches
abstracts from arXiv once into the sidecar (data/abstracts.json), classifies
with automation.classify, and writes human-review sheets under
redesign/migration/. Nothing is written to the new data/ files until the owner
approves a bucket.

Usage:
  python -m automation.migrate calibrate     # mixed ~34-paper calibration batch
"""

from __future__ import annotations

import argparse
import logging
import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from automation import classify, storage
from automation.models import Classification, Paper

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[1]
LEGACY_DATA = _REPO_ROOT / "_legacy" / "data"
REVIEW_DIR = _REPO_ROOT / "redesign" / "migration"

_ARXIV_ID = re.compile(r"^\d{4}\.\d{4,5}$")
_ATOM = {"a": "http://www.w3.org/2005/Atom"}


# ── Legacy corpus access ──────────────────────────────────────────────────────

def load_legacy(old_key: str) -> list[Paper]:
    return storage.load(old_key, data_dir=LEGACY_DATA)


# ── Abstracts: fetch once, reuse forever ──────────────────────────────────────

def ensure_abstracts(ids: list[str]) -> dict[str, str]:
    """Return id->abstract for arXiv ids, fetching missing ones into the sidecar."""
    cache = storage.load_abstracts()
    missing = [i for i in ids if _ARXIV_ID.match(i) and i not in cache]
    for chunk_start in range(0, len(missing), 50):
        chunk = missing[chunk_start:chunk_start + 50]
        url = "https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(chunk)
        logger.info("fetching %d abstracts from arXiv", len(chunk))
        with urllib.request.urlopen(url, timeout=60) as r:
            root = ET.fromstring(r.read())
        for entry in root.findall("a:entry", _ATOM):
            eid = entry.find("a:id", _ATOM).text or ""
            m = re.search(r"abs/(\d{4}\.\d{4,5})", eid)
            summary = entry.find("a:summary", _ATOM)
            if m and summary is not None:
                cache[m.group(1)] = re.sub(r"\s+", " ", summary.text or "").strip()
        time.sleep(3)  # arXiv rate courtesy
    if missing:
        storage.save_abstracts(cache)
    return cache


def _classify_input(paper: Paper, abstracts: dict[str, str]) -> dict[str, str]:
    abstract = abstracts.get(paper.id, "")
    if not abstract:
        # Non-arXiv or fetch miss: fall back to the curator summary from the old data.
        abstract = f"(no abstract available; curator summary:) {paper.summary}"
    return {"id": paper.id, "title": paper.title, "abstract": abstract}


# ── Calibration batch ─────────────────────────────────────────────────────────

# (old_key, how_many): a deliberate mix of clean buckets (sanity) and the messy
# buckets that motivated the redesign (the real test).
CALIBRATION_MIX: list[tuple[str, int]] = [
    ("sql_engineering", 2), ("hardware_engineering", 1), ("code_executing_embodied", 2),
    ("code_executing_web", 2), ("pull_request_review", 1), ("qa", 1), ("3d_object_design", 2),
    ("code_generation", 5), ("issue_resolution", 5), ("terminal", 3),
    ("foundation_models", 2), ("data_synthesis", 3), ("multimodal_coding", 2),
    ("machine_learning_engineering", 2), ("agentic_visualization", 1),
]


def _spread(items: list[Paper], k: int) -> list[Paper]:
    """k papers evenly spread through the bucket (deterministic, no RNG)."""
    if len(items) <= k:
        return items
    step = len(items) / k
    return [items[int(i * step)] for i in range(k)]


def run_calibration(model: str = classify.MODEL) -> Path:
    sample: list[tuple[str, Paper]] = []
    for old_key, k in CALIBRATION_MIX:
        for p in _spread(load_legacy(old_key), k):
            sample.append((old_key, p))
    logger.info("calibration sample: %d papers", len(sample))

    abstracts = ensure_abstracts([p.id for _, p in sample])
    items = [_classify_input(p, abstracts) for _, p in sample]
    verdicts = classify.classify(items, model=model)

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = REVIEW_DIR / "calibration.md"
    out.write_text(_review_sheet(sample, verdicts, model), encoding="utf-8")
    return out


def _review_sheet(sample: list[tuple[str, Paper]], verdicts: list[Classification], model: str) -> str:
    lines = [
        "# Migration calibration batch",
        "",
        f"{len(sample)} papers, mixed clean/messy old buckets, classified by `{model}`.",
        "Review guide: `->` marks the proposed new leaf; `OUT` means proposed as out of",
        "scope; `FAILED` means the classifier gave no valid verdict. Reply with",
        "corrections by row number.",
        "",
        "| # | old bucket | proposed | tags | title | reason |",
        "|---|---|---|---|---|---|",
    ]
    for i, ((old, p), v) in enumerate(zip(sample, verdicts), 1):
        if v.failed:
            proposed = "FAILED"
        elif not v.relevant:
            proposed = "OUT"
        else:
            proposed = v.category
        title = p.title[:70].replace("|", "/")
        reason = v.reason[:110].replace("|", "/")
        tags = ",".join(v.tags) or "-"
        lines.append(f"| {i} | {old} | **{proposed}** | {tags} | {title} | {reason} |")
    return "\n".join(lines) + "\n"


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-7s %(message)s")
    parser = argparse.ArgumentParser(description="Legacy corpus migration tooling")
    parser.add_argument("command", choices=["calibrate"])
    args = parser.parse_args()
    if args.command == "calibrate":
        path = run_calibration()
        print(f"review sheet written: {path}")


if __name__ == "__main__":
    main()
