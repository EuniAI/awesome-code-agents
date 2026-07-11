# Legacy feature audit: the sign-off record before deleting _legacy/

Date: 2026-07-11. Method: four parallel auditors extracted an exhaustive feature
inventory of every legacy code file (including one recovered from bytecode:
papers_with_code.py had only a .pyc); every behavior was then judged against the
new implementation. This document is the formal disposition of every legacy
feature. _legacy/ may be deleted once the owner accepts this record.

## Verdict summary

- 9 real gaps found and FIXED in this audit round (see "Fixed now").
- Everything else is covered, upgraded, or deliberately dropped with rationale.

## Fixed now (audit round, 2026-07-11)

1. Mixed commands on one line ("/approve 1,3 /reject 2 wrong topic"): old parsed
   via finditer; new parser was line-anchored and silently dropped the second
   command. Now finditer-based, applied in positional order.
2. Reviewer login matching: old was case-insensitive; new was exact. Now casefold.
3. Classifier venue_hint: old LLM returned a venue hint and filled empty venues.
   Restored: venue_hint in the output schema, fill-only when our venue is the
   arXiv default, capped at 40 chars.
4. Command acknowledgement: old posted confirmation comments; new gave no signal
   on partial decisions. Now decide thumbs-up every processed command comment
   (stateless-safe: skips already-reacted).
5. Retry give-up: old gave up after 3 failed classification attempts (marked
   processed); new retried forever. Now retry.json holds id->count; at 3 the id
   is marked seen and logged.
6. Idle-day backfill: old advanced the historical sweep on ANY day with nothing
   new to process; new was weekend-only. Now weekends OR idle weekdays advance
   one slice (still gated by the pool cap).
7. Abstract GitHub fallback: old extracted "Code is available at github.com/..."
   from abstracts as the second enrichment source. Restored in enrich_links
   (HF API first, abstract regex fallback, trailing punctuation stripped).
8. Venue post-processing: old trimmed trailing filler ("... conference") and
   punctuation. Ported into extract_venue.
9. Bare arXiv ids in the inbox ("2601.12345" without a URL): old matched them;
   new only matched URLs. Restored with the captured-via-URL dedup subtlety.

Also rescued: scripts/generate_ack_badges.py (acknowledgement badges tooling)
copied out of _legacy before deletion. CORRECTION (owner spotted it): its config
data/ack_repos.yaml was never lost; it still lives in the live data/ directory,
so the acknowledgement tooling is fully intact.

## Covered or upgraded (no action)

- daily/finalize/setup/backfill modes -> crawl (cron) / decide (event-driven,
  seconds not hourly) / one-time setup done / backfill command + weekend cursor.
- Poll-based approvals + last_checked/decided state -> stateless decide: the
  issue body carries its payload; decisions recomputed from full comment history.
- processed_ids/rejected_ids union -> data/seen.json (+ data ids + open pool).
- learned_rules LLM feedback loop (auto-synthesized prompt rules from 10+
  rejections) -> calibration.json owner-labeled examples (fast loop) plus the
  Phase-4 slow loop (rule proposals ratified by the owner). Reject reasons remain
  durable in the issue comments themselves.
- Papers-With-Code enricher (dead API) -> HF papers API + abstract fallback.
- update_papers_badge.py -> automation/badges.py (summary lines preserved
  verbatim, including the retention-policy copy).
- render pipeline + git push chain -> render.py + workflow commit steps.
- Rotating file logs -> Actions logs. Config save/cache -> config never written.
- Corrupt-state resilience -> state files are tiny, committed, and in git.
- yaml_writer duplicate detection by URL/title -> id-is-identity plus
  storage.save dedup safety net (title dups were cleaned during migration).
- No-category file drop -> impossible: schema enum-locks categories and
  storage.save creates files.
- arXiv id version-suffix normalization -> OAI ids are versionless; inbox regex
  ignores vN suffixes.
- Unknown-category triage issues -> impossible by schema; failures go to retry.
- Inbox 👍 acknowledgements -> ack_inbox (already-processed comments included).
- Cross-category/cross-day dedup -> single found dict per harvest + known-ids.
- backfill.sh -> superseded by pipeline backfill; hardcoded paths were stale.

## Deliberately dropped (with rationale)

- Source labels on review issues (auto-discovered vs user-submitted): intake is
  unified now; a per-entry source marker can come with the review UI if wanted.
- Reject-reason storage in state: reasons live in the issue comments (GitHub is
  the durable record); auto-learning from rejects was rejected by design
  (a reject can mean low quality, not out of scope).
- PwC star-ranked repo selection: HF/abstract fallback takes the first match;
  star-ranking is not worth a second API integration for a best-effort field.
- summary field rendering in README: legacy never rendered it either ("not
  rendered yet"); the summary lives in the YAML and the review issue. Owner can
  ask for rendering later; it is a render.py-only change.
- qr_code_generation.py stays as-is in scripts/ (live promo utility).
