# Full migration run


## sql_engineering

| proposed | tags | title | reason |
|---|---|---|---|
| **database** | - | BADGER: Bridging Agentic and Deterministic Evaluation for Generative E | Serves text-to-SQL query generation and evaluation, a database-domain artifact task. |
| **database** | - | Learning to Retrieve: Dual-Level Long-Term Memory for Text-to-SQL Agen | The served task is producing SQL through interactive agents, a database artifact task. |
| **database** | empirical | Rethinking Agentic Workflows: Evaluating Inference-Based Test-Time Sca | Task purpose is producing SQL queries, placing it in the database artifact domain. |
| **database** | - | AGENTIQL: An Agent-Inspired Multi-Expert Framework for Text-to-SQL Gen | Deliverable is SQL query generation, a database artifact task. |
| **database** | training-data | MTSQL-R1: Towards Long-Horizon Multi-Turn Text-to-SQL via Agentic Trai | Deliverable is executable SQL queries, a database artifact task; releases training trajectories. |
| **database** | benchmark | Agent Bain vs. Agent McKinsey: A New Text-to-SQL Benchmark for the Bus | Benchmark whose downstream task is SQL query generation, a database artifact task. |
| **world_research** | - | Agentic generative AI for media content discovery at the national foot | The generated query is a tool for content discovery/insight, not the deliverable itself, matching da |
| **graphics** | benchmark | Towards Reliable Agentic Progressive Text-to-Visualization with Verifi | Delivers visualization query code from an evolving specification, matching chart-from-spec graphics  |
| **database** | benchmark,training-data | SWE-SQL: Illuminating LLM Pathways to Solve User SQL Issues in Real-Wo | Debugging task targets SQL code specifically, which stays under the domain-specific database leaf ra |
| **world_research** | - | GateLens: A Reasoning-Enhanced LLM Agent for Automotive Software Relea | Generated code is the tool for tabular data analysis whose purpose is delivering analytical insight, |

## hardware_engineering

| proposed | tags | title | reason |
|---|---|---|---|
| **hardware** | - | Focus: Better Verilog Generation from Large Language Model via Focused | Task produces hardware description (Verilog) code, matching the hardware artifact domain. |

## system_engineering

| proposed | tags | title | reason |
|---|---|---|---|
| **OUT** | - | LLM-Empowered Agentic MAC Protocols: A Dynamic Stackelberg Game Approa | Code is neither the deliverable nor clearly the language of agentic action; this is a wireless-netwo |
| **systems** | - | Man-Made Heuristics Are Dead. Long Live Code Generators! | The task's ultimate purpose is producing systems-level code (kernel-integrated policies), matching a |
| **OUT** | - | OS Agents: A Survey on MLLM-based Agents for General Computing Devices | These agents act primarily via GUI grounding rather than writing or executing code, so code is neith |

## game_generation

| proposed | tags | title | reason |
|---|---|---|---|
| **game** | - | 90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development | Produces a playable game's codebase from scratch, matching the game artifact domain. |
| **OUT** | - | Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' G | No agent writes/executes code as product or action; it is VLM reasoning training data, out of scope. |
| **game** | benchmark | Agents in the Sandbox: End-to-End Crash Bug Reproduction for Minecraft | Testing/reproducing bugs in a game to serve the game's own codebase falls under the game artifact do |

## software_security_engineering

| proposed | tags | title | reason |
|---|---|---|---|
| **software_security** | model | VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerabi | Task is vulnerability detection/discovery in code, matching software_security. |
| **software_security** | benchmark | SecRepoBench: Benchmarking Code Agents for Secure Code Completion in R | Benchmark for secure code generation/completion falls under software_security. |
| **software_security** | benchmark | From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localiz | Vulnerability localization task fits software_security's vulnerability detection/localization scope. |
| **software_security** | benchmark | SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software | PoC generation and vulnerability patching are core software_security tasks. |
| **software_security** | benchmark | SecureAgentBench: Benchmarking Secure Code Generation under Realistic  | Secure code generation benchmark matches software_security scope. |
| **software_code_generation** | - | Towards Exception Safety Code Generation with Intermediate Representat | Purpose is producing more robust/correct generated code (exception safety), not vulnerability securi |
| **software_security** | - | RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing | Repository-level code auditing for bug/vulnerability discovery matches software_security's auditing  |
| **world_terminal** | benchmark | CVE-Bench: A Benchmark for AI Agents’ Ability to Exploit Real-World We | Offensive exploitation of vulnerabilities is treated like CTF/pentesting, which the taxonomy assigns |
| **software_security** | benchmark | CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ability | Repairing real-world CVEs is the canonical software_security repair task per the taxonomy example. |

## pull_request_review

