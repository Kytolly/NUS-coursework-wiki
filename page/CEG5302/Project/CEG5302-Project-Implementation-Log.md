# CEG5302 项目代码实现与迭代日志 (Project Implementation Log)

> [!IMPORTANT]
> **当前工程状态**：🟡 **框架搭建完成，正式代码实现待小组启动 (Framework Ready / Not Started)**  
> **状态声明**：本页面为项目从零开发过程中的架构设计与版本变更日志，真实记录小组代码演进轨迹。目前题目已建立模块化接口定义，实际编码将随课程实验周期推进更新。

---

## 1. 算法架构与类层次设计 (Class Architecture Design)

项目遵循高内聚、低耦合的面向对象设计原则，将算法逻辑与问题定义彻底解耦：

```
project_workspace/
├── optimizer/
│   ├── base.py              # 优化器抽象基类
│   ├── nsga2.py             # NSGA-II 算法主类 (含 SBX、PM、拥挤排序)
│   └── operators.py         # 约束支配、交叉、变异、多项式核函数
├── problems/
│   ├── base.py              # 问题基类 (n_var, n_obj, bounds, evaluate)
│   ├── part1_zdt3.py        # ZDT3 双目标无约束测试用例
│   ├── part1_vcw.py         # VCW 三目标无约束测试用例
│   ├── part2_mw7.py         # MW7 约束多目标测试用例
│   └── part2_rcm.py         # RCM 工程约束多目标测试用例
├── metrics/
│   ├── igd.py               # 反转世代距离 (Inverted Generational Distance)
│   ├── hypervolume.py       # 超体积指标 (Hypervolume)
│   └── spacing.py           # 解集空间分布均匀度 (Spacing Metric)
└── CEG5302_Group_Project_<xy>.ipynb  # 最终集成实验 Notebook
```

---

## 2. 模块研发进度看板 (Development Kanban)

| 核心组件 | 拟定责任接口 | 核心算法依赖 | 计划完成时间 | 当前状态 |
| :--- | :--- | :--- | :---: | :---: |
| **种群初始化与边界映射** | `NSGA2.initialize()` | 均匀连续空间采样 | Week 7 | ⚪ 待开始 (Planned) |
| **快速非支配排序** | `NSGA2.fast_non_dominated_sort()` | 支配集 $S_p$、计数 $n_p$ | Week 7 | ⚪ 待开始 (Planned) |
| **拥挤距离分配** | `NSGA2.calculate_crowding_distance()` | 目标轴边界极值赋 $\infty$ | Week 8 | ⚪ 待开始 (Planned) |
| **模拟二进制交叉 (SBX)** | `NSGA2.simulated_binary_crossover()` | 分布指数 $\eta_c = 20$ | Week 8 | ⚪ 待开始 (Planned) |
| **多项式变异 (PM)** | `NSGA2.polynomial_mutation()` | 分布指数 $\eta_m = 20$ | Week 8 | ⚪ 待开始 (Planned) |
| **Deb 约束支配扩展** | `NSGA2.constrained_sort()` | 违规值 $CV$ 分级比较 | Week 9 | ⚪ 待开始 (Planned) |
| **ZDT3 动态绘图与验证** | `ZDT3.evaluate()` + `matplotlib` | 5段不连通前沿对照 | Week 9 | ⚪ 待开始 (Planned) |
| **VCW 三维空间前沿投影** | `VCW.evaluate()` + `3D scatter` | 3目标曲面连续性 | Week 10 | ⚪ 待开始 (Planned) |
| **MW7 约束穿透性检验** | `MW7.evaluate()` | 非线性边界可行率 | Week 11 | ⚪ 待开始 (Planned) |
| **RCM 机构优化仿真** | `RCM.evaluate()` | 实际工程可行解集合 | Week 11 | ⚪ 待开始 (Planned) |
| **Notebook 完整性与打包** | `Restart and Run All` | 零静态图片、全动态执行 | Week 12 | ⚪ 待开始 (Planned) |

---

## 3. 版本迭代记录 (Version History)

### v0.1.0 (2026-09-11) - 架构初始化
- 梳理并对齐官方 `project overview.pdf` 指南；
- 确立 `NSGA2` 与四类基准测试问题的输入输出协议；
- 完成无约束与有约束非支配排序算法伪代码设计。
