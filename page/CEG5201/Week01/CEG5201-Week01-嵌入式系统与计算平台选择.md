# 嵌入式系统与计算平台选择

> 本页属于：CEG5201 / Week 01
> 前置知识：[[CEG5201-Week01-为什么需要现代并行平台]]
> 预计阅读时间：11 分钟

---

## 1. 嵌入式系统与典型硬件架构

讲义第 10 页定义了嵌入式系统（Embedded Systems），并给出了其经典组成框图：

![嵌入式系统硬件架构框图](assets/CEG5201/chap1/fig10_embedded_system_diagram.png)

### 1.1 系统核心组成部分
根据讲义第 10 页框图，嵌入式系统由以下核心模块协同构成：
- **微处理器（Microprocessor）**：执行系统控制流与通用运算。
- **专用集成电路（ASICs）**：负责固定算法加速与协处理任务。
- **存储器子系统（Memories）**：包含 SRAM、DRAM 以及用于保存固件程序的 Flash/ROM。
- **模数 / 数模转换器（A/D & D/A Converters）**：连接外部物理世界，将模拟传感信号数字化，并将数字控制量转换为模拟执行信号。
- **传感器与执行器（Sensors & Actuators）**：负责环境感知与物理动作输出。
- **通信接口（Communication Interface）**：负责芯片与外设或网络之间的数据交互。

讲义第 11–12 页进一步指出，现代嵌入式系统在设计实现中面临性能、成本、面积、实时性以及**能耗感知计算（Energy Aware Computing）**的多重严格约束。

---

## 2. 能耗问题与动态电压调节（DVS）

在现代芯片体系中，能耗问题需要硬件工程与软件工程协同优化（讲义第 12–15 页）。

### 2.1 软硬件能耗优化分工（Slides 13 & 15）
- **硬件工程优化（Hardware Optimization）**：
  - 电路级优化（Circuit-level optimization）
  - 体系结构级动态电压与频率调节（DVFS）
  - 门控电源技术（Power gating）
- **软件设计侧重点（Software Design Emphasis）**：
  - 核心目标是最小化能耗（Minimize energy consumption）：
    - 指令级优化（Instruction level）
    - 算法级优化（Algorithm level）
    - 任务调度优化（Task scheduling）

### 2.2 动态电压调节（DVS）的数学建模（Slide 14）
CMOS 数字电路在翻转过程中的动态功耗建模为：

$$
P = 0.5 \cdot f \cdot C \cdot V_{dd}^2
$$

- $f$：工作时钟频率（Clock Frequency）
- $C$：开关负载电容（Capacitance）
- $V_{dd}$：供电电压（Supply Voltage）

门电路传播延迟与供电电压满足物理关系，最大频率 $f$ 表达为：

$$
f = k \cdot \frac{(V_{dd} - V_T)^2}{V_{dd}}
$$

- $V_T$：晶体管开启阈值电压（Threshold Voltage）
- $k$：与工艺相关的常数

由此可知供电电压是频率的函数 $V_{dd} = F(f)$，功耗公式可改写为：

$$
P = 0.5 \cdot f \cdot C \cdot [F(f)]^2
$$

> **DVS 核心原理**：
> 降低时钟频率 $f$ 允许相应地降低供电电压 $V_{dd}$。由于功耗与电压平方成正比，降低工作频率和电压能够带来显著的非线性功耗下降。

---

## 3. 计算平台谱系：性能 vs 灵活性（Performance vs Flexibility）

在选择计算系统时，讲义第 16–20 页给出了不同硬件平台在**性能（Performance）**与**灵活性（Flexibility）**维度的定性分析与权衡谱系：

![性能与灵活性权衡谱系](assets/CEG5201/chap1/fig16_performance_vs_flexibility.png)

- **灵活性（Flexibility）的定义**：系统的易用性，以及适应规格说明变动（Adapt to changes in specifications）的能力。

