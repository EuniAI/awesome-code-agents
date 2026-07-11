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
from pathlib import Path

from automation import classify, storage
from automation.models import Classification, Paper
from automation.sources import (  # all arXiv/network logic lives in sources
    ARXIV_ID as _ARXIV_ID,
    ensure_abstracts,
    ensure_primary_abstracts,
    fetch_arxiv_papers,
    fetch_published,
)

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[1]
LEGACY_DATA = _REPO_ROOT / "_legacy" / "data"
REVIEW_DIR = _REPO_ROOT / "redesign" / "migration"


# ── Legacy corpus access ──────────────────────────────────────────────────────

def load_legacy(old_key: str) -> list[Paper]:
    return storage.load(old_key, data_dir=LEGACY_DATA)


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
    # Primary sources only: never feed the old pipeline's second-hand summaries.
    abstract = abstracts.get(paper.id, "") or "(abstract unavailable; judge from the title alone)"
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
# Owner rulings are no longer hard overrides. They now live in calibration.json as
# positive/negative few-shot examples (see classify._calibration_block): they guide
# the classifier by precedent instead of pinning specific papers by title.

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


def run_full(model: str = classify.MODEL) -> Path:
    from automation import badges, render, taxonomy

    leaves = taxonomy.load().leaf_keys()
    store: dict[str, list[Paper]] = {k: storage.load(k) for k in leaves}
    seen: set[str] = {p.id for ps in store.values() for p in ps}

    report: list[str] = ["# Full migration run", ""]
    removed: list[str] = []
    failed: list[str] = []
    totals = {"placed": 0, "out": 0, "failed": 0, "dup": 0}

    for bucket in BUCKET_ORDER:
        papers = [p for p in load_legacy(bucket) if p.id not in seen]
        dup_count = len(load_legacy(bucket)) - len(papers)
        totals["dup"] += dup_count
        if not papers:
            continue
        logger.info("=== bucket %s: %d papers (%d dups skipped) ===", bucket, len(papers), dup_count)

        to_classify = papers
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
        f"failed {totals['failed']}, duplicates skipped {totals['dup']}"
    )

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = REVIEW_DIR / "full-run.md"
    out.write_text("\n".join(report) + "\n", encoding="utf-8")

    render.main()
    badges.refresh()
    return out


def refetch_reclassify(model: str = classify.MODEL) -> Path:
    """Re-evidence and re-classify every legacy paper that had no primary abstract
    at migration time (it was judged from the old pipeline's summary). Applies
    moves/removals/reinstatements to data/ and writes a delta review sheet."""
    from automation import badges, render, taxonomy

    leaves = taxonomy.load().leaf_keys()
    store = {k: storage.load(k) for k in leaves}
    placement: dict[str, str] = {p.id: k for k in leaves for p in store[k]}

    cache_before = set(storage.load_abstracts())
    seen: set[str] = set()
    affected: list[Paper] = []
    for b in BUCKET_ORDER:
        for p in load_legacy(b):
            if p.id in seen:
                continue
            seen.add(p.id)
            if p.id not in cache_before:
                affected.append(p)
    logger.info("papers without primary evidence at migration time: %d", len(affected))

    cache = ensure_primary_abstracts(affected)

    to_classify = affected
    items = [_classify_input(p, cache) for p in to_classify]
    verdicts = classify.classify(items, model=model) if items else []

    rows: list[str] = []

    def apply(p: Paper, new_cat: str | None, tags: list[str], summary: str, reason: str) -> None:
        before = placement.get(p.id, "OUT")
        evidence = "primary" if p.id in cache else "title-only"
        after = new_cat or "OUT"
        if before != "OUT" and new_cat is None:
            store[before] = [x for x in store[before] if x.id != p.id]
        elif new_cat is not None:
            if before == "OUT":
                p.category, p.tags = new_cat, tags
                if summary:
                    p.summary = summary
                store[new_cat].append(p)
            elif before != new_cat:
                moved = next(x for x in store[before] if x.id == p.id)
                store[before] = [x for x in store[before] if x.id != p.id]
                moved.category, moved.tags = new_cat, tags
                if summary:
                    moved.summary = summary
                store[new_cat].append(moved)
            else:
                cur = next(x for x in store[before] if x.id == p.id)
                cur.tags = tags or cur.tags
                if summary:
                    cur.summary = summary
        mark = "" if before == after else " <- CHANGED"
        rows.append(f"| {before} | **{after}**{mark} | {evidence} | "
                    f"{p.title[:65].replace('|','/')} | {reason[:90].replace('|','/')} |")

    for p, v in zip(to_classify, verdicts):
        if v.failed:
            rows.append(f"| {placement.get(p.id,'OUT')} | FAILED | - | {p.title[:65]} | retry later |")
        else:
            apply(p, v.category if v.relevant else None, v.tags, v.summary, v.reason)

    for k in leaves:
        storage.save(k, storage.newest_first(store[k]))
    render.main()
    badges.refresh()

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = REVIEW_DIR / "refetch-reclass.md"
    out.write_text(
        "# Re-evidence pass: papers previously judged from second-hand summaries\n\n"
        f"{len(affected)} papers re-fetched from primary sources (arXiv title search, "
        "landing pages) and re-classified. Old-pipeline summaries are no longer used "
        "as classification input.\n\n"
        "| before | after | evidence | title | reason |\n|---|---|---|---|---|\n"
        + "\n".join(rows) + "\n",
        encoding="utf-8",
    )
    return out


