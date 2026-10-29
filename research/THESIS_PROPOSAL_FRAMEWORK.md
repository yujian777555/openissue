# 硕士毕业论文开题框架（候选版）

**更新日期：** 2026-10-27  
**所属项目：** `yujian777555/openissue`  
**状态：** 开题研究框架草案；题目、创新点与实验基准尚未正式批准  
**用途：** 服务硕士毕业大论文的开题报告，不把单篇小论文候选误当成整篇毕业论文。

## 0. 研究定位校正

当前任务不是“找到一个算法并立即实现”，而是为毕业大论文建立一个可论证、可执行、能容纳 2–3 个相互关联研究内容的总体框架。

前一阶段的 OSLVC（Operator-Specific Lineage-Value Control）只能视为**候选核心方法**。它可能成为一篇小论文的主方法，也可能在近邻工作审计后被修改；它本身不等于整篇毕业论文，也不能直接拆成三个创新点。

研究约束：
- 演化计算必须是核心方法；必须明确静态 EA 参数如何调优、演化过程中如何在线控制参数/算子。
- 用户明确排除通信方向，不得把多智能体通信协议演化作为候选主线。
- 可以在已有论文基础上借鉴、融合和改进；相关工作拥挤不等于自动放弃，但必须说清机制差异并用强基线验证。
- 不以有限预算或单纯降低调用成本作为毕业论文核心贡献。
- 研究内容应围绕一个总体问题，不为凑满三个创新点强行组合不相关的技巧。
- 目前没有最终批准的论文题目、创新点或实验方案。

## 1. 暂定总体方向与题目

### 推荐的工作题目（暂定）

**《面向复杂工具任务的大语言模型智能体策略自适应演化优化方法研究》**

备选：
1. 《面向任务泛化的大语言模型智能体策略演化优化方法研究》
2. 《大语言模型智能体策略的行为尺度建模与自适应演化控制方法研究》

当前推荐第一个，原因是它能把研究对象限定在可执行的 Agent 工具使用策略/工作流，同时为行为尺度建模、演化参数控制和跨任务泛化保留空间；但不会过早把论文锁死在 OSLVC、某一个特定 EA 或某一个 benchmark 上。

**题目仍然是候选，不是已经定稿。** 在导师确认前，先用它组织开题研究，不要把候选算法名直接放进正式论文题目。

## 2. 大论文要解决的总体问题

### 2.1 问题陈述

复杂工具任务中的 Agent 策略包含规划、工具选择、调用、结果整合等可修改模块。演化计算可以在不依赖梯度的情况下搜索这些策略，但现有方法仍留下三个相互关联的问题：

1. **搜索步幅难以比较：** 文本编辑大小不等于 Agent 行为变化大小；不同类型的变异/重组算子即使请求相同强度，也可能产生不同的实际行为变化。
2. **搜索控制信号不充分：** 固定参数或只根据子代即时得分调节算子，可能无法区分“当前有效的局部改进”和“暂时退步但有助于后续改进的结构变化”。不过，行为尺度控制、动态算子选择和谱系信用都已有先行工作，不能单独作为新颖性声明。
3. **训练任务表现不等于跨任务泛化：** 控制策略可能过拟合优化时见到的任务族。需要独立验证学到的演化控制机制是否能迁移到未见任务族，而不是只报告训练任务上的最优分数。

### 2.2 总体科学问题

> 对于结构化的大语言模型 Agent 策略，如何将实际行为变化纳入演化搜索的表示与反馈，并据此设计可调优、可自适应且能在未见任务族上保持有效性的演化控制机制，从而提升任务成功率与跨任务泛化能力？

### 2.3 为什么以演化计算为核心

研究对象是 Agent 策略，但主要方法问题属于演化计算：
- 个体表示与合法变异邻域如何定义；
- 变异、重组等算子的行为尺度如何校准；
- 种群规模、后代数、变异/交叉概率、选择压力和算子混合比例如何调优；
- 搜索过程中如何自适应选择算子与强度；
- 如何给演化动作分配即时与长期信用；
- 控制策略如何跨任务迁移并与固定参数 EA 比较。

