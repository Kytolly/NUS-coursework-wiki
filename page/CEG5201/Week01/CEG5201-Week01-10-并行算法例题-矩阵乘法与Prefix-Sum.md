# 并行算法例题：矩阵乘法与Prefix-Sum

> 本页对应课件：CG5201_Chap1 (2627).pdf, pp. 71–72；Chap1 BigOExamples.pdf, pp. 1–4
> 本页属于：CEG5201 / Week 01
> 上一页：[[CEG5201-Week01-09-PRAM理论模型与变体比较]]
> 下一页：[[CEG5201-Week01-11-Amdahl定律与可扩展性]]
> 预计阅读时间：14 分钟

---

## 1. 为什么需要研究具体并行算法例题？

前两节系统建立了计算复杂性（Big-O、P/NP）与抽象共享存储计算模型（PRAM 四大变体）。现在，我们必须将理论工具应用于经典的实际计算问题：
1. 经典算法（如矩阵乘法与前缀和）在不同处理器数量下如何切分任务？
2. 算法的时间复杂度、加速比与总成本（Cost）如何严密推导？
3. 如何判断一个并行算法是否达到了理论性能下界与工作最优性？

讲义第 71–72 页与配套手写讲义 [Chap1 BigOExamples.pdf](assets/CEG5201/chap1/fig_bigo_page_1.png) 第 1–4 页给出了完整的推导范式。

---

## 2. 算子一：矩阵乘法（Matrix Multiplication）

设给定两个维度均为 $n 	imes n$ 的实数方阵 $A$ 和 $B$，计算乘积方阵 $C = A 	imes B$：

$$
C_{ij} = \sum_{k=1}^n A_{ik} \cdot B_{kj} \quad (1 \le i, j \le n)
$$

### 2.1 单核串行基准（手写讲义第 1 页）

![手写讲义第 1 页：矩阵乘法串行与一维行切分](assets/CEG5201/chap1/fig_bigo_page_1.png)
*图：手写讲义第 1 页（来源：Chap1 BigOExamples.pdf 第 1 页）*

```text
i = 1 to n           (循环 n 次)
    j = 1 to n       (循环 n 次)
        k = 1 to n   (循环 n 次)
            Cij + Aik * Bkj => Cij
```

- 三重嵌套循环总共执行 $n 	imes n 	imes n = n^3$ 次乘加操作；
- 单处理器串行基准时间复杂度为：

$$
T_1(n) = O(n^3)
$$

---

### 2.2 并行方案 1：分配 $n$ 个处理器的一维行切分（Using $n$ Processors）

手写讲义第 1 页下半部分与第 2 页上半部分推导了行切分方案：

![手写讲义第 2 页：行切分与二维点切分推导](assets/CEG5201/chap1/fig_bigo_page_2.png)
*图：手写讲义第 2 页（来源：Chap1 BigOExamples.pdf 第 2 页）*

- **任务映射**：系统配备 $n$ 个处理器 $P_1, P_2, \dots, P_n$。第 $i$ 个处理器 $P_i$ 独占负责计算输出矩阵 $C$ 的整个第 $i$ 行：

$$
P_i \implies 	ext{Compute Row } i = \{C_{i1}, C_{i2}, \dots, C_{in}\}
$$

- **计算量与时间**：
  - 计算整行共 $n$ 个元素，每个元素需要 $n$ 次点积累加操作；
  - 单个处理器的运算量为 $n 	imes n = n^2$ 次；
  - 所有 $n$ 个处理器完全并发独立执行，总并行时间为：

$$
T_n(n) = O(n^2)
$$

- **指标评价**：
  - 加速比：$S_n = rac{T_1}{T_n} = rac{O(n^3)}{O(n^2)} = O(n)$（达到线性加速）；
  - 算法成本：$	ext{Cost} = p 	imes T_p = n 	imes O(n^2) = O(n^3)$。由于与最优串行时间同阶，该算法是**工作最优的（Work-Optimal）**；
  - **PRAM 模型需求（Slide 71）**：所有处理器在计算同一列时需并发读取矩阵 $B$ 的数据，因此要求底层支持并发读，属于 **CREW PRAM**。

---

### 2.3 并行方案 2：分配 $n^2$ 个处理器的二维点切分（Using $n^2$ Processors）
- **任务映射**：配备 $n^2$ 个处理器，逻辑上排布为二维阵列 $P_{ij}$（$1 \le i, j \le n$）。每个处理器仅负责计算单一标量元素 $C_{ij}$：

