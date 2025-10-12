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
- **Jules** · [Website](https://jules.google/)
- **OpenCode** · [Website](https://opencode.ai/)
- **KAT-Coder**
- **Kiro** · [Website](https://kiro.dev/)
- **Droids**
- **Essential** · [Website](https://www.essential.com/)

---

## 📊 Benchmarks & Leaderboards
> Standardized evaluation suites for SWE agents.

<!-- START PAPERS:benchmarks -->
- **Terminal-Bench: A Benchmark for AI Agents in Terminal Environments.**  
  _The Terminal-Bench Team._ 2025.  
  [![GitHub Stars](https://img.shields.io/github/stars/laude-institute/terminal-bench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/laude-institute/terminal-bench) [![Website](https://img.shields.io/website?url=https://www.tbench.ai/&up_message=TBENCH.AI&up_color=blue&down_message=TBENCH.AI&down_color=blue&style=for-the-badge)](https://www.tbench.ai/)

- **SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?**  
  _Xiang Deng, Jeff Da, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean Hendryx, Zifan Wang, Chen Bo Calvin Zhang, Noah Jacobson, Bing Liu, Brad Kenstler._ arXiv 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.16941) [![GitHub Stars](https://img.shields.io/github/stars/scaleapi/SWE-bench_Pro-os?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/scaleapi/SWE-bench_Pro-os) [![Website](https://img.shields.io/website?url=https://scale.com/leaderboard/swe_bench_pro_public&up_message=SWE-BENCH-PRO-PUBLIC&up_color=blue&down_message=SWE-BENCH-PRO-PUBLIC&down_color=blue&style=for-the-badge)](https://scale.com/leaderboard/swe_bench_pro_public)

- **SWE-SQL: Illuminating LLM Pathways to Solve User SQL Issues in Real-World Applications.**  
  _Jinyang Li, Xiaolong Li, Ge Qu, Per Jacobsson, Bowen Qin, Binyuan Hui, Shuzheng Si, Nan Huo, Xiaohan Xu, Yue Zhang, Ziwei Tang, Yuanshuai Li, Florensia Widjaja, Xintong Zhu, Feige Zhou, Yongfeng Huang, Yannis Papakonstantinou, Fatma Ozcan, Chenhao Ma, Reynold Cheng._ arXiv 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.18951) [![GitHub Stars](https://img.shields.io/github/stars/bird-bench/BIRD-CRITIC-1?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/bird-bench/BIRD-CRITIC-1) [![Website](https://img.shields.io/website?url=https://bird-critic.github.io/&up_message=BIRD-CRITIC&up_color=blue&down_message=BIRD-CRITIC&down_color=blue&style=for-the-badge)](https://bird-critic.github.io/)

- **SWE-bench Goes Live!**  
  _Linghao Zhang, Shilin He, Chaoyun Zhang, Yu Kang, Bowen Li, Chengxing Xie, Junhao Wang, Maoquan Wang, Yufan Huang, Shengyu Fu, Elsie Nallipogu, Qingwei Lin, Yingnong Dang, Saravan Rajmohan, Dongmei Zhang._ arXiv 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.23419) [![GitHub Stars](https://img.shields.io/github/stars/microsoft/SWE-bench-Live?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/microsoft/SWE-bench-Live) [![Website](https://img.shields.io/website?url=https://swe-bench-live.github.io/&up_message=SWE-BENCH-LIVE&up_color=blue&down_message=SWE-BENCH-LIVE&down_color=blue&style=for-the-badge)](https://swe-bench-live.github.io/)

- **SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks.**  
  _Pavel Adamenko, Mikhail Ivanov, Aidar Valeev, Rodion Levichev, Pavel Zadorozhny, Ivan Lopatin, Dmitry Babayev, Alena Fenogenova, Valentin Malykh._ arXiv 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059) [![GitHub Stars](https://img.shields.io/github/stars/MERA-Evaluation/repotest?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/MERA-Evaluation/repotest) [![Website](https://img.shields.io/website?url=https://mera-evaluation.github.io/demo-swe-mera/&up_message=DEMO-SWE-MERA&up_color=blue&down_message=DEMO-SWE-MERA&down_color=blue&style=for-the-badge)](https://mera-evaluation.github.io/demo-swe-mera/)

- **SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?**  
  _Samuel Miserendino, Michele Wang, Tejal Patwardhan, Johannes Heidecke._ ICML 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.12115) [![GitHub Stars](https://img.shields.io/github/stars/openai/frontier-evals?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/openai/frontier-evals/tree/main/project/swelancer) [![Website](https://img.shields.io/website?url=https://openai.com/index/swe-lancer/&up_message=SWE-LANCER&up_color=blue&down_message=SWE-LANCER&down_color=blue&style=for-the-badge)](https://openai.com/index/swe-lancer/)

- **OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution.**  
  _Lianghong Guo, Wei Tao, Runhan Jiang, Yanlin Wang, Jiachi Chen, Xilin Liu, Yuchi Ma, Mingzhi Mao, Hongyu Zhang, Zibin Zheng._ ISSTA 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.04606) [![GitHub Stars](https://img.shields.io/github/stars/DeepSoftwareAnalytics/OmniGIRL?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/DeepSoftwareAnalytics/OmniGIRL) [![Website](https://img.shields.io/website?url=https://deepsoftwareanalytics.github.io/omnigirl_leaderboard.html&up_message=OMNIGIRL-LEADERBOARD&up_color=blue&down_message=OMNIGIRL-LEADERBOARD&down_color=blue&style=for-the-badge)](https://deepsoftwareanalytics.github.io/omnigirl_leaderboard.html)

- **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**  
  _Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan._ ICLR 2024.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2310.06770) [![GitHub Stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/SWE-bench/SWE-bench) [![Website](https://img.shields.io/website?url=https://www.swebench.com/&up_message=SWEBENCH&up_color=blue&down_message=SWEBENCH&down_color=blue&style=for-the-badge)](https://www.swebench.com/)
<!-- END PAPERS:benchmarks -->

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

<!-- START PAPERS:issue_resolution -->
- **Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases.**  
  _Zimin Chen, Yue Pan, Siyu Lu, Jiayi Xu, Claire Le Goues, Martin Monperrus, He Ye._ arXiv 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.19942) [![GitHub Stars](https://img.shields.io/github/stars/EuniAI/Prometheus?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/EuniAI/Prometheus) [![Website](https://img.shields.io/website?url=https://euni.ai/&up_message=EUNI.AI&up_color=blue&down_message=EUNI.AI&down_color=blue&style=for-the-badge)](https://euni.ai/)
<!-- END PAPERS:issue_resolution -->

- **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering.** _John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press._ NeurIPS 2024.<br>[![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15793) [![GitHub Stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/SWE-agent/SWE-agent)
- **AutoCodeRover: Autonomous Program Improvement.**  _Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury._ ISSTA 2024.<br>[![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2404.05427) [![GitHub Stars](https://img.shields.io/github/stars/AutoCodeRoverSG/auto-code-rover?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/AutoCodeRoverSG/auto-code-rover)
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

### 👩‍💻 Machine Learning Engineering
> Autonomous agents across end-to-end ML workflows.

<!-- START PAPERS:machine_learning_engineering -->
- **MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering.**  
  _Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, Aleksander Mądry._ ICLR 2025.  
  [![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2410.07095) [![GitHub Stars](https://img.shields.io/github/stars/openai/mle-bench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/openai/mle-bench) [![Website](https://img.shields.io/website?url=https://openai.com/index/mle-bench/&up_message=MLE-BENCH&up_color=blue&down_message=MLE-BENCH&down_color=blue&style=for-the-badge)](https://openai.com/index/mle-bench/)
<!-- END PAPERS:machine_learning_engineering -->

### SQL Issue Resolution
>  Fix user issues in real-world database applications (_e.g._, professional DBs).

- **SWE-SQL: Illuminating LLM Pathways to Solve User SQL Issues in Real-World Applications.** _Jinyang Li, Xiaolong Li, Ge Qu, Per Jacobsson, Bowen Qin, Binyuan Hui, Shuzheng Si, Nan Huo, Xiaohan Xu, Yue Zhang, Ziwei Tang, Yuanshuai Li, Florensia Widjaja, Xintong Zhu, Feige Zhou, Yongfeng Huang, Yannis Papakonstantinou, Fatma Ozcan, Chenhao Ma, Reynold Cheng._ arXiv 2025.<br>[![Paper](https://img.shields.io/badge/paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.18951) [![GitHub Stars](https://img.shields.io/github/stars/bird-bench/BIRD-CRITIC-1?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/bird-bench/BIRD-CRITIC-1)

### 🕹️ Unified Agents
> Unified Software Engineering agent as AI Software Engineer

### 🎓 Post-Training
> Instruction tuning, alignment, reinforcement learning for SWE agents.

- Training Software Engineering Agents and Verifiers with SWE-Gym
- SEAlign: Alignment Training for Software Engineering Agent
- Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards

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
- SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation


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
