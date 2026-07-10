#!/usr/bin/env python3
"""Thin shim kept for existing callers (cron, git_push). Real logic: automation/render.py."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation.render import main

if __name__ == "__main__":
    main()