$$
P_{ij} \implies 	ext{Compute } C_{ij} = \sum_{k=1}^n A_{ik} \cdot B_{kj}
$$

- **时间与成本**：
  - 单个处理器仅需执行长为 $n$ 的向量内积（$n$ 次乘加操作）；
  - 并行执行时间缩短为：

$$
T_{n^2}(n) = O(n)
$$

  - 算法成本：$	ext{Cost} = n^2 	imes O(n) = O(n^3)$，依然保持**工作最优**；同样需要 **CREW PRAM**。

---

### 2.4 并行方案 3：分配 $n^3$ 个处理器与二叉树加法归约
若动用 $p = n^3$ 个处理器：
1. 第一步：$n^3$ 次标量乘法在 $O(1)$ 常数时间一步完成；
2. 第二步：利用 $n$ 个处理器对每个 $(i, j)$ 位置的 $n$ 个乘积项构建深度为 $\lceil \log_2 n ceil$ 的二叉加法归约树，耗时 $O(\log n)$；
3. **时间与成本**：
   - 并行时间：$T_{n^3}(n) = O(\log n)$；
   - 算法成本：$	ext{Cost} = n^3 	imes O(\log n) = O(n^3 \log n) > O(n^3)$。
   - **结论**：虽然达成了对数级时间，但由于存在处理器空闲等待，**该方案不再具备工作最优性**。

---

### 2.5 物理拓扑映射：2D Mesh 网格脉动阵列（Slide 72 B）
讲义第 72 页练习题 B 与手写讲义第 2 页底部抛出了一个针对真实物理架构的经典思考题：
> **讲义练习 B（Slide 72）**：
> *Consider a matrix multiplication problem ($2$ matrices of size $n 	imes n$ each) on a mesh topology. Demonstrate an algorithm that can perform in $O(n)$ time, where $n^2$ is the number of processors arranged in a mesh configuration. DIY!*
> （手写讲义提问：*Mesh Architecture: $n 	imes n$ processors, Claim: $O(n)$. Describe the algorithm. What is the PRAM model?*）

- **算法机理（Cannon 脉动网格算法）**：
  在真实的二维 $n 	imes n$ 网格中，各个处理单元仅与上下左右的邻近节点有物理连线（无集中式全局共享内存）。通过行循环左移与列循环上移，数据在网格中脉动流动，每个 PE 步进执行局部乘累加。
- **复杂度与模型对应**：
  - 算法共经历 $n$ 次邻居通信与计算步进，每次常数时间，**总运行时间为严格的 $O(n)$**；
  - **PRAM 模型对应**：由于每个数据项仅在点对点私有通道上流动，不存在并发读写冲突，通信语义等价于最严格的 **EREW**。

---

## 3. 算子二：前缀和计算（Prefix-Sum / Scan）

前缀和是并行算法领域的基石原语（手写讲义第 3–4 页；讲义第 72 页）：

![手写讲义第 3 页：前缀和定义与串行复杂度](assets/CEG5201/chap1/fig_bigo_page_3.png)
*图：手写讲义第 3 页（来源：Chap1 BigOExamples.pdf 第 3 页）*

### 3.1 问题形式化定义
- 输入序列：$X = \{x_0, x_1, \dots, x_{n-1}\}$；
- 目标：计算前缀和序列 $S = \{S_0, S_1, \dots, S_{n-1}\}$，满足：

$$
S_i = \sum_{k=0}^i x_k = x_0 + x_1 + \dots + x_i \quad (0 \le i \le n-1)
$$

- 单核串行基准：$S_0 = x_0, S_i = S_{i-1} + x_i$，耗时为：

$$
T_1(n) = O(n)
$$

---

### 3.2 PRAM 并行前缀和算法（Hillis-Steele 扫描）

手写讲义第 4 页给出了基于 $n$ 个处理器的并行前缀扫描算法：

![手写讲义第 4 页：PRAM 前缀和算法与网格图](assets/CEG5201/chap1/fig_bigo_page_4.png)
*图：手写讲义第 4 页（来源：Chap1 BigOExamples.pdf 第 4 页）*

#### 算法伪代码（手写讲义第 4 页）
```text
for j = 0 to log2(n) - 1 do
    for i = 2^j to n - 1 doPar
        S_i = S_{i - 2^j} + S_i
    endfor
endfor
```

#### 复杂度与理论下界分析（Slide 72 C）
1. **并行时间**：外层循环执行 $\log_2 n$ 轮，每轮内部并发执行加法，总时间为：

$$
T_p(n) = O(\log n)
$$

