# EA 七大组件

> 本页属于：CEG5302 / Lecture 02
>
> 前置知识：[[CEG5302-Lecture02-Computational-Complexity-and-EC-Motivation]]
>
> 预计阅读时间：8 分钟

> 预计阅读时间：11 分钟

## 🎯 学习目标（Learning Objectives）

学完本页，你应该能：

1. 默写 EA 的七大组件，并说出每个组件在循环里的作用。
2. 解释「representation 的作用是 phenotype↔genotype 的可逆映射」，并给出 phenotype/genotype/gene/allele 的定义与同义词。
3. 说明 population 是 **multiset**、diversity 为什么不止一个度量。
4. 区分 recombination（n 元）与 mutation（一元）在不同 EA（GA/GP/EP）里的角色。
5. 列举 termination condition 的常见形式，并理解“低 diversity/停滞 ≠ 找到全局最优”。

## 基本结构与七大组件

> 📘 先复习 EC metaphor（slides 9–11）：
> - **自然进化**：种群在资源有限的环境中竞争存活与繁殖；环境适应能力与竞争力决定个体的 fitness；**只有最适应者存活/繁殖（带有随机性，不是完全完美）**。
> - **遗传学是自然进化的微观视角**：每个个体有**表型（phenotype，外部属性）**与**基因型（genotype，内部属性）**双重属性；表型由基因编码（如身高由基因编码）；表型变异由基因变异引起。**allele 是某个 gene 能取的一个值**。
> - **繁殖**：个体可有一个父代（无性）或两个父代（有性）；**子代组合父代基因，但组合并不完美，会受 mutation 影响** → 基因型变异造成表型/ fitness 变化 → 再经受选择（更好的个体有更高概率繁殖/存活）。

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

![EA 基本结构](assets/CEG5302/fig-002-ea-structure.png)

**图：** EA 基本结构——初始随机种群 → 评估 → 父代选择 → 重组/变异产生后代 → 后代评估 → 生存选择形成新一代，循环直至满足终止条件。

*来源：Lecture 2b-EA components_20Aug2026.pdf，第 8 页；核对 2026-09-07。*

### 图意解析（Figure Meaning）

- **`Given objective function to be maximised`**：先确定目标（课件默认最大化；最小化可乘 -1 转换）。
- **`Initialise a population of random candidate solutions` → `Evaluation Function` → `Quantify quality of each individual`**：随机初始化并计算 fitness。
- **`Parent Selection` → `Choose parent(s) with higher fitness as seeds for next generation`**：从种群选出 mating pool（较好个体概率更高）。
- **`Recombination and/or mutation` → `Offsprings generated` → `Evaluation Function`**：生成并评估后代。
- **`Survivor Selection`（`Age/fitness-based competition`）→ `New population`**：决定下一代。
- **`Repeat until max. fitness reaches required quality`**：直到满足终止条件。

| 组件 | 课件页 | 作用 |
|---|---|---|
| Representation | 19–23 | 定义个体（genotype），phenotype→genotype 的可逆映射 |
| Evaluation function | 24–25 | 量化个体质量，指导选择 |
| Population | 26–30 | genotype 的多重集，随代数演化分布 |
| Parent selection | 31–34 | 从种群选出 mating pool |
| Variation operators | 35–45 | recombination（n 元）与 mutation（一元） |
| Survivor selection | 46–48 | 确定下一代（replacement） |
| Termination condition | 49–52 | 何时停止 |

### EA 有哪些变体（slide 12）

课件列举：**Evolutionary Strategies, Evolutionary Programming, Genetic Algorithm, Genetic Programming, Differential Evolution**。虽然编码/算子不同，但有**共同特征**构成基本结构；细节留待后面讲次。

### 为什么 EA 是随机的

EA 在每一环节都引入随机性（Lecture 2b, slides 30, 33, 38, 43, 48, 51）：随机初始化、概率性 parent selection、随机的 crossover 点与 mutation 位、随机 survivor。因此同一问题、同一配置，两次运行结果可能不同。这种随机性正是“探索新区域”的来源；开发者需要靠多次运行与统计来评估稳定性，而不是指望一次运行就得到全局最优。

伪代码（依据 slides 29–36 整理；核对 2026-09-07）：

```text
P ← 随机初始化并评估
while 终止条件未满足:
    M ← parent_selection(P)          # 概率性，允许重复
    O ← 用 M 做 recombination / mutation 生成
    评估 O
    P ← survivor_selection(P ∪ O)    # 固定规模 μ
```

## Representation：phenotype 与 genotype

- **Phenotype**：原问题领域中的 candidate solution。
- **Genotype / chromosome**：EA 实际操作的编码。
- **Gene / position / variable**：genotype 的一个组成部分。
- **Allele**：某个 gene 可以取的一个值。

**同义词对照（slide 23）**：`Individual / phenotype / candidate solution` 等价；`Genotype / chromosome / individual` 等价；`Elements of individual / variable / position / gene / allele` 等价。

