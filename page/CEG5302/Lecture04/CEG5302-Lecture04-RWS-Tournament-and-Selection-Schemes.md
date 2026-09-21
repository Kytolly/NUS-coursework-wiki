# RWS 与 Tournament 等选择

> 本页属于：CEG5302 / Lecture 04
>
> 前置知识：[[CEG5302-Lecture04-Population-Models-FPS-and-Ranking]]
>
> 预计阅读时间：13 分钟

## 🎯 学习目标（Learning Objectives）

学完本页，你应该能：

1. 手算 RWS：给定概率 → cumulative probability → 用 $u \in [0,1]$ 落到个体区间。
2. 解释 SRWS 的“期望份数 = 概率 × pool size → 取整数部分 → 小数部分再跑一次 RWS”，并排出一张表格。
3. 解释 SUS 为什么“份数至少为 $\lfloor \lambda P(i) \rfloor$、至多多 1”，并用一次多指针轮盘直觉说明。
4. 说明 Tournament 为何只需相对比较（无需全局 fitness 知识），以及参数 $k / p_{\text{best}}$ 如何调 selection pressure。
5. 区分 RWS 与 Tournament 的适用场景（全局 fitness 可得 vs 只能相对比较）。

## Roulette wheel selection（RWS）

把轮盘面积设为与选择概率成正比，转 $\mu$ 次得到 $\mu$ 个父代。实现时计算 cumulative probability，对每个名额生成 $u \in [0,1]$ 并落到对应区间。（Lecture 4, slides 27–33）

**具体实现（slides 31–33）**：先由概率算出 cumulative probability，再对每个名额抽一个 $u \in [0,1]$ 落到区间。

| Individual | Prob. of i | Cumulative prob. |
|---|---:|---:|
| 1 | 0.25 | 0.25 |
| 2 | 0.05 | 0.30 |
| 3 | 0.40 | 0.70 |
| 4 | 0.10 | 0.80 |
| 5 | 0.20 | 1.00 |

- 若 $u \le 0.25$ 选体 1；$0.25 < u \le 0.30$ 选体 2；$0.30 < u \le 0.70$ 选体 3；$0.70 < u \le 0.80$ 选体 4；$0.80 < u \le 1.00$ 选体 5。

示例：概率 0.25/0.05/0.40/0.10/0.20，累计 0.25/0.30/0.70/0.80/1.0；$u=0.79 \to \text{个体 } 4$、$0.1 \to 1$、$0.5 \to 3$、$0.6 \to 3$、$0.9 \to 5$，mating pool = {4,1,3,3,5}。

![轮盘赌选择](assets/CEG5302/fig-003-roulette-wheel.png)

**图：** 轮盘赌选择示意——每个个体占据与选中概率成正比的扇形面积，转动轮盘若干次得到 mating pool；实现上用累计概率落在区间内的方式判定。

*来源：Lecture 4-Selection and Population management_03Sept2026.pdf，第 28 页；核对 2026-09-07。*

### 图意解析（Figure Meaning）

- **扇形面积正比于选中概率**：越大的扇形 = 越高 fitness = 越容易被抽中。
- **“转 $\mu$ 次”**：每次独立抽一个 $u$，落在哪个扇形就选哪个个体，因此**同一个体可被多次抽中**（重复允许）。
- **实现不能用真轮盘**，而是用累计概率区间；所以 RWS 依赖**所有个体的 fitness** 已知。

RWS 实现简单，但 mating pool 方差高、可能不能精确反映概率分布。两个改进：（slides 35–41）

- **SRWS（Stochastic Reminder RWS）**：期望份数 = 概率 × pool size；先取整数部分，剩余名额用小数部分作 fitness 再跑一次 RWS。
- **SUS（Stochastic Universal Sampling）**：相当于一次旋转带 $\mu$ 个等距指针的轮盘；保证个体 $i$ 的份数至少是 $\lfloor \mu \cdot P(i) \rfloor$、至多多 1。

### SRWS 完整手算（slides 36–38，$\mu=5$）

| Individual | Prob. of i | Expected copies $=P \cdot 5$ | Integer part | Fractional part |
|---|---:|---:|---:|---:|
| 1 | 0.25 | 1.25 | 1 | 0.25 |
| 2 | 0.05 | 0.25 | 0 | 0.25 |
| 3 | 0.40 | 2.00 | 2 | 0.00 |
| 4 | 0.10 | 0.50 | 0 | 0.50 |
| 5 | 0.20 | 1.00 | 1 | 0.00 |

- **第 1 步**：把 integer part 直接放进 mating pool → 已经放入 `1, 3, 3, 5`（共 4 个）。
- **第 2 步**：还剩 $5-4=1$ 个名额，用 **fractional part 作为 fitness 再跑一次 RWS**（0.25/0.25/0.00/0.50/0.00）→ 大概率抽到个体 4（其 fractional 0.5 最大），把它补进 mating pool。

> 💡 **为什么 SRWS 更好**：它**先确保“大概率该有多少就至少有整数部分那么多”**，把方差压下来；又用小数部分补足剩余名额，比纯 RWS 更贴近期望分布。

### SUS 伪代码与保证（slides 39–42）

- **直觉**：等价于**一次转动一个带 $\lambda$ 个等距指针的轮盘**，而不是 $\lambda$ 次转单一指针轮盘。
- **伪代码**（slide 40）：
```text
# SUS: 一次生成 λ 个等距指针
offset = uniform(0, 1/λ)
for k in 0..λ-1:
    ptr = offset + k/λ
    选累积概率区间覆盖 ptr 的个体
```
- **保证（slide 41）**：个体 $i$ 的份数**至少为 $\lfloor \lambda \cdot P(i) \rfloor$，且至多多 1**；因此它**不会像 RWS 那样方差很大**。

