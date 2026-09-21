# CEG5302 测验真题考点与讲义知识点映射 (Quiz Topic Mapping)

> [!NOTE]
> 本页面建立了往年测验真题（`quiz1.docx`，共 11 题，20 分）与课程讲义知识体系之间的双向索引。帮助学生在刷题过程中实现“以题带点、溯源精读”。

---

## 考点映射总览矩阵 (Topic Mapping Matrix)

| 题号 | 分值 | 核心考点 (Key Concept) | 考察层级 | 所属讲义模块 | 深度阅读直达链接 |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **Q1** | 1 pt | 变异与重组算子对编码表示的依赖性；选择算子的表示无关性 | 理解 / 辨析 | Lecture 3 (编码与变异) | [[CEG5302-Lecture03-Binary-and-Integer-Representation]] |
| **Q2** | 1 pt | 动态适应度景观下 $(\mu, \lambda)$ 与 $(\mu+\lambda)$ 存活策略权衡 | 分析 / 评价 | Lecture 4 (种群管理) | [[CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure]] |
| **Q3** | 1 pt | 锦标赛规模 $k$ 对选择压力与多样性丧失速度的影响 | 理解 / 记忆 | Lecture 4 (选择机制) | [[CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure]] |
| **Q4** | 3 pts | 进化算法终止条件的必要性，计算预算与收敛停滞判据 | 分析 / 应用 | Lecture 2b (算法框架) | [[CEG5302-Lecture02-EA-Seven-Components]] |
| **Q5** | 4 pts | 编码解码、极小化二元锦标赛、单点交叉、代际替代全手算 | 综合应用 | Lecture 2b / Lecture 4 | [[CEG5302-Lecture02-Canonical-GA-Worked-Example]]<br>[[CEG5302-Lecture04-RWS-Tournament-and-Selection-Schemes]] |
| **Q6** | 1 pt | 标准遗传算法 (SGA) 规范结构、实数/排列需求、重复采样与无重组算法 | 理解 / 辨析 | Lecture 2b / Lecture 3 | [[CEG5302-Lecture02-Canonical-GA-Worked-Example]]<br>[[CEG5302-Lecture03-Binary-and-Integer-Representation]] |
| **Q7** | 1 pt | 交叉重组算子的统计无偏性原理与进化的定向驱动力分离 | 理论深度 | Lecture 3 (算子理论) | [[CEG5302-Lecture03-Real-Valued-Recombination]] |
| **Q8** | 2 pts | 多样性保持、适应度共享 (Fitness Sharing)、拥挤机制与孤岛模型 | 综合辨析 | Lecture 4 (多样性) | [[CEG5302-Lecture04-Diversity-Maintenance-and-Niching]] |
| **Q9** | 3 pts | 随机余数轮盘赌选择 (Stochastic Remainder RWS) 期望计算与余数投针 | 计算应用 | Lecture 4 (选择算子) | [[CEG5302-Lecture04-Population-Models-FPS-and-Ranking]] |
| **Q10** | 1 pt | 精英保留策略 (Elitism) 的单调收敛优势与早熟收敛风险 | 评价 / 权衡 | Lecture 4 (存活选择) | [[CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure]] |
| **Q11** | 2 pts | 锦标赛选择对比比例选择在负值适应度、多目标排序及并行化中的优势 | 对比分析 | Lecture 4 (选择算子) | [[CEG5302-Lecture04-RWS-Tournament-and-Selection-Schemes]] |

---

## 模块知识点反向索引 (By Lecture Topic)

### Lecture 2b: 进化计算基本组件 (EA Components)
- **终止判据 (Termination Criteria)**：对应真题 **Q4**。
  - 为什么必须有终止判据？因为 EA 是随机启发式算法，缺乏全局最优性的内在确定性判决。
  - 常见终止条件：最大代数、最大评估次数、目标适应度达标、多样性崩溃停滞。
- **EA 总体执行循环 (General EA Loop)**：对应真题 **Q5**、**Q6**。
  - 表现型与基因型的解码映射、父代选择、交叉、变异、子代评估与代际更迭。

### Lecture 3: 编码表示与变异重组 (Representation & Variation)
- **算子与编码的绑定关系**：对应真题 **Q1**。
  - 基因型空间算子：位翻转、高斯/多项式、PMX/OX 必须紧密结合底层编码。
- **重组算子的统计无偏性**：对应真题 **Q7**。
  - 算子不改变种群均值，将方向性搜索职责完全剥离给选择压力。
- **标准遗传算法 (SGA) 规范**：对应真题 **Q6**。
  - Holland/Goldberg 规范下的二进制编码定义与适用局限。

### Lecture 4: 选择机制与种群管理 (Selection & Population Management)
- **比例选择与随机余数选择 (Stochastic Remainder RWS)**：对应真题 **Q9**。
  - 计算期望复制数 $e_i = N \frac{F_i}{\sum F}$，整数部分保底，余数部分构建小轮盘赌映射。
- **锦标赛选择机制 (Tournament Selection)**：对应真题 **Q3**、**Q5**、**Q11**。
  - 规模 $k$ 控制选择压力；对负值、单调变换与多目标非支配排序天然免疫。
- **代际更迭与精英保留 (Generational Replacement & Elitism)**：对应真题 **Q2**、**Q5**、**Q10**。
  - $(\mu, \lambda)$ vs $(\mu+\lambda)$：自适应景观下逗号策略更灵活，加号策略易被历史最优解锁死。
  - 精英策略的双刃剑效应。
- **小生境技术与种群多样性保持 (Niching & Diversity)**：对应真题 **Q8**。
  - 适应度共享（按小生境计数惩罚密集个体）；
  - 拥挤机制（相似替换保持基底）；
  - 孤岛模型与细胞模型拓扑演化特性。
