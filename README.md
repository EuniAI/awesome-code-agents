<div align="center">

<a href="https://euni.ai/"><img src="./assets/icon.png" alt="Euni logo" height="135"></a>

# Awesome Code Agents

### The Digital World We Are Building. The Real World We Are Acting In.

*A curated, ever-growing collection of frontier research papers and technical reports on autonomous code agents.*

[![Stars](https://img.shields.io/github/stars/EuniAI/awesome-code-agents?style=for-the-badge&color=yellow)](https://github.com/EuniAI/awesome-code-agents/stargazers)
[![Forks](https://img.shields.io/github/forks/EuniAI/awesome-code-agents?style=for-the-badge&color=blue)](https://github.com/EuniAI/awesome-code-agents/forks)
[![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)
<br>
[![Papers](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FEuniAI%2Fawesome-code-agents%2Fmain%2Fassets%2Fpapers.json&style=for-the-badge)](#quick-navigation)
[![Last Commit](https://img.shields.io/github/last-commit/EuniAI/awesome-code-agents?style=for-the-badge&color=blueviolet)](https://github.com/EuniAI/awesome-code-agents/commits)
[![Commits](https://img.shields.io/github/commit-activity/m/EuniAI/awesome-code-agents?style=for-the-badge&color=blue&label=Commits)](https://github.com/EuniAI/awesome-code-agents/graphs/commit-activity)

[![Website](https://img.shields.io/badge/Website-2E3440?style=flat&logo=safari&logoColor=white)](https://euni.ai/)
[![X/Twitter](https://img.shields.io/badge/X%2FTwitter-000000?style=flat&logo=x&logoColor=white)](https://x.com/Euni_AI)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/euni-ai/)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/jDG4wqkKZj)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/EuniAI/awesome-code-agents)
<br>
[![Awesome](https://img.shields.io/badge/Awesome-2AA198?style=flat&logo=awesomelists&logoColor=white)](https://awesome.re)
[![Issues Closed](https://img.shields.io/github/issues-search?query=repo%3AEuniAI%2Fawesome-code-agents%20is%3Aclosed&label=Issues%20Closed&style=flat&logo=github&logoColor=white&color=5d6b98&labelColor=5d6b98)](https://github.com/EuniAI/awesome-code-agents/issues)
[![Discussions](https://img.shields.io/github/discussions/EuniAI/awesome-code-agents?label=Discussions&style=flat&logo=github&logoColor=white&color=7a5af8&labelColor=7a5af8)](https://github.com/EuniAI/awesome-code-agents/discussions)
[![PRs Welcome](https://img.shields.io/badge/PRs_Welcome-E24B4A?style=flat&logo=github&logoColor=white)](https://github.com/EuniAI/awesome-code-agents/pulls)

<img src="assets/main_v1-min.png" alt="Awesome Code Agents" width="100%">

*Photo Credit: [Gemini-Nano-Banana-Pro🍌](https://deepmind.google/models/gemini-image/pro/)*.

</div>

<!-- Optional teaser -->
<!--
<p align="center">
  <img src="assets/teaser.png" width="520px"/>
</p>
-->
<!-- <p align="center">
  A curated list of <b>frontier research papers and technical reports</b> on <b>Code Agents</b>.
</p> -->

---

## Quick Navigation

<!-- START PAPERS SUMMARY -->
🔥 **We are actively tracking the frontier research of code agents.**<br>
🧹 *The list below shows the last twelve months; the [full paper list](automation/PAPERS.md) holds the complete collection.*<br>
📚 *Currently collected:* **`470` papers.** *(Last update: 2026-07-12)*
<!-- END PAPERS SUMMARY -->

<!-- NAV:BEGIN -->
- [🧠 Foundation Models](#-foundation-models)
- [📊 Surveys & Empirical Studies](#-surveys--empirical-studies)
- [🧱 Code as Artifact: Building the Digital World](#-code-as-artifact-building-the-digital-world)
  * [💻 General Software](#-general-software)
    + [🐛 Debugging & Issue Resolution](#-debugging--issue-resolution)
    + [✏️ Code Generation & Completion](#-code-generation--completion)
    + [🛠️ Environment Setup & CI/CD](#-environment-setup--cicd)
    + [🔄 Maintenance & Evolution](#-maintenance--evolution)
    + [🔍 Code Review](#-code-review)
    + [🔒 Security](#-security)
    + [📖 Comprehension & Documentation](#-comprehension--documentation)
    + [🧪 Testing & Verification](#-testing--verification)
    + [🏗️ Feature Development](#-feature-development)
  * [🧊 3D & CAD](#-3d--cad)
  * [🌐 Web Applications](#-web-applications)
  * [🗄️ Databases](#-databases)
  * [🎨 Graphics & Animation](#-graphics--animation)
  * [⚙️ Systems](#-systems)
  * [🎮 Games](#-games)
  * [🔌 Hardware](#-hardware)
- [🌍 Code as Agency: Acting in the Real World](#-code-as-agency-acting-in-the-real-world)
  * [🔬 Research & Discovery](#-research--discovery)
  * [🖥️ Terminals & Operating Systems](#-terminals--operating-systems)
  * [🤖 The Physical World](#-the-physical-world)
  * [🕹️ Game Worlds](#-game-worlds)
  * [🧭 Browsers & the Web](#-browsers--the-web)
  * [🧰 Software Applications](#-software-applications)
<!-- NAV:END -->
- [🗺️ Research Landscape](#-research-landscape)
- [🤝 Contributing](#-contributing)
- [🌟 Star History](#-star-history)
- [🙏 Acknowledgements](#-acknowledgements)

---

<!-- PAPERS:BEGIN -->
## 🧠 Foundation Models

> Flagship frontier models that both write code and act through it.

- **LoopCoder-v2: Only Loop Once for Efficient Test-Time Computation Scaling.**  
  _Jian Yang, Shawn Guo, Wei Zhang, Tianyu Zheng, Yaxin Du, Haau-Sing Li, Jiajun Wu, Yue Song, Yan Xing, Qingsong Cai, et al._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.18023) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **KAT-Coder Technical Report.**  
  _Zizheng Zhan, Ken Deng, Jinghui Wang, Xiaojiang Zhang, Huaixi Tang, Minglei Zhang, Zhiyi Lai, Haoyang Huang, Wen Xiang, Kun Wu, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.18779) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **Kimi K2: Open Agentic Intelligence.**  
  _Kimi Team: Yifan Bai, Yiping Bao, Guanduo Chen, Jiahao Chen, Ningxin Chen, Ruijue Chen, Yanru Chen, Yuankun Chen, Yutian Chen, Zhuofu Chen, et al._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.20534) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

<sub>… plus 1 earlier paper(s): see the [full list](automation/PAPERS.md#-foundation-models).</sub>

## 📊 Surveys & Empirical Studies

> Research that studies and surveys code agents themselves.

- **3100 Opinions on Code Review in an AI World: Building Causal Theory from Practitioner Discourse.**  
  _Shyam Agarwal, Courtney Miller, Christian Kästner, Bogdan Vasilescu._ arXiv 2026/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.07980) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **From Solvers to Research: Large Language Model-Driven Formal Mathematics at the Research Frontier.**  
  _Eric Jiang, Xiao Liang, Yikai Zhang, Yingjia Wan, Mengting Li, Haikang Deng, Alexander K. Taylor, Justin Baker, Rushil Raghavan, Junyi Zhang, et al._ arXiv 2026/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.07779) ![Position Paper](https://img.shields.io/badge/Position_Paper-9B59B6?style=for-the-badge)

- **How Coding Agents Fail Their Users: A Large-Scale Analysis of Developer-Agent Misalignment in 20,574 Real-World Sessions.**  
  _Ningzhi Tang, Chaoran Chen, Gelei Xu, Yiyu Shi, Yu Huang, Collin McMillan, Tao Dong, Toby Jia-Jun Li._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.29442) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **TrajAudit: Automated Failure Diagnosis for Agentic Coding Systems.**  
  _Minxing Wang, Xiaofei Xie, Yintong Huo._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.26563) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents.**  
  _Bingchen Zhao, Dhruv Srikanth, Yuxiang Wu, Zhengyao Jiang._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.21384) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks.**  
  _Yubin Qu, Ying Zhang, Yanjun Zhang, Gelei Deng, Yuekang Li, Leo Yu Zhang, Yi Liu._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.18583) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Code as Agent Harness.**  
  _Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei, Jiaru Zou, Mengting Ai, Zhining Liu, Ting-Wei Li, et al._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.18747) ![Survey](https://img.shields.io/badge/Survey-2A9D8F?style=for-the-badge)

- **SWE-chat: Coding Agent Interactions From Real Users in the Wild.**  
  _Joachim Baumann, Vishakh Padmakumar, Xiang Li, John Yang, Diyi Yang, Sanmi Koyejo._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.20779) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems.**  
  _Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.14228) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **CodeTracer: Towards Traceable Agent States.**  
  _Han Li, Yifan Yao, Letian Zhu, Rili Feng, Hongyi Ye, Jiaming Wang, Yancheng He, Pengyu Zou, Lehan Zhang, Xinping Lei, et al._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.11641) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Programming by Chat: A Large-Scale Behavioral Analysis of 11,579 Real-World AI-Assisted IDE Sessions.**  
  _Ningzhi Tang, Chaoran Chen, Zihan Fang, Gelei Xu, Maria Dhakal, Yiyu Shi, Collin McMillan, Yu Huang, Toby Jia-Jun Li._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.00436) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **How Do Developers Interact with AI? An Exploratory Study on Modeling Developer Programming Behavior.**  
  _Yinan Wu, Ze Shi Li, Kathryn Thomasset Stolee, Bowen Xu._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.16393) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?**  
  _Tingxu Han, Yi Zhang, Wei Song, Chunrong Fang, Zhenyu Chen, Youcheng Sun, Lijie Hu._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.15401) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Fingerprinting AI Coding Agents on GitHub.**  
  _Taher A. Ghaleb._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.17406) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Agent READMEs: An Empirical Study of Context Files for Agentic Coding.**  
  _Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa, Brittany Reid, Kundjanasith Thonglek, Pattara Leelaprute, Arnon Rungsawang, Bundit Manaskasemsak, Bram Adams, Ahmed E. Hassan, et al._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.12884) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Does AI-Assisted Coding Deliver? A Difference-in-Differences Study of Cursor's Impact on Software Projects.**  
  _Hao He, Courtney Miller, Shyam Agarwal, Christian Kästner, Bogdan Vasilescu._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.04427) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **A Comprehensive Empirical Evaluation of Agent Frameworks on Code-centric Software Engineering Tasks.**  
  _Zhuowen Yin, Cuifeng Gao, Chunsong Fan, Wenzhang Yang, Yinxing Xue, Lijun Zhang._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.00872) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **A Survey of Vibe Coding with Large Language Models.**  
  _Yuyao Ge, Lingrui Mei, Zenghao Duan, Tianhao Li, Yujia Zheng, Yiwei Wang, Lexin Wang, Jiayu Yao, Tianyu Liu, Yujun Cai, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.12399) [![GitHub Stars](https://img.shields.io/github/stars/YuyaoGe/Awesome-Vibe-Coding?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/YuyaoGe/Awesome-Vibe-Coding) ![Survey](https://img.shields.io/badge/Survey-2A9D8F?style=for-the-badge)

- **How can we assess human-agent interactions? Case studies in software agent design.**  
  _Valerie Chen, Rohit Malhotra, Xingyao Wang, Juan Michelini, Xuhui Zhou, Aditya Bharat Soni, Hoang H. Tran, Calvin Smith, Ameet Talwalkar, Graham Neubig._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.09801) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LLM-Empowered Agentic System.**  
  _Jiale Guo, Suizhi Huang, Mei Li, Dong Huang, Xingsheng Chen, Regina Zhang, Zhijiang Guo, Han Yu, Siu-Ming Yiu, Christian Jensen, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.09721) [![GitHub Stars](https://img.shields.io/github/stars/lisaGuojl/LLM-Agent-SE-Survey?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/lisaGuojl/LLM-Agent-SE-Survey) ![Survey](https://img.shields.io/badge/Survey-2A9D8F?style=for-the-badge)

- **On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub.**  
  _Miku Watanabe, Hao Li, Yutaro Kashiwa, Brittany Reid, Hajimu Iida, Ahmed E. Hassan._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.14745) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Agentic Software Engineering: Foundational Pillars and a Research Roadmap.**  
  _Ahmed E. Hassan, Hao Li, Dayi Lin, Bram Adams, Tse-Hsun Chen, Yutaro Kashiwa, Dong Qiu._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.06216) ![Position Paper](https://img.shields.io/badge/Position_Paper-9B59B6?style=for-the-badge)

- **"My productivity is boosted, but ..." Demystifying Users' Perception on AI Coding Assistants.**  
  _Yunbo Lyu, Zhou Yang, Jieke Shi, Jianming Chang, Yue Liu, David Lo._ ASE 2025.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.12285) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **A Survey on Code Generation with LLM-based Agents.**  
  _Yihong Dong, Xue Jiang, Jiaru Qian, Tian Wang, Kechi Zhang, Zhi Jin, Ge Li._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.00083) [![GitHub Stars](https://img.shields.io/github/stars/JiaruQian/awesome-llm-based-agent4code?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/JiaruQian/awesome-llm-based-agent4code) ![Survey](https://img.shields.io/badge/Survey-2A9D8F?style=for-the-badge)

- **The Rise of AI Teammates in Software Engineering (SE) 3.0: How Autonomous Coding Agents Are Reshaping Software Engineering.**  
  _Hao Li, Haoxiang Zhang, Ahmed E. Hassan._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.15003) [![GitHub Stars](https://img.shields.io/github/stars/SAILResearch/AI_Teammates_in_SE3?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/SAILResearch/AI_Teammates_in_SE3) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.**  
  _Joel Becker, Nate Rush, Elizabeth Barnes, David Rein._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.09089) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

<sub>… plus 9 earlier paper(s): see the [full list](automation/PAPERS.md#-surveys--empirical-studies).</sub>

## 🧱 Code as Artifact: Building the Digital World

> Agents that build software, from one function to an entire system.

### 💻 General Software

> Writing and maintaining general-purpose software.

#### 🐛 Debugging & Issue Resolution

> Reproducing, locating, and fixing reported bugs.

- **AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation.**  
  _Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman Pozharskiy, Maksim Parshin, Sergey Nikolenko._ arXiv 2026/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.06624) [![GitHub Stars](https://img.shields.io/github/stars/agent-lens/agent-lens-bench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/agent-lens/agent-lens-bench) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Dockerless: Environment-Free Program Verifier for Coding Agents.**  
  _Wenhao Zeng, Yuling Shi, Xiaodong Gu, Chao Hu, Chaofan Wang, Yuhao Cui, Hongting Zhou, Mengnan Qi, Jianqiao Wangni, Zhaojian Yu, et al._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.28436) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **FastContext: Training Efficient Repository Explorer for Coding Agents.**  
  _Shaoqiu Zhang, Maoquan Wang, Yuling Shi, Yuhang Wang, Xiaodong Gu, Yongqiang Yao, Tori Gong, Sheng Chen, Rao Fu, Anisha Agarwal, et al._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.14066) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks.**  
  _Mengyu Zheng, Kai Han, Boxun Li, Haiyang Xu, Yuchuan Tian, Wei He, Hang Zhou, Jianyuan Guo, Hailin Hu, Lin Ma, et al._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.12344) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SWE-Explore: Benchmarking How Coding Agents Explore Repositories.**  
  _Shaoqiu Zhang, Yuhang Wang, Jialiang Liang, Yuling Shi, Wenhao Zeng, Maoquan Wang, Shilin He, Ningyuan Xu, Siyu Ye, Kai Cai, et al._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.07297) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **CODESKILL: Learning Self-Evolving Skills for Coding Agents.**  
  _Yanzhou Li, Yiran Zhang, Xiaoyu Zhang, Xiaoxia Liu, Yang Liu._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.25430)

- **AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation.**  
  _Priyam Sahoo, Gaurav Mittal, Xiaomin Li, Shengjie Ma, Benjamin Steenhoek, Pingping Lin, Yu Hu._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.12925) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **TACT: Mitigating Overthinking and Overacting in Coding Agents via Activation Steering.**  
  _Yuan Sui, Yulin Chen, Yibo Li, Xue Jiang, Yufei He, Yihong Dong, Xiaoxin He, Tianyu Gao, Bryan Hooi._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.05980)

- **Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis.**  
  _Jiahong Xiang, Xiaoyang Xu, Xiaopan Chu, Hongliang Tian, Yuqun Zhang._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.24212)

- **Asking What Matters: Reward-Driven Clarification for Software Engineering Tasks.**  
  _Sanidhya Vijayvargiya, Vijay Viswanathan, Graham Neubig._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.14624) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **Scaling Test-Time Compute for Agentic Coding.**  
  _Joongwon Kim, Wannan Yang, Kelvin Niu, Hongming Zhang, Yun Zhu, Eryk Helenowski, Ruan Silva, Zhengxing Chen, Srinivasan Iyer, Manzil Zaheer, et al._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.16529)

- **How and Why Agents Can Identify Bug-Introducing Commits.**  
  _Niklas Risse, Marcel Böhme._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.29378) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Coherence Collapse: Diagnosing Why Code Agents Fail After Reaching the Right Code.**  
  _Myeongsoo Kim, Dingmin Wang, Siwei Cui, Farima Farmahinifarahani, Terry Yue Zhuo, Shweta Garg, Baishakhi Ray, Rajdeep Mukherjee, Varun Kumar._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.24631) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **SWE-Next: Scalable Real-World Software Engineering Tasks for Agents.**  
  _Jiarong Liang, Zhiheng Lyu, Zijie Liu, Xiangchao Chen, Ping Nie, Kai Zou, Wenhu Chen._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.20691) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **daVinci-Env: Open SWE Environment Synthesis at Scale.**  
  _Dayuan Fu, Shenyu Wu, Yunze Wu, Zerui Peng, Yaxing Huang, Jie Sun, Ji Zeng, Mohan Jiang, Lin Zhang, Yukun Li, et al._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.13023) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?**  
  _Guoxin Chen, Fanzhe Meng, Jiale Zhao, Minghao Li, Daixuan Cheng, Huatong Song, Jie Chen, Yuzhi Lin, Hui Chen, Xin Zhao, et al._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.03194) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark.**  
  _Boxi Yu, Yang Cao, Yuzhong Zhang, Liting Lin, Junjielong Xu, Zhiqing Zhong, Qinghua Xu, Guancheng Wang, Jialun Cao, Shing-Chi Cheung, et al._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.00520) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale.**  
  _Ibragim Badertdinov, Maksim Nekrashevich, Anton Shevtsov, Alexander Golubev._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.23866) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SWE-MiniSandbox: Container-Free Reinforcement Learning for Building Software Engineering Agents.**  
  _Danlong Yuan, Wei Wu, Enhan Zhao, Zhengren Wang, Xueliang Zhao, Huishuai Zhang, Dongyan Zhao._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.11210)

- **Immersion in the GitHub Universe: Scaling Coding Agents to Mastery.**  
  _Jiale Zhao, Guoxin Chen, Fanzhe Meng, Minghao Li, Jie Chen, Hui Xu, Yongshuai Sun, Wayne Xin Zhao, Ruihua Song, Yuan Zhang, et al._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.09892) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Rethinking the Value of Agent-Generated Tests for LLM-Based Software Engineering Agents.**  
  _Zhi Chen, Zhensu Sun, Yuling Shi, Chao Peng, Xiaodong Gu, David Lo, Lingxiao Jiang._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.07900) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **SWE-Universe: Scale Real-World Verifiable Environments to Millions.**  
  _Mouxiang Chen, Lei Zhang, Yunlong Feng, Xuwu Wang, Wenting Zhao, Ruisheng Cao, Jiaxi Yang, Jiawei Chen, Mingze Li, Zeyao Ma, et al._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.02361) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Closing the Loop: Universal Repository Representation with RPG-Encoder.**  
  _Jane Luo, Chengyu Yin, Xin Zhang, Qingtao Li, Steven Liu, Yiming Huang, Jie Wu, Hao Liu, Yangyu Huang, Yu Kang, et al._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.02084)

- **SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving.**  
  _Chaofan Tao, Jierun Chen, Yuxin Jiang, Kaiqi Kou, Shaowei Wang, Ruoyu Wang, Xiaohui Li, Sidi Yang, Yiming Du, Jianbo Dai, et al._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.01426) [![GitHub Stars](https://img.shields.io/github/stars/SWE-Lego/SWE-Lego?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/SWE-Lego/SWE-Lego) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **Toward Training Superintelligent Software Agents through Self-Play SWE-RL.**  
  _Yuxiang Wei, Zhiqing Sun, Emily McMilin, Jonas Gehring, David Zhang, Gabriel Synnaeve, Daniel Fried, Lingming Zhang, Sida Wang._ arXiv 2025/12.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.18552) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases.**  
  _Zhaodong Wang, Zhenting Qi, Sherman Wong, Nathan Hu, Samuel Lin, Jun Ge, Erwin Gao, Wenlin Chen, Yilun Du, Minlan Yu, et al._ arXiv 2025/12.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.10398)

- **InfCode: Adversarial Iterative Refinement of Tests and Patches for Reliable Software Issue Resolution.**  
  _KeFan Li, Mengfei Wang, Hengzhi Zhang, Zhichao Li, Yuan Yuan, Mu Li, Xiang Gao, Hailong Sun, Chunming Hu, Weifeng Lv._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.16004)

- **Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly?**  
  _Chunqiu Steven Xia, Zhe Wang, Yan Yang, Yuxiang Wei, Lingming Zhang._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.13646) [![GitHub Stars](https://img.shields.io/github/stars/OpenAutoCoder/live-swe-agent?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/OpenAutoCoder/live-swe-agent)

- **SWE-Compass: Towards Unified Evaluation of Agentic Coding Abilities for Large Language Models.**  
  _Jingxuan Xu, Ken Deng, Weihao Li, Songwei Yu, Huaixi Tang, Haoyang Huang, Zhiyi Lai, Zizheng Zhan, Yanan Wu, Chenchen Zhang, et al._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.05459) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents.**  
  _Xingyao Wang, Simon Rosenberg, Juan Michelini, Calvin Smith, Hoang Tran, Engel Nyst, Rohit Malhotra, Xuhui Zhou, Valerie Chen, Robert Brennan, et al._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.03690) [![GitHub Stars](https://img.shields.io/github/stars/OpenHands/software-agent-sdk?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/OpenHands/software-agent-sdk)

- **SWE-Sharp-Bench: A Reproducible Benchmark for C# Software Engineering Tasks.**  
  _Sanket Mhatre, Yasharth Bajpai, Sumit Gulwani, Emerson Murphy-Hill, Gustavo Soares._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.02352) [![GitHub Stars](https://img.shields.io/github/stars/microsoft/prose?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/microsoft/prose/tree/main/misc/SWE-Sharp-Bench) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **HAFixAgent: History-Aware Automated Program Repair Agent.**  
  _Yu Shi, Hao Li, Bram Adams, Ahmed E. Hassan._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.01047)

- **Understanding Code Agent Behaviour: An Empirical Study of Success and Failure Trajectories.**  
  _Oorja Majgaonkar, Zhiwei Fei, Xiang Li, Federica Sarro, He Ye._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.00197) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **TDFlow: Agentic Workflows for Test Driven Software Engineering.**  
  _Kevin Han, Siddharth Maddikayala, Tim Knappe, Om Patel, Austen Liao, Amir Barati Farimani._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.23761)

- **BugPilot: Complex Bug Generation for Efficient Learning of SWE Skills.**  
  _Atharv Sonwane, Isadora White, Hyunji Lee, Matheus Pereira, Lucas Caccia, Minseon Kim, Zhengyan Shi, Chinmay Singh, Alessandro Sordoni, Marc-Alexandre Côté, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.19898) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **When Old Meets New: Evaluating the Impact of Regression Tests on SWE Issue Resolution.**  
  _Yang Chen, Toufique Ahmed, Reyhaneh Jabbarvand, Martin Hirzel._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.18270)

- **More with Less: An Empirical Study of Turn-Control Strategies for Efficient Coding Agents.**  
  _Pengfei Gao, Chao Peng._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.16786) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **SIADAFIX: issue description response for adaptive program repair.**  
  _Xin Cao, Nan Yu._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://www.arxiv.org/abs/2510.16059) [![GitHub Stars](https://img.shields.io/github/stars/liauto-siada/siada-cli?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/liauto-siada/siada-cli)

- **Lingxi: Repository-Level Issue Resolution Framework Enhanced by Procedural Knowledge Guided Scaling.**  
  _Xu Yang, Jiayuan Zhou, Michael Pacheco, Wenhan Zhu, Pengfei He, Shaowei Wang, Kui Liu, Ruiqi Pan._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.11838) [![GitHub Stars](https://img.shields.io/github/stars/lingxi-agent/Lingxi?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/lingxi-agent/Lingxi)

- **Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation.**  
  _Spandan Garg, Ben Steenhoek, Yufan Huang._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.08996) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement.**  
  _Anvith Pabba, Simin Chen, Alex Mathai, Anindya Chakraborty, Baishakhi Ray._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.03588)

- **Abstain and Validate: A Dual-LLM Policy for Reducing Noise in Agentic Program Repair.**  
  _José Cambronero, Michele Tufano, Sherry Shi, Renyao Wei, Grant Uy, Runxiang Cheng, Chin-Jung Liu, Shiying Pan, Satish Chandra, Pat Rondon._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.03217)

- **Improving Code Localization with Repository Memory.**  
  _Boshi Wang, Weijian Xu, Yunsheng Li, Mei Gao, Yujia Xie, Huan Sun, Dongdong Chen._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.01003)

- **ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory.**  
  _Siru Ouyang, Jun Yan, I-Hung Hsu, Yanfei Chen, Ke Jiang, Zifeng Wang, Rujun Han, Long T. Le, Samira Daruki, Xiangru Tang, et al._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25140)

- **Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents.**  
  _Zonghan Yang, Shengjie Wang, Kelin Fu, Wenyang He, Weimin Xiong, Yibo Liu, Yibo Miao, Bofei Gao, Yejie Wang, Yingwei Ma, et al._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.23045) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **A Benchmark for Localizing Code and Non-Code Issues in Software Projects.**  
  _Zejun Zhang, Jian Wang, Qingyun Yang, Yifan Pan, Yi Tang, Yi Li, Zhenchang Xing, Tian Zhang, Xuandong Li, Guoan Zhang._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25242) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Extracting Conceptual Knowledge to Locate Software Issues.**  
  _Ying Wang, Wenjun Mao, Chong Wang, Zhenhao Zhou, Yicheng Zhou, Wenyun Zhao, Yiling Lou, Xin Peng._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.21427)

- **SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?**  
  _Xiang Deng, Jeff Da, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, et al._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.16941) [![GitHub Stars](https://img.shields.io/github/stars/scaleapi/SWE-bench_Pro-os?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/scaleapi/SWE-bench_Pro-os) [![Website](https://img.shields.io/badge/SWE--BENCH--PRO--PUBLIC-blue?style=for-the-badge)](https://scale.com/leaderboard/swe_bench_pro_public) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **An Empirical Study on Failures in Automated Issue Solving.**  
  _Simiao Liu, Fang Liu, Liehao Li, Xin Tan, Yinghao Zhu, Xiaoli Lian, Li Zhang._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.13941) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints.**  
  _Zhiyu Fan, Kirill Vasilevski, Dayi Lin, Boyuan Chen, Yihao Chen, Zhiqing Zhong, Jie M. Zhang, Pinjia He, Ahmed E. Hassan._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.09853) [![Website](https://img.shields.io/badge/SWE--EFFI-blue?style=for-the-badge)](https://github.com/Centre-for-Software-Excellence/SWE-Effi) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **SWE-Mirror: Scaling Issue-Resolving Datasets by Mirroring Issues Across Repositories.**  
  _Junhao Wang, Daoguang Zan, Shulin Xin, Siyao Liu, Yurong Wu, Kai Shen._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.08724) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Automated Generation of Issue-Reproducing Tests by Combining LLMs and Search-Based Testing.**  
  _Konstantinos Kitsios, Marco Castelluccio, Alberto Bacchelli._ ASE 2025.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.01616) [![GitHub Stars](https://img.shields.io/github/stars/kitsiosk/blast?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/kitsiosk/blast)

- **Execution-Feedback Driven Test Generation from SWE Issues.**  
  _Toufique Ahmed, Jatin Ganhotra, Avraham Shinnar, Martin Hirzel._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.06365)

- **Tool-integrated Reinforcement Learning for Repo Deep Search.**  
  _Zexiong Ma, Chao Peng, Qunhong Zeng, Pengfei Gao, Yanzhen Zou, Bing Xie._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.03012) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning.**  
  _Alexander Golubev, Maria Trofimova, Sergei Polezhaev, Ibragim Badertdinov, Maksim Nekrashevich, Anton Shevtsov, Simon Karasik, Sergey Abramov, Andrei Andriushchenko, Filipp Fisin, et al._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.03501)

- **SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents.**  
  _Jiaye Lin, Yifu Guo, Yuzhen Han, Sen Hu, Ziyi Ni, Licheng Wang, Mingguang Chen, Hongzhang Liu, Ronghao Chen, Yangfan He, et al._ NeurIPS 2025.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.02085) [![GitHub Stars](https://img.shields.io/github/stars/JARVIS-Xs/SE-Agent?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/JARVIS-Xs/SE-Agent) [![Website](https://img.shields.io/badge/QUANTAALPHA-blue?style=for-the-badge)](https://quantaalpha.com/)

- **RepoForge: Training a SOTA Fast-thinking SWE Agent with an End-to-End Data Curation Pipeline Synergizing SFT and RL at Scale.**  
  _Zhilong Chen, Chengzong Zhao, Boyuan Chen, Dayi Lin, Yihao Chen, Arthur Leung, Gopi Krishnan Rajbahadur, Gustavo Oliva, Haoxiang Zhang, Aadi Bhatia, et al._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01550) [![Website](https://img.shields.io/badge/REPOFORGE-blue?style=for-the-badge)](https://centre-for-software-excellence.github.io/docs/blog/repoforge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Leveraging Large Language Model for Information Retrieval-based Bug Localization.**  
  _Moumita Asad, Rafed Muhammad Yasir, Sam Malek._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.00253)

- **Trae Agent: An LLM-based Agent for Software Engineering with Test-time Scaling.**  
  _Trae Research Team: Pengfei Gao, Zhao Tian, Xiangxin Meng, Xinchen Wang, Ruida Hu, Yuanan Xiao, Yizhou Liu, Zhao Zhang, Junjie Chen, Cuiyun Gao, et al._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23370) [![GitHub Stars](https://img.shields.io/github/stars/bytedance/trae-agent?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/bytedance/trae-agent) [![Website](https://img.shields.io/badge/TRAE.AI-blue?style=for-the-badge)](https://www.trae.ai/)

- **SWE-Exp: Experience-Driven Software Issue Resolution.**  
  _Silin Chen, Shaoxin Lin, Xiaodong Gu, Yuling Shi, Heng Lian, Longfei Yun, Dong Chen, Weiguo Sun, Lin Cao, Qianxiang Wang._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23361) [![GitHub Stars](https://img.shields.io/github/stars/YerbaPage/SWE-Exp?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/YerbaPage/SWE-Exp)

- **SWE-Debate: Competitive Multi-Agent Debate for Software Issue Resolution.**  
  _Han Li, Yuling Shi, Shaoxin Lin, Xiaodong Gu, Heng Lian, Xin Wang, Yantao Jia, Tao Huang, Qianxiang Wang._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.23348) [![GitHub Stars](https://img.shields.io/github/stars/YerbaPage/SWE-Debate?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/YerbaPage/SWE-Debate)

- **AutoCodeSherpa: Symbolic Explanations in AI Coding Agents.**  
  _Sungmin Kang, Haifeng Ruan, Abhik Roychoudhury._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.22414)

- **Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases.**  
  _Zimin Chen, Yue Pan, Siyu Lu, Jiayi Xu, Claire Le Goues, Martin Monperrus, He Ye._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.19942) [![GitHub Stars](https://img.shields.io/github/stars/EuniAI/Prometheus?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/EuniAI/Prometheus) [![Website](https://img.shields.io/badge/EUNI.AI-blue?style=for-the-badge)](https://euni.ai/)

- **Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic approach with static analysis and test execution feedback.**  
  _Chandra Maddila, Adam Tait, Claire Chang, Daniel Cheng, Nauman Ahmad, Vijayaraghavan Murali, Marshall Roch, Arnaud Avondet, Aaron Meltzer, Victor Montalvao, et al._ TSE 2025.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.18755) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **AssertFlip: Reproducing Bugs via Inversion of LLM-Generated Passing Tests.**  
  _Lara Khatib, Noble Saji Mathews, Meiyappan Nagappan._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.17542)

- **SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks.**  
  _Pavel Adamenko, Mikhail Ivanov, Aidar Valeev, Rodion Levichev, Pavel Zadorozhny, Ivan Lopatin, Dmitry Babayev, Alena Fenogenova, Valentin Malykh._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.11059) [![GitHub Stars](https://img.shields.io/github/stars/MERA-Evaluation/repotest?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/MERA-Evaluation/repotest) [![Website](https://img.shields.io/badge/DEMO--SWE--MERA-blue?style=for-the-badge)](https://mera-evaluation.github.io/demo-swe-mera/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation.**  
  _Gustavo A. Oliva, Gopi Krishnan Rajbahadur, Aaditya Bhatia, Haoxiang Zhang, Yihao Chen, Zhilong Chen, Arthur Leung, Dayi Lin, Boyuan Chen, Ahmed E. Hassan._ ASE 2025.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.09108) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 86 earlier paper(s): see the [full list](automation/PAPERS.md#-debugging--issue-resolution).</sub>

#### ✏️ Code Generation & Completion

> Generating and completing code, from a function to a whole repository.

- **ATM: CID-Brokered Pre-Write Admission for Multi-Agent Code Co-Synthesis.**  
  _Eagl Huang._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.00041)

- **DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch.**  
  _Jiale Zhao, Guoxin Chen, Fanzhe Meng, Wayne Xin Zhao, Ruihua Song, Ji-Rong Wen, Kai Jia._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.10728) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution.**  
  _Liliana Hotsko, Yinxi Li, Yuntian Deng, Pengyu Nie._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.06492) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **CoRe-Code: Collaborative Reinforcement Learning for Code Generation.**  
  _Zhihao Dou, Qinjian Zhao, Zhongwei Wan, Xiaoyu Xia, Sumon Biswas._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.24812)

- **RepoZero: Can LLMs Generate a Code Repository from Scratch?**  
  _Zhaoxi Zhang, Yiming Xu, Jiahui Liang, Weikang Li, Xiaoshuai Chen, Liwei Qian, Xin Pei, Jizhou Huang, Run Sun, Yunfang Wu._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.07122) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **PlayCoder: Making LLM-Generated GUI Code Playable.**  
  _Zhiyuan Peng, Wei Tao, Xin Yin, Chenhao Ying, Yuan Luo, Yiwen Guo._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.19742) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Benchmarking PhD-Level Coding in 3D Geometric Computer Vision.**  
  _Wenyi Li, Renkai Luo, Yue Yu, Huan-ang Gao, Mingju Gao, Li Yuan, Chaoyou Fu, Hao Zhao._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.30038) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **InCoder-32B: Code Foundation Model for Industrial Scenarios.**  
  _Jian Yang, Wei Zhang, Jiajun Wu, Junhang Cheng, Shawn Guo, Haowen Wang, Weicheng Gu, Yaxin Du, Joseph Li, Fanglin Xu, et al._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.16790) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents.**  
  _Zhirui Zhang, Hongbo Zhang, Haoxiang Fei, Zhiyuan Bao, Yubin Chen, Zhengyu Lei, Ziyue Liu, Yixuan Sun, Mingkun Xiao, Zihang Ye, et al._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.09447) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **DevBench: A Realistic, Developer-Informed Benchmark for Code Generation Models.**  
  _Adarsh Kumarappan, Pareesa Ameneh Golnari, Wen Wen, Xiaoyu Liu, Gabriel Ryan, Yuting Sun, Shengyu Fu, Elsie Nallipogu._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.11895) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Smarter Together: Creating Agentic Communities of Practice through Shared Experiential Learning.**  
  _Valentin Tablan, Scott Taylor, Gabriel Hurtado, Kristoffer Bernhem, Anders Uhrenholt, Gabriele Farei, Karo Moilanen._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.08301)

