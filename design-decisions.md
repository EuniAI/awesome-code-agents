# Design Decisions

> Durable record of non-trivial design decisions for this repo. Newest first.
> This repo is English-only — keep every entry in English.

## 2026-07-11: Phase-4 pipeline is event-driven and GitHub-native (3 modules)

The old pipeline's shape (daily crawl cron + HOURLY finalize cron polling for
approvals + a stateful processed.json) was a server-era design. Rebuilt around what
GitHub Actions natively provides:

1. EVENT-DRIVEN APPROVAL. `decide.yml` fires on `issue_comment` the moment the
   reviewer comments on a review issue. The entire poll_approvals concept and the
   hourly cron are gone; approval latency drops from up-to-an-hour to seconds.
2. THE REVIEW ISSUE CARRIES ITS OWN PAYLOAD. The issue body ends with a fenced JSON
   block holding every proposed paper + its proposal. Decide is stateless: it needs
   only the issue, recomputes decisions from the full comment history (later commands
   override earlier ones), and every write is dedup-safe, so re-runs are idempotent.
3. STATE IS ONE FILE. data/seen.json (ids already proposed or auto-skipped),
   committed by the workflow. Curated papers live in data/*.yaml; pending proposals
   live in the open review issue. The old multi-field processed.json state machine is
   retired. Seeded with the 109 inbox ids + 12 legacy rejected ids; deliberately NOT
   seeded with the 2076 legacy processed ids, so the owner can always resurrect an old
   paper through the inbox.
4. TOKEN ISOLATION. Only crawl.yml sees the Claude subscription token; decide.yml
   needs no LLM (calibration whys are templated), so the secret's exposure surface is
   one workflow. decide.yml also gates on the reviewer's login at the workflow level
   AND pipeline.decide re-validates against config.yaml (defense in depth).
5. LEARNING LOOP WIRED IN. Every `/edit category=` correction auto-appends an
   owner-labeled example to calibration.json. Rejects add no example (a reject can
   mean low quality, not out of scope; automating that would poison the example set).
6. gh CLI EVERYWHERE. No hand-rolled GitHub REST client; `gh` is preinstalled on
   runners with GITHUB_TOKEN injected, and it is already authenticated locally.
7. Modules: sources.py (all arXiv/network logic, single home; migrate.py now imports
   from it), reviewflow.py (issue protocol), pipeline.py (crawl/decide entrypoints).
   The dead Papers-With-Code enricher is replaced by a best-effort Hugging Face
   papers-API lookup, run only for approved papers at decide time.

Validated before building: `claude -p` authenticates in a clean empty-HOME
environment with only ANTHROPIC_AUTH_TOKEN set (the exact shape of an Actions
runner), on claude 2.1.165 with a setup-token credential.

## 2026-07-11: owner rulings become calibration examples, not hard overrides

The string-match override list (RULING_OVERRIDES in migrate.py) pinned specific papers
by title substring: fragile (a new paper whose title contains "Tree-of-Code" would be
mis-pinned) and it bypassed the classifier instead of improving it.

Decision: replace it with `calibration.json` (repo root) — the owner's real labeled
papers as positive and negative few-shot examples, each with a `why`. classify.py
injects them into the prompt as "OWNER-LABELED EXAMPLES" (authoritative precedent).

Owner's choice (asked explicitly): examples ONLY, no id-pinning. The labeled papers
GUIDE the classifier by precedent; they do not lock any paper. Even a labeled paper is
re-classified by the LLM. Tradeoff accepted: purer and it tests the classifier, but a
ruled paper can regress and need re-catching. The cure for a regression is a better
example, not a pin. Grow calibration.json whenever a classification is corrected.

Consequence: RULING_OVERRIDES and _override_for deleted; run_full, refetch_reclassify,
reclassify_leaves, and process_inbox now classify every paper (no ruled branch).
`category: null` in calibration.json marks a negative (out-of-scope) example. `id` is a
reference key, not a lock.

## 2026-07-11: Foundation Models added as a third top-level branch, placed first

Owner: flagship frontier general-purpose models from major labs (Kimi K2,
Qwen3-Coder, MiniMax, DeepSeek, Claude, GPT, Gemini) all belong in one place, ahead
of the two task branches. The old repo had a `foundation_models` category (4 papers).

Decision: add `foundation_models` as a THIRD top-level node in taxonomy.json, placed
FIRST (order: foundation_models, artifact, agency). It is a top-level leaf (no L2/L3).

Rationale: our L1 axis is "the task the paper serves", but a flagship general model
serves NO single task; it is the substrate powering both artifact production and
code-as-action. Forcing it into artifact hides its agentic use and vice-versa. So this
node sits deliberately OFF the task axis. Justified by axis-necessity, not by mass; it
is a structurally-guaranteed growing cluster (labs ship these constantly). Framing:
two task branches (what code is for, what code does) + one substrate branch that powers
both — reinforces "Code as Everything". Renders as an L1 section, papers directly under
it (render.py/taxonomy.py already handle a depth-0 leaf).

Strict boundary (prevents every "-Coder" flooding in): a paper enters only if the
model is a flagship general substrate spanning BOTH code production and code-as-action
with no single primary task. Task-specialized models route to their activity leaf +
model tag (SWE-GPT -> software_debugging, JanusCoder -> software_code_generation,
VulnLLM-R -> software_security, Terminus-4B -> world_terminal). Product/marketing
announcements without a technical report stay out of scope; flagship model technical
reports are in. Encoded as master_test step 1 (off-axis escape checked first) and the
node boundary. Moved in now: Kimi K2, Qwen3-Coder. CWM pending owner ruling
(code-gen-centric research model, leaning software_code_generation + model).

## 2026-07-11: review UI is a thin layer OVER GitHub Issues (not a replacement)

Owner wants a fast way to (a) approve newly crawled/inboxed papers and (b) correct
misclassifications on demand, from BOTH desktop and phone, anytime. Writing `/edit`
comments by hand, or telling Claude to move papers, is too slow for a high-frequency
action.

Decision (deferred implementation): build a UI that is a presentation/interaction layer
ON TOP OF GitHub Issues, NOT a separate app that owns state. The actual review still
happens through the Issue protocol (`/approve`, `/edit category=X`, `/reject`), so
GitHub stays the single source of truth and the pipeline (GitHub Actions) reads commands
exactly as designed. The UI just turns typing commands into buttons/dropdowns/keyboard
actions and posts them to the issue on the owner's behalf.

Requirements captured:
- Works on desktop AND mobile, anytime (approve + re-file on the go).
- Likely shape: a responsive client-side web app (could live on GitHub Pages) that uses
  the GitHub API + owner OAuth to read the review issue(s) and post the review commands.
  No server needed; state stays in Issues.
- Each correction should also feed the calibration learning loop (append a
  positive/negative example to calibration.json with an auto-drafted why) so the
  classifier improves from every fix. Ties into the Phase-4 fast/slow learning loop.
- Timing: implement when we rebuild the crawl/approval pipeline (after the core
  refactor), not now.

## 2026-07-11 (later): BOTH general leaves abolished; Studies promoted to top-level

Supersedes the "general leaves kept" decision below. The owner decided to abolish both
general catch-alls entirely, because even with a benchmark-routing rule they stayed
magnets: any paper with slight cross-activity/cross-world flavor fell in.

Two moves:
1. `software_general` -> abolished. Its surveys/positions/empirical became a new leaf
   `software_studies`; its generalist agents/benchmarks were routed to activities by a
   reclass pass (50 -> 31 studies; 19 evicted).
2. `world_general` -> abolished. The owner rejected the "agency is asymmetric, keep it"
   argument: every code-as-action agent has a most-representative world it can be
   assigned to (CodeAct/Tree-of-Code -> a world, not a general bin). Its 12 members were
   re-routed to specific worlds/activities/studies.

Structural consequence: `software_studies` was promoted OUT of artifact/software to a
repo-wide top-level leaf `studies` ("Surveys & Empirical Studies"), so agency-side
surveys (Code as Agent Harness) have a correct home too. L1 is now FOUR branches:
two off the task axis (`foundation_models` = the models, `studies` = research about the
agents) and two task branches (`artifact`, `agency`). Clean symmetry: two meta branches
+ two task branches. Ordering: foundation_models, studies, artifact, agency.

The `studies` hard rule (kills the magnet on both branches): a paper that PROPOSES an
agent, method, or benchmark to do a task routes to that task's leaf, however general it
looks; only research whose OBJECT is the agents/field lives in `studies`. A survey of
ONE activity/world is that leaf + survey tag; only field-wide surveys are in `studies`.

## 2026-07-11: general leaves kept, re-scoped by a benchmark-routing rule

The two "general" leaves (software_general "General-Purpose Software Agents",
world_general "General-Purpose Action Agents") were acting as misclassification
magnets: any paper with a "generalist agent" framing landed there, including agents
actually evaluated on a single activity's benchmark (Confucius on SWE-bench Pro, MASAI
on SWE-bench, SWE-Compass). Owner asked whether to delete software_general.

Decision: KEEP both, but re-scope. Deleting orphans ~17 genuinely cross-cutting
papers (broad multi-activity surveys, position/roadmap papers, productivity/adoption
empirical studies) that fit no single activity. The real fix is a boundary rule:

  BENCHMARK ROUTING DOMINATES GENERALIST FRAMING. A paper evaluated on an
  activity-specific benchmark belongs to that activity (SWE-bench -> debugging,
  KernelBench -> systems), regardless of "general/unified/comprehensive" self-labeling.
  Only papers with NO single-activity benchmark (surveys spanning activities, position
  papers, empirical studies of the practice, truly multi-benchmark platforms) stay in
  a general leaf.

This shrinks software_general from ~42 to ~15, all legitimately cross-cutting. The rule
is to be encoded in the general leaves' boundary fields in taxonomy.json and enforced
in the re-audit pass. Also: general = research on the general FORM of the task; when a
specific class accumulates enough papers, split it out as a new leaf (owner principle).

## 2026-07-11: performance/kernel papers route to systems, no new leaf yet

HTAM (operator optimization, KernelBench) and PerfDojo (ML library generation for
heterogeneous architectures) were misfiled under software_maintenance. They are about
WRITING low-level performance-critical code, which is systems ("kernels, compilers").
Moved to systems (which already holds KernelBench, PithTrain, CrashFixer). The cluster
(HTAM, PerfDojo, KernelBench, SimdBench, ~4-5 papers) is not yet large enough to
warrant a dedicated "HPC/kernel engineering" leaf; revisit if it grows past ~6-8.
SWE-Perf stays in maintenance (optimizing existing repos, not writing kernels).

## 2026-07-11: id is identity; storage.save dedups as a safety net

Found 10 duplicates in migrated data: 7 same-id-within-a-file (caller bug) and 3
same-paper-different-id (arXiv id vs venue link). Rule: id is the identity; a leaf file
never holds two entries with the same id. storage.save() now dedups by id (keep first,
log a warning). For same-paper-different-id, prefer the arXiv id version.

## 2026-07-10: L3 settled: 10 software-lifecycle activities under General Software

### Structure (encoded in taxonomy.json with full definitions/boundaries/examples)
`software_development` (Feature Development), `software_code_generation` (Code
Generation & Completion), `software_testing` (Testing & Verification),
`software_debugging` (Debugging & Issue Resolution), `software_review` (Code Review),
`software_comprehension` (Comprehension & Documentation), `software_maintenance`
(Maintenance & Evolution), `software_security` (Security), `software_infrastructure`
(Environment Setup & CI/CD), `software_general` (General-Purpose Software Agents).

### Rulings and rationale
- Data scan drove the design: old `code_generation` (62) hid at least six communities
  (multi-agent end-to-end dev, repo-level codegen/completion, surveys, documentation,
  code search, requirements); old `issue_resolution` (134) was a dumping ground for
  field-level surveys, scaffolds/SDKs, and generalist agents.
- **development vs code_generation split** (revised 2026-07-10): the line is whether a
  codebase already exists. Producing code from spec/scratch at any scale (function to a
  whole repo/app from zero, incl. MetaGPT/ChatDev multi-agent teams) is code_generation;
  adding a feature into an existing codebase (FEA-Bench/NoCode-bench) is feature_development.
- **testing vs debugging line**: proactive search for unknown defects vs handling a
  known/reported defect; issue reproduction therefore moves from testing to debugging.
- **security kept as one leaf** (coherent community: vuln detection/localization/repair,
  auditing, secure codegen); vuln-targeted fuzzing goes to security, general fuzzing to
  testing; exploiting running systems stays in world_terminal.
- **Formal verification merged into testing** (Testing & Verification): both safeguard
  correctness proactively.
- **software_general is not a misc bin** (owner's rule): admission follows the master
  test; enter only when the served task is software engineering as a whole (field-level
  surveys/roadmaps, generalist agents, scaffolds/SDKs, cross-activity studies). A survey
  of issue-resolution agents belongs to debugging.
- Titles fixed by owner after two rounds: "Environment Setup & CI/CD" (rejected:
  Engineering Infrastructure, Environments & Toolchains as too vague) and
  "General-Purpose Software Agents" (rejected: Foundations & Overviews as vague,
  Agentic Software Engineering as overclaiming the whole field).

The full tree is now complete: 2 (L1) x 14 (L2) with 10 L3 leaves under software,
23 leaf categories total. Next: implementation phase (config sync from taxonomy.json,
data-file migration, README regeneration, classifier prompt rewrite, backlog reset).

## 2026-07-10: L2 settled: 8 artifact domains + 6 agency worlds

### Structure (encoded in taxonomy.json with full definitions/boundaries/examples)
- **artifact** (axis: the domain of the code being built): `software` (General Software,
  the only node that expands into L3), `web` (Web Applications), `database` (Databases),
  `systems` (Systems), `hardware` (Hardware), `game` (Games), `graphics` (Graphics &
  Animation), `cad` (3D & CAD).
- **agency** (axis: the world the agent acts in): `world_terminal` (Terminals & Operating
  Systems), `world_browser` (Browsers & the Web), `world_apps` (Software Applications),
  `world_game` (Game Worlds), `world_physical` (The Physical World), `world_research`
  (Research & Discovery).
- Agency keys carry a `world_` prefix: it guarantees key uniqueness against artifact
  domains (web vs world_browser, game vs world_game) and encodes the branch in data
  filenames.

### Rulings in this round (owner)
- Titles: "General Software" (not Software), "Systems" (not Systems Software).
- **`world_apps` added** (title: Software Applications): agents operating professional
  and everyday software (office, design tools, simulators, enterprise, desktop/mobile)
  through code. Fills a real gap; the papers mis-filed into old `terminal` (e.g.
  Multi-Agent Computer Use) land here.
- **Research merge confirmed**: data analysis + ML engineering + scientific discovery
  form one world, `world_research` (they share one purpose: knowledge through
  interaction; code is the instrument).
- **Theorem proving split**: formal verification of software -> artifact/software; pure
  mathematical theorem proving -> world_research.
- **Scope exclusion**: non-agent papers are out. Pure LLM reasoning that merely emits
  code as a reasoning aid (PAL/PoT, code-interpreter math) is not collected. Recorded in
  taxonomy.json `scope.excludes`.
- DevOps/SRE/live-ops (incl. database tuning) live under `world_terminal`; game-testing
  by playing serves the game's code and stays in artifact.

## 2026-07-10: L1 sealed: four boundary rulings by the owner

All four reduce to one unified test: **is the served task's ultimate purpose producing
code (artifact), or is the produced code merely the tool for completing a task in the
world (agency)?**

1. **Artifact broadened beyond "emits code".** Testing, fuzzing, localization, review,
   comprehension/QA: their ultimate purpose is producing code, so they are artifact.
2. **Environment building is artifact.** Setting up environments serves writing and
   fixing code; it is not interaction for its own sake.
3. **Cross-branch papers: judge the purpose the paper positions itself to serve.**
   Qwen-Coder-style models whose agentic evals are issue resolution: artifact. A generic
   agent method evaluated on SWE-bench plus web/game benches that do not use code as
   action: artifact. The Code-as-Agent-Harness survey covers both branches but advocates
   code-as-action: agency.
4. **Data analysis vs chart generation.** Chart-from-spec (deliverable is chart code):
   artifact. Explore-the-data (deliverable is insight; code and charts are tools):
   agency. Static-vs-interactive is only a proxy for this purpose test.

Residual note: truly 50/50 papers are rare; the classifier picks the closest by stated
purpose and the human review step (approve/edit) is the backstop. All four rulings are
encoded in taxonomy.json (master_test, boundary, examples).

## 2026-07-10: L1 semantics corrected: classify by the task served, not by the paper's own output

### Owner's correction (supersedes the earlier "where evaluation lands" master test)
L1 does not classify what a paper produces, nor how it evaluates. It classifies **the
task the paper serves**:
- **artifact (Building the Digital World)**: the served task's goal is to produce code or
  a repository. The digital world is built of code; the task's deliverable is the code.
- **agency (Acting in the Real World)**: the served task's goal is to complete a
  real-world task through interaction, and code is the tool. A trained model is not a
  digital-world artifact; it is the product of the real-world task "train a model", so
  MLE belongs to agency.

### Implications
- Resource papers (data synthesis, foundation models, benchmarks, surveys) are classified
  by the downstream task they serve, then tagged by contribution form (training-data,
  model, benchmark, survey). Worked examples: synthesizing trajectories/environments for
  issue-resolution agents goes to artifact; synthesizing data for code-as-policy embodied
  agents goes to agency.
- "Every paper both writes and runs code" is the wrong lens; never classify by the
  paper's own artifact or headline metric alone.
- Crisp formulation now in taxonomy.json: **category = the task served; tag = the
  contribution form. The two axes never mix.**

## 2026-07-11: Deployment decided: GitHub Actions with GitHub-native state

- Target deployment for the rebuilt pipeline is **GitHub Actions** (public repo, free
  minutes, built-in GITHUB_TOKEN). This supersedes the old rule "no GitHub Actions,
  state lives on the server": its sole rationale (local state persistence) disappears
  once state is GitHub-native.
- State design for Phase 4: a slim processed-ids file committed to the repo; pending
  review is represented by GitHub Issues (labels), not local JSON; failed
  classifications surface as a triage list. Code stays deployment-agnostic (secrets via
  environment variables only), so server cron remains a zero-cost fallback.
- Implementation timing: decision now, deployment last. The workflow YAML and repo
  secrets are written in Phase 5, after the rebuilt pipeline runs green locally.
  Migration (Phase 3) runs on the server either way.
- Classifier auth under Actions: the `claude setup-token` credential becomes an Actions
  secret, exported to the job as ANTHROPIC_AUTH_TOKEN (see automation/classify.py).

## 2026-07-10: L2 rulings + the name-vs-definition principle for the taxonomy

### The core principle (drives everything below)
Old category names failed not because they were "casual" but because each word tried to
serve two jobs at once — a human-facing label AND a classifier spec — and did neither
well. **Separate the two:**
- **title** — human-facing display name (README); carries the vision; parallel and
  elegant within a level.
- **definition** — classifier-facing spec; carries the precision; stored, not improvised.

Every taxonomy node stores a structured definition (in config.yaml under `taxonomy:`):
- `key` — stable machine id, ASCII, never changes even if the title is reworded.
- `title` — display name.
- `axis` — (non-leaf only) the single dividing axis of its children.
- `definition` — one-sentence precise scope.
- `includes` — positive signals / kinds of papers that belong.
- `boundary` — **the anti-mis-classification field**: explicit "if X, it goes to sibling
  Y instead" rules for every confusable neighbor pair. All past mis-classifications came
  from unwritten sibling boundaries; writing them once, here, feeds them into the
  classifier prompt.
- `examples` — 2-3 real papers, each with a one-line "why here".

### Naming principles (titles)
- Parallel grammatical form within a level: Artifact-L2 = engineering/craft domains
  (`X Engineering` / `X Design`); Agency-L2 = worlds acted in (`The X World` / acting in X).
- The title should telegraph the boundary so human browsing also lands right.
- Drop implementation words like `generation` / `executing` — they are exactly what
  smuggled the "output" and "interface" axes back in and caused the old mess.

### L2 rulings
- **agentic_visualization → artifact (graphics_animation) by default.** General rule the
  owner set: agency = code that, when run, produces actions/interactions in a world; so a
  static chart/figure is an artifact, but a **dynamic, interactive** visualization →
  agency. This "static = artifact / interactive = agency" test is a general discriminator,
  not viz-only.
- **machine_learning_engineering → agency**, grouped under "autonomous research /
  discovery" (evaluated on model/experiment outcomes in the world, not artifact quality).
  Open: whether ML-experiments, data, and scientific-discovery merge into one
  research/discovery world or stay separate agency leaves.

## 2026-07-10: List vision and L1 naming (Code as Everything)

### Vision (the list's thesis, to sit at the top of the README)
> **Code as Everything.**
> The digital world we build. The real world we act in.

Kept deliberately short (fits at the very top of the repo), no dashes. The second
sentence echoes the two L1 chapter titles (*Building the Digital World* / *Acting in the
Real World*), so the tagline closes back on the section headings. "act in" chosen over
"reach/shape/…" for exact consistency with the Agency chapter title (2026-07-10).

Header presentation (2026-07-10, final): the rendered README header is three lines whose
widths increase top-to-bottom (an intentional expanding shape, mirrored from
AssetOpsBench):
1. `# Awesome Code Agents` (name)
2. `### The Digital World We Are Building. The Real World We Are Acting In.` (the vision,
   Title Case, as the subtitle)
3. `*A curated, ever-growing collection of frontier research papers and technical reports
   on autonomous code agents.*`

Notes: the literal "Code as Everything" label was dropped from the visible header — as a
17-char phrase it was shorter than the title and broke the expanding-line shape. It
remains the conceptual thesis of the list and the name of the L1 framing (Code as
Artifact / Code as Agency); it is just not printed as header chrome. Do not "restore" it
to the header assuming it was lost. Title Case for the vision line is deliberate (a hero
tagline reads as a title, not prose); here it also capitalizes cleanly because the only
preposition "in" is the final word.

Rationale: as agents advance rapidly and touch the physical world, code is becoming a
core element of how the world runs, no longer confined to the digital realm — code is
the very core of large models and agents. Key insight (from the owner): **the digital
world is part of the real world** — acting in a terminal, a browser, or a game is just
as much real-world activity, with real consequences. This unifies the whole Agency
branch from browser to robot, and lifts "Code as Everything" from "code is everywhere"
to "code is the substrate of all intelligent action".

### L1 naming (display title separated from internal key)
- Internal machine keys (used in config / data filenames / classifier prompt):
  `artifact` / `agency` — short, stable, ASCII.
- README display titles:
  - **Code as Artifact: Building the Digital World** (= former "product" branch; the
    agent builds an idea into a digital artifact: software, chip design, 3D model;
    evaluated on artifact quality).
  - **Code as Agency: Acting in the Real World** (= former "means" branch; the agent
    uses code to act in the real world, which spans digital and physical; evaluated on
    world-state change).
  - Subtitle preposition locked to **"in"** (2026-07-10): "Acting **in** the Real
    World" — fits "operating from within an environment" better than "on".

### Rejected alternative
- Earlier concern that the "Real World" subtitle over-claims for the Agency branch
  (which includes digital environments like browser/terminal/game); proposed "Acting
  Through Code" instead. **Rejected**: the owner's framing that "the digital world is
  part of the real world" is stronger and does not break the single-axis rule — the
  true L1 axis is always artifact (build an artifact) vs agency (act in a world);
  digital/real is only poetic subtitle flourish and carries no classification weight.

## 2026-07-06: Single-axis-per-level constraint for the new taxonomy

### Background
Diagnosis confirmed the root cause of the old 36-category mis-classification was
**mixing classification axes** (lifecycle-task axis, interaction-surface axis,
output-domain axis, and resource/meta axis all flattened onto one plane): categories
were non-exclusive, so the LLM had no single correct answer. Referenced
[Awesome-Code-as-Agent-Harness-Papers](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers)
and its survey *Code as Agent Harness* (arXiv:2605.18747).

### Locked constraint
- **Each level may use exactly one classification axis; sibling categories at a level
  must be conceptually parallel and mutually exclusive.**
- An earlier mixed-axis top-level proposal (Foundations / Environments / SE Agents /
  Code-as-Action / Creative / Products) was **rejected**: the six groups came from five
  different axes, replicating the old disease at the top level.

### Chosen skeleton (direction approved; full definitions now in taxonomy.json)
- L1 axis = the role of code in the task: **Code as Artifact** (success measured on
  code-artifact quality) vs **Code as Agency** (success measured on external
  world-state change).
- L2 axis (Artifact branch) = the domain of the code artifact: general software / web /
  database / systems software / hardware / game / graphics & animation / 3D-CAD.
- L2 axis (Agency branch) = the world the agent acts in: terminal-OS / browser / game /
  physical / data / ML experiments / scientific discovery.
- L3 axis (only the general-software node expands) = software-lifecycle activity.
- Orthogonal axes demoted to **tags**, which are **sparse and optional** (finalized
  2026-07-06): tag only when applicable; no tag = a plain method paper (no "method"
  default value — consistent with the README's current badge-rendering logic). Two
  facets, each internally parallel:
  - **Paper type** (tag if applicable, mutually exclusive): survey / empirical / position.
  - **Released artifact** (tag if applicable, multi-select): benchmark / model /
    training-data — these co-occur often (training work commonly ships model + data +
    benchmark together), so they are separate from paper type and not force-single-select.
    An `agent` artifact tag was considered and **rejected** (2026-07-10): almost every
    paper here proposes an agent, so it is near-universal and carries no information;
    "did they release a runnable system" is already implicitly carried by the
    `links.github` field.
  foundation_models → artifact=model, data_synthesis → artifact=training-data,
  multimodal_coding dissolves directly into its domain category. Mechanism tags
  (planning/memory/feedback/multi-agent) and a modality tag (multimodal) were
  **rejected**: mechanisms are inherently multi-label and fuzzy, which would move the
  "no single answer" problem from the category layer to the tag layer; the contribution
  facet is the only near-objective axis an LLM can label stably, and it can drive README
  rendering (e.g. a Foundation Models section generated by filtering artifact=model).
- products **deleted** (2026-07-06): `data/papers_products.yaml` (44 product entries)
  removed along with the already-commented Products & Tools section in the README. The
  repo's scope narrows to **frontier research papers and technical reports**; industry
  product entries are no longer collected (history recoverable via git). Paper count
  corrected from 515 to 471 after deletion.
- terminal's seat in the new scheme: the "terminal/OS world" under the Agency branch,
  parallel to browser and embodied.

### Open questions
- Parallelism of security_engineering / fuzzing on the lifecycle axis (activity vs tag).
- product/agency call for agentic_visualization and MLE (leaning toward "where does the
  evaluation land" → agency; the rule must be written into the classifier prompt).
- The L3 split axis for Agency-branch categories once they grow is undecided.

## 2026-06-20: Serious mis-classification in the category system; plan to redesign

### Problem
The LLM classifier had significant mis-classification. Taking the `terminal` category
as an example:
- Of 17 papers assigned to `terminal` awaiting review, several clearly did not belong
  (e.g. EvoTest, Oversight Has a Capacity, EvoArena, Multi-Agent Computer Use).
- 1 clearly terminal-related paper was mis-assigned to `data_synthesis`.
- 10 terminal papers submitted manually via the inbox failed to land correctly for a
  long time.
- 363 papers were backed up in the retry queue due to failed LLM calls, getting slower
  over time.

### Decision
Pause cron; stop accumulating problems with the current system, and wait until the
system is redesigned before resuming.

### Planned redesign directions (to discuss)
- Classification accuracy: prompt design, category definitions, few-shot examples.
- High LLM failure rate: needs a more stable calling mechanism.
- Retry-queue bloat: needs a more reasonable failure-handling strategy.
- Whether the overall architecture needs adjustment.
