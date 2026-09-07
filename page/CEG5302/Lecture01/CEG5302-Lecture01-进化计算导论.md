# 进化计算导论

> 本页属于：CEG5302 / Lecture 01
>
> 前置知识：[[CEG5302-讲义与笔记索引]]
>
> 预计阅读时间：6 分钟

## 什么是进化计算

进化计算（Evolutionary Computation, EC）是一类受自然进化启发的搜索与优化算法。它不直接构造单个解，而是维护一组候选解（population），通过反复评估、选择和变异/重组逐步改善群体。EC 的目标通常是复杂搜索空间中的高质量、可接受或近似最优解，不保证每次都找到精确的全局最优解。（Lecture 1, slides 14, 21, 34–36, 68–69）

## 历史先驱

课程介绍了几类历史先驱，它们的编码方式与算子不同，但共享进化式搜索逻辑：（Lecture 1, slides 11–12, 69）

| 先驱 | 提出者（年份） |
|---|---|
| Evolutionary Strategies | Rechenberg（1964） |
| Evolutionary Programming | Fogel 等（1965） |
| Genetic Algorithms | Holland（1975） |
| Genetic Programming | Koza（1992） |

Lecture 2 的 EA 家族列表在此基础上补充了 Differential Evolution。（Lecture 2b, slide 12）

## 为什么使用 EC

当搜索空间巨大、问题数学上难处理、目标 landscape 不规则，或为简化而建立的模型会偏离真实问题时，经典精确/解析方法可能不实用。EC 提供 population-based、具有并行探索性质的搜索，也可能在没有方便解析模型的情况下找到新颖设计。（Lecture 1, slides 33–36）

适合优先考虑 EC 的情形包括：

- 搜索空间很大；
- 只需满意的近似解；
- 解法本身尚未明确；
- 多个参数需要同时优化；
- 问题很难数学化描述；
- 多个目标与约束相互作用。

以上是适用性条件，不是 EC 一定优于专用算法的证明。

## 核心结论

- EC 以 population 搜索，而不是只沿单一路径搜索。
- Fitness 引导搜索；随机选择与 variation 保留探索能力。
- 最关键的工程设计点是 representation、evaluation、constraints、variation、survivor policy 与 termination。
- EC 用搜索灵活性换取较弱的精确最优保证。
- 使用 EC 之前，先确认问题 formulation 与 evidence 是否支持它，而不是因为有现成实现就直接套用。

## 下一步

- 上一页：[[CEG5302-讲义与笔记索引]]
- 下一页：[[CEG5302-Lecture01-自然进化隐喻与基本循环]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 1 - Introduction (D Srinivasan) 13Aug26.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture%201%20-%20Introduction%20%28D%20Srinivasan%29%2013Aug26.pdf)（扫描版），slide 引用以个人笔记 `notes/lecture/lecture-01-introduction-zh.md` 记录为准。
- 2026-09-03：从 Lecture 1 拆出“进化计算导论”短页。
