# CEG5302 项目 Part-I：无约束多目标优化 (Unconstrained MOO)

> [!NOTE]
> **模块目标**：实现经典 NSGA-II 算法内核，并在两个无约束经典多目标基准测试函数（**ZDT3** 与 **VCW**）上完成求解、前沿拟合与收敛性能分析。

---

## 1. 理论基础：NSGA-II 算法核心组件

非支配排序遗传算法 II (Non-dominated Sorting Genetic Algorithm II, NSGA-II, Deb et al., 2002) 是多目标进化计算领域里程碑式的经典算法。其核心机制包括三大支柱：

### 1.1 快速非支配排序 (Fast Non-dominated Sorting)
对于种群中大小为 $2N$ 的父子混合集合 $R_t = P_t \cup Q_t$：
1. 计算每个个体 $p$ 的支配个体集合 $S_p$ 和被支配计数 $n_p$；
2. 找出所有 $n_p = 0$ 的个体组成第一非支配前沿 $\mathcal{F}_1$；
3. 依次递减被当前前沿支配的个体的 $n_q$，形成后续分层 $\mathcal{F}_2, \mathcal{F}_3, \dots$。
- 时间复杂度由初代 NSGA 的 $O(M N^3)$ 降至 $O(M N^2)$（$M$ 为目标维度，$N$ 为种群规模）。

### 1.2 拥挤距离估计 (Crowding Distance Assignment)
为了在同一非支配层内维持解的广泛分布性，无需用户指定小生境半径 $\sigma_{share}$：
- 对于每个目标 $m \in \{1, \dots, M\}$，按目标值升序对前沿 $\mathcal{F}$ 中的个体排序；
- 边界极值点赋予无限距离：$d_{(1)} = d_{(|\mathcal{F}|)} = \infty$；
- 中间个体的距离为相邻解在归一化目标轴上的跨度累加：
  $$d_i = \sum_{m=1}^M \frac{f_m^{(i+1)} - f_m^{(i-1)}}{f_m^{\max} - f_m^{\min}}$$

### 1.3 拥挤比较算子 (Crowded Comparison Operator $\prec_n$)
个体 $i$ 优于个体 $j$（记作 $i \prec_n j$），当且仅当满足以下条件之一：
1. **非支配等级更优**：$rank_i < rank_j$；
2. **等级相同但分布更稀疏（拥挤距离更大）**：$rank_i = rank_j$ 且 $distance_i > distance_j$。

---

## 2. 基准优化问题数学模型 (Benchmark Problems)

### 2.1 ZDT3 (Zitzler-Deb-Thiele Benchmark 3)
ZDT3 是检验多目标算法处理**不连通非凸 Pareto 前沿 (Disconnected Pareto Front)** 能力的标准测试用例。

- **决策变量维度**：$n = 30$
- **变量边界**：$x_i \in [0, 1], \quad \forall i = 1, 2, \dots, 30$
- **目标函数定义**（双目标极小化）：
  $$\begin{aligned}
  f_1(x) &= x_1 \\
  g(x) &= 1 + \frac{9}{n-1} \sum_{i=2}^n x_i \\
  h(f_1, g) &= 1 - \sqrt{\frac{f_1}{g}} - \left(\frac{f_1}{g}\right) \sin(10 \pi f_1) \\
  f_2(x) &= g(x) \cdot h(f_1, g)
  \end{aligned}$$
- **前沿特征**：由于正弦振荡项 $\sin(10 \pi f_1)$ 的存在，其真实的 Pareto 最优前沿由 5 个相互独立、互不相连的凸弧段构成（$g(x) = 1$ 时达到全局最优）。算法极易遗漏部分孤立岛弧段。

---

### 2.2 VCW (Viennet-Chankong-Wong Benchmark)
VCW 是一个具有 3 个互相冲突目标的复杂多目标连续优化测试用例，决策空间为二维。