def reclassify_leaves(keys: list[str], model: str = classify.MODEL) -> Path:
    """Re-classify the current members of the given leaves under the live rules and
    apply the resulting moves (to any leaf, or OUT). Uses primary abstracts already in
    the sidecar; fills any gaps first. Writes a before/after review sheet."""
    from automation import badges, render, taxonomy

    leaves = taxonomy.load(force=True).leaf_keys()
    store = {k: storage.load(k) for k in leaves}
    subjects = [(k, p) for k in keys for p in store[k]]
    placement = {p.id: k for k, p in subjects}
    logger.info("reclassifying %d papers from %s", len(subjects), ", ".join(keys))

    cache = ensure_primary_abstracts([p for _, p in subjects])
    papers = [p for _, p in subjects]
    items = [_classify_input(p, cache) for p in papers]
    verdicts = classify.classify(items, model=model) if items else []

    rows: list[str] = []
    for p, v in zip(papers, verdicts):
        before = placement[p.id]
        after = (v.category if v.relevant else None) or "OUT"
        if v.failed:
            rows.append(f"| {before} | FAILED | {p.title[:62].replace('|','/')} | retry |")
            continue
        if after != before:
            store[before] = [x for x in store[before] if x.id != p.id]
            if after != "OUT":
                p.category, p.tags = v.category, v.tags
                if v.summary:
                    p.summary = v.summary
                store[after].append(p)
        mark = " <- CHANGED" if after != before else ""
        rows.append(f"| {before} | **{after}**{mark} | {p.title[:62].replace('|','/')} | "
                    f"{v.reason[:95].replace('|','/')} |")

    for k in leaves:
        storage.save(k, storage.newest_first(store[k]))
    render.main()
    badges.refresh()

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = REVIEW_DIR / "reclass-general.md"
    changed = sum(1 for r in rows if "CHANGED" in r)
    out.write_text(
        f"# Re-classification under the benchmark-routing rule: {', '.join(keys)}\n\n"
        f"{len(subjects)} papers re-classified with the live taxonomy rules "
        f"(benchmark routing dominates generalist framing; foundation_models split out). "
        f"{changed} moved.\n\n"
        "| before | after | title | reason |\n|---|---|---|---|\n"
        + "\n".join(rows) + "\n",
        encoding="utf-8",
    )
    return out


