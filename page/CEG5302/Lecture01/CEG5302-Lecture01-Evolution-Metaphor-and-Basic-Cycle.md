# 自然进化隐喻与基本循环

> 本页属于：CEG5302 / Lecture 01
>
> 前置知识：[[CEG5302-Lecture01-Introduction-to-EC]]
>
> 预计阅读时间：7 分钟

> 预计阅读时间：11 分钟

## 🎯 学习目标（Learning Objectives）

学完本页，你应该能：

1. 复述 Darwin 进化的三个必要条件（Variation + Inheritance + Selection = Evolution），并对应到 EA 的计算概念。
2. 解释课件用“染色体（head / 左右臂 / torso / 左右腿）”做个体、用数值 `300/220/200` 等演示一代演化的完整过程。
3. 讲出“为什么选择必须是概率性的”（否则 premature convergence）。
4. 用一个具体动机例子（壁虎/鞋底材料）说明“把进化当作求解模型”的合理性。
5. 说明图 1 中每一条箭头/节点在循环里的作用。

## 自然进化的计算隐喻

> 📘 背景：课件先讲“自然进化是自然界最强大、最有创造力（most powerful and creative process in nature）的过程”，并强调它是**缓慢而渐进的**——生命在成千上万年里适应与变化，**小的变化在世代间累积，最终导致物种的显著改变**。（Lecture 1, slides 15–16）

课件引用 Darwin《Origin of Species（1859）》来说明选择发生的机制（Lecture 1, slide 17）：

> “As many more individuals of each species are born than can possibly survive; and as, consequently, there is a frequently recurring struggle for existence, it follows that any being, if it vary however slightly in any manner profitable to itself … will have a better chance of surviving, and thus be naturally selected. From the strong principle of inheritance, any selected variety will tend to propagate its new and modified form.”

💡 关键理解：**变异的个体必须“比别的个体更能活到繁殖”**，并且**这个有利特征能被遗传下去**——两头都成立，选择才能积累出变化。这就是“survival of the fittest”。课件还举了新突变的具体形式：更长的脖子、更长的腿、更厚的皮肤、更长的妊娠期、更大的脑、皮肤上感光的小斑、一块无害的“松骨”等。（Lecture 1, slide 19）

课件采用的简化 Darwin 机制包括三部分 —— 即 **Universal Darwinism 的“食材”**（Lecture 1, slides 17–21）：

1. **带遗传的繁殖（reproduction with inheritance）**：后代保留父代特征。
2. **变异（variation）**：个体之间存在差异，并可能产生新特征。
3. **选择（selection）**：有利特征更可能存活并繁殖。

```text
Variation + Inheritance + Selection = Evolution   （课件原文，slide 18）
```

在算法中，它们分别对应候选解的编码/继承、变异与重组算子、以及基于 fitness 的选择。选择是概率性的，不是“只有当前最优个体才能繁殖”的绝对规则。

### 一个动机：壁虎爬山 vs 人类没解决的鞋底材料问题

> 📘 Source（Lecture 1, slide 20，题目：“Evolution as Problem Solving Approach”）：**问题——设计一种靴子鞋底材料，能让你沿光滑的垂直砖墙上走。**
> 我们还没解决这个问题……**但自然界已经解决了：壁虎！** 壁虎有粘性脚趾，能爬墙、甚至倒挂在天花板。经过数百万年，它们进化出这种能力，得以在恶劣环境中获取食物、躲避捕食者。

💡 这个例子说明 EC 的核心思想：**不要直接“设计”解，而是让“解”在种群中经过变异/重组/选择被演化出来。** 自然界用“漫长世代 + 选择”发现了人类工程师还没想到的壁虎脚趾结构，这正是 EC 想借用“演化搜索”而非“逐步构造”来求解复杂问题的原因。

## 基本进化循环

课件用包含头部大小、四肢和躯干等属性的 chromosome 表示个体。一般循环为：（Lecture 1, slides 22–32）

![EC 基本循环/个体示意图](assets/CEG5302/fig-001-ec-basic-loop.png)

