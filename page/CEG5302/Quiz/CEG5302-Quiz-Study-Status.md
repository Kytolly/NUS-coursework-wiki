# CEG5302 测验复习与考点自测状态表 (Study Status Matrix)

> [!NOTE]
> 本表用于追踪 CEG5302 进化计算部分核心考点的复习进度、公式熟练度、手算题演练情况以及常见陷阱规避清单。

---

## 考点自测与熟练度矩阵 (Knowledge Readiness Matrix)

| 知识模块 | 关键考点 / 技能目标 | 考查形式 | 核心公式 / 判据 | 易错陷阱 (Pitfalls) | 掌握状态 |
| :--- | :--- | :---: | :--- | :--- | :---: |
| **基础框架** | 算法终止判据 (Termination) | 简答题 | $G \ge G_{max}$ 或 $\Delta f < \epsilon$ | 误以为 EA 可以像凸优化一样通过梯度为 0 自动检测理论最优 | 🟢 完备 |
| **基础框架** | SGA 规范定义 (SGA Structure) | 选择题 | Holland 规范：$\{0, 1\}^L$ 位串 | 混淆 SGA 的二进制位串与通用 EA 的整型/实数编码 | 🟢 完备 |
| **表示与算子** | 算子对表示的依赖性 | 多选题 | 变异/交叉 $\in$ 基因型空间 | 误将独立于编码的选择算子（适应度空间）选入 | 🟢 完备 |
| **表示与算子** | 交叉算子均值无偏性 | 简答题 | $E[\bar{x}_{child}] = \bar{x}_{parent}$ | 忽视算子正交化原则，企图在交叉中人为引入方向偏置 | 🟢 完备 |
| **选择机制** | 锦标赛选择压力控制 | 填空题 | 规模 $k \uparrow \implies$ 压力 $\uparrow$ | 记反 $k$ 与选择压力的正相关关系 | 🟢 完备 |
| **选择机制** | 锦标赛全流程手算 | 计算题 | 极小化比较 $f(x_A) < f(x_B)$ | 极小化问题误选了数值大的个体；位串切点位置数错 | 🟢 完备 |
| **选择机制** | 随机余数轮盘赌手算 | 计算题 | $e_i = N \frac{F_i}{\sum F}$, $r_i = e_i - \lfloor e_i \rfloor$ | 忘记第一阶段的整数确定性分配；余数未归一化区间映射 | 🟢 完备 |
| **选择机制** | 锦标赛对比轮盘赌场景 | 简答题 | 负值适应度、Pareto 多目标、并行化 | 答成抽象的“速度快”，未指出轮盘赌对非正值或非标量失效 | 🟢 完备 |
| **存活与替代** | 自适应景观下的存活选择 | 简答题 | $(\mu, \lambda)$ 淘汰旧父代 | 忽略景观动态变化特性，盲目认为保底的加号策略处处最优 | 🟢 完备 |
| **存活与替代** | 精英保留策略权衡 (Elitism) | 简答题 | 单调收敛 vs 早熟收敛 | 只写出优点，未指出降低多样性、导致局部最优锁死的弊端 | 🟢 完备 |
| **小生境技术** | 适应度共享与拥挤机制 | 多选题 | $f'_i = \frac{f_i}{\sum \operatorname{sh}(d_{ij})}$，同类替换 | 误以为小生境是为了收敛到单一最优；误以为拥挤替换差异父代 | 🟢 完备 |

---

## 核心计算公式备忘速查 (Exam Formula Cheat Sheet)

### 1. 期望复制数与随机余数选择 (Stochastic Remainder Sampling)
- **个体相对选择概率**：
  $$p_i = \frac{F_i}{\sum_{k=1}^N F_k}$$
- **期望复制数 (Expected Value)**：
  $$e_i = N \cdot p_i = N \cdot \frac{F_i}{\sum_{k=1}^N F_k}$$
- **确定性保留份额**：
  $$n_i^{(det)} = \lfloor e_i \rfloor$$
- **余数轮盘赌概率**：
  $$r_i = e_i - \lfloor e_i \rfloor, \quad p'_i = \frac{r_i}{\sum_{k=1}^N r_k}$$

### 2. 适应度共享 (Fitness Sharing)
- **共享适应度计算**：
  $$f'_i = \frac{f_i}{m_i}, \quad m_i = \sum_{j=1}^N \operatorname{sh}(d(i, j))$$
- **经典共享函数**：
  $$\operatorname{sh}(d) = \begin{cases} 1 - \left(\frac{d}{\sigma_{share}}\right)^\alpha & \text{if } d < \sigma_{share} \\ 0 & \text{otherwise} \end{cases}$$

### 3. 二进制无符号整数解码 (Binary String Decoding)
- 对于 $L$ 位二进制串 $b_1 b_2 \cdots b_L$（$b_1$ 为最高有效位 MSB，$b_L$ 为最低有效位 LSB），在实数区间 $[X_{min}, X_{max}]$ 上的映射值为：
  $$x = X_{min} + \frac{\sum_{j=1}^L b_j \cdot 2^{L-j}}{2^L - 1} \cdot (X_{max} - X_{min})$$
