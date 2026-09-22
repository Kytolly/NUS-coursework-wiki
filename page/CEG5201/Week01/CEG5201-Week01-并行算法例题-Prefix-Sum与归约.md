# 并行算法例题：Prefix-Sum与归约

> 本页属于：CEG5201 / Week 01
> 前置知识：[[CEG5201-Week01-并行算法例题-矩阵乘法]]
> 预计阅读时间：14 分钟

---

## 1. 前缀和（Prefix-Sum / Scan）问题定义

**前缀和（Prefix-Sum Computation）**是并行算法中极其重要的基础原语（手写讲义 [Chap1 BigOExamples.pdf](assets/CEG5201/chap1/fig_bigo_page_3.png) 第 3–4 页；[CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) 第 72 页）。

![手写讲义第 3 页：前缀和问题形式化定义与串行复杂度](assets/CEG5201/chap1/fig_bigo_page_3.png)
*图：手写讲义第 3 页（来源：Chap1 BigOExamples.pdf 第 3 页）*

### 1.1 形式化数学定义
- 设输入集合为包含 $n$ 个自然数的序列：

$$
X = \{x_0, x_1, \dots, x_{n-1}\}
$$

- 设 $\oplus$ 为集合上的二元结合算子（如加法）；
- **求解目标**：计算前缀和序列 $S = \{S_0, S_1, \dots, S_{n-1}\}$，使得：

$$
S_i = x_0 + x_1 + \dots + x_i, \quad 0 \le i \le n-1
$$

### 1.2 单核串行基准（RAM Model）
在单处理器 RAM 模型上，通过顺序累加计算：
- $S_0 = x_0$
- $S_i = S_{i-1} + x_i \quad (1 \le i \le n-1)$
- 共需 $n-1$ 次加法，耗时为：

$$
T_1(n) = O(n)
$$

---

## 2. PRAM 并行前缀和算法（Hillis-Steele 扫描）

手写讲义第 4 页展示了在 PRAM 模型上利用 $n$ 个处理器实现对数级时间求解的并行算法：

![手写讲义第 4 页：PRAM 并行前缀和算法与网格图](assets/CEG5201/chap1/fig_bigo_page_4.png)
*图：手写讲义第 4 页（来源：Chap1 BigOExamples.pdf 第 4 页）*

### 2.1 硬件与内存环境
- **处理器规模**：给定 $n$ 个处理器，设 $n$ 为 2 的幂（$n$ is a power of 2）；
- **存储单元**：共享内存位置 $m_0, m_1, \dots, m_{n-1}$；
- **初始状态**：$m_i \leftarrow x_i$；
- **终止状态**：算法结束时 $m_i \leftarrow S_i$。

### 2.2 算法伪代码（手写讲义第 4 页）

```text
for j = 0 to log2(n) - 1 do
    for i = 2^j to n - 1 doPar
        S_i = S_{i - 2^j} + S_i
    endfor
endfor
```

### 2.3 复杂度与理论下界分析（Slide 72 C）
1. **时间复杂度（Parallel Time）**：
   - 外层循环迭代 $\log_2 n$ 轮；
   - 内层循环在各处理器上并发执行（耗时 $O(1)$）；
   - **并行时间**：

$$
T_p(n) = O(\log n)
$$

2. **Non-CRCW 理论时间下界（Slide 72 C）**：
   > **讲义重点提示（Slide 72 C）**：
   > 该算法在所有 **非 CRCW（NON-CRCW）并行机器** 中具备最优时间复杂度（Optimal time complexity among all NON-CRCW machines）。
   > **原因**：因为计算最终的前缀项 $S_{n-1} = \sum_{k=0}^{n-1} x_k$ 涉及 $n$ 个数的求和，在任何 Non-CRCW 并行机器上，其计算时间均具有 $\Omega(\log n)$ 的理论下界！