- **Towards Realistic Project-Level Code Generation via Multi-Agent Collaboration and Semantic Architecture Modeling.**  
  _Qianhui Zhao, Li Zhang, Fang Liu, Junhang Cheng, Chengru Wu, Junchen Ai, Qiaoyuanhe Meng, Lichen Zhang, Xiaoli Lian, Shubin Song, et al._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.03404) [![GitHub Stars](https://img.shields.io/github/stars/whisperzqh/ProjectGen?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/whisperzqh/ProjectGen) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence.**  
  _Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Lei Li, Kai Chen, Qipeng Guo, Ben Kao, Fei Yuan._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.23538) [![GitHub Stars](https://img.shields.io/github/stars/InternLM/JanusCoder?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/InternLM/JanusCoder) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **SpecAgent: A Speculative Retrieval and Forecasting Agent for Code Completion.**  
  _George Ma, Anurag Koul, Qi Chen, Yawen Wu, Sachit Kuhar, Yu Yu, Aritra Sengupta, Varun Kumar, Murali Krishna Ramanathan._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.17925) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Vibe Checker: Aligning Code Evaluation with Human Preference.**  
  _Ming Zhong, Xiang Zhou, Ting-Yun Chang, Qingze Wang, Nan Xu, Xiance Si, Dan Garrette, Shyam Upadhyay, Jeremiah Liu, Jiawei Han, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.07315) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches.**  
  _Yicheng Tao, Yao Qin, Yepang Liu._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.04905) ![Survey](https://img.shields.io/badge/Survey-2A9D8F?style=for-the-badge)

- **CWM: An Open-Weights LLM for Research on Code Generation with World Models.**  
  _FAIR CodeGen team, Jade Copet, Quentin Carbonneaux, Gal Cohen, Jonas Gehring, Jacob Kahn, Jannik Kossen, Felix Kreuk, Emily McMilin, Michel Meyer, et al._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.02387) [![GitHub Stars](https://img.shields.io/github/stars/facebookresearch/cwm?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/facebookresearch/cwm) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation.**  
  _Jane Luo, Xin Zhang, Steven Liu, Jie Wu, Jianfeng Liu, Yiming Huang, Yangyu Huang, Chengyu Yin, Ying Xin, Yuefeng Zhan, et al._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.16198) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion.**  
  _Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.05980)

