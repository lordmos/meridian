# Meridian — Windsurf Rules

可复用的开源 Agent 项目运营工具包。给定任何一个开源 Agent 项目，在一次 AI 会话里完成全套运营基础设施搭建。

## Quick Start

给目标项目做运营配套（触发句）：
> 请你阅读我的项目，项目目录在 `[目标项目路径]`，理解这个项目，给这个项目做一下运营配套。

中断后恢复：
> 请读 checkpoint.md，继续上次未完成的工作。

## Key Files

- `QUICK_START.md` — AI 编排入口
- `PROMPT.md` — 核心提示词（10 项运营任务）
- `templates/` — 模板文件（含 `{{变量名}}` 占位符，勿替换）
- `checkpoint.md` — 进度追踪

## Rules

1. 产出写入**目标项目**，不写入 Meridian 本仓库
2. `templates/` 文件是模板，保持占位符原样
3. 每步完成后更新 checkpoint.md
