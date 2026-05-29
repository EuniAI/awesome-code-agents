"""Loads and caches config.yaml from the automation directory."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import yaml

_CONFIG_PATH = Path(__file__).parent / "config.yaml"


@lru_cache(maxsize=1)
def load_config() -> dict:
    with open(_CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_config(cfg: dict) -> None:
    """Write back a modified config (e.g. to persist inbox issue number)."""
    _CONFIG_PATH.write_text(
        yaml.dump(cfg, allow_unicode=True, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )
    load_config.cache_clear()
