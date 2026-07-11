"""
Operational configuration. A key exists here only when a live module consumes it
(currently: repo identity and the inbox issue number). Category definitions live in
taxonomy.json, never here; arxiv crawl settings return when sources.py is rebuilt.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = Path(__file__).resolve().parent / "data" / "config.yaml"


@lru_cache(maxsize=1)
def load(path: Path = CONFIG_PATH) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))
