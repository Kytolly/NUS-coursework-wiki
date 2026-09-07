# 种群管理模型与 FPS 及 Ranking

> 本页属于：CEG5302 / Lecture 04
>
> 前置知识：[[CEG5302-Lecture03-Tree表示与Crossover一般结论]]
>
> 预计阅读时间：10 分钟

## 复习与两种种群管理模型

本讲讨论 **selection（parent 与 survivor）**——它对表示是 agnostic 的——以及如何维持种群多样性。（Lecture 4, slides 5–6）

两类种群管理模型：（slides 7–11）

1. **Generational（代际）**：整代 population 在下一代被全部替换（Simple GA 的方式）。注意 Simple GA 中初始种群、mating pool 与 offspring 数量相同，但并非所有 EA 都如此；例如 Evolution Strategies 的 **(μ,λ)** 策略里 μ≠λ（如 μ/λ = 5/7）。（slides 9–10）
2. **Steady-state（稳态）**：每代只替换一部分个体，λ 个旧个体被 offspring 替换；**generation gap** 指被替换的比例，研究中常取 λ=1。（slide 11）

Selection 出现在两处：parent selection 与 survivor selection。（slide 12）

## Fitness-proportional selection（FPS）

个体 i 的选中概率 `p_i = f_i / Σ_j f_j`，基于绝对 fitness（Simple GA 与手算都用它）。（slides 13–14）

它的问题：（slide 15）

- 杰出个体迅速占据种群，导致 premature convergence 到局部区域/local minimum；
- 一旦所有个体 fitness 接近，selection pressure 变低，随机选择占主导，后期提升缓慢；
- **Transposing 问题**：对 fitness function 做平移（如加常数）会显著改变相对 selection probability，尽管 optimum 位置不变。

### 解决平移问题

（slide 16）

- **Windowing**：从每个 fitness 减去某值 β（如当代最小 fitness，或过去若干代移动平均以减少波动）。
- **Sigma scaling**：`f'(x) = max(f(x) - (f̄ - c·σ_f), 0)`，常数 c 通常取 2。

## Ranking selection

按 fitness 排序后，基于**名次**而非绝对值分配概率，从而保持恒定的 selection pressure（最差个体 rank 0，最优个体 rank μ-1）。映射可线性或指数，所有概率之和必须为 1。（slides 17–19）

- **线性映射**：设参数 s 为最优个体期望分配的 offspring 数（1 < s ≤ 2），rank i 的概率：

```
P(i) = (2-s)/μ + 2i(s-1)/(μ(μ-1))
```

第一项对所有个体恒定（保证 ΣP=1），第二项在最差个体（i=0）处为 0。中位 fitness 个体有 1 次繁殖机会；s > 2 会使部分概率为负，因此 s 上限为 2，selection pressure 受限。（slides 20–23）

- **指数映射**：`P(i) = (1 - e^(-i))/c`（c 为归一化常数），比线性映射给出更高 selection pressure。（slide 24）

## 下一步

- 上一页：[[CEG5302-Lecture03-Tree表示与Crossover一般结论]]
- 下一页：[[CEG5302-Lecture04-RWS与Tournament等选择]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 4-Selection and Population management_03Sept2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture%204-Selection%20and%20Population%20management_03Sept2026.pdf)，slides 5–24。
- 2026-09-03：从 Lecture 4 拆出“种群管理模型与 FPS 及 Ranking”短页。
