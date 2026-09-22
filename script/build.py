#!/usr/bin/env python3
"""把 page/ 下的 Wiki Markdown 拍平为 MkDocs 预览文档。"""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "page"
DOCS = ROOT / "build" / "preview" / "docs"
MERMAID_VENDOR = ROOT / "script" / "vendor" / "mermaid-11.17.2.min.js"
SKIP = {"_Sidebar.md", "_Footer.md", "_META.md"}

EXTRA_CSS = """
:root {
  --course-accent: #4051b5;
  --course-soft: color-mix(in srgb, var(--course-accent) 10%, transparent);
}

.md-grid { max-width: 82rem; }
.md-content__inner { padding-bottom: 3rem; }
.md-typeset h1 { font-weight: 750; letter-spacing: -0.025em; }
.md-typeset h2 { margin-top: 2.1em; font-weight: 700; }

.md-typeset blockquote:first-of-type {
  margin: .6rem 0 1.4rem;
  padding: .65rem .9rem;
  border-left: .2rem solid var(--course-accent);
  border-radius: 0 .35rem .35rem 0;
  background: var(--course-soft);
  color: var(--md-default-fg-color--light);
}
.md-typeset table:not([class]) { border-radius: .45rem; overflow: hidden; }
.md-typeset table:not([class]) th { background: var(--course-soft); }

.mermaid {
  margin: 1.25rem auto;
  padding: 1rem;
  overflow: auto;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: .65rem;
  background: var(--md-default-bg-color);
  text-align: center;
}
.mermaid svg { max-width: 100%; height: auto; }
"""

MERMAID_JS = """
mermaid.initialize({
  startOnLoad: false,
  securityLevel: "strict",
  theme: "neutral",
  flowchart: { htmlLabels: true, curve: "basis" }
});

async function renderMermaid() {
  document.querySelectorAll("pre.mermaid").forEach((block) => {
    const container = document.createElement("div");
    container.className = "mermaid";
    container.textContent = block.textContent;
    block.replaceWith(container);
  });
  const diagrams = document.querySelectorAll(
    ".mermaid:not([data-processed='true']):not([data-rendering='true'])"
  );
  if (diagrams.length) {
    diagrams.forEach((diagram) => diagram.dataset.rendering = "true");
    try {
      await mermaid.run({ nodes: diagrams });
    } catch (error) {
      diagrams.forEach((diagram) => delete diagram.dataset.rendering);
      console.error("Mermaid rendering failed:", error?.message ?? error);
    }
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", renderMermaid, { once: true });
} else {
  renderMermaid();
}

if (typeof document$ !== "undefined") {
  document$.subscribe(renderMermaid);
}
"""

MATHJAX_JS = """
window.MathJax = {
  tex: {
    inlineMath: [["\\\\(", "\\\\)"]],
    displayMath: [["\\\\[", "\\\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  if (typeof MathJax !== "undefined") {
    if (MathJax.startup && MathJax.startup.output) {
      MathJax.startup.output.clearCache();
    }
    if (MathJax.typesetClear) {
      MathJax.typesetClear();
    }
    if (MathJax.texReset) {
      MathJax.texReset();
    }
    if (MathJax.typesetPromise) {
      MathJax.typesetPromise();
    }
  }
});
"""


