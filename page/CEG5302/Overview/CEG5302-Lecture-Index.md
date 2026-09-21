# CEG5302 讲义与笔记索引

> 本页属于：CEG5302 / 知识索引
>
> 前置知识：[[CEG5302-Course-Materials]]
>
> 预计阅读时间：6 分钟

> 📘 **本 Wiki 的每页阅读约定**：每个知识点页都包含 **🎯 学习目标（Learning Objectives）**、**📚 知识点正文**（尽量按 *动机 → 推理 → 结果* 展开）、**图意解析 / 手算示例**、**Exam Checklist（考试自查）**，并在正文中用 `📘 Source / 💡 Explanation / 🔍 Inference / 🧪 Example` 区分“老师原话/教学解释/推断/示例”。如果你想“跟着老师讲一遍”，直接照页内顺序读即可；如果要“考前速查”，跳到每页底部的 Exam Checklist。

## 按讲进入

### Lecture 01：进化计算导论

- [[CEG5302-Lecture01-Introduction-to-EC]]
- [[CEG5302-Lecture01-Evolution-Metaphor-and-Basic-Cycle]]
- [[CEG5302-Lecture01-Problem-Types-and-Applications]]

### Lecture 02：问题建模与 EA 组件

- [[CEG5302-Lecture02-Problem-Types-and-Single-Objective]]
- [[CEG5302-Lecture02-Computational-Complexity-and-EC-Motivation]]
- [[CEG5302-Lecture02-EA-Seven-Components]]
- [[CEG5302-Lecture02-Canonical-GA-Worked-Example]]

### Lecture 03：表示与变异

- [[CEG5302-Lecture03-Representation-Concepts-and-Criteria]]
- [[CEG5302-Lecture03-Binary-and-Integer-Representation]]
- [[CEG5302-Lecture03-Real-Valued-Mutation]]
- [[CEG5302-Lecture03-Real-Valued-Recombination]]
- [[CEG5302-Lecture03-Permutation-Representation]]
- [[CEG5302-Lecture03-Tree-Representation-and-Crossover-Conclusions]]

### Lecture 04：选择与种群管理

- [[CEG5302-Lecture04-Population-Models-FPS-and-Ranking]]
- [[CEG5302-Lecture04-RWS-Tournament-and-Selection-Schemes]]
- [[CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure]]
- [[CEG5302-Lecture04-Diversity-Maintenance-and-Niching]]
- [[CEG5302-Lecture04-Island-Cellular-EA-and-MATLAB]]

### Lecture 05：约束处理

- [[CEG5302-Lecture05-Constraint-Handling-Overview]]
- [[CEG5302-Lecture05-Penalty-Functions-Principles]]
- [[CEG5302-Lecture05-Penalty-Function-Types-and-Key-Points]]

## 概念衔接

- **L1 → L2**：第 1 讲的 basic loop 与 fitness/selection 隐喻，在第 2 讲形式化为 EA 七大组件与 `input → model → output` 的问题分类。
- **L2 → L3**：第 2 讲指出“变异算子必须匹配表示”，第 3 讲逐一种类给出每个表示的 mutation 与 recombination 算子。
- **L2 → L4**：第 2 讲引入 parent/survivor selection 与 population，第 4 讲展开选择算子、selection pressure 与 niching。
- **L3 → L4**：第 4 讲开篇重申 selection 是 representation-agnostic 的，承接第 3 讲“selection 与表示无关”的结论。
- **L4 → L5**：经历表示与选择之后，第 5 讲转向真实问题中的约束，用间接/直接法与罚函数把约束并入 EA；为项目 Part-II 带约束优化铺垫。
- **L1/L2 → 多目标**：Lecture 1（Pareto trade-off）、Lecture 2a（单目标优化）、Lecture 2b（MOO 入门，含 iPhone 例子）共同为项目 Part-I（NSGA-II / ZDT3）与后续多目标讲次铺垫；`many-objective（目标>3）` 明确不在本模块范围内。

## 四个横切主线（跨讲反复出现）

- **Exploration ↔ Exploitation**：L1 引入 → L2 的 EC vs SI 与“Anything that works” → L3 的表示/变异步长（σ、BLX、SBX）→ L4 的选择压力与 niching。
- **Selection Pressure**：L2b 的 FPS/选择 → L4 的 FPS 问题、Ranking、Tournament、over-selection 与 takeover time $\tau^*$。
- **Diversity**：L2b 的 population diversity → L3 的 representation bias / crossover 增多样性 → L4 的 niching（显式/隐式）。
- **Feasibility**：L2a 的约束与可行域 → L5 的间接（罚函数）与直接（修复/表示/解码）处理。

## 个人笔记的作用

`notes/lecture/lecture-0X-*-zh.md` 与 `-en.md`（本仓库以 `notebook/week-0X-*.md` 提供）是课堂参考与问题记录。正式 Wiki 页面以对应老师课件为主，并标出 PDF 与 slide 范围；笔记中的额外解释只有在能被课件支持时才纳入正文。Lecture 1 课件为扫描版，其内容以笔记记录为桥梁核对。

## 来源

- 讲义目录：[CEG5302 Assets Release](https://github.com/Kytolly/NUS-coursework-wiki/releases/tag/CEG5302)（本机核对）。
- 参考笔记：[CEG5302 Assets Release](https://github.com/Kytolly/NUS-coursework-wiki/releases/tag/CEG5302)。
- 核对日期：2026-09-07。

## 下一步

- 上一页：[[CEG5302-Course-Requirements]]
- 下一页：[[CEG5302-Lecture01-Introduction-to-EC]]
- 返回：[[Home]]

## 更新日志

- 2026-09-03：建立 Lecture 01–04 拆分页索引，并明确课件优先原则。
- 2026-09-07：纳入 Lecture 05 三个拆分页。
- 2026-09-09：补充“每页阅读约定”（学习目标/图意解析/手算/Exam Checklist）；扩展概念衔接（MOO 前置）并新增四个横切主线索引。
