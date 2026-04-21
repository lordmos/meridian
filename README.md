> **语言 / Language**: **简体中文** · [English](README.en.md) · [日本語](README.ja.md) · [繁體中文](README.zh-TW.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/lordmos/meridian?style=flat-square&color=gold)](https://github.com/lordmos/meridian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/lordmos/meridian?style=flat-square)](https://github.com/lordmos/meridian/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/lordmos/meridian/pulls)
[![Docs](https://img.shields.io/badge/Docs-online-4a9eff?style=flat-square&logo=vitepress&logoColor=white)](https://lordmos.github.io/meridian/)

<div align="center">
  <img src=".github/assets/hero.svg" alt="Meridian" width="120" />
</div>

# Meridian

把项目的 README、多语言、文档站、Logo、AI 工具上下文——这些重复劳动——压缩成一次 AI 会话。

---

## Quick Start

用 AI 工具（Claude Code / Cursor / Windsurf 等）打开 Meridian 目录，说这一句话：

> 请你阅读我的项目，项目目录在 `[你的项目路径]`，理解这个项目，给这个项目做一下运营配套。

AI 会先自主探索你的项目，再提案 3 个配色方案供你选择，并列出 README 现存问题。你确认后，AI 自动完成所有运营工作。

你只需要做三件事：① 回答初始问答 → ② 选择配色方案 → ③ 验收成果。

**中断后恢复** → 告诉 AI：`请读 checkpoint.md，继续上次未完成的工作。`

---

## Meridian 能做什么

**视觉**
- 项目 Logo：SVG 渐变光效，配色跟随用户选定方案
- 统一主题：logo / 文档站 / 图标共用一套配色

**内容**
- 品牌命名：有历史/文化内涵的英文名 + 命名说明
- i18n 多语言化：简中/英/日/繁中 四语言 + 翻译状态追踪
- README 运营化：徽章组 + 语言切换 + Quick Start 前置 + 文档站链接

**文档站**
- VitePress 多语言站 + GitHub Pages 自动部署

**AI 适配**
- 上下文文件：CLAUDE.md / AGENTS.md / .cursor/rules / .windsurf/rules
- 编排入口：QUICK_START.md（一句话启动，AI 自主跑全程）

---

## 文件说明

| 文件 | 说明 |
|------|------|
| `PROMPT.md` | 可复用的运营提示词（核心产出物，包含 10 项任务） |
| `QUICK_START.md` | AI 编排入口，写给 AI 助手读 |
| `templates/` | 提示词引用的模板文件（VitePress 配置、GitHub Actions、Logo SVG、AI 工具文件等） |

---

**这个项目就是 Meridian，它的展示页是用自己做的。** README、徽章、语言切换、[文档站](https://lordmos.github.io/meridian/)、Logo、AI 工具上下文——你看到的一切都是 Meridian 跑过自身一次后的产出。

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit</sub>