RENAME_MAP = {
    # Overview
    "CEG5302-课程总览": "CEG5302-Course-Overview",
    "CEG5302-课件与讲义": "CEG5302-Course-Materials",
    "CEG5302-课程要求与截止日期": "CEG5302-Course-Requirements",
    "CEG5302-课程资源总览": "CEG5302-Course-Resources",
    "CEG5302-讲义与笔记索引": "CEG5302-Lecture-Index",
    "CEG5302-当前进度与待补内容": "CEG5302-Course-Progress",
    # Lecture 01
    "CEG5302-Lecture01-进化计算导论": "CEG5302-Lecture01-Introduction-to-EC",
    "CEG5302-Lecture01-自然进化隐喻与基本循环": "CEG5302-Lecture01-Evolution-Metaphor-and-Basic-Cycle",
    "CEG5302-Lecture01-四类问题与工程应用": "CEG5302-Lecture01-Problem-Types-and-Applications",
    # Lecture 02
    "CEG5302-Lecture02-问题类型与单目标优化": "CEG5302-Lecture02-Problem-Types-and-Single-Objective",
    "CEG5302-Lecture02-计算复杂度与进化计算动机": "CEG5302-Lecture02-Computational-Complexity-and-EC-Motivation",
    "CEG5302-Lecture02-EA七大组件": "CEG5302-Lecture02-EA-Seven-Components",
    "CEG5302-Lecture02-CanonicalGA与手算示例": "CEG5302-Lecture02-Canonical-GA-Worked-Example",
    # Lecture 03
    "CEG5302-Lecture03-表示的概念与选择准则": "CEG5302-Lecture03-Representation-Concepts-and-Criteria",
    "CEG5302-Lecture03-Binary与Integer表示": "CEG5302-Lecture03-Binary-and-Integer-Representation",
    "CEG5302-Lecture03-Real表示的变异": "CEG5302-Lecture03-Real-Valued-Mutation",
    "CEG5302-Lecture03-Real表示的重组": "CEG5302-Lecture03-Real-Valued-Recombination",
    "CEG5302-Lecture03-Permutation表示": "CEG5302-Lecture03-Permutation-Representation",
    "CEG5302-Lecture03-Tree表示与Crossover一般结论": "CEG5302-Lecture03-Tree-Representation-and-Crossover-Conclusions",
    # Lecture 04
    "CEG5302-Lecture04-种群管理模型与FPS及Ranking": "CEG5302-Lecture04-Population-Models-FPS-and-Ranking",
    "CEG5302-Lecture04-RWS与Tournament等选择": "CEG5302-Lecture04-RWS-Tournament-and-Selection-Schemes",
    "CEG5302-Lecture04-SurvivorSelection与选择压力": "CEG5302-Lecture04-Survivor-Selection-and-Selection-Pressure",
    "CEG5302-Lecture04-多样性维持与Niching": "CEG5302-Lecture04-Diversity-Maintenance-and-Niching",
    "CEG5302-Lecture04-Island与CellularEA及MATLAB": "CEG5302-Lecture04-Island-Cellular-EA-and-MATLAB",
    # Lecture 05
    "CEG5302-Lecture05-约束处理概览与分类": "CEG5302-Lecture05-Constraint-Handling-Overview",
    "CEG5302-Lecture05-罚函数原理": "CEG5302-Lecture05-Penalty-Functions-Principles",
    "CEG5302-Lecture05-罚函数类型与要点": "CEG5302-Lecture05-Penalty-Function-Types-and-Key-Points",
    # CEG5201 Week01 Backward Compatibility Mappings
    "CEG5201-Week01-为什么需要现代并行平台": "CEG5201-Week01-01-现代计算需求与硬件演进",
    "CEG5201-Week01-嵌入式系统与计算平台选择": "CEG5201-Week01-02-嵌入式系统与计算平台选择",
    "CEG5201-Week01-并发并行与Flynn体系分类": "CEG5201-Week01-03-现代计算系统与Flynn分类",
    "CEG5201-Week01-性能度量与计算吞吐率": "CEG5201-Week01-04-性能度量与计算吞吐率",
    "CEG5201-Week01-多处理器体系结构与系统设计流": "CEG5201-Week01-07-NUMA架构与多处理器设计流",
    "CEG5201-Week01-算法复杂度与P-NP理论": "CEG5201-Week01-08-Vector-SIMD与算法复杂度理论",
    "CEG5201-Week01-PRAM理论模型与变体比较": "CEG5201-Week01-09-PRAM理论模型与变体比较",
    "CEG5201-Week01-并行算法例题-矩阵乘法": "CEG5201-Week01-10-并行算法例题-矩阵乘法与Prefix-Sum",
    "CEG5201-Week01-并行算法例题-Prefix-Sum与归约": "CEG5201-Week01-10-并行算法例题-矩阵乘法与Prefix-Sum",
    "CEG5201-Week01-Amdahl定律与可扩展性分析": "CEG5201-Week01-11-Amdahl定律与可扩展性",
    "CEG5201-Week01-集群计算Cloud与虚拟化": "CEG5201-Week01-13-Annex-集群计算Cloud与虚拟化",
}