3. **算法成本与工作效率**：
   - 根据讲义定义 $	ext{Cost} = 	ext{Running Time} 	imes 	ext{\# of Processors}$：

$$
	ext{Cost} = O(\log n) 	imes n = O(n \log n)
$$

   - 由于 $O(n \log n) > O(n)$，该算法不是成本最优的（Not cost-optimal），其额外的 $\log n$ 因子来自部分处理器在各步中的空闲与重复计算。

---

## 3. UMA 多处理器求和数值分析例题（Slides 52–55）

讲义第 52–55 页提供了一个严密、完整的共享存储 UMA 多处理器真实求和案例（Example 1.2）：

### 3.1 串行处理与并行分解代码对比（Slide 52）

![Slide 52 代码对比](assets/CEG5201/chap1/fig52_uma_example_code.png)
*图：Example 1.2 串行与并行代码（来源：CG5201_Chap1 (2627).pdf 第 52 页）*

| 序号 | 串行程序（Sequential） | 并行程序（Multiprocessing, $L = N/M$） |
| :--- | :--- | :--- |
| **L1** | `DO 10 I = 1, N` | `DOALL k = 1, M` |
| **L2** | `  A(I) = B(I) + C(I)` | `  DO 10 I = L(k-1) + 1, kL` |
| **L3** | `10 CONTINUE` | `    A(I) = B(I) + C(I)` |
| **L4** | `SUM = 0` | `  10 CONTINUE` |
| **L5** | `DO 20 J = 1, N` | `  SUM(k) = 0` |
| **L6** | `  SUM = SUM + A(J)` | `  DO 20 J = 1, L` |
| **L7** | `20 CONTINUE` | `    SUM(k) = SUM(k) + A(L(k-1) + J)` |
| **L8** | | `  20 CONTINUE` |
| **L9** | | `ENDALL` |

### 3.2 串行基准耗时与机器周期分析（Slide 53）

![Slide 53 周期分析](assets/CEG5201/chap1/fig53_uma_example_analysis.png)
*图：串行与多处理机器周期分析（来源：CG5201_Chap1 (2627).pdf 第 53 页）*

- **机器周期约定**：
  - 核心计算语句（L2 数组相加、L4 赋零、L6 累加）每次执行记为 **1 个机器周期（1 m/c cycle）**；
  - 循环控制与跳转语句（L1, L3, L5, L7）在理论分析中忽略不计。
- **串行处理总耗时**：
  - 第一个循环（I 循环）执行 $N$ 次，耗时 $N$ 周期；
  - 第二个循环（J 循环）执行 $N$ 次，耗时 $N$ 周期；
  - **串行总耗时**：

$$
T_{	ext{seq}} = 2N 	ext{ 周期}
$$

---

### 3.3 多处理器并行处理的两阶段推导（Slides 53–54）

设系统拥有 $M$ 个并行处理器，数据总量为 $N$，$L = N/M$。

#### 阶段一：各处理器独立计算局部部分和（Phase 1: Local Computation）
- `DOALL` 指明所有 $M$ 个分区由 $M$ 个处理器并行执行；
- $I$ 循环：每个处理器执行 $L$ 次，耗时 $L$ 周期；
- $J$ 循环：每个处理器在 $L$ 周期内生成本分区的局部和 $SUM(k)$；
- **阶段一总耗时**：

$$
T_{	ext{phase1}} = 2L 	ext{ 周期} \quad \left(L = rac{N}{M}ight)
$$

此时共生成 $M$ 个局部和（$M$ partial sums），需要将它们合并以获得最终的全局总和。

#### 阶段二：二叉加法树归约（Phase 2: Binary Adder Tree）

讲义第 54 页展示了合并 $M$ 个局部和的二叉归约树结构：

![Slide 54 二叉树归约架构](assets/CEG5201/chap1/fig54_binary_reduction_tree.png)
*图：二叉树归约架构（来源：CG5201_Chap1 (2627).pdf 第 54 页）*

- **硬件延迟模型**：
  - 成对数据通信耗时：**$k$ 个周期（$k$ cycles per pair for communication）**；
  - 标量加法耗时：**$1$ 个周期（1 cycle for addition）**；
  - 归约树的每一层级耗时为：$k + 1$ 周期。
- **树的高度与阶段二耗时**：
  - 归约层级数：$l = \log_2 M$；
  - **阶段二总耗时**：

$$
T_{	ext{phase2}} = (k + 1) \cdot \log_2 M 	ext{ 周期}
$$

---

### 3.4 加速比公式与讲义算例（Slide 55）

#### 总并行执行时间
$$
T_{	ext{par}} = 2L + (k + 1)\log_2 M = 2\left(rac{N}{M}ight) + (k + 1)\log_2 M
$$

#### 加速比闭式表达式（Speedup Formula）
$$
	ext{Speedup} = rac{T_{	ext{seq}}}{T_{	ext{par}}} = rac{2N}{2L + (k + 1)\log_2 M} = rac{2N}{2\left(rac{N}{M}ight) + (k + 1)\log_2 M}
$$

#### 讲义数值算例（Slide 55）
- 设定数据规模 $N = 2^{20}$（约 100 万个数），处理器数 $M = 256 = 2^8$；
- 局部块大小 $L = rac{2^{20}}{2^8} = 2^{12} = 4096$；
- 讲义给出评估结论：
  > *"Let's say, $N = 2^{20}, M = 256$, we have, Speedup ~= 83%"*
  > （注：讲义此处表述中的 83% 对应于并行效率 $E = rac{	ext{Speedup}}{M} pprox 83\%$，反映出在考虑了跨处理器通信 $k$ 与二叉树层级延迟后，系统能保持约 83% 的有效线性加速效率）。

#### 讲义思考题（Slide 55）
> **思考题**：*“若要求达到指定的加速比目标 $S^*$，在给定问题规模 $N$ 与延迟参数 $k$ 的条件下，所需要的最小处理器数量 $M$ 是多少？”*
> 
> **解法推导**：
> 令 $	ext{Speedup} \ge S^*$，代入闭式解：
> 
> $$
> rac{2N}{rac{2N}{M} + (k+1)\log_2 M} \ge S^*
> $$
> 
> 即要求：
> 
> $$
> rac{2N}{M} + (k+1)\log_2 M \le rac{2N}{S^*}
> $$
> 
> 在已知 $N$、$k$ 和 $S^*$ 时，可通过数值代入或单调性二分求出满足不等式的最小正整数 $M$。

---

## 学习目标 / Problem-Solving Skills

完成本节学习后，你应能掌握讲义中的以下核心知识与分析技能：

1. **PRAM 前缀和算法掌握**：
   - 准确写出手写讲义第 4 页中 Hillis-Steele 前缀和的双层循环伪代码；
   - 证明算法的时间复杂度为 $O(\log n)$，总成本为 $O(n \log n)$，并解释为什么它在 Non-CRCW 机器上达到了理论下界 $\Omega(\log n)$。
2. **UMA 归约两阶段模型与周期分析**：
   - 熟练写出 Example 1.2 的串行时间 $T_{	ext{seq}} = 2N$ 周期与阶段一本地部分和耗时 $2L = 2(N/M)$ 周期；
   - 解释二叉归约树阶段：高度为 $\log_2 M$，每层耗费 $(k+1)$ 周期（$k$ 周期通信 + $1$ 周期加法），得出阶段二耗时 $(k+1)\log_2 M$；
   - 准确写出总时间 $T_{	ext{par}} = 2L + (k+1)\log_2 M$ 与加速比公式。
3. **参数代入与逆向求解**：
   - 能够代入 $N = 2^{20}, M = 256$ 进行全流程数值分析；
   - 能够解答 Slide 55 的课堂思考题：根据加速比不等式反解达到目标加速比 $S^*$ 所需的最小核心数 $M$。

---

## 下一步

- 上一页：[[CEG5201-Week01-并行算法例题-矩阵乘法]]
- 下一页：[[CEG5201-Week01-Amdahl定律与可扩展性分析]]
- 模块总览：[[CEG5201-讲义与笔记索引]]
- 返回知识库：[[Home]]

---

## 来源与更新日志

- 来源：[Chap1 BigOExamples.pdf](assets/CEG5201/chap1/fig_bigo_page_3.png) pp. 3–4; [CG5201_Chap1 (2627).pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5201/CG5201_Chap1%20%282627%29.pdf) pp. 52–55, 72.
- 2026-09-08：初始简略版归档。
- 2026-09-23：严格依讲义重构，完整收纳手写稿原件图与 Slide 52–55 原版图片，精确还原 Example 1.2 的机器周期推导、二叉树归约 $(k+1)\log_2 M$ 延迟、Slide 55 算例与最小核心数 $S^*$ 思考题。
