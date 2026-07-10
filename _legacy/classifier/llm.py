"""
LLM-based classifier — uses LiteLLM proxy (OpenAI-compatible) to:
  1. Decide if a paper is relevant to code agents
  2. Assign the single most relevant category
  3. Detect special tags (benchmark / survey / position / empirical)
  4. Generate a 2-sentence summary

Output is structured JSON, parsed and validated here.
"""

from __future__ import annotations

import json
import logging
import os
import time
from typing import Any

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

# ── Client initialisation ─────────────────────────────────────────────────────

def _make_client() -> OpenAI:
    base_url = os.environ.get("LITELLM_BASE_URL", "http://localhost:4000")
    api_key  = os.environ.get("LITELLM_API_KEY", "anything")
    return OpenAI(base_url=base_url, api_key=api_key)


# ── Prompt ────────────────────────────────────────────────────────────────────

_SYSTEM_PROMPT = """\
You are a research librarian for "Awesome Code Agents" — a curated list of papers
about AI agents that use CODING or CLI as a core tool or action space.

The core criterion: the agent must use code execution or a terminal/CLI as a
primary means of action — regardless of what the end task is.
This includes (but is not limited to): software engineering, data analysis,
scientific computing, web automation, embodied agents that write code to act,
game-playing agents that use code, etc.

Respond ONLY with valid JSON — no markdown fences, no prose.
"""

def _build_user_prompt(
    paper: dict[str, Any],
    categories: dict[str, str],
    tags: dict[str, str],
    learned_rules: str = "",
) -> str:
    cat_lines = "\n".join(f'  "{k}": "{v}"' for k, v in categories.items())
    tag_lines = "\n".join(f'  "{k}": "{v}"' for k, v in tags.items())
    learned_section = f"\nAdditional rules learned from curator feedback:\n{learned_rules}\n" if learned_rules else ""

    return f"""\
Paper to classify:
  Title:    {paper['title']}
  Abstract: {paper['abstract'][:1200]}

Available categories (key → description):
{{{cat_lines}}}

Available tags (apply ALL that fit, or empty list):
{{{tag_lines}}}
{learned_section}
Respond with this exact JSON schema:
{{
  "relevant": true | false,
  "reason": "<one sentence — why relevant or not>",
  "category": "<category key from the list above, or null if not relevant>",
  "tags": ["<tag key>", ...],
  "summary": "<exactly 2 sentences summarising the paper's contribution and method>",
  "venue_hint": "<if the abstract explicitly mentions a conference/journal, state it; else empty string>"
}}

Strict relevance rules — mark relevant=false if ANY of these apply:
- The agent does NOT write or execute code, and does NOT use a terminal/CLI.
- It is a general-purpose LLM agent that reasons or plans in natural language only
  (e.g. pure web browsing agents, QA chatbots, math reasoning agents without code).
- It uses tools or APIs but none of the tools involve code execution or shell commands.
- The primary contribution is a general NLP/ML method that happens to be evaluated
  on a code dataset, but the method itself is not about code-executing agents.

Mark relevant=true if ANY of the following:
- The agent uses code execution or CLI as a primary action (regardless of end task).
- The paper surveys, systematically reviews, or empirically evaluates code/CLI agents.
- The paper proposes a benchmark or dataset for evaluating code/CLI agents.
- The paper studies the impact, behaviour, or limitations of AI coding tools/agents.

Other rules:
- Choose the SINGLE most specific functional category (e.g. code_generation,
  issue_resolution, benchmarks are NOT valid categories — use tags instead).
  Never invent new categories.
- Tags are orthogonal to categories — apply ALL that fit, but be strict:
  "benchmark" = the paper's PRIMARY contribution is a new benchmark/dataset, not just
    a paper that uses or evaluates on a benchmark;
  "survey" = comprehensive literature review of existing work;
  "empirical" = the PRIMARY contribution is studying/measuring/analysing existing
    systems — do NOT apply if the paper proposes a new method and includes experiments
    to validate it (that is standard practice, not an empirical study);
  "position" = opinion or vision paper without new experimental results.
- The summary must be self-contained and ≤ 60 words total.
"""


