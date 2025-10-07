<div align="center">
  <h1>🤖 Awesome Code Agents</h1>

  <!-- Badges -->
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome">
  </a>
  <a href="https://img.shields.io/badge/PRs-Welcome-red">
    <img src="https://img.shields.io/badge/PRs-Welcome-red" alt="PRs Welcome">
  </a>
  <a href="https://img.shields.io/github/last-commit/EuniAI/awesome-code-agents?color=green">
    <img src="https://img.shields.io/github/last-commit/EuniAI/awesome-code-agents?color=green" alt="Last Commit">
  </a>
</div>

<!-- Optional teaser -->
<!--
<p align="center">
  <img src="assets/teaser.png" width="520px"/>
</p>
-->
<p align="center">
  A curated list of <b>products, benchmarks, and research papers</b> on <b>Code Agents</b>.
</p>

---

## Quick Navigation

- [🚀 Products & Tools](#-products--tools)
- [📊 Leaderboards & Benchmarks](#-leaderboards--benchmarks)
- [📚 Papers](#-papers)
  * [Surveys](#-surveys)
  * [Environment Building](#-environment-building)
  * [Issue Reproduction](#-issue-reproduction)
  * [Issue Localization](#-issue-localization)
  * [Issue Resolution](#-issue-resolution)
  * [Q&A](#-qa)
  * [PR & Review](#-pr--review)
  * [Feature Development](#-feature-development)
  * [Git Management](#-git-management)
  * [Performance Optimization](#-performance-optimization)
  * [Website Generation](#-website-generation)
  * [Post-Training](#-post-training)
  * [Test-time Scaling](#-test-time-scaling)
  * [Multimodal](#-multimodal)
  * [Data Synthesis](#-data-synthesis)
  * [Empirical Studies](#-empirical-studies)  
- [🤝 Contributing](#-contributing)
- [🌟 Star History](#-star-history)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 🚀 Products & Tools
> Open-source systems, frameworks, and real-world developer assistants.

- **OpenHands** [![Star](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=social&label=Star)](https://github.com/All-Hands-AI/OpenHands) · [Website](https://all-hands.dev)
- **Prometheus** [![Star](https://img.shields.io/github/stars/EuniAI/Prometheus?style=social&label=Star)](https://github.com/EuniAI/Prometheus) · [Website](https://euni.ai/)
- **Aider** [![Star](https://img.shields.io/github/stars/paul-gauthier/aider?style=social&label=Star)](https://github.com/paul-gauthier/aider)
- **AutoCodeRover** 
- **KAT-Coder**
- **Kiro**
- **Droids**

---

## 📊 Leaderboards & Benchmarks
> Standardized evaluation suites for SWE agents.

- **SWE-bench Verified** — strict evaluation with verified solutions.  
  [![Star](https://img.shields.io/github/stars/princeton-nlp/SWE-bench?style=social&label=Star)](https://github.com/princeton-nlp/SWE-bench) · [Leaderboard](https://swe-bench.github.io/)

- **SWE-bench Pro** — professional benchmark variant for real-world SWE tasks.  
  [Link](https://swe-bench.github.io/)
- **SWE-bench Live** — SWE-bench Goes Live! [Link](https://swe-bench-live.github.io/)
- SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?
- SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks
- OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution
- SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation
- **Terminal-Bench** — command-line reasoning & execution benchmark.  
- **OSWorld / WebArena** — realistic environments for agent evaluation.  

---

## 📚 Papers
### 🔎 Surveys

- Agents in Software Engineering: Survey, Landscape, and Vision
- **OS Agents Survey** (Dec 2024) — survey on MLLM-based OS/IDE agents.  

---

### 🏗 Environment Building
> Papers describing new environments, IDE sandboxes, benchmarks, or agent playgrounds.

- R2E: Turning any Github Repository into a Programming Agent Environment
- R2E-Gym: Procedural Environment Generation and Hybrid Verifiers for Scaling Open-Weights SWE Agents
- RepoST: Scalable Repository-Level Coding Environment Construction with Sandbox Testing
- You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects
- Automated Benchmark Generation for Repository-Level Coding Tasks
- EnvBench: A Benchmark for Automated Environment Setup
- Treefix: Enabling Execution with a Tree of Prefixes
- CompileAgent: Automated Real-World Repo-Level Compilation with Tool-Integrated LLM-based Agent System
- AutoDev: Automated AI-Driven Development
- CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building
- CSR-Bench: Benchmarking LLM Agents in Deployment of Computer Science Research Repositories
- Automatically Generating Dockerfiles via Deep Learning: Challenges and Promises
- Beyond pip Install: Evaluating LLM Agents for the Automated Installation of Python Projects
- Repo2Run: Automated Building Executable Environment for Code Repository at Scale

### 🔁 Issue Reproduction
> Research on reproducing software bugs deterministically.

- Issue2Test: Generating Reproducing Test Cases from Issue Reports

### 🎯 Issue Localization
> Code search, fault localization, vulnerability detection.
- LocAgent: Graph-Guided LLM Agents for Code Localization
- ToolTrain: Tool-integrated Reinforcement Learning for Repo Deep Search
- CoSIL: Software Issue Localization via LLM-Driven Code Repository Graph Searching

### 🛠 Issue Resolution
> Automated bug fixing, patch generation, repair techniques.

- SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- AutoCodeRover: Autonomous Program Improvement
- Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases
- debug-gym: A Text-Based Environment for Interactive Debugging
- SemAgent: A Semantics-Aware Program Repair Agent
- CodeR: Issue Resolving with Multi-Agent and Task Graphs
- Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks
- SWE-Exp: Experience-Driven Software Issue Resolution
- SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents
- SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution
- Co-PatcheR: Collaborative Software Patching with Component(s)-specific Small Reasoning Models
- A Self-Improving Coding Agent
- SWE-Bench-CL: Continual Learning for Coding Agents
- Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling
- SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning
- Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning

### ❓ Q&A
> Code understanding, documentation, and retrieval-based Q&A.

- SWE-QA: Can Language Models Answer Repository-level Code Questions?

### 🔍 PR & Review
> Automated pull request creation, review assistance, linting, refactoring.  

### ✨ Feature Development
> Studies on agent-driven feature extension, repo-level edits.

- SWE-Dev: Evaluating and Training Autonomous Feature-Driven Software Development
- NoCode-bench: A Benchmark for Evaluating Natural Language-Driven Feature Addition

### 🔄 Git Management
> Agents for git workflows (branching, rebasing, conflict resolution).  

- GitGoodBench: A Novel Benchmark For Evaluating Agentic Performance On Git

### ⚡ Performance Optimization
> Code profiling, optimization, memory & latency improvements.

- SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories?

### 🌐 Website Generation
> Code agents that generate or maintain websites/frontends.

- WebGen-Bench: Evaluating LLMs on Generating Interactive and Functional Websites from Scratch
- ScreenCoder: Advancing Visual-to-Code Generation for Front-End Automation via Modular Multimodal Agents

### 🕹️ Unified Agents
> Unified Software Engineering agent as AI Software Engineer

### 🎓 Post-Training
> Instruction tuning, alignment, reinforcement learning for SWE agents.

- Training Software Engineering Agents and Verifiers with SWE-Gym
- SEAlign: Alignment Training for Software Engineering Agent

### ⚖ Test-time Scaling
> Chain-of-thought, self-reflection, scaling strategies during inference.  

- SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement
- Thinking Longer, Not Larger: Enhancing Software Engineering Agents via Scaling Test-Time Compute

### 🖼 Multimodal
> Agents that leverage images/screenshots/GUI for coding tasks.

- Seeing is Fixing: Cross-Modal Reasoning with Multimodal LLMs for Visual Software Issue Fixing

### 🧬 Data Synthesis
> Synthetic data generation for code tasks, self-play, augmentation.

- MCTS-Refined CoT: High-Quality Fine-Tuning Data for LLM-Based Repository Issue Resolution
- SWE-Flow: Synthesizing Software Engineering Data in a Test-Driven Manner
- SWE-Factory: Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks

### 📊 Empirical Studies
> Evaluations of LLMs/agents on large-scale software repositories. Analysis of failure cases, bias, reproducibility.  

- Understanding Software Engineering Agents Through the Lens of Traceability: An Empirical Study
- Can LLMs Replace Manual Annotation of Software Engineering Artifacts?
- Understanding Software Engineering Agents: A Study of Thought-Action-Result Trajectories

---

## 🤝 Contributing
We welcome contributions! Please:  
1. Use the [entry template](#entry-template).  
2. Place items in the right category & order by **reverse-chronology**.  
3. Include badges for GitHub stars, arXiv, website if available.

We're grateful to all our amazing contributors who have made this project what it is today!

<a href="https://github.com/EuniAI/awesome-code-agents/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=EuniAI/awesome-code-agents&r="  width="80px"/>
</a>

If you have any questions or encounter issues, please feel free to reach out. For quick queries, you can also check our `Issues` page for common questions and solutions.

---

## 🌟 Star History
[![Star History Chart](https://api.star-history.com/svg?repos=EuniAI/awesome-code-agents&type=Date)](https://www.star-history.com/#EuniAI/awesome-code-agents&Date)

---

## 🙏 Acknowledgements
- Thanks to all contributors and the research community.
