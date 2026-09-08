# 网络规划流程与链路预算

> 本页属于：CEG5104 / Week 01
> 前置知识：[[CEG5104-Week01-蜂窝网络概述与演进]]
> 预计阅读时间：6 分钟

**蜂窝网络规划**分三大块：**无线网络规划**（最关键，直面用户）、**传输网络规划**、**核心网络规划**。无线网规划的对象是基站（BTS）与移动台（MS）及其之间的无线接口，目标是用尽量低的成本提供足够的**覆盖（coverage）**与**容量（capacity）**，同时保证质量；设计准则随地区而变，取决于主导因素是**容量还是覆盖**，并须与传输/核心网规划紧密协同。（来源：1_network_planning.pdf 第 32–34 页。）

**规划流程**（五步）：① Start：收集容量、覆盖、质量等输入参数；② Pre-planning：用输入做出理论上的覆盖与容量方案；③ Site selection：结合传输与安装工程师挑选候选站址；④ Frequency allocation：给每小区分配频率信道，使干扰最小并维持质量；⑤ Final radio plan：输出覆盖图、容量估计、干扰图、功率预算、参数集与频率表。

![无线网络规划流程](assets/CEG5104/fig-002-radio-planning-process.png)

图 1：无线网络规划流程——网络需求 → 预规划（覆盖/容量）→ 站址勘测与选择 → C/I 分析与频率规划 → 参数规划 → 无线网计划（来源：1_network_planning.pdf 第 34 页；核对 2026-09-07）。

**配置容量（dimensioning）输入**：要覆盖的地理区域、每区估算话务、每区最小功率要求与拥塞标准、路径损耗、所用频段与频率复用方式。dimensioning 的目标是确定满足覆盖与质量要求所需的设备与网络类型。（来源：1_network_planning.pdf 第 36 页。）

详细无线网计划又分成三个子计划：**链路预算计算**、**覆盖/容量规划与频谱效率**、**参数规划**。（来源：1_network_planning.pdf 第 37 页。）

**链路预算（link budget）**：它决定**小区半径**和覆盖门限，要分别对**上行**和**下行**做，并且**上行功率预算更关键**。需考虑：上行看基站接收灵敏度，下行看发射功率与天线增益、合路器损耗（combiner loss），双向都要算电缆损耗。主要成分：MS/BTS 灵敏度（如 MS −102/−100 dBm、BTS −106 dBm）、衰落裕度（fade margin，dense urban 约 2 dB、urban 约 1 dB）、电缆损耗（按 dB/100 m）+ 接插件损耗（约 0.1 dB）、MS 天线增益约 0 dBi、BTS 天线增益 8–21 dBi。要注意“dBm + dBi − dB = dBm”这类单位换算，以及灵敏度常取“接收机噪声系数 + 最小 SNR”（来源：1_network_planning.pdf 第 38–39 页。）

| 成分 | 典型取值 | 说明 |
| --- | --- | --- |
| MS/BTS 灵敏度 | −102/−100 dBm、−106 dBm | 由噪声系数与最小 SNR 决定 |
| 衰落裕度 | dense urban 2 dB、urban 1 dB | 接收信号与接收门限之差 |
| 电缆损耗 | 按 dB/100 m 查表 | 沿馈线衰减 |
| 接插件损耗 | 约 0.1 dB | 远小于电缆损耗 |
| MS 天线增益 | 约 0 dBi | 手机天线增益低 |
| BTS 天线增益 | 8–21 dBi | 基站天线增益高 |

**Worked Example 1 功率预算**：取 MS 发射功率 32 dBm、天线 0 dBi、电缆 0 dB；BTS 发射功率 42 dBm、天线 18 dBi、电缆 2 dB、合路器 2 dB、BTS 灵敏度 −108 dBm、MS 灵敏度 −106 dBm。（来源：1_network_planning.pdf 第 40 页。）

上行允许路径损耗：
```text
EIRPm = Ptm − (Lcm + Lom) + Gm = 32 − (0+0) + 0 = 32 dBm
Prb   = −Gb + (Lcb + Lob) + Bs = −18 + (2+0) + (−108) = −124 dBm
PLu   = EIRPm − Prb = 32 − (−124) = 156 dB
```

下行：
```text
EIRPb = Ptb + Gtb − (Lcb + Lccb) = 42 + 18 − (2+2) = 56 dBm
Prm   = Ms + (Lcm + Lom) − Gm = −106 + (0+0) − 0 = −106 dBm
PLd   = EIRPb − Prm = 56 − (−106) = 162 dB
```

**含义**：上行 156 dB < 下行 162 dB，说明**上行是瓶颈**：手机功率小、天线增益低，基站能覆盖的范围比手机能“打回去”的范围更大，因此下行覆盖更好。想缩小差距可以降低下行功率，但会损失覆盖；更推荐在 BTS 引入**分集（diversity）**或**低噪声放大器（LNA）**来提升上行接收能力。（来源：1_network_planning.pdf 第 41–43 页。）

## 下一步

- 上一页：[[CEG5104-Week01-蜂窝网络概述与演进]]
- 下一页：[[CEG5104-Week01-覆盖与传播模型]]
- 返回：[[Home]]

## 来源与更新日志

- 来源：[1_network_planning.pdf](https://github.com/Kytolly/NUS-coursework-wiki/releases/download/CEG5104/1_network_planning.pdf)，slide 32–37（规划流程/输入/子计划）、38–43（链路预算与 Worked Example 1）。
- 2026-09-07：从 Week 1 课件拆出该主题短页。
- 2026-09-07：补全内容并新增图解与原图（规划流程原图 fig-002、链路预算成分表）。
