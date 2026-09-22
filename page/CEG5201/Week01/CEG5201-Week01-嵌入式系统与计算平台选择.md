# 嵌入式系统与计算平台选择

> 本页属于：CEG5201 / Week 01
> 前置知识：[[CEG5201-Week01-为什么需要现代并行平台]]
> 预计阅读时间：12 分钟

---

## 1. 嵌入式系统的定义与严苛约束

嵌入式系统（Embedded Systems）是指被内嵌在特定宿主设备内部、用于执行专门控制或计算任务的专用计算机系统（[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) 第 10–12 页）。与追求峰值平均吞吐率的桌面 PC 和服务器不同，嵌入式系统具有以下四个核心特征：

1. **资源极度受限（Resource-Constrained）**：片上 SRAM/DRAM 容量小、功耗上限（Thermal Design Power, TDP）极严（通常在毫瓦至数瓦范围）、硅片面积与物料成本（BOM Cost）受限。
2. **实时性约束（Real-Time Deadlines）**：
   - **硬实时（Hard Real-Time）**：系统必须在严格截止时间内产生输出，超时即判定为灾难性系统失效（例如汽车防抱死制动 ABS、安全气囊展开、航空飞控）。
   - **软实时（Soft Real-Time）**：偶发超时会导致服务质量（QoS）下降，但不会造成物理灾难（例如音视频解码帧丢失）。
3. **极高可靠性与容错（High Reliability & Safety）**：很多设备部署后处于无人值守或极端恶劣物理环境中，要求长期稳定无故障运行。
4. **能效驱动（Energy-Awareness）**：移动终端与物联网边缘节点通常依赖有限的电池供电，能耗直接决定了设备的生命周期。

---

## 2. 嵌入式系统典型硬件架构框图

讲义第 10 页给出了现代嵌入式系统的经典功能框图，体现了其“异构计算组件 + 模拟/数字接口 + 专用外设”的典型组织形式：

![嵌入式系统硬件架构框图](assets/CEG5201/chap1/fig10_embedded_system_diagram.png)

### 核心子系统职能划分
- **通用微处理器 / 微控制器（Microprocessor / MCU）**：执行系统控制流、运行轻量级实时操作系统（RTOS）或固件、协调各外设工作。
- **专用集成电路 / 加速器（ASICs / Coprocessors）**：针对高吞吐率算法（如音视频编解码、密码学散列、神经网络前向推理）进行全定制或半定制硬件固化。
- **混合信号转换模块（A/D & D/A Converters）**：
  - **A/D（模数转换器）**：将物理世界传感器采集的连续模拟信号（温度、压力、声波、电磁信号）离散量化为数字信号供处理器计算。
  - **D/A（数模转换器）**：将计算处理后的数字指令还原为模拟控制电压/电流，驱动电机、执行器或扬声器。
- **分级存储系统（Memory Subsystem）**：
  - 片内高速 SRAM：存放时间敏感的中断向量表、关键循环代码与临时数据。
  - 片外/片内 Flash (ROM)：存放不可变系统固件与启动引导程序（Bootloader）。
  - DRAM：用于大规模数据缓冲。

---

## 3. 核心能耗建模与动态电压调节（DVS）

在现代芯片体系结构中，CMOS 数字电路的能量消耗是系统设计的首要物理约束（讲义第 12–15 页）。

### 3.1 CMOS 动态功耗模型
CMOS 电路在开关翻转过程中对负载电容充放电产生的动态功耗（Dynamic Power）建模为：

$$
P = \frac{1}{2} \cdot f \cdot C \cdot V_{dd}^2
$$

- $f$：处理器工作时钟频率（Clock Frequency）。
- $C$：电路节点等效开关负载电容（Effective Load Capacitance）。
- $V_{dd}$：芯片供电电源电压（Supply Voltage）。

### 3.2 门延迟与最高工作频率的物理约束
MOSFET 晶体管的栅极传播延迟（Propagation Delay）$\tau_{gate}$ 反比于饱和驱动电流，由长沟道晶体管的 $\alpha$-功率律（$\alpha$-power law）可知：