不能只把 EA 当作一个黑盒优化器，也不能只通过提高 LLM 提示词质量来宣称演化计算创新。

## 3. 相关工作给出的边界

| 工作 | 已经解决/覆盖的部分 | 对本论文的约束 |
|---|---|---|
| **EVOTOOL (ACL 2026)** — https://aclanthology.org/2026.acl-long.2016/ | 将工具使用策略模块化；轨迹归因定位失败模块；定向变异；多样性选择 | 不能把模块化、失败归因、定向变异或多样性保留单独作为新贡献。可作为最直接的 Agent 策略演化基线之一，代码与数据可用性仍需核验。 |
| **EvoMAS: Evolutionary Generation of Multi-Agent Systems (ICML 2026)** — https://proceedings.mlr.press/v306/hu26bg.html | 在结构化 MAS 配置空间中演化；依据执行轨迹进行反馈条件化变异/交叉；维护经验记忆 | 不能把结构化 Agent 配置演化、反馈引导变异/交叉、经验记忆作为泛化创新点。其代码许可证为 CC BY-NC 4.0，使用需遵守非商业与署名条款。 |
| **EvoMAS: Heuristics in the Loop (ICML 2026)** — https://proceedings.mlr.press/v306/wei26m.html | 七种演化策略、自适应策略选择、角色级演化、课程学习与反思式元控制 | 不能把动态算子库或元控制器本身作为创新。需要核对最终论文中的状态、信用分配和策略更新机制。 |
| **ELMER (2026 preprint)** — https://arxiv.org/abs/2608.10196 | 基于执行行为校准低/中/高语义变异尺度，并通过偏好优化增强控制 | 不能把行为尺度校准或条件化语义变异本身作为新。可研究其校准机制能否扩展到异质的 Agent 演化算子，以及是否能支持外层控制器。 |
| **The Time Value of Evolution / LVPG (2026 preprint)** — https://arxiv.org/abs/2608.13297 | 基于搜索状态和剩余步数选择变异尺度；用后代路径的 best-so-far 改进分配长期信用 | 不能把在线强度控制、长期谱系信用单独作为新。需检验它们与异质 Agent 算子结合后是否存在额外收益。 |
| **LLaMEA-HPO** — https://doi.org/10.1145/3731567 | 将算法结构生成与数值超参数优化分开 | 本研究必须先得到调优后的强静态 EA，再验证在线控制的额外价值；不能只与默认参数比较。 |
| **CATArena (ICML 2026)** — https://proceedings.mlr.press/v306/fu26a.html | 评估代码 Agent 在多轮迭代、反思和同伴学习中的演化能力 | 可作为演化能力评测方面的参考，但它不直接证明 OSLVC 的算法创新；其任务/许可证适配需另行审计。 |

**当前判断：** 大方向有明确价值，但大方向本身不新。可继续验证的具体机制假设是：对异质的 Agent 演化算子分别校准行为尺度，再联合控制“算子 × 行为尺度”，并检验谱系价值是否提供超过即时收益和已有 AOS 的额外信息。这个假设还没有通过完整的近邻工作审查。

## 4. 研究内容与候选创新点的组织方式

以下是开题阶段的**拟研究内容**，不是已经确认的创新结论。优先形成两个紧密相连的核心方法；第三项只有在发现独立、可验证的机制差异后才升格为创新点。

### 研究内容一：Agent 演化算子的行为尺度表征与校准

**研究问题：** 不同的 Agent 策略变异算子在请求相同“低/中/高”强度时，是否产生不同的实际行为变化？如果是，按算子校准行为尺度能否提高演化邻域的可控性？