def target_name(name: str) -> str:
    name = RENAME_MAP.get(name, name)
    return "index.md" if name == "Home" else f"{name}.md"


def normalize_math(text: str) -> str:
    lines = text.split("\n")
    new_lines = []
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            in_code = not in_code
            new_lines.append(line)
            i += 1
            continue
        if in_code:
            new_lines.append(line)
            i += 1
            continue

        single_dollar = re.match(r"^(\s*)\$\$(.+?)\$\$\s*$", line)
        if single_dollar:
            indent = single_dollar.group(1)
            math_content = single_dollar.group(2).strip()
            if indent or (new_lines and new_lines[-1].strip().startswith(("-", "*", "1.", "2.", "3.", "4.", "5."))):
                new_lines.append(f"{indent}${math_content}$")
                i += 1
                continue
            else:
                if new_lines and new_lines[-1].strip() != "":
                    new_lines.append("")
                new_lines.append("$$")
                new_lines.append(math_content)
                new_lines.append("$$")
                if i + 1 < len(lines) and lines[i+1].strip() != "":
                    new_lines.append("")
                i += 1
                continue

        if line.strip() == "$$":
            if new_lines and new_lines[-1].strip() != "":
                if new_lines[-1].strip().startswith("- "):
                    bullet_text = new_lines[-1].strip()[2:]
                    colon = "：" if "：" in bullet_text else ":"
                    b_clean = bullet_text.rstrip("：:")
                    new_lines[-1] = f"**{b_clean}**{colon}"
                new_lines.append("")
            new_lines.append("$$")
            i += 1
            while i < len(lines):
                cur = lines[i]
                if cur.strip() == "$$":
                    new_lines.append("$$")
                    if i + 1 < len(lines) and lines[i+1].strip() != "":
                        new_lines.append("")
                    i += 1
                    break
                else:
                    if cur.strip() != "":
                        new_lines.append(cur)
                    i += 1
            continue

        new_lines.append(line)
        i += 1

    return "\n".join(new_lines)


def convert(text: str) -> str:
    text = normalize_math(text)
    text = re.sub(r'\((?:\.\./)+assets/', '(assets/', text)
    def repl(m):
        raw = m.group(1).strip()
        if "|" in raw:
            target, label = raw.split("|", 1)
            target = target.strip()
            label = label.strip()
        else:
            target = raw
            label = raw
        resolved = RENAME_MAP.get(target, target)
        return f"[{label}]({target_name(resolved)})"
    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)


def main() -> None:
    shutil.rmtree(DOCS, ignore_errors=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    seen = {}
    for src in sorted(SRC.rglob("*.md")):
        if src.name in SKIP:
            continue
        if src.name in seen:
            raise SystemExit(f"duplicate page basename: {src} and {seen[src.name]}")
        seen[src.name] = src
        dst = DOCS / ("index.md" if src.name == "Home.md" else src.name)
        dst.write_text(convert(src.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"built {dst.name}")
    assets_src = SRC / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, DOCS / "assets", dirs_exist_ok=True)
        print("built assets/")
    css = DOCS / "stylesheets" / "extra.css"
    css.parent.mkdir(parents=True, exist_ok=True)
    css.write_text(EXTRA_CSS, encoding="utf-8")
    print("built stylesheets/extra.css")
    js = DOCS / "javascripts" / "mermaid.js"
    js.parent.mkdir(parents=True, exist_ok=True)
    js.write_text(MERMAID_JS, encoding="utf-8")
    print("built javascripts/mermaid.js")
    math_js = DOCS / "javascripts" / "mathjax.js"
    math_js.parent.mkdir(parents=True, exist_ok=True)
    math_js.write_text(MATHJAX_JS, encoding="utf-8")
    print("built javascripts/mathjax.js")
    vendor_js = DOCS / "javascripts" / "vendor" / MERMAID_VENDOR.name
    vendor_js.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MERMAID_VENDOR, vendor_js)
    print(f"built javascripts/vendor/{MERMAID_VENDOR.name}")


if __name__ == "__main__":
    main()