- **决策变量维度**：$n = 2$
- **变量边界**：$x_1, x_2 \in [-4, 4]$
- **目标函数定义**（三目标极小化）：
  $$\begin{aligned}
  f_1(x) &= 0.5 (x_1^2 + x_2^2) + \sin(x_1^2 + x_2^2) \\
  f_2(x) &= \frac{(3 x_1 - 2 x_2 + 4)^2}{8} + \frac{(x_1 - x_2 + 1)^2}{27} + 15 \\
  f_3(x) &= \frac{1}{x_1^2 + x_2^2 + 1} - 1.1 \exp\left(-(x_1^2 + x_2^2)\right)
  \end{aligned}$$
- **前沿特征**：三维目标空间内呈现一条复杂的弯曲空间曲线/曲面，能够严格检验算法在多目标（$M > 2$）下的高维逼近与分布均匀性。

---

## 3. 官方代码骨架与实现模板 (Code Template)

官方讲义（`CEG5302 -  project overview.pdf` Slide 3-4）给出了如下规范模板：

```python
import numpy as np
import matplotlib.pyplot as plt

class NSGA2:
    """NSGA-II 优化器实现 (Part-I: 无约束版本)"""
    def __init__(self, pop_size=100, pc=0.9, pm=None, eta_c=20, eta_m=20):
        self.pop_size = pop_size
        self.pc = pc                          # 模拟二进制交叉概率
        self.eta_c = eta_c                    # SBX 分布指数
        self.eta_m = eta_m                    # 多项式变异分布指数
        self.pm = pm                          # 变异概率 (默认 1 / n_var)

    def initialize(self, prob):
        """种群决策变量随机初始化"""
        x = prob.lower + (prob.upper - prob.lower) * np.random.rand(
            self.pop_size, prob.n_var
        )
        return x

    def fast_non_dominated_sort(self, fx):
        """快速非支配排序：返回按分层索引的列表 fronts = [front_1, front_2, ...]"""
        pop_size = fx.shape[0]
        s = [[] for _ in range(pop_size)]     # 存储被当前个体支配的个体列表
        n = np.zeros(pop_size, dtype=int)     # 存储支配当前个体的总计数
        rank = np.zeros(pop_size, dtype=int)
        fronts = [[]]

        for p in range(pop_size):
            for q in range(pop_size):
                # 判定 p 是否支配 q (极小化问题)
                p_dominates_q = np.all(fx[p] <= fx[q]) and np.any(fx[p] < fx[q])
                q_dominates_p = np.all(fx[q] <= fx[p]) and np.any(fx[q] < fx[p])
                if p_dominates_q:
                    s[p].append(q)
                elif q_dominates_p:
                    n[p] += 1
            if n[p] == 0:
                rank[p] = 0
                fronts[0].append(p)

        i = 0
        while len(fronts[i]) > 0:
            next_front = []
            for p in fronts[i]:
                for q in s[p]:
                    n[q] -= 1
                    if n[q] == 0:
                        rank[q] = i + 1
                        next_front.append(q)
            i += 1
            fronts.append(next_front)
        
        # 移除末尾空集合
        if len(fronts[-1]) == 0:
            fronts.pop()
        return fronts, rank

    def calculate_crowding_distance(self, fx, front):
        """计算特定非支配层内所有个体的拥挤距离"""
        l = len(front)
        if l == 0:
            return np.array([])
        if l <= 2:
            return np.full(l, np.inf)

        distance = np.zeros(l)
        n_obj = fx.shape[1]

        for m in range(n_obj):
            # 按第 m 个目标值升序排序
            obj_vals = fx[front, m]
            sorted_idx = np.argsort(obj_vals)
            distance[sorted_idx[0]] = np.inf
            distance[sorted_idx[-1]] = np.inf

            val_range = obj_vals[sorted_idx[-1]] - obj_vals[sorted_idx[0]]
            if val_range == 0:
                continue

            for i in range(1, l - 1):
                distance[sorted_idx[i]] += (
                    obj_vals[sorted_idx[i + 1]] - obj_vals[sorted_idx[i - 1]]
                ) / val_range
        return distance

    def simulated_binary_crossover(self, p1, p2, prob):
        """模拟二进制交叉 (Simulated Binary Crossover, SBX)"""
        c1, c2 = p1.copy(), p2.copy()
        if np.random.rand() <= self.pc:
            for i in range(prob.n_var):
                if np.random.rand() <= 0.5:
                    if abs(p1[i] - p2[i]) > 1e-14:
                        y1 = min(p1[i], p2[i])
                        y2 = max(p1[i], p2[i])
                        lb, ub = prob.lower[i], prob.upper[i]
                        
                        beta = 1.0 + (2.0 * (y1 - lb) / (y2 - y1))
                        alpha = 2.0 - np.power(beta, -(self.eta_c + 1.0))
                        rand = np.random.rand()
                        if rand <= 1.0 / alpha:
                            beta_q = np.power(rand * alpha, 1.0 / (self.eta_c + 1.0))
                        else:
                            beta_q = np.power(1.0 / (2.0 - rand * alpha), 1.0 / (self.eta_c + 1.0))
                        
                        c1_val = 0.5 * ((y1 + y2) - beta_q * (y2 - y1))
                        
                        beta = 1.0 + (2.0 * (ub - y2) / (y2 - y1))
                        alpha = 2.0 - np.power(beta, -(self.eta_c + 1.0))
                        if rand <= 1.0 / alpha:
                            beta_q = np.power(rand * alpha, 1.0 / (self.eta_c + 1.0))
                        else:
                            beta_q = np.power(1.0 / (2.0 - rand * alpha), 1.0 / (self.eta_c + 1.0))
                        c2_val = 0.5 * ((y1 + y2) + beta_q * (y2 - y1))
                        
                        c1[i] = np.clip(c1_val, lb, ub)
                        c2[i] = np.clip(c2_val, lb, ub)
        return c1, c2

    def polynomial_mutation(self, ind, prob):
        """多项式变异 (Polynomial Mutation, PM)"""
        pm = self.pm if self.pm is not None else 1.0 / prob.n_var
        mutated = ind.copy()
        for i in range(prob.n_var):
            if np.random.rand() <= pm:
                y = mutated[i]
                lb, ub = prob.lower[i], prob.upper[i]
                delta1 = (y - lb) / (ub - lb)
                delta2 = (ub - y) / (ub - lb)
                rand = np.random.rand()
                mut_pow = 1.0 / (self.eta_m + 1.0)
                if rand <= 0.5:
                    xy = 1.0 - delta1
                    val = 2.0 * rand + (1.0 - 2.0 * rand) * np.power(xy, self.eta_m + 1.0)
                    delta_q = np.power(val, mut_pow) - 1.0
                else:
                    xy = 1.0 - delta2
                    val = 2.0 * (1.0 - rand) + 2.0 * (rand - 0.5) * np.power(xy, self.eta_m + 1.0)
                    delta_q = 1.0 - np.power(val, mut_pow)
                mutated[i] = np.clip(y + delta_q * (ub - lb), lb, ub)
        return mutated
```

---

## 4. ZDT3 问题类规范 (Problem Implementation)

```python
class ZDT3:
    """ZDT3 经典测试问题"""
    def __init__(self):
        self.name = 'ZDT3'
        self.n_obj = 2                      # 双目标
        self.n_var = 30                     # 30 维决策变量
        self.lower = np.zeros(self.n_var)  # 下界 [0, 0, ..., 0]
        self.upper = np.ones(self.n_var)   # 上界 [1, 1, ..., 1]

    def evaluate(self, x):
        pop_size = len(x)
        f = np.zeros((pop_size, self.n_obj))
        f[:, 0] = x[:, 0]
        g = 1.0 + 9.0 * np.sum(x[:, 1:], axis=1) / (self.n_var - 1)
        h = 1.0 - np.power(f[:, 0] / g, 0.5) - (f[:, 0] / g) * np.sin(10.0 * np.pi * f[:, 0])
        f[:, 1] = g * h
        return f
```
