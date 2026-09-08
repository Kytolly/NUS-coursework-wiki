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

## EC 的统一框架

无论具体是 GA、ES、EP 还是 GP，进化计算都共享同一条思路：用「种群 + 变异/重组 + 选择」反复迭代，而不是单点改进。通用伪代码如下（Lecture 2b, slides 29–36 的补充，本页先给概念框架）：

```text
初始化并评估种群 P
while 终止条件未满足:
    按适应度从 P 选父代（进入 mating pool）
    用 recombination/mutation 生成 offspring
    评估 offspring
    从 parents + offspring 中选 survivors 形成下一代
    P = survivors
```

下图给出从「自然进化」到「进化计算」的映射链（自制，依据课件第 17–23、33–36 页；核对 2026-09-07）：

```mermaid
flowchart LR
  A[自然进化<br/>繁殖+变异+选择] --> B[进化计算 EC]
  B --> C[维护候选解种群]
  C --> D[适应度评估]
  D --> E[变异/重组+选择]
  E --> F{终止?}
  F -- 否 --> C
  F -- 是 --> G[输出近优解]
```

> [!QUESTION] Q-CEG5302-W01-1
> **Context:** EC 是随机搜索家族；它在「什么都可能」的问题上未必优于随机游走（No Free Lunch 定理在第 2、4 周提及）。
> **Question:** 如何为具体问题加入问题知识（memetic GA）以在保持泛化性的同时优于随机搜索？这与“随机搜索平均最优”是否冲突？
> **Status:** Open

## 为什么使用 EC

当搜索空间巨大、问题数学上难处理、目标 landscape 不规则，或为简化而建立的模型会偏离真实问题时，经典精确/解析方法可能不实用。EC 提供 population-based、具有并行探索性质的搜索，也可能在没有方便解析模型的情况下找到新颖设计。（Lecture 1, slides 33–36）

进化与优化之间的隐喻映射（Lecture 1, slide 21; Lecture 2a, slide 43）：

| 自然进化 | 计算问题求解 |
|---|---|
| Environment（环境） | Problem（问题） |
| Individual（个体） | Candidate solution（候选解） |
| Fitness（适应度） | Quality of solution（解质量） |

### 探索与开发的平衡

EC 在运行中同时进行**探索（exploration，尝试新区域）**与**开发（exploitation，深挖有希望区域）**。开发过强会过早陷入局部最优；探索过强会显著拉长运行时间、收敛变慢。（Lecture 1, slides 34–36; Lecture 2a, slides 48–49）

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

- 来源：[Lecture 1 - Introduction (D Srinivasan) 13Aug26.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.1.-.Introduction.D.Srinivasan.13Aug26.pdf)（扫描版）、[Lecture 2a-Introduction_20Aug2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.2a-Introduction_20Aug2026.pdf)，slides 14–36（对应 EC 框架/隐喻），slide 引用以个人笔记 `notes/lecture/lecture-01-introduction-zh.md` 记录为准。
- 2026-09-03：从 Lecture 1 拆出“进化计算导论”短页。
- 2026-09-07：扩写统一框架、伪代码、术语映射表与探索/开发说明，新增 EC 映射链 Mermaid 图。
