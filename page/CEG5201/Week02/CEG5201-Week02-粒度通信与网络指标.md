# 粒度、通信与网络指标

> 本页属于：CEG5201 / Week 02
> 前置知识：[[CEG5201-Week02-Bernstein条件与软件并行性]]
> 预计阅读时间：8 分钟

## 粒度

粒度（grain size / granularity）是一个并行任务包含的计算量，可用指令数近似（[CG5201_Chap2 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap2%20%282627%29.pdf) 第 22–23 页）：

| 层次 | 粒度 | 说明 |
|---|---|---|
| 指令级 / 循环级 | 细（2–1000 条指令） | 编译器辅助（隐式并行）；循环迭代控制独立时可向量化/流水化（第 24 页） |
| 过程 / 子程序级 | 中（<2000 条指令） | 多任务；依赖提取较烦，需程序员重构（第 25 页） |
| 作业级 | 粗 | 独立作业放到不同处理器；时间/空间共享（第 26 页） |

细粒度暴露更多并行度，但同步和通信更多；粗粒度降低通信次数，却可能减少并行度并恶化负载均衡。讲义举早期 Kruatrachue 与 Lewis（1988）的 grain packing and scheduling 演示说明粒度的选择（第 28 页），并关联 `Chap 2_1_TenNodeFine_vs_Coarse_Grain_Scheduling.pdf` 与扫描页 7–8；这些为扫描辅助材料，具体例题标注 Open。

## 通信规模

通信延迟除链路延迟外，还由通信模式决定（第 27 页）。若 `n` 个任务两两通信，潜在交互数最多为：

`n(n−1)/2`

因此通信成本可呈二次增长，给可用处理器数量设定上限。广播（broadcasting）与多播（multicasting）可减少重复发送，但收益取决拓扑与通信模式。

## 网络基本指标

对互连图 `G=(V,E)`（第 30–33 页）：

- **distance(u,v)**：最短路径长度；
- **diameter d**：所有节点对距离的最大值 `d = max Distance(u,v)`，衡量最坏通信延迟；
- **degree deg(u)**：节点 incident 的链路数；若所有节点度数均为 `δ`，称为 `δ`-regular；
- **节点不连通度（node-connectivity K）**：使网络断开的最少节点删除数，是容错度量；
- **f-fault diameter**：删除至多 `f` 个节点后的最坏直径。

对 `δ`-regular 网络，成本常记作 `C = d·δ`，而 packing density = 节点数/成本，packing density 越高，所需 VLSI 芯片面积越小（第 32 页）。可对 mesh、hypercube、ring 等标准图核算上述指标（第 33 页）。

## 其他术语与静态/动态网络

- **延迟（latency）**：机器子系统间通信开销的时间度量，如内存延迟、同步延迟（第 23 页）；通信延迟由链路延迟与通信模式共同决定。
- **node-disjoint 路径**：两条路径除端点 `u`、`v` 外无其他公共节点，是多路径路由与容错设计的基础（第 31 页）。
- 网络可分**静态**（点对点、mesh、hypercube、ring、tree、star 等，链路固定）与**动态**（总线、crossbar 等，物理/逻辑链路随连接变化）两大类（第 29–30 页）。

静态规则图可核算 diameter、degree、node-connectivity 等指标，便于做折中；动态网络则需要考虑切换/仲裁与阻塞。粒度和网络选择要一起权衡：粗粒度任务通信少，更适合低开销的静态拓扑；细粒度任务同步频繁，在动态网络下要更小心调度与仲裁。

## 复习链

```mermaid
flowchart LR
    A[数据/任务可分性] --> B[依赖图]
    B --> C[Bernstein 检验]
    C --> D[选择粒度]
    D --> E[估计通信/同步开销]
    E --> F[网络与编程模型]
```

图 1：从可分割到网络/编程模型选择的复习链（自制，依据 [CG5201_Chap2 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap2%20%282627%29.pdf) pp.22–33；核对于 2026-09-07）。

## 易错点

直径是拓扑属性，交通信/同步是运行开销；二次通信成本意味着“多处理器”并不必然带来线性加速。粒度选择要在并行度、同步开销与负载均衡之间折中。

## 下一步

- 上一页：[[CEG5201-Week02-Bernstein条件与软件并行性]]
- 下一页：[[CEG5201-Week03-MIN结构与路由]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[CG5201_Chap2 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap2%20%282627%29.pdf)，pp.22–33；[Chap 2_1_TenNodeFine_vs_Coarse_Grain_Scheduling.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_1_TenNodeFine_vs_Coarse_Grain_Scheduling.pdf)（扫描版，标 Open）；个人参考 `notebook/lecture2.md`。
- 2026-09-01：拆出粒度、通信和网络指标短页。
- 2026-09-07：扩写粒度分层、二次通信成本、δ-regular 成本与 packing density，补扫瞄版例题 Open 说明并更新图注。
