# Awesome Code Agents — Project Context

## Working Preferences (owner: Zhaoyang-Chu)

- **Always work directly on `main`**, no worktrees. Commit and push after each
  logical change so nothing gets lost.
- **Do NOT add `Co-Authored-By: Claude` to commit messages.** Commits show only
  the owner's account.
- **English-only repo.** Every file (data, docs, commit messages, comments) is
  English. No Chinese anywhere in the repo.
- **No em-dashes in anything we write** (they read as AI-written). Use colons,
  commas, parentheses, or separate sentences. Never alter em-dashes inside a
  paper's own title or abstract (quoted source text).
- **Capture design decisions as they happen** into automation/design-decisions.md (each
  with a one-line rationale). Chat is ephemeral; the repo is the memory.

## What This Is

A curated list of research papers on autonomous code agents, published at
[euni.ai](https://euni.ai) and github.com/EuniAI/awesome-code-agents. Rebuilt
from the ground up in 2026-07 (taxonomy, data, and pipeline); the old system
lives only in git history. Rebuild rationale: automation/design-decisions.md; the legacy
feature disposition: records/legacy-audit.md.

## The Two Sources of Truth

- **automation/taxonomy.json**: the category system. Four top-level branches:
  `foundation_models` (flagship general models), `studies` (surveys and
  empirical research about the agents), `artifact` (code as the deliverable;
  8 domains, software expands into 10 lifecycle activities), `agency` (code as
  the language of action; 6 worlds). Machine-facing contract per node:
  definition / includes / boundary / examples; plus a repo-wide scope with a
  hardened relevance gate and an ordered master_test. The classifier prompt is
  COMPILED from this file; never hand-write category text elsewhere.
- **automation/calibration.json**: owner-labeled real papers as positive and
  negative few-shot examples (each with a why). They guide the classifier by
  precedent; they never pin papers by id. Grows automatically from review
  feedback (see the learning loop) and by hand when the owner rules on a case.

## Data Layout

- `automation/data/papers_{leaf}.yaml`: one file per taxonomy leaf; newest first (arXiv v1
  date); id is identity; storage.save dedups as a safety net.
- `automation/data/abstracts.json`: abstract sidecar (fetch once, reuse forever).
- `automation/data/seen.json`: ids the pipeline has handled (proposed or auto-skipped).
- `automation/data/retry.json`: classification-failure counts (give up at 3 -> seen).
- `automation/data/harvest.json`: announcement-day ledger (every swept day + record count;
  a missing day = a coverage gap) plus the daily cursor.
- `automation/data/backfill.json`: historical-sweep cursor (weekend/idle slices).
- `automation/data/feedback.json`: owner review reasons queued for LLM distillation.
- `automation/data/ack_repos.yaml`: acknowledgement badges config (docs/static/images/generate_ack_badges.py).
- `README.md`: generated zones between NAV/PAPERS markers show papers from the
  last 12 months; `automation/PAPERS.md` (fully generated) is the complete collection
  including the recent ones. Never
  hand-edit either; run `python -m automation.render`.

## Pipeline (GitHub Actions, event-driven, GitHub-native state)

```
crawl.yml  (cron 06:30 UTC daily + manual)         decide.yml (fires on issue_comment)
  OAI-PMH announcement harvest since cursor          parse ALL reviewer comments (stateless)
  + inbox issue links + retry queue                  apply /approve /reject /edit
  -> classify (Claude subscription token)            -> write the data files, render, badges
  -> chunked review issues (the pool, 25/issue)      -> queue reasons in feedback.json
  -> venue upgrades from update stream               -> thumbs-up processed comments
  -> weekends/idle days: backfill slice              -> close issue when all decided
  -> distill feedback.json -> calibration.json
```

- Classifier: `claude -p --json-schema` on the Claude subscription
  (`CLAUDE_CODE_OAUTH_TOKEN` repo secret, exported as ANTHROPIC_AUTH_TOKEN to a
  scrubbed subprocess; renew yearly with `claude setup-token`). Only crawl.yml
  sees the token; decide.yml is token-free.
- Review commands (reviewer only, case-insensitive login, several per line):
  `/approve all` · `/approve 1,3-5` · `/reject 2 optional reason` ·
  `/edit 3 category=web tags=benchmark venue=ICSE 2026 reason=why`.
  Positional order; later commands override earlier ones. /edit implies approve.
- **The pool**: open `paper-review` issues ARE the backlog; nothing is dropped,
  partial review is fine, issues close themselves when fully decided.
  Backpressure: historical intakes pause while the pool holds >= review.pool_cap
  (config.yaml) papers; the daily crawl is never gated.
- **Learning loop**: /edit corrections and /reject reasons are distilled by the
  next crawl run into calibration examples (quality-rejections are excluded by
  the LLM's judgment: quality is not a scope rule).
- Manual tools: `python -m automation.pipeline backfill --from A --to B`,
  `... reclass <leaf...>` (after rule changes), `... crawl --dry-run`.

## Module Map (automation/, flat, every convention in exactly one place)

taxonomy.py (sole reader of taxonomy.json) · models.py (Paper, Classification)
· storage.py (data/ layout owner + state files) · sources.py (ALL arXiv/network:
OAI harvest, id fetch, inbox, enrichment, venue extraction) · classify.py
(prompt compiler + claude runner + validation) · reviewflow.py (issue protocol:
payload-carrying issues, command parsing, acks) · pipeline.py (crawl / decide /
backfill / reclass entrypoints) · render.py (README + PAPERS.md) · badges.py
(count badge + summary block) · config.yaml (repo/review/backfill/arxiv:
categories + keyword recall net) · tests/ (30 tests, no network).

## Roadmap (agreed, not yet built)

1. **Review UI** (next): a thin layer OVER the GitHub issue protocol (GitHub
   Pages + OAuth + API, no server). One screen per paper, buttons post the
   /commands; desktop + mobile; source markers shown; the pool renders as one
   queue. The pool is parked (~470 papers) until this exists.
2. **Golden-set regression eval**: measure classifier precision on the approved
   corpus + recorded OUTs after every rule change, instead of discovering
   regressions through the owner's pain.
3. **Subscription feature** for readers (per-category updates), for euni.ai.

## Notes for Future Sessions

- The classifier prompt = taxonomy.json + calibration.json. To change behavior,
  edit those (and run `pipeline reclass` on affected leaves), not the code.
- Scope gate matters more than routing: most owner-reported errors were
  papers that should never have entered. See scope.excludes (7 rules).
- GitHub logins, issue payloads, comment history: decide is stateless and
  re-runnable; every write is dedup-safe.
- taxonomy.json survives `json.dumps(indent=2, ensure_ascii=False)` round-trips
  (verified); edit it programmatically for structural changes.
- Old pipeline reference: git history and records/legacy-audit.md (file-by-file
  disposition); records/completeness-diff.md is the deletion warrant with every
  written OUT verdict. The transient migration review sheets live in git history.