def process_inbox(model: str = classify.MODEL) -> Path:
    """Read arXiv links from the inbox issue, classify those not already in the corpus
    under the live rules, and add the relevant ones. Writes a review sheet."""
    import json
    import subprocess

    from automation import badges, config, render, taxonomy

    cfg = config.load()
    owner, repo = cfg["repo"]["owner"], cfg["repo"]["name"]
    issue = cfg["inbox"]["issue_number"]

    raw = subprocess.run(
        ["gh", "api", "--paginate", f"repos/{owner}/{repo}/issues/{issue}/comments"],
        capture_output=True, text=True, timeout=120,
    )
    if raw.returncode != 0:
        raise RuntimeError(f"gh api failed: {raw.stderr[:300]}")
    # gh --paginate merges array-endpoint pages into a single JSON array.
    comments = json.loads(raw.stdout)
    inbox_ids: list[str] = []
    for c in comments:
        for mm in re.findall(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", c.get("body", ""), re.I):
            if mm not in inbox_ids:
                inbox_ids.append(mm)
    logger.info("inbox: %d unique arXiv ids across %d comments", len(inbox_ids), len(comments))

    leaves = taxonomy.load(force=True).leaf_keys()
    have = storage.all_ids(leaves)
    new_ids = [i for i in inbox_ids if i not in have]
    logger.info("inbox: %d already in corpus, %d new to classify", len(inbox_ids) - len(new_ids), len(new_ids))

    papers_by_id = fetch_arxiv_papers(new_ids)
    papers = [papers_by_id[i] for i in new_ids if i in papers_by_id]
    cache = storage.load_abstracts()

    to_classify = papers
    items = [_classify_input(p, cache) for p in to_classify]
    verdicts = classify.classify(items, model=model) if items else []

    store = {k: storage.load(k) for k in leaves}
    rows: list[str] = []
    added = 0

    def place(p: Paper, cat: str | None, tags: list[str], summary: str, reason: str) -> None:
        nonlocal added
        if cat:
            p.category, p.tags = cat, tags
            if summary:
                p.summary = summary
            store[cat].append(p)
            added += 1
        rows.append(f"| **{cat or 'OUT'}** | {p.title[:62].replace('|','/')} | "
                    f"{reason[:95].replace('|','/')} |")

    for p, v in zip(to_classify, verdicts):
        if v.failed:
            rows.append(f"| FAILED | {p.title[:62].replace('|','/')} | retry |")
        else:
            place(p, v.category if v.relevant else None, v.tags, v.summary, v.reason)

    for k in leaves:
        storage.save(k, storage.newest_first(store[k]))
    render.main()
    badges.refresh()

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = REVIEW_DIR / "inbox-run.md"
    out.write_text(
        f"# Inbox classification run\n\n"
        f"{len(inbox_ids)} arXiv ids in inbox issue #{issue}; "
        f"{len(inbox_ids) - len(new_ids)} already in corpus; {len(new_ids)} classified; "
        f"{added} added, {len(new_ids) - added} out of scope.\n\n"
        "| category | title | reason |\n|---|---|---|\n" + "\n".join(rows) + "\n",
        encoding="utf-8",
    )
    return out


def process_backlog() -> None:
    """One-off: absorb the old pipeline's stale pending review issues (the ~271
    issues left open when automation paused in 2026-06). Harvests their arXiv ids,
    routes the unhandled papers through the live pipeline into chunked review
    issues (the pool), then closes the old-format issues. Safe to re-run: handled
    ids are seen, and closing an already-closed issue is a no-op."""
    import json as _json
    import subprocess

    from automation import config, pipeline, reviewflow, taxonomy

    state = _json.loads((_REPO_ROOT / "_legacy" / "state" / "processed.json").read_text())
    pending = state["pending_issues"]
    ids: list[str] = []
    for it in pending:
        for a in it.get("arxiv_ids", []):
            if a not in ids:
                ids.append(a)
    known = (storage.all_ids(taxonomy.load().leaf_keys())
             | storage.load_seen() | reviewflow.pending_ids())
    new_ids = [i for i in ids if i not in known]
    logger.info("backlog: %d unique ids in %d stale issues; %d unhandled",
                len(ids), len(pending), len(new_ids))

    papers = list(fetch_arxiv_papers(new_ids).values())
    pipeline.classify_and_propose(papers)

    # New pool issues exist; now retire the old-format ones.
    cfg = config.load()["repo"]
    repo = f"{cfg['owner']}/{cfg['name']}"
    closed = 0
    for it in pending:
        num = it.get("issue_number")
        if not num:
            continue
        proc = subprocess.run(
            ["gh", "api", "--method", "PATCH", f"repos/{repo}/issues/{num}",
             "-f", "state=closed"],
            capture_output=True, text=True, timeout=60,
        )
        if proc.returncode == 0:
            closed += 1
        else:
            logger.warning("could not close old issue #%s: %s", num, proc.stderr[:120])
    logger.info("backlog: closed %d/%d stale issues", closed, len(pending))


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-7s %(message)s")
    parser = argparse.ArgumentParser(description="Legacy corpus migration tooling")
    parser.add_argument("command",
                        choices=["calibrate", "run", "dates", "refetch", "reclass", "inbox", "backlog"])
    parser.add_argument("keys", nargs="*", help="leaf keys to reclassify (for reclass)")
    args = parser.parse_args()
    if args.command == "calibrate":
        print(f"review sheet written: {run_calibration()}")
    elif args.command == "run":
        print(f"review sheet written: {run_full()}")
    elif args.command == "refetch":
        print(f"review sheet written: {refetch_reclassify()}")
    elif args.command == "reclass":
        keys = args.keys or ["studies"]
        print(f"review sheet written: {reclassify_leaves(keys)}")
    elif args.command == "inbox":
        print(f"review sheet written: {process_inbox()}")
    elif args.command == "backlog":
        process_backlog()
    else:
        backfill_dates()


if __name__ == "__main__":
    main()