- **VisCodex: Unified Multimodal Code Generation via Merging Vision and Coding Models.**  
  _Lingjie Jiang, Shaohan Huang, Xun Wu, Yixia Li, Dongdong Zhang, Furu Wei._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.09945) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Next Edit Prediction: Learning to Predict Code Edits from Context and Interaction History.**  
  _Ruofan Lu, Yintong Huo, Meng Zhang, Yichen Li, Michael R. Lyu._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.10074) [![GitHub Stars](https://img.shields.io/github/stars/lurf21/NextEditPrediction?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/lurf21/NextEditPrediction) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **SimdBench: Benchmarking Large Language Models for SIMD-Intrinsic Code Generation.**  
  _Yibo He, Shuoran Zhao, Jiaming Huang, Yingjie Fu, Hao Yu, Cunjian Huang, Tao Xie._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.15224) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 39 earlier paper(s): see the [full list](automation/PAPERS.md#-code-generation--completion).</sub>

#### 🛠️ Environment Setup & CI/CD

> Setting up environments, builds, CI/CD, and version control.

- **SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code Repository Setup?**  
  _Zihang Zhou, Ziqian Ren, Yukai Wu, Yingjie Xiong, Wei Zhou, Chao Peng, Dong Zhang, Bingheng Yan, Xuanhe Zhou, Fan Wu._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.26186)

- **DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle.**  
  _Yuheng Tang, Kaijie Zhu, Bonan Ruan, Chuqi Zhang, Michael Yang, Hongwei Li, Suyue Guo, Tianneng Shi, Zekun Li, Christopher Kruegel, et al._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.20882) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Exploring and Unleashing the Power of Large Language Models in CI/CD Configuration Translation.**  
  _Chong Wang, Chen Zhang, Jiajun Wu, Wunan Guo, Jianfeng Qu, Yewen Tian, Yang Liu._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.01316) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Can Language Models Go Beyond Coding? Assessing the Capability of Language Models to Build Real-World Systems.**  
  _Chenyu Zhao, Shenglin Zhang, Zeshun Huang, Weilin Jin, Yongqian Sun, Dan Pei, Chaoyun Zhang, Qingwei Lin, Chetan Bansal, Saravan Rajmohan, et al._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.00780) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Process-Level Trajectory Evaluation for Environment Configuration in Software Engineering Agents.**  
  _Jiayi Kuang, Yinghui Li, Xin Zhang, Yangning Li, Di Yin, Xing Sun, Ying Shen, Philip S. Yu._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.25694) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 12 earlier paper(s): see the [full list](automation/PAPERS.md#-environment-setup--cicd).</sub>

#### 🔄 Maintenance & Evolution

> Refactoring, migrating, and optimizing existing code.

- **SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration.**  
  _Jialong Chen, Xander Xu, Hu Wei, Chuan Chen, Bing Zhao._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.03823) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Controlled Self-Evolution for Algorithmic Code Optimization.**  
  _Tu Hu, Ronghao Chen, Shuo Zhang, Jianghao Yin, Mou Xiao Feng, Jingping Liu, Shaolei Zhang, Wenqi Jiang, Yuqi Fang, Sen Hu, et al._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.07348) [![GitHub Stars](https://img.shields.io/github/stars/QuantaAlpha/EvoControl?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/QuantaAlpha/EvoControl)

- **RefAgent: A Multi-agent LLM-based Framework for Automatic Software Refactoring.**  
  _Khouloud Oueslati, Maxime Lamothe, Foutse Khomh._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.03153)

- **What a diff makes: automating code migration with large language models.**  
  _Katherine A. Rosenfeld, Cliff C. Kerr, Jessica Lundin._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.00160) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair.**  
  _Ali Reza Ibrahimzada, Brandon Paulsen, Reyhaneh Jabbarvand, Joey Dodds, Daniel Kroening._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.16187)

