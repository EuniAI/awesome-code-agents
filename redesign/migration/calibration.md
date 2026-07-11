# Migration calibration batch

34 papers, mixed clean/messy old buckets, classified by `claude-sonnet-5`.
Review guide: `->` marks the proposed new leaf; `OUT` means proposed as out of
scope; `FAILED` means the classifier gave no valid verdict. Reply with
corrections by row number.

| # | old bucket | proposed | tags | title | reason |
|---|---|---|---|---|---|
| 1 | sql_engineering | **database** | benchmark | BADGER: Bridging Agentic and Deterministic Evaluation for Generative E | Serves text-to-SQL query generation task, so classified as database despite added agentic evaluation component |
| 2 | sql_engineering | **database** | benchmark | Agent Bain vs. Agent McKinsey: A New Text-to-SQL Benchmark for the Bus | Ultimate purpose is generating SQL queries, matching the database leaf definition. |
| 3 | hardware_engineering | **hardware** | - | Focus: Better Verilog Generation from Large Language Model via Focused | Produces hardware description (Verilog) code, matching the hardware leaf. |
| 4 | code_executing_embodied | **OUT** | - | Robo-Blocks: Generative Scaffolding in End-User Design and Programming | No autonomous agent writes/executes code to complete a task; it is an HCI end-user tool study, out of scope. |
| 5 | code_executing_embodied | **world_physical** | model | RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis | Code is the tool for controlling a robot's physical actions, matching world_physical rather than a code artifa |
| 6 | code_executing_web | **world_apps** | benchmark | OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents | Agents operate applications/tools within a computer-use environment, matching world_apps definition. |
| 7 | code_executing_web | **OUT** | - | Tree-of-Code: A Self-Growing Tree Framework for End-to-End Code Genera | Fits the PAL/PoT-style exclusion where code is emitted merely as a reasoning tool with no agentic task. |
| 8 | pull_request_review | **software_review** | empirical | Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and  | Served task is judging and reviewing code changes, matching software_review. |
| 9 | qa | **OUT** | - | Can LLMs Replace Manual Annotation of Software Engineering Artifacts? | No agent writes or executes code to accomplish a task; it's a meta-research/methodology study, out of scope. |
| 10 | 3d_object_design | **cad** | benchmark | Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agenti | Deliverable is 3D scene code (Blender program), matching the cad leaf definition. |
| 11 | 3d_object_design | **cad** | - | CAD-Llama: Leveraging Large Language Models for Computer-Aided Design  | Produces CAD program code as the deliverable, matching the cad leaf. |
| 12 | code_generation | **world_terminal** | survey | Code as Agent Harness | A cross-domain survey advocating code-as-action infrastructure for agents is classified under agency per the c |
| 13 | code_generation | **software_maintenance** | benchmark | SlopCodeBench: Community driven benchmark for measuring code erosion u | Concerned with preserving code quality through iterative evolution, matching software_maintenance. |
| 14 | code_generation | **software_code_generation** | - | SEW: Self-Evolving Agentic Workflows for Automated Code Generation | The served task is producing code from specifications via optimized agentic workflows, i.e. code generation. |
| 15 | code_generation | **OUT** | - | Multi-Agent Collaboration via Evolving Orchestration | Generic multi-agent orchestration without code as the deliverable or action language falls outside scope. |
| 16 | code_generation | **software_code_generation** | benchmark | RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems | Repository-aware code completion is a code-generation task per the taxonomy's explicit example. |
| 17 | issue_resolution | **software_debugging** | - | Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis | Provides dynamic analysis to diagnose and repair reported issues, matching debugging & issue resolution. |
| 18 | issue_resolution | **software_debugging** | - | InfCode: Adversarial Iterative Refinement of Tests and Patches for Rel | End-to-end reproduction, diagnosis, and repair of reported issues is core issue resolution. |
| 19 | issue_resolution | **software_general** | benchmark | SWE-PolyBench: A multi-language benchmark for repository level evaluat | Spans multiple lifecycle activities (bugs, features, refactoring) with no single one dominating, matching the  |
| 20 | issue_resolution | **software_debugging** | training-data | Agent-RLVR: Training Software Engineering Agents via Guidance and Envi | The downstream task trained for is SWE-bench issue resolution, so it follows that leaf plus training-data tag. |
| 21 | issue_resolution | **software_debugging** | - | PatchPilot: A Cost-Efficient Software Engineering Agent with Early Att | Issue resolution pipeline on SWE-bench is a debugging/patching task. |
| 22 | terminal | **world_terminal** | benchmark | TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks | Benchmark of terminal-native agent tasks, the terminal/OS is the agent's world. |
| 23 | terminal | **world_terminal** | training-data | TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis fo | Training-data resource serving terminal-task agents. |
| 24 | terminal | **world_terminal** | training-data | Learning CLI Agents with Structured Action Credit under Selective Obse | CLI/terminal interaction as the agent's world of action, resource for terminal agents. |
| 25 | foundation_models | **software_general** | model | CWM: An Open-Weights LLM for Research on Code Generation with World Mo | Broad code foundation model spanning multiple software lifecycle tasks, no single activity dominates. |
| 26 | foundation_models | **software_general** | model | Qwen3-Coder: Agentic Coding in the World | Generalist agentic coding foundation model spans multiple software tasks. |
| 27 | data_synthesis | **software_debugging** | training-data,benchmark | R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open | Resource paper whose downstream task is issue resolution on SWE-bench. |
| 28 | data_synthesis | **software_debugging** | training-data | RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End  | Training-data/environment resource serving SWE-bench issue-resolution agents. |
| 29 | data_synthesis | **software_development** | training-data,benchmark | SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Mann | Task is incremental feature/requirement implementation guided by tests, matching feature development. |
| 30 | multimodal_coding | **software_code_generation** | training-data,benchmark | VisCodex: Unified Multimodal Code Generation via Merging Vision and Co | Purpose is producing code from multimodal specifications, a code-generation task. |
| 31 | multimodal_coding | **world_terminal** | benchmark | GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Thr | Agents use code repositories as tools to complete real-world tasks (task success, not code artifact, is the de |
| 32 | machine_learning_engineering | **software_general** | benchmark | PithTrain: A Compact and Agent-Native MoE Training System | Served task is agent-friendly software framework design and cross-activity agent efficiency on a codebase, mat |
| 33 | machine_learning_engineering | **world_research** | - | AIDE: AI-Driven Exploration in the Space of Code | The agent's code is the instrument for training/tuning ML models, an MLE-engineering task that belongs to worl |
| 34 | agentic_visualization | **software_code_generation** | model,training-data | JanusCoder: Towards a Foundational Visual-Programmatic Interface for C | A resource paper whose downstream task is producing code (across visual/code domains) from specifications, fit |

## Rulings (owner + evidence audit, 2026-07-11)

- Structural fix: agency branch gained a general leaf, `world_general` (General-Purpose
  Action Agents), mirroring software_general's admission rule. Motivated by row 12.
- Row 12 Code as Agent Harness: world_general + survey (was shoehorned into world_terminal).
- Rows 4, 7, 9, 15: OUT confirmed (Robo-Blocks HCI tool study; Tree-of-Code PAL-style
  reasoning; manual-annotation methodology study; generic multi-agent orchestration).
- Row 31 GitTaskBench: world_general + benchmark (tasks span 7 domains/modalities; no
  single world dominates; abstract-verified).
- Row 32 PithTrain: systems + benchmark (builds an MoE training framework, i.e. systems
  infrastructure code; abstract-verified).
- Row 13 SlopCodeBench: software_development + benchmark (iterative spec-refinement
  development; medium confidence, no abstract available; recheck at full migration).
- Row 24 sigma-Reveal CLI agents: keep world_terminal, drop training-data tag (RL method
  paper; no released dataset stated).
- Row 30 VisCodex: add model tag (releases model + dataset + benchmark; all three tags).
- Row 5 RoboCodeX: keep world_physical + model (no abstract; consistent with known work).
- All other rows: accepted as classified.
