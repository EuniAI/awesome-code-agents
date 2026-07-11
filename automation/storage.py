"""
The single owner of the data/ layout.

One YAML file per taxonomy leaf: data/papers_{leaf}.yaml, newest first. Each record
also carries its `category` field, so re-classification is a field change plus a
save, never manual file surgery. Identity and dedup key is Paper.id.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

import yaml

from automation.models import Paper

_REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = _REPO_ROOT / "data"


def path_for(key: str, data_dir: Path = DATA_DIR) -> Path:
    return data_dir / f"papers_{key}.yaml"


def load(key: str, data_dir: Path = DATA_DIR) -> list[Paper]:
    """Papers of one leaf; a missing file is an empty category."""
    path = path_for(key, data_dir)
    if not path.exists():
        return []
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(raw, list):
        raise ValueError(f"{path} must contain a YAML list")
    papers = [Paper.from_dict(d) for d in raw]
    for p in papers:
        p.category = p.category or key
    return papers


def save(key: str, papers: list[Paper], data_dir: Path = DATA_DIR) -> None:
    """Write one leaf's papers (callers keep newest-first order).

    Id is identity, so a file must never hold two entries with the same id.
    Dedup here (keep first) is a safety net against caller bugs, logged loudly.
    """
    data_dir.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    deduped: list[Paper] = []
    for p in papers:
        if p.id in seen:
            logging.getLogger(__name__).warning("dropping duplicate id %s in %s", p.id, key)
            continue
        seen.add(p.id)
        deduped.append(p)
    papers = deduped
    text = yaml.dump(
        [p.to_dict() for p in papers],
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    )
    path_for(key, data_dir).write_text(text, encoding="utf-8")


def add(paper: Paper, data_dir: Path = DATA_DIR) -> bool:
    """Prepend one paper to its category file; False if its id already exists there."""
    if not paper.category:
        raise ValueError(f"Paper has no category: {paper.title!r}")
    existing = load(paper.category, data_dir)
    if any(p.id == paper.id for p in existing):
        return False
    save(paper.category, [paper] + existing, data_dir)
    return True


def all_ids(leaf_keys: list[str], data_dir: Path = DATA_DIR) -> set[str]:
    """Every stored paper id across the given leaves (the global dedup set)."""
    ids: set[str] = set()
    for key in leaf_keys:
        ids.update(p.id for p in load(key, data_dir))
    return ids


def newest_first(papers: list[Paper]) -> list[Paper]:
    """Sort newest first by first-publication date (arXiv v1). Fallback when
    `published` is empty: an 'arXiv YYYY/MM' venue, then any year in the venue;
    undated papers sink to the end. Stable within equal keys."""
    import re as _re

    def key(p: Paper) -> str:
        if p.published:
            return p.published
        m = _re.search(r"arXiv (\d{4})/(\d{2})", p.venue)
        if m:
            return f"{m.group(1)}-{m.group(2)}-00"
        m = _re.search(r"(20\d{2})", p.venue)
        if m:
            return f"{m.group(1)}-00-00"
        return "0000"

    return sorted(papers, key=key, reverse=True)


# ── Seen ids (pipeline state) ─────────────────────────────────────────────────
# The whole pipeline state is one committed file: ids the pipeline has already
# handled (proposed for review or auto-skipped as out of scope). Curated papers
# live in the data files; pending proposals live in the open review issue.

def _seen_path(data_dir: Path = DATA_DIR) -> Path:
    return data_dir / "seen.json"


def load_seen(data_dir: Path = DATA_DIR) -> set[str]:
    path = _seen_path(data_dir)
    if not path.exists():
        return set()
    return set(json.loads(path.read_text(encoding="utf-8")))


def save_seen(seen: set[str], data_dir: Path = DATA_DIR) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    _seen_path(data_dir).write_text(
        json.dumps(sorted(seen), indent=1) + "\n", encoding="utf-8"
    )


# ── Abstract sidecar ──────────────────────────────────────────────────────────
# Raw source material (id -> abstract), kept out of the human-facing curated YAML.
# Fetched once, reused forever: re-classification, golden-set evals, future search.

def _abstracts_path(data_dir: Path = DATA_DIR) -> Path:
    return data_dir / "abstracts.json"


def load_abstracts(data_dir: Path = DATA_DIR) -> dict[str, str]:
    path = _abstracts_path(data_dir)
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_abstracts(abstracts: dict[str, str], data_dir: Path = DATA_DIR) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    _abstracts_path(data_dir).write_text(
        json.dumps(abstracts, indent=1, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