- **SWE-Perf: Can Language Models Optimize Code Performance on Real-World Repositories?**  
  _Xinyi He, Qian Liu, Mingzhe Du, Lin Yan, Zhijie Fan, Yiming Huang, Zejian Yuan, Zejun Ma._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.12415) [![GitHub Stars](https://img.shields.io/github/stars/SWE-Perf/SWE-Perf?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/SWE-Perf/SWE-Perf) [![Website](https://img.shields.io/badge/SWE--PERF-blue?style=for-the-badge)](https://swe-perf.github.io/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 4 earlier paper(s): see the [full list](automation/PAPERS.md#-maintenance--evolution).</sub>

#### 🔍 Code Review

> Reviewing code changes and pull requests.

- **Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency.**  
  _Chris Adams, Arjun Singh Banga, Parveen Bansal, Souvik Bhattacharya, Rujin Cao, Pedro Canahuati, Nate Cook, Brian Ellis, Prabhakar Goyal, Gurinder Grewal, et al._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.30208) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **Issue-Oriented Agent-Based Framework for Automated Review Comment Generation.**  
  _Shuochuan Li, Dong Wang, Patanamon Thongtanunam, Zan Wang, Jiuqiao Yu, Junjie Chen._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.00517)

- **Benchmarking and Studying the LLM-based Code Review.**  
  _Zhengran Zeng, Ruikai Shi, Keke Han, Yixin Li, Kaicheng Sun, Yidong Wang, Zhuohao Yu, Rui Xie, Wei Ye, Shikun Zhang._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.01494) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 4 earlier paper(s): see the [full list](automation/PAPERS.md#-code-review).</sub>

#### 🔒 Security

> Detecting and fixing security vulnerabilities in code.

- **VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection.**  
  _Yuzhou Nie, Hongwei Li, Chengquan Guo, Ruizhe Jiang, Zhun Wang, Bo Li, Dawn Song, Wenbo Guo._ arXiv 2025/12.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.07533) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks.**  
  _Songwen Zhao, Danqing Wang, Kexun Zhang, Jiaxuan Luo, Zhuo Li, Lei Li._ arXiv 2025/12.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.03262) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **When “Correct” Is Not Safe: Can We Trust Functionally Correct Patches Generated by Code Agents?**  
  _Yibo Peng, James Song, Lei Li, Xinyu Yang, Mihai Christodorescu, Ravi Mangal, Corina Pasareanu, Haizhong Zheng, Beidi Chen._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.17862) [![GitHub Stars](https://img.shields.io/github/stars/Infini-AI-Lab/FCV?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/Infini-AI-Lab/FCV) [![Website](https://img.shields.io/badge/FCV-blue?style=for-the-badge)](https://infini-ai-lab.github.io/FCV/)

- **From Trace to Line: LLM Agent for Real-World OSS Vulnerability Localization.**  
  _Haoran Xi, Minghao Shao, Brendan Dolan-Gavitt, Muhammad Shafique, Ramesh Karri._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.02389) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SecureAgentBench: Benchmarking Secure Code Generation under Realistic Vulnerability Scenarios.**  
  _Junkai Chen, Huihui Huang, Yunbo Lyu, Junwen An, Jieke Shi, Chengran Yang, Ting Zhang, Haoye Tian, Yikun Li, Zhenhao Li, et al._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.22097) [![GitHub Stars](https://img.shields.io/github/stars/iCSawyer/SecureAgentBench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/iCSawyer/SecureAgentBench) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Locus: Agentic Predicate Synthesis for Directed Fuzzing.**  
  _Jie Zhu, Chihao Shen, Ziyang Li, Jiahao Yu, Yizheng Chen, Kexin Pei._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.21302)

<sub>… plus 4 earlier paper(s): see the [full list](automation/PAPERS.md#-security).</sub>

#### 📖 Comprehension & Documentation

> Understanding, documenting, and searching code.

- **SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution.**  
  _Mohit Raghavendra, Soham Dan, Miguel Romero Calvo, Yannis Yiming He, Johannes Baptist Mols, Gautam Anand, Cole McCollum, Edgar Arakelyan, Vijay Bharadwaj, Andrew Park, et al._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.08366) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Lost in Code Generation: Reimagining the Role of Software Models in AI-driven Software Engineering.**  
  _Jürgen Cito, Dominik Bork._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.02475) ![Position Paper](https://img.shields.io/badge/Position_Paper-9B59B6?style=for-the-badge)

- **Gistify! Codebase-Level Understanding via Runtime Execution.**  
  _Hyunji Lee, Minseon Kim, Chinmay Singh, Matheus Pereira, Atharv Sonwane, Isadora White, Elias Stengel-Eskin, Mohit Bansal, Zhengyan Shi, Alessandro Sordoni, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.26790) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **RANGER: Repository-Level Agent for Graph-Enhanced Retrieval.**  
  _Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25257)

- **SWE-QA: Can Language Models Answer Repository-level Code Questions?**  
  _Weihan Peng, Yuling Shi, Yuhang Wang, Xinyun Zhang, Beijun Shen, Xiaodong Gu._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.14635) [![GitHub Stars](https://img.shields.io/github/stars/peng-weihan/SWE-QA-Bench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/peng-weihan/SWE-QA-Bench) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 5 earlier paper(s): see the [full list](automation/PAPERS.md#-comprehension--documentation).</sub>

#### 🧪 Testing & Verification

> Writing tests and finding bugs before release.

- **Sakura: An Approach for Generating Complex Tests from Natural Language Test Descriptions.**  
  _Tyler Stennett, Rangeet Pan, Bridget McGinn, Alessandro Orso, Saurabh Sinha._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.00530) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SWE-Mutation: Can LLMs Generate Reliable Test Suites in Software Engineering?**  
  _Yuxuan Sun, Yuze Zhao, Yufeng Wang, Yao Du, Zhiyuan Ma, Jinbo Wang, Mengdi Zhang, Kai Zhang, Zhenya Huang._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.22175) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements.**  
  _Xiwen Teoh, Yun Lin, Duc-Minh Nguyen, Ruofei Ren, Wenjie Zhang, Jin Song Dong._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.11724)

- **Position: Vibe Coding Needs Vibe Reasoning: Improving Vibe Coding with Formal Verification.**  
  _Jacqueline Mitchell, Yasser Shaaban._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.00202) ![Position Paper](https://img.shields.io/badge/Position_Paper-9B59B6?style=for-the-badge)

- **Benchmarking LLMs for Unit Test Generation from Real-World Functions.**  
  _Dong Huang, Jie M. Zhang, Mark Harman, Qianru Zhang, Mingzhe Du, See-Kiong Ng._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.00408) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Intention-Driven Generation of Project-Specific Test Cases.**  
  _Binhang Qi, Yun Lin, Xinyi Weng, Yuhuan Huang, Chenyan Liu, Hailong Sun, Zhi Jin, Jin Song Dong._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.20619)

<sub>… plus 2 earlier paper(s): see the [full list](automation/PAPERS.md#-testing--verification).</sub>

#### 🏗️ Feature Development

> Adding new features to an existing codebase.

- **U2F: Encouraging SWE-Agent to Seize Novelty without Losing Feasibility.**  
  _Wencheng Ye, Yan Liu._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.03517)

