"""
The single reader of taxonomy.json (repo root).

Everything that needs the category tree (rendering, classification, migration,
review validation) goes through this module. Loading validates the tree and
fails loudly; nothing downstream should ever see a malformed taxonomy.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

_REPO_ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_PATH = _REPO_ROOT / "taxonomy.json"

_KEY_RE = re.compile(r"^[a-z][a-z0-9_]*$")


@dataclass
class Node:
    key: str
    title: str
    definition: str
    blurb: str = ""  # short, human-facing, vision-flavored one-liner for the README
    emoji: str = ""
    includes: list[str] = field(default_factory=list)
    boundary: list[str] = field(default_factory=list)
    examples: list[dict[str, str]] = field(default_factory=list)
    axis: str = ""
    children: list["Node"] = field(default_factory=list)

    @property
    def is_leaf(self) -> bool:
        return not self.children


@dataclass
class Taxonomy:
    raw: dict[str, Any]
    nodes: list[Node]

    def walk(self) -> Iterator[tuple[Node, int]]:
        """Depth-first (node, depth) traversal; depth 0 = L1."""

        def _walk(node: Node, depth: int) -> Iterator[tuple[Node, int]]:
            yield node, depth
            for child in node.children:
                yield from _walk(child, depth + 1)

        for node in self.nodes:
            yield from _walk(node, 0)

    def leaves(self) -> list[Node]:
        return [n for n, _ in self.walk() if n.is_leaf]

    def by_key(self, key: str) -> Node:
        for node, _ in self.walk():
            if node.key == key:
                return node
        raise KeyError(f"Unknown taxonomy key: {key!r}")

    def leaf_keys(self) -> list[str]:
        return [n.key for n in self.leaves()]

    # Convenience accessors for the classifier
    @property
    def scope(self) -> dict[str, Any]:
        return self.raw.get("scope", {})

    @property
    def master_test(self) -> list[str]:
        return self.raw.get("master_test", [])

    @property
    def tags(self) -> dict[str, Any]:
        return self.raw.get("tags", {})


def _parse_node(obj: dict[str, Any]) -> Node:
    return Node(
        key=obj["key"],
        title=obj["title"],
        definition=obj["definition"],
        blurb=obj.get("blurb", ""),
        emoji=obj.get("emoji", ""),
        includes=obj.get("includes", []),
        boundary=obj.get("boundary", []),
        examples=obj.get("examples", []),
        axis=obj.get("axis", ""),
        children=[_parse_node(c) for c in obj.get("children", [])],
    )


def _validate(tax: Taxonomy) -> None:
    seen: set[str] = set()
    for node, _depth in tax.walk():
        if not _KEY_RE.match(node.key):
            raise ValueError(f"Invalid key (must be lowercase ASCII): {node.key!r}")
        if node.key in seen:
            raise ValueError(f"Duplicate taxonomy key: {node.key!r}")
        seen.add(node.key)
        if not node.title.strip():
            raise ValueError(f"Node {node.key!r} has an empty title")
        if not node.definition.strip():
            raise ValueError(f"Node {node.key!r} has an empty definition")
        if not node.is_leaf and not node.axis.strip():
            raise ValueError(f"Non-leaf node {node.key!r} must declare its axis")
    if not tax.nodes:
        raise ValueError("Taxonomy has no top-level nodes")


_cache: Taxonomy | None = None


def load(path: Path | None = None, force: bool = False) -> Taxonomy:
    """Load, validate, and cache the taxonomy."""
    global _cache
    if _cache is not None and not force and path is None:
        return _cache

    raw = json.loads((path or TAXONOMY_PATH).read_text(encoding="utf-8"))
    tax = Taxonomy(raw=raw, nodes=[_parse_node(n) for n in raw["nodes"]])
    _validate(tax)
    if path is None:
        _cache = tax
    return tax
