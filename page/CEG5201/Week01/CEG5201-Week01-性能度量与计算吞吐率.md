# 性能度量与计算吞吐率

> 本页属于：CEG5201 / Week 01
> 前置知识：[[CEG5201-Week01-嵌入式系统与计算平台选择]]
> 预计阅读时间：10 分钟

---

## 1. 程序执行周期与 CPU 时间（Program Performance Cycle）

讲义第 37 页指出，一个程序的典型执行周期包括：磁盘/内存访问、输入/输出活动、编译时间、操作系统响应时间以及实际的 **CPU 执行时间（CPU Time）**。

- **顺序处理系统（Sequential Processing）**：
  为最小化总周转时间，需最小化各独立时间之和：
  $$T^* = \min \sum_{k=1}^n T_k$$
- **多道程序并发环境（Multi-programmed Environment）**：
  I/O 和系统开销可以与其他程序所需的 CPU 时间重叠：
  $$T^* = \min \max \{ T_k \}$$
- **基准度量标准**：衡量系统最客观的基准是测量精确的 **CPU 时钟周期数** 或执行给定程序所需的 **CPU 时间**。

---

## 2. 核心性能参数与基本公式（Slides 38–40）

讲义第 38–40 页建立了处理器的基础性能度量方程：

### 2.1 时钟与指令参数
- **时钟周期时间（Clock Cycle Time, $\tau$）**：以纳秒（$\text{ns}$）计。
- **时钟频率（Clock Rate, $f$）**：主频以 $\text{MHz}$ 或 $\text{GHz}$ 计，满足：
  $$f = \frac{1}{\tau}$$
- **指令计数（Instruction Count, $I_c$）**：程序中动态执行的机器指令（Machine Instructions, MIs）总数。
- **平均每指令时钟周期（Clocks Per Instruction, CPI）**：不同机器指令所需时钟周期不同，讲义中使用 $\text{CPI}$ 均指代指令集的加权平均 $\text{CPI}$。

### 2.2 CPU 时间基础公式（Equation 1）
执行程序所需的 CPU 时间 $T$ 为：

$$
T = I_c \cdot \text{CPI} \cdot \tau = \frac{I_c \cdot \text{CPI}}{f}
$$

指令执行包含五个微步骤：取指（Instruction fetch）$\to$ 译码（Decode）$\to$ 取操作数（Operand fetch）$\to$ 执行（Execution）$\to$ 存储（Storage）。

### 2.3 考虑访存周期的展开公式（Equation 2）
完成一次存储器访问所需的时间称为**内存周期（Memory Cycle）**，通常为：

$$\text{Memory Cycle} = k \cdot \tau$$

其中比值 $k$ 取决于存储器制造技术。据此，讲义将 CPU 时间展开重写为：

$$
T = I_c \cdot (p + m \cdot k) \cdot \tau
$$

- $p$：每条指令译码与执行所需的**处理器内部周期数**
- $m$：每条指令所需的**存储器访问次数**
- $k$：访存周期与处理器时钟周期的比值（$k = \tau_{\text{mem}} / \tau$）
- $I_c$：指令总数
- $\tau$：处理器时钟周期时间

---

## 3. MIPS 指标与深入思考（Slides 41–42）

讲义第 41–42 页推导了处理器速率指标 **MIPS（Million Instructions Per Second，每秒百万条指令数）**。

### 3.1 MIPS 速率公式推导（Equation 3）
设执行程序所需的总时钟周期数为 $C = I_c \cdot \text{CPI}$，则 CPU 时间亦可写为 $T = C \cdot \tau = C / f$。

MIPS 速率定义为：

$$
\text{MIPS rate} = \frac{I_c}{T \cdot 10^6} = \frac{f}{\text{CPI} \cdot 10^6} = \frac{f \cdot I_c}{C \cdot 10^6}
$$

反之，执行时间可由 MIPS 表达为：

$$
T = \frac{I_c \cdot 10^{-6}}{\text{MIPS}}
$$

- MIPS 速率直接正比于时钟频率 $f$，反比于平均 $\text{CPI}$。
- 指令计数 $I_c$、$\text{CPI}$、主频 $f$ 以及总周期 $C$ 均会影响 MIPS 速率，且随程序不同而变化。