| proposed | tags | title | reason |
|---|---|---|---|
| **software_review** | empirical | Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and  | Judging and approving code changes at scale is code review, artifact/software_review. |
| **software_review** | benchmark | Benchmarking and Studying the LLM-based Code Review | Benchmark and study targeting automated code review quality falls under software_review. |
| **software_general** | empirical | On the Use of Agentic Coding: An Empirical Study of Pull Requests on G | Cross-activity empirical study of agentic PR contributions spanning multiple lifecycle tasks fits so |
| **software_general** | empirical,training-data | The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonom | A cross-activity resource studying autonomous coding agents' behavior across the whole SE workflow,  |
| **software_review** | - | Issue-Oriented Agent-Based Framework for Automated Review Comment Gene | Generates review comments judging code changes, matching software_review. |
| **software_review** | - | Armchair | Grouped contextually among code review tools, presumed to serve judging code changes (software_revie |
| **software_review** | benchmark | PReview: A Benchmark Dataset for Pull Request Outcomes and Quality Ana | Benchmark dataset serving PR quality/outcome analysis falls under software_review. |
| **software_review** | - | PR-Agent: An AI-Powered Tool for Automated Pull Request Analysis, Feed | Tool for automated PR analysis and feedback directly serves the code review task. |
| **software_review** | - | CodeAgent: Autonomous Communicative Agents for Code Review | Multi-agent system whose task is code review judgment fits software_review. |
| **software_review** | model,benchmark | Automating Code Review Activities by Large-Scale Pre-training | Pretraining and benchmark explicitly serving code review activities (quality estimation, comment gen |
| **software_review** | survey | Can We Benchmark Code Review Studies? A Systematic Mapping Study of Me | Survey of code review benchmarking practices serves the code-review lifecycle activity, matching sof |

## agentic_fuzzing

| proposed | tags | title | reason |
|---|---|---|---|
| **software_testing** | benchmark | Sakura: An Approach for Generating Complex Tests from Natural Language | Proactive test generation task; falls under software_testing. |
| **software_testing** | - | Intention-Driven Generation of Project-Specific Test Cases | Test generation focused on validating intended behavior, i.e., software_testing. |
| **software_testing** | benchmark | UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench | Generating tests to rigorously validate patches is a proactive testing/verification task, not a spec |
| **software_security** | - | Locus: Agentic Predicate Synthesis for Directed Fuzzing | Directed fuzzing aimed at vulnerabilities/bug discovery falls under software_security per the fuzzin |

## code_completion

| proposed | tags | title | reason |
|---|---|---|---|
| **software_code_generation** | benchmark | SpecAgent: A Speculative Retrieval and Forecasting Agent for Code Comp | Repository-aware code completion serves code_generation per taxonomy examples. |
| **software_code_generation** | benchmark | Repoformer: Selective Retrieval for Repository-Level Code Completion | Repo-aware completion falls under software_code_generation per taxonomy. |
| **software_code_generation** | benchmark | Dataflow-Guided Retrieval Augmentation for Repository-Level Code Compl | Repository-level code completion task maps to software_code_generation. |
| **software_code_generation** | benchmark | RepoCoder: Repository-Level Code Completion Through Iterative Retrieva | Repository-level completion is a code_generation task per taxonomy examples. |

## qa

| proposed | tags | title | reason |
|---|---|---|---|
| **OUT** | - | Can LLMs Replace Manual Annotation of Software Engineering Artifacts? | owner ruling (calibration) |
| **software_comprehension** | benchmark | SWE-QA: Can Language Models Answer Repository-level Code Questions? | Task is understanding/answering questions about code repositories, not judging or producing code. |
| **software_comprehension** | benchmark | Benchmarking Long-Context Language Models on Long Code Understanding | Served task is code understanding at scale, matching software_comprehension. |
| **software_comprehension** | - | On Improving Repository-Level Code QA for Large Language Models | Improving repo-level QA serves code comprehension, not judgment or production. |

## website_generation

| proposed | tags | title | reason |
|---|---|---|---|
| **web** | benchmark | I-WebGenBench : Evaluating Interactivity in LLM-Generated Scientific W | Delivered artifact is interactive web application code, so it falls under web. |
| **web** | - | ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic We | Purpose is producing front-end/web code, matching the web leaf. |
| **software_code_generation** | model,training-data | JanusCoder: Towards a Foundational Visual-Programmatic Interface for C | A general code-generation foundation model spanning multiple visual code domains, best fit is code g |
| **web** | - | Automatically Generating Web Applications from Requirements Via Multi- | Delivers a functional full-stack web application, placing it in the web leaf. |
| **web** | benchmark | InteractScience: Programmatic and Visually-Grounded Evaluation of Inte | Task delivers interactive front-end code, so it belongs to the web leaf despite scientific framing. |
| **web** | - | EfficientUICoder: Efficient MLLM-based UI Code Generation via Input an | Purpose is efficient generation of website/UI code, matching the web leaf. |
| **web** | - | WebGen-Agent: Enhancing Interactive Website Generation with Multi-Leve | Delivers a website codebase, so it fits the web leaf. |
| **web** | benchmark,training-data | WebGen-Bench: Evaluating LLMs on Generating Interactive and Functional | Benchmark and training data target website-code generation, placing it in the web leaf. |
| **web** | - | ScreenCoder: Advancing Visual-to-Code Generation for Front-End Automat | Task purpose is producing front-end code from UI designs, matching the web leaf. |
| **web** | benchmark | Interaction2Code: Benchmarking MLLM-based Interactive Webpage Code Gen | Benchmark targets generation of interactive webpage code, fitting the web leaf. |
| **web** | benchmark | DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code G | Benchmark for producing/editing web front-end code, so artifact/web. |
| **web** | - | DesignCoder: Hierarchy-Aware and Self-Correcting UI Code Generation wi | Method that produces web/UI front-end code, so artifact/web. |
| **web** | - | Divide-and-Conquer: Generating UI Code from Screenshots | Task is producing UI code from screenshots, so artifact/web. |
| **web** | benchmark | MLLM-Based UI2Code Automation Guided by UI Layout Information | Produces web front-end code from UI images, with a released benchmark dataset. |
| **web** | benchmark | Design2Code: Benchmarking Multimodal Code Generation for Automated Fro | Benchmark whose downstream task is generating web front-end code. |
| **web** | benchmark | WebMMU: A Benchmark for Multimodal Multilingual Website Understanding  | Benchmark serving generation/editing of web code, artifact/web. |
| **world_browser** | - | UXAgent: An LLM Agent-Based Usability Testing Framework for Web Design | Agents act through a browser to evaluate a live website's usability, not to produce code, so world_b |
| **web** | benchmark | MRWeb: An Exploration of Generating Multi-Page Resource-Aware Web Code | Task and released dataset serve generation of functional multi-page web code, artifact/web. |

## backend_generation

| proposed | tags | title | reason |
|---|---|---|---|
| **web** | benchmark | BaxBench: Can LLMs Generate Correct and Secure Backends? | The served task is generating backend/web application code, so it falls under the web domain despite |

## svg_generation

| proposed | tags | title | reason |
|---|---|---|---|
| **graphics** | - | Chat2SVG: Vector Graphics Generation with Large Language Models and Im | Produces vector-graphic (SVG) code from a specification, matching the graphics leaf definition. |

## animation_generation

| proposed | tags | title | reason |
|---|---|---|---|
| **OUT** | - | LiveSVG: Zero-Shot SVG Animation via Video Generation | No LLM agent writes or executes code; the method uses differentiable rendering fitting rather than a |
| **web** | - | Figma2Code: Automating Multimodal Design to Code in the Wild | Design-to-code generation delivers web front-end code as the artifact, matching the web domain's scr |
| **graphics** | - | LogoMotion: Visually-Grounded Code Synthesis for Creating and Editing  | Produces animation code from a design/logo specification, matching the graphics domain's animation-c |

## 3d_object_design

| proposed | tags | title | reason |
|---|---|---|---|
| **cad** | benchmark | Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agenti | Deliverable is executable Blender code building a 3D artifact, matching the cad boundary. |
| **cad** | - | From Idea to CAD: A Language Model-Driven Multi-Agent System for Colla | Purpose is producing a parametric CAD program, the deliverable is 3D-model code. |
| **cad** | - | CADDesigner: Conceptual Design of CAD Models Based on General-Purpose  | Task's ultimate purpose is generating CAD modeling code, i.e. a 3D artifact. |
| **cad** | benchmark | Agentic Design of Compositional Machines | The task's product is a structural machine design expressed as code, akin to parametric 3D/CAD model |
| **cad** | - | Imperative vs. Declarative Programming Paradigms for Open-Universe Sce | Deliverable is program code constructing a 3D scene layout, matching the 3D/CAD 'scene construction  |
| **cad** | - | Learning Object Placement Programs for Indoor Scene Synthesis with Ite | Purpose is producing placement programs (3D scene construction as code), fitting the cad domain. |
| **OUT** | - | HSM: Hierarchical Scene Motifs for Multi-Scale Indoor Scene Generation | No agentic code generation or execution is described; the scene generation process is not code-based |
| **cad** | training-data | MeshCoder: LLM-Powered Structured Mesh Code Generation from Point Clou | The deliverable is executable Blender code representing a 3D object, matching the cad domain. |
| **cad** | benchmark,training-data | MetaGen: A DSL, Database, and Benchmark for VLM-Assisted Metamaterial  | Downstream task is generating parametric 3D/metamaterial structures as DSL code, fitting cad plus re |
| **cad** | - | ShapeLib: Designing a Library of Programmatic 3D Shape Abstractions wi | Task's purpose is producing reusable programs that construct 3D shapes, matching the cad domain. |
| **graphics** | - | VLMaterial: Procedural Material Generation with Large Vision-Language  | Produces code (procedural material programs) that renders a visual artifact, matching graphics. |
| **cad** | - | Generating CAD Code with Vision-Language Models for 3D Designs | Purpose is producing 3D/CAD code, matching cad domain. |
| **cad** | - | CAD-Llama: Leveraging Large Language Models for Computer-Aided Design  | Produces parametric CAD program code, matching cad domain. |
| **cad** | - | The Scene Language: Representing Scenes with Programs, Words, and Embe | Scene construction as code for 3D artifacts falls under cad. |
| **cad** | benchmark | BlenderGym: Benchmarking Foundational Model Systems for Graphics Editi | Editing 3D scene code via Blender scripting serves the cad domain of 3D artifact production. |
| **cad** | training-data | CAD-Editor: A Locate-then-Infill Framework with Automated Training Dat | Task is editing CAD program code, and the paper contributes synthesized training data for it. |
| **cad** | benchmark | IR3D-Bench: Evaluating Vision-Language Model Scene Understanding as Ag | Agents generate code to reconstruct a 3D scene, matching cad's 3D scene construction focus. |
| **cad** | - | SceneGenAgent: Precise Industrial Scene Generation with Coding Agent | Deliverable is 3D scene code, matching cad domain. |
| **cad** | - | SceneMotifCoder: Example-driven Visual Program Learning for Generating | Produces 3D scene arrangement code from programs, matching cad domain. |
| **cad** | - | 3D-GPT: Procedural 3D Modeling with Large Language Models | Purpose is producing procedural 3D modeling code, matching cad. |
| **cad** | - | SceneGenAgent: Precise Industrial Scene Generation with Coding Agent | Agent produces 3D scene code, matching the cad artifact domain. |
| **cad** | benchmark | CADTalk: An Algorithm and Benchmark for Semantic Commenting of CAD Pro | Lifecycle activity (commenting/documentation) on CAD code stays within the cad artifact domain. |
| **cad** | - | SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code | Produces 3D scene-construction code, matching the cad leaf per its examples. |
| **cad** | - | Open-Universe Indoor Scene Generation using LLM Program Synthesis and  | LLM program synthesis produces 3D scene layout code, fitting the cad artifact domain. |
| **OUT** | - | How Can Large Language Models Help Humans in Design and Manufacturing? | No agentic code-writing/execution focus; broad exploratory position paper on LLM capabilities, exclu |

## issue_reproduction

| proposed | tags | title | reason |
|---|---|---|---|
| **software_debugging** | - | Issue2Test: Generating Reproducing Test Cases from Issue Reports | Issue reproduction is a core debugging/issue-resolution activity. |
| **software_debugging** | - | When Old Meets New: Evaluating the Impact of Regression Tests on SWE I | Serves bug reproduction and patch validation for SWE issue resolution. |
| **software_debugging** | - | Execution-Feedback Driven Test Generation from SWE Issues | Issue reproduction test generation is part of debugging/issue-resolution. |
| **software_testing** | benchmark | Benchmarking LLMs for Unit Test Generation from Real-World Functions | Proactive unit test generation and benchmarking is software_testing, not tied to a reported bug. |
| **software_debugging** | - | AssertFlip: Reproducing Bugs via Inversion of LLM-Generated Passing Te | Bug reproducing test generation is an issue-resolution/debugging task. |
| **software_debugging** | - | Agentic Bug Reproduction for Effective Automated Program Repair at Goo | Bug reproduction integrated with automated program repair is software_debugging. |
| **software_testing** | - | Can LLM Generate Regression Tests for Software Commits? | Proactive regression/fuzzing-oriented test generation not tied to a specific reported issue is softw |
| **software_debugging** | benchmark | Otter: Generating Tests from Issues to Validate SWE Patches | Generating tests from issues to validate patches serves issue resolution/debugging, with a new bench |
| **software_debugging** | - | Automated Generation of Issue-Reproducing Tests by Combining LLMs and  | Issue-reproducing test generation is a debugging/issue-resolution task. |
| **software_debugging** | - | AEGIS: An Agent-based Framework for General Bug Reproduction from Issu | General bug reproduction from issues is core to debugging/issue-resolution. |
| **software_debugging** | empirical | An Empirical Study on Leveraging Images in Automated Bug Report Reprod | Studies reproducing a reported bug, a sub-task of issue resolution (software_debugging). |
| **software_debugging** | - | LLMs as Continuous Learners: Improving the Reproduction of Defective C | Issue reproduction (turning a bug report into a failing repro) falls under software_debugging. |
| **software_debugging** | benchmark | TDD-Bench Verified: Can LLMs Generate Tests for Issues Before They Get | Generating fail-to-pass tests tied to a specific reported issue is issue reproduction, part of softw |
| **software_debugging** | empirical | Evaluating Diverse Large Language Models for Automatic and General Bug | Bug reproduction for known defects is a software_debugging activity. |
| **software_debugging** | benchmark | SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agent | Test generation from bug reports to validate fixes is issue reproduction/validation within software_ |
| **software_debugging** | - | Large Language Models are Few-shot Testers: Exploring LLM-based Genera | Producing failure-reproducing tests for reported bugs is issue reproduction, part of software_debugg |

## issue_localization

| proposed | tags | title | reason |
|---|---|---|---|
| **software_debugging** | - | Improving Code Localization with Repository Memory | Fault localization for issue resolution falls under software_debugging. |
| **software_debugging** | - | Extracting Conceptual Knowledge to Locate Software Issues | Localization of reported issues is fault localization, part of software_debugging. |
| **software_debugging** | - | Leveraging Large Language Model for Information Retrieval-based Bug Lo | Bug localization from reports is fault localization within software_debugging. |
| **software_debugging** | benchmark | A Benchmark for Localizing Code and Non-Code Issues in Software Projec | Benchmark for fault/issue localization serves software_debugging. |
| **software_debugging** | training-data | Tool-integrated Reinforcement Learning for Repo Deep Search | Training method targets issue localization, a software_debugging subtask. |
| **software_debugging** | training-data | SweRank: Software Issue Localization with Code Ranking | Issue localization with a released training dataset falls under software_debugging plus training-dat |
| **software_comprehension** | - | RANGER: Repository-Level Agent for Graph-Enhanced Retrieval | General repository code search/QA/completion spans comprehension and retrieval rather than a single  |
| **software_debugging** | benchmark | Benchmarking and Enhancing LLM Agents in Localizing Linux Kernel Bugs | Fault localization benchmark and enhancement belong to software_debugging. |
| **software_debugging** | - | Bridging Bug Localization and Issue Fixing: A Hierarchical Localizatio | Bug localization feeding into issue fixing is software_debugging. |
| **software_debugging** | - | OrcaLoca: An LLM Agent Framework for Software Issue Localization | Issue localization for repair is software_debugging. |
| **software_debugging** | - | LocAgent: Graph-Guided LLM Agents for Code Localization | Fault localization for a reported defect falls under software_debugging. |
| **software_debugging** | - | Issue Localization via LLM-Driven Iterative Code Graph Searching | Fault localization for reported issues is part of debugging/issue resolution. |

## code_migration

| proposed | tags | title | reason |
|---|---|---|---|
| **software_maintenance** | benchmark | RustRepoTrans: Repository-level Code Translation Benchmark Targeting R | Behavior-preserving cross-language code translation is software_maintenance; benchmark release. |
| **software_maintenance** | - | MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Tran | Validating and repairing code translations is behavior-preserving evolution, i.e. software_maintenan |
| **software_maintenance** | benchmark | MigrationBench: Repository-Level Code Migration Benchmark from Java 8 | Repository migration between language versions is software_maintenance; benchmark release. |
| **software_maintenance** | - | MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Tran | Duplicate entry; validating and repairing code translations is software_maintenance. |
| **software_infrastructure** | empirical | Exploring and Unleashing the Power of Large Language Models in CI/CD C | Translating CI/CD configuration files is CI/CD configuration work under software_infrastructure. |
| **software_maintenance** | training-data | What a diff makes: automating code migration with large language model | Dependency-version migration preserving behavior is software_maintenance. |
| **software_maintenance** | - | AlphaTrans: A Neuro-Symbolic Compositional Approach for Repository-Lev | Repository-level code translation with correctness preservation is software_maintenance. |

## software_refactoring

| proposed | tags | title | reason |
|---|---|---|---|
| **software_maintenance** | - | RefAgent: A Multi-agent LLM-based Framework for Automatic Software Ref | Refactoring is a behavior-preserving code evolution task, matching software_maintenance. |

## performance_optimization

| proposed | tags | title | reason |
|---|---|---|---|
| **software_maintenance** | - | HTAM: Hierarchical Transition-Attended Memory for Operator Optimizatio | Performance optimization of existing GPU operator code is behavior-preserving evolution, matching so |
| **software_maintenance** | - | Controlled Self-Evolution for Algorithmic Code Optimization | Iteratively refining code for better algorithmic complexity/efficiency is performance optimization,  |
| **software_maintenance** | benchmark | SWE-Perf: Can Language Models Optimize Code Performance on Real-World  | Repository-level code performance optimization is behavior-preserving evolution, matching software_m |

## environment_building

| proposed | tags | title | reason |
|---|---|---|---|
| **world_terminal** | benchmark | Large Language Models for IT Automation Tasks: Are We There Yet? | Sysadmin/DevOps automation via shell/config tools matches world_terminal's system administration sco |
| **world_research** | - | Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scient | Enables agentic scientific-tool usage for discovery/research rather than producing code artifacts, m |
| **software_infrastructure** | benchmark | DI-BENCH: Benchmarking Large Language Models on Dependency Inference w | Dependency inference to make repos runnable is enabling/environment-setup work in service of code, i |
| **software_general** | - | AutoDev: Automated AI-Driven Development | Spans multiple lifecycle activities (editing, building, testing, git ops) with no single activity do |
| **software_debugging** | training-data,benchmark,model | R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open | Downstream task served is GitHub issue resolution, i.e. software_debugging plus training-data/benchm |
| **software_infrastructure** | benchmark | Can Language Models Go Beyond Coding? Assessing the Capability of Lang | Task is repairing build failures/toolchain issues, matching software_infrastructure's build-repair s |
| **software_infrastructure** | benchmark | Repo2Run: Automated Building Executable Environment for Code Repositor | Automates environment/build setup for repositories, matching software_infrastructure. |
| **software_infrastructure** | training-data,benchmark | RepoST: Scalable Repository-Level Coding Environment Construction with | Environment construction for code repositories serves software production, matching software_infrast |
| **software_infrastructure** | - | Treefix: Enabling Execution with a Tree of Prefixes | Enables execution of code snippets to support downstream dynamic program analysis, an enabling activ |
| **software_infrastructure** | - | You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Proj | Automates building and running test suites to make code executable, matching software_infrastructure |
| **software_infrastructure** | - | CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Softwar | Environment/build setup enabling code production falls under software_infrastructure. |
| **software_infrastructure** | - | CompileAgent: Automated Real-World Repo-Level Compilation with Tool-In | Compilation/build tasks are enabling work for code, matching software_infrastructure. |
| **software_infrastructure** | benchmark | CSR-Bench: Benchmarking LLM Agents in Deployment of Computer Science R | Deployment/environment setup benchmark serves enabling work, hence software_infrastructure. |
| **software_infrastructure** | benchmark | EnvBench: A Benchmark for Automated Environment Setup | Environment setup benchmark directly serves the enabling/software_infrastructure category. |
| **software_infrastructure** | benchmark | Beyond pip install: Evaluating LLM Agents for the Automated Installati | Dependency installation is environment-setup enabling work, so software_infrastructure. |
| **software_debugging** | benchmark,training-data | R2E: Turning any Github Repository into a Programming Agent Environmen | Downstream task served is repository-level issue resolution/programming agent evaluation, per master |
| **software_infrastructure** | training-data | Automatically Generating Dockerfiles via Deep Learning: Challenges and | Dockerfile generation configures build/execution environments, matching software_infrastructure's CI |

## git_management

| proposed | tags | title | reason |
|---|---|---|---|
| **software_infrastructure** | benchmark | GitGoodBench: A Novel Benchmark For Evaluating Agentic Performance On  | Git operations are enabling work in service of code, matching software_infrastructure's version-cont |

## feature_development

| proposed | tags | title | reason |
|---|---|---|---|
| **software_general** | empirical | Prompting Large Language Models to Tackle the Full Software Developmen | Spans the full lifecycle with no single activity dominating, matching software_general boundary. |
| **software_development** | - | EvoDev: An Iterative Feature-Driven Framework for End-to-End Software  | Task is implementing user-valued features into projects, matching software_development. |
| **software_development** | benchmark | NoCode-bench: A Benchmark for Evaluating Natural Language-Driven Featu | Explicitly matches software_development example: NL-driven feature addition into existing codebases. |
| **software_development** | benchmark | FEA-Bench: A Benchmark for Evaluating Repository-Level Code Generation | Matches given example: repository-level feature implementation benchmark is software_development. |
| **software_debugging** | training-data | SWE-Dev: Building Software Engineering Agents with Training and Infere | Downstream task served is SWE-bench issue resolution, so software_debugging plus training-data tag. |

## code_executing_web

| proposed | tags | title | reason |
|---|---|---|---|
| **OUT** | - | Tree-of-Code: A Self-Growing Tree Framework for End-to-End Code Genera | owner ruling (calibration) |
| **world_apps** | benchmark | OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents | Agents operate software applications via GUI and tool calls, so it belongs to world_apps. |
| **world_browser** | - | SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Ski | Code (APIs) is the tool for completing tasks on live websites, matching world_browser. |
| **world_research** | benchmark | WebDS: An End-to-End Benchmark for Web-based Data Science | The deliverable is data-science insight from interaction, not code or web-app artifacts, matching wo |
| **world_browser** | - | Inducing Programmatic Skills for Agentic Tasks | Programs serve as reusable action skills for completing tasks on the web, matching world_browser. |
| **world_general** | training-data | Executable Code Actions Elicit Better LLM Agents | Advocates code-as-action as a general paradigm spanning many worlds/tasks, matching world_general pe |
| **world_apps** | benchmark | AppWorld: A Controllable World of Apps and People for Benchmarking Int | Agents act through generated code to operate a world of applications, matching world_apps. |
| **world_general** | training-data | APIGen: Automated PIpeline for Generating Verifiable and Diverse Funct | Serves general-purpose tool-use/action agents not tied to a single world, matching world_general wit |
| **world_general** | survey | If LLM Is the Wizard, Then Code Is the Wand: A Survey on How Code Empo | A field-level survey advocating code-as-agency across many domains falls under world_general per the |

## code_executing_game

| proposed | tags | title | reason |
|---|---|---|---|
| **world_game** | position | Develop AI Agents for System Engineering in Factorio | Advocates using a game world as the arena for agents to act and be evaluated, so it serves world_gam |
| **OUT** | - | Game-TARS: Pretrained Foundation Models for Scalable Generalist Multim | Agent acts via keyboard-mouse control signals, not by writing or executing code, so it falls outside |
| **world_game** | benchmark | One Life to Learn: Inferring Symbolic World Models for Stochastic Envi | The programmatic world model serves planning and acting within a game environment, so it belongs to  |
| **world_game** | - | PoE-World: Compositional World Modeling with Products of Programmatic  | The learned code-based world model is the instrument for planning and acting within Atari game envir |
| **world_game** | - | WorldCoder, a Model-Based LLM Agent: Building World Models by Writing  | The synthesized code is a means for the agent to model and act within an interactive (game-like) env |

## code_executing_embodied

| proposed | tags | title | reason |
|---|---|---|---|
| **OUT** | - | Robo-Blocks: Generative Scaffolding in End-User Design and Programming | owner ruling (calibration) |
| **OUT** | - | MORSE-500: A Programmatically Controllable Video Benchmark to Stress-T | No agent writes or executes code to perform a task; code is only used to generate benchmark stimuli, |
| **OUT** | - | Chain-of-Modality: Learning Manipulation Programs from Multimodal Huma | No code generation or execution by an agent; task plans/parameters are extracted via multimodal prom |
| **OUT** | - | Visual Agentic AI for Spatial Reasoning with a Dynamic API | Resembles code-as-reasoning-aid (PoT/PAL style) for visual QA rather than an agent acting in a world |
| **world_physical** | - | Code-as-Monitor: Constraint-aware Visual Programming for Reactive and  | Code is generated and executed as the control/monitoring language for acting on physical robotic sys |
| **world_physical** | training-data | GRS: Generating Robotic Simulation Tasks from Real-World Images | Downstream task served is embodied robot manipulation, so it belongs to world_physical despite being |
| **OUT** | - | Can Large Language Models Understand Symbolic Graphics Programs? | No agent writes or executes code to accomplish a task; this is a comprehension/evaluation study of L |
| **OUT** | - | Endowing Visual Reprogramming with Adversarial Robustness | No agent, no code artifact or code-as-action task involved. |
| **OUT** | - | Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multim | Serves general VLM training for image understanding rather than a code-artifact or code-as-agency ta |
| **world_physical** | benchmark | RoboScript: Code Generation for Free-Form Manipulation Tasks across Re | Generated code is the control language for acting on real/simulated robots, matching world_physical' |
| **world_physical** | - | RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthesis | Code is produced as the means to control a physical robot, fitting the world_physical leaf under the |
| **OUT** | - | Visual Program Distillation: Distilling Tools and Programmatic Reasoni | Code generation is used only as a reasoning aid for visual QA, not as an agent completing a real-wor |
| **OUT** | - | Recursive Visual Programming | Program generation serves as a reasoning tool for visual QA, matching the excluded PAL/PoT-style rea |
| **OUT** | - | Video Question Answering with Procedural Programs | Code is a reasoning aid for answering questions, not an agent acting in the world or producing a cod |
| **world_physical** | - | ChatGPT for Robotics: Design Principles and Model Abilities | Code is generated as the control/action language for physical robots, matching world_physical. |
| **world_physical** | - | ProgPrompt: Generating Situated Robot Task Plans using Large Language  | Generated programs serve as executable action plans controlling embodied/physical robots, i.e., code |
| **world_physical** | - | Code as Policies: Language Model Programs for Embodied Control | Code is explicitly the policy/control language for physical robot action, the canonical world_physic |
| **OUT** | - | Visual Programming: Compositional visual reasoning without training | Program generation is a reasoning/tool-composition aid for visual tasks, not an agent acting in a re |
| **OUT** | - | ViperGPT: Visual Inference via Python Execution for Reasoning | Code generation serves as a compositional reasoning tool for visual QA, matching the reasoning-aid e |
| **OUT** | - | ViStruct: Visual Structural Knowledge Extraction via Curriculum Guided | Code is used only as a representation format for training a perception model, not as an agent's acti |
| **OUT** | - | Modular Visual Question Answering via Code Generation | Code generation is a reasoning aid for visual question answering, excluded as non-agentic tool use. |
| **world_physical** | - | Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions w | Code is the policy language controlling a physical robot, matching world_physical boundary for code- |

## automated_data_science

| proposed | tags | title | reason |
|---|---|---|---|
| **world_research** | survey | LLM-Based Data Science Agents: A Survey of Capabilities, Challenges, a | Serves data-science exploration/insight tasks, which is world_research; survey tag applied. |
| **world_research** | model,training-data | DeepAnalyze: Agentic Large Language Models for Autonomous Data Science | Autonomous data science pipeline delivering insight/reports, not code artifacts, so world_research;  |
| **world_research** | - | AutoMind: Adaptive Knowledgeable Agent for Automated Data Science | Task is automating the data science/ML pipeline for insight and models, matching world_research (MLE |
| **world_research** | benchmark | DA-Code: Agent Data Science Code Generation Benchmark for Large Langua | Benchmark for data-science agent tasks whose purpose is insight/analysis, so world_research; benchma |

## machine_learning_engineering

| proposed | tags | title | reason |
|---|---|---|---|
| **systems** | benchmark | PithTrain: A Compact and Agent-Native MoE Training System | owner ruling (calibration) |
| **world_research** | - | Can We Predict Before Executing Machine Learning Agents? | Agent accelerates ML experimentation/training, an interactive research task, so world_research. |
| **OUT** | - | We Got Claude to Fine-Tune an Open Source LLM | Appears to be an industry blog/product write-up rather than a frontier research paper. |
| **world_research** | - | ArchPilot: A Proxy-Guided Multi-Agent Approach for Machine Learning En | Task is automated ML engineering/experimentation, an interactive research task, so world_research. |
| **world_research** | - | AI Research Agents for Machine Learning: Search, Exploration, and Gene | Serves the task of automated ML experimentation, an interactive research task, so world_research. |
| **world_research** | benchmark | The Automated LLM Speedrunning Benchmark: Reproducing NanoGPT Improvem | Benchmark serves ML research reproduction, an interactive experimentation task, so world_research pl |
| **world_research** | benchmark | MLGym: A New Framework and Benchmark for Advancing AI Research Agents | Framework/benchmark serves ML research agent development, an interactive experimentation task, so wo |
| **world_research** | training-data | Reinforcement Learning for Machine Learning Engineering Agents | Serves ML engineering agents that train models through experimentation, an interactive research task |
| **world_research** | benchmark,training-data | MLE-Smith: Scaling MLE Tasks with Automated Multi-Agent Pipeline | Resource paper whose downstream task is ML engineering agent evaluation/training, an interactive res |
| **software_maintenance** | - | PerfDojo: Automated ML Library Generation for Heterogeneous Architectu | Task is behavior-preserving performance optimization of existing code, matching software_maintenance |
| **world_research** | - | AIDE: AI-Driven Exploration in the Space of Code | Serves ML engineering experimentation where the model is the product of interaction, so world_resear |
| **world_research** | benchmark | Towards Community-Driven Agents for Machine Learning Engineering | ML engineering via experimentation/interaction serves world_research. |
| **world_research** | model | ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engin | Training-based agentic ML engineering serves world_research. |
| **world_research** | benchmark | MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engi | ML engineering benchmark for experimental agents serves world_research. |
| **world_research** | - | MLE-STAR: Machine Learning Engineering Agent via Search and Targeted R | Iterative ML experimentation and model refinement serves world_research. |
| **world_research** | - | ResearchCodeAgent: An LLM Multi-Agent System for Automated Codificatio | Automating research codification for experimentation purposes serves world_research. |
| **world_research** | benchmark | MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Researc | Open-ended ML research and discovery evaluation serves world_research. |
| **world_general** | benchmark | RepoMaster: Autonomous Exploration and Understanding of GitHub Reposit | Cross-domain task solving via repo reuse with no single dominant world matches world_general per Git |
| **world_research** | benchmark | MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engi | Duplicate of paper 2; ML engineering benchmark serves world_research. |
| **world_research** | benchmark | ML-Bench: Evaluating Large Language Models and Agents for Machine Lear | Repository-driven ML task execution for experimentation serves world_research. |

## scientific_workflows

| proposed | tags | title | reason |
|---|---|---|---|
| **OUT** | - | MPMWorlds: Material-Point-Method Simulations for Inferring and Extrapo | Single-shot code generation for physics modeling with no agentic interaction; falls under reasoning- |
| **world_research** | benchmark | ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Sci | Agents operate scientific software to advance discovery workflows, matching world_research's scope o |

## agentic_visualization

| proposed | tags | title | reason |
|---|---|---|---|
| **graphics** | benchmark | Plot2Code: A Comprehensive Benchmark for Evaluating Multi-modal Large  | Chart-from-spec code generation benchmark whose deliverable is visualization code, matching the grap |
| **graphics** | benchmark,training-data | OpusAnimation: Code-Based Dynamic Chart Generation | Serves animation/chart code generation from specification, matching the graphics leaf; releases benc |
| **graphics** | benchmark | From Charts to Code: A Hierarchical Benchmark for Multimodal Models | Chart-from-spec code generation benchmark whose deliverable is visualization code, matching the grap |
| **OUT** | - | Chart-CoCa: Self-Improving Chart Understanding of Vision LMs via Code- | Code is used only as an internal tool to synthesize training data for chart understanding, not as th |

## terminal

| proposed | tags | title | reason |
|---|---|---|---|
| **world_terminal** | - | Learning CLI Agents with Structured Action Credit under Selective Obse | owner ruling (calibration) |
| **world_terminal** | benchmark | TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks | Benchmark for agents acting in the terminal/OS world. |
| **world_terminal** | model | Terminus-4B: Can a Smaller Model Replace Frontier LLMs at Agentic Exec | Serves terminal execution as the agent's world of action, not code-artifact production. |
| **world_terminal** | - | ECHO: Terminal Agents Learn World Models for Free | Training method for agents whose task is acting in the terminal environment. |
| **world_terminal** | position | Terminal Agents Suffice for Enterprise Automation | Terminal agent used to accomplish enterprise tasks in the world, not to produce code artifacts. |
| **world_terminal** | training-data | Toward Scalable Terminal Task Synthesis via Skill Graphs | Resource paper whose downstream task is training terminal-operating agents. |
| **world_terminal** | position | What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adver | Position paper on evaluation design for agents operating in the terminal world. |
| **world_terminal** | training-data | TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis fo | Resource paper serving training of agents that act within terminal environments. |
| **world_terminal** | training-data,model | On Data Engineering for Scaling LLM Terminal Capabilities | Dataset and model resource paper serving terminal-agent training. |
| **world_terminal** | training-data | Endless Terminals: Scaling RL Environments for Terminal Agents | Resource paper providing RL environments for training terminal-operating agents. |
| **world_terminal** | training-data | Large-Scale Terminal Agentic Trajectory Generation from Dockerized Env | Resource paper whose downstream task is training agents to act in terminal environments. |
| **world_terminal** | benchmark | MMTB: Evaluating Terminal Agents on Multimedia-File Tasks | Terminal agents completing real workflows via shell commands is world_terminal; code is the tool of  |
| **world_terminal** | benchmark,training-data | Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,6 | Environments and trajectories serve terminal-agent evaluation/robustness, so world_terminal per reso |
| **world_terminal** | training-data | LiteCoder-Terminal: Scaling Long-Horizon Terminal Environments for Lea | Downstream task served is terminal-agent training, i.e., acting in the terminal world, so world_term |
| **world_terminal** | empirical,training-data | What Makes Interaction Trajectories Effective for Training Terminal Ag | Empirical study of training data for agents operating in terminal environments, so world_terminal +  |
| **world_terminal** | - | A Self-Evolving Framework for Efficient Terminal Agents via Observatio | Serves terminal agents completing real-world command-line tasks, matching world_terminal. |
| **world_terminal** | benchmark | Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Comman | Benchmark for agents acting in terminal/CLI environments, matching world_terminal. |

## foundation_models

| proposed | tags | title | reason |
|---|---|---|---|
| **software_general** | model | CWM: An Open-Weights LLM for Research on Code Generation with World Mo | Foundation model spanning multiple software-lifecycle activities (generation, SWE-bench issue resolu |
| **software_general** | model | Introducing: Devstral 2 and Mistral Vibe CLI | General-purpose coding model/agent release spanning multiple software tasks, classified under softwa |
| **software_general** | model | Qwen3-Coder: Agentic Coding in the World | General agentic code model spanning multiple software-lifecycle activities, so software_general per  |
| **software_general** | model | Kimi K2: Open Agentic Intelligence | Generalist agentic foundation model spanning issue resolution, coding, and math with no single lifec |

## data_synthesis

| proposed | tags | title | reason |
|---|---|---|---|
| **software_debugging** | training-data | SWE-Factory: Your Automated Factory for Issue Resolution Training Data | Downstream task is issue resolution training data, so software_debugging plus training-data tag. |
| **software_debugging** | training-data | SWE-Synth: Synthesizing Verifiable Bug-Fix Data to Enable Large Langua | Serves automated program repair/issue resolution training, hence software_debugging with training-da |
| **software_debugging** | training-data | SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Acros | Downstream task is issue resolution training data, categorized software_debugging plus training-data |
| **software_debugging** | training-data,benchmark | RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End  | Serves issue-resolution agent training with released environments/data, so software_debugging with t |
| **software_debugging** | training-data | MCTS-Refined CoT: High-Quality Fine-Tuning Data for LLM-Based Reposito | Downstream task is issue resolution, so software_debugging plus training-data tag. |
| **software_debugging** | training-data | SWE-smith: Scaling Data for Software Engineering Agents | Serves software issue-resolution agent training, categorized software_debugging with training-data t |
| **software_debugging** | training-data,benchmark | Training Software Engineering Agents and Verifiers with SWE-Gym | Downstream task is issue resolution; environment/dataset release warrants training-data and benchmar |
| **software_debugging** | training-data,benchmark | SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Mann | Serves repository-level fix/development task training with released benchmark and data, closest to s |
| **software_code_generation** | benchmark | Automated Benchmark Generation for Repository-Level Coding Tasks | Serves repository-level code generation benchmark creation, so software_code_generation with benchma |
| **software_debugging** | benchmark | SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Tes | Serves issue-resolution dataset labeling, categorized software_debugging with benchmark tag for the  |
| **OUT** | - | AgentGen: Enhancing Planning Abilities for Large Language Model based  | No code-generation or code-as-action task is specified; excluded as out of scope for the code-agent  |

## multimodal_coding

| proposed | tags | title | reason |
|---|---|---|---|
| **software_code_generation** | model,training-data,benchmark | VisCodex: Unified Multimodal Code Generation via Merging Vision and Co | owner ruling (calibration) |
| **world_general** | benchmark | GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Thr | owner ruling (calibration) |
| **software_debugging** | - | Seeing is Fixing: Cross-Modal Reasoning with Multimodal LLMs for Visua | End-to-end reproduction, localization, and repair of reported visual bugs fits software_debugging. |
| **world_general** | - | Coding Agents with Multimodal Browsing are Generalist Problem Solvers | Served task spans multiple worlds (software, web, general assistant tasks) with no single world domi |
| **software_debugging** | benchmark | SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Doma | Benchmark whose downstream task is issue resolution places it in software_debugging with benchmark t |
| **software_debugging** | - | CodeV: Issue Resolving with Visual Data | Purpose is repairing reported issues, matching software_debugging's end-to-end defect handling. |
| **software_code_generation** | benchmark | MMCode: Benchmarking Multimodal Large Language Models for Code Generat | Task is producing code from a specification, matching software_code_generation with benchmark tag. |

## code_generation

| proposed | tags | title | reason |
|---|---|---|---|
| **world_general** | survey | Code as Agent Harness | owner ruling (calibration) |
| **OUT** | - | Multi-Agent Collaboration via Evolving Orchestration | owner ruling (calibration) |
| **software_general** | empirical | Is Multi-Agent Debate (MAD) the Silver Bullet? An Empirical Analysis o | Spans two distinct lifecycle activities (comprehension and maintenance) with no single dominant task |
| **software_general** | empirical | Measuring the Impact of Early-2025 AI on Experienced Open-Source Devel | Empirical study of AI-assisted software development spanning general tasks, not any single lifecycle |
| **software_general** | empirical | Code with Me or for Me? How Increasing AI Automation Transforms Develo | Cross-activity empirical study of general-purpose coding agents versus copilots fits software_genera |
| **software_general** | survey | Assessing and Advancing Benchmarks for Evaluating Large Language Model | Survey spanning the full SE task landscape with no single dominant lifecycle activity, matching soft |
| **software_code_generation** | benchmark | Vibe Checker: Aligning Code Evaluation with Human Preference | Serves code generation as the downstream task by providing an evaluation resource for produced code  |
| **software_general** | survey | Vibe Coding vs. Agentic Coding: Fundamentals and Practical Implication | Field-level survey/position piece covering software agents broadly rather than one lifecycle activit |
| **software_testing** | position | Position: Vibe Coding Needs Vibe Reasoning: Improving Vibe Coding with | Advocates formal verification of code correctness, which the taxonomy explicitly places under softwa |
| **software_general** | survey | A Survey on Code Generation with LLM-based Agents | Explicitly covers the full SDLC rather than one lifecycle activity, so it serves software engineerin |
| **software_general** | survey | A Survey of Vibe Coding with Large Language Models | Field-level survey of the vibe/agentic coding ecosystem as a whole fits software_general. |
| **software_general** | empirical | Does AI-Assisted Coding Deliver? A Difference-in-Differences Study of  | Empirical analysis of an agentic coding tool's impact across general software development, not a sin |
| **software_general** | position | Lost in Code Generation: Reimagining the Role of Software Models in AI | Spans comprehension and maintenance concerns for AI-generated code as a whole rather than one lifecy |
| **software_code_generation** | benchmark | Towards Realistic Project-Level Code Generation via Multi-Agent Collab | Generates complete repositories/projects from requirements, matching whole-repository generation und |
| **software_code_generation** | - | Smarter Together: Creating Agentic Communities of Practice through Sha | The served task is improving the quality of generated code, so it belongs to software_code_generatio |
| **software_code_generation** | survey | Retrieval-Augmented Code Generation: A Survey with Focus on Repository | Survey whose downstream task is repository-level code generation, placing it in software_code_genera |
| **software_code_generation** | - | GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchi | Repository-aware code completion is a code-generation task per the software_code_generation scope. |
| **software_code_generation** | benchmark,training-data | Next Edit Prediction: Learning to Predict Code Edits from Context and  | Repo-aware next-edit prediction is explicitly listed under software_code_generation's repository-lev |
| **software_code_generation** | benchmark | FullStack Bench: Evaluating LLMs as Full Stack Coders | Benchmark for general code generation across domains serves the code-generation task, not tied to on |
| **software_code_generation** | benchmark | RPG: A Repository Planning Graph for Unified and Scalable Codebase Gen | Whole-repository generation from scratch falls under software_code_generation per its scope. |
| **software_code_generation** | benchmark | SimdBench: Benchmarking Large Language Models for SIMD-Intrinsic Code  | Benchmark for producing performance-critical code from specification is a code-generation task. |
| **software_code_generation** | - | MutaGReP: Execution-Free Repository-Grounded Plan Search for Code-Use | Serves repository-level code generation by grounding plans in codebase context, fitting software_cod |
| **software_code_generation** | - | Improving Cursor Tab with online RL | Task is producing/completing code via a tab-completion model, so it fits software_code_generation. |
| **world_general** | - | EvoAgentX: An Automated Framework for Evolving Agentic Workflows | A cross-domain agentic workflow scaffold spanning multiple worlds/tasks with no single domain domina |
| **software_code_generation** | - | SEW: Self-Evolving Agentic Workflows for Automated Code Generation | The served task is producing code from specifications via multi-agent workflows, matching software_c |
| **software_comprehension** | - | Repository-level Code Search with Neural Retrieval Methods | Code search and navigation to understand a repository fits software_comprehension, not a fix pipelin |
| **software_code_generation** | - | Co-Saving: Resource Aware Multi-Agent Collaboration for Software Devel | Multi-agent whole-software development akin to ChatGPT/MetaGPT/ChatDev examples maps to software_cod |
| **software_development** | - | Think Like an Engineer: A Neuro-Symbolic Collaboration Agent for Gener | Turning natural-language requirements into feature specifications for software development matches s |
| **software_general** | - | HyperAgent: Generalist Software Engineering Agents to Solve Coding Tas | A generalist agent spanning many software-lifecycle activities matches the software_general definiti |
| **systems** | benchmark | KernelBench: Can LLMs Write Efficient GPU Kernels? | Producing low-level performance-critical kernel code is systems-level code generation. |
| **software_code_generation** | training-data | EpiCoder: Encompassing Diversity and Complexity in Code Generation | Downstream task is code generation and the paper's contribution is training data synthesis for it. |
| **software_code_generation** | empirical | On the Impacts of Contexts on Repository-Level Code Generation | An empirical study on repository-level code generation quality maps to software_code_generation. |
| **software_code_generation** | - | CodeSIM: Multi-Agent Code Generation and Problem Solving through Simul | Produces code from a problem specification, so it is code generation. |
| **software_code_generation** | - | On the Impacts of Contexts on Repository-Level Code Generation | Focuses on producing repository-aware code, matching code generation & completion. |
| **software_code_generation** | benchmark | ProjectEval: A Benchmark for Programming Agents Automated Evaluation o | Benchmark serving the task of producing project-scale code, so code generation. |
| **software_code_generation** | - | AgileCoder: Dynamic Collaborative Agents for Software Development base | Builds whole software codebases from user input, matching whole-repository code generation. |
| **software_review** | benchmark | CodeVisionary: An Agent-based Framework for Evaluating Large Language  | Judges the quality of generated code rather than producing it, matching code review's assessment rol |
| **software_general** | - | Multi-Agent Collaboration via Cross-Team Orchestration | A generic multi-agent collaboration mechanism spanning software dev broadly with no single lifecycle |
| **software_general** | - | Scaling Large Language Model-based Multi-Agent Collaboration | A generic collaboration-scaling study applied broadly to software agents rather than one specific li |
| **software_code_generation** | - | Commit0: Library Generation from Scratch | Whole-library generation from scratch is code generation at repository scale. |
| **software_code_generation** | - | RLCoder: Reinforcement Learning for Repository-Level Code Completion | Serves repository-level code completion, a code generation task. |
| **software_code_generation** | - | CATCODER: Repository-Level Code Generation with Relevant Code and Type | Targets producing repository-aware code, matching code generation & completion. |
| **software_code_generation** | - | Iterative Experience Refinement of Software-Developing Agents | Serves whole software generation by agents, so software_code_generation. |
| **software_code_generation** | - | CodeTree: Agent-guided Tree Search for Code Generation with Large Lang | Primary purpose is producing correct code via search, i.e., code generation. |
| **software_code_generation** | - | AgentCoder: Multi-Agent-based Code Generation with Iterative Testing a | Ultimate goal is producing correct code, testing is instrumental to generation. |
| **software_code_generation** | - | Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large- | Task is generating/optimizing large code, fitting software_code_generation. |
| **software_code_generation** | - | GraphCoder: Enhancing Repository-Level Code Completion via Code Contex | Repository-aware code completion is software_code_generation per taxonomy. |
| **software_code_generation** | - | MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework | Builds whole codebases from scratch via multi-agent teams, matching software_code_generation example |
| **software_code_generation** | benchmark | RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems | Resource paper serving repository-level code completion, a software_code_generation task. |
| **software_general** | - | AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emerg | Generic multi-agent scaffold whose software-relevant use spans multiple lifecycle activities, matchi |
| **software_code_generation** | benchmark | RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems | Duplicate entry; resource paper serving repository-level code completion, a software_code_generation |
| **software_comprehension** | - | RepoAgent: An LLM-Powered Open-Source Framework for Repository-level C | Documentation generation from code understanding fits software_comprehension. |
| **software_code_generation** | benchmark | CodeAgent: Enhancing Code Generation with Tool-Integrated Agent System | Repo-level code generation from scratch/context is the produced-code task, so software_code_generati |
| **software_code_generation** | - | Experiential Co-Learning of Software-Developing Agents | Multi-agent software development pipeline producing code from specs falls under software_code_genera |
| **software_code_generation** | - | ChatDev: Communicative Agents for Software Development | Generates a whole application/codebase from scratch via a multi-agent team, matching the software_co |
| **software_code_generation** | - | MapCoder: Multi-Agent Code Generation for Competitive Problem Solving | Competitive programming code generation from specification is core software_code_generation. |
| **software_code_generation** | - | Iterative Refinement of Project-Level Code Context for Precise Code Ge | Compiler-feedback-driven refinement serves producing correct repo-level code, so software_code_gener |
| **software_code_generation** | - | A Pair Programming Framework for Code Generation via Multi-Plan Explor | Task is producing code from specifications via iterative refinement, i.e. software_code_generation. |
| **software_maintenance** | - | CodePlan: Repository-Level Coding using LLMs and Planning | Task is behavior-preserving multi-file migration/adaptation across a repo, matching software_mainten |
| **software_code_generation** | - | A3-CodGen: A Repository-Level Code Generation Framework for Code Reuse | Produces code completions/units aware of repo context, fitting software_code_generation. |
| **software_code_generation** | - | Monitor-Guided Decoding of Code LMs with Static Analysis of Repository | Improves code completion generation using static analysis, serving the code-production task of softw |

## issue_resolution

| proposed | tags | title | reason |
|---|---|---|---|
| **software_debugging** | - | Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis | Serves issue reproduction/localization/repair within known bugs, i.e. issue resolution. |
| **software_general** | position | Position: Future Research and Challenges Remain Towards AI for Softwar | Field-level position paper spanning software engineering, no single lifecycle activity dominates. |
| **software_general** | empirical | How can we assess human-agent interactions? Case studies in software a | Cross-activity empirical study of software agent design and human-agent collaboration, not a single  |
| **software_general** | empirical | A Comprehensive Empirical Evaluation of Agent Frameworks on Code-centr | Cross-cutting empirical evaluation spanning multiple SE tasks, no single lifecycle activity dominate |
| **software_general** | survey | Large Language Model-Based Agents for Software Engineering: A Survey | Field-level survey of software agents as a whole. |
| **software_general** | survey | A Comprehensive Survey on Benchmarks and Solutions in Software Enginee | Field-level survey spanning benchmarks and solutions across many SE lifecycle activities. |
| **software_general** | survey | Agents in software engineering: survey, landscape, and vision | Matches the canonical software_general example of a field-level survey. |
| **software_general** | position | Agentic Software Engineering: Foundational Pillars and a Research Road | Field-level vision/roadmap for software engineering as a whole, not a single lifecycle activity. |
| **software_general** | survey | How Does LLM Reasoning Work for Code? A Survey and a Call to Action | Spans multiple SE tasks (generation, testing, issue resolution) with no single dominating activity. |
| **software_general** | benchmark | SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Softwa | Cross-activity collaborative SE benchmark not tied to a single lifecycle task, so falls to software_ |
| **software_debugging** | benchmark | SWE-Bench+: Enhanced Coding Benchmark for LLMs | Benchmark for issue-resolution agents falls under software_debugging. |
| **software_debugging** | - | Prometheus: Unified Knowledge Graphs for Issue Resolution in Multiling | Task is end-to-end issue reproduction, localization and patch generation, i.e. software_debugging. |
| **software_debugging** | training-data,model | SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Is | Downstream task served by the SFT data/models is issue resolution, hence software_debugging with tra |
| **software_debugging** | empirical | Are "Solved Issues" in SWE-bench Really Solved Correctly? An Empirical | Study analyzes correctness of issue-resolution patches, squarely software_debugging. |
| **software_general** | benchmark | Unified Software Engineering Agent as AI Software Engineer | Generalist agent spanning many software lifecycle activities with no single activity dominating fits |
| **software_debugging** | empirical | Beyond Final Code: A Process-Oriented Error Analysis of Software Devel | Focuses specifically on SWE-bench issue-resolution agent trajectories, so software_debugging. |
| **software_debugging** | empirical | LLM-based Agents for Automated Bug Fixing: How Far Are We? | Comparative analysis of automated repair systems is software_debugging. |
| **world_general** | model,training-data | Let It Flow: Agentic Crafting on Rock and Roll, Building the ROME Mode | Cross-world generalist agent infrastructure spanning software and terminal tasks with no single worl |
| **software_debugging** | training-data | Toward Training Superintelligent Software Agents through Self-Play SWE | Training approach whose downstream task is issue resolution, so software_debugging plus training-dat |
| **software_general** | - | Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codeba | Agent scaffold/SDK serving software engineering as a whole rather than one lifecycle activity fits s |
| **software_security** | benchmark,empirical | Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Cod | Evaluates security of agent-generated code, matching the software_security lifecycle activity. |
| **software_debugging** | - | Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly | Served task is repository-level issue resolution, so it falls under software_debugging despite self- |
| **software_general** | - | The OpenHands Software Agent SDK: A Composable and Extensible Foundati | A scaffold/SDK serving software agents broadly across lifecycle activities fits software_general. |
| **software_general** | benchmark | CodeClash: Benchmarking Goal-Oriented Software Engineering | No single lifecycle activity dominates the goal-oriented, open-ended software development task, so i |
| **software_debugging** | - | InfCode: Adversarial Iterative Refinement of Tests and Patches for Rel | Directly targets repository-level issue resolution, matching software_debugging. |
| **software_general** | empirical | Agent READMEs: An Empirical Study of Context Files for Agentic Coding | Studies infrastructure supporting agentic coding broadly across the software lifecycle, fitting soft |
| **software_debugging** | empirical | Understanding Code Agent Behaviour: An Empirical Study of Success and  | Analyzes agent behavior specifically on SWE-bench issue-resolution trajectories, so it falls under s |
| **software_general** | benchmark | SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities fo | Spans many software-lifecycle task types without one dominating, matching software_general. |
| **software_debugging** | empirical | More with Less: An Empirical Study of Turn-Control Strategies for Effi | Evaluation is grounded in SWE-bench issue-resolution tasks, placing it under software_debugging. |
| **software_debugging** | benchmark | SWE-Sharp-Bench: A Reproducible Benchmark for C# Software Engineering  | Follows the SWE-bench issue-resolution paradigm for a new language, fitting software_debugging. |
| **software_development** | - | U2F: Encouraging SWE-Agent to Seize Novelty without Losing Feasibility | Task is implementing novel solutions to feature/enabler requirements in existing systems, matching s |
| **software_general** | benchmark | Programming with Pixels: Can Computer-Use Agents do Software Engineeri | Benchmark spans many SWE lifecycle tasks with no single activity dominating, matching software_gener |
| **world_general** | training-data | Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tun | Training-data resource spans multiple worlds/domains evenly, matching the cross-world world_general  |
| **software_comprehension** | benchmark | Gistify! Codebase-Level Understanding via Runtime Execution | The task's purpose is evaluating codebase-level understanding, matching software_comprehension even  |
| **software_debugging** | - | Abstain and Validate: A Dual-LLM Policy for Reducing Noise in Agentic  | Directly serves automated program repair/issue resolution, matching software_debugging. |
| **software_debugging** | - | REFINE: Enhancing Program Repair Agents through Context-Aware Patch Re | Improves patch quality within automated program repair pipelines, matching software_debugging. |
| **software_infrastructure** | benchmark | Process-Level Trajectory Evaluation for Environment Configuration in S | Focuses on environment/build setup for software, matching software_infrastructure. |
| **software_debugging** | training-data | BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills | Training data explicitly serves issue-resolution/program-repair agents, matching software_debugging  |
| **software_security** | - | When “Correct” Is Not Safe: Can We Trust Functionally Correct Patches  | Concerns vulnerability introduction in code patches, matching software_security. |
| **software_debugging** | - | TDFlow: Agentic Workflows for Test Driven Software Engineering | Core task is repository-scale bug repair/issue resolution guided by tests, matching software_debuggi |
| **software_debugging** | - | Enhancing repository-level software repair via repository-aware knowle | Repository-level issue repair with fault localization is core software_debugging. |
| **software_comprehension** | - | Code Digital Twin: Empowering LLMs with Tacit Knowledge for Complex So | Builds knowledge representations to understand and document codebases for downstream assistants, mat |
| **software_debugging** | - | SIADAFIX: issue description response for adaptive program repair | Issue-driven automated program repair is software_debugging. |
| **software_debugging** | model,training-data | Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents | Downstream task is SWE-bench issue resolution, so software_debugging with model/training-data tags. |
| **software_debugging** | empirical | An Empirical Study on Failures in Automated Issue Solving | Empirical study and improvement targeting SWE-bench issue resolution. |
| **software_debugging** | empirical | Understanding Software Engineering Agents Through the Lens of Traceabi | Analysis of automated program repair agents is software_debugging. |
| **software_debugging** | benchmark | Is Your Automated Software Engineer Trustworthy? | Benchmark targeting trustworthiness of issue-resolution/bug-fixing agents falls under software_debug |
| **software_debugging** | benchmark | Interactive Agents to Overcome Ambiguity in Software Engineering | Evaluated via SWE-Bench Verified variant on issue resolution, placing it in software_debugging. |
| **software_debugging** | benchmark | SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering T | Benchmark for issue-resolution style long-horizon SWE tasks is software_debugging. |
| **software_debugging** | benchmark | SWE-PolyBench: A multi-language benchmark for repository level evaluat | Repository-level execution-based benchmark spanning bug fixes/features centers on issue resolution s |
| **software_debugging** | benchmark,training-data | Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving | Downstream task is issue resolution (bug repair), so software_debugging; benchmark and training-data |
| **software_debugging** | benchmark,training-data | SWE-rebench: An Automated Pipeline for Task Collection and Decontamina | Serves issue-resolution agents; dataset and benchmark for that task place it in software_debugging. |
| **software_debugging** | - | Trae Agent: An LLM-based Agent for Software Engineering with Test-time | Task is repairing reported issues in repositories, matching software_debugging. |
| **software_general** | - | ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | Generic cross-task method spanning multiple lifecycle/world activities with no single dominant softw |
| **software_debugging** | - | EXPEREPAIR: Dual-Memory Enhanced LLM-based Repository-Level Program Re | Directly targets automated program repair of reported issues, i.e., software_debugging. |
| **software_debugging** | - | SWE-Exp: Experience-Driven Software Issue Resolution | Explicitly targets issue resolution/repair, placing it in software_debugging. |
| **software_debugging** | model,training-data | Thinking Longer, Not Larger: Enhancing Software Engineering Agents via | Focuses on fault localization and patch generation for issue resolution, so software_debugging. |
| **software_debugging** | - | AutoCodeSherpa: Symbolic Explanations in AI Coding Agents | Used to validate/reject patches within issue-resolution pipelines, serving software_debugging. |
| **software_debugging** | model | Satori-SWE: Evolutionary Test-Time Scaling for Sample-Efficient Softwa | Directly targets GitHub issue resolution performance, matching software_debugging. |
| **systems** | benchmark | CrashFixer: A crash resolution agent for the Linux kernel | Domain of the code is systems-level kernel software, which collapses lifecycle activities into the s |
| **software_debugging** | - | DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance b | Serves SWE-bench issue resolution, the reported/known-bug repair task. |
| **software_debugging** | - | Large Language Model Critics for Execution-Free Evaluation of Code Cha | Evaluation proxy serving SWE-bench style issue-resolution patch quality assessment. |
| **software_debugging** | benchmark | debug-gym: A Text-Based Environment for Interactive Debugging | Environment built specifically for interactive debugging of code defects. |
| **software_debugging** | - | HAFixAgent: History-Aware Automated Program Repair Agent | Automated program repair of known bugs is core software_debugging task. |
| **software_debugging** | - | SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resoluti | Directly targets SWE-bench issue localization and repair. |
| **software_debugging** | model | Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents | Foundation model trained specifically for SWE-bench issue resolution. |
| **software_debugging** | - | SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and | Search/refinement method targeting SWE-bench repository-level issue resolution. |
| **software_debugging** | - | SEAlign: Alignment Training for Software Engineering Agent | Primary evaluation and framing target SWE-bench issue resolution despite mention of app-building dem |
| **software_debugging** | - | Lingxi: Repository-Level Issue Resolution Framework Enhanced by Proced | Framework explicitly targets SWE-bench issue resolution. |
| **software_debugging** | model | Code Graph Model (CGM): A Graph-Integrated Large Language Model for Re | Model built and benchmarked for SWE-bench Lite issue resolution. |
| **software_debugging** | benchmark | SWE-Bench-CL: Continual Learning for Coding Agents | Built on SWE-bench issue resolution, serving debugging/issue-resolution agents. |
| **software_general** | - | A Self-Improving Coding Agent | Spans multiple software lifecycle activities (repair and generation) with no single one dominating,  |
| **software_debugging** | - | Agent-RLVR: Training Software Engineering Agents via Guidance and Envi | Downstream task served is SWE-bench issue resolution. |
| **software_debugging** | - | Training Long-Context, Multi-Turn Software Engineering Agents with Rei | Training method whose downstream task is SWE-bench issue resolution. |
| **software_debugging** | empirical | SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under R | Empirical re-evaluation of issue-resolution agents on SWE-bench. |
| **world_general** | training-data | Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents i | Resource paper whose downstream tasks span multiple worlds (terminal/software, web, desktop) with no |
| **software_debugging** | - | Enhancing repository-level software repair via repository-aware knowle | Repository-level program repair for reported issues is issue resolution. |
| **software_debugging** | - | SemAgent: A Semantics Aware Program Repair Agent | Automated program repair targeting reported issues is core software_debugging work. |
| **software_debugging** | benchmark | Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Ev | Benchmark resource serving realistic evaluation of issue-resolution agents. |
| **software_debugging** | benchmark | SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language  | New benchmark resource for issue-resolution agent evaluation. |
| **software_debugging** | benchmark | Auto-SWE-Bench: A Framework for the Scalable Generation of Software En | Benchmark serves issue-resolution/debugging evaluation. |
| **software_debugging** | benchmark | Can Agents Fix Agent Issues? | Task is reported bug/issue resolution, i.e. software_debugging. |
| **software_debugging** | - | Co-PatcheR: Collaborative Software Patching with Component(s)-specific | End-to-end issue localization and repair pipeline is software_debugging. |
| **software_debugging** | - | SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoni | Trajectory optimization method evaluated on real-world issue resolution, i.e. software_debugging. |
| **software_code_generation** | model | Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning | Primary served task is improving code generation accuracy, with test generation as a co-training sig |
| **software_debugging** | training-data | SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Sof | Matches taxonomy example: RL training on software evolution data for issue-resolving agents -> softw |
| **software_debugging** | benchmark | SWE-bench Goes Live! | Benchmark for real-world issue resolution is software_debugging. |
| **software_debugging** | - | Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks  | Localization and patch generation for issue resolution is software_debugging. |
| **software_debugging** | - | Guided Search Strategies in Non-Serializable Environments with Applica | Search method evaluated on and targeting SWE-bench issue resolution is software_debugging. |
| **software_general** | benchmark | SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelanc | Broad benchmark spanning multiple lifecycle activities (bugs, features, management) with no single a |
| **software_debugging** | benchmark | Automated Benchmark Generation for Repository-Level Coding Tasks | Resource paper whose downstream task is SWE-bench-style issue resolution. |
| **software_debugging** | - | PatchPilot: A Cost-Efficient Software Engineering Agent with Early Att | End-to-end reported-issue reproduction, localization, and repair on SWE-bench. |
| **software_general** | - | OpenHands: An Open Platform for AI Software Developers as Generalist A | Generalist scaffold serving software engineering as a whole, no single lifecycle activity dominates. |
| **software_debugging** | - | RepoGraph: Enhancing AI Software Engineering with Repository-level Cod | Comprehension aid used inside issue-resolution pipelines follows the task it serves (SWE-bench debug |
| **software_debugging** | - | Diversity Empowers Intelligence: Integrating Expertise of Software Eng | Combining SE agent expertise serves the issue-resolution task. |
| **software_debugging** | model | SWE-GPT: A Process-Centric Language Model for Automated Software Impro | Trained model whose downstream task is GitHub issue resolution. |
| **software_debugging** | - | SpecRover: Code Intent Extraction via LLMs | Specification inference is in service of resolving reported GitHub issues. |
| **software_debugging** | empirical | Understanding Software Engineering Agents: A Study of Thought-Action-R | Analyzes agents whose served task is program repair/issue resolution. |
| **software_general** | empirical | "My productivity is boosted, but ..." Demystifying Users' Perception o | No single lifecycle activity dominates; studies coding assistants broadly as a field. |
| **software_debugging** | - | DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performance b | Improves an agent whose served task is issue resolution (SWE-bench style). |
| **software_debugging** | training-data | SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning | Issue resolution training method serves software_debugging. |
| **software_debugging** | training-data,model | SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHu | GitHub issue resolution via patch generation is software_debugging. |
| **software_debugging** | - | SynFix: Dependency-Aware Program Repair via RelationGraph Analysis | Program repair task falls under software_debugging. |
| **software_debugging** | - | UniDebugger: Hierarchical Multi-Agent Framework for Unified Software D | Debugging/repair framework serves software_debugging. |
| **software_debugging** | - | Agentless: Demystifying LLM-based Software Engineering Agents | Issue resolution pipeline serves software_debugging. |
| **software_debugging** | benchmark | OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Res | Benchmark for issue resolution serves software_debugging. |
| **software_debugging** | training-data | Boosting Open-Source LLMs for Program Repair via Reasoning Transfer an | Program repair improvement method serves software_debugging. |
| **software_debugging** | - | Integrating Various Software Artifacts for Better LLM-based Bug Locali | Bug localization and repair serves software_debugging. |
| **software_debugging** | empirical | Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic a | Agentic repair driven by test failures serves software_debugging. |
| **software_debugging** | - | AutoCodeRover: Autonomous Program Improvement | Autonomous GitHub issue resolution serves software_debugging. |
| **software_debugging** | - | SWE-agent: Agent-Computer Interfaces Enable Automated Software Enginee | Task is end-to-end resolution of reported software issues, matching software_debugging. |
| **software_debugging** | - | MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution | Multi-agent system targets GitHub issue resolution, a software_debugging task. |
| **software_general** | - | MASAI: Modular Architecture for Software-engineering AI Agents | Modular agent architecture spans multiple lifecycle activities, so it fits the generalist software_g |
| **software_debugging** | benchmark | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | Benchmark whose downstream task is reported-issue resolution, i.e. software_debugging plus benchmark |
| **software_general** | benchmark | InterCode: Standardizing and Benchmarking Interactive Coding with Exec | Cross-domain interactive coding benchmark spanning multiple lifecycle/domains with no single activit |

## Removed (out of scope)

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

## Failed (to retry)

(none)

## Totals
placed 412, out 28, failed 0, duplicates skipped 31, owner-ruled 9

## Post-review corrections (2026-07-11, owner)

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
