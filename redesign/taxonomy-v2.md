# 分类体系 v2 重构规格(草案,对齐中)

> 状态:**DRAFT** — 骨架已与 owner 达成一致,标注 ⚖️ 的条目待 owner 拍板。
> 决策沿革见 [design-decisions.md](../design-decisions.md)。

## Vision(list 的 thesis,置于 README 顶部)

> **Code as Everything** — 从 agent 构建的数字世界,到它行动其中的真实世界。

随着 agent 触及现实,代码正成为世界运行的核心要素,不再局限于 digital world。
数字世界是真实世界的一部分——在终端/浏览器/游戏里行动同样是真实世界的活动。

## 0. 设计原则(已锁定)

1. **每一层只用一条划分轴,同层类别概念平级、互斥**(单轴原则)。
2. 仓库定位:**前沿研究论文与技术报告**,不收工业产品条目。
3. 收录边界:agent 以写/执行代码为行动手段的一切好论文,不限领域(含 CAD、机器人等)。
4. tag 是稀疏标注、非必填;正交维度一律进 tag,不占类别席位。

## 1. 分类树(23 个叶子类别,原 36 个)

每层的划分轴显式声明;**叶子 = 分类器目标 = 数据文件**。

内部机器 key 用短名 `artifact` / `agency`;README 展示用大标题。

```
L1 轴:代码在任务中的角色(评价标准落在哪)
│
├── 🧱 artifact — Code as Artifact: Building the Digital World(按代码工件质量评价)
│   L2 轴:代码工件所属领域
│   ├── software — 通用软件
│   │   L3 轴:软件生命周期活动
│   │   ├── software_feature_development   ← feature_development (5)
│   │   ├── software_code_authoring        ← code_generation (62) + code_completion (4)
│   │   ├── software_testing               ← agentic_fuzzing (4) + issue_reproduction (17)
│   │   ├── software_debugging             ← issue_localization (12) + issue_resolution (134)
│   │   ├── software_code_review           ← pull_request_review (11)
│   │   ├── software_code_comprehension    ← qa (4)
│   │   ├── software_maintenance           ← refactoring (1) + migration (7) + perf_opt (3)
│   │   ├── software_security ⚖️           ← software_security_engineering (9)
│   │   └── software_infrastructure        ← environment_building (17) + git_management (1)
│   ├── web_generation                     ← website_generation (18) + backend_generation (1)
│   ├── database_engineering               ← sql_engineering (10)
│   ├── systems_software                   ← system_engineering (3)
│   ├── hardware_engineering               ← hardware_engineering (1)
│   ├── game_generation                    ← game_generation (3)
│   ├── graphics_animation                 ← svg_generation (1) + animation_generation (4)
│   │                                         + agentic_visualization (5) ⚖️
│   └── cad_3d                             ← 3d_object_design (25)
│
└── 🌍 agency — Code as Agency: Acting on the Real World(按外部世界状态改变评价)
    L2 轴:agent 所作用的世界(横跨数字与物理)
    ├── world_terminal                     ← terminal (18,需按新定义清洗)
    ├── world_browser                      ← code_executing_web (10)
    ├── world_game                         ← code_executing_game (5)
    ├── world_physical                     ← code_executing_embodied (23)
    ├── world_data                         ← automated_data_science (5)
    ├── world_ml_experiments               ← machine_learning_engineering (22)
    └── world_science                      ← scientific_workflows (2)
```

**溶解为 tag、逐篇重新归类的旧类别**(约 24 篇人工过一遍):

- `foundation_models` (4) → 按领域归入叶子类别 + tag `model`
- `data_synthesis` (13) → 归入其目标领域 + tag `training-data`
- `multimodal_coding` (7) → 逐篇按领域归类(screenshot-to-code → `web_generation`)

**已删除**:`products` (44,2026-07-10 删除,git 可回溯)。

### 关键判定规则(写入分类 prompt)

- **product vs means**:看论文的成功度量落在哪——代码工件本身的质量/正确性 → product;
  外部世界的状态/任务完成度 → means。
- **game_generation vs world_game**:产出游戏代码 → 前者;用代码玩游戏 → 后者。
- **world_terminal 收录标准**:贡献点在于终端/OS 作为 agent 的环境或世界
  (terminal benchmark、terminal-specific 方法);只是恰好在终端里跑的 SWE 论文
  归其任务类别。

