# Meridian — AI Coding Assistant Context

## ⚡ Quick Reference

给目标项目做运营配套（触发句）：
> 请你阅读我的项目，项目目录在 `[目标项目路径]`，理解这个项目，给这个项目做一下运营配套。

中断后恢复：
> 请读 checkpoint.md，继续上次未完成的工作。

---

## 📖 About This Project

- **Name**: Meridian
- **Description**: 可复用的开源 Agent 项目运营工具包
- **GitHub**: https://github.com/lordmos/meridian

---

## 🏗️ Architecture

Meridian 是一个"提示词 + 模板文件"工具包，不包含可执行代码。

工作原理：用户填入目标项目信息 → 粘贴 `PROMPT.md` 到 AI 会话 → AI 自动执行 10 项运营任务。

核心设计：`PROMPT.md` 是主要产出物；`templates/` 提供可复用的模板文件（通过 file-pointer 方式引用，避免提示词臃肿）。

---

## 📁 Key Files

| 文件 | 说明 |
|------|------|
| `QUICK_START.md` | AI 编排入口，一句话启动 Meridian 工作流 |
| `PROMPT.md` | 核心产出：可复用的运营提示词（10 项任务） |
| `checkpoint.md` | 进度追踪文件，中断后恢复用（执行过程中生成） |
| `templates/hero.svg` | 指南针/子午线风格 Logo 模板 |
| `templates/vitepress-config.mts` | VitePress 多语言配置模板 |
| `templates/docs-workflow.yml` | GitHub Pages 部署 workflow 模板 |
| `templates/CLAUDE.md` | AI 工具上下文文件模板 |
| `templates/cursor-rules.mdc` | Cursor rules 模板 |
| `templates/windsurf-rules.md` | Windsurf rules 模板 |
| `templates/glossary.md` | 术语表模板（任务 2 i18n 统一术语用） |
| `templates/icons/` | Lucide outline SVG 图标库（任务 11 emoji → SVG 替换用） |
| `templates/scripts/check-i18n-drift.py` | 多语言漂移检测脚本（任务 10 收尾校验用） |
| `templates/tasks/` | 分片任务说明（task-2/3/9/11） |
| `scripts/check-i18n-drift.py` | Meridian 自身的 i18n 漂移检测（与 template 同步维护） |

---

## 🔑 Rules

1. Meridian 的工作**产出在目标项目仓库内**，不在本仓库
2. `templates/` 目录中的文件含 `{{变量名}}` 占位符——这是模板，不要替换
3. `PROMPT.md` 是主要产出物，不要随意修改其任务结构
4. 每步完成后更新 `checkpoint.md`