# ── Core classify function ────────────────────────────────────────────────────

def classify_paper(
    paper: dict[str, Any],
    categories: dict[str, str],
    tags: dict[str, str],
    model: str | None = None,
    temperature: float = 0.1,
    max_tokens: int = 1024,
    retries: int = 3,
    learned_rules: str = "",
) -> dict[str, Any]:
    """
    Classify a single paper. Returns a dict with keys:
      relevant, reason, category, tags, summary, venue_hint
    On failure returns {"relevant": False, "reason": "LLM error", ...}.
    """
    client = _make_client()
    model  = model or os.environ.get("LITELLM_MODEL", "gemini/gemini-2.5-flash")

    messages = [
        {"role": "system", "content": _SYSTEM_PROMPT},
        {"role": "user",   "content": _build_user_prompt(paper, categories, tags, learned_rules)},
    ]

    for attempt in range(1, retries + 1):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            raw = resp.choices[0].message.content.strip()
            result = json.loads(raw)
            # Validate required keys
            for key in ("relevant", "category", "tags", "summary"):
                if key not in result:
                    raise ValueError(f"Missing key '{key}' in LLM response")
            return result
        except json.JSONDecodeError as exc:
            logger.warning("Attempt %d: JSON parse error: %s\nRaw: %.200s", attempt, exc, raw)
        except Exception as exc:
            logger.warning("Attempt %d: LLM error: %s", attempt, exc)
        if attempt < retries:
            time.sleep(2 ** attempt)

    logger.error("All %d attempts failed for paper: %s", retries, paper.get("arxiv_id"))
    return {
        "relevant":    False,
        "reason":      "LLM classification failed after retries",
        "llm_failed":  True,   # distinguishes LLM error from "genuinely not relevant"
        "category":    None,
        "tags":        [],
        "summary":     "",
        "venue_hint":  "",
    }


def classify_papers(
    papers: list[dict[str, Any]],
    categories: dict[str, str],
    tags: dict[str, str],
    model: str | None = None,
    temperature: float = 0.1,
    learned_rules: str = "",
) -> tuple[list[dict[str, Any]], list[str]]:
    """
    Classify a list of papers. Mutates each paper in place, adding:
      - paper["category"]  : str | None
      - paper["tags"]      : list[str]
      - paper["summary"]   : str
      - paper["relevant"]  : bool

    Returns (relevant_papers, failed_arxiv_ids):
      - relevant_papers: papers the LLM confirmed are relevant
      - failed_arxiv_ids: papers where LLM call failed (should be retried later)
    """
    relevant: list[dict[str, Any]] = []
    failed_ids: list[str] = []

    for i, paper in enumerate(papers, 1):
        logger.info("[%d/%d] Classifying: %s", i, len(papers), paper["title"][:80])
        result = classify_paper(paper, categories, tags, model=model, temperature=temperature, learned_rules=learned_rules)

        if result.get("llm_failed"):
            aid = paper.get("arxiv_id", "")
            if aid:
                failed_ids.append(aid)
            logger.warning("  → LLM FAILED, will retry next run: %s", paper["title"][:60])
            time.sleep(0.5)
            continue

        paper["relevant"]   = result.get("relevant", False)
        paper["category"]   = result.get("category")
        paper["tags"]       = result.get("tags", [])
        paper["summary"]    = result.get("summary", "")

        # Use venue_hint to refine venue if classifier found something better
        hint = result.get("venue_hint", "").strip()
        if hint and not paper.get("venue"):
            paper["venue"] = hint

        if paper["relevant"] and paper["category"]:
            relevant.append(paper)
            logger.info("  → %s | tags=%s", paper["category"], paper["tags"])
        else:
            logger.info("  → NOT relevant: %s", result.get("reason", ""))

        # Small delay to avoid hammering the proxy
        time.sleep(0.5)

    logger.info("Classified %d papers → %d relevant, %d failed",
                len(papers), len(relevant), len(failed_ids))
    return relevant, failed_ids
