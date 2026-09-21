# Blocking 与 CLOS

> 本页属于：CEG5201 / Week 03
> 前置知识：[[CEG5201-Week03-MIN结构与路由]]
> 预计阅读时间：9 分钟

## Blocking 是什么

当输入端和输出端都空闲，但中间链路或交换单元已被已有连接占用，新的连接仍然无法建立，这就是 **blocking**（[Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf) 第 3 页）。问题不在端点，而在共享的中间资源。单路径 Banyan/Omega/Baseline/二元 n-cube 网络按定义属于阻塞类；Benes 属于可重排非阻塞；CLOS 目标是非阻塞（第 3 页）。

## 三种性质

| 性质 | 含义 |
|---|---|
| Blocking | 某些输入-输出排列会因中间资源冲突而无法建立 |
| Strictly non-blocking | 无论已有连接如何，只要输入/输出空闲，总能立即找到路径 |
| Rearrangeably non-blocking | 可能需要重排已有连接后才能建立新连接（成本低、有重配置开销） |

## CLOS 直观

CLOS 网络通常由输入级、中间级、输出级三级组成：输入模块把请求分发到多个中间模块，输出模块再把来自中间模块的数据汇聚到目的端（第 6 页）。多个中间模块提供多条可选路径，降低阻塞概率，但会增加交换单元、布线与控制复杂度。

![CLOS 三级网络：任意输入可到任意输出](assets/CEG5201/fig-004-clos-network.png)

图 1：CLOS 三级网络（输入级 $r_1 \times r_2$、中间级 $m$、输出级 $m \times n_2$，任意输入有路径到任意输出）；来源：[Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf) 第 6 页；核对 2026-09-07。

## 为什么需要中间级

两级结构（输入级直接连到输出模块）会把“到某输出模块的链路”当成唯一通道：该链路一旦被已有连接占用，即使两端都空闲，新连接也无法建立；继续扩大规模会让中间链路成为瓶颈、复杂度快速上升。引入**中间级**后，每个输入模块可经多个中间模块到达同一输出模块，从而在成本与阻塞之间折中（第 6–7 页）。

CLOS 的参数一般记作：输入级每个模块为 $r_1 \times r_2$ 交换，最后一级为 $m \times n_2$ 交换，中间级有 $m$ 个模块；$n_1$、$n_2$ 是输入/输出模块的端口数，$m$ 是中间级模块数。增加 $m$ 或每个模块的可用链路会提升路径多样性，但代价是交换单元、布线与控制复杂度上升。

## 非阻塞条件与 Fat-tree

讲义给出（第 7 页）：CLOS 网络**非阻塞**取决于中间级交换单元数 $m$，判据为：

$$
m \ge n_1 + n_2 - 1
$$

其中 $n_1$、$n_2$ 是输入/输出模块的端口数（讲义也写作中间级元素数需足够多）。这就是 CLOS 之所以被选用的原因：高可扩展性（连接数千个 PE/加速器）、高带宽、低时延（多路径降低拥塞）、成本效益（比全 crossbar 用更少交换机）。

**Fat-tree** 是 CLOS 的一种实际/优化实现：把越靠近上层的链路“加粗”以提供更大聚合带宽，从而避免瓶颈。讲义总结：CLOS 是基础网络架构，Fat-tree 是其面向高带宽通信的优化形态，因而成为现代 AI 集群与数据中心的主流选择（第 7 页）。

## 待确认范围

> [!QUESTION] Q-CEG5201-L3-01（Open）
> **Context:** `Chap 2_3_CLOSNonBlkingProof.pdf` 为扫描版，无文本层；讲义第 35 页也说明 MIN 部分是教师自编材料。
> **Question:** 课堂采用的 CLOS 阻塞证明步骤与 switch-state convention 是什么？$m \ge n_1 + n_2 - 1$ 的证明是否按讲义定义展开？
> **Status:** Open — 需回看正式课堂 Canvas slides 后再把证明写为定理。

## 下一步

- 上一页：[[CEG5201-Week03-MIN结构与路由]]
- 下一页：[[CEG5201-Week03-RC粒度比与性能模型]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Chap 2_2_MINs.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_2_MINs.pdf) 第 3、6–7 页；[Chap 2_3_CLOSNonBlkingProof.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/Chap%202_3_CLOSNonBlkingProof.pdf)（扫描版，无文本层，标 Open）；个人参考 `notebook/lecture3.md`。
- 2026-09-01：拆出 blocking、non-blocking 和 CLOS 设计直觉。
- 2026-09-07：扩写三种性质、CLOS 判据 $m \ge n_1+n_2-1$ 与 Fat-tree 关系，新增 CLOS 原图（第 6 页）并补 Open 问题。
