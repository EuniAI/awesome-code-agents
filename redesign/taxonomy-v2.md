# Taxonomy v2 — Redesign Spec (draft, under alignment)

> Status: **DRAFT** working spec; items marked ⚖️ await the owner's decision. Decision
> history in [design-decisions.md](../design-decisions.md).
> **Category definitions are now maintained in [taxonomy.json](../taxonomy.json) (single
> source of truth); where this draft differs, taxonomy.json wins.** In particular, the
> L1 rule here ("where evaluation lands") is superseded: classify by the task the paper
> serves.

## Vision (the list's thesis, to sit at the top of the README)

> **Code as Everything.**
> The digital world we build. The real world we act in.

As agents touch reality, code is becoming a core element of how the world runs, no longer
confined to the digital realm. The digital world is part of the real world: acting in a
terminal, a browser, or a game is just as much real-world activity. The two sentences map
to the two L1 chapters (Building the Digital World / Acting in the Real World).

## 0. Design principles (locked)

1. **Each level uses exactly one classification axis; siblings at a level are
   conceptually parallel and mutually exclusive** (single-axis rule).
2. Repo scope: **frontier research papers and technical reports**; no industry product
   entries.
3. Inclusion boundary: any good paper where an agent uses writing/executing code as its
   means of action, across all domains (including CAD, robotics, etc.).
4. Tags are sparse and optional; every orthogonal dimension goes to tags, never a
   category seat.

## 1. Classification tree (23 leaf categories, down from 36)

The dividing axis of each level is stated explicitly; **leaf = classifier target = data
file**. Internal machine keys use short names `artifact` / `agency`; the README shows the
full display titles.

```
L1 axis: the role of code in the task (where the evaluation lands)
│
├── 🧱 artifact — Code as Artifact: Building the Digital World (evaluated on artifact quality)
│   L2 axis: the domain of the code artifact
│   ├── software — general software
│   │   L3 axis: software-lifecycle activity
│   │   ├── software_feature_development   ← feature_development (5)
│   │   ├── software_code_authoring        ← code_generation (62) + code_completion (4)
│   │   ├── software_testing               ← agentic_fuzzing (4) + issue_reproduction (17)
│   │   ├── software_debugging             ← issue_localization (12) + issue_resolution (134)
│   │   ├── software_code_review           ← pull_request_review (11)
│   │   ├── software_code_comprehension    ← qa (4)
│   │   ├── software_maintenance           ← refactoring (1) + migration (7) + perf_opt (3)
│   │   ├── software_security ⚖️           ← software_security_engineering (9)
│   │   └── software_infrastructure        ← environment_building (17) + git_management (1)
│   ├── web_generation                     ← website_generation (18) + backend_generation (1)
│   ├── database_engineering               ← sql_engineering (10)
│   ├── systems_software                   ← system_engineering (3)
│   ├── hardware_engineering               ← hardware_engineering (1)
│   ├── game_generation                    ← game_generation (3)
│   ├── graphics_animation                 ← svg_generation (1) + animation_generation (4)
│   │                                         + agentic_visualization (5) ⚖️
│   └── cad_3d                             ← 3d_object_design (25)
│
└── 🌍 agency — Code as Agency: Acting in the Real World (evaluated on world-state change)
    L2 axis: the world the agent acts in (spanning digital and physical)
    ├── world_terminal                     ← terminal (18, needs cleanup to new definition)
    ├── world_browser                      ← code_executing_web (10)
    ├── world_game                         ← code_executing_game (5)
    ├── world_physical                     ← code_executing_embodied (23)
    ├── world_data                         ← automated_data_science (5)
    ├── world_ml_experiments               ← machine_learning_engineering (22)
    └── world_science                      ← scientific_workflows (2)
```

**Old categories dissolved into tags, re-classified paper by paper** (~24 papers to
review by hand):

- `foundation_models` (4) → into a domain leaf by topic + tag `model`
- `data_synthesis` (13) → into its target domain + tag `training-data`
- `multimodal_coding` (7) → per-paper by domain (screenshot-to-code → `web_generation`)

**Deleted**: `products` (44, removed 2026-07-10, recoverable via git).

### Key decision rules (to be written into the classifier prompt)

