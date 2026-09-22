# 算法复杂度与P-NP理论

> 本页属于：CEG5201 / Week 01
> 前置知识：[[CEG5201-Week01-多处理器体系结构与系统设计流]]
> 预计阅读时间：10 分钟

---

## 1. 理论模型与算法复杂度（Time and Space Complexities）

在设计与评估并行算法时，首先需要脱离具体硬件实现的微架构细节，在抽象的理论模型下评估算法的固有复杂度（[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) 第 64 页）：

- **理论模型的价值（PRAM 等）**：
  - 便于开发并行算法，而无需受底层物理实现细节的干扰（Convenient to develop parallel algorithms without worrying about implementation details）；
  - 可用于获取并行计算机的理论上下界，或在芯片流片制造之前评估特定芯片面积下的 VLSI 复杂度及其他指标。
- **复杂度维度**：
  - 算法求解规模为 $s$ 的问题时的复杂度，是**执行时间（Execution Time）**与**存储空间（Storage Space）**的函数。
  - **时间复杂度（Time Complexity）**：输入问题规模 $s$ 的函数。在算法分析中，通常重点考察**最坏情况时间复杂度（Worst-case time complexity）**。
  - **空间复杂度（Space Complexity）**：同样是问题规模 $s$ 的函数，渐近空间复杂度指代程序处理大规模输入时所需的数据存储开销。

---

## 2. 大 $O$ 渐近阶记号的严格数学定义（Big-O Notation）

讲义第 65 页给出了时间复杂度大 $O$ 阶的数学定义：

### 数学定义
若存在一个正实数常数 $c > 0$ 以及一个非负阈值 $s_0$，使得对所有满足 $s > s_0$ 的非负规模 $s$，恒有：

$$
g(s) \le c \cdot f(s)
$$

则称算法的时间复杂度 $g(s)$ 为 $O(f(s))$。

阶数记号 $O(\cdot)$ 表达的是算法的**渐近时间复杂度（Asymptotic Time Complexity）**，用于刻画当问题规模 $s$ 趋向于很大时算法耗时的增长速率。

### 确定性与非确定性算法（Deterministic vs Non-deterministic）

讲义第 65 页明确区分了计算模型的两种基本算法类型：

1. **确定性算法（Deterministic Algorithms）**：
   - 算法执行的每一步骤都有唯一确定的定义（Every step is uniquely defined）；
   - 这与程序在真实物理计算机上的执行方式严格一致。
2. **非确定性算法（Non-deterministic Algorithms）**：
   - 算法包含某种特殊操作，其执行可以在一组可能的候选结果集合中产生某一个结果（Contains operations resulting in one outcome in a set of possible outcomes）。

---

## 3. 多项式复杂度与 P / NP 问题阶层

讲义第 66–67 页阐述了现代计算复杂性理论的核心划分：

### 3.1 多项式复杂度与 P 类问题
- **多项式复杂度（Polynomial Complexity）**：若存在一个多项式 $p(s)$，使得对于任意规模为 $s$ 的问题，算法的时间复杂度均为 $O(p(s))$，则称该算法具有多项式复杂度。
- **P 类问题（P-class problems）**：所有拥有多项式复杂度确定性算法的问题集合（The set of problems having polynomial complexity algorithms）。
- **可处理性（Tractability）**：**P 类问题在计算上被视为可处理的（Computationally Tractable）**。

### 3.2 NP 类问题（NP-class problems）
- **定义**：可由非确定性算法在多项式时间内求解的问题集合（The set of problems solvable by non-deterministic algorithms in polynomial time）。
- **$P \subseteq NP$ 的包含关系**：由于确定性算法本身是非确定性算法的一个特例（Special class），因此可以直接得出：

$$
P \subseteq NP
$$

- **不可处理性（Intractability）**：NP 类中的难解问题通常被认为是计算上不可处理的（Intractable）。
- **$P$ 是否等于 $NP$ 的千禧年悬疑**：
  > 讲义第 67 页指出：计算机科学家目前**并不知道**究竟是 $P = NP$ 还是 $P 
eq NP$。这是理论计算机科学中著名的开放难题（Open problem for computer scientists）。

![NP-Completeness 概念图](assets/CEG5201/chap1/fig66_np_completeness.png)
*图：NP-Completeness 示意（来源：CG5201_Chap1 (2627).pdf 第 66 页）*

