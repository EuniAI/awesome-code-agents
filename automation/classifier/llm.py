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
You are a research librarian specialising in AI code agents.
Your job is to classify arXiv papers for the "Awesome Code Agents" repository,
which tracks research on autonomous AI systems that write, fix, review, execute,
or interact with code and software.

Respond ONLY with valid JSON — no markdown fences, no prose.
"""

def _build_user_prompt(paper: dict[str, Any], categories: dict[str, str], tags: dict[str, str]) -> str:
    cat_lines = "\n".join(f'  "{k}": "{v}"' for k, v in categories.items())
    tag_lines = "\n".join(f'  "{k}": "{v}"' for k, v in tags.items())

    return f"""\
Paper to classify:
  Title:    {paper['title']}
  Abstract: {paper['abstract'][:1200]}

Available categories (key → description):
{{{cat_lines}}}

Available tags (apply ALL that fit, or empty list):
{{{tag_lines}}}

Respond with this exact JSON schema:
{{
  "relevant": true | false,
  "reason": "<one sentence — why relevant or not>",
  "category": "<category key from the list above, or null if not relevant>",
  "tags": ["<tag key>", ...],
  "summary": "<exactly 2 sentences summarising the paper's contribution and method>",
  "venue_hint": "<if the abstract explicitly mentions a conference/journal, state it; else empty string>"
}}

Rules:
- Set "relevant" to false if the paper is NOT about AI/LLM agents that write, fix, test,
  review, execute or otherwise interact with source code or software systems.
- Choose the SINGLE most specific category that fits. Never invent new categories.
- Only set tags that genuinely apply. "benchmark" = introduces a new eval dataset/suite;
  "survey" = comprehensive literature review; "position" = opinion/vision paper;
  "empirical" = primary contribution is empirical measurement/study.
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
        {"role": "user",   "content": _build_user_prompt(paper, categories, tags)},
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
        "relevant":   False,
        "reason":     "LLM classification failed after retries",
        "category":   None,
        "tags":       [],
        "summary":    "",
        "venue_hint": "",
    }


def classify_papers(
    papers: list[dict[str, Any]],
    categories: dict[str, str],
    tags: dict[str, str],
    model: str | None = None,
    temperature: float = 0.1,
) -> list[dict[str, Any]]:
    """
    Classify a list of papers. Mutates each paper in place, adding:
      - paper["category"]  : str | None
      - paper["tags"]      : list[str]
      - paper["summary"]   : str
      - paper["relevant"]  : bool
    Returns only the relevant papers.
    """
    relevant: list[dict[str, Any]] = []

    for i, paper in enumerate(papers, 1):
        logger.info("[%d/%d] Classifying: %s", i, len(papers), paper["title"][:80])
        result = classify_paper(paper, categories, tags, model=model, temperature=temperature)

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

    logger.info("Classified %d papers → %d relevant", len(papers), len(relevant))
    return relevant
