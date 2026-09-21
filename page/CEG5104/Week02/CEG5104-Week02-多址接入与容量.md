# 多址接入与容量

> 本页属于：CEG5104 / Week 02
> 前置知识：[[CEG5104-讲义与笔记索引]]
> 预计阅读时间：6 分钟

本页先快速回顾蜂窝网络与网络规划，再讲多址接入（multiple access）如何让多个用户共享频谱，最后用 GSM 做一次容量估算。

**回顾**：蜂窝网由基站（BTS）、小区（cell）、扇区（sector）组成，终端通常由最近的基站服务。2G 语音架构为 `BTS → BSC（BSS）→ MSC → GMSC → PSTN`；3G 新增的数据网与语音核心网**并行**（SGSN/GGSN 接入因特网）。网络规划分三步：无线网、传输网、核心网；无线网规划追求覆盖、容量、质量三者之间的成本最优，主导因素随地区而异（覆盖主导或容量主导）。（来源：2_capacity_analysis.pdf 第 3–8 页。）

**为什么需要多址**：多路用户共享同一段频谱资源。**复用（multiplexing）**让多用户共享昂贵的系统，同时引入排队/丢失：数据分组在发射/排队时产生**时延（delay）**，缓冲区满时新到分组被**丢弃（loss）**。（来源：2_capacity_analysis.pdf 第 9 页。）

**多址接入方式**（让多个用户共享频谱）：

| 方式 | 共享维度 | 用于 | 典型系统 |
| --- | --- | --- | --- |
| **FDMA** | 每个用户分一个**唯一频率** | 模拟系统 | AMPS |
| **TDMA** | 每个用户分一个**时隙**来收/发数据突发 | 数字系统 | GSM |
| **CDMA** | 每个用户分一个**码**去乘所发/收信号 | 扩频系统 | IS-95/3G |

**GSM 的多址**是细胞式 **FDM-TDMA**：FDM 作双工（duplexing）机制，TDMA 作复用（multiplexing）机制。系统带宽被划分为多个互不重叠的 FDM 频道；每个频道再把时间切成时隙，每个时隙分给不同用户。（来源：2_capacity_analysis.pdf 第 10–11 页。）

**GSM 容量示例**：可用带宽 $5\text{ MHz}$，保护带占 1 个频道，频道间隔 $200\text{ kHz}$，TDMA 每帧 8 时隙：

$$
\begin{aligned}
\text{FDM 频道数} &= \frac{5\text{ MHz}}{200\text{ kHz}} = 25 \\
\text{扣除 1 个保护频道} &\to 24\text{ 个频道} \\
\text{可承载呼叫数} &= 24 \times 8\text{ 时隙} = 192\text{ 路}
\end{aligned}
$$

（来源：2_capacity_analysis.pdf 第 12 页。）注：这里的“192 路”是**同时可服务的信道数**，不是 Erlang 容量；要换算成话务承载还需 Week 2 后段的呼损模型（Erlang-B）。

```mermaid
flowchart LR
  A[5 MHz 频谱] --> B[按 200 kHz 切分 => 25 个 FDM 频道]
  B --> C[扣除 1 个保护频道 => 24 个 FDM 频道]
  C --> D[每个频道切为 8 个 TDMA 时隙]
  D --> E[24 x 8 = 192 路可同时服务]
  E --> F[一个呼叫 = 频率 x 时隙 车位]
```

图 1：GSM FDM-TDMA 容量分解（自制，依据 2_capacity_analysis.pdf 第 11–13 页；核对 2026-09-07）。

类比：把一条大马路按频率分成若干条车道，每条车道再按时间分成 8 个车位；一个呼叫占用一个“频率 × 时隙”车位。这就是蜂窝 FDM-TDMA 容量的来源。需要提醒：把“频率”与“时隙”两个维度组合后，容量由两者乘积决定，但实际系统还存在**保护频带、双工间隔、信道间隔**等开销，因此“192 路”是理论最大同时服务数，并非可承载话务；换算为实际话务还需加上 Week 2 末尾的呼损模型（Erlang-B）。

## 下一步

- 上一页：[[CEG5104-Week01-容量初步与参数规划优化]]
- 下一页：[[CEG5104-Week02-话务建模与话务强度]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[2_capacity_analysis.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5104/2_capacity_analysis.pdf)，slide 3–13（回顾、多址接入、GSM 容量示例）。
- 2026-09-07：从 Week 2 课件拆出该主题短页。
- 2026-09-07：补全内容并新增图解与原图（FDMA/TDMA/CDMA 对比表、GSM 容量 Mermaid 图）。