- **EvoDev: An Iterative Feature-Driven Framework for End-to-End Software Development with LLM-based Agents.**  
  _Junwei Liu, Chen Xu, Chong Wang, Tong Bai, Weitong Chen, Kaseng Wong, Yiling Lou, Xin Peng._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.02399)

- **CodeClash: Benchmarking Goal-Oriented Software Engineering.**  
  _John Yang, Kilian Lieret, Joyce Yang, Carlos E. Jimenez, Ofir Press, Ludwig Schmidt, Diyi Yang._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.00839) [![Website](https://img.shields.io/badge/CODECLASH.AI-blue?style=for-the-badge)](https://codeclash.ai/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Automatically Benchmarking LLM Code Agents through Agent-Driven Annotation and Evaluation.**  
  _Lingyue Fu, Bolun Zhang, Hao Guan, Yaoming Zhu, Lin Qiu, Weiwen Liu, Xuezhi Cao, Xunliang Cai, Weinan Zhang, Yong Yu._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.24358) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **NoCode-bench: A Benchmark for Evaluating Natural Language-Driven Feature Addition.**  
  _Le Deng, Zhonghao Jiang, Jialun Cao, Michael Pradel, Zhongxin Liu._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.18130) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Think Like an Engineer: A Neuro-Symbolic Collaboration Agent for Generative Software Requirements Elicitation and Self-Review.**  
  _Sai Zhang, Zhenchang Xing, Jieshan Chen, Dehai Zhao, Zizhong Zhu, Xiaowang Zhang, Zhiyong Feng, Xiaohong Li._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.14969)

<sub>… plus 3 earlier paper(s): see the [full list](automation/PAPERS.md#-feature-development).</sub>

### 🧊 3D & CAD

> Generating 3D models and CAD programs.

- **3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code.**  
  _Yipeng Gao, Lei Shu, Genzhi Ye, Xi Xiong, Ameesh Makadia, Meiqi Guo, Laurent Itti, Jindong Chen._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.01057) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects.**  
  _Puyi Wang, Yuhao Wang, Linjie Li, Zhengyuan Yang, Kevin Qinghong Lin, Yangguang Li, Yu Cheng._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.19587)

- **Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code Synthesis.**  
  _Yixuan Yang, Zhen Luo, Wanshui Gan, Jinkun Hao, Junru Lu, Jinghao Yan, Zhaoyang Lyu, Xudong Xu._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.18451) [![GitHub Stars](https://img.shields.io/github/stars/YxuanAr/Code-as-Room?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/YxuanAr/Code-as-Room) [![Website](https://img.shields.io/badge/CODE--AS--ROOM-blue?style=for-the-badge)](https://code-as-room.github.io/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Agentic Design of Compositional Machines.**  
  _Wenqian Zhang, Weiyang Liu, Zhen Liu._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.14980) [![GitHub Stars](https://img.shields.io/github/stars/Godheritage/BesiegeField?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/Godheritage/BesiegeField) [![Website](https://img.shields.io/badge/BESIEGEFIELD-blue?style=for-the-badge)](https://besiegefield.github.io/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **MetaGen: A DSL, Database, and Benchmark for VLM-Assisted Metamaterial Generation.**  
  _Liane Makatura, Benjamin Jones, Siyuan Bian, Wojciech Matusik._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.17568) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **MeshCoder: LLM-Powered Structured Mesh Code Generation from Point Clouds.**  
  _Bingquan Dai, Li Ray Luo, Qihong Tang, Jie Wang, Xinyu Lian, Hao Xu, Minghan Qin, Xudong Xu, Bo Dai, Haoqian Wang, et al._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.14879) [![GitHub Stars](https://img.shields.io/github/stars/InternRobotics/MeshCoder?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/InternRobotics/MeshCoder) [![Website](https://img.shields.io/badge/MESHCODER-blue?style=for-the-badge)](https://daibingquan.github.io/MeshCoder/) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **CADDesigner: Conceptual Design of CAD Models Based on General-Purpose Agent.**  
  _Jingzhe Ni, Xiaolong Yin, Xingyu Lu, Xintong Li, Ji Wei, Ruofeng Tong, Min Tang, Peng Du._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01031)

<sub>… plus 16 earlier paper(s): see the [full list](automation/PAPERS.md#-3d--cad).</sub>

### 🌐 Web Applications

> Building websites, front-ends, and back-end services.

- **I-WebGenBench : Evaluating Interactivity in LLM-Generated Scientific Web Applications.**  
  _Dasen Dai, Biao Wu, Meng Fang, Shuoqi Li, Wenhao Wang._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.00750) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models.**  
  _Xinping Lei, Xinyu Che, Junqi Xiong, Chenchen Zhang, Yukai Huang, Chenyu Zhou, Haoyang Huang, Minghao Liu, Letian Zhu, Hongyi Ye, et al._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.18224) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Figma2Code: Automating Multimodal Design to Code in the Wild.**  
  _Yi Gui, Jiawan Zhang, Yina Wang, Tianran Ma, Yao Wan, Shilin He, Dongping Chen, Zhou Zhao, Wenbin Jiang, Xuanhua Shi, et al._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.13648) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic Web Coding.**  
  _Yuhang Li, Chenchen Zhang, Ruilin Lv, Ao Liu, Ken Deng, Yuanxing Zhang, Jiaheng Liu, Wiggin Zhou, Bo Zhou._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.11498)

- **InteractScience: Programmatic and Visually-Grounded Evaluation of Interactive Scientific Demonstration Code Generation.**  
  _Qiaosheng Chen, Yang Liu, Lei Li, Kai Chen, Qipeng Guo, Gong Cheng, Fei Yuan._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.09724) [![GitHub Stars](https://img.shields.io/github/stars/open-compass/InteractScience?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/open-compass/InteractScience) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Automatically Generating Web Applications from Requirements Via Multi-Agent Test-Driven Development.**  
  _Yuxuan Wan, Tingshuo Liang, Jiakai Xu, Jingyu Xiao, Yintong Huo, Michael R. Lyu._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.25297) [![GitHub Stars](https://img.shields.io/github/stars/yxwan123/TDDev?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/yxwan123/TDDev)

- **WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning.**  
  _Zimu Lu, Houxing Ren, Yunqiao Yang, Ke Wang, Zhuofan Zong, Junting Pan, Mingjie Zhan, Hongsheng Li._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.22644) [![GitHub Stars](https://img.shields.io/github/stars/mnluzimu/WebGen-Agent?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/mnluzimu/WebGen-Agent)

- **EfficientUICoder: Efficient MLLM-based UI Code Generation via Input and Output Token Compression.**  
  _Jingyu Xiao, Zhongyi Zhang, Yuxuan Wan, Yintong Huo, Yang Liu, Michael R.Lyu._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.12159) [![GitHub Stars](https://img.shields.io/github/stars/WebPAI/EfficientUICoder?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/WebPAI/EfficientUICoder)

- **WebMMU: A Benchmark for Multimodal Multilingual Website Understanding and Code Generation.**  
  _Rabiul Awal, Mahsa Massoud, Aarash Feizi, Zichao Li, Suyuchen Wang, Christopher Pal, Aishwarya Agrawal, David Vazquez, Siva Reddy, Juan A. Rodriguez, et al._ EMNLP 2025.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.16763) [![Website](https://img.shields.io/badge/WEBMMU--PAPER-blue?style=for-the-badge)](https://webmmu-paper.github.io/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **LaTCoder: Converting Webpage Design to Code with Layout-as-Thought.**  
  _Yi Gui, Zhen Li, Zhongyi Zhang, Guohao Wang, Tianpeng Lv, Gaoyang Jiang, Yi Liu, Dongping Chen, Yao Wan, Hongyu Zhang, et al._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.03560) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **ScreenCoder: Advancing Visual-to-Code Generation for Front-End Automation via Modular Multimodal Agents.**  
  _Yilei Jiang, Yaozhi Zheng, Yuxuan Wan, Jiaming Han, Qunzhong Wang, Michael R. Lyu, Xiangyu Yue._ arXiv 2025/07.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.22827) [![GitHub Stars](https://img.shields.io/github/stars/leigest519/ScreenCoder?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/leigest519/ScreenCoder)

<sub>… plus 12 earlier paper(s): see the [full list](automation/PAPERS.md#-web-applications).</sub>

### 🗄️ Databases

> Generating SQL queries and database code.

- **BADGER: Bridging Agentic and Deterministic Evaluation for Generative Enterprise Reasoning.**  
  _Shannon Serrao, Soumitra Chatterjee, Dorina Strori, Abhishek Sharma, Nathan Miller._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.02109)

- **Learning to Retrieve: Dual-Level Long-Term Memory for Text-to-SQL Agents.**  
  _Yibo Wang, Nikki Lijing Kuang, Philip S. Yu, Zhewei Yao, Yuxiong He._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.00547)

- **Rethinking Agentic Workflows: Evaluating Inference-Based Test-Time Scaling Strategies in Text2SQL Tasks.**  
  _Jiajing Guo, Kenil Patel, Jorge Piazentin Ono, Wenbin He, Liu Ren._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.10885) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge)

- **AGENTIQL: An Agent-Inspired Multi-Expert Framework for Text-to-SQL Generation.**  
  _Omid Reza Heidari, Siobhan Reid, Yassine Yaakoubi._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.10661)

- **MTSQL-R1: Towards Long-Horizon Multi-Turn Text-to-SQL via Agentic Training.**  
  _Taicheng Guo, Hai Wang, ChaoChun Liu, Mohsen Golalikhani, Xin Chen, Xiangliang Zhang, Chandan K. Reddy._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.12831) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Agent Bain vs. Agent McKinsey: A New Text-to-SQL Benchmark for the Business Domain.**  
  _Yue Li, Ran Tao, Derek Hommel, Yusuf Denizay Dönder, Sungyong Chang, David Mimno, Unso Eun Seo Jo._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.07309) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 1 earlier paper(s): see the [full list](automation/PAPERS.md#-databases).</sub>

### 🎨 Graphics & Animation

> Generating vector graphics, animation, and chart code.

- **Towards Reliable Agentic Progressive Text-to-Visualization with Verification Rules.**  
  _Wenxin Xu, Chen Jason Zhang, Xiaoyong Wei, Haoyang Li, Hwanhee Kim, Yuanfeng Song, Raymond Chi-Wing Wong._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.29692) [![GitHub Stars](https://img.shields.io/github/stars/wxxv/PMVis?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/wxxv/PMVis) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **From Charts to Code: A Hierarchical Benchmark for Multimodal Models.**  
  _Jiahao Tang, Henry Hengyuan Zhao, Lijian Wu, Yifei Tao, Dongxing Mao, Yang Wan, Jingru Tan, Min Zeng, Min Li, Alex Jinpeng Wang._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.17932) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **OpusAnimation: Code-Based Dynamic Chart Generation.**  
  _Bozheng Li, Miao Yang, Zhenhan Chen, Jiawang Cao, Mushui Liu, Yi Lu, Yongliang Wu, Bin Zhang, Yangguang Ji, Licheng Tang, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.03341) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

<sub>… plus 4 earlier paper(s): see the [full list](automation/PAPERS.md#-graphics--animation).</sub>

### ⚙️ Systems

> Writing systems code: OS, kernels, compilers, networking.

- **PithTrain: A Compact and Agent-Native MoE Training System.**  
  _Ruihang Lai, Hao Kang, Haozhan Tang, Akaash R. Parthasarathy, Zichun Yu, Junru Shao, Todd C. Mowry, Chenyan Xiong, Tianqi Chen._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.31463) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **HTAM: Hierarchical Transition-Attended Memory for Operator Optimization.**  
  _Yining Zhang, Mingyang Yi, Chen Wang, Xuwen Xiang, Tianhe Jia, Zedong Dan, Chengqing Zong, Yue Wang._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.29734)

- **Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation.**  
  _Yee Hin Chong, Jiaming Wu, Youhui Zhang, Peng Qu._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.26720)

- **PerfDojo: Automated ML Library Generation for Heterogeneous Architectures.**  
  _Andrei Ivanov, Siyuan Shen, Gioele Gottardo, Marcin Chrapek, Afif Boudaoud, Timo Schneider, Luca Benini, Torsten Hoefler._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.03586)

- **Man-Made Heuristics Are Dead. Long Live Code Generators!**  
  _Rohit Dwivedula, Divyanshu Saxena, Aditya Akella, Swarat Chaudhuri, Daehyeok Kim._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.08803)