**图：** EC 基本循环示意——随机初始化并评估种群 → 选择 → 修改（变异/重组）→ 评估后代 → 淘汰较差成员，循环直至终止。图中还展示个体由 head、torso、四肢等属性构成的 chromosome。

*来源：Lecture 1 - Introduction (D Srinivasan) 13Aug26.pdf，第 23 页；核对 2026-09-07。*

### 图意解析（Figure Meaning）

- **左侧 `initiate population & evaluate`**：随机生成候选解，并算每个个体的 quality/fitness。
- **中间 `selection` → `parents`**：按 fitness 挑出用于繁殖的父代（概率性）。
- **右侧 `modification` → `modified offspring`**：对父代做 recombination / mutation，产生子代。
- **下方 `evaluation` → `evaluated offspring`**：重新评估子代 fitness。
- **底部 `discard` / `deleted members`**：淘汰较差成员，恢复目标种群大小。
- **环回**：进入下一代，直到终止条件。
- **`Chromosome` 示意**（head size / left & right arm / torso / left & right leg）：说明个体在 genotype 空间被编码成一段有结构的字符串，而不是一个抽象“点”；每个“属性”就是一个 gene，取值就是 allele。

三要素与算子的对应关系（Lecture 1, slides 18, 23–32）：

| 自然进化机制 | 计算对应 | 课件页 |
|---|---|---|
| Reproduction with inheritance | 编码/继承（后代保留父代结构） | 18, 23 |
| Variation | 变异（mutation）+ 重组（recombination） | 27–30 |
| Selection | 基于 fitness 的父代/生存选择 | 26, 32 |

通用循环伪代码（依据课件第 23–32 页整理；核对 2026-09-07）：

```text
P ← 随机初始化 $\mu$ 个个体的种群
for t = 1,2,...:
    评估每个个体 quality/fitness
    按 fitness（概率性）选 parents 进入 mating pool
    对 parents 施加 crossover（2 个父代）与 mutation（1 个父代）
    评估 offspring
    从 parents + offspring 中选出 $\mu$ 个 survivors
    若满足 termination condition，退出
```

```text
初始化并评估 population
         |
         v
选择 parents -> modification/recombination -> 评估 offspring
  ^                                             |
  |                                             v
  +--------- 保留 survivors / 丢弃较差成员 <-----+
                         |
                         +---- 重复直到终止
```

具体步骤：

1. 随机生成初始 population。
2. 在环境中评估每个 individual，并计算质量或 fitness。
3. 让质量较好的个体获得更高的选择概率。
4. 通过父代重组生成 offspring。
5. 以概率方式进行 mutation，增加新的变化。
6. 重新评估 offspring。
7. 进行 survivor selection，丢弃其余成员，使下一代恢复目标 population size。
8. 直到满足 termination condition。

生成 offspring 后，临时群体可能比目标 population 大，因为 parents 与 offspring 可以先共存；population size 只会在 discard/replacement 步骤后恢复。（Lecture 1, slides 27–32）

### 一代演化的完整手算示例（slides 23–32）

> 🧪 本示例是课件第 23–32 页的**逐帧演示**：个体用 chromosome（`head size / left arm / right arm / torso / left leg / right leg`）表示，fitness 用数值（如 300/220/200）表示，便于跟手。以下数字取自课件图示。

**第 1 步：初始化并评估。** 随机生成 3 个个体 A、B、C，并各自在“环境”中评估得到 fitness：

| 个体 | Chromosome（示意） | Fitness |
|---|---|---|
| A | head size / left arm / right arm / torso / left leg / right leg | 300 |
| B | 同上 | 220 |
| C | 同上 | 200 |

**第 2 步：选择。** fitness 高的个体有更高概率被选为 parent，但选择是**概率性**的（不是只留最优）。（slide 26）

