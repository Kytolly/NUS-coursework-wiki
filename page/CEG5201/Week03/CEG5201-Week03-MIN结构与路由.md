# MIN 的结构与路由

> 本页属于：CEG5201 / Week 03
> 前置知识：[[CEG5201-Week02-粒度通信与网络指标]]
> 预计阅读时间：8 分钟

## MIN 是什么？

Multistage Interconnection Network（MIN）用多级小型交换单元连接输入端与输出端。它像把一个大型交换站拆成多排小道闸：每一级根据目的地址的一部分决定直通或交叉。

## 路由和规模

典型二元 MIN 在 `N=2^n` 个端点时约有 `log2 N` 级，但精确级数、单元数量和路径数取决于网络族及课堂图示。路由算法在各级消耗目的地址比特，确定性强但可能形成热点。

## 网络目标

设计需要平衡低延迟、高带宽、可扩展性和硬件成本。讲义列举 CLOS、baseline、Omega 等网络族；它们的路径选择和阻塞性质不能混为一谈。

```mermaid
flowchart LR
    I[输入端] --> S1[交换级 1]
    S1 --> S2[交换级 2]
    S2 --> SN[交换级 n]
    SN --> O[输出端]
```

图 1：MIN 多级路由概念图（自制，依据 [Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf)；核对于 2026-09-01）。

## 下一步

- 上一页：[[CEG5201-Week02-粒度通信与网络指标]]
- 下一页：[[CEG5201-Week03-Blocking与CLOS]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf)；Chapter 2 context pp.34–46；个人参考 `notebook/lecture3.md`。
- 2026-09-01：拆出 MIN 结构和路由短页。