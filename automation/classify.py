"""
Taxonomy-driven paper classifier, running on the Claude subscription.

The prompt is compiled from taxonomy.json (scope, master test, the full tree with
definitions/boundaries/examples, tag facets); no category text is hand-written here.
Papers are classified in batches through `claude -p` (headless) with a JSON-schema-
enforced output, so a syntactically invalid response cannot occur; semantic
validation (leaf keys, tag vocabulary) happens here, with one retry per batch.

Environment notes, learned the hard way (2026-07-10):
- The subprocess gets a scrubbed environment. When this code runs inside a Claude
  Code session, the parent's ANTHROPIC_BASE_URL and session variables hijack the
  CLI's authentication.
- The `claude setup-token` credential authenticates via ANTHROPIC_AUTH_TOKEN
  (Bearer); CLAUDE_CODE_OAUTH_TOKEN is not honored by headless claude 2.1.165.
  We store the token under CLAUDE_CODE_OAUTH_TOKEN in automation/.env (its
  conventional name) and export it as ANTHROPIC_AUTH_TOKEN to the subprocess.
"""

from __future__ import annotations

import json
import logging
import os
import subprocess
from pathlib import Path
from typing import Any, Callable

from automation import taxonomy
from automation.models import Classification

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = _REPO_ROOT / "automation" / ".env"

MODEL = "claude-sonnet-5"
BATCH_SIZE = 10
_TIMEOUT_S = 900

PAPER_TYPES = ("survey", "empirical", "position")
ARTIFACT_TAGS = ("benchmark", "model", "training-data")


# ── Auth and environment ──────────────────────────────────────────────────────

def _auth_token() -> str:
    token = os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "")
    if not token and ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            if line.startswith("CLAUDE_CODE_OAUTH_TOKEN="):
                token = line.split("=", 1)[1].strip()
                break
    if not token:
        raise RuntimeError(
            "No CLAUDE_CODE_OAUTH_TOKEN found (env or automation/.env). "
            "Generate one with `claude setup-token`."
        )
    return token


def _subprocess_env() -> dict[str, str]:
    """Minimal, scrubbed environment for the claude subprocess."""
    return {
        "HOME": os.environ.get("HOME", ""),
        "PATH": os.environ.get("PATH", ""),
        "ANTHROPIC_AUTH_TOKEN": _auth_token(),
    }


# ── Prompt compilation (everything comes from taxonomy.json) ─────────────────

def _node_block(node: taxonomy.Node, is_leaf: bool) -> str:
    lines = [f"definition: {node.definition}"]
    if node.includes:
        lines.append("includes: " + " | ".join(node.includes))
    if node.boundary:
        lines.append("boundary: " + " | ".join(node.boundary))
    if is_leaf and node.examples:
        ex = "; ".join(f"{e['paper']} -> {e['verdict']} ({e['why']})" for e in node.examples)
        lines.append(f"examples: {ex}")
    return "\n".join(lines)


def build_prompt(items: list[dict[str, str]]) -> str:
    """Compile the classification prompt for a batch of {id,title,abstract} items."""
    tax = taxonomy.load()
    parts: list[str] = []

    parts.append(
        "You are the classifier for Awesome Code Agents, a curated list of research "
        "papers on autonomous code agents. Classify each paper below into exactly one "
        "leaf category of the taxonomy, plus optional sparse tags, and write a summary."
    )

    scope = tax.scope
    parts.append("RELEVANCE SCOPE\ncollects: " + scope.get("collects", ""))
    parts.append("excludes (mark these relevant=false):\n- " + "\n- ".join(scope.get("excludes", [])))

    parts.append("MASTER TEST (apply in order):\n" + "\n".join(f"{i+1}. {r}" for i, r in enumerate(tax.master_test)))

    tree: list[str] = ["TAXONOMY (choose exactly one LEAF key for each relevant paper):"]
    for node, depth in tax.walk():
        indent = "  " * depth
        head = f"{indent}[{node.key}] {node.title}" + ("" if node.is_leaf else f"  (axis: {node.axis})")
        tree.append(head)
        body = _node_block(node, node.is_leaf)
        tree.append("\n".join(indent + "  " + l for l in body.splitlines()))
    parts.append("\n".join(tree))

    leaf_keys = ", ".join(tax.leaf_keys())
    parts.append(f"VALID LEAF KEYS (category must be one of): {leaf_keys}")

    parts.append(
        "TAGS (sparse; only when clearly applicable; empty list is the common case):\n"
        f"- paper_type, at most one of: {', '.join(PAPER_TYPES)}. No tag = plain method paper.\n"
        f"- released_artifact, any of: {', '.join(ARTIFACT_TAGS)}. Tag `benchmark`/`model`/"
        "`training-data` only when releasing that artifact is a primary contribution."
    )

    papers = ["PAPERS TO CLASSIFY:"]
    for i, it in enumerate(items):
        papers.append(f"--- paper {i} ---\ntitle: {it['title']}\nabstract: {it.get('abstract', '')[:2500]}")
    parts.append("\n".join(papers))

    parts.append(
        "OUTPUT: an object {results: [...]} with exactly one entry per paper, in input "
        "order, each: {index, relevant, category (leaf key, or null if not relevant), "
        "tags (possibly empty), summary (2 sentences, self-contained, max 60 words), "
        "reason (one short sentence: which rule/boundary decided the category)}."
    )
    return "\n\n".join(parts)