Representation 是 phenotype space 到 genotype space 的映射，应当可逆（invertible）。课件指出它处理的是 **genotype space 的数据结构**，而非实际映射关系本身（slide 21）：例如把整数 `08` 映射成 `0000 1000`。两个整数变量 `(height, weight)=(2,4)` 可各用 5 bits 编码为 `00010 00100`；`(5,7)` → `00101 00111`。EA 结束时需把最优 genotype decode 回问题领域得到 phenotype。**phenotype space 与 genotype space 非常不同**；最佳 phenotype 是在终止后解码 best genotype 得到的。（Lecture 2b, slides 19–23）

## Evaluation function

Evaluation/fitness function 把问题需求转换为数值质量，用于 selection 并推动 population quality 随时间变化。它在语义上来自 phenotype，但实现时可以先 decode genotype；minimization/maximization 的约定必须与 selection 方法一致。（Lecture 2b, slides 24–25）

> 🧪 课件示例（slide 25）：以 $f(x)=x^4$ 为 fitness function，则 $x=2 \to f=16$，$x=3 \to f=81$。**最小化可转最大化、反之亦然。**

## Population

Population 是 genotype 的 **multiset**（允许重复个体）。Individual 本身是静态编码，population 的分布随 generations 改变。（Lecture 2b, slides 26–27）

- **Diversity** 可用 unique genotypes、unique phenotypes、unique fitness values、entropy 或领域距离衡量；这些指标不等价。（slide 28）
- **为什么不等价**（slide 28 的含金量）：`1 fitness value ≠ 1 phenotype`；`1 phenotype ≠ 1 genotype`；**`1 genotype = 1 phenotype = 1 fitness value`**。所以“数 unique fitness”不等于“数 unique phenotype”，更不等于“数 unique genotype”。
- 初始化通常从 search space 随机采样，有时用问题相关知识提高初始 fitness。（Lecture 2b, slides 29–30）

## Parent selection

Parent selection 在 population 层面运行，产生 mating pool。质量较好的个体通常有更高繁殖概率，但低质量个体仍应有非零机会，避免完全贪心导致过早陷入 local optimum。（Lecture 2b, slides 31–34）

## Variation operators

- **Recombination/crossover**：n-ary operator（两个或更多 parents → 一个或多个 offspring），是 GA/GP 的核心、EP 中不使用。
- **Mutation**：unary operator（一个 parent → 小幅随机修改），是 EP 的主要变化来源；recombination 重组已有 building blocks，mutation 可引入父代中不存在的新 allele。（Lecture 2b, slides 35–45）

## Survivor selection 与 termination

- **Survivor selection（replacement）** 决定下一代 population，通常维持固定 size；可按 fitness、age、parents+offspring 或 offspring-only 选择。Parent selection 通常是 stochastic，survivor selection 很多时候是 deterministic（但非必然）。（Lecture 2b, slides 46–48）
- **Termination condition** 包括 CPU-time budget、最大 fitness evaluation 数、连续若干代 improvement 小于阈值、population diversity 低于阈值、达到已知目标质量；可 OR 组合多个条件。低 diversity 或停滞表示搜索可能收敛，但不证明找到 global optimum。（Lecture 2b, slides 49–52）

> 📘 **“何时停”的理想 vs 现实（slide 51）**：理想是**达到已知全局最优**，或**在容差 $\epsilon > 0$ 内接近全局最优**。但实践中**我们往往永远达不到**——否则算法就**永远不会停**！所以实际用上面那些“实用终止条件”替代。

**伪代码（依据 slides 29–36 整理；核对 2026-09-07）：**

```text
P ← 随机初始化并评估
while 终止条件未满足:
    M ← parent_selection(P)                 # 概率性，允许重复
    O ← 用 M 做 recombination / mutation 生成
    评估 O
    P ← survivor_selection(P ∪ O)           # 固定规模 μ
```

## Exam Checklist（考试自查）

- **必须理解**：七大组件各自的职责；recombination 与 mutation 在不同 EA 中的角色；population 为何是 multiset；diversity 度量的不等价。
- **必须记忆**：phenotype/genotype/gene/allele 定义与同义词；`1 genotype = 1 phenotype = 1 fitness`；termination condition 常见形式（预算/评估数/停滞/多样性/已知目标）。
- **必须手算**：$f(x)=x^4$（$x=2 \to 16, x=3 \to 81$）与 `(height,weight)` 的 5-bit 编码。
- **了解即可**：各 EA 变体细节（GA/ES/EP/GP/DE 的具体差异）。
- **明确 out of scope**：本讲不要求实现 EA，也不证明低多样性≠全局最优。

## 下一步

- 上一页：[[CEG5302-Lecture02-Computational-Complexity-and-EC-Motivation]]
- 下一页：[[CEG5302-Lecture02-Canonical-GA-Worked-Example]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 2b-EA components_20Aug2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.2b-EA.components_20Aug2026.pdf)，slides 8–52；配图取自第 8 页。
- 2026-09-03：从 Lecture 2b 拆出“EA 七大组件”短页。
- 2026-09-07：嵌入 EA 基本结构原图（第 8 页）、新增七大组件功能对照表。
- 2026-09-09：新增学习目标；补充 EC metaphor/遗传学（表型/基因型/allele）、EA 变体列表、图意解析（每节点含义）、representation 同义词与编码示例、`f=x^4` 示例、diversity 度量“1 genotype=1 phenotype=1 fitness”、“何时停”理想/现实；新增 Exam Checklist。
