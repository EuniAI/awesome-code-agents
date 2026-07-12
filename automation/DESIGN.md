# Design

The design philosophy behind this repo, organized by theme. Everything from here
to the roadmap is built and running; the reasoning that holds it up is stated
alongside it, not as a log of how we got here. The final section is the roadmap:
good designs we have reasoned through but not yet shipped. English only.

## Thesis: Code as Everything

The list has one thesis: code is the substrate of all intelligent action, no
longer confined to the digital realm. Two worlds follow from it:

> **Code as Everything.**
> The digital world we build. The real world we act in.

The digital world is part of the real world: acting in a terminal, a browser, or
a game has real consequences. That unifies the whole agency branch from browser
to robot, and lifts the thesis from "code is everywhere" to "code is the core of
large models and agents."

The rendered README header is three lines of increasing width (name, vision
subtitle in Title Case, one-line description), an intentional expanding shape.

## Taxonomy

The taxonomy is the contract. The classifier prompt is compiled from it; category
text lives nowhere else.

### One axis per level

Each level uses exactly one classification axis, and sibling categories at a level
are conceptually parallel and mutually exclusive. Mixing axes (lifecycle task,
interaction surface, output domain, resource form all flattened onto one plane) is
the root cause of misclassification: it leaves the classifier with no single
correct answer. Every node separates two jobs that a single name cannot serve at
once:

- **title**: the human-facing display name (carries the vision, parallel within a
  level).
- **definition**: the classifier-facing spec (carries the precision, stored not
  improvised), with `includes` (positive signals), `boundary` (explicit "if X, go
  to sibling Y instead" rules for every confusable neighbor), and `examples` (real
  papers, each with a one-line why).

`key` is the stable machine id: ASCII, never changes even when the title is
reworded.

### Four top-level branches

Two task branches and two off-axis branches, in this order:

1. **foundation_models**: flagship general models. The substrate that powers both
   task branches, so it sits deliberately off the task axis.
2. **studies**: surveys and empirical research whose object is the agents/field.
3. **artifact**: code as the deliverable (what code is for).
4. **agency**: code as the language of action (what code does).

Clean symmetry: two meta branches (the models, and research about the agents) plus
two task branches. This reinforces the thesis rather than diluting it.

### Classify by the task served, not the paper's output

L1 does not classify what a paper produces or how it evaluates. It classifies the
task the paper serves:

- **artifact**: the served task's goal is to produce code or a repository; the
  deliverable is the code. Testing, fuzzing, localization, review, comprehension,
  and environment setup are artifact, because their ultimate purpose is producing
  or safeguarding code.
- **agency**: the served task's goal is to complete a task in a world, and code is
  the tool; success is measured on world-state change. Training a model is an
  agency task (the model is the product of "train a model", not a digital-world
  artifact), so ML engineering is agency.

The unifying test: is the served task's ultimate purpose producing code, or is the
produced code merely the tool for a task in the world? A static chart from a spec
is an artifact; a dynamic, interactive visualization is agency (the static /
interactive line is a general proxy for this purpose test). Resource papers (data,
models, benchmarks, surveys) are classified by the downstream task they serve, then
tagged by contribution form. Category is the task served; tag is the contribution
form; the two axes never mix.

### artifact: 8 domains

Axis: the domain of the code being built. `software` (the only node that expands
into lifecycle activities), `web`, `database`, `systems`, `hardware`, `game`,
`graphics` (graphics and animation), `cad` (3D and CAD).

### agency: 6 worlds

Axis: the world the agent acts in. `world_terminal` (terminals and operating
systems, including DevOps/SRE/live-ops and database tuning), `world_browser`,
`world_apps` (professional and everyday software operated through code),
`world_game`, `world_physical`, `world_research` (data analysis, ML engineering,
and scientific discovery share one purpose: knowledge through interaction, code is
the instrument). Agency keys carry a `world_` prefix so they stay unique against
artifact domains (web vs world_browser, game vs world_game).

### software: 10 lifecycle activities

Only the `software` domain expands, along the software-lifecycle axis:
`software_development` (feature development into an existing codebase),
`software_code_generation` (producing code from spec or scratch, including
multi-agent end-to-end teams), `software_testing` (proactive search for unknown
defects, plus formal verification), `software_debugging` (handling a known or
reported defect, including issue reproduction), `software_review`,
`software_comprehension`, `software_maintenance`, `software_security` (one coherent
community: detection, localization, repair, auditing, secure codegen),
`software_infrastructure` (environment setup and CI/CD), `software_studies`.

Key boundaries: development vs code generation is whether a codebase already
exists; testing vs debugging is proactive search vs a known defect; vuln-targeted
fuzzing is security, general fuzzing is testing; performance and kernel work is
systems (writing low-level code), while optimizing an existing repo is maintenance.

### Foundation Models: an off-axis substrate branch