- **artifact vs agency**: look at where the paper's success is measured — quality/
  correctness of the code artifact itself → artifact; state/task-completion of an
  external world → agency.
- **game_generation vs world_game**: produces game code → the former; plays a game by
  executing code → the latter.
- **world_terminal inclusion bar**: the contribution is the terminal/OS *as the agent's
  environment or world* (terminal benchmarks, terminal-specific methods); a SWE paper
  that merely happens to run in a terminal goes to its task category.

## 2. Tag system (locked)

Sparse; tag if applicable; nothing applies = no tag (a plain method paper):

| Facet | Values | Rule |
|---|---|---|
| Paper type | `survey` / `empirical` / `position` | mutually exclusive, single |
| Released artifact | `benchmark` / `model` / `training-data` | multi-select, often co-occur |

Reuses the existing `tags:` list field in YAML (badge rendering already exists; no schema
change).

## 3. Repo file-architecture changes

### config.yaml

- Flat `categories:` → nested `taxonomy:`; each node has `title` (README section
  heading), `axis` (that level's dividing-axis note), `definition` (classifier-facing
  text), and `children`.
- A leaf node's key is the data-file suffix (`data/papers_{key}.yaml`).
- The `tags:` block becomes the two facet definitions.

### data/

- 36 files → 23 files; merges/renames done in one scripted pass; the ~24 dissolved-
  category papers filed by hand.
- Entry schema unchanged (title/authors/venue/summary/tags/links).

### README.md

- Structure generated from the `taxonomy:` tree: L1 two chapters → L2 domain/world
  sections → L3 lifecycle subsections (software only).
- Quick Navigation generated from the same tree.
- ⚖️ The current standalone "🌍 Foundation Models" section is removed; those papers go
  into their domain categories, flagged by the `model` badge (fallback: keep one section
  auto-generated by tag filter).

### scripts/

- `render_papers.py`: iterate the taxonomy tree instead of the flat category list
  (section titles, depth, and order all taken from the tree).
- `update_papers_badge.py`: no material change (still counts data/*.yaml).

### automation/ (classifier side)

- Rewrite the `classifier/llm.py` prompt as a **hierarchical decision**: relevance → L1
  binary choice (with the where-does-evaluation-land rule) → leaf within the branch
  (showing only sibling definitions, shrinking the choice space from a flat 36 to
  2→8/7→9) → sparse tags. Each confusable boundary gets a few-shot example.
- LLM failure rate / retry-queue bloat is a separate second phase, out of scope for this
  classification redesign, but the queue must be reset afterward (see migration plan).

## 4. Migration plan (dependency order)

1. **Finalize this spec** (clear all ⚖️).
2. Write the new taxonomy + tag definitions into config.yaml.
3. Script the data/ file migration (mechanical merge/rename); in the same pass, hand-file
   the 24 dissolved papers and clean up the 18 terminal papers (⚖️ handle the 9 security
   and 5 visualization papers per the decisions).
4. Update `render_papers.py`; regenerate the README (structure + Quick Navigation + count).
5. Rewrite the classifier prompt + few-shot; small-sample back-test (sample already-filed
   papers to check classification consistency).
6. **State and backlog handling** ⚖️: the 271 pending GitHub Issues were generated under
   the old scheme — recommend closing them all as void; clear the 705-entry retry queue;
   re-run affected papers through the new classifier. Keep `processed_ids` for dedup.
7. Resume cron.

## 5. Decisions pending ⚖️

| # | Question | Options | Leaning |
|---|---|---|---|
| 1 | security, 9 papers | keep a `software_security` leaf vs split by actual task (fuzzing→testing, patching→debugging) | split is purer, keeping is easier |
| 2 | visualization, 5 papers | `graphics_animation` (chart is the artifact) vs `world_data` (chart is an analysis by-product) | graphics_animation, re-check each on migration |
| 3 | code_authoring, 66 papers | split now vs wait for artifact tags, then decide by distribution | don't split yet |
| 4 | Foundation Models README section | remove (badge only) vs a tag-driven auto section | remove |
| 5 | backlog handling | close all 271 pending Issues + clear retry + re-run vs rescue one by one | close & re-run |
| 6 | leaf key naming | the `software_*` / `world_*` prefix scheme | as above; can rename wholesale |
```
