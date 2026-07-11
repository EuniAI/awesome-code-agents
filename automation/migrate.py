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
import urllib.parse
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
    # Primary sources only: never feed the old pipeline's second-hand summaries.
    abstract = abstracts.get(paper.id, "") or "(abstract unavailable; judge from the title alone)"
    return {"id": paper.id, "title": paper.title, "abstract": abstract}


def _norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", t.lower())


def search_arxiv_by_title(title: str) -> str | None:
    """Find a paper's arXiv abstract by exact-ish title match; None if absent."""
    q = urllib.parse.quote(f'ti:"{title}"')
    url = f"https://export.arxiv.org/api/query?search_query={q}&max_results=5"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            root = ET.fromstring(r.read())
    except Exception as exc:
        logger.warning("arxiv title search failed for %r: %s", title[:50], exc)
        return None
    want = _norm_title(title)
    for entry in root.findall("a:entry", _ATOM):
        got = _norm_title(entry.find("a:title", _ATOM).text or "")
        if got == want or got.startswith(want) or want.startswith(got):
            summary = entry.find("a:summary", _ATOM)
            if summary is not None and summary.text:
                return re.sub(r"\s+", " ", summary.text).strip()
    return None


def fetch_landing_abstract(url: str) -> str | None:
    """Best-effort abstract extraction from a paper's landing page (meta tags, ACL div)."""
    if not url.startswith("http"):
        return None
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (paper-metadata-fetch)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", errors="replace")
    except Exception as exc:
        logger.warning("landing fetch failed for %s: %s", url[:60], exc)
        return None
    for pattern in (
        r'name="citation_abstract"\s+content="([^"]{100,})"',
        r'property="og:description"\s+content="([^"]{100,})"',
        r'class="[^"]*acl-abstract[^"]*"[^>]*>\s*(?:<[^>]+>)*([^<]{100,})',
    ):
        m = re.search(pattern, html, re.DOTALL)
        if m:
            import html as _html
            return re.sub(r"\s+", " ", _html.unescape(m.group(1))).strip()
    return None


def ensure_primary_abstracts(papers: list[Paper]) -> dict[str, str]:
    """Primary-source abstracts for any papers: arXiv id -> arXiv title search ->
    landing page. Results cached in the sidecar under each paper's id."""
    cache = storage.load_abstracts()
    arxiv_ids = [p.id for p in papers if _ARXIV_ID.match(p.id)]
    if any(i not in cache for i in arxiv_ids):
        cache = ensure_abstracts(arxiv_ids)
    changed = False
    for p in papers:
        if p.id in cache or _ARXIV_ID.match(p.id):
            continue
        ab = search_arxiv_by_title(p.title)
        time.sleep(3)
        if not ab:
            ab = fetch_landing_abstract(p.links.get("paper", ""))
        if ab:
            cache[p.id] = ab
            changed = True
            logger.info("recovered abstract for: %s", p.title[:60])
        else:
            logger.info("no primary abstract found: %s", p.title[:60])
    if changed:
        storage.save_abstracts(cache)
    return cache


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
    ("Tree-of-Code", ("world_general", [])),
    ("Chain-of-Modality", ("world_physical", [])),
    ("SWE-Compass", ("software_debugging", ["benchmark"])),
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

    ruled: list[tuple[Paper, tuple[str, list[str]] | None]] = []
    to_classify: list[Paper] = []
    for p in affected:
        hit, ruling = _override_for(p.title)
        if hit:
            ruled.append((p, ruling))
        else:
            to_classify.append(p)
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

    for p, ruling in ruled:
        if ruling is None:
            apply(p, None, [], "", "owner ruling")
        else:
            apply(p, ruling[0], ruling[1], "", "owner ruling")
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
    # Owner rulings are ground truth and override the classifier.
    ruled = {p.id: _override_for(p.title)[1] for _, p in subjects if _override_for(p.title)[0]}
    papers = [p for _, p in subjects if p.id not in ruled]
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


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-7s %(message)s")
    parser = argparse.ArgumentParser(description="Legacy corpus migration tooling")
    parser.add_argument("command", choices=["calibrate", "run", "dates", "refetch", "reclass"])
    parser.add_argument("keys", nargs="*", help="leaf keys to reclassify (for reclass)")
    args = parser.parse_args()
    if args.command == "calibrate":
        print(f"review sheet written: {run_calibration()}")
    elif args.command == "run":
        print(f"review sheet written: {run_full()}")
    elif args.command == "refetch":
        print(f"review sheet written: {refetch_reclassify()}")
    elif args.command == "reclass":
        keys = args.keys or ["software_general", "world_general"]
        print(f"review sheet written: {reclassify_leaves(keys)}")
    else:
        backfill_dates()


if __name__ == "__main__":
    main()
