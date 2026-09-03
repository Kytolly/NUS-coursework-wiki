# Real 表示的重组

> 本页属于：CEG5302 / Lecture 03
>
> 前置知识：[[CEG5302-Lecture03-Real表示的变异]]
>
> 预计阅读时间：9 分钟

## 与 binary/integer 的区别

binary/integer 的 1-point/n-point/uniform crossover 只能传播父代已有的 allele；只有 mutation 能引入新 allele。实数表示下 uniform crossover 的对应物称 **discrete recombination**。（Lecture 3, slides 53–54）

## Intermediate / Arithmetic recombination

`z_i = α·x_i + (1-α)·y_i`，`α ∈ [0,1]`。它能产生新 allele，但只能落在两父代之间，随代数增加 allele 取值范围会因（加权）平均而缩小。三种形式：（slides 55–58）

- **Simple**：取随机切点 k，前 k 个分量来自父代 1，其余分量取平均。
- **Single**：仅在第 k 个分量取平均，其余照抄。
- **Whole**：所有分量并行加权平均。

## Blend recombination（BLX-α）

允许 offspring 略微超出两父代范围。设 `d_i = y_i - x_i`（`x_i < y_i`），child 落在 `[x_i - α·d_i, y_i + α·d_i]`：（slides 59–64）

```
γ = (1+2α)·u - α
z_i = (1-γ)·x_i + γ·y_i
```

父代相距远时 offspring 范围也大（偏 exploration），相距近时 offspring 也在附近（偏 exploitation），因此具有 self-adaptive 特性；研究显示 `α = 0.5` 效果最好，使 child 落在两父代之内/之外的概率相当。

## Simulated Binary Crossover (SBX)

用实数算子模拟 binary 的 1-point crossover（推导超出本课程范围）。与 BLX-α 一样，spread 依赖父代距离，但 offspring 更可能产生**小**变化。给定 `u ∈ [0,1)` 与 distribution index `η_c`：（slides 65–67）

```
β = (2u)^(1/(η_c+1))                 (u ≤ 0.5)
β = (1/(2(1-u)))^(1/(η_c+1))         (u > 0.5)

x' = 0.5·[(1+β)·x + (1-β)·y]
y' = 0.5·[(1-β)·x + (1+β)·y]
```

Offspring 关于两父代对称（不偏向任一父代），且 `offspring2 - offspring1 = β·(parent2 - parent1)`，spread 与父代 spread 成正比。

## 下一步

- 上一页：[[CEG5302-Lecture03-Real表示的变异]]
- 下一页：[[CEG5302-Lecture03-Permutation表示]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：`Lecture 3-Representation and Variation_27Aug2026.pdf`，slides 53–67。
- 2026-09-03：从 Lecture 3 拆出“Real 表示的重组”短页。
