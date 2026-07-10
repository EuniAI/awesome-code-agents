#!/usr/bin/env python3
import os
import re
import json
from glob import glob
import datetime


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_ROOT, "data")
BADGE_DIR = os.path.join(REPO_ROOT, "docs", "static", "badges")

README_PATH = os.path.join(REPO_ROOT, "README.md")
START = r"<!-- START PAPERS SUMMARY -->"
END = r"<!-- END PAPERS SUMMARY -->"


def count_papers_from_yaml_file(file_path: str) -> int:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Count entries that start a list item with a title field
    # Example:
    # - title: "..."
    matches = re.findall(r"^\s*-\s*title\s*:\s*", content, flags=re.MULTILINE)
    return len(matches)


def count_all_papers(data_dir: str) -> int:
    total = 0
    for file_path in sorted(glob(os.path.join(data_dir, "*.yaml"))):
        total += count_papers_from_yaml_file(file_path)
    return total


def write_files(total_papers: int) -> None:
    os.makedirs(BADGE_DIR, exist_ok=True)

    # Write shields.io endpoint JSON (the header badge reads this).
    json_path = os.path.join(BADGE_DIR, "papers.json")
    endpoint = {
        "schemaVersion": 1,
        "label": "Papers",
        "message": str(total_papers),
        "color": "brightgreen",
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(endpoint, f)
        f.write("\n")


def update_readme_summary(total_papers: int) -> None:
    if not os.path.exists(README_PATH):
        return
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    today = datetime.date.today().isoformat()
    # summary = (
    #     f"**We actively track the latest agent research and keep this list updated. "
    #     f"Currently indexed: `{total_papers}` papers.** *(Last update: {today})*"
    # )
    summary = (
        f"🔥 **We are actively tracking the frontier research of code agents.**<br>\n"
        f"🧹 *We periodically curate our collection, retaining only published papers and interesting arXiv preprints from the last six months.*<br>\n"
        f"📚 *Currently collected:* **`{total_papers}` papers.** *(Last update: {today})*"
    )

    pattern = re.compile(
        rf"({START})(.*)({END})",
        flags=re.DOTALL
    )
    new_content = pattern.sub(rf"\1\n{summary}\n\3", content)

    if new_content != content:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)


def main() -> None:
    total = count_all_papers(DATA_DIR)
    write_files(total)
    update_readme_summary(total)
    print(f"Total papers: {total}")


if __name__ == "__main__":
    main()
