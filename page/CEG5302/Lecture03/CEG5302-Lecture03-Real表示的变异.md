# Real 表示的变异

> 本页属于：CEG5302 / Lecture 03
>
> 前置知识：[[CEG5302-Lecture03-Binary与Integer表示]]
>
> 预计阅读时间：10 分钟

## Real / Floating-point 表示

染色体为实值向量 `[x1, ..., xn]`，`xi ∈ ℝ`，用于连续 decision variables（如吊臂长度与缆绳长度）。mutation 把 `[x1..xn]` 变为 `[x1'..xn']`，各分量有下/上界 `[Li, Ui]`。（Lecture 3, slides 33–36）

## Uniform mutation

`xi'` 从 `[Li, Ui]` 均匀采样，通常配合逐位置 mutation 概率。（slides 36–37）

## Non-uniform mutation

以小幅变化为主（类似整数 creep）。（slides 38–42）

- **Gaussian**：在当前值上加一个均值 0、用户指定标准差的 Gaussian 量，必要时裁剪到 `[Li, Ui]`。约 2/3 采样落在 ±1 个标准差内（多为小变化），但尾部非零，故仍有概率产生大变化。
- **Cauchy**：尾部比 Gaussian 更厚，增大出现大 mutation 的概率。
- 标准差即 **mutation step size**，本身已是变异幅度的控制参数，故不必再设 mutation 概率（或设为 1）。

### Polynomial mutation

（slides 40–41）

```
x'_i = x_i + (x_i^U - x_i^L) · δ_i
```

其中 `u_i ∈ [0,1]`，`η_m`（polynomial distribution index）是用户参数：

```
δ_i = (2u_i)^(1/(η_m+1)) - 1            (u_i < 0.5)
δ_i = 1 - (2(1-u_i))^(1/(η_m+1))        (u_i ≥ 0.5)
```

## Self-adaptive mutation

把 step size 本身放进 chromosome，让它随 EA 一起经历 variation 与 selection；先修改 step size，再用它重新生成 decision variables。（slide 42）

### Uncorrelated mutation

**单步长（one step size）**：所有分量共用一个控制参数 σ，每代更新：（slides 43–45）

```
σ' = σ · e^(τ·N(0,1))
x'_i = x_i + σ'·N_i(0,1)
τ ∝ 1/√n
```

用 lognormal 乘子是因为：小修改应比大修改更常见、σ 必须 > 0、中位数应为 1、且 mutation 平均中立（抽到某值与它的倒数等概率）。σ 需设下界 `ε_0` 避免几乎为零；`τ` 可类比神经网络中的 learning rate。

**n 步长（n step sizes）**：每个维度独立步长，使 fitness 变化更陡的维度获得更大 mutation：（slides 46–49）

```
σ'_i = σ_i · e^(τ'·N(0,1) + τ·N_i(0,1))
x'_i = x_i + σ'_i·N_i(0,1)
τ' ∝ 1/√(2n)，τ ∝ 1/√(2√n)
```

二维 fitness landscape 说明：单步长时所有方向 mutation 概率相同，n 步长时椭圆沿敏感维度拉伸。

### Correlated mutation

进一步允许坐标系统旋转，使 mutation 沿 landscape 最陡方向最有效；课件明确“不展示数学推导”。（slides 50–52）

## 下一步

- 上一页：[[CEG5302-Lecture03-Binary与Integer表示]]
- 下一页：[[CEG5302-Lecture03-Real表示的重组]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：`Lecture 3-Representation and Variation_27Aug2026.pdf`，slides 33–52。
- 2026-09-03：从 Lecture 3 拆出“Real 表示的变异”短页。
