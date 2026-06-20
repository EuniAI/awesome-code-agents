
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
