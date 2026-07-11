"""
Paper-count surfaces: the shields endpoint JSON and the README summary block.
"""

from __future__ import annotations

import datetime
import json
import re
from pathlib import Path

from automation import storage, taxonomy

_REPO_ROOT = Path(__file__).resolve().parents[1]
BADGE_JSON = _REPO_ROOT / "docs" / "static" / "badges" / "papers.json"
README = _REPO_ROOT / "README.md"

_SUMMARY_RE = re.compile(
    r"<!-- START PAPERS SUMMARY -->.*?<!-- END PAPERS SUMMARY -->", re.DOTALL
)


def total_papers() -> int:
    return sum(len(storage.load(k)) for k in taxonomy.load().leaf_keys())


def refresh() -> int:
    total = total_papers()

    BADGE_JSON.parent.mkdir(parents=True, exist_ok=True)
    BADGE_JSON.write_text(
        json.dumps({"schemaVersion": 1, "label": "Papers", "message": str(total),
                    "color": "brightgreen"}) + "\n",
        encoding="utf-8",
    )

    today = datetime.date.today().isoformat()
    summary = (
        "<!-- START PAPERS SUMMARY -->\n"
        "🔥 **We are actively tracking the frontier research of code agents.**<br>\n"
        "🧹 *The main list below shows papers from the last twelve months; everything "
        "older lives in the [full archive](ARCHIVE.md), so nothing is ever lost.*<br>\n"
        f"📚 *Currently collected:* **`{total}` papers.** *(Last update: {today})*\n"
        "<!-- END PAPERS SUMMARY -->"
    )
    content = README.read_text(encoding="utf-8")
    new_content = _SUMMARY_RE.sub(summary, content)
    if new_content != content:
        README.write_text(new_content, encoding="utf-8")
    return total