$$
\tau_{gate} \propto \frac{V_{dd}}{(V_{dd} - V_T)^\alpha} \implies f_{max} \propto \frac{(V_{dd} - V_T)^\alpha}{V_{dd}}
$$

- $V_T$：晶体管开启阈值电压（Threshold Voltage）。
- 在讲义模型中取经典理想状态 $\alpha = 2$：
  $$f = k \cdot \frac{(V_{dd} - V_T)^2}{V_{dd}}$$
- **核心结论**：供电电压 $V_{dd}$ 决定了晶体管的最大充放电驱动电流，因而直接决定了处理器所能达到的最高工作时钟频率 $f$。

### 3.3 动态电压调节（Dynamic Voltage Scaling, DVS）的节能效益
若一个计算任务包含 $N_{\text{cycle}}$ 个时钟周期，完成该任务所需的总时间为 $T = N_{\text{cycle}} / f$。该任务消耗的动态总电能 $E$ 为：

$$
E = P \cdot T = \left( \frac{1}{2} \cdot f \cdot C \cdot V_{dd}^2 \right) \cdot \left( \frac{N_{\text{cycle}}}{f} \right) = \frac{1}{2} \cdot C \cdot N_{\text{cycle}} \cdot V_{dd}^2
$$

- **非线性平方级收益**：**总能量消耗 $E$ 与时钟频率 $f$ 在一阶近似下无关，而严格正比于供电电压的平方 $V_{dd}^2$！**
- **DVS 的工作机制**：当系统检测到计算任务存在充裕的松弛时间（Slack Time）或处于轻载时，通过降低时钟频率 $f$，使电路能够安全运行在显著降低的供电电压 $V_{dd}$ 下。
- **示例对比**：若将 $V_{dd}$ 降低至原值的 $0.7$ 倍（频率同步下调至约 $0.5$ 倍）：
  - 功耗降至 $P_{\text{new}} \approx 0.5 \times (0.7)^2 \times P_{\text{old}} \approx 0.245 \cdot P_{\text{old}}$（功耗降低约 $75\%$）；
  - 尽管执行时间翻倍（$T_{\text{new}} = 2 T_{\text{old}}$），总能耗却降至 $E_{\text{new}} = (0.7)^2 \cdot E_{\text{old}} \approx 0.49 \cdot E_{\text{old}}$（净节省超过 $50\%$ 的宝贵电能）。

### 3.4 软硬件能耗优化协同体系

| 优化维度 | 硬件工程技术（Hardware Techniques） | 软件工程技术（Software Techniques） |
| :--- | :--- | :--- |
| **时钟与电压管理** | 动态电压与频率调节（DVFS）、自适应电压缩放（AVS）。 | 基于任务截止时间的松弛调度算法（Slack-Aware Scheduling）、CPU 频率调节器（Governor）。 |
| **静态漏电控制** | 细粒度时钟门控（Clock Gating）、多阈值 CMOS（MTCMOS，非关键路径使用高 $V_T$ 抑制漏电）、电源岛休眠（Power Gating）。 | 批处理减少唤醒次数（Duty Cycling）、低功耗模式深度休眠管理。 |
| **存储访问优化** | 片上分级缓存、预取缓冲（Prefetch Buffer）、片上暂存器（Scratchpad Memory）。 | 循环分块（Loop Tiling）提升缓存命中率、数据结构内存对齐减少突发传输浪费。 |

---

## 4. 计算平台谱系：灵活性 vs 性能/能效（Flexibility vs Performance）

在嵌入式与边缘计算系统中，选择计算平台本质上是在**设计灵活性（Flexibility）**与**执行能效/性能（Performance & Efficiency）**之间进行工程权衡（讲义第 16–22 页）：

![性能与灵活性权衡谱系](assets/CEG5201/chap1/fig16_performance_vs_flexibility.png)

讲义第 22 页进一步补充了在内存性能受限下各平台的定位关系：

![内存受限下的性能与灵活性](assets/CEG5201/chap1/fig22_memory_performance_flexibility.png)

### 平台五大核心类别全方位横向对比

