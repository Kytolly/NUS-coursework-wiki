# CEG5302 小组大作业总览 (Group Project: Multi-Objective Optimization)

> [!NOTE]
> **课程模块**：CEG5302 / EE5904  
> **作业名称**：Multi-Objective Optimization with NSGA-II  
> **考核权重**：**25%** (总评占比 1/4)  
> **核心任务**：实现非支配排序遗传算法 II (NSGA-II) 并求解无约束与有约束经典多目标基准问题  
> **官方证据源**：`materials/CEG5302 -  project overview.pdf`

---

## 1. 项目全景与结构 (Project Structure)

大作业要求学生基于 Python 从零构建或完善 NSGA-II 算法内核，并分别在两类多目标测试集上展开算法验证、实验调优与对比分析：

```mermaid
graph TD
    A[CEG5302 Group Project<br>NSGA-II 算法实现与测试] --> B[Part-I: 无约束多目标优化 (Unconstrained MOO)]
    A --> C[Part-II: 有约束多目标优化 (Constrained MOO)]

    B --> B1[ZDT3 测试函数<br>具有不连通 Pareto 前沿]
    B --> B2[VCW 测试函数<br>多目标连续非凸前沿]

    C --> C1[MW7 测试函数<br>具有复杂约束边界]
    C --> C2[RCM 测试函数<br>工程约束多目标问题]

    A --> D[最终交付件 (Deliverables)]
    D --> D1[report_<xy>.pdf<br>2-3 页深度学术报告]
    D --> D2[CEG5302_Group_Project_<xy>.ipynb<br>全动态可复现 Jupyter Notebook]
    D --> D3[15-20 min Group Demo<br>现场/在线答辩汇报]
```

---

## 2. 关键时间节点 (Important Milestones)

根据官方项目指南（`CEG5302 -  project overview.pdf` Slide 6），项目里程碑时间如下：

| 里程碑事项 (Milestone) | 官方截止时间 (Deadline) | 教学周 (Week) | 说明 (Notes) |
| :--- | :--- | :---: | :--- |
| **组队确认截止 (Group Formation)** | **Sun, Sept 06, 2026 — 11:00 p.m. SGT** | Week 4 | 自由分组并在 Canvas 登记 |
| **大作业题目正式发布 (Project Release)** | **Thu, Sept 17, 2026 — 11:00 p.m. SGT** | Week 6 | 发布完整参数与指导文档 |
| **项目报告与代码提交 (Final Submission)** | **Mon, Nov 09, 2026 — 11:00 p.m. SGT** | Week 13 | 题目发布后 53 天完整冲刺周期 |
| **小组答辩展示 (Demo Presentation)** | **Sat, 07 Nov & Thu, 12 Nov, 2026** | Week 13-14 | 每组 15-20 分钟，共 21 个展示槽位 |

---

## 3. 提交规范与交付清单 (Submission Requirements)

### 3.1 打包与命名格式
- 最终提交必须为一个单一的 ZIP 压缩包，严格命名为：
  $$\mathbf{EC\_Group\_<xy>.zip}$$
  其中 `<xy>` 为系统分配的小组编号（例如：`EC_Group_22.zip`）。
- ZIP 包内仅包含且必须包含以下两个文件，**严禁嵌套任何额外的子文件夹或辅助临时文件**：
  1. `report_<xy>.pdf`（例如：`report_22.pdf`）
  2. `CEG5302_Group_Project_<xy>.ipynb`（例如：`CEG5302_Group_Project_22.ipynb`）

### 3.2 代码文件规范 (`.ipynb`)
- 必须使用 **Jupyter Notebook (`.ipynb`)** 格式，**绝对不接受纯 `.py` 脚本文件**。
- Notebook 必须保持“一键自顶向下运行（Fully runnable from start to finish）”。
- 提交前必须保证所有单元格已执行完成并保留输出；**严禁插入静态图片伪造结果**，所有 Pareto 前沿对比图与收敛曲线必须由代码动态生成。

### 3.3 报告规范 (`.pdf`)
- 篇幅限制：**严格 2-3 页**（不包括引用）。
- 排版格式：**单栏排版 (Single column)**，字体 **Times New Roman**，字号 **12 pt**。
- 内容侧重：对 NSGA-II 在 ZDT3、VCW、MW7、RCM 上的收敛性与分布均匀性进行机制层面的原因分析与见解阐述。

---

## 4. 模块导航与工作区快速直达 (Project Subspaces)

- [项目规范与提交检查单 (Requirements & Checklist)](CEG5302-Project-Requirements.md)
- [Part-I 无约束多目标问题理论与实现 (Part-I: ZDT3 & VCW)](CEG5302-Project-Part-I.md)
- [Part-II 约束多目标处理机制与实战 (Part-II: MW7 & RCM)](CEG5302-Project-Part-II.md)
- [算法实现与代码迭代日志 (Implementation Log)](CEG5302-Project-Implementation-Log.md)
- [实验数据与对比记录日志 (Experiment Log)](CEG5302-Project-Experiment-Log.md)
- [提交前综合检查清单 (Submission Checklist)](CEG5302-Project-Submission-Checklist.md)
