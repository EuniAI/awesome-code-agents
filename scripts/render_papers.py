#!/usr/bin/env python3
import re
import sys
from pathlib import Path
import yaml
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
README = ROOT / "README.md"

BLOCK_RE = re.compile(
    r"<!-- START PAPERS:(\w+) -->(.*?)<!-- END PAPERS:\1 -->",
    re.DOTALL
)

def to_title_case(text: str) -> str:
    """Title-case the string while preserving acronyms and internal caps.

    Rules:
    - Capitalize first and last words, and any word following a colon.
    - Lowercase minor words (articles, conjunctions, prepositions) unless first/last/after colon.
    - Preserve words with internal capitalization (e.g., ShapeLib), all-caps acronyms, and words with digits (e.g., 3D, GPT-4).
    - For hyphenated words, capitalize each component using the same rules.
    """
    text = text.strip()
    if not text:
        return text

    tokens = re.split(r"(\s+)", text)
    word_indices = [i for i, t in enumerate(tokens) if not t.isspace()]
    if not word_indices:
        return text
    first_idx = word_indices[0]
    last_idx = word_indices[-1]

    def preserve_original(word: str) -> bool:
        # Preserve internal caps, acronyms, or digits
        if any(ch.isdigit() for ch in word):
            return True
        # Internal capitalization (CamelCase) or all caps with length>1
        letters = re.sub(r"[^A-Za-z]", "", word)
        if len(letters) > 1 and word.isupper():
            return True
        if re.search(r"[A-Z].*[A-Z]", word):
            return True
        return False

    def cap_word(word: str, force_cap: bool) -> str:
        if not word:
            return word
        if preserve_original(word):
            return word
        base = word.lower()
        return base[:1].upper() + base[1:]

    out = []
    capitalize_next = True  # first word
    for i, tok in enumerate(tokens):
        if tok.isspace():
            out.append(tok)
            continue
        is_first = (i == first_idx)
        is_last = (i == last_idx)
        force_cap = capitalize_next or is_first or is_last

        # Handle hyphenated compounds
        parts = re.split(r"(-)", tok)
        new_parts = []
        for j, part in enumerate(parts):
            if part == "-":
                new_parts.append(part)
                continue
            # Always capitalize parts after hyphen per common title-case style
            part_force = force_cap or j > 0
            new_parts.append(cap_word(part, part_force))
        new_tok = "".join(new_parts)
        out.append(new_tok)

        capitalize_next = tok.endswith(":")

    return "".join(out)

def repo_slug(github_url: str) -> str:
    if not github_url:
        return ""
    p = urlparse(github_url)
    parts = p.path.strip("/").split("/")
    return "/".join(parts[:2]) if len(parts) >= 2 else ""

def badge_paper(url: str) -> str:
    return f"[![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)]({url})" if url else ""

def badge_github(url: str) -> str:
    slug = repo_slug(url)
    return f"[![GitHub Stars](https://img.shields.io/github/stars/{slug}?style=for-the-badge&logo=github&label=GitHub&color=black)]({url})" if slug else ""

def badge_website(url: str) -> str:
    if not url:
        return ""
    try:
        parsed = urlparse(url)
        label = ""
        if parsed.path.strip("/"):
            label = parsed.path.strip("/").split("/")[-1]
            label = re.sub(r"\.(html|md)$", "", label)
        else:
            # label = parsed.netloc
            domain = parsed.netloc.lower()
            domain = re.sub(r"^www\.", "", domain)
            domain = re.sub(r"\.(com|org|net|co|gov|edu|github|dev)(\.[a-z]{2})?$", "", domain)
            label = domain
        label = label.replace("_", "-").upper()
        return (
            f"[![Website]"
            f"(https://img.shields.io/website?url={url}"
            f"&up_message={label}"
            f"&up_color=blue"
            f"&down_message={label}"
            f"&down_color=blue"
            f"&style=for-the-badge)]({url})"
        )
    except Exception as e:
        return f"[![Website](https://img.shields.io/website?url={url}&up_message=Website&up_color=blue&down_message=Website&down_color=blue&style=for-the-badge)]({url})"

def render_entry(e: dict) -> str:
    # title = to_title_case(e.get("title", "").rstrip("."))
    title = e.get("title", "").rstrip(".")
    authors = e.get("authors", "")
    venue = e.get("venue", "")
    links = e.get("links", {}) or {}
    paper = links.get("paper", "")
    github = links.get("github", "")
    website = links.get("website", "")

    badges = " ".join(x for x in [badge_paper(paper), badge_github(github), badge_website(website)] if x)

    lines = []
    lines.append(f"- **{title}**  " if title[-1] in "?!" else f"- **{title}.**  ")
    lines.append(f"  _{authors}._ {venue}.  ")
    if badges:
        lines.append(f"  {badges}")
    return "\n".join(lines)

def render_list(entries):
    return "\n\n".join(render_entry(e) for e in entries)

def load_yaml_for(section_id: str):
    path = DATA_DIR / f"papers_{section_id}.yaml"
    if not path.exists():
        print(f"[WARN] {path} not found. Leaving block empty.", file=sys.stderr)
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        for i, e in enumerate(data):
            if not isinstance(e, dict):
                raise ValueError(f"Entry {i} in {path} is not a dict.")
            if "title" not in e or "authors" not in e or "venue" not in e or "links" not in e:
                raise ValueError(f"Entry {i} in {path} missing required keys.")
        return data
    except Exception as ex:
        print(f"[ERR] Failed to load {path}: {ex}", file=sys.stderr)
        return []

def main():
    if not README.exists():
        print(f"[ERR] README.md not found at {README}", file=sys.stderr)
        sys.exit(1)

    content = README.read_text(encoding="utf-8")

    def repl(match):
        section_id = match.group(1)  # code / computer / research / game
        entries = load_yaml_for(section_id)
        md = render_list(entries)
        return f"<!-- START PAPERS:{section_id} -->\n{md}\n<!-- END PAPERS:{section_id} -->"

    new_content, n = BLOCK_RE.subn(repl, content)
    if n == 0:
        print("[ERR] No <!-- START PAPERS:ID --> blocks found.", file=sys.stderr)
        sys.exit(2)

    if new_content != content:
        README.write_text(new_content, encoding="utf-8")
        print(f"[OK] Updated {n} block(s).")
    else:
        print("[OK] README unchanged.")

if __name__ == "__main__":
    main()
