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


def approx_text_width(text: str) -> int:
    # Very rough width estimation for SVG text in px
    # Works well enough for shields-like small font sizing
    if not text:
        return 0
    # Digits are a bit wider typically; use 7 for digits, 6 for letters, 5 for punctuation/others
    width = 0
    for ch in text:
        if ch.isdigit():
            width += 7
        elif ch.isalpha():
            width += 6
        else:
            width += 5
    return width


def generate_svg_badge(label: str, message: str, color: str = "#4c1") -> str:
    # Basic shield-style badge (approximation)
    padding_x = 10
    height = 20
    label_width = approx_text_width(label) + padding_x
    value_width = approx_text_width(message) + padding_x
    total_width = label_width + value_width

    # Colors
    label_color = "#555"
    text_color = "#fff"

    svg = f"""
<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"{total_width}\" height=\"{height}\" role=\"img\" aria-label=\"{label}: {message}\">
  <title>{label}: {message}</title>
  <linearGradient id=\"s\" x2=\"0\" y2=\"100%\">
    <stop offset=\"0\" stop-color=\"#bbb\" stop-opacity=\".1\"/>
    <stop offset=\"1\" stop-opacity=\".1\"/>
  </linearGradient>
  <clipPath id=\"r\"><rect width=\"{total_width}\" height=\"{height}\" rx=\"3\" fill=\"#fff\"/></clipPath>
  <g clip-path=\"url(#r)\">
    <rect width=\"{label_width}\" height=\"{height}\" fill=\"{label_color}\"/>
    <rect x=\"{label_width}\" width=\"{value_width}\" height=\"{height}\" fill=\"{color}\"/>
    <rect width=\"{total_width}\" height=\"{height}\" fill=\"url(#s)\"/>
  </g>
  <g fill=\"{text_color}\" text-anchor=\"middle\" font-family=\"DejaVu Sans,Verdana,Geneva,Arial,sans-serif\" font-size=\"11\">
    <text x=\"{label_width / 2:.1f}\" y=\"14\">{label}</text>
    <text x=\"{label_width + value_width / 2:.1f}\" y=\"14\">{message}</text>
  </g>
</svg>""".strip()
    return svg


def write_files(total_papers: int) -> None:
    os.makedirs(BADGE_DIR, exist_ok=True)

    # Write SVG
    svg = generate_svg_badge("papers", str(total_papers), color="#2ea44f")
    svg_path = os.path.join(BADGE_DIR, "papers.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg + "\n")

    # Also write shields.io endpoint JSON (optional usage)
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
        f"📚 *Currently collected:* **`{total_papers}` papers and products** — *(Last update: {today})*"
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