**候选方法：**
1. 将 Agent 个体表示为结构化、可执行的策略/工作流配置。
2. 选取少量可解释的合法算子，例如模块内语义修改、结构修改和兼容重组；不在第一版引入过多算子。
3. 在训练任务的共同 probe 集上记录父代与子代的动作/工具调用轨迹。
4. 定义可复现的行为距离，同时单独记录合法性、任务成功率与严重退化，避免把“变化大”误认为“变化好”。
5. 比较统一尺度映射、算子特定尺度映射和不控制尺度的基线。

**与 ELMER 的可能差异：** ELMER 已建立执行行为驱动的语义变异尺度；本研究不能重复该贡献。待验证的区别是将校准对象扩展到不同 Agent 算子，并证明算子条件化校准能改善后续搜索，而不仅仅提高距离预测相关性。

**独立论文潜力：** 中等、待验证。只有当校准机制对下游任务成功率/搜索质量产生可重复的增益时，才值得独立投稿；否则并入研究内容二。

### 研究内容二：面向 Agent 策略演化的自适应算子—强度联合控制

**研究问题：** 在固定任务和评估条件下，动态选择算子与实际行为尺度，是否能优于最强静态参数配置、经典自适应算子选择、仅调强度和仅使用谱系信用的控制器？

**候选控制动作：**
[
a_t=(o_t,s_t)
]
其中 (o_t) 为演化算子，(s_t) 为该算子的目标行为变化尺度。

**候选状态信息：**
- 当前候选及其适应度/排名；
- 最近若干代的改进幅度、停滞和回退；
- 种群行为多样性；
- 当前算子和尺度的历史表现；
- 已观测的父子行为距离及合法性；
- 当前任务可见的描述特征和剩余演化步数。

**候选信用分配：**
- 即时信用：子代在固定训练/验证规则下带来的改善；
- 谱系信用：该子代及其后代在预先规定的深度/时间窗内是否带来新的 best-so-far 改进；
- 不把“产生了新颖但无效的子代”自动当作正收益；
- 不把乐观的后代最大值直接当成无偏期望，需要与可校准的估计和即时收益对照。

**必须比较的基线：**
1. 默认静态 EA；
2. 经随机搜索或 SMAC 调优的强静态 EA；
3. 预设变异强度/算子比例调度；
4. 经典自适应算子选择（如 Probability Matching、Adaptive Pursuit 或 UCB 类方法）；
5. 自适应/自适应编码的演化参数；
6. ELMER 式强度控制；
7. LVPG 式谱系信用控制；
8. EvoMAS 策略选择（在相同对象与任务上可公平适配时）；
9. 候选联合控制器。

**可能成为核心创新的条件：** 联合控制必须在匹配任务、基础模型、评价次数、种群设置与停止规则的条件下，优于最强静态 HPO 和单机制控制器；且消融能证明算子条件化尺度和谱系信用的贡献不是简单叠加或额外试验次数带来的。

### 研究内容三（可选）：演化控制器的跨任务迁移与泛化

此项当前是**待审查的扩展方向**，不能仅凭“在未见任务上测试”就称为创新。

拟研究的问题是：在若干训练任务族上学到的算子—强度控制规律，能否迁移到未见任务族，而不需要重新从零调参？如果要将其升格为独立创新，必须提出明确的迁移机制，并与任务条件化演化、跨任务元启发式迁移（如 MECo/MTHS 相关工作）及任务特定控制器比较。

- 若只有泛化测试而没有新的方法机制：将其作为研究内容二的关键验证，不单列创新点。
- 若能提出与已有迁移方法有清晰区别的任务条件化控制机制，并有独立证据：再考虑将其作为第三个创新点/小论文。
- 若差异不成立：不强行凑第三点，毕业论文以两个有力方法贡献为主。

## 5. 演化计算如何调参与控制（开题必须明确）

### 5.1 不混淆五类变量