| 硬件平台 | 体系结构代表 | 灵活性 (Flexibility) | 峰值能效比 (Energy Efficiency) | NRE 研发成本 & 周期 | 典型适用场景 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **通用处理器 (GPP)** | ARM Cortex-A, x86, RISC-V | **极高**（完全通过高级语言软件编程，修改成本为零） | **低**（指令译码、乱序调度等控制逻辑开销占比超 $70\%$） | 极低，即买即用 | 复杂人机交互、多任务操作系统调度、频繁变动的控制流逻辑。 |
| **数字信号处理器 (DSP)** | TI TMS320, Qualcomm Hexagon | **高**（软件可编程，具备专属 MAC 硬件与环形寻址指令） | **中偏高**（针对特定流式信号运算高度优化，硬件开销低于 GPP） | 低，依赖成熟 C/C++ 编译器与 DSP 专用库 | 无线基带滤波、音频编码、电机闭环数字控制。 |
| **专用指令集处理器 (ASIP)** | Tensilica Xtensa, Synopsys ARC | **中等**（在可配置核心基座上自定义特定微架构指令） | **高**（消除通用指令浪费，为特定领域算子定制硬件数据通路） | 中等，需专用 EDA 编译链自动生成工具 | 专用传感器前端处理、特定加密协议加速。 |
| **现场可编程门阵列 (FPGA)** | AMD/Xilinx UltraScale, Intel Agilex | **中高**（纯硬件电路重构，出厂后可通过比特流重新配置） | **高**（纯硬件硬件流水线，但因可编程开关阵列存在电容开销） | 中高，Verilog/VHDL 门级综合，开发验证周期长 | 5G 前传物理层处理、雷达高速接口采集、AI 算法前期硬件原型验证。 |
| **专用集成电路 (ASIC)** | Google TPU, Apple Neural Engine | **极低**（硅片掩膜流片后硬件逻辑完全固定，无法更改） | **极致最高**（晶体管利用率极高，电路完全贴合目标算法，无任何控制开销） | 极高（单次流片 NRE 成本数百万至数千万美元，周期 1–2 年） | 大规模量产消费电子（手机 SoC）、超大规模云计算专用 AI 推理加速。 |

---

## 5. 硬件加速（Hardware Acceleration, HA）准则

讲义第 25 页提出：**硬件加速（HA）是指将计算密集型任务从通用主处理器（Host CPU）卸载到专用硬件加速设备上执行**。

### 5.1 加速收益的数学成立条件
设一个计算任务在 CPU 上的执行时间为 $T_{\text{CPU}}$。将该任务卸载到硬件加速器执行时，总时间包含三部分：
1. 主存到加速器设备的数据传输时间：$T_{\text{host-to-device}}$
2. 加速器硬件核心的实际运算时间：$T_{\text{kernel}}$
3. 运算结果从加速器回传主存的时间：$T_{\text{device-to-host}}$

硬件加速产生净性能增益的充要条件是：

$$
T_{\text{host-to-device}} + T_{\text{kernel}} + T_{\text{device-to-host}} < T_{\text{CPU}}
$$

净加速比（Net Speedup）定义为：

$$
S_{\text{net}} = \frac{T_{\text{CPU}}}{T_{\text{transfer}} + T_{\text{kernel}}} \quad (\text{其中 } T_{\text{transfer}} = T_{\text{host-to-device}} + T_{\text{device-to-host}})
$$

### 5.2 适合硬件加速的任务特征
- **高计算访存比（High Arithmetic Intensity）**：每搬运 1 字节数据需要执行数千次甚至数万次数学运算（如深度学习 GEMM、高维 FFT），使得 $T_{\text{kernel}}$ 远大于 $T_{\text{transfer}}$。
- **高数据级并行度（Massive DLP）**：数据间无复杂的循环交叉依赖，可天然展开为多流水级或宽阵列执行。
- **低控制分支分散度（Low Divergence）**：控制流规整，无繁琐的复杂动态跳转判断。

---

## 6. 深度架构剖析：FPGA 与 GPU

### 6.1 FPGA 内部微架构：细粒度位级可重构
讲义第 23 页展示了现代 FPGA 的典型内部组织结构：