## 2. Tag 体系(已锁定)

稀疏标注,适用才打,都不适用 = 无 tag(普通方法论文):

| Facet | 值 | 规则 |
|---|---|---|
| 论文类型 | `survey` / `empirical` / `position` | 互斥,单选 |
| 发布工件 | `benchmark` / `model` / `training-data` | 可多选,常共存 |

YAML 中沿用现有 `tags:` 列表字段(渲染为徽章的机制已存在,无 schema 变更)。

## 3. 仓库文件架构变更

### config.yaml

- 平铺 `categories:` → 嵌套 `taxonomy:`,每个节点含 `title`(README 节标题)、
  `axis`(该层划分轴说明)、`definition`(喂给分类器的判定文案)、`children`。
- 叶子节点的 key 即数据文件名后缀(`data/papers_{key}.yaml`)。
- `tags:` 段改为两个 facet 的定义。

### data/

- 36 个文件 → 23 个文件;合并/改名用脚本一次完成,溶解类别的约 24 篇人工归档。
- 条目 schema 不变(title/authors/venue/summary/tags/links)。

### README.md

- 结构由 `taxonomy:` 树驱动生成:L1 两大章 → L2 领域/世界节 → L3 生命周期小节
  (仅 software 展开)。
- Quick Navigation 同步由树生成。
- ⚖️ 现有独立的 "🌍 Foundation Models" 节取消,相关论文归入领域类别、以 `model`
  徽章标识(候补方案:保留一个由 tag 过滤自动生成的汇总节)。

### scripts/

- `render_papers.py`:从遍历平铺类别改为遍历 taxonomy 树(节标题、层级、顺序均取自树)。
- `update_papers_badge.py`:无实质变更(继续数 data/*.yaml)。

### automation/(分类器侧)

- `classifier/llm.py` prompt 重写为**层级式判定**:相关性 → L1 二选一(附评价标准
  规则)→ 分支内叶子类别(只呈现同层兄弟的定义,选择空间从 36 平铺降为 2→8/7→9)
  → 稀疏 tags。每个易混边界配 few-shot 示例。
- LLM 失败率 / retry 队列膨胀是独立的第二期工作,不在本次分类重构范围,但重构后
  队列需重置(见迁移计划)。

## 4. 迁移计划(依赖顺序)

1. **定稿本规格**(消掉全部 ⚖️)。
2. config.yaml 写入新 taxonomy + tags 定义。
3. 脚本迁移 data/ 文件(机械合并/改名),同轮人工归档 24 篇溶解论文、
   清洗 terminal 18 篇(⚖️ security 9 篇、visualization 5 篇按拍板结果处理)。
4. 改 `render_papers.py`,重生成 README(结构 + Quick Navigation + 计数)。
5. 重写分类器 prompt + few-shot,小样本回测(用已归档论文抽样验证分类一致性)。
6. **状态与积压处理** ⚖️:271 个 pending GitHub Issues 按旧分类生成,建议全部关闭
   作废;705 条 retry 队列清空;涉及论文重新走新分类器。`processed_ids` 保留防重。
7. 恢复 cron。

## 5. 待拍板清单 ⚖️

| # | 问题 | 选项 | 倾向 |
|---|---|---|---|
| 1 | security 9 篇 | 保留 `software_security` 叶子 vs 按实际任务打散(fuzzing→testing、patching→debugging) | 打散更纯粹,保留更省事 |
| 2 | visualization 5 篇 | `graphics_animation`(图是工件) vs `world_data`(图是分析副产品) | 归 graphics_animation,迁移时逐篇复核 |
| 3 | code_authoring 66 篇要不要拆 | 现在拆 vs 打完 artifact tag 看分布再定 | 先不拆 |
| 4 | Foundation Models README 节 | 取消(徽章标识) vs tag 驱动自动汇总节 | 取消 |
| 5 | 积压处理 | 271 pending Issues 全关 + retry 清空重跑 vs 逐个救 | 全关重跑 |
| 6 | 叶子 key 命名 | `software_*` / `world_*` 前缀方案 | 如上;可整体换 |