<sub>… plus 2 earlier paper(s): see the [full list](automation/PAPERS.md#-systems).</sub>

### 🎮 Games

> Generating game code and full game projects.

- **OpenGame: Open Agentic Coding for Games.**  
  _Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng, Jiaming Han, Tianshuo Peng, Kaixuan Fan, Manyuan Zhang, et al._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.18394) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **90% Faster, 100% Code-Free: MLLM-Driven Zero-Code 3D Game Development.**  
  _Runxin Yang, Yuxuan Wan, Shuqing Li, Michael R. Lyu._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.26161)

<sub>… plus 1 earlier paper(s): see the [full list](automation/PAPERS.md#-games).</sub>

### 🔌 Hardware

> Generating hardware description code like RTL and HDL.

- **Focus: Better Verilog Generation from Large Language Model via Focused Reasoning.**  
  _Zhuorui Zhao, Bing Li, Grace Li Zhang, Ulf Schlichtmann._ SOCC 2025.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.02285)

<sub>… plus 2 earlier paper(s): see the [full list](automation/PAPERS.md#-hardware).</sub>

## 🌍 Code as Agency: Acting in the Real World

> Agents that use code to act in the world.

### 🔬 Research & Discovery

> Running experiments and analysis to make discoveries.

- **Can We Predict Before Executing Machine Learning Agents?**  
  _Jingsheng Zheng, Jintian Zhang, Yujie Luo, Yuren Mao, Yunjun Gao, Lun Du, Huajun Chen, Ningyu Zhang._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.05930)

- **Deploy-Master: Automating the Deployment of 50,000+ Agent-Ready Scientific Tools in One Day.**  
  _Yi Wang, Zhenting Huang, Zhaohan Ding, Ruoxue Liao, Yuan Huang, Xinzijian Liu, Jiajun Xie, Siheng Chen, Linfeng Zhang._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.03513) [![Website](https://img.shields.io/badge/DEPLOY--MASTER-blue?style=for-the-badge)](https://www.bohrium.com/apps/deploy-master)

- **ArchPilot: A Proxy-Guided Multi-Agent Approach for Machine Learning Engineering.**  
  _Zhuowen Yuan, Tao Liu, Yang Yang, Yang Wang, Feng Qi, Kaushik Rangadurai, Bo Li, Shuang Yang._ arXiv 2025/11.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2511.03985)

- **DeepAnalyze: Agentic Large Language Models for Autonomous Data Science.**  
  _Shaolei Zhang, Ju Fan, Meihao Fan, Guoliang Li, Xiaoyong Du._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.16872) [![GitHub Stars](https://img.shields.io/github/stars/ruc-datalab/DeepAnalyze?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/ruc-datalab/DeepAnalyze) [![Website](https://img.shields.io/badge/RUC--DEEPANALYZE-blue?style=for-the-badge)](https://ruc-deepanalyze.github.io/) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Agentic generative AI for media content discovery at the national football league.**  
  _Henry Wang, Md Sirajus Salekin, Jake Lee, Ross Claytor, Shinan Zhang, Michael Chi._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.07297)

- **MLE-Smith: Scaling MLE Tasks with Automated Multi-Agent Pipeline.**  
  _Rushi Qiang, Yuchen Zhuang, Anikait Singh, Percy Liang, Chao Zhang, Sherry Yang, Bo Dai._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.07307) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **LLM-Based Data Science Agents: A Survey of Capabilities, Challenges, and Future Directions.**  
  _Mizanur Rahman, Amran Bhuiyan, Mohammed Saidul Islam, Md Tahmid Rahman Laskar, Ridwan Mahbub, Ahmed Masry, Shafiq Joty, Enamul Hoque._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.04023) ![Survey](https://img.shields.io/badge/Survey-2A9D8F?style=for-the-badge)

- **Reinforcement Learning for Machine Learning Engineering Agents.**  
  _Sherry Yang, Joy He-Yueya, Percy Liang._ arXiv 2025/09.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.01684) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **WebDS: An End-to-End Benchmark for Web-based Data Science.**  
  _Ethan Hsu, Hong Meng Yam, Ines Bouissou, Aaron Murali John, Raj Thota, Josh Koe, Vivek Sarath Putta, G K Dharesan, Alexander Spangher, Shikhar Murty, et al._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.01222) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 17 earlier paper(s): see the [full list](automation/PAPERS.md#-research--discovery).</sub>

### 🖥️ Terminals & Operating Systems

> Completing tasks in terminals and operating systems.

- **TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents.**  
  _Shoufa Chen, Luyuan Wang, Xuan Yang, Zhiheng Liu, Yuren Cong, Yuanfeng Ji, Feiyan Zhou, Xiaohui Zhang, Fanny Yang, Belinda Zeng._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.28480) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **What Makes Interaction Trajectories Effective for Training Terminal Agents?**  
  _Sidi Yang, Chaofan Tao, Jierun Chen, Tiezheng Yu, Ruoyu Wang, Yuxin Jiang, Yiming Du, Wendong Xu, Jing Xiong, Taiqiang Wu, et al._ arXiv 2026/06.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.03461) ![Empirical Study](https://img.shields.io/badge/Empirical_Study-4A90D9?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **LiteCoder-Terminal: Scaling Long-Horizon Terminal Environments for Learning Language Agents.**  
  _Xiaoxuan Peng, Kaiqi Zhang, Xinyu Lu, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.29559) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **ECHO: Terminal Agents Learn World Models for Free.**  
  _Vaishnavi Shrivastava, Piero Kauffmann, Ahmed Awadallah, Dimitris Papailiopoulos._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.24517)

- **TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks.**  
  _Zhaoyang Chu, Jiarui Hu, Xingyu Jiang, Pengyu Zou, Han Li, Chao Peng, Peter O'Hearn, Earl T. Barr, Mark Harman, Federica Sarro, et al._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.22535) [![GitHub Stars](https://img.shields.io/github/stars/EuniAI/TerminalWorld?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/EuniAI/TerminalWorld) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments.**  
  _Chiyu Zhang, Huiqin Yang, Bendong Jiang, Xiaolei Zhang, Yiran Zhao, Ruyi Chen, Lu Zhou, Xiaogang Xu, Jiafei Wu, Liming Fang, et al._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.10779) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Learning CLI Agents with Structured Action Credit under Selective Observation.**  
  _Haoyang Su, Ying Wen._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.08013)

