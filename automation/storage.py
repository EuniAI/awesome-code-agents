"""
The single owner of the data/ file layout.

One YAML file per taxonomy leaf: data/papers_{key}.yaml, newest first.
A missing file means an empty category (legitimate for new categories and
during migration); malformed YAML is an error, not an empty list.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = _REPO_ROOT / "data"

REQUIRED_ENTRY_KEYS = ("title", "authors", "venue", "links")


def path_for(key: str) -> Path:
    return DATA_DIR / f"papers_{key}.yaml"


def load_entries(key: str) -> list[dict[str, Any]]:
    path = path_for(key)
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a YAML list")
    for i, entry in enumerate(data):
        if not isinstance(entry, dict):
            raise ValueError(f"{path} entry {i} is not a mapping")
        missing = [k for k in REQUIRED_ENTRY_KEYS if k not in entry]
        if missing:
            raise ValueError(f"{path} entry {i} missing keys: {missing}")
    return data
