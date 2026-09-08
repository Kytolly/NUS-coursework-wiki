# 自然进化隐喻与基本循环

> 本页属于：CEG5302 / Lecture 01
>
> 前置知识：[[CEG5302-Lecture01-进化计算导论]]
>
> 预计阅读时间：7 分钟

## 自然进化的计算隐喻

课件采用的简化 Darwin 机制包括三部分：（Lecture 1, slides 17–21）

1. **带遗传的繁殖（reproduction with inheritance）**：后代保留父代特征。
2. **变异（variation）**：个体之间存在差异，并可能产生新特征。
3. **选择（selection）**：有利特征更可能存活并繁殖。

在算法中，它们分别对应候选解的编码/继承、变异与重组算子、以及基于 fitness 的选择。选择是概率性的，不是“只有当前最优个体才能繁殖”的绝对规则。

## 基本进化循环

课件用包含头部大小、四肢和躯干等属性的 chromosome 表示个体。一般循环为：（Lecture 1, slides 22–32）

![EC 基本循环/个体示意图](assets/CEG5302/fig-001-ec-basic-loop.png)

**图：** EC 基本循环示意——随机初始化并评估种群 → 选择 → 修改（变异/重组）→ 评估后代 → 淘汰较差成员，循环直至终止。图中还展示个体由 head、torso、四肢等属性构成的 chromosome。

*来源：Lecture 1 - Introduction (D Srinivasan) 13Aug26.pdf，第 23 页；核对 2026-09-07。*

三要素与算子的对应关系（Lecture 1, slides 18, 23–32）：

| 自然进化机制 | 计算对应 | 课件页 |
|---|---|---|
| Reproduction with inheritance | 编码/继承（后代保留父代结构） | 18, 23 |
| Variation | 变异（mutation）+ 重组（recombination） | 27–30 |
| Selection | 基于 fitness 的父代/生存选择 | 26, 32 |

通用循环伪代码（依据课件第 23–32 页整理；核对 2026-09-07）：

```text
P ← 随机初始化 μ 个个体的种群
for t = 1,2,...:
    评估每个个体 quality/fitness
    按 fitness（概率性）选 parents 进入 mating pool
    对 parents 施加 crossover（2 个父代）与 mutation（1 个父代）
    评估 offspring
    从 parents + offspring 中选出 μ 个 survivors
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

### 为什么“选择是概率性的”很重要

课件强调 selection 是概率性的，而不是“只有当前最优个体才能繁殖”的绝对规则（Lecture 1, slides 19, 26）。若总是只让最优个体繁殖，虽然单代提升快，但很快会失去种群多样性、陷在同一区域（过早收敛）。保留较小概率让较差个体繁殖，相当于给算法保留“翻盘”的探索机会。这与第 4 讲“低质量个体必须有非零被选概率”呼应（见 [[CEG5302-Lecture04-SurvivorSelection与选择压力]]）。

## 与后续讲次的衔接

- 本循环在第 2 讲被形式化为 EA 七大组件与 `input → model → output` 的问题分类（见 [[CEG5302-Lecture02-EA七大组件]]）。
- “选择”在第 4 讲展开为 parent/survivor selection 与 selection pressure（见 [[CEG5302-Lecture04-SurvivorSelection与选择压力]]）。

## 下一步

- 上一页：[[CEG5302-Lecture01-进化计算导论]]
- 下一页：[[CEG5302-Lecture01-四类问题与工程应用]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 1 - Introduction (D Srinivasan) 13Aug26.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.1.-.Introduction.D.Srinivasan.13Aug26.pdf)（扫描版），slides 17–32；slide 引用以个人笔记 `notes/lecture/lecture-01-introduction-zh.md` 记录为准；配图取自第 23 页。
- 2026-09-03：从 Lecture 1 拆出“自然进化隐喻与基本循环”短页。
- 2026-09-07：嵌入 EC 基本循环原图（第 23 页）、新增三要素对应表与通用循环伪代码。
