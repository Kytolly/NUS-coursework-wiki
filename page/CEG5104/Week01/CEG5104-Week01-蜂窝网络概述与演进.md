# 蜂窝网络概述与演进

> 本页属于：CEG5104 / Week 01
> 前置知识：[[CEG5104-讲义与笔记索引]]
> 预计阅读时间：5 分钟

蜂窝网络的核心思想是：用多个**基站（BS）**把一片区域切成许多**小区（cell）**，每个基站覆盖自己的“服务范围”，基站之间接力，让用户不管走到哪儿都有人“接”。新加坡运营商就有上千个 5G 基站。小区还能用**定向天线**切成多个**扇区（sector）**；终端通常由**最近的基站**服务。（来源：1_network_planning.pdf 第 21 页。）

**历史与演进（终端世代）**：1864 年 Maxwell 预言无线电波，1886 年 Hertz 实验验证，1895–1901 年 Marconi 实现越距无线通信；1938 年出现第一台便携 AM 收音机（SCR-194/195，美陆军通信兵团制造，约 25 磅、5 英里射程）；1973 年 Motorola DynaTAC 原型机（DYNamic Adaptive Total Area Coverage）由副总裁 Martin Cooper 在非车载场景打通第一通私人移动电话；1980 年代迎来 1G。（来源：1_network_planning.pdf 第 2–8 页。）

| 世代 | 核心特征 | 代表制式/代表设备 | 关键变化 |
| --- | --- | --- | --- |
| 1G | 纯模拟 | NMT（1982 Mobira Senator）、AMPS（1983 DynaTAC，<2 磅、约 $4000） | 模拟语音，首次全自动国际蜂窝服务（NMT） |
| 2G | 数字加密 | GSM（1992 Motorola International 3200；1996 StarTAC 翻盖；1997 Nokia 9000 Communicator） | 数字化+加密，短信/低速数据，智能手机雏形 |
| 3G | 数据导向 | Palm（Treo 700w / Windows Mobile）、Motorola ROKR E1（2005）、iPhone（2007） | 移动互联网，语音与数据**并行**组网 |
| 4G | 全 IP | 2013 年后的 4G 手机 | 全 IP，EPC 核心网，语音走 VoLTE 类 |
| 5G | 现代智能机 | 现代 5G 智能手机 | 高吞吐、低时延、海量连接 |

**蜂窝基本概念**：**簇（cluster）**是一组相邻、内部不重复用频率的小区；频谱被分成**子带（sub-band）**，每个子带只用于簇内一个小区。小区大小：话务重的地方用小小区，话务轻的用大小区。小区类型依覆盖半径分：**宏小区**（约 6 英里直径，大功率、郊区/偏远）、**微小区**（约半英里，低功率、城市）、**微微小区**（楼宇/隧道）。注意“簇”与“子带”是一对多的映射：一个簇含 N_reuse 个小区，整个频谱被分成 N_reuse 组互不重叠的子带，同频子带仅分配给簇内不同位置的小区，这正是 Week 3 频率复用的雏形（N_reuse = i²+ij+j²、D/R = √(3·N_reuse)）。（来源：1_network_planning.pdf 第 22 页。）

**网络组件**：**BTS**（基站收发信机，小区主体，用多副天线收发信息）、**BSC**（基站控制器，经电缆或微波链路连接多个 BTS 并转接话务；课件把 Base 误拼为 Basic，标准叫法为 Base Station Controller）、**MSC**（移动交换中心，连接多个 BSC，并把蜂窝网接到 PSTN）。BTS+BSC 合称 **BSS**，MSC 与 PSTN 之间可再经 **GMSC**。3G 新增 **RNC**、**SGSN**、**GGSN**；4G 变为 **eNode-B**、**MME**、**HSS**、**S-GW**、**P-GW**。

| 组件 | 英文全称 | 主要职责 |
| --- | --- | --- |
| BTS | Base Transceiver Station | 小区主体，与移动台收发数据/语音 |
| BSC | Base Station Controller | 连接多个 BTS，BTS 间话务路由 |
| MSC | Mobile Switching Center | 蜂窝网协调者，连接多个 BSC，接 PSTN |
| RNC | Radio Network Controller | 3G 无线网络控制器，相当于 3G 版 BSC |
| SGSN/GGSN | Serving/Gateway GPRS Support Node | 3G 数据面：SGSN 会话管理、GGSN 接因特网 |
| eNode-B / EPC | evolved Node B / Enhanced Packet Core | 4G 基站与全 IP 核心网 |

**各代架构**：2G 语音为 `BTS–BSC（合称 BSS）–MSC–GMSC–PSTN`；3G 语音+数据**并行**组网，语音核心不变，数据经 SGSN→GGSN 到 Internet；4G 全 IP **EPC**，UE→eNode-B→S-GW/P-GW，控制面走 MME 与 HSS。

![3G 语音+数据并行组网架构](assets/CEG5104/fig-001-cellular-architecture.png)

图 1：3G（语音+数据）网络架构——语音核心网不变、数据网经 SGSN/GGSN 与语音网并行（来源：1_network_planning.pdf 第 26 页；核对 2026-09-07）。

**呼叫建立**：开机时手机扫描控制信道挑最强信号 → 发自身 ID 给 BTS → BTS 确认注册并分配信道。**发起呼叫**：拨号→BTS→BSC→MSC→对端 MSC→对端 BSC→对端 BTS。**接收呼叫**：空闲手机监听控制信道 → 收到含自身号码的分页消息 → 比对吻合回 ACK → 鉴权后接通。

```mermaid
flowchart LR
  MS -->|发起/接收| BTS --> BSC --> MSC -->|跨网络| 对端MSC --> 对端BSC --> 对端BTS --> 对端MS
```

图 2：蜂窝呼叫建立与接续链路（自制，依据 1_network_planning.pdf 第 28–31 页；核对 2026-09-07）。

## 下一步

- 上一页：[[CEG5104-讲义与笔记索引]]
- 下一页：[[CEG5104-Week01-网络规划流程与链路预算]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[1_network_planning.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5104/1_network_planning.pdf)，slide 2–13（历史/世代）、21–27（蜂窝概念/组件/架构）、28–31（呼叫建立/发起/接收）。
- 2026-09-07：从 Week 1 课件拆出该主题短页。
- 2026-09-07：补全内容并新增图解与原图（世代对比表、组件表、3G 架构原图 fig-001）。
