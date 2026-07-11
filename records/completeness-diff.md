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

## Appendix: every written OUT verdict

Consolidated from the migration review sheets before their deletion
(the full sheets remain in git history).

### Full migration run: removed

- [system_engineering] LLM-Empowered Agentic MAC Protocols: A Dynamic Stackelberg Game Approach: Code is neither the deliverable nor clearly the language of agentic action; this is a wireless-networking control paper, not a code agent.
- [system_engineering] OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use: These agents act primarily via GUI grounding rather than writing or executing code, so code is neither the product nor the language of action.
- [game_generation] Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning: No agent writes/executes code as product or action; it is VLM reasoning training data, out of scope.
- [qa] Can LLMs Replace Manual Annotation of Software Engineering Artifacts? (owner ruling)
- [animation_generation] LiveSVG: Zero-Shot SVG Animation via Video Generation: No LLM agent writes or executes code; the method uses differentiable rendering fitting rather than agentic code generation, so it is out of scope.
- [3d_object_design] HSM: Hierarchical Scene Motifs for Multi-Scale Indoor Scene Generation: No agentic code generation or execution is described; the scene generation process is not code-based, so it falls outside scope.
- [3d_object_design] How Can Large Language Models Help Humans in Design and Manufacturing?: No agentic code-writing/execution focus; broad exploratory position paper on LLM capabilities, excluded per scope.
- [code_executing_web] Tree-of-Code: A Self-Growing Tree Framework for End-to-End Code Generation and Execution in Complex Tasks (owner ruling)
- [code_executing_game] Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents: Agent acts via keyboard-mouse control signals, not by writing or executing code, so it falls outside the code-agent scope.
- [code_executing_embodied] Robo-Blocks: Generative Scaffolding in End-User Design and Programming of Social Robots (owner ruling)
- [code_executing_embodied] MORSE-500: A Programmatically Controllable Video Benchmark to Stress-Test Multimodal Reasoning: No agent writes or executes code to perform a task; code is only used to generate benchmark stimuli, not as agentic action or deliverable.
- [code_executing_embodied] Chain-of-Modality: Learning Manipulation Programs from Multimodal Human Videos with Vision-Language-Models: No code generation or execution by an agent; task plans/parameters are extracted via multimodal prompting, not code as action.
- [code_executing_embodied] Visual Agentic AI for Spatial Reasoning with a Dynamic API: Resembles code-as-reasoning-aid (PoT/PAL style) for visual QA rather than an agent acting in a world, which is explicitly out of scope.
- [code_executing_embodied] Can Large Language Models Understand Symbolic Graphics Programs?: No agent writes or executes code to accomplish a task; this is a comprehension/evaluation study of LLM reasoning about program semantics.
- [code_executing_embodied] Endowing Visual Reprogramming with Adversarial Robustness: No agent, no code artifact or code-as-action task involved.
- [code_executing_embodied] Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multimodal Data Generation: Serves general VLM training for image understanding rather than a code-artifact or code-as-agency task, so it falls outside scope.
- [code_executing_embodied] Visual Program Distillation: Distilling Tools and Programmatic Reasoning into Vision-Language Models: Code generation is used only as a reasoning aid for visual QA, not as an agent completing a real-world task.
- [code_executing_embodied] Recursive Visual Programming: Program generation serves as a reasoning tool for visual QA, matching the excluded PAL/PoT-style reasoning-aid pattern.
- [code_executing_embodied] Video Question Answering with Procedural Programs: Code is a reasoning aid for answering questions, not an agent acting in the world or producing a code artifact.
- [code_executing_embodied] Visual Programming: Compositional visual reasoning without training: Program generation is a reasoning/tool-composition aid for visual tasks, not an agent acting in a real-world environment.
- [code_executing_embodied] ViperGPT: Visual Inference via Python Execution for Reasoning: Code generation serves as a compositional reasoning tool for visual QA, matching the reasoning-aid exclusion.
- [code_executing_embodied] ViStruct: Visual Structural Knowledge Extraction via Curriculum Guided Code-Vision Representation: Code is used only as a representation format for training a perception model, not as an agent's action or a produced software artifact.
- [code_executing_embodied] Modular Visual Question Answering via Code Generation: Code generation is a reasoning aid for visual question answering, excluded as non-agentic tool use.
- [machine_learning_engineering] We Got Claude to Fine-Tune an Open Source LLM: Appears to be an industry blog/product write-up rather than a frontier research paper.
- [scientific_workflows] MPMWorlds: Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics: Single-shot code generation for physics modeling with no agentic interaction; falls under reasoning-aid exclusion, not an agent task.
- [agentic_visualization] Chart-CoCa: Self-Improving Chart Understanding of Vision LMs via Code-Driven Synthesis and Candidate-Conditioned Answering: Code is used only as an internal tool to synthesize training data for chart understanding, not as the task's deliverable or an agentic action, so it falls outside scope.
- [data_synthesis] AgentGen: Enhancing Planning Abilities for Large Language Model based Agent via Environment and Task Generation: No code-generation or code-as-action task is specified; excluded as out of scope for the code-agent collection.
- [code_generation] Multi-Agent Collaboration via Evolving Orchestration (owner ruling)