- **MMTB: Evaluating Terminal Agents on Multimedia-File Tasks.**  
  _Chiyeong Heo, Jaechang Kim, Junhyuk Kwon, Hoyoung Kim, Dongmin Park, Jonghyun Lee, Jungseul Ok._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.10966) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Terminus-4B: Can a Smaller Model Replace Frontier LLMs at Agentic Execution Tasks?**  
  _Spandan Garg, Vikram Nitin, Yufan Huang._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.03195) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adversarial, Difficult, and Legible Evaluation Design.**  
  _Ivan Bercovich._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.28093) ![Position Paper](https://img.shields.io/badge/Position_Paper-9B59B6?style=for-the-badge)

- **Toward Scalable Terminal Task Synthesis via Skill Graphs.**  
  _Zhiyuan Fan, Tinghao Yu, Yuanjun Cai, Jiangtao Guan, Yun Yang, Dingxin Hu, Jiang Zhou, Xing Wu, Zhuo Han, Feng Zhang, et al._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.25727) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression.**  
  _Jincheng Ren, Siwei Wu, Yizhi Li, Kang Zhu, Shu Xu, Boyu Feng, Ruibin Yuan, Wei Zhang, Riza Batista-Navarro, Jian Yang, et al._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.19572) [![GitHub Stars](https://img.shields.io/github/stars/multimodal-art-projection/TACO?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/multimodal-art-projection/TACO)

- **Terminal Wrench: A Dataset of 331 Reward-Hackable Environments and 3,632 Exploit Trajectories.**  
  _Ivan Bercovich, Ivgeni Segal, Kexun Zhang, Shashwat Saxena, Aditi Raghunathan, Ziqian Zhong._ arXiv 2026/04.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.17596) [![GitHub Stars](https://img.shields.io/github/stars/few-sh/terminal-wrench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/few-sh/terminal-wrench) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Terminal Agents Suffice for Enterprise Automation.**  
  _Patrice Bechard, Orlando Marquez Ayala, Emily Chen, Jordan Skelton, Sagar Davasam, Srinivas Sunkara, Vikas Yadav, Sai Rajeswar._ arXiv 2026/03.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.00073) ![Position Paper](https://img.shields.io/badge/Position_Paper-9B59B6?style=for-the-badge)

- **On Data Engineering for Scaling LLM Terminal Capabilities.**  
  _Renjie Pi, Grace Lam, Mohammad Shoeybi, Pooya Jannaty, Bryan Catanzaro, Wei Ping._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.21193) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge) ![Model](https://img.shields.io/badge/Model-E76F51?style=for-the-badge)

- **TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for Terminal Agents.**  
  _Kaijie Zhu, Yuzhou Nie, Yijiang Li, Yiming Huang, Jialian Wu, Jiang Liu, Ximeng Sun, Zhenfei Yin, Lun Wang, Zicheng Liu, et al._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.07274) [![GitHub Stars](https://img.shields.io/github/stars/ucsb-mlsec/terminal-bench-env?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/ucsb-mlsec/terminal-bench-env) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments.**  
  _Siwei Wu, Yizhi Li, Yuyang Song, Wei Zhang, Yang Wang, Riza Batista-Navarro, Xian Yang, Mingjie Tang, Bryan Dai, Jian Yang, et al._ arXiv 2026/02.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.01244) [![GitHub Stars](https://img.shields.io/github/stars/Wusiwei0410/TerminalTraj?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/Wusiwei0410/TerminalTraj) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Endless Terminals: Scaling RL Environments for Terminal Agents.**  
  _Kanishk Gandhi, Shivam Garg, Noah D. Goodman, Dimitris Papailiopoulos._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.16443) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **Computer Environments Elicit General Agentic Intelligence in LLMs.**  
  _Daixuan Cheng, Shaohan Huang, Yuxian Gu, Huatong Song, Guoxin Chen, Li Dong, Wayne Xin Zhao, Ji-Rong Wen, Furu Wei._ arXiv 2026/01.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.16206)

- **Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces.**  
  _Mike A. Merrill, Alexander G. Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, Ivan Bercovich, Lin Shi, Jeong Yeon Shin, Thomas Walshe, E. Kelly Buchanan, et al._ 2026.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.11868) [![GitHub Stars](https://img.shields.io/github/stars/harbor-framework/terminal-bench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/harbor-framework/terminal-bench) [![Website](https://img.shields.io/badge/TBENCH.AI-blue?style=for-the-badge)](https://www.tbench.ai/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

- **Let It Flow: Agentic Crafting on Rock and Roll, Building the ROME Model within an Open Agentic Learning Ecosystem.**  
  _Weixun Wang, XiaoXiao Xu, Wanhe An, Fangwen Dai, Wei Gao, Yancheng He, Ju Huang, Qiang Ji, Hanqi Jin, Xiaoyang Li, et al._ arXiv 2025/12.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.24873)

- **Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents.**  
  _Yueqi Song, Ketan Ramaneti, Zaid Sheikh, Ziru Chen, Boyu Gou, Tianbao Xie, Yiheng Xu, Danyang Zhang, Apurva Gandhi, Fan Yang, et al._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.24702) [![GitHub Stars](https://img.shields.io/github/stars/neulab/agent-data-protocol?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/neulab/agent-data-protocol) [![Website](https://img.shields.io/badge/AGENTDATAPROTOCOL-blue?style=for-the-badge)](https://www.agentdataprotocol.com/) ![Training Data](https://img.shields.io/badge/Training_Data-8AB17D?style=for-the-badge)

- **GitTaskBench: A Benchmark for Code Agents Solving Real-World Tasks Through Code Repository Leveraging.**  
  _Ziyi Ni, Huacan Wang, Shuo Zhang, Shuo Lu, Ziyang He, Wang You, Zhenheng Tang, Yuntao Du, Bill Sun, Hongzhang Liu, et al._ arXiv 2025/08.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.18993) [![GitHub Stars](https://img.shields.io/github/stars/QuantaAlpha/GitTaskBench?style=for-the-badge&logo=github&label=GitHub&color=black)](https://github.com/QuantaAlpha/GitTaskBench) [![Website](https://img.shields.io/badge/GITTASKBENCH-blue?style=for-the-badge)](https://gittaskbench.github.io/) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 6 earlier paper(s): see the [full list](automation/PAPERS.md#-terminals--operating-systems).</sub>

### 🤖 The Physical World

> Controlling robots and physical systems with code.

<sub>… plus 9 earlier paper(s): see the [full list](automation/PAPERS.md#-the-physical-world).</sub>

### 🕹️ Game Worlds

> Playing games by writing and running code.

- **One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration.**  
  _Zaid Khan, Archiki Prasad, Elias Stengel-Eskin, Jaemin Cho, Mohit Bansal._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.12088) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 2 earlier paper(s): see the [full list](automation/PAPERS.md#-game-worlds).</sub>

### 🧭 Browsers & the Web

> Operating web browsers to get things done online.

<sub>… plus 3 earlier paper(s): see the [full list](automation/PAPERS.md#-browsers--the-web).</sub>

### 🧰 Software Applications

> Operating desktop, mobile, and professional software.

- **GenClaw: Code-Driven Agentic Image Generation.**  
  _Junyan Ye, Jun He, Zilong Huang, Dongzhi Jiang, Xuan Yang, Rui Chen, Weijia Li._ arXiv 2026/05.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.30248)

- **OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents.**  
  _Hongrui Jia, Jitong Liao, Xi Zhang, Haiyang Xu, Tianbao Xie, Chaoya Jiang, Ming Yan, Si Liu, Wei Ye, Fei Huang._ arXiv 2025/10.  
  [![Paper](https://img.shields.io/badge/Paper-A42C25?style=for-the-badge&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.24563) ![Benchmark](https://img.shields.io/badge/Benchmark-F4A261?style=for-the-badge)

<sub>… plus 1 earlier paper(s): see the [full list](automation/PAPERS.md#-software-applications).</sub>
<!-- PAPERS:END -->

## 🗺️ Research Landscape

We are a young team passionate about the future of code agents, and we look forward to discussing exciting ideas with the community.
This field sits at the intersection of software engineering, artificial intelligence (especially LLMs and agentic reasoning), and automated code development, experiencing extremely rapid evolution since 2023.

### 🌟 Vision
Advancing toward general-purpose agents capable of understanding, modifying, and creating complex codebases, collaborating with humans, and autonomously driving end-to-end software engineering processes—from requirements, to implementation, to testing, deployment, and maintenance.

### 🧩 Open Problems
- **Long-horizon planning:** Enabling agents to reason and act coherently over many steps in large, realistic codebases.
- **Robust evaluation:** Designing benchmarks and metrics that reflect real-world complexity, generalizability, and value beyond short snippets.
- **Interpretability & safety:** Ensuring agent actions are understandable, controllable, and safe for deployment on critical systems.
- **Collaboration:** Seamlessly integrating multiple agents and human-in-the-loop workflows.
- **Repository-level grounding:** Equipping agents with persistent context over evolving, multi-file software.
- **Resource efficiency:** Addressing compute/memory requirements for large-scale agentic work.

### Conferences and Workshops

- ICSE — International Conference on Software Engineering [SE]
- FSE (ESEC/FSE) — Foundations of Software Engineering [SE]
- ASE — Automated Software Engineering [SE]
- ISSTA — International Symposium on Software Testing and Analysis [SE/Testing]
- ICLR — International Conference on Learning Representations [ML]
- ICML — International Conference on Machine Learning [ML]
- NeurIPS — Conference on Neural Information Processing Systems [ML]
- ACL — Annual Meeting of the Association for Computational Linguistics [NLP]
- EMNLP — Empirical Methods in Natural Language Processing [NLP]
- NAACL — North American Chapter of the ACL [NLP]
- TheWebConf (WWW) — The Web Conference (formerly WWW) [Web]

### 🧪 Frontier Labs and Teams

- **OpenAI:** Work on MLE-bench, large-scale evaluations, and agent architecture.
- **Google DeepMind:** Pioneering code-centric models and embodied agent applications.
- **Microsoft Research:** Advances in multi-agent collaboration, feature-benchmarks, and tool-assisted agents.
- **THUDM (Tsinghua):** SWE-Dev, general SE agent architecture research.
- **Scale AI:** SWE-Bench, SWE-Bench Pro, real-world repo agent benchmarking.
- **Amazon AWS AI Lab:** SWE-PolyBench and multilingual repo agent research.
- **Meta AI Research:** Studies on agent robustness and failure analysis.
- **QuantaAlpha:** GitTaskBench and RepoMaster for sophisticated repo understanding.
- **Stanford Human-Centered AI:** Software agents for ML engineering, pipeline automation.

(See main list for additional innovative contributors. Please suggest more leading labs!)


## 🤝 Contributing

Contributing a paper takes one step: **drop its arXiv abstract link in the [paper inbox (issue #4)](https://github.com/EuniAI/awesome-code-agents/issues/4).**

That is all. A pipeline takes it from there: it fetches the metadata, classifies the paper into the right category, and queues it for a quick maintainer review before it appears in the list. No pull request, no template, no manual formatting. The list (categories, ordering, badges) is fully generated, so please do not edit the tables by hand: hand edits are overwritten on the next render.

You can drop several links in one comment, and anything on topic is welcome: a new paper, a technical report, or one we have missed. Suggestions for leading labs and venues are welcome too.

We're grateful to everyone who suggests papers and helps shape this collection.

Questions or problems? Open an [issue](https://github.com/EuniAI/awesome-code-agents/issues) and we will help.

---

## 🌟 Star History
[![Star History Chart](assets/star-history.svg)](https://www.star-history.com/#EuniAI/awesome-code-agents&Date)

---

## 🙏 Acknowledgements
- Thanks to all contributors and the research community.
- We would also like to thank the maintainers of many inspiring awesome agent repositories, including:
  - [awesome-llm-based-agent4code](https://github.com/JiaruQian/awesome-llm-based-agent4code)  [![Stars](https://img.shields.io/github/stars/JiaruQian/awesome-llm-based-agent4code?label=stars)](https://github.com/JiaruQian/awesome-llm-based-agent4code/stargazers)  <a href="https://img.shields.io/github/last-commit/JiaruQian/awesome-llm-based-agent4code?color=green"><img src="https://img.shields.io/github/last-commit/JiaruQian/awesome-llm-based-agent4code?color=green" alt="Last Commit"></a>
  - [awesome-engineering-agents](https://github.com/usejina/awesome-engineering-agents)  [![Stars](https://img.shields.io/github/stars/usejina/awesome-engineering-agents?label=stars)](https://github.com/usejina/awesome-engineering-agents/stargazers)  <a href="https://img.shields.io/github/last-commit/usejina/awesome-engineering-agents?color=green"><img src="https://img.shields.io/github/last-commit/usejina/awesome-engineering-agents?color=green" alt="Last Commit"></a>
  - [awesome-vibe-coding](https://github.com/ai-for-developers/awesome-vibe-coding)  [![Stars](https://img.shields.io/github/stars/ai-for-developers/awesome-vibe-coding?label=stars)](https://github.com/ai-for-developers/awesome-vibe-coding/stargazers)  <a href="https://img.shields.io/github/last-commit/ai-for-developers/awesome-vibe-coding?color=green"><img src="https://img.shields.io/github/last-commit/ai-for-developers/awesome-vibe-coding?color=green" alt="Last Commit"></a>
  - [awesome-ai-coding-tools](https://github.com/ai-for-developers/awesome-ai-coding-tools)  [![Stars](https://img.shields.io/github/stars/ai-for-developers/awesome-ai-coding-tools?label=stars)](https://github.com/ai-for-developers/awesome-ai-coding-tools/stargazers)  <a href="https://img.shields.io/github/last-commit/ai-for-developers/awesome-ai-coding-tools?color=green"><img src="https://img.shields.io/github/last-commit/ai-for-developers/awesome-ai-coding-tools?color=green" alt="Last Commit"></a>
  - [awesome-code-agents](https://github.com/sorrycc/awesome-code-agents)  [![Stars](https://img.shields.io/github/stars/sorrycc/awesome-code-agents?label=stars)](https://github.com/sorrycc/awesome-code-agents/stargazers)  <a href="https://img.shields.io/github/last-commit/sorrycc/awesome-code-agents?color=green"><img src="https://img.shields.io/github/last-commit/sorrycc/awesome-code-agents?color=green" alt="Last Commit"></a>
  - [awesome-ai-software-development-agents](https://github.com/flatlogic/awesome-ai-software-development-agents)  [![Stars](https://img.shields.io/github/stars/flatlogic/awesome-ai-software-development-agents?label=stars)](https://github.com/flatlogic/awesome-ai-software-development-agents/stargazers)  <a href="https://img.shields.io/github/last-commit/flatlogic/awesome-ai-software-development-agents?color=green"><img src="https://img.shields.io/github/last-commit/flatlogic/awesome-ai-software-development-agents?color=green" alt="Last Commit"></a>
  - [Awesome-Repo-Level-Code-Generation](https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation)  [![Stars](https://img.shields.io/github/stars/YerbaPage/Awesome-Repo-Level-Code-Generation?label=stars)](https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation/stargazers)  <a href="https://img.shields.io/github/last-commit/YerbaPage/Awesome-Repo-Level-Code-Generation?color=green"><img src="https://img.shields.io/github/last-commit/YerbaPage/Awesome-Repo-Level-Code-Generation?color=green" alt="Last Commit"></a>
  - [awesome-devins](https://github.com/e2b-dev/awesome-devins)  [![Stars](https://img.shields.io/github/stars/e2b-dev/awesome-devins?label=stars)](https://github.com/e2b-dev/awesome-devins/stargazers)  <a href="https://img.shields.io/github/last-commit/e2b-dev/awesome-devins?color=green"><img src="https://img.shields.io/github/last-commit/e2b-dev/awesome-devins?color=green" alt="Last Commit"></a>
  - [awesome-AI-driven-development](https://github.com/eltociear/awesome-AI-driven-development)  [![Stars](https://img.shields.io/github/stars/eltociear/awesome-AI-driven-development?label=stars)](https://github.com/eltociear/awesome-AI-driven-development/stargazers)  <a href="https://img.shields.io/github/last-commit/eltociear/awesome-AI-driven-development?color=green"><img src="https://img.shields.io/github/last-commit/eltociear/awesome-AI-driven-development?color=green" alt="Last Commit"></a>
  - [Awesome-Vibe-Coding](https://github.com/YuyaoGe/Awesome-Vibe-Coding)  [![Stars](https://img.shields.io/github/stars/YuyaoGe/Awesome-Vibe-Coding?label=stars)](https://github.com/YuyaoGe/Awesome-Vibe-Coding/stargazers)  <a href="https://img.shields.io/github/last-commit/YuyaoGe/Awesome-Vibe-Coding?color=green"><img src="https://img.shields.io/github/last-commit/YuyaoGe/Awesome-Vibe-Coding?color=green" alt="Last Commit"></a>
  - [Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM)  [![Stars](https://img.shields.io/github/stars/codefuse-ai/Awesome-Code-LLM?label=stars)](https://github.com/codefuse-ai/Awesome-Code-LLM/stargazers)  <a href="https://img.shields.io/github/last-commit/codefuse-ai/Awesome-Code-LLM?color=green"><img src="https://img.shields.io/github/last-commit/codefuse-ai/Awesome-Code-LLM?color=green" alt="Last Commit"></a>
  - [CodeLLMSurvey](https://github.com/juyongjiang/CodeLLMSurvey)  [![Stars](https://img.shields.io/github/stars/juyongjiang/CodeLLMSurvey?label=stars)](https://github.com/juyongjiang/CodeLLMSurvey/stargazers)  <a href="https://img.shields.io/github/last-commit/juyongjiang/CodeLLMSurvey?color=green"><img src="https://img.shields.io/github/last-commit/juyongjiang/CodeLLMSurvey?color=green" alt="Last Commit"></a>
  - [Awesome-Multimodal-LLM-for-Code](https://github.com/xjywhu/Awesome-Multimodal-LLM-for-Code)  [![Stars](https://img.shields.io/github/stars/xjywhu/Awesome-Multimodal-LLM-for-Code?label=stars)](https://github.com/xjywhu/Awesome-Multimodal-LLM-for-Code/stargazers)  <a href="https://img.shields.io/github/last-commit/xjywhu/Awesome-Multimodal-LLM-for-Code?color=green"><img src="https://img.shields.io/github/last-commit/xjywhu/Awesome-Multimodal-LLM-for-Code?color=green" alt="Last Commit"></a>
  - [awesome-copilot](https://github.com/github/awesome-copilot)  [![Stars](https://img.shields.io/github/stars/github/awesome-copilot?label=stars)](https://github.com/github/awesome-copilot/stargazers)  <a href="https://img.shields.io/github/last-commit/github/awesome-copilot?color=green"><img src="https://img.shields.io/github/last-commit/github/awesome-copilot?color=green" alt="Last Commit"></a>
  - [awesome-web-agents](https://github.com/steel-dev/awesome-web-agents)  [![Stars](https://img.shields.io/github/stars/steel-dev/awesome-web-agents?label=stars)](https://github.com/steel-dev/awesome-web-agents/stargazers)  <a href="https://img.shields.io/github/last-commit/steel-dev/awesome-web-agents?color=green"><img src="https://img.shields.io/github/last-commit/steel-dev/awesome-web-agents?color=green" alt="Last Commit"></a>
  - [GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List)  [![Stars](https://img.shields.io/github/stars/OSU-NLP-Group/GUI-Agents-Paper-List?label=stars)](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List/stargazers)  <a href="https://img.shields.io/github/last-commit/OSU-NLP-Group/GUI-Agents-Paper-List?color=green"><img src="https://img.shields.io/github/last-commit/OSU-NLP-Group/GUI-Agents-Paper-List?color=green" alt="Last Commit"></a>
  - [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers)  [![Stars](https://img.shields.io/github/stars/luo-junyu/Awesome-Agent-Papers?label=stars)](https://github.com/luo-junyu/Awesome-Agent-Papers/stargazers)  <a href="https://img.shields.io/github/last-commit/luo-junyu/Awesome-Agent-Papers?color=green"><img src="https://img.shields.io/github/last-commit/luo-junyu/Awesome-Agent-Papers?color=green" alt="Last Commit"></a>
  - [LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers)  [![Stars](https://img.shields.io/github/stars/zjunlp/LLMAgentPapers?label=stars)](https://github.com/zjunlp/LLMAgentPapers/stargazers)  <a href="https://img.shields.io/github/last-commit/zjunlp/LLMAgentPapers?color=green"><img src="https://img.shields.io/github/last-commit/zjunlp/LLMAgentPapers?color=green" alt="Last Commit"></a>
  - [LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers)  [![Stars](https://img.shields.io/github/stars/AGI-Edgerunners/LLM-Agents-Papers?label=stars)](https://github.com/AGI-Edgerunners/LLM-Agents-Papers/stargazers)  <a href="https://img.shields.io/github/last-commit/AGI-Edgerunners/LLM-Agents-Papers?color=green"><img src="https://img.shields.io/github/last-commit/AGI-Edgerunners/LLM-Agents-Papers?color=green" alt="Last Commit"></a>
  - [Self-Evolving-Agents](https://github.com/CharlesQ9/Self-Evolving-Agents)  [![Stars](https://img.shields.io/github/stars/CharlesQ9/Self-Evolving-Agents?label=stars)](https://github.com/CharlesQ9/Self-Evolving-Agents/stargazers)  <a href="https://img.shields.io/github/last-commit/CharlesQ9/Self-Evolving-Agents?color=green"><img src="https://img.shields.io/github/last-commit/CharlesQ9/Self-Evolving-Agents?color=green" alt="Last Commit"></a>
  - [Awesome-Self-Evolving-Agents](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents)  [![Stars](https://img.shields.io/github/stars/EvoAgentX/Awesome-Self-Evolving-Agents?label=stars)](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents/stargazers)  <a href="https://img.shields.io/github/last-commit/EvoAgentX/Awesome-Self-Evolving-Agents?color=green"><img src="https://img.shields.io/github/last-commit/EvoAgentX/Awesome-Self-Evolving-Agents?color=green" alt="Last Commit"></a>
  - [OS-Agent-Survey](https://github.com/OS-Agent-Survey/OS-Agent-Survey)  [![Stars](https://img.shields.io/github/stars/OS-Agent-Survey/OS-Agent-Survey?label=stars)](https://github.com/OS-Agent-Survey/OS-Agent-Survey/stargazers)  <a href="https://img.shields.io/github/last-commit/OS-Agent-Survey/OS-Agent-Survey?color=green"><img src="https://img.shields.io/github/last-commit/OS-Agent-Survey/OS-Agent-Survey?color=green" alt="Last Commit"></a>
  - [Awesome-AI4Research](https://github.com/LightChen233/Awesome-AI4Research)  [![Stars](https://img.shields.io/github/stars/LightChen233/Awesome-AI4Research?label=stars)](https://github.com/LightChen233/Awesome-AI4Research/stargazers)  <a href="https://img.shields.io/github/last-commit/LightChen233/Awesome-AI4Research?color=green"><img src="https://img.shields.io/github/last-commit/LightChen233/Awesome-AI4Research?color=green" alt="Last Commit"></a>
  - [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)  [![Stars](https://img.shields.io/github/stars/Hannibal046/Awesome-LLM?label=stars)](https://github.com/Hannibal046/Awesome-LLM/stargazers)  <a href="https://img.shields.io/github/last-commit/Hannibal046/Awesome-LLM?color=green"><img src="https://img.shields.io/github/last-commit/Hannibal046/Awesome-LLM?color=green" alt="Last Commit"></a>
  - [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey)  [![Stars](https://img.shields.io/github/stars/RUCAIBox/LLMSurvey?label=stars)](https://github.com/RUCAIBox/LLMSurvey/stargazers)  <a href="https://img.shields.io/github/last-commit/RUCAIBox/LLMSurvey?color=green"><img src="https://img.shields.io/github/last-commit/RUCAIBox/LLMSurvey?color=green" alt="Last Commit"></a>
  - [open-llms](https://github.com/eugeneyan/open-llms)  [![Stars](https://img.shields.io/github/stars/eugeneyan/open-llms?label=stars)](https://github.com/eugeneyan/open-llms/stargazers)  <a href="https://img.shields.io/github/last-commit/eugeneyan/open-llms?color=green"><img src="https://img.shields.io/github/last-commit/eugeneyan/open-llms?color=green" alt="Last Commit"></a>
  - [LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide)  [![Stars](https://img.shields.io/github/stars/Mooler0410/LLMsPracticalGuide?label=stars)](https://github.com/Mooler0410/LLMsPracticalGuide/stargazers)  <a href="https://img.shields.io/github/last-commit/Mooler0410/LLMsPracticalGuide?color=green"><img src="https://img.shields.io/github/last-commit/Mooler0410/LLMsPracticalGuide?color=green" alt="Last Commit"></a>
  - [Awesome-LLM-Reasoning-with-NeSy](https://github.com/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy)  [![Stars](https://img.shields.io/github/stars/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy?label=stars)](https://github.com/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy/stargazers)  <a href="https://img.shields.io/github/last-commit/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy?color=green"><img src="https://img.shields.io/github/last-commit/LAMDASZ-ML/Awesome-LLM-Reasoning-with-NeSy?color=green" alt="Last Commit"></a>
  - [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps)  [![Stars](https://img.shields.io/github/stars/tensorchord/Awesome-LLMOps?label=stars)](https://github.com/tensorchord/Awesome-LLMOps/stargazers)  <a href="https://img.shields.io/github/last-commit/tensorchord/Awesome-LLMOps?color=green"><img src="https://img.shields.io/github/last-commit/tensorchord/Awesome-LLMOps?color=green" alt="Last Commit"></a>
  - [Awesome-VLA-Papers](https://github.com/Psi-Robot/Awesome-VLA-Papers)  [![Stars](https://img.shields.io/github/stars/Psi-Robot/Awesome-VLA-Papers?label=stars)](https://github.com/Psi-Robot/Awesome-VLA-Papers/stargazers)  <a href="https://img.shields.io/github/last-commit/Psi-Robot/Awesome-VLA-Papers?color=green"><img src="https://img.shields.io/github/last-commit/Psi-Robot/Awesome-VLA-Papers?color=green" alt="Last Commit"></a>
  - [Awesome-Neural-CAD](https://github.com/BunnySoCrazy/Awesome-Neural-CAD)  [![Stars](https://img.shields.io/github/stars/BunnySoCrazy/Awesome-Neural-CAD?label=stars)](https://github.com/BunnySoCrazy/Awesome-Neural-CAD/stargazers)  <a href="https://img.shields.io/github/last-commit/BunnySoCrazy/Awesome-Neural-CAD?color=green"><img src="https://img.shields.io/github/last-commit/BunnySoCrazy/Awesome-Neural-CAD?color=green" alt="Last Commit"></a>
  - [Awesome-3D-Generation](https://github.com/BunnySoCrazy/Awesome-3D-Generation)  [![Stars](https://img.shields.io/github/stars/BunnySoCrazy/Awesome-3D-Generation?label=stars)](https://github.com/BunnySoCrazy/Awesome-3D-Generation/stargazers)  <a href="https://img.shields.io/github/last-commit/BunnySoCrazy/Awesome-3D-Generation?color=green"><img src="https://img.shields.io/github/last-commit/BunnySoCrazy/Awesome-3D-Generation?color=green" alt="Last Commit"></a>
  - [Awesome-AIGC-3D](https://github.com/hitcslj/Awesome-AIGC-3D)  [![Stars](https://img.shields.io/github/stars/hitcslj/Awesome-AIGC-3D?label=stars)](https://github.com/hitcslj/Awesome-AIGC-3D/stargazers)  <a href="https://img.shields.io/github/last-commit/hitcslj/Awesome-AIGC-3D?color=green"><img src="https://img.shields.io/github/last-commit/hitcslj/Awesome-AIGC-3D?color=green" alt="Last Commit"></a>
  - [Awesome-Indoor-Scene-Synthesis](https://github.com/YandanYang/Awesome-Indoor-Scene-Synthesis)  [![Stars](https://img.shields.io/github/stars/YandanYang/Awesome-Indoor-Scene-Synthesis?label=stars)](https://github.com/YandanYang/Awesome-Indoor-Scene-Synthesis/stargazers)  <a href="https://img.shields.io/github/last-commit/YandanYang/Awesome-Indoor-Scene-Synthesis?color=green"><img src="https://img.shields.io/github/last-commit/YandanYang/Awesome-Indoor-Scene-Synthesis?color=green" alt="Last Commit"></a>
  - [Awesome-World-Model](https://github.com/LMD0311/Awesome-World-Model)  [![Stars](https://img.shields.io/github/stars/LMD0311/Awesome-World-Model?label=stars)](https://github.com/LMD0311/Awesome-World-Model/stargazers)  <a href="https://img.shields.io/github/last-commit/LMD0311/Awesome-World-Model?color=green"><img src="https://img.shields.io/github/last-commit/LMD0311/Awesome-World-Model?color=green" alt="Last Commit"></a>
  - [Awesome-World-Models](https://github.com/leofan90/Awesome-World-Models)  [![Stars](https://img.shields.io/github/stars/leofan90/Awesome-World-Models?label=stars)](https://github.com/leofan90/Awesome-World-Models/stargazers)  <a href="https://img.shields.io/github/last-commit/leofan90/Awesome-World-Models?color=green"><img src="https://img.shields.io/github/last-commit/leofan90/Awesome-World-Models?color=green" alt="Last Commit"></a>
  - [Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models)  [![Stars](https://img.shields.io/github/stars/knightnemo/Awesome-World-Models?label=stars)](https://github.com/knightnemo/Awesome-World-Models/stargazers)  <a href="https://img.shields.io/github/last-commit/knightnemo/Awesome-World-Models?color=green"><img src="https://img.shields.io/github/last-commit/knightnemo/Awesome-World-Models?color=green" alt="Last Commit"></a>
  - [AwesomeWorldModels](https://github.com/Li-Zn-H/AwesomeWorldModels)  [![Stars](https://img.shields.io/github/stars/Li-Zn-H/AwesomeWorldModels?label=stars)](https://github.com/Li-Zn-H/AwesomeWorldModels/stargazers)  <a href="https://img.shields.io/github/last-commit/Li-Zn-H/AwesomeWorldModels?color=green"><img src="https://img.shields.io/github/last-commit/Li-Zn-H/AwesomeWorldModels?color=green" alt="Last Commit"></a>
  - [Awesome-World-Models](https://github.com/PatrickHua/Awesome-World-Models)  [![Stars](https://img.shields.io/github/stars/PatrickHua/Awesome-World-Models?label=stars)](https://github.com/PatrickHua/Awesome-World-Models/stargazers)  <a href="https://img.shields.io/github/last-commit/PatrickHua/Awesome-World-Models?color=green"><img src="https://img.shields.io/github/last-commit/PatrickHua/Awesome-World-Models?color=green" alt="Last Commit"></a>
