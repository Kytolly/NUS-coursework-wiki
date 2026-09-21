# 表示的概念与选择准则

> 本页属于：CEG5302 / Lecture 03
>
> 前置知识：[[CEG5302-Lecture02-Canonical-GA-Worked-Example]]
>
> 预计阅读时间：10 分钟

## 🎯 学习目标（Learning Objectives）

学完本页，你应该能：

1. 解释“表示（representation）是 phenotype↔genotype 的可逆映射”，并说明它**只影响 variation**。
2. 说清选择表示的 3 条准则（合法性/完备性、landscape 平滑性、representation bias）与背后的直觉。
3. 用“binary 表示实数 → 离散化/Hamming 悬崖”解释为什么表示会决定邻域结构、影响搜索效率。
4. 判断哪些组件与表示相关、哪些无关。
5. 记住“表示很难选、需要实践与领域知识、通常不穷尽”。

## 复习：表示与相关组件

- **Phenotype** 是原问题领域中的个体；**Genotype** 是 EA 领域中的个体。
- **Representation** 是 phenotype space 到 genotype space 的映射，应当可逆（invertible）。

表示只影响 **variation operators（mutation 与 recombination）**；evaluation function、parent selection、survivor selection 与 termination condition 是 **representation-independent** 的。（Lecture 3, slides 5, 10）

> 💡 **为什么“表示”很重要**：对任何问题，**第一步就是选表示方案**。课件明确说，这是使用 EA **最困难的部分之一**，**需要实践与领域知识**（slide 6）。后面我们会看到，binary 历史上被当作“大多数问题的唯一选择”，但这**并不总是对的**——表示一变，landscape 与搜索效果就可能完全不同。

## 选择表示的准则

（Lecture 3, slides 6–9）

1. **合法性与完备性**：映射应保证所有可能 genotype 都对应一个合法 solution，反之所有可能 solution 都能被某个 genotype 表示。（slide 6）
2. **对 fitness landscape 的影响**：表示决定 landscape 的邻域结构。好的表示让 landscape 更平滑——小的遗传改变只带来小的 fitness 变化，从而提升搜索效率；这是问题相关的。例如对实数值 decision variable 使用 binary 表示会离散化搜索空间。（slides 7–8）
3. **Representation bias**：由于编码方式，某些 phenotype 更容易被生成，使搜索偏向特定区域，可能降低 diversity、导致 premature convergence 或陷入 local optima。两个使用相同 fitness function 与 selection 准则但不同表示的 EA 可能得到截然不同的结果。（slide 9）

### 图意：表示如何塑造 fitness landscape（slides 7–8）

> 📘 课件强调 **representation scheme 决定了 fitness landscape 的 neighborhood structure**。图通常画成“fitness 曲面上的一个点/一小步”，用来对比两种表示：
> - **好表示**：小步基因改变 → 小步 fitness 变化 → landscape **平滑** → 搜索高效；
> - **差表示**：小步基因改变 → 可能大跳变 → landscape **崎岖/多悬崖** → 容易卡在局部峰。
> **问题相关**：同一表示在不同问题上平滑与否不同。

## 表示相关 vs 无关

表示方案只影响 **variation（mutation 与 recombination）**；下列组件与表示无关（依据课件第 5、10 页整理；核对 2026-09-07）：

| 类别 | 组件 |
|---|---|
| 表示相关（representation-dependent） | Mutation、Recombination |
| 表示无关（representation-independent） | Evaluation function、Parent selection、Survivor selection、Termination condition |

## 选择表示的决策链路

选择表示时按以下链条检查（自制，依据课件第 6–9 页；核对 2026-09-07）：

```mermaid
flowchart TD
  A[问题: 决定变量类型] --> B{能否满足合法性/完备性?<br/>genotype↔phenotype 一一对应}
  B -- 否 --> D[换一种表示或加约束处理]
  B -- 是 --> C[是否平滑 landscape?<br/>小基因改变→小适应度改变]
  C -- 否 --> E[考虑 binary 离散化/Gray code/<br/>其它编码]
  C -- 是 --> F[是否产生表示偏差?<br/>偏置某些 phenotype 更易到达]
  F --> G[评估表示 bias 影响]
  G --> H[选择 5 种表示之一:<br/>binary/integer/real/permutation/tree]
```

## 好表示的检查清单

结合课件“合法性/完备性、landscape 平滑、bias”三条准则，可整理成实践时逐项核对的问题（依据 slides 6–9 整理；核对 2026-09-07）：

- [ ] 每个 genotype 都对应一个合法 phenotype？（合法性）
- [ ] 每个可行 phenotype 都能被某个 genotype 表示？（完备性）
- [ ] 小基因改变通常只带来小 fitness 改变吗？（平滑 landscape）
- [ ] 是否存在明显偏好某些区域/解、从而伤害多样性的表示 bias？
- [ ] 该表示下 mutation/recombination 是否容易定义且高效？（表示相关组件）

**示例（平滑性）**：对连续变量用二进制编码会把搜索空间离散化（如把 $[0,1]$ 切成 256 级），相邻整数（如 $3=011$、$4=100$）Hamming 距离为 3，突变一位可能从数值附近跳到很远——landscape 显得“不平滑”。改用 Gray code（相邻整数只差 1 bit）或直接实数编码，可让单 bit 突变近似对应小步长。（依据 slides 8, 16–17 的二进制讨论，合并此处）

## 本讲范围

逐一介绍 5 种表示（binary、integer、real、permutation、tree）的常用 mutation 与 recombination 技术；这些不是穷尽列表，实践中可能需要 hybrid、problem-dependent 的表示。（Lecture 3, slide 11）

## Exam Checklist（考试自查）

- **必须理解**：三准则的本质；为什么“表示决定 landscape 邻域结构”；为什么 binary 表示实数是“不必要的不平滑”。
- **必须记忆**：表示相关组件（mutation/recombination）vs 表示无关组件（evaluation/parent/survivor/termination）；$3=011, 4=100$ 的 Hamming 悬崖。
- **必须手算**：给定 genotype 判断合法性/完备性；解释一个 bit 翻转对数值/ fitness 的影响。
- **了解即可**：Gray code 的完整构造、具体二进制定点量化位数。
- **明确 out of scope**：本讲不要求证明“表示 bias 一定有害”，也不枚举所有编码。

## 下一步

- 上一页：[[CEG5302-Lecture02-Canonical-GA-Worked-Example]]
- 下一页：[[CEG5302-Lecture03-Binary-and-Integer-Representation]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 3-Representation and Variation_27Aug2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.3-Representation.and.Variation_27Aug2026.pdf)，slides 4–17。
- 2026-09-03：从 Lecture 3 拆出“表示的概念与选择准则”短页。
- 2026-09-07：新增表示相关/无关组件对照表与表示选择决策链路 Mermaid 图。
- 2026-09-09：新增学习目标；补充“为什么选择表示很难（slide 6）”、fitness landscape 图意解析、三准则直觉；新增 Exam Checklist。
