# 多样性维持与 Niching

> 本页属于：CEG5302 / Lecture 04
>
> 前置知识：[[CEG5302-Lecture04-SurvivorSelection与选择压力]]
>
> 预计阅读时间：9 分钟

## 为什么需要 niching

multi-modal 问题有多个 local optima，需平衡 exploration/exploitation 以覆盖整个搜索空间、避免遗漏 optima，并提供多个选项供主观判断；此外 fitness function 可能不够准确或随时间变化，且窄峰可能是 overfitting 的伪影（宽峰更可取）。由于通常允许任意父代重组（**panmictic mixing**），整个种群会收敛到单一峰，因此需要 niching 方案让个体分散在多个峰上。（Lecture 4, slides 67–71）

## 多样性在何处度量

（slide 72）

- **Phenotype space**：现实中的 Manhattan/Euclidean 距离。
- **Genotype space**：chromosome 间的 Hamming/Euclidean/Manhattan 距离。
- **Algorithmic space**：population 空间的概念划分，或跨多个 CPU core 的物理分布。

## 显式 vs 隐式方法

（slide 73）

- **显式（explicit）**：直接修改算子以保持多样性、基于 genotype/phenotype 距离（fitness sharing、crowding、speciation）。
- **隐式（implicit）**：提供促进（但不保证）多样性的框架、工作在 algorithmic space（island model、cellular EA）。

## Fitness sharing

niche 是一小块邻域；在 selection 前按个体所在 niche 的拥挤程度共享/削减 fitness，使 selection 按 niche fitness 成比例分配个体。直觉是“越拥挤 fitness 越低”，人为引入资源稀缺。（slides 74–76）

计算所有个体对（含自身）的距离 `d(i,j)`，调整后 fitness：

```
F'(i) = F(i) / Σ_j sh(d(i,j))
```

sharing function 常取 `sh(d) = 1 - (d/σ_share)^α`（当 `d < σ_share`，否则 0）。α=1 时线性，α>1 时相近个体的削减作用随距离衰减更快；`σ_share`（sharing radius）决定能维持多少个 niche，一般取 5–10。（slides 77–80）

## Crowding

限制 offspring 只能替换与之相似的个体，避免用与多数个体都相似的 offspring 替换掉唯一个体。**Deterministic crowding**：mating pool 随机配对，每对经 recombination 产生 2 个 offspring，mutation 并评估；计算 4 个 offspring-parent 两两距离，每个 offspring 与最相似父代竞争，更优者进入下一代。（slides 81–82）

- **Fitness sharing vs crowding**：fitness sharing 按各峰 fitness 成比例分配个体；crowding 均匀地把个体分配到各峰。（slide 83）

## Speciation

施加交配限制——只有同/相近 species 的成员才能重组；可给 chromosome 加 species 标签并让其随 variation 进化；潜在配偶须在特定距离内，超出则拒绝。可与 fitness sharing 结合。（slide 84）

## 下一步

- 上一页：[[CEG5302-Lecture04-SurvivorSelection与选择压力]]
- 下一页：[[CEG5302-Lecture04-Island与CellularEA及MATLAB]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 4-Selection and Population management_03Sept2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture%204-Selection%20and%20Population%20management_03Sept2026.pdf)，slides 67–84。
- 2026-09-03：从 Lecture 4 拆出“多样性维持与 Niching”短页。
