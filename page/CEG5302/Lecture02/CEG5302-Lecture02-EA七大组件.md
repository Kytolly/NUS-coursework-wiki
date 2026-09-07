# EA 七大组件

> 本页属于：CEG5302 / Lecture 02
>
> 前置知识：[[CEG5302-Lecture02-计算复杂度与进化计算动机]]
>
> 预计阅读时间：8 分钟

## 基本结构与七大组件

不同 EA 变体虽使用不同的 representation、operators 和 selection policies，但共享以下循环：（Lecture 2b, slides 8–18）

```text
initialize population
        |
        v
evaluate individuals
        |
        v
select mating pool -- recombination/mutation --> offspring
        |                                       |
        +----------- survivor selection <-------+
                            |
                            v
                     next population
                            |
                     termination test
```

七大组件为：representation、evaluation function、population、parent selection、variation operators（recombination + mutation）、survivor selection、termination condition。（Lecture 2b, slide 18）

## Representation：phenotype 与 genotype

- **Phenotype**：原问题领域中的 candidate solution。
- **Genotype / chromosome**：EA 实际操作的编码。
- **Gene / position / variable**：genotype 的一个组成部分。
- **Allele**：某个 gene 可以取的一个值。

Representation 是 phenotype space 到 genotype space 的映射，应当可逆（invertible）。例如两个整数变量 `(height, weight)=(2,4)` 可各用 5 bits 编码为 `00010 00100`。EA 结束时需把最优 genotype decode 回问题领域得到 phenotype。（Lecture 2b, slides 19–23）

## Evaluation function

Evaluation/fitness function 把问题需求转换为数值质量，用于 selection 并推动 population quality 随时间变化。它在语义上来自 phenotype，但实现时可以先 decode genotype；minimization/maximization 的约定必须与 selection 方法一致。（Lecture 2b, slides 24–25）

## Population

Population 是 genotype 的 **multiset**（允许重复个体）。Individual 本身是静态编码，population 的分布随 generations 改变。（Lecture 2b, slides 26–27）

- **Diversity** 可用 unique genotypes、unique phenotypes、unique fitness values、entropy 或领域距离衡量；这些指标不等价，因为多个 genotype 可能对应同一 phenotype，不同 phenotype 也可能有相同 fitness。（Lecture 2b, slide 28）
- 初始化通常从 search space 随机采样，有时用问题相关知识提高初始 fitness。（Lecture 2b, slides 29–30）

## Parent selection

Parent selection 在 population 层面运行，产生 mating pool。质量较好的个体通常有更高繁殖概率，但低质量个体仍应有非零机会，避免完全贪心导致过早陷入 local optimum。（Lecture 2b, slides 31–34）

## Variation operators

- **Recombination/crossover**：n-ary operator（两个或更多 parents → 一个或多个 offspring），是 GA/GP 的核心、EP 中不使用。
- **Mutation**：unary operator（一个 parent → 小幅随机修改），是 EP 的主要变化来源；recombination 重组已有 building blocks，mutation 可引入父代中不存在的新 allele。（Lecture 2b, slides 35–45）

## Survivor selection 与 termination

- **Survivor selection（replacement）** 决定下一代 population，通常维持固定 size；可按 fitness、age、parents+offspring 或 offspring-only 选择。Parent selection 通常是 stochastic，survivor selection 很多时候是 deterministic（但非必然）。（Lecture 2b, slides 46–48）
- **Termination condition** 包括 CPU-time budget、最大 fitness evaluation 数、连续若干代 improvement 小于阈值、population diversity 低于阈值、达到已知目标质量；可 OR 组合多个条件。低 diversity 或停滞表示搜索可能收敛，但不证明找到 global optimum。（Lecture 2b, slides 49–52）

## 下一步

- 上一页：[[CEG5302-Lecture02-计算复杂度与进化计算动机]]
- 下一页：[[CEG5302-Lecture02-CanonicalGA与手算示例]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 2b-EA components_20Aug2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture%202b-EA%20components_20Aug2026.pdf)，slides 8–52。
- 2026-09-03：从 Lecture 2b 拆出“EA 七大组件”短页。
