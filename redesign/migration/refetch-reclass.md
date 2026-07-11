# Re-evidence pass: papers previously judged from second-hand summaries

77 papers re-fetched from primary sources (arXiv title search, landing pages) and re-classified. Old-pipeline summaries are no longer used as classification input.

| before | after | evidence | title | reason |
|---|---|---|---|---|
| OUT | **OUT** | primary | Can LLMs Replace Manual Annotation of Software Engineering Artifa | owner ruling |
| world_general | **world_general** | primary | Tree-of-Code: A Self-Growing Tree Framework for End-to-End Code G | owner ruling |
| software_security | **software_security** | primary | CVE-Bench: Benchmarking LLM-based Software Engineering Agent’s Ab | Task is vulnerability repair, matching software_security's boundary example on CVE benchma |
| software_review | **OUT** <- CHANGED | title-only | Armchair | Insufficient information to determine relevance or category. |
| software_review | **software_review** | title-only | PReview: A Benchmark Dataset for Pull Request Outcomes and Qualit | Judging pull requests/quality maps to software_review boundary definition. |
| software_review | **software_review** | primary | CodeAgent: Autonomous Communicative Agents for Code Review | Core served task is judging and reviewing code changes, matching software_review. |
| software_review | **OUT** <- CHANGED | primary | Can We Benchmark Code Review Studies? A Systematic Mapping Study  | Not an agent paper that writes or executes code; it is a meta-analysis of research methodo |
| software_comprehension | **software_comprehension** | primary | Benchmarking Long-Context Language Models on Long Code Understand | Served task is understanding code, matching software_comprehension's repository/long-code  |
| software_comprehension | **software_comprehension** | primary | On Improving Repository-Level Code QA for Large Language Models | Repository QA is explicitly listed under software_comprehension. |
| web | **web** | title-only | Divide-and-Conquer: Generating UI Code from Screenshots | Screenshot-to-code UI generation is a canonical web example. |
| graphics | **graphics** | primary | Chat2SVG: Vector Graphics Generation with Large Language Models a | Delivers vector-graphic SVG code, matching the graphics leaf definition. |
| web | **web** | primary | Figma2Code: Automating Multimodal Design to Code in the Wild | Design-to-code UI generation delivering front-end code is a web task. |
| cad | **cad** | primary | Generating CAD Code with Vision-Language Models for 3D Designs | Produces CAD scripting code as the deliverable artifact. |
| cad | **cad** | primary | CAD-Llama: Leveraging Large Language Models for Computer-Aided De | Generates parametric CAD model code. |
| cad | **cad** | primary | The Scene Language: Representing Scenes with Programs, Words, and | Delivers a program-based 3D scene representation, i.e. code building a 3D artifact. |
| cad | **cad** | primary | BlenderGym: Benchmarking Foundational Model Systems for Graphics  | Task is producing/editing 3D scene code (Blender), matching cad/3D domain over generic gra |
| cad | **cad** | primary | SceneGenAgent: Precise Industrial Scene Generation with Coding Ag | Purpose is producing 3D scene code for industrial simulation, fitting the cad/3D domain. |
| cad | **cad** | primary | 3D-GPT: Procedural 3D Modeling with Large Language Models | Deliverable is 3D model/asset code generated procedurally. |
| cad | **cad** | primary | CADTalk: An Algorithm and Benchmark for Semantic Commenting of CA | Task is understanding/documenting CAD code, still serving the 3D/CAD code domain. |
| cad | **cad** | primary | SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Cod | Produces 3D scene code (Blender Python scripts) as the deliverable. |
| software_debugging | **software_debugging** | primary | Evaluating Diverse Large Language Models for Automatic and Genera | Bug reproduction turning a report into a failing test falls under debugging & issue resolu |
| software_debugging | **software_debugging** | primary | LocAgent: Graph-Guided LLM Agents for Code Localization | Fault localization for reported issues is core to debugging & issue resolution. |
| software_infrastructure | **software_code_generation** <- CHANGED | primary | RepoST: Scalable Repository-Level Coding Environment Construction | Resource paper serving repository-level code generation/completion, so software_code_gener |
| software_infrastructure | **software_infrastructure** | primary | CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source So | Automated project building is enabling work that makes code buildable, matching software_i |
| software_infrastructure | **software_infrastructure** | primary | CompileAgent: Automated Real-World Repo-Level Compilation with To | Automating compilation and build error resolution is enabling work, i.e. software_infrastr |
| software_infrastructure | **software_infrastructure** | primary | CSR-Bench: Benchmarking LLM Agents in Deployment of Computer Scie | Deployment and environment setup for repositories is enabling work, matching software_infr |
| software_debugging | **software_general** <- CHANGED | primary | R2E: Turning any Github Repository into a Programming Agent Envir | A cross-activity resource/environment builder for general software agent evaluation, not t |
| software_infrastructure | **software_infrastructure** | primary | GitGoodBench: A Novel Benchmark For Evaluating Agentic Performanc | Git/VCS operation tasks are enabling work explicitly listed under software_infrastructure. |
| software_general | **software_general** | primary | Prompting Large Language Models to Tackle the Full Software Devel | Spans multiple lifecycle activities with none dominating, matching software_general's cros |
| world_apps | **world_apps** | primary | AppWorld: A Controllable World of Apps and People for Benchmarkin | Agents write code as the tool to operate everyday applications, matching world_apps. |
| world_general | **OUT** <- CHANGED | primary | APIGen: Automated PIpeline for Generating Verifiable and Diverse  | Serves function/tool-calling capability rather than code-writing or code-execution agency, |
| world_game | **world_general** <- CHANGED | primary | WorldCoder, a Model-Based LLM Agent: Building World Models by Wri | Code is the instrument for acting/planning across generic environments rather than the del |
| OUT | **OUT** | primary | Visual Agentic AI for Spatial Reasoning with a Dynamic API | Code is used purely as a reasoning aid for answering visual questions, matching the exclud |
| world_physical | **world_physical** | primary | GRS: Generating Robotic Simulation Tasks from Real-World Images | Resource paper synthesizing simulation environments/tasks whose downstream purpose is trai |
| OUT | **OUT** | title-only | Endowing Visual Reprogramming with Adversarial Robustness | No code-writing or code-acting agentic task is indicated by the title; falls outside scope |
| world_physical | **world_physical** | primary | RoboCodeX: Multimodal Code Generation for Robotic Behavior Synthe | Code is the policy/control language for physical robot action, matching the code-as-policy |
| OUT | **OUT** | primary | Recursive Visual Programming | Code is generated purely as a reasoning aid to answer visual questions, matching the exclu |
| OUT | **OUT** | title-only | Video Question Answering with Procedural Programs | Code serves as a reasoning tool for question answering rather than an agentic real-world t |
| OUT | **OUT** | primary | Modular Visual Question Answering via Code Generation | Code is a reasoning aid composing model calls to answer questions, matching the excluded P |
| world_research | **world_research** | primary | DA-Code: Agent Data Science Code Generation Benchmark for Large L | Serves data-science/data-exploration agent tasks where code is the instrument for producin |
| OUT | **OUT** | primary | We Got Claude to Fine-Tune an Open Source LLM | Industry blog post with no described agentic code-production or code-action task; out of s |
| software_general | **OUT** <- CHANGED | primary | Introducing: Devstral 2 and Mistral Vibe CLI | Industry product announcement, excluded per scope rules against industry products/technica |
| software_general | **software_general** | title-only | Qwen3-Coder: Agentic Coding in the World | Generalist agentic coding model spanning software tasks, no single lifecycle activity domi |
| software_code_generation | **software_debugging** <- CHANGED | primary | Automated Benchmark Generation for Repository-Level Coding Tasks | Serves issue-resolution benchmarking, matching SWE-bench style tasks -> software_debugging |
| OUT | **OUT** | primary | AgentGen: Enhancing Planning Abilities for Large Language Model b | No code artifact or code-as-action task involved; generic planning agent training falls ou |
| software_debugging | **software_debugging** | primary | SWE-bench Multimodal: Do AI Systems Generalize to Visual Software | Benchmark for GitHub issue resolution across a new domain -> software_debugging. |
| software_debugging | **software_debugging** | primary | CodeV: Issue Resolving with Visual Data | Directly targets GitHub issue resolution -> software_debugging. |
| software_code_generation | **software_code_generation** | primary | MMCode: Benchmarking Multimodal Large Language Models for Code Ge | Function/problem-level code generation from specification -> software_code_generation. |
| software_code_generation | **software_code_generation** | title-only | Improving Cursor Tab with online RL | Code completion is a code-generation task -> software_code_generation. |
| software_code_generation | **software_code_generation** | primary | On the Impacts of Contexts on Repository-Level Code Generation | Repo-aware code generation task -> software_code_generation. |
| software_code_generation | **software_code_generation** | primary | ProjectEval: A Benchmark for Programming Agents Automated Evaluat | Project-level code generation from specifications -> software_code_generation. |
| software_code_generation | **software_code_generation** | primary | Commit0: Library Generation from Scratch | Whole-repository generation from scratch matches software_code_generation per taxonomy exa |
| software_code_generation | **software_code_generation** | primary | RepoBench: Benchmarking Repository-Level Code Auto-Completion Sys | Benchmark serving repository-aware code completion, a code generation task. |
| software_general | **OUT** <- CHANGED | primary | AgentVerse: Facilitating Multi-Agent Collaboration and Exploring  | General multi-agent framework not focused on code as artifact or action, out of scope. |
| software_code_generation | **software_code_generation** | primary | RepoBench: Benchmarking Repository-Level Code Auto-Completion Sys | Duplicate of paper 0; benchmark for repository-aware code completion. |
| software_comprehension | **software_comprehension** | primary | RepoAgent: An LLM-Powered Open-Source Framework for Repository-le | Documentation generation serves understanding of code, matching software_comprehension's i |
| software_code_generation | **software_general** <- CHANGED | primary | Experiential Co-Learning of Software-Developing Agents | Improves generalist software-developing agents across activities rather than one specific  |
| software_code_generation | **software_code_generation** | primary | ChatDev: Communicative Agents for Software Development | Builds whole software codebases from scratch via multi-agent collaboration, matching softw |
| software_code_generation | **software_code_generation** | primary | MapCoder: Multi-Agent Code Generation for Competitive Problem Sol | Produces code from natural-language problem descriptions, a core code generation task. |
| software_code_generation | **software_code_generation** | primary | Iterative Refinement of Project-Level Code Context for Precise Co | Purpose is producing correct project-context-aware code, a code generation task. |
| software_maintenance | **software_maintenance** | primary | CodePlan: Repository-Level Coding using LLMs and Planning | Primary evaluated task is package migration, a behavior-evolving activity matching softwar |
| software_code_generation | **software_code_generation** | title-only | A3-CodGen: A Repository-Level Code Generation Framework for Code  | Title signals a repository-level code generation framework, matching software_code_generat |
| software_code_generation | **software_code_generation** | title-only | Monitor-Guided Decoding of Code LMs with Static Analysis of Repos | Purpose is producing correct code via guided completion, so software_code_generation. |
| software_general | **software_general** | title-only | Position: Future Research and Challenges Remain Towards AI for So | Field-wide position paper on SE agents with no single lifecycle activity dominating, so so |
| software_general | **software_general** | primary | Agents in software engineering: survey, landscape, and vision | Survey of software agents spanning the whole field, not one lifecycle activity, so softwar |
| software_debugging | **software_debugging** | primary | SWE-Bench+: Enhanced Coding Benchmark for LLMs | Serves the issue-resolution task by auditing its benchmark, so software_debugging. |
| software_debugging | **software_debugging** | title-only | Auto-SWE-Bench: A Framework for the Scalable Generation of Softwa | Resource paper whose downstream task is issue resolution, so software_debugging with bench |
| software_debugging | **software_debugging** | title-only | Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering T | Improves localization for issue resolution, matching software_debugging. |
| software_debugging | **software_debugging** | primary | Diversity Empowers Intelligence: Integrating Expertise of Softwar | Evaluated and framed around SWE-Bench issue resolution, so software_debugging. |
| software_debugging | **software_debugging** | primary | DARS: Dynamic Action Re-Sampling to Enhance Coding Agent Performa | Coding agent method targeting SWE-Bench issue resolution performance, software_debugging. |
| software_debugging | **software_debugging** | primary | SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuni | Training method whose downstream task is issue resolution, so software_debugging. |
| software_debugging | **software_debugging** | primary | SynFix: Dependency-Aware Program Repair via RelationGraph Analysi | Program repair of known defects falls under software_debugging. |
| software_debugging | **software_debugging** | primary | UniDebugger: Hierarchical Multi-Agent Framework for Unified Softw | End-to-end bug reproduction/localization/repair pipeline matches software_debugging. |
| software_debugging | **software_debugging** | primary | Agentless: Demystifying LLM-based Software Engineering Agents | Targets SWE-bench issue resolution end-to-end, i.e. software_debugging. |
| software_debugging | **software_debugging** | primary | Integrating Various Software Artifacts for Better LLM-based Bug L | Fault localization plus patch generation for reported bugs is software_debugging. |
| software_debugging | **software_debugging** | primary | MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolutio | GitHub issue resolution task maps directly to software_debugging. |
| software_general | **software_debugging** <- CHANGED | primary | MASAI: Modular Architecture for Software-engineering AI Agents | Evaluated on SWE-bench Lite issue resolution, placing it in software_debugging. |
