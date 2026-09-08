# RWS 与 Tournament 等选择

> 本页属于：CEG5302 / Lecture 04
>
> 前置知识：[[CEG5302-Lecture04-种群管理模型与FPS及Ranking]]
>
> 预计阅读时间：9 分钟

## Roulette wheel selection（RWS）

把轮盘面积设为与选择概率成正比，转 μ 次得到 μ 个父代。实现时计算 cumulative probability，对每个名额生成 `u ∈ [0,1]` 并落到对应区间。（Lecture 4, slides 27–33）

示例：概率 0.25/0.05/0.40/0.10/0.20，累计 0.25/0.30/0.70/0.80/1.0；`u=0.79→个体4、0.1→1、0.5→3、0.6→3、0.9→5`，mating pool = {4,1,3,3,5}。

![轮盘赌选择](assets/CEG5302/fig-003-roulette-wheel.png)

**图：** 轮盘赌选择示意——每个个体占据与选中概率成正比的扇形面积，转动轮盘若干次得到 mating pool；实现上用累计概率落在区间内的方式判定。

*来源：Lecture 4-Selection and Population management_03Sept2026.pdf，第 28 页；核对 2026-09-07。*

RWS 实现简单，但 mating pool 方差高、可能不能精确反映概率分布。两个改进：（slides 35–41）

- **SRWS（Stochastic Reminder RWS）**：期望份数 = 概率 × pool size；先取整数部分，剩余名额用小数部分作 fitness 再跑一次 RWS。
- **SUS（Stochastic Universal Sampling）**：相当于一次旋转带 μ 个等距指针的轮盘；保证个体 i 的份数至少是 `μ·P(i)` 的整数部分、至多多 1。

### 三种基于概率的取样算法对比

（依据课件第 27–41 页整理；核对 2026-09-07）

| 算法 | 步骤 | 优点 | 缺点/性质 |
|---|---|---|---|
| RWS | 累计概率 → 每名额抽 `u∈[0,1]` 落区间 | 实现简单 | 方差高，可能偏离概率分布 |
| SRWS | 期望份数=概率×pool；先取整数部分，剩余用小数部分再 RWS | 更贴近期望 | 仍需一轮 RWS 取样 |
| SUS | 一次旋转带 `λ` 等距指针 | 份数至少为 `⌊λP(i)⌋`、至多多 1 | 需维护指针间距 |

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

**数值示例（k=2，最小化）**：种群 fitness 为 `{5, 12, 3, 9}`。一次随机取到 `(5, 9)`，则选 fitness 5；再取 `(12, 3)` 选 3。tournament size 越大，越容易只选中高 fitness 个体，选择压力越高；`p_best<1` 时最优个体也有被略过的可能，压力下降。（依据 slides 45–48 整理）

| 参数 | 作用 | 变化方向 |
|---|---|---|
| Tournament size k | 每次参与比较的个体数 | k↑ → 选择压力↑ |
| p_best（最优个胜出概率） | 通常 =1（确定性） | `<1` → 压力↓ |

## Uniform parent selection

每个个体作为父代的概率相同，用于 Evolutionary Programming / Evolutionary Strategies；看似 selection pressure 为 0，实际由强 survivor selection 机制施加压力。（slide 49）

## Over-selection

用于超大种群（如 Genetic Programming 中的数千个体）。先按 fitness 排名，分为 top x% 与 bottom (100-x)%；选择父代时 80% 从 top x% 选、20% 从其余选，从而在大种群中保持很高 pressure。（slides 50–52）

## 下一步

- 上一页：[[CEG5302-Lecture04-种群管理模型与FPS及Ranking]]
- 下一页：[[CEG5302-Lecture04-SurvivorSelection与选择压力]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 4-Selection and Population management_03Sept2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.4-Selection.and.Population.management_03Sept2026.pdf)，slides 25–52；配图取自第 28 页。
- 2026-09-03：从 Lecture 4 拆出“RWS 与 Tournament 等选择”短页。
- 2026-09-07：嵌入轮盘赌选择原图（第 28 页）、新增取样算法对比表、RWS 与 Tournament 伪代码及数值示例。
