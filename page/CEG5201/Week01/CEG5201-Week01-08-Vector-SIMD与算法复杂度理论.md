# Vector-SIMD与算法复杂度理论

> 本页对应课件：CG5201_Chap1 (2627).pdf, pp. 62–68
> 本页属于：CEG5201 / Week 01
> 上一页：[[CEG5201-Week01-07-NUMA架构与多处理器设计流]]
> 下一页：[[CEG5201-Week01-09-PRAM理论模型与变体比较]]
> 预计阅读时间：12 分钟

---

## 1. 为什么需要进入理论模型与算法复杂度？

在完成了物理多处理器系统（UMA/NUMA）的工程微架构探讨之后，讲义的叙事视角转向了更深层次的**超级计算与理论计算机科学**：
1. 对于向量机与 SIMD 超级计算机，如何用形式化的数学模型准确描述其指令控制与数据流动？
2. 为什么需要在脱离底层物理布线与门级电路的前提下建立算法理论模型？
3. 在评估算法时，如何从计算复杂性理论的角度界定什么是“可有效计算的”，什么是“不可处理的”？

讲义第 62–68 页系统回答了上述问题（[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) 第 62–68 页）。

---

## 2. 向量机与 SIMD 形式化计算模型（Slides 62–63）

### 2.1 超级计算机的两大经典分支（Slide 62）
- **向量机（Vector Computers）**：依托高度流水化的向量功能部件，按时间流水线方式连续处理长向量数据。
- **SIMD 阵列机（SIMD Computers）**：由中央控制单元集中控制大量的物理处理单元（PE），在空间上同步对多个数据流执行相同的操作。

### 2.2 SIMD 形式化体系结构 5 元组（Slide 63）
讲义第 63 页给出了 SIMD 计算模型的经典 5 元组形式化定义：

$$
M = \langle N, C, I, M, R angle
$$

各分量的严格定义如下：
- $N$：系统中物理处理单元（PE, Processing Elements）的数量；
- $C$：由中央控制单元（Control Unit, CU）**直接执行并解释的标量指令与控制流指令集合**（Scalar/control flow instructions directly executed by CU）；
- $I$：由控制单元**广播给所有活跃 PE 并行执行的操作指令集合**（Instructions broadcast to PEs for execution）；
- $M$：掩码向量集合（Masking schemes），用于动态屏蔽或使能特定 PE 参与当前的计算；
- $R$：处理单元之间的数据互连通信拓扑路由模式（Interconnection routing patterns）。

---

## 3. 理论建模初衷与时空复杂度（Slide 64）

讲义第 64 页指出了引入抽象理论模型（如 PRAM）的核心价值：

- **摆脱实现细节的干扰**：
  在抽象理论模型下开发并行算法，研究者无需受困于特定硬件的缓存一致性协议、总线仲裁、死锁避免等繁杂工程细节（Convenient to develop parallel algorithms without worrying about implementation details）。
- **获取理论上下界与芯片预估**：
  理论模型可用于推导并行计算的内在性能上下界，或在芯片流片制造之前评估给定芯片面积下的 VLSI 复杂度指标。

### 3.1 时间复杂度与空间复杂度定义
- 算法求解规模为 $s$ 的问题时的复杂度，是**执行时间**与**存储空间**的函数。
- **时间复杂度（Time Complexity）**：输入问题规模 $s$ 的函数。在算法分析中，通常重点考察**最坏情况时间复杂度（Worst-case time complexity）**。
- **空间复杂度（Space Complexity）**：同样是问题规模 $s$ 的函数，渐近空间复杂度刻画程序处理大规模数据时所需的额外物理存储空间。

---

## 4. 大 $O$ 阶记号与算法类型（Slide 65）

### 4.1 大 $O$ 渐近阶的严格数学定义
讲义第 65 页给出了大 $O$ 符号的形式化数学定义：

> **数学定义（Slide 65）**：
> 若存在一个正实数常数 $c > 0$ 以及一个非负阈值 $s_0$，使得对所有满足 $s > s_0$ 的非负规模 $s$，恒有：
> 
> $$
> g(s) \le c \cdot f(s)
> $$
> 
> 则称算法的时间复杂度 $g(s)$ 为 $O(f(s))$。

阶数记号 $O(\cdot)$ 表达的是算法的**渐近时间复杂度（Asymptotic Time Complexity）**，用于刻画当问题规模 $s$ 很大时耗时的增长趋势。

### 4.2 确定性 vs 非确定性算法（Slide 65）
讲义严格区分了计算模型的两种基本算法类型：
1. **确定性算法（Deterministic Algorithms）**：
   - 算法执行的每一步骤都有唯一确定的定义（Every step is uniquely defined）；
   - 这与程序在真实物理计算机上的执行方式严格一致。