### 3.2 讲义思考题：Points to ponder!（Slide 42）
讲义在第 42 页提出了两个经典课堂思考题：
1. **当处理器主频已达到 GHz 级别时，为什么 MIPS 仍然是一个有用的参数？**
   - 它直观反映了处理器在特定程序上单位时间的纯指令吞吐能力。
2. **在什么情况下我们不能使用 MIPS 指标？为什么？**
   - 当对比**不同指令集架构（ISA）**（如 RISC 与 CISC）或不同编译器优化等级时不能简单使用 MIPS。因为不同架构下单条指令完成的工作量不同，指令数 $I_c$ 差异极大，MIPS 较高的处理器其程序真实执行时间 $T$ 反而可能更慢。

---

## 4. 吞吐率度量：系统吞吐率 vs 处理器吞吐率（Slide 43）

讲义第 43 页严格定义了吞吐率：系统单位时间内能执行的程序数量（Programs per unit time）。

### 4.1 处理器吞吐率（CPU Throughput, $W_p$）
单处理器理论上执行单一任务的吞吐率为执行时间的倒数：

$$
W_p = \frac{1}{T} = \frac{f}{I_c \cdot \text{CPI}} = \frac{\text{MIPS} \cdot 10^6}{I_c}
$$

### 4.2 系统吞吐率（System Throughput, $W_s$）
在真实多道程序运行环境中，系统吞吐率记为 $W_s$（单位通常为程序数/秒，$\text{programs/second}$）。

讲义明确强调了关键不等式：

$$
W_s < W_p
$$

- **原因**：在多任务并发系统中存在操作系统中断响应、进程调度与上下文切换、共享总线竞争等额外系统开销（Overheads）。
- **理想状态**：仅在零额外系统开销的极端理想情况下，才有 $W_s = W_p$。

---

## 5. 移动计算平台能效指标（Slide 44）

讲义第 44 页针对移动计算平台（Mobile Platforms）指出：
- 上述所有性能度量指标在移动端依然成立；
- 移动平台的性能指标必须考量为 **MIPS/mW（每毫瓦功耗交付的 MIPS）**；
- 大多数移动平台在实际运行中会采取**降频运行（Underclocked）**策略以有效控制发热和延长续航；
- 移动端最优的 CPU 是能够提供 **最大 MIPS/mW** 的处理器。

---

## 学习目标 / Problem-Solving Skills

1. **基本性能公式计算**：掌握 $T = I_c \cdot \text{CPI} \cdot \tau = I_c \cdot \text{CPI} / f$ 的计算，能在已知任意三个参数时求解第四个参数。
2. **访存展开公式运用**：熟练运用 $T = I_c (p + m \cdot k)\tau$，分析存储器周期倍率 $k$ 与每指令访存次数 $m$ 对程序总执行时间的拉长效应。
3. **MIPS 速率推导与局限性解释**：
   - 掌握 $\text{MIPS} = \frac{I_c}{T \cdot 10^6} = \frac{f}{\text{CPI} \cdot 10^6}$ 的推导及 $T = I_c \cdot 10^{-6}/\text{MIPS}$；
   - 能回答讲义思考题：解释为什么跨不同指令集架构对比时不能直接用 MIPS 评价机器优劣。
4. **吞吐率辨析**：计算单处理器理论吞吐率 $W_p = 1/T$，并解释为何在真实多道程序系统中必然存在 $W_s < W_p$。
5. **移动平台能效指标**：写出移动平台的关键能效指标 MIPS/mW，并解释移动端为何通常采取降频设计。

---

## 下一步

- 上一页：[[CEG5201-Week01-嵌入式系统与计算平台选择]]
- 下一页：[[CEG5201-Week01-并发并行与Flynn体系分类]]
- 模块总览：[[CEG5201-讲义与笔记索引]]
- 返回知识库：[[Home]]

---

## 来源与更新日志

- 来源：[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) pp. 37–44.
- 2026-09-08：初始归档。
- 2026-09-23：依据原始课件重构：准确还原程序执行周期（Slide 37）、基础铁律与访存展开模型 $T=I_c(p+mk)\tau$（Slide 38–40）、MIPS 闭式解与 Slide 42 两道课堂思考题、系统吞吐率不等式 $W_s < W_p$（Slide 43）以及移动端 MIPS/mW 指标（Slide 44）。