### 三种基于概率的取样算法对比

（依据课件第 27–41 页整理；核对 2026-09-07）

| 算法 | 步骤 | 优点 | 缺点/性质 |
|---|---|---|---|
| RWS | 累计概率 → 每名额抽 $u \in [0,1]$ 落区间 | 实现简单 | 方差高，可能偏离概率分布 |
| SRWS | 期望份数=概率×pool；先取整数部分，剩余用小数部分再 RWS | 更贴近期望 | 仍需一轮 RWS 取样 |
| SUS | 一次旋转带 $\lambda$ 等距指针 | 份数至少为 $\lfloor \lambda P(i) \rfloor$、至多多 1 | 需维护指针间距 |

伪代码（依据 slide 32, 34 整理；核对 2026-09-07）：

```text
# RWS
cum[1..μ]; cum[1]=p_1; cum[i]=cum[i-1]+p_i
for slot in 1..μ:
    u = uniform(0,1)
    取最小 k 使 u <= cum[k]
```

## Tournament selection

RWS 需要知道所有个体的 fitness；大种群或分布式种群中这未必可行，且当 fitness 只能相对比较（如比较两件艺术品、博弈策略）时 RWS 失效。Tournament 是 **ordering-based**，只比较两个个体的相对 rank，简单快速、无需全局 fitness 知识。（slides 42–44）

- 不受 transposing 问题影响（用相对排名而非绝对值）。（slide 46）
- 参数：**tournament size**（越大，selection pressure 越高）；**最优个体获胜概率**（通常为 1，即确定性 tournament；<1 为随机，降低它会减小 pressure）。（slides 47–48）

Tournament 伪代码（依据 slide 44 整理；核对 2026-09-07）：

```text
# 最小化问题；deterministic tournament（p_best=1）
repeat 直到 mating pool 满:
    from 种群随机取 k 个个体
    选其中 fitness 最小者加入 mating pool
```

**数值示例（$k=2$，最小化）**：种群 fitness 为 $\{5, 12, 3, 9\}$。一次随机取到 $(5, 9)$，则选 fitness 5；再取 $(12, 3)$ 选 3。tournament size 越大，越容易只选中高 fitness 个体，选择压力越高；$p_{\text{best}} < 1$ 时最优个体也有被略过的可能，压力下降。（依据 slides 45–48 整理）

> 📘 **图意（slide 45）**：课件把每个个体画成一个圆，圆内是 fitness 值；有些值带 **`+xx`**，表示**为约束违反而额外加上的项**（constraint violation 的 penalty），这里暂时不重要。重点是：tournament 只比较**两个个体的相对 rank**，因此对 fitness 的绝对平移不敏感。

| 参数 | 作用 | 变化方向 |
|---|---|---|
| Tournament size $k$ | 每次参与比较的个体数 | $k \uparrow \to$ 选择压力 $\uparrow$ |
| $p_{\text{best}}$（最优个胜出概率） | 通常 $=1$（确定性） | $<1 \to$ 压力 $\downarrow$ |

## Uniform parent selection

每个个体作为父代的概率相同，用于 Evolutionary Programming / Evolutionary Strategies；看似 selection pressure 为 0，实际由强 survivor selection 机制施加压力。（slide 49）

## Over-selection

用于超大种群（如 Genetic Programming 中的数千个体）。先按 fitness 排名，分为 top $x\%$ 与 bottom $(100-x)\%$；选择父代时 80% 从 top $x\%$ 选、20% 从其余选，从而在大种群中保持很高 pressure。（slides 50–52）

## Exam Checklist（考试自查）

- **必须手算**：RWS（cumulative probability → 匹配 $u$）；SRWS（expected copies / integer part / fractional part）；Tournament（$k=2$ 最小化）。
- **必须理解**：SRWS/SUS 为什么比 RWS 方差低；Tournament 为何“不需要全局 fitness 知识、不受 transposing 影响”；over-selection 用于超大种群。
- **必须记忆**：RWS（实现简单但方差高）、SRWS（期望份数→整数部分→小数部分）、SUS（$\lfloor \lambda P(i) \rfloor \le \text{copies} \le \lfloor \lambda P(i) \rfloor+1$）；tournament 的两个参数（$k$、$p_{\text{best}}$）。
- **了解即可**：SUS 伪代码的具体指针步进实现。
- **明确 out of scope**：本讲不要求证明 SUS 的界，也不推导 p_best 与压力关系的定量公式。

## 下一步

- 上一页：[[CEG5302-Lecture04-Population-Models-FPS-and-Ranking]]
- 下一页：[[CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 4-Selection and Population management_03Sept2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.4-Selection.and.Population.management_03Sept2026.pdf)，slides 25–52；配图取自第 28 页。
- 2026-09-03：从 Lecture 4 拆出“RWS 与 Tournament 等选择”短页。
- 2026-09-07：嵌入轮盘赌选择原图（第 28 页）、新增取样算法对比表、RWS 与 Tournament 伪代码及数值示例。
- 2026-09-09：新增学习目标；补充 RWS 的 cumulative probability 表与区间判定、图意解析；新增 SRWS 完整手算表（μ=5）与 SUS 伪代码/保证；补充 tournament 图的 `+xx` 约束惩罚项说明；新增 Exam Checklist。
