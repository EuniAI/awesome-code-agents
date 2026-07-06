
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
- 正交轴全部降级为 **tags**：贡献类型（benchmark / model / training-data / survey /
  empirical / position）、机制（planning / memory / feedback / multi-agent）、模态
  （multimodal）。foundation_models、data_synthesis、multimodal_coding 作为类别溶解。
- products 移出论文分类体系，README 独立版块。
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
