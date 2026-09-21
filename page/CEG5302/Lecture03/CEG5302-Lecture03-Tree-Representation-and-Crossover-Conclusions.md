# Tree 表示与 Crossover 一般结论

> 本页属于：CEG5302 / Lecture 03
>
> 前置知识：[[CEG5302-Lecture03-Permutation-Representation]]
>
> 预计阅读时间：10 分钟

## 🎯 学习目标（Learning Objectives）

学完本页，你应该能：

1. 说明 tree 是 Genetic Programming 的基础，能表示算术/逻辑公式甚至程序代码。
2. 解释 tree 与其他表示相比的独特价值：**保留程序结构、支持变长解、语法灵活（任意操作都能作为合法节点）**。
3. 说出 function set 与 terminal set 的含义。
4. 解释 tree 的 mutation（替换子树）与 recombination（交换子树），并说明为什么 mutation 通常只给很小比例（约 5%）。
5. 复述“crossover 的一般原则”（保持 population 均值、增加 diversity）及其推理。

## Tree 表示

树是最基础的表示之一，是 **Genetic Programming** 的基础。可表示算术/逻辑公式甚至程序代码。例如课件公式：$2 \cdot \pi + ((x + 3) - y/(5 + 1))$（slides 98–100）——根为 $+$，左子树 $2 \cdot \pi$，右子树 $((x+3) - y/(5+1))$，内部节点是 $+ / \times / - / \div$ 等函数，叶节点是变量 $x$、$y$ 与常量 $2$、$\pi$、$3$、$5$、$1$。它也能表示**程序代码**（slide 101 的树形程序节点）。

- **独特价值（slide 100）**：
  1. **保留程序结构**；
  2. 允许 **变长解**（variable length solutions）——这与前面所有定长表示（binary/integer/real/permutation）都不同；
  3. 仍保持**语法灵活性**——任意操作都可以作为合法节点（any operation can be included as a valid node）。
- **Function set**：允许的内部节点集合；**Terminal set**：允许的叶节点集合。（slide 102）

![树表示](assets/CEG5302/fig-004-tree-rep.png)

**图：** Tree 表示示意——内部节点为函数（如 `+`,`×`,`−`,`/`,`sin`），叶节点为终端（如变量 `x`、常量 `2`、`π`）；这正是 Genetic Programming 的基础。

*来源：Lecture 3-Representation and Variation_27Aug2026.pdf，第 98 页；核对 2026-09-07。*

### 图意解析（Figure Meaning）

- **根节点**：`+`（公式的最高层运算）。
- **内部节点（function set）**：`+`、`×`、`−`、`/`、`sin` 等，决定“如何组合”。
- **叶节点（terminal set）**：变量 `x`、常量 `2`、`π` 等。
- **意义**：整棵树就是一个合法表达式/程序；**recombination 交换子树**会改变程序的“子表达式”，**mutation 替换子树**会引入全新子表达式——这与“程序演化”思想吻合。

| 组成 | 含义 | 例子 |
|---|---|---|
| Function set | 允许的内部节点 | `+`, `−`, `×`, `/`, `sin`, `cos` |
| Terminal set | 允许的叶节点 | 变量 `x`、常量 `2`、`π` |

### Mutation 与 Recombination

（slides 103–106）

- **Mutation**：随机选一个节点，用**随机生成的子树**替换该节点及其子树；这个新子树**与初始种群生成方式类似**（也是随机生成）。可能增加深度。参数包括 mutation 与 recombination 之间的选择概率、选内部点作为子树根的概率；mutation 通常只占很小比例（如 5%），因为它造成巨大变化。
- **Recombination**：在两个父代各随机选一个节点，交换对应子树。参数包括 recombination 概率、选内部点作为交叉点的概率。

### 树算子参数

| 算子 | 参数 | 参考页 |
|---|---|---|
| Mutation | mutation vs recombination 的选择概率；选内部节点作为被替换子树根的概率 | 103–104 |
| Recombination | recombination vs mutation 概率；选内部节点作为交叉点的概率 | 105–106 |

mutation 通常只给很小的角色（约 5%），因为随机生成一整棵子树会造成很大结构变化；recombination 交换两棵子树，通常保留父代结构。（依据 slides 103–106 整理；核对 2026-09-07）

## 关于 Crossover 的一般结论

一般来说，crossover 应当：（slides 107–108）

1. **保持 population 均值不变**：crossover 没有 fitness 信息，不应把整个 population 推向任一方向。
2. **增加 population 的 diversity**：selection 直观上会降低 diversity，crossover 应抵消这一效应，防止 premature convergence 到 local optimum。

**推理**：(1) 若 crossover 把某一段基因从一种安排“平均化”成另一种，而它并不借助 fitness 信息，就不应主动把整个种群推向某个固定方向，否则等于引入一个未经验证的偏差；(2) selection 每一代都让更优解“多留一份”，会减少不同基因型数量，crossover 通过交换大块信息重新组合新个体，从而减缓 diversity 流失、给算法更多机会避免早熟。（依据 slides 107–108 整理；核对 2026-09-07）

## Crossover 与各表示的对照

| 表示 | Crossover 目标 | 是否具备 respect（保留双亲共有特征） |
|---|---|---|
| Binary / Integer | 交换块/位，倾向保留构建块 | 通常具备 |
| Real | 产生区间内或超出区间的新实值 | 无“共有特征”概念，看算子设计 |
| Permutation | 保留 order / adjacency 信息 | PMX 不具备，binary/integer 具备 |
| Tree | 交换子树，保留程序结构 | 保留结构片段 |

## Exam Checklist（考试自查）

- **必须理解**：tree 为什么是变长/语法灵活/保留结构；function set vs terminal set；crossover 的两个一般原则（均值不变、增 diversity）。
- **必须手算**：能画一棵 $2\pi + ((x+3) - y/(5+1))$ 的树；说明一次 mutation 替换子树/一次 recombination 交换子树的结果。
- **必须记忆**：mutation 通常只占 ~5%（因为造成巨大变化）；mutation 可能增加深度。
- **了解即可**：GP 的完整程序演化细节（后续讲次）。
- **明确 out of scope**：本讲不要求证明“crossover 一定增 diversity”，也不深入 GP 的树生成算法。

## 下一步

- 上一页：[[CEG5302-Lecture03-Permutation-Representation]]
- 下一页：[[CEG5302-Lecture04-Population-Models-FPS-and-Ranking]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 3-Representation and Variation_27Aug2026.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture.3-Representation.and.Variation_27Aug2026.pdf)，slides 98–108；配图取自第 98 页。
- 2026-09-03：从 Lecture 3 拆出“Tree 表示与 Crossover 一般结论”短页。
- 2026-09-07：嵌入树表示原图（第 98 页）、新增函数/终端集表与树算子参数表。
- 2026-09-09：新增学习目标；补充 $2\pi + ((x+3) - y/(5+1))$ 树形解读、tree 三大独特价值（结构/变长/语法灵活）、图意解析、mutation 子树“随机生成”细节；新增 Exam Checklist。
