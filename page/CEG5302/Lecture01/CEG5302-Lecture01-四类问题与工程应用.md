# 四类问题与工程应用

> 本页属于：CEG5302 / Lecture 01
>
> 前置知识：[[CEG5302-Lecture01-自然进化隐喻与基本循环]]
>
> 预计阅读时间：6 分钟

## 四类问题

### Scheduling

Scheduling 具有巨大的组合搜索空间、可行性约束和多个竞争性质量指标。大学课表、航空器路径/维护/机组安排都是例子。大量候选 schedule 可能不可行，因此 representation 和 constraint handling 会直接影响搜索。（Lecture 1, slides 48–50）

### Optimization 与 design

给定模型与目标性能，optimization 搜索能产生目标结果的 decision variables。课件例子包括卫星结构、天线几何、高速列车气动设计、可再生能源与储能、交通信号和电动车充电。（Lecture 1, slides 51–58）

### Modeling

给定输入-输出观测，modeling 搜索能预测输出的函数、规则集或程序。信用评估、股票交易规则和 RoboCup 决策策略都可以这样表达；此时被进化的 individual 是模型，fitness 衡量预测或决策表现。（Lecture 1, slides 59–62）

### Simulation 与生成式系统

给定 model 与 inputs，simulation 计算不同情景下的 outputs，常用于动态环境中的 “what-if” 问题。进化计算也可生成控制器、虚拟生物、图像、音乐和结构设计，fitness 可由目标函数或人的偏好提供。（Lecture 1, slides 63–66）

## 工程应用的共同结构

```text
candidate representation
    + objective / fitness
    + feasibility constraints
    + variation and selection
    -> 一组多样且高质量的候选方案
```

课件列举了课表安排、项目分配、交通控制与事故检测、家庭能源调度、可再生能源与储能、EV 充电、市场投标和多目标工程设计。（Lecture 1, slides 37–45）

对于成本、可靠性、性能、环境影响等互相冲突的目标，合理结果常常是一组 **Pareto trade-off solutions**，而不是一个对所有决策者都最好的解。这与第 2 讲的 multi-objective optimization 呼应（见 [[CEG5302-Lecture02-问题类型与单目标优化]] 的姊妹概念，详见 Lecture 2b）。

## 下一步

- 上一页：[[CEG5302-Lecture01-自然进化隐喻与基本循环]]
- 下一页：[[CEG5302-Lecture02-问题类型与单目标优化]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[Lecture 1 - Introduction (D Srinivasan) 13Aug26.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5302/Lecture%201%20-%20Introduction%20%28D%20Srinivasan%29%2013Aug26.pdf)（扫描版），slides 37–66；slide 引用以个人笔记 `notes/lecture/lecture-01-introduction-zh.md` 记录为准。
- 2026-09-03：从 Lecture 1 拆出“四类问题与工程应用”短页。
