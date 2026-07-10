"""
Operational configuration only (repo, inbox, arxiv, llm, schedule).
Category definitions live in taxonomy.json, never here.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = _REPO_ROOT / "automation" / "config.yaml"


@lru_cache(maxsize=1)
def load(path: Path = CONFIG_PATH) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))
