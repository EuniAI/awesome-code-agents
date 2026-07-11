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

- [x] **taxonomy.json is consumed by nothing.** DONE 2026-07-10: `automation/taxonomy.py`
      (load/validate/walk/leaves/by_key, fails loudly) + `automation/storage.py` (sole
      owner of the data-file layout). 2026-07-10: `categories:`/`tags:` deleted from
      config.yaml (old classifier parked in _legacy); `automation/config.py` loads
      operational config only. New data model in `automation/models.py` (Paper: id as
      identity, category as a field); old data parked in `_legacy/data/`.
- [x] **Classifier prompt encodes the old worldview and contradicts L1.** DONE
      2026-07-11: `automation/classify.py` compiles the prompt from taxonomy.json
      (scope, master_test, tree with boundaries/examples, tag facets); zero
      hand-written category text. Smoke test 3/3 with reasons citing our boundary
      rules verbatim. Backend: `claude -p` on the subscription, scrubbed subprocess
      env; note: setup-token auths via ANTHROPIC_AUTH_TOKEN (not
      CLAUDE_CODE_OAUTH_TOKEN) on claude 2.1.165.
- [x] **No structured-output guarantee; unlimited retries.** DONE 2026-07-11:
      `--json-schema` enforced output (object root; payload in envelope
      `structured_output`), category enum-locked to the 23 leaf keys at schema
      level, semantic validation + exactly one retry per batch, failures marked
      (`Classification.failed`) instead of re-queued forever. Remaining sub-step:
      surface failed papers in a triage list when the daily pipeline is rebuilt.
- [x] **README structure is hand-maintained; render only fills 23 scattered blocks.**
      DONE 2026-07-10: `automation/render.py` generates NAV and PAPERS zones from the
      tree between two marker pairs (idempotent, fails loudly on missing markers);
      old 36-block chapter surgically removed; `scripts/render_papers.py` is now a
      thin shim; tests in `automation/tests/`.
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
      (a) `claude -p` headless with --json-schema <- owner's preference, default.
          Runs on the Claude subscription via a `claude setup-token` long-lived token
          (documented for CI use; store as env var / Actions secret; renew yearly).
          Zero marginal cost; batch 20-50 papers per invocation to amortize startup;
          works identically under server cron and GitHub Actions.
          Model: pass --model explicitly (never rely on the session default).
          Migration runs on claude-sonnet-5 (accuracy first; whole-corpus cost is
          trivial). Daily pipeline model decided by a golden-set A/B of haiku-4-5 vs
          sonnet-5 after migration; downgrade only if accuracy ties.
      (b) Anthropic Messages API with structured outputs (pay-per-token, ~USD 1-2
          per month at current volume) as fallback if subscription limits ever bite;
      (c) keep LiteLLM proxy with a better model + structured output (if proxy quota
          is effectively free).
      The golden-set eval (P2) can A/B these on accuracy before committing.

## Post-migration quality audit (open items as of 2026-07-11)

Owner is reviewing the migrated corpus; more error reports incoming. Pending work:

- [x] **Misclassification reports from owner** (fixed 2026-07-11):
      - HTAM -> systems (KernelBench operator optimization). DONE.
      - PerfDojo -> systems (ML library gen for hardware; same kernel cluster). DONE.
      - Confucius Code Agent -> software_debugging (SWE-bench Pro). DONE.
      - Kimi K2 -> world_general + model (general agentic model). DONE.
      - SWE-Compass -> software_debugging. DONE (earlier).
      - Dedup: removed 10 duplicates (7 same-id, 3 same-paper-different-id incl.
        MatchFixAgent); storage.save now dedups as a safety net. DONE.
      - (owner will send more; append here)
- [x] **Owner rulings formalized into calibration examples (2026-07-11).** Was a
      fragile title-substring override list; now `calibration.json` (repo root) holds
      owner-labeled positive/negative examples fed into the classifier prompt. Examples
      only, no id-pinning (owner's call). Grow it whenever a classification is corrected;
      it doubles as the future golden-set (P2). Note: the earlier note about needing a
      more formal id-based override form is resolved by this (examples, not overrides).
- [ ] **DECIDED 2026-07-11 (execute in re-audit): keep general leaves, purge via
      benchmark-routing rule.** software_general is a misclassification magnet; owner
      asked whether to delete it. Decision (design-decisions.md): KEEP, re-scope.
      Rule: a paper on an activity-specific benchmark (SWE-bench->debugging,
      KernelBench->systems) goes to that activity, not general; only surveys/positions/
      productivity-empirical/multi-benchmark-platforms stay. Shrinks ~42 -> ~15.
      TODO: encode this in software_general/world_general boundary in taxonomy.json,
      then re-run classification over both general leaves and apply the purge.
- [ ] **Rules-revision round** (do once owner's error list is in):
      - Encode owner's general-leaf semantics into taxonomy.json definitions of
        software_general/world_general: general = research on the GENERAL FORM of the
        task that fits no specific leaf; NOT an overviews/surveys bin; when a specific
        class accumulates, split it out as a new leaf.
      - Move the anti-marketing-framing rule (already in the classifier prompt) into
        the general leaves' boundary fields in taxonomy.json.
      - Add explicit judgment rule: benchmark evidence (e.g. runs on KernelBench /
        SWE-bench) is a strong category signal; look up what the benchmark tests.
- [ ] **Pending owner rulings** (from my software_general audit + refetch pass):
      - Cross-Team Orchestration + Scaling LLM-based Multi-Agent Collaboration:
        same family as AgentVerse/Evolving Orchestration which owner OUTed; consistency
        says OUT too. Confirm.
      - InterCode: interactive bash/SQL/CTF environments = code-as-action; move to
        agency (world_terminal or world_general)?
      - Kimi K2: general agentic FM, not SE-specific; world_general + model, or out?
      - "A Survey on Code Generation with LLM-based Agents": activity-specific survey;
        move to software_code_generation + survey per our own rule?
      - SWE-Lancer / MAD-empirical / ReasoningBank: medium suspects in software_general.
      - Armchair: OUTed on title-only evidence ("insufficient information"); owner may
        know the paper; identify and re-place or confirm OUT.
      - APIGen scope ruling: does function/tool-calling count as code-as-action?
        If yes: world_general; if no: OUT stands, and write the exclusion into
        taxonomy.json scope.
- [ ] **Re-audit pass after rules revision**: re-run classification over
      software_general and world_general members (and spot-check 20 random others);
      the 12 title-only papers (see refetch-reclass.md, evidence=title-only) get a
      manual look.
- [ ] **Remaining migration work**: inbox rescue (~70 papers not yet in the list;
      compute fresh from inbox issue #4 vs current data); close 271 stale pending
      GitHub Issues + retire _legacy/state/processed.json (keep rejected_ids for
      reference until rescue done); completeness diff against _legacy/ then delete it.
- [ ] CLAUDE.md full rewrite after the rebuild settles (banner added 2026-07-11 is
      interim).

## After the checklist

Paper migration (36 -> 23 files, per-paper re-filing of dissolved categories and the
old terminal cleanup) -> close 271 stale pending issues, clear retry queue -> resume
cron. Then delete this file.
