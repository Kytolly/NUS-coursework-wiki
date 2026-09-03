# Island 与 Cellular EA 及 MATLAB

> 本页属于：CEG5302 / Lecture 04
>
> 前置知识：[[CEG5302-Lecture04-多样性维持与Niching]]
>
> 预计阅读时间：8 分钟

## Island model EAs

（coarse-grained parallel EAs）并行运行多个种群，通过 ring/torus/hypercube 结构通信，每隔固定代数（**epoch**）与邻居交换个体（**migration**）：种群内 exploitation，种群间 exploration。（Lecture 4, slides 85–93）

设计问题：

- **多久交换一次**：太频繁会全部收敛到同一区域，太少则浪费算力；epoch 常取 25–150 代。
- **交换多少、哪些个体**：通常 2–5 个；随机选择更不易被新高 fitness 移民接管。
- **如何划分**：需满足最小 subpopulation 大小，subpopulation 越多性能越好。
- **各岛是否相同**：可以不同——subpopulation 大小、recombination/mutation 算子与概率都可各异。

## Cellular EAs

在**单个种群内**维持空间分布，demes 形成于 algorithmic subspace（类比地理距离导致的信息缓慢扩散）。实现：个体置于（通常环面）网格顶点，每代对每个 deme（如方格网格上节点及其 8 个近邻，共 9 个）选择 2 个父代、recombination、mutation、评估，再用 offspring 替换 deme 内某个节点上的个体。（slides 94–96）

## MATLAB 中的 GA

MATLAB Global Optimization Toolbox 实现了 Simple GA（可带/不带约束），设置参数后直接调用 `ga` 函数即可，无需手写代码。语法与参数见 MathWorks 文档 <https://www.mathworks.com/help/gads/ga.html>，或在 MATLAB 中运行 `doc ga`。（slides 97–104）

## 下一步

- 上一页：[[CEG5302-Lecture04-多样性维持与Niching]]
- 下一页：[[CEG5302-当前进度与待补内容]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：`Lecture 4-Selection and Population management_03Sept2026.pdf`，slides 85–104。
- 2026-09-03：从 Lecture 4 拆出“Island 与 Cellular EA 及 MATLAB”短页。