![FPGA 可配置逻辑块微架构](assets/CEG5201/chap1/fig23_fpga_clb_architecture.png)

- **可配置逻辑块（Configurable Logic Blocks, CLBs）**：FPGA 的基本计算单元。每个 CLB 包含多个 Slice，每个 Slice 内集成：
  - **查找表（LUTs, Look-Up Tables）**：通常为 6 输入 LUT（6-LUT），本质上是微型高速 SRAM，能够实现任意 6 输入布尔逻辑函数。
  - **触发器与寄存器（Flip-Flops / Latches）**：用于暂存状态，构建深度硬件流水线。
  - **快速进位链（Fast Carry Chains）**：专用于高效实现加法器与累加器。
- **可编程互连网络（Programmable Interconnects）**：由水平和垂直布线通道及可编程开关矩阵（Switch Boxes）组成，负责任意逻辑块之间的低延迟布线。
- **硬核辅助单元**：现代 FPGA 内嵌大容量分布式 **Block RAM (BRAM)** 与专属 **DSP Slices**（内含 18×25 乘加器 MAC），以弥补用纯 LUT 搭建乘法器导致的面积与频率劣势。

### 6.2 NVIDIA Fermi GPU 体系结构：经典大规模并行典范
讲义第 24 页深入剖析了开启现代通用 GPU 计算（GPGPU）纪元的 NVIDIA Fermi 体系结构：

![NVIDIA Fermi GPU 架构图](assets/CEG5201/chap1/fig24_fermi_cuda_architecture.png)

- **全局宏观结构**：
  - 包含 4 个独立的**图形处理集群（Graphics Processing Clusters, GPCs）**。
  - 共集成 16 个**流多处理器（Streaming Multiprocessors, SMs）**，通过高带宽片上交叉开关总线互连。
  - 底部集成 6 组 64 位 GDDR5 显存控制器（构成 384-bit 全局存储接口）与统一的 **768 KB L2 Cache**。
- **单流多处理器（SM）微架构**：
  - 每个 SM 包含 **32 个 CUDA 核心**（每个核心包含完整的单精度浮点 ALU 与定点整型 ALU）。
  - **双 Warp 调度器与指令分发单元（Dual Warp Scheduler）**：能够同时调度并交错发射两个独立 Warp（每个 Warp 为 32 个线程的锁步执行集合）。
  - **可配置高速片内存储（64 KB SRAM）**：在硬件上允许灵活划分为“16 KB L1 Cache + 48 KB 共享内存（Shared Memory）”或“48 KB L1 Cache + 16 KB 共享内存”，由程序员根据算法的数据复用特征自行决策。

---

## 考试时你应该会什么

1. **公式推导与计算**：
   - 熟练写出 CMOS 动态功耗模型公式 $P = \frac{1}{2} f C V_{dd}^2$，并能结合频率-电压关系 $f \propto \frac{(V_{dd}-V_T)^2}{V_{dd}}$ 推导 DVS 下能耗 $E$ 与电压 $V_{dd}^2$ 的正比关系。
   - 能够计算在电压降至 $\alpha V_{dd}$、频率降至 $\beta f$ 时，功耗 $P$ 与总任务能耗 $E$ 的具体衰减百分比。
2. **定性分析与选型决策**：
   - 给出具体的工程场景（如超低功耗助听器、5G 基站前传、通用办公笔记本、数据中心千万级并发大模型推理），能够从灵活性、能效比、NRE 研发成本三轴进行平台选型论证。
   - 能够定量列出硬件加速（HA）带来净性能提升的充要条件，指出哪些算法特征适合卸载至 FPGA/GPU。
3. **架构机制理解**：
   - 说明 FPGA 中 LUT（查找表）如何实现布尔组合逻辑；
   - 描述 GPU 中 Warp 调度的基本概念以及共享内存（Shared Memory）在隐藏显存访存延迟中的作用。

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
- 2026-09-23：重构扩写，推导 DVS 动态功耗与二次能耗公式，补全 FPGA CLB 与 NVIDIA Fermi 核心图解及微架构细节，增加硬件加速卸载判定准则。
