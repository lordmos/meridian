> **语言 / Language**: **简体中文** · [English](README.en.md) · [日本語](README.ja.md) · [繁體中文](README.zh-TW.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/lordmos/meridian?style=flat-square&color=gold)](https://github.com/lordmos/meridian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/lordmos/meridian?style=flat-square)](https://github.com/lordmos/meridian/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/lordmos/meridian/pulls)

# Meridian

可复用的开源 Agent 项目运营工具包。给定任何一个开源 Agent 项目，在一次 AI 会话里完成全套运营基础设施搭建。

---

## Quick Start

用 AI 工具（Claude Code / Cursor / Windsurf 等）打开 Meridian 目录，说这一句话：

> 请你阅读我的项目，项目目录在 `[你的项目路径]`，理解这个项目，给这个项目做一下运营配套。

AI 会先自主探索你的项目，再提案 3 个配色方案供你选择，并列出 README 现存问题。你确认后，AI 自动完成所有运营工作。

你只需要做三件事：① 回答初始问答 → ② 选择配色方案 → ③ 验收成果。

**中断后恢复** → 告诉 AI：`请读 checkpoint.md，继续上次未完成的工作。`

---

## Meridian 能做什么

| 工作项 | 产出物 |
|--------|--------|
| **品牌命名** | 有历史/文化内涵的英文项目名，附命名说明 |
| **i18n 多语言化** | 简中/英/日/繁中 四语言文档，含翻译状态注释头 |
| **VitePress 文档站** | 多语言 docs/ 站点 + GitHub Pages 自动部署 |
| **项目 Logo** | SVG 渐变光效 logo，配色与用户选择的方案一致 |
| **AI 工具适配** | CLAUDE.md / AGENTS.md / .cursor/rules / .windsurf/rules |
| **QUICK_START.md** | AI 编排入口：一句话启动，AI 自主运行全程 |
| **Quick Start Guide** | 四语言人类可读文档，三步上手 |
| **README 运营化** | 徽章组 + 语言切换 + Quick Start 前置 + 文档站链接 |

---

## 背景

Meridian 从 [Scriptorium](https://github.com/lordmos/tech-editorial) 的运营工作中提炼而来。Scriptorium 是一个多 Agent 技术书籍编写框架，其运营工作涵盖：

1. 给项目取名（Scriptorium）
2. 翻译全部文档为 4 种语言（25 个 Markdown 文件 × 4 语言）
3. 搭建 VitePress 文档站 + GitHub Pages 自动部署
4. 设计渐变光效 SVG Logo
5. 为 Claude Code / OpenCode / Amp / Cursor / Windsurf 创建 AI 工具上下文文件
6. 创建 `QUICK_START.md`：AI 编排入口，实现"说一句话，AI 跑全程"的 UX
7. 完善 README（徽章、语言切换、Quick Start 前置、文档站入口）

---

## 文件说明

| 文件 | 说明 |
|------|------|
| `PROMPT.md` | 可复用的运营提示词（核心产出物，包含 10 项任务） |
| `QUICK_START.md` | AI 编排入口，写给 AI 助手读 |
| `templates/` | 提示词引用的模板文件（VitePress 配置、GitHub Actions、Logo SVG、AI 工具文件等） |
