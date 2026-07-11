# Completeness diff: the _legacy deletion warrant

Date: 2026-07-11. Every paper the old world ever knew is accounted for in the new
world; _legacy/ carries no unique information and is deleted (recoverable from git
history at any time).

## The accounting

Legacy universe: 947 unique paper ids
(= the 35 old curated papers_*.yaml files + all arXiv ids in the 271 stale
pending review issues recorded in _legacy/state/processed.json).

| disposition | count |
|---|---|
| in the curated corpus (data/papers_*.yaml) | 432 |
| in data/seen.json (handled: auto-skipped or given up, with run logs) | 554 |
| awaiting review in the open pool issues | 392 |
| none of the above, but with a written OUT verdict in redesign/migration reports | 33 |
| **unaccounted (orphans)** | **0** |

(Rows overlap: an id can be both in seen and in the pool payloads' history.)

## What was deleted with _legacy/

- The old pipeline code (main, crawler, inbox, enricher, classifier, review,
  finalizer, state_manager, config_loader): every feature audited file-by-file in
  redesign/legacy-audit.md; 9 gaps were ported before deletion.
- The old curated data files: fully re-classified into the new taxonomy
  (redesign/migration/full-run.md and follow-up passes).
- _legacy/state/processed.json: its pending ids were absorbed by the backlog run
  (2026-07-11, 479 classified, 271 issues closed); rejected ids were seeded into
  data/seen.json; learned_rules were superseded by calibration.json.
- automation/migrate.py (the migration tooling) retired with it; the one durable
  command, reclass, moved to automation/pipeline.py.
