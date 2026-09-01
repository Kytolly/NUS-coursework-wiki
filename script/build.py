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


def target_name(name: str) -> str:
    return "index.md" if name == "Home" else f"{name}.md"


def convert(text: str) -> str:
    return re.sub(r"\[\[([^\]]+)\]\]", lambda m: f"[{m.group(1).strip()}]({target_name(m.group(1).strip())})", text)


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
    css = DOCS / "stylesheets" / "extra.css"
    css.parent.mkdir(parents=True, exist_ok=True)
    css.write_text(EXTRA_CSS, encoding="utf-8")
    print("built stylesheets/extra.css")
    js = DOCS / "javascripts" / "mermaid.js"
    js.parent.mkdir(parents=True, exist_ok=True)
    js.write_text(MERMAID_JS, encoding="utf-8")
    print("built javascripts/mermaid.js")
    vendor_js = DOCS / "javascripts" / "vendor" / MERMAID_VENDOR.name
    vendor_js.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MERMAID_VENDOR, vendor_js)
    print(f"built javascripts/vendor/{MERMAID_VENDOR.name}")


if __name__ == "__main__":
    main()
