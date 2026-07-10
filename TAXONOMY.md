# Taxonomy — Awesome Code Agents

> The authoritative definition of this repo's category system. This file is the **single
> source of truth**: `automation/config.yaml` is kept in sync from it, and it drives both
> the README structure and the auto-classifier. Rationale and history live in
> [design-decisions.md](design-decisions.md).

## How this taxonomy works

- **Vision — Code as Everything.** We collect every strong paper in which an agent writes
  or runs code, across all domains. Code is either the *thing being built* or the
  *language of action*; that split is Level 1.
- **Single-axis rule.** Each level divides on exactly one axis. Sibling categories at a
  level are conceptually parallel and mutually exclusive.
- **Name vs definition.** Each node has a human-facing `title` and a separate,
  machine-facing definition block (`Definition` / `Includes` / `Boundary` / `Examples`).
  The title carries the vision; the definition block is the classifier's contract. The
  `Boundary` lines — "if X, it belongs to sibling Y instead" — are what prevent
  mis-classification.
- **Stable keys.** Every node has a `key` (ASCII, lowercase). Keys never change even when
  a title is reworded; data files, README markers, and the classifier all reference keys.
- **Tags are orthogonal and sparse** (not categories). Tag only when it applies:
  - *Paper type* (mutually exclusive): `survey` / `empirical` / `position`.
  - *Released artifact* (multi-select): `benchmark` / `model` / `training-data`.

---

## Level 1 — the role of code

**Axis:** where the paper's success is measured. This is the master test; apply it first.

### 🧱 Code as Artifact — Building the Digital World &nbsp;`key: artifact`

**Definition.** The agent's deliverable *is* a code artifact, and the paper's success is
measured by the quality or correctness of that artifact itself — does the code compile,
pass tests, meet the spec, resolve the issue, match the design.

**Includes.** Agents that write, complete, test, debug, localize, review, or maintain
software; and agents that generate other digital artifacts — web apps, database queries,
systems software, hardware/HDL, games, graphics, animations, 3D/CAD models — where the
output is judged on its own merits.

**Boundary.**
- If success is measured by a change in some external world's state (a task completed, a
  game won, a robot moved, an experiment's result, a dataset analyzed) rather than by the
  artifact's quality → **agency**.
- Static output that is inspected as an artifact → artifact; code that is *run to act or
  interact* in a world → agency. (E.g. a static chart is artifact; an interactive,
  dynamic visualization is agency.)

**Examples.**
- SWE-bench-style issue resolution — the patch is judged by whether tests pass. → artifact
- Text-to-SQL generation — judged by query correctness. → artifact
- RTL/HDL generation — judged by whether the chip passes verification. → artifact

### 🌍 Code as Agency — Acting in the Real World &nbsp;`key: agency`

**Definition.** The agent uses writing and running code as a *means of action*, and the
paper's success is measured by the resulting change in an external world's state — digital
or physical — not by the code's own quality. The digital world (terminals, browsers,
games) is part of the real world; acting there produces real consequences.

**Includes.** Agents that operate terminals and operating systems, drive web browsers,
play in game worlds, control robots and the physical world, or autonomously run data
analysis, machine-learning experiments, and scientific discovery — anywhere code is the
lever and the outcome lives outside the code.

**Boundary.**
- If the deliverable is a code artifact judged on its own quality → **artifact** (see the
  master test above).
- Producing game code → artifact (game development); playing a game by executing code →
  agency. Writing a data-viz artifact → artifact; running an interactive/dynamic
  visualization or dashboard → agency.

**Examples.**
- A terminal agent completing enterprise automation tasks — judged by task completion. → agency
- An embodied agent executing code to move a robot — judged by the physical outcome. → agency
- An ML-engineering agent running a training pipeline — judged by model performance. → agency

---

## Level 2 — *(to be defined)*

Two independent sub-axes, one per Level-1 branch:
- Under **artifact**: the domain of the code artifact.
- Under **agency**: the world the agent acts in.

## Level 3 — *(to be defined)*

Only the general-software node under **artifact** expands, on a software-lifecycle axis.
