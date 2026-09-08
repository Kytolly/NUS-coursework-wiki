# Real 表示的变异

> 本页属于：CEG5302 / Lecture 03
>
> 前置知识：[[CEG5302-Lecture03-Binary与Integer表示]]
>
> 预计阅读时间：10 分钟

## Real / Floating-point 表示

染色体为实值向量 `[x1, ..., xn]`，`xi ∈ ℝ`，用于连续 decision variables（如吊臂长度与缆绳长度）。mutation 把 `[x1..xn]` 变为 `[x1'..xn']`，各分量有下/上界 `[Li, Ui]`。（Lecture 3, slides 33–36）

## Real 表示的变异技术总览

（自制，依据课件第 36–52 页；核对 2026-09-07）

```mermaid
flowchart TD
  A[Real 变异<br/>x_i ∈ [L_i, U_i]] --> B[Uniform mutation<br/>x_i' 从 [L_i,U_i] 均匀采样]
  A --> C[Non-uniform mutation<br/>小改动为主]
  A --> D["Polynomial mutation (PM)"]
  A --> E[Self-adaptive mutation<br/>σ 进染色体]
  C --> C1[Gaussian<br/>均值 0, 用户 σ]
  C --> C2[Cauchy<br/>更厚尾部, 大改动更多]
  E --> E1[单步长<br/>1 个 σ]
  E --> E2[n 步长<br/>每维 σ_i]
  E1 --> E3[Correlated<br/>旋转坐标]
  E2 --> E3
```

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

**数值示例（PM）**：设 `x_i=0.5`，`x_i^L=0`，`x_i^U=1`，`η_m=2`。若 `u_i=0.5`，则 `a_i=1-(2(1-0.5))^(1/3)=1-1^(1/3)=0`，`x_i'=0.5`（不变）。若 `u_i=0.1`，则 `a_i=(2×0.1)^(1/3)-1=0.2^(1/3)-1≈0.585-1=-0.415`，`x_i'=0.5+1×(-0.415)=0.085`。可见 `η_m` 越大，后代越集中在父代附近（小改动更常见）。（依据 slide 41 公式演算，自拟数值）

**数值示例（Gaussian non-uniform）**：设 `σ=0.1`、`x_i=0.5`，抽样 `N(0,0.1)=+0.04`，得 `x_i'=0.54`（需再裁剪到 `[L_i,U_i]`）。因为约 2/3 采样落在 ±1 个 σ 内，多数改动是小量；但尾部非零，仍可能产生接近 `3σ=0.3` 的大跳跃。（依据 slides 38–40 演算）

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

## Real 变异方式小结

（依据课件第 36–52 页整理；核对 2026-09-07）

| 方式 | 是否需 mutation 概率 | 步长/参数 | 主要特点 |
|---|---|---|---|
| Uniform | 是（逐位置） | 无额外参数 | 完全随机重置到区间内 |
| Non-uniform (Gaussian/Cauchy) | 可设为 1（σ 即步长） | σ | 小改动为主，尾部可大改 |
| Polynomial (PM) | 是 | `η_m` | 控制大小改动分布 |
| Self-adaptive (1/n step) | 否（σ 进染色体） | σ 或 σ_i | 自适应探索/开发 |
| Correlated | 否 | 旋转矩阵 | 沿 landscape 最陡方向 |

**选择思路**：若不知道各维敏感度差异，先用单步长 self-adaptive；若问题维数低、想要更强适应，可升级到 n 步长或 correlated。σ 过大会让搜索跳来跳去、难以精炼；σ 过小则探索不足，可能早熟。（依据 slides 43–52 的思想整理）

## 下一步

- 上一页：[[CEG5302-Lecture03-Binary与Integer表示]]
- 下一页：[[CEG5302-Lecture03-Real表示的重组]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 3-Representation and Variation_27Aug2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.3-Representation.and.Variation_27Aug2026.pdf)，slides 33–52。
- 2026-09-03：从 Lecture 3 拆出“Real 表示的变异”短页。
- 2026-09-07：新增 Real 变异技术总览 Mermaid 图与 PM、Gaussian 数值示例。
