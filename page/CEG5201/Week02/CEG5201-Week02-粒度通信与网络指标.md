# 粒度、通信与网络指标

> 本页属于：CEG5201 / Week 02
> 前置知识：[[CEG5201-Week02-Bernstein条件与软件并行性]]
> 预计阅读时间：8 分钟

## 粒度

粒度是一个并行任务包含的计算量。指令/循环通常是细粒度，过程/子程序是中粒度，作业级是粗粒度。细粒度暴露更多并行性，但需要更多同步；粗粒度降低通信次数，却可能降低负载均衡。

## 通信规模

若 `n` 个任务两两通信，潜在交互数最多为：

`n(n−1)/2`

广播或多播可以减少重复发送，但具体收益依赖拓扑和通信模式。

## 网络基本指标

对互连图 `G=(V,E)`：

- distance：两节点间最短路径长度；
- diameter：所有节点对距离的最大值；
- degree：节点的 incident links 数量；
- node-connectivity：使网络断开的最少节点删除数；
- f-fault diameter：删除最多 `f` 个节点后的最坏直径。

## 复习链

```mermaid
flowchart LR
    A[依赖关系] --> B[可用并行度]
    B --> C[任务粒度]
    C --> D[通信/同步开销]
    D --> E[网络与编程模型]
```

图 1：从依赖到网络选择的复习链（自制，依据 Chapter 2 pp.22–33；核对于 2026-09-01）。

## 下一步

- 上一页：[[CEG5201-Week02-Bernstein条件与软件并行性]]
- 下一页：[[CEG5201-Week03-MIN结构与路由]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[CG5201_Chap2 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap2%20%282627%29.pdf)，pp.22–33；[Chap 2_1_TenNodeFine_vs_Coarse_Grain_Scheduling.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_1_TenNodeFine_vs_Coarse_Grain_Scheduling.pdf)；个人参考 `notebook/lecture2.md`。
- 2026-09-01：拆出粒度、通信和网络指标短页。