2. **Non-CRCW 理论时间下界（Slide 72 C）**：
   > **讲义重点结论（Slide 72 C）**：
   > 该算法在所有 **非 CRCW（NON-CRCW）并行机器** 中具备最优时间复杂度（Optimal time complexity among all NON-CRCW machines）。
   > **原因**：因为计算最终项 $S_{n-1} = \sum_{k=0}^{n-1} x_k$ 涉及 $n$ 个数的累加，在任何 Non-CRCW 并行机器上，其计算时间均具有 $\Omega(\log n)$ 的坚硬理论下界！
3. **算法成本度量（Slide 72 C）**：
   - 讲义明确定义算法成本公式为：

$$
	ext{Cost} = 	ext{Running Time} 	imes 	ext{\# of Processors}
$$

   - 代入本算法参数：$	ext{Cost} = O(\log n) 	imes n = O(n \log n)$。由于 $O(n \log n) > O(n)$，该算法不是工作最优的（Not cost-optimal）。

---

## 4. 经典算法并行化特征综合对比表

| 算子名称 | 方案策略 | 处理器数 $p$ | 并行时间 $T_p$ | 加速比 $S$ | 算法成本 $	ext{Cost}$ | 是否工作最优? | 体系/模型约束 |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **矩阵乘法** | 单处理器串行基准 | $1$ | $O(n^3)$ | $1$ | $O(n^3)$ | 是 | RAM |
| **矩阵乘法** | 一维行切分 | $n$ | $O(n^2)$ | $O(n)$ | $O(n^3)$ | **是** | CREW PRAM |
| **矩阵乘法** | 二维点切分 | $n^2$ | $O(n)$ | $O(n^2)$ | $O(n^3)$ | **是** | CREW PRAM |
| **矩阵乘法** | 三维二叉树归约 | $n^3$ | $O(\log n)$ | $O(n^3 / \log n)$ | $O(n^3 \log n)$ | **否** | CREW / CRCW |
| **矩阵乘法** | 2D Mesh 网格脉动 | $n^2$ | $O(n)$ | $O(n^2)$ | $O(n^3)$ | **是** | EREW 语义 |
| **前缀和** | 单处理器串行基准 | $1$ | $O(n)$ | $1$ | $O(n)$ | 是 | RAM |
| **前缀和** | Hillis-Steele 扫描 | $n$ | $O(\log n)$ | $O(n / \log n)$ | $O(n \log n)$ | **否** | CREW (Non-CRCW 理论最优时间) |

---

## 学习目标 / Problem-Solving Skills

完成本节学习后，你应能掌握讲义中的以下核心知识与分析技能：

1. **矩阵乘法多尺度推导**：
   - 熟练写出串行基准 $O(n^3)$ 的三层循环推导；
   - 证明 $p = n$ 行切分时间为 $O(n^2)$，$p = n^2$ 点切分时间为 $O(n)$，并能运用公式 $	ext{Cost} = p 	imes T_p$ 验证其工作最优性；
   - 掌握 $p = n^3$ 方案利用二叉树在 $O(\log n)$ 时间完成的机制，并解释其为何破坏了工作最优性。
2. **2D Mesh 脉动网格分析（Slide 72 B）**：
   - 说明 2D Mesh 网格如何通过点对点邻接移位在 $O(n)$ 时间内完成矩阵乘法，并指出其属于 EREW 模型。
3. **PRAM 前缀和算法掌握（Slide 72 C）**：
   - 默写手写讲义第 4 页的 Hillis-Steele 双层循环伪代码；
   - 掌握并行时间 $O(\log n)$ 与成本 $O(n \log n)$；
   - 准确阐述 Slide 72 C 的结论：为什么该算法在所有 Non-CRCW 机器上达到了理论下界 $\Omega(\log n)$。

---

## 下一步

- 上一页：[[CEG5201-Week01-09-PRAM理论模型与变体比较]]
- 下一页：[[CEG5201-Week01-11-Amdahl定律与可扩展性]]
- 模块总览：[[CEG5201-讲义与笔记索引]]
- 返回知识库：[[Home]]

---

## 来源与更新日志

- 来源：[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) pp. 71–72; [Chap1 BigOExamples.pdf](assets/CEG5201/chap1/fig_bigo_page_1.png) pp. 1–4.
- 2026-09-23：按照讲义顺序重构，建立正规编号与讲义映射页眉，系统整合矩阵乘法与前缀和算子的严密数学推导、手写讲义原件图与 Slide 72 理论下界/成本判定。