### 讲义第 17–20 页归纳的 7 个核心观察要点
1. **最高性能平台**：ASICs 与 GPGPUs 拥有最高的计算性能。
2. **ASIC 与 GPGPU 的权衡**：ASIC 灵活性的不足由其**极高的能效比**得到弥补；相比之下，GPGPU 性能极为出色（并配有软件支持），但**极其消耗电能（extremely power consuming）**。
3. **多核（Multicore）的定位**：当应用的内在并行性与多核架构匹配时，多核处理器的性能相对接近 GPGPU。
4. **并行模式的区别**：GPGPU 充分开发**数据并行性（Data Parallelism）**，而多核系统最适合处理**多任务并发（Multi-Tasking）**。
5. **DSP 的灵活性**：在灵活性方面，DSP 处理器优于单通用微处理器/微控制器，因为 DSP 是针对特定功能定制设计的。
6. **FPGA 与微处理器的对比**：与单通用微处理器相比，传统 FPGA 灵活性相对较低，因为微处理器采用**基于软件的方案**，而 FPGA 采用**基于硬件的方案**。
7. **可重构 FPGA 的优势**：存在能够在运行期间动态重构的 FPGA。重构 FPGA 本质上只需向其配置存储器中写入新数值，因此在理想情况下可视为与软件平台一样灵活。**FPGA 介于 ASIC 与软件系统之间：既具备接近硬件的速度，又兼具接近软件的灵活性**。

讲义第 21 页进一步列出不同技术的工具链与设计方法学：Microcontrollers/CPUs、DSP Processors、Multicore Processors & GPGPUs、FPGAs、ASICs。

---

## 4. 灵活硬件与硬件加速（HA）

### 4.1 灵活硬件实例一：FPGA 架构（Slide 23）
讲义第 23 页展示了现场可编程门阵列（FPGA）的基本组织结构：

![FPGA 可配置逻辑块微架构](assets/CEG5201/chap1/fig23_fpga_clb_architecture.png)

- FPGA 由可编程逻辑块阵列（Logic Blocks）、I/O 块（I/O Blocks）和布线通道（Routing Channels）构成，可通过编程实现自定义数字电路。

### 4.2 灵活硬件实例二：GPU - Fermi CUDA 架构（Slide 24）
讲义第 24 页给出了经典的 NVIDIA Fermi GPU 体系结构图：

![NVIDIA Fermi GPU 架构图](assets/CEG5201/chap1/fig24_fermi_cuda_architecture.png)

- 包含 512 个 CUDA 核心，划分为多个流多处理器（Streaming Multiprocessors, SM），辅以 GigaThread 调度引擎、L2 高速缓存以及外部 DRAM 接口。

### 4.3 硬件加速（Hardware Acceleration, HA）定义与特征（Slide 25）
讲义第 25 页明确界定了硬件加速（HA）：
- **定义**：将任务从软件卸载（Offload）到能够比软件更快执行这些任务的专用设备/硬件上。
- **适用场景特征**：
  - 高计算需求（High computational demand）
  - 高数据吞吐率（High data rate）
  - 能耗效率成为关键考量（Energy efficiency is an issue）
- **典型实现载体**：GPU、FPGA、专用加密硬件（Cryptographic hardware）。

---

## 学习目标 / Problem-Solving Skills

1. **嵌入式架构认知**：熟记嵌入式系统的核心组件（处理器、ASIC、存储器、A/D 与 D/A、传感器/执行器）。
2. **DVS 能耗计算**：熟练写出动态功耗公式 $P = 0.5 \cdot f \cdot C \cdot V_{dd}^2$，理解频率与供电电压的关联 $f \propto (V_{dd}-V_T)^2 / V_{dd}$，掌握通过降频降压实现非线性节能的物理原理。
3. **平台权衡与选型**：熟记讲义关于 ASIC、GPGPU、Multicore、DSP、FPGA、CPU 的 7 点核心定性对比，能够根据能耗、灵活性与数据并行特性进行合理选型。
4. **硬件加速判定**：说明硬件加速（HA）的定义及其适用的三种计算特征。

---

## 下一步

- 上一页：[[CEG5201-Week01-为什么需要现代并行平台]]
- 下一页：[[CEG5201-Week01-性能度量与计算吞吐率]]
- 模块总览：[[CEG5201-讲义与笔记索引]]
- 返回知识库：[[Home]]

---

## 来源与更新日志

- 来源：[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) pp. 10–25.
- 2026-09-08：初始归档。
- 2026-09-23：依据原始课件重构：准确还原嵌入式框图（Slide 10）、DVS 公式与软硬件分工（Slide 13–15）、平台谱系与 7 点核心定性观察（Slide 16–20）、FPGA 架构图（Slide 23）、Fermi 架构图（Slide 24）以及硬件加速判定特征（Slide 25）。