| 层次 | 变量示例 | 研究方式 |
|---|---|---|
| Agent 基因型 | 策略模块、工具选择规则、调用约束、工作流结构、提示/规则内容 | 定义合法表示与变异算子 |
| 静态 EA 超参数 | 种群规模、每代后代数、变异/交叉概率、选择压力、精英保留、算子混合比例 | 在训练/验证任务上用随机搜索/SMAC 等调优，冻结测试配置 |
| 在线控制参数 | 当前算子、变异尺度、探索/开发倾向、停滞后的算子切换 | 比较固定配置、预设调度、经典 AOS、自适应参数与候选控制器 |
| 变异模型参数 | 生成模型、采样设置、结构约束、强度条件 | 固定或单独调优；防止把模型变化误认为 EA 贡献 |
| 任务与评估设置 | 任务族划分、环境种子、验证器、难度、停止规则 | 预注册并固定；测试集不得用于调参或控制器更新 |

### 5.2 实验顺序

1. **先固定基准和基因型。** 选择有明确许可、可执行、可重复的 Agent 任务；定义合法算子和行为距离。
2. **先测静态参数敏感性。** 使用小规模分阶段/部分因子设计，找出对结果影响较大的参数，不跑无意义的全笛卡尔积。
3. **调出强静态基线。** 用随机搜索或 SMAC 在训练/验证任务上选出配置；完整记录搜索空间、随机种子、选择规则。
4. **再测在线控制。** 与固定参数、预设调度、经典 AOS、自适应参数、自适应强度和谱系控制对比。
5. **最后验证跨任务泛化。** 按任务模板、工具族或任务组合划分 holdout；不能只随机拆分同一模板的近似改写。
6. **匹配公平性条件。** 主要比较应控制基础模型、可用训练任务、评价次数和停止规则；费用/Token 作为次要报告，不作为核心研究目标。

## 6. 总体技术路线

`文献与代码审计`
`→ 定义结构化 Agent 策略基因型与可执行评估器`
`→ 选定合法 benchmark 并复现强基线`
`→ 行为距离与算子特定尺度校准`
`→ 静态 EA 参数敏感性分析与 HPO`
`→ 自适应算子—尺度控制及谱系信用`
`→ 消融、强基线比较与未见任务族测试`
`→ 汇总为毕业论文，并按独立研究问题拆分小论文`

## 7. 基线与实验环境选择原则

### 7.1 直接方法基线

- **EvoTool（ACL 2026）**：当前最直接的 Agent 策略演化基线，官方实现为 MIT 许可；其模块定向变异、轨迹归因和多样性选择均属于已有方法，必须公平复现或对比。
- **静态 EA + HPO**：必须先在训练/验证任务上调优种群规模、后代数、变异概率、选择压力与固定算子比例，再冻结配置。
- **机制近邻**：ELMER（行为尺度控制）、LVPG（尺度/谱系价值控制）、经典 AOS 与自适应参数控制。不得把这些已有机制本身写成创新点。
- **EvoMAS 两篇论文**：Wei et al. 的 *Heuristics in the Loop* 与 Hu et al. 的 *Evolutionary Generation of Multi-Agent Systems* 是不同论文，不能混为一谈；前者最终版精确信用机制仍待全文核验，后者已覆盖反馈条件化变异/交叉与经验记忆。

### 7.2 实验环境：控制机制验证 + 经审计的真实任务验证

