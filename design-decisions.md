
## 2026-07-10：确立 list 的 vision 与 L1 命名（Code as Everything）

### Vision（list 的 thesis，置于 README 顶部）
> **Code as Everything** — 从 agent 构建的数字世界，到它行动其中的真实世界。

论点：随着 agent 迅猛发展并触及现实，代码正成为世界运行的核心要素，不再局限于 digital
world。关键洞见（owner 提出）：**数字世界是真实世界的一部分**——在终端/浏览器/游戏里
行动同样是真实世界的活动、同样产生真实后果。这统一了 Agency 分支从浏览器到机器人的全部
成员，也让 "Code as Everything" 从"代码无处不在"升级为"代码是一切智能行动的基底"。

### L1 命名（display title 与内部 key 分离）
- 内部机器 key（config / data 文件名 / 分类 prompt 用）：`artifact` / `agency`
  ——保持短、稳定、ASCII。
- README 展示标题：
  - **Code as Artifact: Building the Digital World**（= 原 product 分支；agent 把想法
    建造成数字造物：软件、芯片设计、3D 模型；评价落在工件质量）
  - **Code as Agency: Acting on the Real World**（= 原 means 分支；agent 用代码行动于
    真实世界，该世界横跨数字与物理；评价落在世界状态改变）
  - ⚖️ 微调待定：副标题 "Acting **on** the Real World" vs "Acting **in** the Real World"
    （in 更贴"置身环境中操作"，on 更有力度）。暂用 on。

### 被否决的前案
- 曾担心 "Real World" 副标题对 Agency 分支（含 browser/terminal/game 等数字环境）过度
  声称，建议改为 "Acting Through Code"。**否决**：owner 的"数字世界属于真实世界"框架
  更有力，且不违反单轴——L1 真轴始终是 artifact(建造工件) vs agency(行动于世界)，
  digital/real 只是副标题的诗意修辞，不承担分类判定。

## 2026-07-06：新分类体系的设计约束——每一层必须单轴、同层概念平级

### 背景
诊断确认旧 36 类误分类的根因是**分类轴混用**（生命周期任务轴、交互界面轴、产出物领域轴、资源/元层面轴混在同一平面），类别不互斥，LLM 分类没有唯一正确答案。参考了
[Awesome-Code-as-Agent-Harness-Papers](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers)
及其 survey《Code as Agent Harness》(arXiv:2605.18747)。

### 锁定的约束
- **每一层分类只允许使用一条划分轴，同层类别必须概念平级、互斥。**
- 曾提出的混轴顶层方案（Foundations / Environments / SE Agents / Code-as-Action /
  Creative / Products 六大组）被**否决**，原因：六个组来自五条不同的轴，把旧病复制到顶层。

### 候选方案（骨架已认可方向，细节待定）
- L1 轴 = 代码在任务中的角色：**Code as Product**（成功度量在代码工件质量）vs
  **Code as Means**（成功度量在外部世界状态改变）
- L2 轴（Product 支）= 代码工件所属领域：通用软件 / Web / 数据库 / 系统软件 / 硬件 /
  游戏 / 图形动画 / 3D-CAD
- L2 轴（Means 支）= agent 所作用的世界：终端-OS / 浏览器 / 游戏世界 / 物理世界 /
  数据 / ML 实验 / 科学发现
- L3 轴（仅通用软件展开）= 软件生命周期活动
- 正交轴降级为 **tags**，且 tag 是**稀疏标注、非必填**（2026-07-06 定稿）：适用才打，
  都不适用则无 tag（无 tag = 普通方法论文，不设 method 默认值——与 README 现行徽章
  渲染逻辑一致）。两个 facet，各自内部平级：
  - **论文类型**（适用才打，互斥）：survey / empirical / position
  - **发布工件**（适用才打，可多选）：benchmark / model / training-data
    ——常共存（训练类工作常一次放出模型+数据+基准），故与论文类型分开、不强行单选。
    曾考虑加 `agent` 工件 tag，**否决**（2026-07-10）：本列表论文绝大多数都提出 agent，
    近乎全集、无信息量；"是否放出可运行系统"由 links.github 字段已隐含承载。
  foundation_models → artifact=model、data_synthesis → artifact=training-data、
  multimodal_coding 直接溶解进领域类别。曾考虑的机制 tags（planning/memory/feedback/
  multi-agent）和模态 tag（multimodal）被**否决**：机制天然多标签、边界模糊，会把
  "无唯一答案"问题从类别层搬到 tag 层；贡献维度是唯一近乎客观、LLM 可稳定判定的轴，
  且可驱动 README 渲染（如 Foundation Models 节由 artifact=model 过滤生成）。
- products **已删除**（2026-07-06）：`data/papers_products.yaml`（44 条产品）连同 README
  中已注释的 Products & Tools 版块一并移除。仓库定位收窄为**前沿研究论文与技术报告**，
  不再收录工业产品条目（历史数据 git 可回溯）。删除后论文计数由 515 修正为 471。
- terminal 在新体系中的席位：Means 支下的"终端/OS 世界"，与 browser、embodied 平级。

### 待解决
- security_engineering / fuzzing 在生命周期轴上的平行性（活动 vs tag）
- agentic_visualization、MLE 的 product/means 判定（倾向按"评价标准落在哪"判 means，
  规则需写死进分类 prompt）
- B 支类别未来膨胀后的 L3 拆分轴未定

## 2026-06-20：分类系统严重误分类问题，计划重新设计

### 问题描述
当前 LLM 分类器存在显著误分类问题，以 `terminal` 类别为例：
- 17篇被分到 terminal 类的待 review 论文中，多篇明显不属于该类
  （如 EvoTest、Oversight Has a Capacity、EvoArena、Multi-Agent Computer Use）
- 1篇明确是 terminal 相关的论文被错误分到 `data_synthesis`
- inbox 中手动提交的 10篇 terminal 论文长期未能正确入库
- 363篇论文因 LLM 调用失败积压在 retry 队列，越跑越慢

### 决策
暂停 cron，不再用现有系统继续积累问题，等待系统重新设计后再恢复。

### 计划重新设计的方向（待讨论）
- 分类准确性问题：prompt 设计、类别定义、few-shot 示例
- LLM 失败率过高：需要更稳定的调用机制
- retry 队列膨胀：需要更合理的失败处理策略
- 整体架构是否需要调整
