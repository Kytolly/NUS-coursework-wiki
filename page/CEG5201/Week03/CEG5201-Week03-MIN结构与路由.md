# MIN 的结构与路由

> 本页属于：CEG5201 / Week 03
> 前置知识：[[CEG5201-Week02-粒度通信与网络指标]]
> 预计阅读时间：8 分钟

## MIN 是什么？

多级互连网络（Multistage Interconnection Network, MIN）用若干级小型交换单元把一组处理器/输入端与一组存储器/输出端互连起来（[Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf) 第 1 页）。它的目标是在可接受硬件成本下提供低延迟、高带宽与可扩展通信。讲义列举的网络族包括 CLOS、baseline、Omega；现代 AI 加速器（Google TPU pods、Cerebras Wafer-Scale Engine）与 HPC/数据中心（InfiniBand、Ethernet 的 CLOS/fat-tree）仍在使用这类多级交换结构（[CG5201_Chap2 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap2%20%282627%29.pdf) 第 34–35 页）。

## 设计空间：四个维度

讲义把互连网络的设计空间写成笛卡尔积（第 1–2 页）：

- **操作方式（Operation）**：同步与异步。
- **控制策略（Control Strategy）**：对交换单元的控制是集中式还是分布式。
- **交换策略（Switching Strategy）**：电路交换（circuit switching）与包交换（packet switching）。
- **网络拓扑（Network Strategy）**：静态（linear array、star、bus、ring、tree、mesh、systolic array、complete graph、n-cube）与动态（single-stage、multi-stage、crossbar）。

单级动态网络如 **shuffle-exchange** 属于“再循环网络”，数据可能要绕行多次才到达目的地（第 2、4 页）。多级网络能连接任意输入到任意输出，分一面/两面（input 与 output 同侧或两侧）（第 3 页）。

## Baseline 网络与自路由

Baseline 网络是基于**完美洗牌（perfect shuffle）**交换模式的再循环/多级网络。对 `n` 位地址 `(x_{n−1},…,x_0)`，`Shuffle` 把最高位移到最低位（第 4 页）。Baseline 的每级由 2×2 交换单元组成，控制位按目的地址的比特从 MSB 到 LSB 决定“0-上、1-下”，因此具有**自路由（self-routing）**能力（第 5 页）。对 `N=2^n` 个端点的典型二元 MIN，约需 `n=log2 N` 级；每级、每路的控制与级数取决于网络族与讲义图示。

![Baseline MIN 网络：自路由与地址标签](assets/CEG5201/fig-003-baseline-min.png)

图 1：Baseline MIN 网络（自路由、地址标签、0-上/1-下）；来源：[Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf) 第 5 页；核对 2026-09-07。

## 级数与路径的注意点

自路由实现简单、延迟可预测，但确定性的路径选择容易形成热点。讲义提醒：这一部分（第 35 页）是教师自编材料，考试以课堂 Canvas slides 为准；因此本页只描述结构与路由机制，不把“具体级数/单元数/路径数”当作统一公式。

## 多级网络的分类

讲义把多级网络按能否同时建立任意连接分为三类（第 3 页）：

- **Blocking**：`Baseline`、`Omega`、二元 `n-cube` 会在同时连接多对终端时争用公共链路。
- **Rearrangeable（可重排非阻塞）**：如 `Benes`，可通过重排已有连接完成所有可能连接。
- **Non-blocking（非阻塞）**：如 `CLOS`，能处理所有可能连接而不阻塞。

多级网络还分**一侧**（input 与 output 同侧）与**两侧**（分处两侧）（第 3 页）。设计目标（第 1 页）是在硬件成本与阻塞概率之间折中，连接成千上万处理单元并保持低延迟、高带宽与可扩展。单段 shuffle-exchange 属再循环网络，数据可能要多次绕行；多级网络则可一次到达目的端。

## 路由和阻塞的边界

单路径 Banyan/Omega/Baseline 类网络通常会发生**阻塞**（blocking）：两个连接各自的输入、输出都空闲，但会在中间链路/交换单元争用（第 3 页）。这里的“阻塞”是连接状态造成的资源争用，与网络直径（拓扑最坏距离）是不同的概念。

## 下一步

- 上一页：[[CEG5201-Week02-粒度通信与网络指标]]
- 下一页：[[CEG5201-Week03-Blocking与CLOS]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf) 第 1–5 页；Chapter 2 context pp.34–35；个人参考 `notebook/lecture3.md`。
- 2026-09-01：拆出 MIN 结构和路由短页。
- 2026-09-07：扩写设计空间四维度、shuffle/Baseline 自路由与阻塞边界，新增 Baseline 原图（第 5 页）。
