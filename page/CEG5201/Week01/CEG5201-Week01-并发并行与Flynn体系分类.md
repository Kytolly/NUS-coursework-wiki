# 并发并行与Flynn体系分类

> 本页属于：CEG5201 / Week 01
> 前置知识：[[CEG5201-Week01-性能度量与计算吞吐率]]
> 预计阅读时间：12 分钟

---

## 1. 并发 vs 并行：概念辨析与四象限（Slides 45–48）

在并行系统设计中，讲义第 45–48 页对**并发（Concurrency）**与**并行（Parallelism）**给出了精确的对比定义：

### 1.1 核心定义辨析（Slide 47）
- **并发（Concurrency）**：指应用程序**如何处理其所面对的多个任务**。应用程序可以一次只处理一个任务（串行），也可以在同一时间段内同时推进多个任务（并发）。
- **并行（Parallelism）**：指应用程序**如何处理每一个具体的独立任务**。应用程序可以从头到尾串行执行该任务，也可以将该任务拆解为若干子任务（Subtasks），并在硬件上同时完成。

### 1.2 四种组合情况与四象限图解（Slides 46–47）
讲义第 46 页展示了著名的四象限图：

![并发与并行四象限模型](assets/CEG5201/chap1/fig46_concurrency_vs_parallelism.png)

讲义在第 47 页列出了四种典型的组合形态：
1. **是并发、非并行（Concurrent, but not parallel）**：系统同时处理多个任务，但每个任务内部没有被拆解为子任务。
2. **是并行、非并发（Parallel, but not concurrent）**：系统每次只处理一个任务，但该任务被拆分为多个子任务并发执行。
3. **既非并发、亦非并行（Neither concurrent nor parallel）**：系统每次只处理一个任务，且任务从不被分解。
4. **既并发、又并行（Both concurrent and parallel）**：系统同时处理多个任务，且每个任务内部进一步分解为子任务并行执行。

### 1.3 讲义的重要警示（Slide 48）
> **讲义重点提示**：
> 在第 4 种“既并发又并行”的情况下，**并发与并行带来的一部分收益可能会相互抵消甚至丧失**。因为计算机中的 CPU 核心在仅面对高并发或纯并行时就已经处于相对饱和状态；将二者强行叠加，可能只会带来极小的性能增益，甚至可能由于调度争用导致性能倒退。
> 因此，在采用并发并行混合模型前，必须进行严谨的分析与实际测量。

### 1.4 并行编程的两种流派（Slide 45）
- **隐式并行（Implicit Parallelism）**：
  - 程序员编写串行源代码（Seq versions）；
  - 由**并行化编译器（Parallelizing Compiler）**自动分析并生成并行目标代码；
  - 由运行时系统调度执行。
- **显式并行（Explicit Parallelism）**：
  - 程序员直接编写显式并行源代码（Parallel versions）；
  - 由**保并发编译器（Concurrency preserving Compiler）**编译生成并发目标代码；
  - 由运行时系统调度执行。

---

## 2. Flynn 体系结构分类法（1972）

讲义第 31–33 页介绍了 Michael J. Flynn 于 1972 年提出的经典分类体系。该分类依据**指令流（Instruction Stream）**与**数据流（Data Stream）**的多重性将计算机分为四类：

![Flynn 分类体系详细图解](assets/CEG5201/chap1/fig32_flynn_classification.png)

1. **SISD（Single Instruction, Single Data）**：
   - 单处理器执行单条指令流，操作单一数据流。经典单核顺序冯·诺依曼机器。
2. **SIMD（Single Instruction, Multiple Data）**：
   - 单一控制单元广播单条指令流，多个处理单元（PE）在不同的数据流上同步执行相同操作。适用于向量处理与规则数据并行。
3. **MISD（Multiple Instruction, Single Data）**：
   - 多个指令流同时作用于同一个数据流。在通用计算中较少使用，常用于特定容错表决与脉动阵列。
4. **MIMD（Multiple Instruction, Multiple Data）**：
   - 多个独立的处理器分别执行不同的指令流，处理各自独立的数据流。现代多核处理器与多计算机集群的主流模式。

---

## 3. 并行与向量计算机（Parallel / Vector Computers）

