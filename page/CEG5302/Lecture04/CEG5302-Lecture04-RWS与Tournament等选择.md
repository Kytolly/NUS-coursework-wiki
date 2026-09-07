# RWS 与 Tournament 等选择

> 本页属于：CEG5302 / Lecture 04
>
> 前置知识：[[CEG5302-Lecture04-种群管理模型与FPS及Ranking]]
>
> 预计阅读时间：9 分钟

## Roulette wheel selection（RWS）

把轮盘面积设为与选择概率成正比，转 μ 次得到 μ 个父代。实现时计算 cumulative probability，对每个名额生成 `u ∈ [0,1]` 并落到对应区间。（Lecture 4, slides 27–33）

示例：概率 0.25/0.05/0.40/0.10/0.20，累计 0.25/0.30/0.70/0.80/1.0；`u=0.79→个体4、0.1→1、0.5→3、0.6→3、0.9→5`，mating pool = {4,1,3,3,5}。

RWS 实现简单，但 mating pool 方差高、可能不能精确反映概率分布。两个改进：（slides 35–41）

- **SRWS（Stochastic Reminder RWS）**：期望份数 = 概率 × pool size；先取整数部分，剩余名额用小数部分作 fitness 再跑一次 RWS。
- **SUS（Stochastic Universal Sampling）**：相当于一次旋转带 μ 个等距指针的轮盘；保证个体 i 的份数至少是 `μ·P(i)` 的整数部分、至多多 1。

## Tournament selection

RWS 需要知道所有个体的 fitness；大种群或分布式种群中这未必可行，且当 fitness 只能相对比较（如比较两件艺术品、博弈策略）时 RWS 失效。Tournament 是 **ordering-based**，只比较两个个体的相对 rank，简单快速、无需全局 fitness 知识。（slides 42–44）

- 不受 transposing 问题影响（用相对排名而非绝对值）。（slide 46）
- 参数：**tournament size**（越大，selection pressure 越高）；**最优个体获胜概率**（通常为 1，即确定性 tournament；<1 为随机，降低它会减小 pressure）。（slides 47–48）

## Uniform parent selection

每个个体作为父代的概率相同，用于 Evolutionary Programming / Evolutionary Strategies；看似 selection pressure 为 0，实际由强 survivor selection 机制施加压力。（slide 49）

## Over-selection

用于超大种群（如 Genetic Programming 中的数千个体）。先按 fitness 排名，分为 top x% 与 bottom (100-x)%；选择父代时 80% 从 top x% 选、20% 从其余选，从而在大种群中保持很高 pressure。（slides 50–52）

## 下一步

- 上一页：[[CEG5302-Lecture04-种群管理模型与FPS及Ranking]]
- 下一页：[[CEG5302-Lecture04-SurvivorSelection与选择压力]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 4-Selection and Population management_03Sept2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture%204-Selection%20and%20Population%20management_03Sept2026.pdf)，slides 25–52。
- 2026-09-03：从 Lecture 4 拆出“RWS 与 Tournament 等选择”短页。
