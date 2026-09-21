# NUS Coursework Wiki

记录 NUS Computer Engineering coursework 的课程要求、原始资源、短知识页面、CA/项目过程与最终产出。

## 当前范围

- 进行中课程：CEG5104、CEG5201、CEG5301、CEG5302。
- CEG5104 已整理：Week 01–04 讲义拆分页（含 Week 04 非地面网络 NTN）、课程资源、课程要求。
- CEG5201 已整理：Week 01–04 讲义拆分页、CA1 Consultation、Kai Hwang 课后习题解析、课程资源与要求。
- CEG5301 已整理：Part I Week 01–04 讲义拆分页、课程资源与要求；Week 05–06 与 Part II 待补。
- CEG5302 已整理：Lecture 01–05 讲义拆分页（含手算示例、图示解析与 Exam Checklist）、Quiz 真题题解、NSGA-II 小组项目工作区、课程资源与要求。
- 待补：各课后续周次/讲次课件、未公布的三次测试与编程作业细则。

内容源文件位于 `page/`，构建脚本位于 `script/`，本地预览与站点产物位于被忽略的 `build/`。`page/` 是唯一可编辑的内容源，`build/` 全为生成物，不要手改。

本地预览使用仓库内固定版本的 Mermaid 11.17.2 浏览器构建，避免依赖外部 CDN；第三方许可证位于 `script/vendor/mermaid-LICENSE`。数学公式由 MathJax 渲染。

## 本地预览

先安装固定版本的 MkDocs 工具链到 `build/preview/.venv`，再构建：

```bash
python3 -m venv build/preview/.venv
./build/preview/.venv/bin/pip install -r script/requirements.txt
python3 script/build.py
./build/preview/.venv/bin/mkdocs serve -f script/mkdocs.yml -a 127.0.0.1:8000
```

或在 Bash 环境运行 `./script/serve.sh`（会调用 `build.py` 后 `mkdocs serve`）；Windows PowerShell 可运行 `./script/serve.ps1`。

## 发布

### GitHub Pages（主发布方式）

站点由 GitHub Actions 自动构建并发布到 GitHub Pages：

- 工作流：`.github/workflows/pages.yml`（push 到 `main` 或手动 `workflow_dispatch` 触发）。
- 流程：`script/build.py` 把 `page/` 投射到 `build/preview/docs` → `mkdocs build -f script/mkdocs.yml` 生成 `build/preview/site` → 作为 Pages artifact 部署。
- 站点地址：<https://kytolly.github.io/NUS-coursework-wiki/>。
- 仓库 Settings → Pages 的 Source 需为 **GitHub Actions**（首次执行时工作流会用 `configure-pages` 自动启用）。

发布前请检查不应公开的声明表、个人信息和草稿没有被复制进 `page/`。

### GitHub Wiki（可选备用）

`script/publish-wiki.sh` 会把 `page/` 下的 Markdown 拍平推送到 GitHub Wiki 仓库。使用前需确认仓库 Wiki 功能已启用。