### Post-review corrections (2026-07-11, owner)

- Tree-of-Code: reinstated -> world_general. ACL page confirms CodeAct-style agentic
  execution (agent generates AND executes code as actions); the OUT verdict was made
  from a stale second-hand summary.
- Chain-of-Modality: reinstated -> world_physical. Owner has read the paper: it
  executes generated Manipulation Programs (code) as robot actions; the abstract
  understates the mechanism.
- SWE-Compass: software_general -> software_debugging. SWE-style unified coding
  evaluations are issue-resolution family; "unified" branding is not cross-activity.
- General semantics clarified by owner: general = research on the general form of the
  task that fits no specific leaf, NOT an overviews bin; when a specific class emerges,
  split it out. Ordering rule: categories by size desc, general always last.
- 144 arXiv venues corrected to the true v1 upload month (arXiv YYYY/MM from the
  `published` field).

### OUT rows from refetch-reclass.md

| OUT | **OUT** | primary | Can LLMs Replace Manual Annotation of Software Engineering Artifa | owner ruling |
| software_review | **OUT** <- CHANGED | title-only | Armchair | Insufficient information to determine relevance or category. |
| software_review | **OUT** <- CHANGED | primary | Can We Benchmark Code Review Studies? A Systematic Mapping Study  | Not an agent paper that writes or executes code; it is a meta-analysis of research methodo |
| world_general | **OUT** <- CHANGED | primary | APIGen: Automated PIpeline for Generating Verifiable and Diverse  | Serves function/tool-calling capability rather than code-writing or code-execution agency, |
| OUT | **OUT** | primary | Visual Agentic AI for Spatial Reasoning with a Dynamic API | Code is used purely as a reasoning aid for answering visual questions, matching the exclud |
| OUT | **OUT** | title-only | Endowing Visual Reprogramming with Adversarial Robustness | No code-writing or code-acting agentic task is indicated by the title; falls outside scope |
| OUT | **OUT** | primary | Recursive Visual Programming | Code is generated purely as a reasoning aid to answer visual questions, matching the exclu |
| OUT | **OUT** | title-only | Video Question Answering with Procedural Programs | Code serves as a reasoning tool for question answering rather than an agentic real-world t |
| OUT | **OUT** | primary | Modular Visual Question Answering via Code Generation | Code is a reasoning aid composing model calls to answer questions, matching the excluded P |
| OUT | **OUT** | primary | We Got Claude to Fine-Tune an Open Source LLM | Industry blog post with no described agentic code-production or code-action task; out of s |
| software_general | **OUT** <- CHANGED | primary | Introducing: Devstral 2 and Mistral Vibe CLI | Industry product announcement, excluded per scope rules against industry products/technica |
| OUT | **OUT** | primary | AgentGen: Enhancing Planning Abilities for Large Language Model b | No code artifact or code-as-action task involved; generic planning agent training falls ou |
| software_general | **OUT** <- CHANGED | primary | AgentVerse: Facilitating Multi-Agent Collaboration and Exploring  | General multi-agent framework not focused on code as artifact or action, out of scope. |

### OUT rows from reclass-general.md

| software_studies | **OUT** <- CHANGED | AgentSPEX: An Agent SPecification and EXecution Language | A general-purpose agent orchestration/workflow language not focused on code as artifact or as t |

### OUT rows from reclass-studies.md

| software_studies | **OUT** <- CHANGED | AgentSPEX: An Agent SPecification and EXecution Language | A general-purpose agent orchestration/workflow language not focused on code as artifact or as t |

### OUT rows from inbox-run.md

| **OUT** | Function2Scene: 3D Indoor Scene Layout from Functional Specifi | No code artifact or code-as-action is produced; out of scope for a code-agent list. |
| **OUT** | MORSE-500: A Programmatically Controllable Video Benchmark to  | No agent writes or executes code as its task; out of scope per exclusion of non-agentic reasoni |
| **OUT** | Program-as-Weights: A Programming Paradigm for Fuzzy Functions | Not an agentic task or code-producing/code-acting paper; it compiles specs to neural weights ra |

### OUT rows from world_general-abolished.md

| **OUT** | EvoAgentX: An Automated Framework for Evolving Agentic Workf | A general multi-agent orchestration framework not centered on code as artifact or as the l |

