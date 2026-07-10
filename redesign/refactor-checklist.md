# Refactor Checklist (temporary working file)

> Working checklist for the automation refactor. Check items off as they land; delete
> this file when everything is done. Problems come from the 2026-07-10 architecture
> review (see design-decisions.md). Paper migration happens only after the P0 items.

## Guiding rules (read before touching anything)

- **Minimal code, no overengineering.** This is a single-maintainer cron pipeline
  handling tens of papers a day. No database, no queue, no plugin system, no async,
  no speculative abstraction. Files + cron is the right tech.
- Every convention lives in exactly one place (schema, file layout, taxonomy, markers).
- Prefer deleting code over adding code. Prefer a function over a class.
- Flat beats nested: keep the package as flat as clarity allows.
- Any new abstraction must be justified by at least two concrete call sites, today.

## P0: foundations (before paper migration)

- [ ] **taxonomy.json is consumed by nothing.** Add a small `taxonomy` module (load,
      validate, walk, leaves, by_key); make it the only reader of taxonomy.json.
      Delete `categories:` and `tags:` from config.yaml; config keeps operational
      settings only.
- [ ] **Classifier prompt encodes the old worldview and contradicts L1** (requires
      "agent executes code/CLI"; would reject review/QA/localization and resource
      papers). Rebuild the prompt by compiling scope + master_test + tree
      (definitions/boundaries/examples) from the taxonomy module. No hand-written
      category text anywhere.
- [ ] **No structured-output guarantee; unlimited retries** (the 705-entry queue).
      Use JSON response format, cap retries, add a dead-letter list surfaced for
      manual triage instead of silent re-queueing.
- [ ] **README structure is hand-maintained; render only fills 23 scattered blocks.**
      Generate the whole Papers chapter (headings, section intros, Quick Navigation,
      entries) from the taxonomy tree between one pair of global markers.
- [ ] **Paper is a raw dict mutated across stages; entry schema implicit in 3 places.**
      One small `Paper` dataclass (+ `Classification`); YAML (de)serialization lives
      only in a `storage` module that owns the `papers_{key}.yaml` layout and dedup.
- [ ] **finalize shells out to render scripts via subprocess.** Make render/badges
      importable functions; `scripts/` folder dissolves into the package.

## P1: data sources (parallel with P0)

- [ ] **arXiv categories miss whole branches of the new taxonomy**: add cs.RO
      (world_physical), cs.AR (hardware), cs.DC + cs.OS (systems).
- [ ] **Keyword list is old-worldview and noisy**: regenerate per the 23 leaves
      (add terminal/CLI/shell, embodied/code-as-policy, computer use, AI scientist,
      theorem proving, CAD; prune pure-noise generics like `agentic`, `tool use`,
      `vulnerability`); keywords stay a cheap pre-filter.
- [ ] **Papers-With-Code enricher is dead** (API 302s to HuggingFace; every GitHub
      link lookup silently fails). Replace with HF Papers API + GitHub search
      fallback.

## P2: flow and hygiene (before or after migration)

- [ ] Review issues: include the taxonomy path + classifier reasoning in the issue
      body; validate `/edit category=` against leaf keys; auto-create missing
      `papers_{key}.yaml` on finalize instead of silently skipping.
- [ ] State: cap retry counts (dead-letter after N), atomic writes. Keep the single
      JSON file (single writer; splitting buys little).
- [ ] **Golden-set regression**: pick 40-60 already-filed papers with expected leaf;
      one script re-classifies and reports accuracy. Run it on every prompt/model
      change and as the migration back-test.
- [ ] New tag badges (`model`, `training-data`) in render; drop the unused
      papers.svg generator.
- [ ] Delete dead code: `learned_rules` half-feature (keep reject feedback in state),
      `migrate_deprecated_categories.py` (archive), old flat-category plumbing.

## Open questions (decide when reached)

- [ ] Final package layout: flat modules vs light subpackages (decide at P0 start;
      default to flat unless it gets crowded).
- [ ] `learned_rules`: confirmed delete? (default: delete)
- [ ] Classifier LLM backend (researched 2026-07-10; orchestration stays python+cron
      either way; Claude Code routines/loop rejected: cloud routines cannot access the
      server's gitignored state, /loop needs a live session):
      (a) Anthropic Messages API with structured outputs (guaranteed schema, ~USD 1-2
          per month at current volume) <- recommended default;
      (b) `claude -p` headless with --json-schema (runs on subscription via
          `claude setup-token`, heavier per call, can read repo files itself);
      (c) keep LiteLLM proxy with a better model + structured output (if proxy quota
          is effectively free).
      The golden-set eval (P2) can A/B these on accuracy before committing.

## After the checklist

Paper migration (36 -> 23 files, per-paper re-filing of dissolved categories and the
old terminal cleanup) -> close 271 stale pending issues, clear retry queue -> resume
cron. Then delete this file.