A flagship general model serves no single task; it powers both artifact production
and code-as-action, so it sits off the task axis, first. Justified by axis
necessity, not by mass, and structurally guaranteed to grow (labs ship these
constantly). Strict boundary keeps every "-Coder" out: a paper enters only if the
model is a flagship general substrate spanning both code production and
code-as-action with no single primary task. Task-specialized models route to their
activity leaf plus a model tag. Product announcements without a technical report
are out of scope; flagship technical reports are in.

### Studies: an off-axis research branch, and no "general" catch-alls

`studies` holds only research whose object is the agents or the field. The hard
rule that keeps it from becoming a magnet: a paper that proposes an agent, method,
or benchmark to do a task routes to that task's leaf, however general it looks; a
survey of one activity or world is that leaf plus a survey tag; only field-wide
surveys live in `studies`.

There are deliberately no "general-purpose agent" leaves. Every code-as-action
agent has a most-representative world it can be assigned to, and every software
agent a most-representative activity. Catch-all leaves acted as misclassification
magnets: any paper with slight cross-scope flavor fell in. Benchmark routing
dominates generalist framing: a paper evaluated on an activity-specific benchmark
belongs to that activity, regardless of "general/unified/comprehensive"
self-labeling.

### Tags: sparse, contribution-form facets

Tags are sparse and optional; no tag means a plain method paper (there is no
default tag value). Two independent facets: **paper type** (survey / empirical /
position, mutually exclusive) and **released artifact** (benchmark / model /
training-data, multi-select, since training work commonly ships all three). We do
not tag "agent": nearly every paper proposes one, so it carries no information, and
"did they release a runnable system" is already implicit in the github link.
Mechanism tags (planning, memory, multi-agent) are rejected as inherently
multi-label and fuzzy, which would move the "no single answer" problem from the
category layer to the tag layer.

### id is identity

A paper's arXiv id is its identity; a leaf file never holds two entries with the
same id, and storage dedups by id as a safety net. For the same paper under
different ids (arXiv id vs a venue link), prefer the arXiv id.

## Classification: precedent, not pins

The classifier is guided by owner-labeled real papers as positive and negative
few-shot examples (calibration.json), each with a why, injected as authoritative
precedent. Examples guide by precedent; they never pin a paper by id. Even a
labeled paper is re-classified by the LLM, so the example set is tested rather than
trusted blindly; the cure for a regression is a better example, not a lock. A
negative example (out-of-scope) is marked by a null category.

The scope gate matters more than routing: most errors are papers that should never
have entered, not papers routed to the wrong leaf. The gate excludes generic
methods that merely emit code as a reasoning aid, non-agent papers, and domain
case studies with only incidental code. Quality is not a scope rule: a low-quality
paper is a reject, not a scope exclusion, and quality rejections never become
negative calibration examples.

## Pipeline

The pipeline is event-driven GitHub Actions with GitHub-native state. Its shape
follows from what Actions natively provides, not from a server-era design.

- **Single-writer rule**: only Actions Python writes to the repo. Every other
  interface (the review UI included) reads GitHub and posts issue comments; no
  second brain owns state.
- **Event-driven approval, stateless decide**: a review issue carries its own JSON
  payload in the body. Deciding needs only the issue: it recomputes decisions from
  the full comment history (later commands override earlier), and every write is
  dedup-safe, so re-runs are idempotent. Approval latency is seconds, not an hour
  of cron polling.
- **Concurrency is tolerated, not prevented**: the review UI submits several issues
  in quick succession, so decide runs race. We do not serialize them with a
  concurrency group, because GitHub keeps only one pending run per group and
  silently cancels the rest, which would drop approvals with no error. Instead each
  decide run is self-healing: it applies against the latest main, commits, and
  pushes, and on a lost push race it resets to the new main and re-runs the
  idempotent decide. The generated views (README, PAPERS.md, papers.json) are
  derived from the data, so a concurrent write is resolved by regenerating them,
  never by merging their text. Crawl, which is too expensive to re-run, keeps its
  group (no overlapping crawls) and resolves the same view conflicts by
  regenerating after a rebase.
- **The issue is the source of truth, and a reconciler enforces it**: an open
  review issue with an un-acked reviewer comment means "not yet processed", so no
  decision is ever truly lost while its issue exists. The daily crawl opens with a
  reconcile pass that scans every open issue and re-applies any decision missing
  from the data (an approval whose paper is not stored, or a fully decided issue
  still open). It is idempotent and repairs only the issues with a gap, so a
  healthy pool costs a few reads and no writes. This turns "an operator might
  notice the failed run" into "the system checks itself every day."
- **Announcement-driven crawl**: the daily source is "every arXiv announcement
  mailing since my last successful run", via OAI-PMH indexed by announcement
  datestamp. One run equals one announcement batch. The cursor is self-healing: a
  failed run leaves it untouched and the next run harvests the gap. There is no
  lookback window to tune.
