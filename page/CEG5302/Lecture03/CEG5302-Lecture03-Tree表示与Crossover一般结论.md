# Tree 表示与 Crossover 一般结论

> 本页属于：CEG5302 / Lecture 03
>
> 前置知识：[[CEG5302-Lecture03-Permutation表示]]
>
> 预计阅读时间：7 分钟

## Tree 表示

树是最基础的表示之一，是 **Genetic Programming** 的基础。可表示算术/逻辑公式甚至程序代码（如 `2·π + ((x+3) − y/5 + 1)`）。它能保留程序结构、支持**变长**解，并因任意操作都可作为合法节点而保持语法灵活性。（Lecture 3, slides 98–101）

- **Function set**：允许的内部节点集合；**Terminal set**：允许的叶节点集合。（slide 102）

### Mutation 与 Recombination

（slides 103–106）

- **Mutation**：随机选一个节点，用随机生成的子树替换该节点及其子树；可能增加深度。参数包括 mutation 与 recombination 之间的选择概率、选内部点作为子树根的概率；mutation 通常只占很小比例（如 5%），因为它造成巨大变化。
- **Recombination**：在两个父代各随机选一个节点，交换对应子树。参数包括 recombination 概率、选内部点作为交叉点的概率。

## 关于 Crossover 的一般结论

一般来说，crossover 应当：（slides 107–108）

1. **保持 population 均值不变**：crossover 没有 fitness 信息，不应把整个 population 推向任一方向。
2. **增加 population 的 diversity**：selection 直观上会降低 diversity，crossover 应抵消这一效应，防止 premature convergence 到 local optimum。

## 下一步

- 上一页：[[CEG5302-Lecture03-Permutation表示]]
- 下一页：[[CEG5302-Lecture04-种群管理模型与FPS及Ranking]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：`Lecture 3-Representation and Variation_27Aug2026.pdf`，slides 98–108。
- 2026-09-03：从 Lecture 3 拆出“Tree 表示与 Crossover 一般结论”短页。
