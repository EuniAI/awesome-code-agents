# Inbox classification run

109 arXiv ids in inbox issue #4; 37 already in corpus; 72 classified; 69 added, 3 out of scope.

| category | title | reason |
|---|---|---|
| **world_apps** | GenClaw: Code-Driven Agentic Image Generation | code is an intermediate control tool for a media-generation task whose deliverable is an image, |
| **software_general** | TrajAudit: Automated Failure Diagnosis for Agentic Coding Syst | the paper diagnoses failures of coding agents across their whole lifecycle behavior rather than |
| **software_infrastructure** | SetupX: Can LLM Agents Learn from Past Failures in Functionali | the task is environment and dependency setup so code can be built and run, matching software_in |
| **software_general** | How Coding Agents Fail Their Users: A Large-Scale Analysis of  | an empirical study spanning coding-agent behavior across many lifecycle activities with no sing |
| **software_general** | Programming by Chat: A Large-Scale Behavioral Analysis of 11,5 | an empirical study of AI-assisted software development practice as a whole, not tied to one lif |
| **software_general** | SWE-chat: Coding Agent Interactions From Real Users in the Wil | a dataset and empirical characterization of real-world coding-agent usage spanning the whole de |
| **software_debugging** | Coherence Collapse: Diagnosing Why Code Agents Fail After Reac | the diagnosis targets SWE-bench Verified issue-resolution trajectories, so it serves the debugg |
| **software_debugging** | Rethinking the Value of Agent-Generated Tests for LLM-Based So | the analyzed behavior is embedded in repository issue-resolution workflows on SWE-bench Verifie |
| **systems** | Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agent | the task produces CUDA kernel (systems-level) code, matching the systems leaf. |
| **software_general** | Fingerprinting AI Coding Agents on GitHub | an empirical cross-activity study of AI coding agent behavior on GitHub, not tied to a single l |
| **cad** | SceneCode: Executable World Programs for Editable Indoor Scene | The deliverable is executable code building a 3D scene/asset, matching the cad leaf's definitio |
| **software_code_generation** | DevBench: A Realistic, Developer-Informed Benchmark for Code G | Benchmark for code completion/generation tasks routes to software_code_generation. |
| **world_terminal** | LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Re | The agent acts through OS-level operations in a terminal environment, matching world_terminal's |
| **web** | Figma2Code: Automating Multimodal Design to Code in the Wild | Task delivers front-end web UI code from design specs, matching the web leaf's design-to-code i |
| **web** | WebCode2M: A Real-World Dataset for Code Generation from Webpa | Dataset serves webpage code generation, routing to the web leaf per the training-data resource  |
| **web** | UICopilot: Automating UI Synthesis via Hierarchical Code Gener | Method produces front-end HTML/UI code from designs, matching the web leaf. |
| **web** | LaTCoder: Converting Webpage Design to Code with Layout-as-Tho | Delivers webpage front-end code from design images, matching the web leaf. |
| **software_general** | SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution | Benchmark spans multiple distinct lifecycle activities (comprehension, testing, maintenance) wi |
| **cad** | 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via C | Task produces procedural code that builds 3D artifacts, matching the cad leaf definition. |
| **software_general** | SpecBench: Measuring Reward Hacking in Long-Horizon Coding Age | Benchmark studies agent behavior across diverse software-building tasks without one lifecycle a |
| **hardware** | SymRTLO: Enhancing RTL Code Optimization with LLMs and Neuron- | Produces optimized hardware description (RTL) code, so it belongs to hardware. |
| **software_code_generation** | CoRe-Code: Collaborative Reinforcement Learning for Code Gener | The served task is producing code from specification, so software_code_generation. |
| **software_code_generation** | SWE-AGI: Benchmarking Specification-Driven Software Constructi | Whole-codebase generation from specifications with no pre-existing repo routes to software_code |
| **software_testing** | WebTestPilot: Agentic End-to-End Web Testing against Natural L | Proactive test oracle inference for correctness assurance, independent of a specific reported d |
| **hardware** | Spec2RTL-Agent: Automated Hardware Code Generation from Comple | Delivers hardware description/RTL code from specifications, fitting the hardware leaf. |
| **software_general** | AgentSPEX: An Agent SPecification and EXecution Language | A cross-activity agent scaffold/SDK not tied to one lifecycle activity fits software_general's  |
| **software_debugging** | Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agen | Issue-resolution benchmarking (SWE-bench style) routes to software_debugging. |
| **software_debugging** | SWE-Explore: Benchmarking How Coding Agents Explore Repositori | Exploration/localization ground truth derived from issue-resolution trajectories serves the deb |
| **software_general** | TACT: Mitigating Overthinking and Overacting in Coding Agents  | A generic reliability method for coding agents evaluated across multiple activity/world benchma |
| **software_code_generation** | DeNovoSWE: Scaling Long-Horizon Environments for Generating En | Training data serving whole-repository generation from specs routes to software_code_generation |
| **software_code_generation** | RepoST: Scalable Repository-Level Coding Environment Construct | Resource paper serving repository-level code generation via execution feedback. |
| **software_code_generation** | Code2LoRA: Hypernetwork-Generated Adapters for Code Language M | Serves repository-aware code completion, matching software_code_generation. |
| **OUT** | Function2Scene: 3D Indoor Scene Layout from Functional Specifi | No code artifact or code-as-action is produced; out of scope for a code-agent list. |
| **software_code_generation** | RepoZero: Can LLMs Generate a Code Repository from Scratch? | Evaluates generating whole repositories from scratch, per software_code_generation's boundary e |
| **software_general** | SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World  | Cross-activity empirical benchmark of software engineering practice with no single lifecycle ac |
| **software_code_generation** | InCoder-32B: Code Foundation Model for Industrial Scenarios | A specialized code-generation model, not a general-purpose agentic substrate, so routes to soft |
| **software_general** | BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo B | Benchmark spanning multiple software-lifecycle activities with no single one dominating, per so |
| **software_testing** | SWE-Mutation: Can LLMs Generate Reliable Test Suites in Softwa | Focused on test-suite generation quality, matching software_testing's proactive correctness-ass |
| **software_general** | DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle | Spans multiple software lifecycle activities (build, monitoring, debugging, testing) with none  |
| **software_debugging** | SWE-Universe: Scale Real-World Verifiable Environments to Mill | Resource paper whose downstream task is issue resolution, evidenced by SWE-bench Verified evalu |
| **software_general** | How Do Developers Interact with AI? An Exploratory Study on Mo | Human-agent collaboration empirical study spanning software engineering broadly, not tied to on |
| **software_development** | SWE-Dev: Evaluating and Training Autonomous Feature-Driven Sof | Adds new features to existing codebases, matching software_development's feature-implementation |
| **software_debugging** | SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale | Resource paper whose downstream task is SWE-bench-style issue resolution training, routed per m |
| **software_debugging** | Skywork-SWE: Unveiling Data Scaling Laws for Software Engineer | Training data and model targeting SWE-bench issue resolution, routed to software_debugging plus |
| **software_debugging** | daVinci-Env: Open SWE Environment Synthesis at Scale | Environment/trajectory construction serving issue-resolution agent training, per the environmen |
| **software_development** | Automatically Benchmarking LLM Code Agents through Agent-Drive | Evaluates agents implementing requirements into existing/new projects, closest to feature-drive |
| **software_debugging** | Immersion in the GitHub Universe: Scaling Coding Agents to Mas | Data construction pipeline serving SWE-bench issue-resolution agent training. |
| **software_debugging** | SWE-MiniSandbox: Container-Free Reinforcement Learning for Bui | Training infrastructure whose served downstream task is SWE agent issue resolution, per environ |
| **software_debugging** | Closing the Loop: Universal Repository Representation with RPG | Benchmark routing dominates: strong SWE-bench localization evaluation routes this to software_d |
| **software_debugging** | FastContext: Training Efficient Repository Explorer for Coding | Specialized exploration models evaluated primarily on SWE-bench issue-resolution benchmarks, ro |
| **software_debugging** | AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evalu | Benchmark/analysis serving issue-resolution (SWE-bench) evaluation, so software_debugging. |
| **software_debugging** | SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated  | Adversarial benchmark strengthening for SWE-bench issue-resolution evaluation, software_debuggi |
| **software_code_generation** | PlayCoder: Making LLM-Generated GUI Code Playable | Produces and repairs GUI application code from scratch/repo context, matching software_code_gen |
| **software_general** | Dive into Claude Code: The Design Space of Today's and Future  | Cross-cutting architectural analysis of a general-purpose coding agent scaffold, not tied to on |
| **web** | WebCompass: Towards Multimodal Web Coding Evaluation for Code  | Benchmark for producing/editing web application code, matching the web leaf. |
| **game** | OpenGame: Open Agentic Coding for Games | Builds a game's codebase end-to-end, matching artifact/game. |
| **software_debugging** | SWE-Next: Scalable Real-World Software Engineering Tasks for A | Data/environment synthesis serving issue-resolution agent training, software_debugging plus tra |
| **software_maintenance** | SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases | Focuses on preserving/evolving codebase quality over time (maintainability), matching software_ |
| **OUT** | MORSE-500: A Programmatically Controllable Video Benchmark to  | No agent writes or executes code as its task; out of scope per exclusion of non-agentic reasoni |
| **world_general** | Computer Environments Elicit General Agentic Intelligence in L | Generalist code-sandbox agent spanning many disparate task domains with no single world dominat |
| **software_debugging** | Code Researcher: Deep Research Agent for Large Systems Code an | Serves issue resolution/patch generation for reported crashes, routed to software_debugging. |
| **software_general** | CODESKILL: Learning Self-Evolving Skills for Coding Agents | A cross-activity skill-management framework spanning environment setup, debugging, and terminal |
| **software_code_generation** | Benchmarking PhD-Level Coding in 3D Geometric Computer Vision | Task is code completion/generation of functions, routed to software_code_generation as a benchm |
| **software_general** | CodeTracer: Towards Traceable Agent States | A tracing/observability scaffold serving coding agents across multiple lifecycle activities, no |
| **software_debugging** | How and Why Agents Can Identify Bug-Introducing Commits | Root-cause/fault-origin identification for defects belongs to software_debugging. |
| **world_terminal** | TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents | The contribution is a benchmark for the terminal/OS as the agent's world, not code production. |
| **software_debugging** | Dockerless: Environment-Free Program Verifier for Coding Agent | A verifier resource enabling issue-resolution training pipelines, routed to the downstream task |
| **OUT** | Program-as-Weights: A Programming Paradigm for Fuzzy Functions | Not an agentic task or code-producing/code-acting paper; it compiles specs to neural weights ra |
| **software_general** | Overeager Coding Agents: Measuring Out-of-Scope Actions on Ben | An empirical safety study spanning multiple coding-agent products/tasks with no single lifecycl |
| **software_general** | ATM: CID-Brokered Pre-Write Admission for Multi-Agent Code Co- | A cross-cutting scaffold/governance substrate for multi-agent software engineering, not tied to |
| **software_general** | Scaling Test-Time Compute for Agentic Coding | Generic test-time scaling method for agentic coding spanning multiple activities/worlds (issue  |
| **software_debugging** | Asking What Matters: Reward-Driven Clarification for Software  | Targets resolution of underspecified software engineering issues, matching the software_debuggi |