- **Recall-first keyword net**: the cheap title+abstract pre-filter that feeds the
  classifier leans deliberately broad, because the two failure modes are not
  symmetric. A false positive costs one classifier call and is then auto-skipped
  before the review pool (the classifier is the precision stage), so noise never
  reaches the owner. A false negative is invisible and permanent: a paper the net
  misses never enters the pipeline and no later stage can recover it. So the net is
  a flat OR over a broad, per-leaf keyword list (whole-word, plural-tolerant), and
  when a term's noisiness is in doubt we keep it. The one deliberate exclusion is
  bare agent/model words (agent, LLM, language model): alone they match most of
  cs.AI/CL/LG and would disable the filter rather than widen it, so only
  code-specific agent/model phrases are keywords.
- **The pool**: open paper-review issues are the backlog; nothing is dropped,
  partial review is fine, and issues close themselves when fully decided. Issues
  are chunked and taxonomy-ordered so a batch is coherent to review.
- **Backpressure**: historical intakes pause while the pool is at capacity; the
  daily crawl is never gated, so fresh papers always flow.
- **Learning loop**: reject and edit reasons are queued and distilled by the next
  crawl into calibration examples (edits become positive, out-of-scope rejects
  become negative, quality rejects are excluded by the LLM's judgment). The owner's
  terse reasons expand into reusable rules of thumb.
- **Token isolation**: only the crawl workflow holds the Claude subscription token;
  the decide workflow needs no LLM, so the secret's exposure surface is one
  workflow. Decide also gates on the reviewer's login at the workflow level and
  re-validates it in Python (defense in depth).

## Presentation

- **Freshness split**: the README shows only papers from the last twelve months;
  the complete collection lives in a fully generated PAPERS.md with per-leaf
  anchors. Nothing is ever deleted; the main list stays frontier-focused and free
  of bloat. Both zones are generated, never hand-edited.
- Summary sentences stay unrendered on the README (kept in data, not shown).
- **Self-hosted star history**: the star-history chart is rendered from the repo's
  own stargazer timestamps into a committed SVG (assets/star-history.svg, refreshed
  weekly), not embedded from star-history.com. GitHub restricted stargazer data so
  the third-party embed now needs a per-viewer token and is permanently broken in a
  README; a self-owned static SVG depends on nothing external and cannot break.

## Review UI

A private, single-user tool for the owner; readers never see it. It is a thin
client over the issue protocol, not a replacement for it.

- **Remote control, never a second brain**: the UI only reads GitHub and posts
  issue comments. No YAML in the browser, no direct commits, no duplicated storage
  logic. GitHub stays the single source of truth.
- **Draft then submit, incremental**: decisions accumulate locally; submit posts
  one aggregated comment per affected issue. Multiple partial submits are the normal
  flow. Already-decided papers are derived statelessly by re-parsing the reviewer's
  comments (the UI mirrors the decide parser) and drop out of the queue; fully
  decided issues close themselves. No new state anywhere.
- **Chinese in, English out**: the owner writes reasons in Chinese; on submit the
  UI translates them to English via the GitHub Models API and posts pure English.
  On translation failure the draft stays local and submission is blocked, so no
  Chinese ever reaches comments, feedback, or calibration.

v0 covers the intake queue (approve, reject, edit newly crawled papers). Editing
already-collected papers is the planned next step (see the roadmap).

## Discoverability

The Pages site root is an indexable landing page (canonical, Open Graph,
description) that links to the repo; the private review tool lives under a noindex
path. The goal is to raise the repo's pages into the always-mirrored primary
search index through genuine backlink signal (an indexable landing, a link from the
product site, cross-links from sibling repos, and real distribution), rather than
relying on a secondary index that regional serving nodes may not mirror.

## Roadmap

Everything above is built. These are designs we have reasoned through but not yet
shipped: the standing to-do list, each with the reason it is worth doing.

- [ ] **Collection management in the review UI (v2)**: a pinned Curation issue plus
  id-addressed commands (`/remove`, `/move`, `/set`) parsed by the decide workflow,
  a `curation` label, and a machine-readable `assets/collection.json` export. This
  extends the same thin-client, single-writer design from the intake queue to
  editing already-collected papers, with reasoned removals feeding the same learning
  loop. Reason: correcting a filed paper today still means hand-writing a command.
- [ ] **Golden-set regression eval**: measure classifier precision on the approved
  corpus plus the recorded out-of-scope verdicts after every taxonomy or calibration
  change. Reason: regressions should surface in a report, not in the owner's review
  pain one paper at a time.
- [ ] **Reader subscription**: per-category update feeds for readers, surfaced on
  euni.ai. Reason: the taxonomy already yields clean per-leaf slices, so readers can
  follow one world or activity instead of the whole firehose.
- [ ] **Backlink signal for discoverability**: a body link from euni.ai, cross-links
  from sibling repos' READMEs, and one genuine distribution post. Reason: real
  inbound links are what pull the pages from the regional secondary index into the
  always-mirrored primary index.
- [ ] **Credit inbox contributors**: record the GitHub handle of whoever suggested a
  paper (the inbox reader already sees the commenter's login) and acknowledge
  suggesters in the README. Reason: contributions arrive as inbox links, not git
  commits, so git-based contributor displays (badge, avatar wall) never reflect the
  real community and were removed; this credits the actual contribution model, and
  is worth building once suggestions come from many people.