### 3.3 经典问题复杂度对比

讲义第 67 页给出了具体的经典算法实例：

| 问题描述 | 对应算法复杂度 | 复杂度性质 | 归属判定 |
| :--- | :--- | :--- | :--- |
| **数值排序（Sorting numbers）** | $O(n \log n)$ | 多项式阶 | **P 类（Tractable）** |
| **矩阵相乘（Multiplying 2 matrices）** | $O(n^3)$ | 多项式阶 | **P 类（Tractable）** |
| **旅行商问题（Traveling Salesman Problem, TSP）** | $O(n^2 2^n)$ | **指数阶（Exponential）** | **NP 类（目前无确定性多项式算法）** |

对于旅行商问题（TSP）等问题，目前已开发的算法复杂度为 $O(n^2 2^n)$ 等非多项式形式。这些复杂度属于指数级别，迄今为止尚未发现任何确定性多项式时间算法。这些具有指数复杂度的问题属于 NP 类。

---

## 4. 问题可处理性判定与归约方法（Reduction to Known NP Problems）

讲义第 68 页总结了在科研与工程实践中判定问题可处理性的实用方法论：

1. **直觉与初步实验**：
   - 面对一个新的计算问题，首先明确该问题是否为可处理的（Tractable）至关重要。
   - 通常可以通过人类直觉（Intuition）以及初步的数值测试来感知问题的可处理性。
2. **多项式归约法（Reduction Method）**：
   - 在实践中，证明一个新问题属于 NP 类的最常用方法是：**将一个已知的 NP 类问题归约（Reduce）到当前研究的问题上**；
   - 证明已知 NP 问题的某个实例等价于当前问题的实例。既然已知问题属于 NP 类，则当前研究的问题同样属于 NP 类。
3. **权威参考文献**：
   - 在文献中存在一批用于映射和归约的标准经典 NP 问题。熟练掌握这些经典已知问题，是证明新问题属于 NP 类的基本功。
   - 讲义特别推荐权威经典著作：
     > **M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*** —— 讲义称其为该领域的“必读之书与圣经”（A must read book and the bible on this topic）。

---

## 学习目标 / Problem-Solving Skills

完成本节学习后，你应能掌握讲义中的以下核心知识与分析技能：

1. **渐近复杂度大 $O$ 数学定义**：
   - 能够准确写出大 $O$ 记号的形式化不等式定义（存在正实常数 $c$ 与非负阈值 $s_0$，使所有 $s > s_0$ 均有 $g(s) \le c f(s)$）；
   - 区分确定性算法与非确定性算法的定义。
2. **P 类与 NP 类的理论划分**：
   - 明确 P 类的定义（确定性多项式时间可解）与 NP 类的定义（非确定性多项式时间可解）；
   - 解释为什么 $P \subseteq NP$ 恒成立，并明确指出 $P$ 与 $NP$ 是否相等仍是未决的开放问题；
   - 掌握计算可处理性（Tractable vs Intractable）的划分。
3. **算法实例复杂度识记**：
   - 熟记排序为 $O(n \log n)$、矩阵乘法为 $O(n^3)$（属于 P 类），以及 TSP 的指数算法复杂度 $O(n^2 2^n)$（属于 NP 类）。
4. **NP 问题的证明思路**：
   - 阐述利用“已知 NP 问题归约法（Reduction to known NP problem）”证明新问题属于 NP 类的基本逻辑；
   - 了解 Gary & Johnson 的经典理论著作。

---

## 下一步

- 上一页：[[CEG5201-Week01-多处理器体系结构与系统设计流]]
- 下一页：[[CEG5201-Week01-PRAM理论模型与变体比较]]
- 模块总览：[[CEG5201-讲义与笔记索引]]
- 返回知识库：[[Home]]

---

## 来源与更新日志

- 来源：[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) pp. 64–68.
- 2026-09-08：初始简略版归档。
- 2026-09-23：严格依讲义重构，剔除非讲义的 $10^{80}$ 粒子比喻、Cook-Levin 展开等推想内容；忠实保留讲义中确定性/非确定性算法定义、大 O 数学定义、$P \subseteq NP$ 论证、TSP 复杂度 $O(n^2 2^n)$、已知 NP 归约逻辑与 Garey & Johnson 经典书单推荐。
