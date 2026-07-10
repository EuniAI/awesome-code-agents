# Design Decisions

> Durable record of non-trivial design decisions for this repo. Newest first.
> This repo is English-only — keep every entry in English.

## 2026-07-10: List vision and L1 naming (Code as Everything)

### Vision (the list's thesis, to sit at the top of the README)
> **Code as Everything** — as agents reach into reality, code becomes the substrate
> the world runs on: the medium through which intelligence *builds the digital world*
> and *acts in the real one*.

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

### Chosen skeleton (direction approved; details in redesign/taxonomy-v2.md)
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