1. **机制隔离环境：** 优先审查 Tool-Veritas（Apache-2.0 子项目）作为本地确定性工具执行 substrate。它有状态沙箱、逐轮硬状态检查和完整轨迹记录；但当前打包的 `all.jsonl` 只有 70 个案例、覆盖 16 个领域，没有可直接用于本研究的 train/validation/test 划分。应以其执行框架为参考，构建并独立核验规模更适合演化实验的任务族；不能直接把 70 个示例当成充分基准。
2. **真实任务验证：** 优先审查并固定官方 `sierra-research/tau2-bench` 的单一版本（当前候选为 v2.0.0），但必须审计所选任务及其评分器。2026 年的独立评测有效性审计在 496 个工具调用任务执行中发现 92 个评分器与人工判断不一致（18.5%），其中 τ²-Bench Retail 样本为 11/112（9.8%）；Epoch AI 的另一项 BFCL v4 审查也报告了较高的抽样缺陷率。因此，官方分数只能作为一个结果，不应未经核验就当成绝对真值。
3. **任务划分：** 对任务模板、场景意图、工具/动作签名进行分组，完整任务族只能进入 train、validation 或 test 其中一个集合。固定版本、任务 ID、模型、解码设置、环境状态、种子和评分器版本。
4. **评分器设计：** 主要成功指标使用可检查的目标状态/不变量；工具调用合法性和对话质量单独报告。只有当“必须使用特定工具”本身就是任务目标时，才将某个工具写成硬性必选条件，避免把另一条同样成功的执行路径误判为失败。
5. **冻结的 `text-v1` 限制：** 该 manifest 与源 train/test 列表有重叠：airline_50 = 30/20，retail_50 = 28/22，telecom_50 = 27/23（train/test）。若演化使用了源 train 任务，不能再把完整 `text-v1` 分数当作 held-out 结果。只能报告锁定测试任务/任务族，或明确标注自定义研究 split；不得称为官方 leaderboard 分数。

细节见 `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`。
### 7.3 其他基准的使用边界

- **BFCL v4**：可作为额外鲁棒性验证，但不宜单独作为主要证据；2026 年独立审查在抽样的 50 个任务中报告了 24 个存在影响评测的问题，选用子集前需逐项审计。
- **ToolMaze**：许可与 split 问题尚未解决，不作为默认主基准。
- **EvoTool 自带 demo split**：只用于 smoke test，不用于最终测试或官方分数；其 τ-bench demo builder 先从 upstream test/train/dev 来源顺序选任务，再随机切分 demo 池。

详细审计与 split 数量见 `research/BENCHMARK_AND_BASELINE_DECISION_R2.md`。在完成最终近邻论文审计与数据/split gate 前，不启动正式付费实验。
## 8. 主要评价指标与统计设计

**主要指标：**
- 任务成功率（主指标）；
- 未见任务族上的成功率与泛化差距；
- 相对基础 Agent 的平均性能改善。

**次要指标：**
- 子代合法/可执行率；
- 请求尺度与实际行为距离的相关性及校准误差；
- 暂时退化后恢复的概率；
- 行为覆盖/种群多样性；
- 评估次数、Token 与 API 成本。

采用多随机种子和配对任务评测，报告效应量与不确定性区间。统计单位、主要对比和停止规则应在实验前确定，避免从大量指标中挑选有利结果。

## 9. 预期论文组织（工作方案，不是承诺）

| 产出 | 暂定研究问题 | 独立性条件 |
|---|---|---|
| 小论文 A（候选） | 异质 Agent 算子的行为尺度校准是否改善可控变异和下游搜索？ | 需要单独证明校准机制有独立效益；否则并入 B |
| 小论文 B（核心候选） | 联合算子—强度控制与谱系信用是否优于强静态 HPO 和已有控制器？ | 必须有完整强基线、消融与任务成功提升 |
| 小论文 C（可选） | 控制器是否能跨任务族迁移，且是否需要独立迁移机制？ | 只有在形成独立算法贡献后才拆分；否则作为 B 的泛化实验 |

毕业论文整合的主线是“可控变异 → 自适应演化控制 → 泛化验证”，不是三个互不相干的算法技巧。

## 10. 开题报告建议结构

