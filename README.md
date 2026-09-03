# NUS Coursework Wiki

记录 NUS Computer Engineering coursework 的课程要求、原始资源、短知识页面、CA/项目过程与最终产出。

## 当前范围

- 当前课程：CEG5201（Week 04 进行中）、CEG5302（Lecture 04 进行中）
- CEG5201 已整理：Week 01–03 讲义拆分页、课程资源、课程要求、CA1 Consultation 页面
- CEG5201 未整理：Week 04 及以后讲义、CA1 个人最终产出、CA2 正式项目内容
- CEG5302 已整理：Lecture 01–04 讲义拆分页（以老师课件为准、个人笔记为辅）、课程资源、课程要求
- CEG5302 未整理：Lecture 05 及以后讲义、三次测试/编程作业/project 产出

内容源文件位于 `page/`，构建脚本位于 `script/`，本地预览产物位于被忽略的 `build/`。

本地预览使用仓库内固定版本的 Mermaid 11.17.2 浏览器构建，避免依赖外部 CDN；第三方许可证位于 `script/vendor/mermaid-LICENSE`。

## 本地预览

先按 `references/build-and-publish.md` 为 `build/preview/.venv` 安装 `mkdocs-material`，然后：

```powershell
python script/build.py
& .\build\preview\.venv\Scripts\mkdocs.exe serve -f .\script\mkdocs.yml -a 127.0.0.1:8000
```

或在 Bash 环境运行 `./script/serve.sh`；Windows PowerShell 可运行 `./script/serve.ps1`。

## 发布

GitHub Wiki 页面拍平发布脚本为 `script/publish-wiki.sh`。发布前请确认 Wiki 功能已启用，并检查不应公开的声明表、个人信息和草稿没有被复制进 `page/`。
