"""
The single owner of the data/ layout.

One YAML file per taxonomy leaf: data/papers_{leaf}.yaml, newest first. Each record
also carries its `category` field, so re-classification is a field change plus a
save, never manual file surgery. Identity and dedup key is Paper.id.
"""

from __future__ import annotations

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
    """Write one leaf's papers (callers keep newest-first order)."""
    data_dir.mkdir(parents=True, exist_ok=True)
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