1. **研究背景与意义：** Agent 策略设计与优化的困难；为什么演化计算适合结构化、不可微的策略搜索；为何要研究搜索控制而非只调提示词。
2. **国内外研究现状：** Agent 策略演化（EVOTOOL、EvoMAS）；行为尺度控制（ELMER）；谱系价值控制（LVPG）；经典 EA 参数控制/AOS；静态 HPO 与跨任务迁移。
3. **现有研究不足：** 只列有文献或代码证据支持的具体不足；区分作者已承认的限制与本研究待验证的推断。
4. **研究目标与关键科学问题：** 对应总体问题与 RQ1–RQ3。
5. **研究内容和拟创新点：** 先列 2 个核心候选，第三点作为有条件扩展；写明各自与最接近工作的差异。
6. **研究方案与技术路线：** 基因型、算子、静态 HPO、在线控制器、适应度与行为距离、holdout 设计。
7. **实验条件与可行性：** 代码、模型、GPU/API、数据许可、复现成本和备选方案。
8. **进度安排与预期成果：** 文献审计、基线复现、方法实现、消融与泛化、论文撰写；具体月份由开题时间与导师要求确定。
9. **风险与替代方案：** 若尺度校准不增益则删除该模块；若联合控制不优于强静态 HPO/AOS则修改控制机制；若第三点没有独立贡献则只保留两点。

## 11. 当前结论与开题前的门槛

目前最合理的做法不是宣布 OSLVC 已经创新，而是用这个框架推进开题论证，并优先关闭三个门槛：

1. **G0：近邻机制审计。** 尤其核对 EvoMAS: Heuristics in the Loop 最终发表版本、ELMER、LVPG 和经典 AOS 的精确控制/信用机制。
2. **G1：基准与许可。** 确定一个能公平复现、具有训练/验证/测试任务族划分的 Agent 任务集。
3. **G2：可行性基线。** 在实现新控制器前，确认基础 Agent 与现有演化基线能够稳定运行，并能可靠测量行为变化。

只有 G0–G2 通过，才将拟创新点写成更强的开题承诺。开题阶段可以提出清晰的研究假设，但不应把尚未验证的假设写成已经得到证明的结果。


## 12. 2026-10-27 refinement: the main candidate must improve credit assignment, not merely combine controls

The first OSLVC sketch—operator-specific behavior scale + joint control + lineage return—is too broad as a novelty claim. ELMER already controls behaviorally measured mutation scale, LVPG already controls mutation radius using search state/horizon and lineage returns, and classical AOS already studies operator selection with fitness- and diversity-based credit. The official ICML 2026 record for EvoMAS: Heuristics in the Loop also confirms a dynamic seven-strategy portfolio and reflective meta-controller; its exact credit equations remain to be checked from the full paper.

The refined candidate is **scale-conditioned lineage-value credit**: estimate the continuation value of an operator conditional on the actual behavior displacement it generates, using matched parent/task/state comparisons. The central hypothesis is that raw operator reward may confound operator quality with perturbation magnitude. The candidate must beat (i) tuned static HPO, (ii) classical AOS including diversity/parent-distance credit, (iii) ELMER-style strength-only control, (iv) LVPG-style lineage-only control, and (v) a naive joint operator–strength controller using raw lineage return. See `research/OSLVC_R1_SCALE_CONDITIONED_LINEAGE_CREDIT.md`.

This is a more precise hypothesis, not a confirmed innovation. If the conditional credit adds no value, drop it; do not retain it merely because it sounds novel. Communication-protocol evolution remains excluded.


## 13. Source and benchmark gate update (2026-10-27)

The latest audit adds a strong direct Agent+EC baseline: EvoTool (ACL 2026), whose official implementation provides blame-aware targeted mutation, diversity-aware population selection, and an offline tool executor. These mechanisms must be included in the baseline ladder; neither targeted mutation nor diversity-aware selection is a new contribution for this thesis.

A benchmark-integrity issue was also identified: the EvoTool τ-bench converter selects from canonical test tasks before train/dev, after which the reference runner randomly splits the 150-instance demo subset. The resulting demo test split is not guaranteed to be independent of the official benchmark test pool. Use this subset for smoke testing only. Final evaluation must split by task template or tool/API family, freeze test tasks, and verify upstream data terms. The original τ-bench repository warns that its tasks are outdated; the updated τ³-bench line is a possible external-validation target after adapter work.

The official ICML/PMLR EvoMAS record confirms a seven-strategy portfolio, adaptive strategy selection, role-level evolution, curriculum, and reflective meta-controller, but exact reward/credit equations remain unverified in this pass. G0 is still open. See research/EVOMAS_HIL_METHOD_AUDIT_R1.md and research/PROPOSAL_GAP_MATRIX_R1.md.


