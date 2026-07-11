"""
Migration tooling: re-classify the legacy corpus into the new taxonomy.

Reads paper facts (title/authors/venue/links) from `_legacy/data/`, fetches
abstracts from arXiv once into the sidecar (data/abstracts.json), classifies
with automation.classify, and writes human-review sheets under
redesign/migration/. Nothing is written to the new data/ files until the owner
approves a bucket.

Usage:
  python -m automation.migrate calibrate     # mixed ~34-paper calibration batch
  python -m automation.migrate run           # full legacy migration into data/
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


def fetch_published(ids: list[str]) -> dict[str, str]:
    """id -> first-publication date (arXiv v1 <published>), YYYY-MM-DD."""
    dates: dict[str, str] = {}
    arxiv_ids = [i for i in ids if _ARXIV_ID.match(i)]
    for start in range(0, len(arxiv_ids), 50):
        chunk = arxiv_ids[start:start + 50]
        url = "https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(chunk)
        logger.info("fetching %d publication dates from arXiv", len(chunk))
        with urllib.request.urlopen(url, timeout=60) as r:
            root = ET.fromstring(r.read())
        for entry in root.findall("a:entry", _ATOM):
            eid = entry.find("a:id", _ATOM).text or ""
            m = re.search(r"abs/(\d{4}\.\d{4,5})", eid)
            pub = entry.find("a:published", _ATOM)
            if m and pub is not None and pub.text:
                dates[m.group(1)] = pub.text[:10]
        time.sleep(3)
    return dates


def backfill_dates() -> None:
    """Set Paper.published from arXiv v1 dates and sort every leaf newest first."""
    from automation import badges, render, taxonomy

    leaves = taxonomy.load().leaf_keys()
    all_papers = {k: storage.load(k) for k in leaves}
    ids = [p.id for ps in all_papers.values() for p in ps if not p.published]
    dates = fetch_published(ids)
    filled = 0
    for key, papers in all_papers.items():
        for p in papers:
            if not p.published and p.id in dates:
                p.published = dates[p.id]
                filled += 1
        storage.save(key, storage.newest_first(papers))
    logger.info("published dates filled: %d; all leaves re-sorted newest first", filled)
    render.main()
    badges.refresh()


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


# ── Full migration ────────────────────────────────────────────────────────────

# Owner rulings from the calibration review (redesign/migration/calibration.md).
# Matched by title fragment; None = out of scope, else (category, tags).
RULING_OVERRIDES: list[tuple[str, tuple[str, list[str]] | None]] = [
    ("Robo-Blocks", None),
    ("Tree-of-Code", None),
    ("Can LLMs Replace Manual Annotation", None),
    ("Multi-Agent Collaboration via Evolving Orchestration", None),
    ("Code as Agent Harness", ("world_general", ["survey"])),
    ("GitTaskBench", ("world_general", ["benchmark"])),
    ("PithTrain", ("systems", ["benchmark"])),
    ("SlopCodeBench", ("software_development", ["benchmark"])),
    ("Learning CLI Agents with Structured Action Credit", ("world_terminal", [])),
    ("VisCodex", ("software_code_generation", ["model", "training-data", "benchmark"])),
]

# Processing order: clean buckets first, then the messy ones.
BUCKET_ORDER = [
    "sql_engineering", "hardware_engineering", "system_engineering", "game_generation",
    "software_security_engineering", "pull_request_review", "agentic_fuzzing",
    "code_completion", "qa", "website_generation", "backend_generation",
    "svg_generation", "animation_generation", "3d_object_design",
    "issue_reproduction", "issue_localization", "code_migration",
    "software_refactoring", "performance_optimization", "environment_building",
    "git_management", "feature_development", "code_executing_web",
    "code_executing_game", "code_executing_embodied", "automated_data_science",
    "machine_learning_engineering", "scientific_workflows", "agentic_visualization",
    "terminal", "foundation_models", "data_synthesis", "multimodal_coding",
    "code_generation", "issue_resolution",
]


def _override_for(title: str) -> tuple[bool, tuple[str, list[str]] | None]:
    for frag, ruling in RULING_OVERRIDES:
        if frag.lower() in title.lower():
            return True, ruling
    return False, None


def run_full(model: str = classify.MODEL) -> Path:
    from automation import badges, render, taxonomy

    leaves = taxonomy.load().leaf_keys()
    store: dict[str, list[Paper]] = {k: storage.load(k) for k in leaves}
    seen: set[str] = {p.id for ps in store.values() for p in ps}

    report: list[str] = ["# Full migration run", ""]
    removed: list[str] = []
    failed: list[str] = []
    totals = {"placed": 0, "out": 0, "failed": 0, "dup": 0, "overridden": 0}

    for bucket in BUCKET_ORDER:
        papers = [p for p in load_legacy(bucket) if p.id not in seen]
        dup_count = len(load_legacy(bucket)) - len(papers)
        totals["dup"] += dup_count
        if not papers:
            continue
        logger.info("=== bucket %s: %d papers (%d dups skipped) ===", bucket, len(papers), dup_count)

        # Split off owner-ruled papers; classify the rest.
        ruled: list[tuple[Paper, tuple[str, list[str]] | None]] = []
        to_classify: list[Paper] = []
        for p in papers:
            hit, ruling = _override_for(p.title)
            if hit:
                ruled.append((p, ruling))
            else:
                to_classify.append(p)

        abstracts = ensure_abstracts([p.id for p in to_classify])
        items = [_classify_input(p, abstracts) for p in to_classify]
        verdicts = classify.classify(items, model=model) if items else []

        report.append(f"\n## {bucket}\n")
        report.append("| proposed | tags | title | reason |")
        report.append("|---|---|---|---|")

        def _row(proposed: str, tags: list[str], title: str, reason: str) -> None:
            report.append(
                f"| **{proposed}** | {','.join(tags) or '-'} | "
                f"{title[:70].replace('|', '/')} | {reason[:100].replace('|', '/')} |"
            )

        for p, ruling in ruled:
            totals["overridden"] += 1
            seen.add(p.id)
            if ruling is None:
                totals["out"] += 1
                removed.append(f"- [{bucket}] {p.title} (owner ruling)")
                _row("OUT", [], p.title, "owner ruling (calibration)")
            else:
                cat, tags = ruling
                p.category, p.tags = cat, tags
                store[cat].append(p)
                totals["placed"] += 1
                _row(cat, tags, p.title, "owner ruling (calibration)")

        for p, v in zip(to_classify, verdicts):
            seen.add(p.id)
            if v.failed:
                totals["failed"] += 1
                failed.append(f"- [{bucket}] {p.title}")
                _row("FAILED", [], p.title, "no valid verdict; retry later")
            elif not v.relevant:
                totals["out"] += 1
                removed.append(f"- [{bucket}] {p.title}: {v.reason}")
                _row("OUT", [], p.title, v.reason)
            else:
                p.category, p.tags = v.category, v.tags
                if v.summary:
                    p.summary = v.summary
                store[v.category].append(p)
                totals["placed"] += 1
                _row(v.category, v.tags, p.title, v.reason)

        # Persist incrementally so an interruption loses at most one bucket.
        for key in leaves:
            storage.save(key, store[key])

    report.append("\n## Removed (out of scope)\n")
    report.extend(removed or ["(none)"])
    report.append("\n## Failed (to retry)\n")
    report.extend(failed or ["(none)"])
    report.append(
        f"\n## Totals\nplaced {totals['placed']}, out {totals['out']}, "
        f"failed {totals['failed']}, duplicates skipped {totals['dup']}, "
        f"owner-ruled {totals['overridden']}"
    )

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = REVIEW_DIR / "full-run.md"
    out.write_text("\n".join(report) + "\n", encoding="utf-8")

    render.main()
    badges.refresh()
    return out


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-7s %(message)s")
    parser = argparse.ArgumentParser(description="Legacy corpus migration tooling")
    parser.add_argument("command", choices=["calibrate", "run", "dates"])
    args = parser.parse_args()
    if args.command == "calibrate":
        print(f"review sheet written: {run_calibration()}")
    elif args.command == "run":
        print(f"review sheet written: {run_full()}")
    else:
        backfill_dates()


if __name__ == "__main__":
    main()
