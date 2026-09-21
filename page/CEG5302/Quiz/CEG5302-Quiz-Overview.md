# CEG5302 测验与考试总览 (Quiz & Assessment Overview)

> [!NOTE]
> **模块代码**：CEG5302 / EE5904  
> **模块名称**：Neural Networks & Evolutionary Computation (神经网络与进化计算 - 进化计算部分)  
> **主讲教师**：Prof. Dipti Srinivasan  
> **归档状态**：已建立正式归档 / 证据链锚定 (Evidence-grounded)

---

## 1. 考核结构全景 (Assessment Breakdown)

根据课程讲义第一讲（`Lecture 1 - Introduction` Slide 6）及官方大纲，CEG5302 的学期考核权重分布如下：

| 考核组成部分 (Component) | 形式 (Format) | 权重 (Weight) | 状态 / 证据源 (Status & Source) |
| :--- | :--- | :---: | :--- |
| **Individual Tests** | 3 次独立闭卷/限时测试 | **65%** | 正式期中/期末考核，覆盖基础理论与算法推导 |
| **Individual Coding Assignment** | 编程大作业 (Python) | **10%** | 讲义已列入考核大纲，具体题目待发布 (Pending Release) |
| **Group Project** | 多目标优化算法设计 (NSGA-II) | **25%** | 已发布完整 Project Overview 文档，分组与基准已锁定 |
| **Weekly Class Quizzes** | 课堂随堂小测 (Canvas) | **0% (平时练习)** | 每周自测，帮助巩固课堂核心概念 (不计入最终总评) |

---

## 2. 测验归档库 (Quiz Archives)

Wiki 为 CEG5302 设立了专门的测验复习与真题归档工作区：

1. **往年测验原题与推导题解 (Past Quiz Archive)**：
   - 入口页面：[CEG5302-Quiz-Past-Paper.md](CEG5302-Quiz-Past-Paper.md)
   - 证据来源：`CEG5302/materials/Repository of ungraded quizzes/quiz1.docx`
   - 题量与分值：共 11 道题目，满分 20 分。
   - 包含选择题、简答题、以及包含完整手算步骤的数值计算题（二进制锦标赛选择与交叉、随机余数轮盘赌选择）。
   - **重要声明**：所有题解均为课程助教/学者视角重构与推导（`Solution status: derived / reconstructed`），非官方标准答案。

2. **考点与知识点映射 (Topic Mapping)**：
   - 入口页面：[CEG5302-Quiz-Topic-Mapping.md](CEG5302-Quiz-Topic-Mapping.md)
   - 将真题中的每一道小题严格映射到 Lecture 2b、Lecture 3、Lecture 4 的具体章节与公式中，提供反向链接。

3. **知识掌握状态矩阵 (Study Status Matrix)**：
   - 入口页面：[CEG5302-Quiz-Study-Status.md](CEG5302-Quiz-Study-Status.md)
   - 追踪各个考点的复习进度、公式熟练度与常见易错陷阱。

---

## 3. 核心考点分布雷达 (Core Examination Areas)

根据真题与课堂练习，CEG5302 进化计算测试重点围绕以下四大核心维度展开：

```mermaid
graph TD
    A[CEG5302 测验核心模块] --> B[编码与变异算子 (Representation & Variation)]
    A --> C[选择机制与选择压力 (Selection Mechanisms & Pressure)]
    A --> D[种群多样性与小生境 (Diversity & Niching)]
    A --> E[算法框架与终止条件 (EA Components & Termination)]

    B --> B1[二进制/实数/排列编码]
    B --> B2[算子对表示的依赖性 Q1]
    B --> B3[交叉算子均值无偏性 Q7]

    C --> C1[轮盘赌与随机余数选择计算 Q9]
    C --> C2[锦标赛选择计算与规模效应 Q3, Q5]
    C --> C3[锦标赛相比轮盘赌的适用场景 Q11]

    D --> D1[适应度共享机制 Fitness Sharing Q8]
    D --> D2[拥挤机制 Crowding Q8]
    D --> D3[孤岛模型与细胞模型 Q8]
    D --> D4[精英保留策略优缺点 Q10]

    E --> E1[终止判据必要性与常用指标 Q4]
    E --> E2[动态自适应景观下的存活策略 Q2]
    E --> E3[标准遗传算法 SGA 规范特征 Q6]
```

---

## 4. 复习建议与自测指引 (Revision Guide)

> [!TIP]
> 1. **计算题务必写出规范步骤**：测验中的计算题（如 Q5 的位串二元锦标赛、单点交叉以及代际替代；Q9 的期望副本数、整数向下取整分配、余数轮盘赌归一化区间映射）占总分约 35%（7/20 分）。请务必亲手推导一遍，切忌只看答案。
> 2. **深入理解算子设计哲学**：简答题（如 Q2 自适应景观下 $(\mu, \lambda)$ 为什么优于 $(\mu+\lambda)$、Q7 交叉为什么不应改变种群均值、Q10 精英保留的双刃剑效应）考察的是对演化动态平衡的深层理解。
> 3. **关联课堂讲义深度阅读**：遇到概念盲区时，点击 [CEG5302-Quiz-Topic-Mapping.md](CEG5302-Quiz-Topic-Mapping.md) 快速跳转到讲义对应页面查阅图文解释与原始课件截图。