def _output_schema(n: int) -> dict[str, Any]:
    """Top level must be an object: the CLI implements --json-schema as a forced
    tool call, and tool input schemas reject non-object roots."""
    leaf_keys = taxonomy.load().leaf_keys()
    return {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "minItems": n,
                "maxItems": n,
                "items": {
                    "type": "object",
                    "properties": {
                        "index": {"type": "integer"},
                        "relevant": {"type": "boolean"},
                        "category": {"anyOf": [{"type": "string", "enum": leaf_keys}, {"type": "null"}]},
                        "tags": {"type": "array", "items": {"type": "string", "enum": list(PAPER_TYPES + ARTIFACT_TAGS)}},
                        "summary": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["index", "relevant", "category", "tags", "summary", "reason"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["results"],
        "additionalProperties": False,
    }


# ── Backend ───────────────────────────────────────────────────────────────────

def _run_claude(prompt: str, schema: dict[str, Any], model: str) -> list[dict[str, Any]]:
    """One headless claude call; returns the parsed JSON array."""
    cmd = [
        "claude", "-p",
        "--model", model,
        "--output-format", "json",
        "--json-schema", json.dumps(schema),
        "--bare",
    ]
    proc = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True,
        timeout=_TIMEOUT_S, env=_subprocess_env(),
    )
    envelope = json.loads(proc.stdout) if proc.stdout.strip() else {}
    if proc.returncode != 0 or envelope.get("is_error"):
        detail = envelope.get("result") or proc.stderr
        raise RuntimeError(f"claude failed (exit {proc.returncode}): {str(detail)[:300]}")
    # The schema-validated payload lives in `structured_output`, not `result`.
    out = envelope.get("structured_output")
    if not isinstance(out, dict) or "results" not in out:
        raise RuntimeError(f"no structured_output in envelope: {str(envelope)[:200]}")
    return out["results"]


# ── Validation and public API ─────────────────────────────────────────────────

def _validate(raw: list[dict[str, Any]], n: int) -> list[Classification] | None:
    leaves = set(taxonomy.load().leaf_keys())
    vocab = set(PAPER_TYPES + ARTIFACT_TAGS)
    if not isinstance(raw, list) or len(raw) != n:
        return None
    out: list[Classification | None] = [None] * n
    for item in raw:
        i = item.get("index")
        if not isinstance(i, int) or not (0 <= i < n) or out[i] is not None:
            return None
        relevant = bool(item.get("relevant"))
        category = item.get("category") or ""
        tags = item.get("tags") or []
        if relevant and category not in leaves:
            return None
        if any(t not in vocab for t in tags) or sum(t in PAPER_TYPES for t in tags) > 1:
            return None
        out[i] = Classification(
            relevant=relevant,
            category=category if relevant else "",
            tags=list(tags),
            summary=(item.get("summary") or "").strip(),
            reason=(item.get("reason") or "").strip(),
        )
    return out  # type: ignore[return-value]


def classify(
    items: list[dict[str, str]],
    model: str = MODEL,
    batch_size: int = BATCH_SIZE,
    runner: Callable[[str, dict[str, Any], str], list[dict[str, Any]]] = _run_claude,
) -> list[Classification]:
    """Classify papers ({id,title,abstract}); one retry per batch, failures marked."""
    results: list[Classification] = []
    for start in range(0, len(items), batch_size):
        batch = items[start:start + batch_size]
        prompt, schema = build_prompt(batch), _output_schema(len(batch))
        verdicts = None
        for attempt in (1, 2):
            try:
                verdicts = _validate(runner(prompt, schema, model), len(batch))
            except Exception as exc:
                logger.warning("batch %d attempt %d failed: %s", start // batch_size, attempt, exc)
                verdicts = None
            if verdicts is not None:
                break
        if verdicts is None:
            logger.error("batch %d failed after retry; marking %d papers failed", start // batch_size, len(batch))
            verdicts = [Classification(relevant=False, failed=True, reason="classification failed") for _ in batch]
        results.extend(verdicts)
        logger.info("classified %d/%d", len(results), len(items))
    return results
