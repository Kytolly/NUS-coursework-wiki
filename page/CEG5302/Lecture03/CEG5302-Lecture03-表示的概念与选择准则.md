# 表示的概念与选择准则

> 本页属于：CEG5302 / Lecture 03
>
> 前置知识：[[CEG5302-Lecture02-CanonicalGA与手算示例]]
>
> 预计阅读时间：7 分钟

## 复习：表示与相关组件

- **Phenotype** 是原问题领域中的个体；**Genotype** 是 EA 领域中的个体。
- **Representation** 是 phenotype space 到 genotype space 的映射，应当可逆（invertible）。

表示只影响 **variation operators（mutation 与 recombination）**；evaluation function、parent selection、survivor selection 与 termination condition 是 **representation-independent** 的。（Lecture 3, slides 5, 10）

## 选择表示的准则

（Lecture 3, slides 6–9）

1. **合法性与完备性**：映射应保证所有可能 genotype 都对应一个合法 solution，反之所有可能 solution 都能被某个 genotype 表示。（slide 6）
2. **对 fitness landscape 的影响**：表示决定 landscape 的邻域结构。好的表示让 landscape 更平滑——小的遗传改变只带来小的 fitness 变化，从而提升搜索效率；这是问题相关的。例如对实数值 decision variable 使用 binary 表示会离散化搜索空间。（slides 7–8）
3. **Representation bias**：由于编码方式，某些 phenotype 更容易被生成，使搜索偏向特定区域，可能降低 diversity、导致 premature convergence 或陷入 local optima。两个使用相同 fitness function 与 selection 准则但不同表示的 EA 可能得到截然不同的结果。（slide 9）

## 本讲范围

逐一介绍 5 种表示（binary、integer、real、permutation、tree）的常用 mutation 与 recombination 技术；这些不是穷尽列表，实践中可能需要 hybrid、problem-dependent 的表示。（Lecture 3, slide 11）

## 下一步

- 上一页：[[CEG5302-Lecture02-CanonicalGA与手算示例]]
- 下一页：[[CEG5302-Lecture03-Binary与Integer表示]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：`Lecture 3-Representation and Variation_27Aug2026.pdf`，slides 4–11。
- 2026-09-03：从 Lecture 3 拆出“表示的概念与选择准则”短页。