## 14. Second EvoMAS method audit and claim boundaries (2026-10-27)

Distinguish two ICML 2026 papers with the same name. Hu et al., *EvoMAS: Evolutionary Generation of Multi-Agent Systems*, covers execution-trace-conditioned mutation of one component type per step, topology-inheriting crossover, task-relevance/performance-history selection, reward-based pool updates, and cross-query experience memory. Wei et al., *EvoMAS: Heuristics in the Loop*, covers a seven-strategy portfolio, adaptive strategy selection, role-level evolution, curriculum, and reflective meta-control. Cite them separately.

Feedback-guided mutation, crossover, configuration evolution, experience memory, and adaptive operator portfolios cannot be standalone innovations. The only current narrow hypothesis is whether operator continuation value should be estimated conditional on realized behavior displacement under matched parent/task/state comparisons. This remains provisional until the Wei HIL mechanism is verified and strong baselines reject simpler explanations. See research/EVOMAS_CONFIG_EVOLUTION_METHOD_AUDIT_R1.md.




## 15. Thesis feasibility and conditional research gates (2026-10-29)

The current thesis route is considered feasible enough to continue proposal preparation, but the specific OSLVC mechanism is not yet established. The latest discussion used these **subjective planning ranges only**: overall thesis completion 75–85%; OSLVC becoming the final effective algorithmic contribution 35–50%; 2–3 independent defensible innovation points 50–65%; 2–3 small-paper submissions 40–60%. These are not calibrated probabilities, experimental results, or publication forecasts and must be revised when the validation gates produce evidence.

- **G0 (OPEN):** verify the final EvoMAS: Heuristics in the Loop mechanism and closest prior art at equation/ablation level.
- **G1 (PARTIAL/OPEN):** finalize data/license review, task-family split, scorer checks, and benchmark version.
- **G2 (NOT RUN):** local controlled pilot to test operator/strength displacement heterogeneity and whether displacement-conditioned lineage credit adds value.
- Do not begin large/paid API experiments before G0/G1 are closed. Static EA HPO must precede adaptive-control claims.
- If OSLVC fails, revise or remove the conditional-credit component; retain the broader thesis frame only if a distinct alternative EC mechanism can be supported. Do not manufacture three innovations by splitting one method.
- Full continuity record: `research/FEASIBILITY_AND_NEXT_GATE_2026-10-29.md`.

## 16. G1 benchmark and family-split protocol (2026-10-29)

The current evaluation design is recorded in `research/G1_TASK_FAMILY_SPLIT_PROTOCOL_R1.md`: a proposed 120-task original deterministic suite, five mock domains, twelve global task families, two variants each, and whole-family split of 60 train / 30 validation / 30 test. Task files, oracle tests, and manifest hashes are not yet created, so this is not a completed benchmark.

The current external candidate is tau2-bench v2.0.0 source test (20 airline + 40 retail IDs, pinned in the protocol); it must not be reported as the frozen `text-v1` leaderboard. Δτ-Bench has been newly identified as a candidate for cross-version tool adaptation, but its separately hosted dataset license/revision/checksum and family overlap remain open. G1 remains PARTIAL/OPEN; no experiment has run.



## 17. Controlled-suite implementation milestone (2026-10-29)

The family-held-out evaluation design now has a first executable software prototype in `research/controlled_suite/`:
- 22 deterministic in-memory tools across five isolated domains;
- 12 original representative cases covering F01–F12;
- state-invariant and trace-constraint scoring;
- 14 local unit/smoke tests passed.

This milestone validates the feasibility of deterministic task execution and scoring only. It does not establish that evolutionary search improves Agent capability or that OSLVC is novel/effective. The other 108 planned cases, independent oracle review, family leakage audit, final data hashes, and external adapter/scorer are still pending. G1 remains PARTIAL/OPEN; G2 has not started.