2. **非确定性算法（Non-deterministic Algorithms）**：
   - 算法包含某种特殊操作，其执行可以在一组可能的候选结果集合中产生某一个结果（Contains operations resulting in one outcome in a set of possible outcomes）。

---

## 5. 计算复杂性阶层：P 类与 NP 类（Slides 66–67）

![NP-Completeness 概念图](assets/CEG5201/chap1/fig66_np_completeness.png)
*图：NP 完全性概念示意（来源：CG5201_Chap1 (2627).pdf 第 66 页）*

### 5.1 多项式复杂度与 P 类问题
- **多项式复杂度（Polynomial Complexity）**：若存在一个多项式 $p(s)$，使得对于任意规模为 $s$ 的问题，时间复杂度均为 $O(p(s))$，则称该算法具有多项式复杂度。
- **P 类问题（P-class problems）**：所有拥有多项式复杂度确定性算法的问题集合。
- **计算可处理性（Tractability）**：**P 类问题在理论上被定义为可处理的（Computationally Tractable）**。

### 5.2 NP 类问题与 $P \subseteq NP$
- **NP 类问题（NP-class problems）**：由非确定性算法在多项式时间内可解的问题集合（Solvable by non-deterministic algorithms in polynomial time）。
- **包含关系证明**：
  > 由于确定性算法本身是非确定性算法的一个特例（Special class），因此可以直接得出：
  > 
  > $$
  > P \subseteq NP
  > $$
- **$P = NP$ 开放问题**：
  讲义第 67 页明确指出：计算机科学家目前**并不知道**究竟是 $P = NP$ 还是 $P 
eq NP$，这是理论计算机科学著名的未解之谜（Open problem for computer scientists）。

### 5.3 经典问题复杂度对比（Slide 67）

| 经典问题 | 对应已知算法复杂度 | 复杂度属性 | 计算可处理性判定 |
| :--- | :--- | :--- | :--- |
| **数值排序（Sorting numbers）** | $O(n \log n)$ | 多项式阶 | **P 类（Tractable，可处理）** |
| **两矩阵相乘（Multiplying 2 matrices）** | $O(n^3)$ | 多项式阶 | **P 类（Tractable，可处理）** |
| **旅行商问题（Traveling Salesman Problem, TSP）** | $O(n^2 2^n)$ | **指数阶（Exponential）** | **NP 类（Intractable，目前无确定性多项式解）** |

---

## 6. 问题可处理性判定与归约方法（Slide 68）

讲义第 68 页总结了在科研与算法设计中判定未知问题复杂度的实用方法论：

1. **可处理性感知**：面对新问题，首先判断其是否在计算上可处理至关重要，通常基于直觉和初步数值实验进行感知。
2. **多项式归约法（Reduction Method）**：
   - 证明一个新问题属于 NP 类的经典标准方法是：**将一个已知的 NP 类问题归约（Reduce）到当前研究的问题上**；
   - 证明已知 NP 问题的某个实例等价于当前问题的实例。既然已知问题属于 NP 类，则当前问题同样属于 NP 类。
3. **权威参考文献**：
   - 讲义特别推荐了该领域的权威经典著作：
     > **M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness***（讲义称其为“必读之书与该领域的圣经”）。

---

## 学习目标 / Problem-Solving Skills

完成本节学习后，你应能掌握讲义中的以下核心知识与分析技能：

1. **SIMD 形式化模型掌握**：
   - 默写 SIMD 5 元组 $M = \langle N, C, I, M, R angle$，并准确说出各个分量的含义（特别是 $C$ 为 CU 执行指令，$I$ 为广播给 PEs 指令）。
2. **渐近时间复杂度与算法分类**：
   - 准确写出大 $O$ 阶记号的形式化数学不等式定义；
   - 区分确定性算法与非确定性算法的定义。
3. **P 类与 NP 类的理论划分**：
   - 说明 P 类与 NP 类的定义，阐述为什么 $P \subseteq NP$ 成立；
   - 指出 $P=NP$ 目前仍是开放性难题；
   - 熟记排序 $O(n \log n)$、矩阵乘法 $O(n^3)$ 与 TSP $O(n^2 2^n)$ 的复杂度归属。
4. **归约方法逻辑**：
   - 阐明如何通过“已知 NP 问题归约法”证明一个新问题属于 NP 类的逻辑推导链条。

---

## 下一步

- 上一页：[[CEG5201-Week01-07-NUMA架构与多处理器设计流]]
- 下一页：[[CEG5201-Week01-09-PRAM理论模型与变体比较]]
- 模块总览：[[CEG5201-讲义与笔记索引]]
- 返回知识库：[[Home]]

---

## 来源与更新日志

- 来源：[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) pp. 62–68.
- 2026-09-23：按照讲义顺序重构，建立正规编号与讲义映射页眉，系统整合 SIMD 5 元组、PRAM 建模动机、大 O 数学定义、P/NP 理论与 Garey & Johnson 归约方法学。