**第 3 步：重组生成新个体。** 课件演示了在染色体上**选一个 crossover point、交换基因**（slide 27）。例如把 A 与 B、A 与 C、B 与 C 分别组合，得到多个 offspring，构成**新的 offspring population**。课件提问：**“现在种群里有几个个体？”**——因为 parents 与 offspring 先共存，临时群体数量会增加。（slide 28–29）

**第 4 步：变异生成全新个体。** 随机选一个个体，对其 chromosome 的**一个 gene 做 mutation**（slide 30）。注意：重组只是交换已有基因；**mutation 才会创造出父代里不存在的“全新个体/基因型”**，这是探索新区域的关键。

**第 5 步：重新评估整个种群。** 再次计算所有个体（包括重组出的 offspring 与变异出的新个体）的 fitness（slide 31）。课件给出的示例值包括：`300, 220, 200, 170, 320, 230, 240, 190, 310`——即有高有低、有起有伏。

**第 6 步：淘汰较差个体，保留 top 6。** 从临时群体中**保留 fitness 最好的 6 个**作为下一代（slide 32）。

**第 7 步：循环。** 过程不断重复，直到终止条件满足；经过很多代后，我们得到一组“优异解”（excellent solutions）。（slide 32）

> 💡 这段手算说明三件事：(a) 种群在早期是**散布**的，随着演化才聚向峰；(b) 一代内的最佳 fitness 可能**起伏**（100→….→170→320…），单代波动不代表算法失败；(c) **重组 vs 变异**分工不同——重组组合已有块，变异创造新值，二者都对多样性必不可少。

### 为什么“选择是概率性的”很重要

课件强调 selection 是概率性的，而不是“只有当前最优个体才能繁殖”的绝对规则（Lecture 1, slides 19, 26）。若总是只让最优个体繁殖，虽然单代提升快，但很快会失去种群多样性、陷在同一区域（过早收敛）。保留较小概率让较差个体繁殖，相当于给算法保留“翻盘”的探索机会。这与第 4 讲“低质量个体必须有非零被选概率”呼应（见 [[CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure]]）。

## 与后续讲次的衔接

- 本循环在第 2 讲被形式化为 EA 七大组件与 `input → model → output` 的问题分类（见 [[CEG5302-Lecture02-EA-Seven-Components]]）。
- “选择”在第 4 讲展开为 parent/survivor selection 与 selection pressure（见 [[CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure]]）。
- “变异 vs 重组”的分工在第 3 讲按不同 representation 逐一展开（见 [[CEG5302-Lecture03-Representation-Concepts-and-Criteria]]）。

## Exam Checklist（考试自查）

- **必须理解**：三要素 `Variation + Inheritance + Selection = Evolution`；为什么选择是概率性的；重组与变异的分工。
- **必须手算**：用 `300/220/200` 这类数值走完一代（初始化→选择→重组→变异→重评估→淘汰 top 6）。
- **必须记忆**：Darwin 关键句话与“survival of the fittest”；壁虎/鞋底材料动机例子。
- **了解即可**：Darwin 原文的完整措辞、具体 mutation 例子（长颈/长腿/厚皮肤等）。
- **明确 out of scope**：本讲不要求证明“进化一定收敛”或给出变异概率建议。

## 下一步

- 上一页：[[CEG5302-Lecture01-Introduction-to-EC]]
- 下一页：[[CEG5302-Lecture01-Problem-Types-and-Applications]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 1 - Introduction (D Srinivasan) 13Aug26.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.1.-.Introduction.D.Srinivasan.13Aug26.pdf)（扫描版），slides 17–32；slide 引用以个人笔记 `notes/lecture/lecture-01-introduction-zh.md` 记录为准；配图取自第 23 页。
- 2026-09-03：从 Lecture 1 拆出“自然进化隐喻与基本循环”短页。
- 2026-09-07：嵌入 EC 基本循环原图（第 23 页）、新增三要素对应表与通用循环伪代码。
- 2026-09-09：新增学习目标、Darwin/Universal Darwinism 背景、壁虎动机例子、图意解析（每箭头/节点含义），并新增“一代演化完整手算示例（slides 23–32）”；补 Exam Checklist。