### 3.1 MIMD 的两类实现形式（Slide 34）
讲义第 34 页指出，MIMD 运行模式主要分为：
1. **共享存储型（Shared Memory）**
2. **分布式存储型（Distributed Memory）**

### 3.2 向量处理器（Vector Processors, Slide 35）
讲义第 35 页展示了向量处理器的基本架构：

![向量处理器体系结构](assets/CEG5201/chap1/fig35_vector_processor_architecture.png)

讲义提示：向量处理器的微架构细节将在 Chapter 3 中深入讨论。

---

## 4. 超级计算机体系（Supercomputers, Slides 62–63）

### 4.1 向量超级计算机（Vector Supercomputers, Slide 62）
- 向量计算机通常**建立在标量处理器之上（Built on top of a scalar processor）**。
- **数据分流控制机制**：
  - 标量数据：直接由标量处理单元（Scalar Unit）执行；
  - 向量数据：发送给向量处理单元（Vector Unit）；
  - **向量控制单元（Vector Control Unit）**：负责监督主存与向量流水线功能部件之间的数据流，并进行协调。
- **两类经典模型**：
  - **寄存器-寄存器模型（Register-to-register models）**：典型代表为 **CRAY 系列**。
  - **存储器-存储器模型（Memory-to-memory models）**：典型代表为 **Cyber 205**。

### 4.2 SIMD 超级计算机的 5 元组运行模型（Slide 63）
讲义第 63 页给出了 SIMD 计算机的形式化数学描述。一台 SIMD 机器的运行模型由一个 **5 元组（5-Tuple）** 完全确定：

$$
M = \langle N, C, I, M, R \rangle
$$

各分量定义如下：
- **$N$（Number of PEs）**：处理单元（Processing Elements）的数量。
  - 实例：Illiac IV 拥有 64 个 PE，Connection Machine CM-2 拥有 65,536 个 PE。
- **$C$（Control Unit Instructions）**：由控制单元（CU）**直接执行的指令集合**，包括标量运算和程序流程控制操作。
- **$I$（Broadcast Instructions）**：由控制单元（CU）**广播给所有 PE 并行执行的指令集合**。
- **$M$（Masking Schemes）**：掩码方案集合。每个掩码用于将全部 PE 划分为不同子集（决定哪些 PE 激活执行当前广播指令，哪些被屏蔽）。
- **$R$（Data-Routing Functions）**：数据路由通信函数集合，规定互连网络（Interconnection Networks, INs）中的各种数据交换模式。

---

## 学习目标 / Problem-Solving Skills

1. **并发与并行辨析**：准确陈述并发与并行的定义差异，画出四象限图并解释四种组合状态；说明为何盲目将并发与并行叠加可能导致性能损失。
2. **隐式 vs 显式并行**：写出隐式并行（顺序源码 $\to$ 并行化编译器）与显式并行（并行源码 $\to$ 保并发编译器）的处理链条。
3. **Flynn 分类掌握**：默写 SISD、SIMD、MISD、MIMD 的全称与含义，并指出多核服务器属于 MIMD。
4. **向量机架构分类**：说明向量处理器如何在标量与向量单元间分流数据，并列出 CRAY（寄存器-寄存器）与 Cyber 205（存储器-存储器）两大代表流派。
5. **SIMD 5 元组形式化默写**：完整默写出 $M = \langle N, C, I, M, R \rangle$ 并准确解释每个分量的定义（尤其注意 $C$ 是控制单元执行的标量/控制指令集，$I$ 是广播给 PE 的指令集）。

---

## 下一步

- 上一页：[[CEG5201-Week01-性能度量与计算吞吐率]]
- 下一页：[[CEG5201-Week01-多处理器体系结构与系统设计流]]
- 模块总览：[[CEG5201-讲义与笔记索引]]
- 返回知识库：[[Home]]

---

## 来源与更新日志

- 来源：[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) pp. 31–36, 45–48, 62–63.
- 2026-09-08：初始归档。
- 2026-09-23：依据原始课件重构：准确还原隐式/显式并行链（Slide 45）、并发与并行四象限图及 Slide 48 核心警告、Flynn 四大分类（Slide 31–33）、向量机双流派（CRAY vs Cyber 205，Slide 62）以及 SIMD 5 元组严格定义（Slide 63）。
