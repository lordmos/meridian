<!--
  Translation status:
  Source file : README.md
  Source commit: (uncommitted)
  Translated  : 2026-04-04
  Status      : up-to-date
-->

> **語言 / Language**: [简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md) · **繁體中文**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/lordmos/meridian?style=flat-square&color=gold)](https://github.com/lordmos/meridian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/lordmos/meridian?style=flat-square)](https://github.com/lordmos/meridian/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/lordmos/meridian/pulls)

# Meridian

可複用的開源 Agent 專案運營工具包。給定任何一個開源 Agent 專案，在一次 AI 會話裡完成全套運營基礎設施搭建。

---

## Quick Start

用 AI 工具（Claude Code / Cursor / Windsurf 等）開啟 Meridian 目錄，說這一句話：

> 請你閱讀我的專案，專案目錄在 `[你的專案路徑]`，理解這個專案，給這個專案做一下運營配套。

AI 會先自主探索你的專案，再提案 3 個配色方案供你選擇，並列出 README 現存問題。你確認後，AI 自動完成所有運營工作。

你只需要做三件事：① 回答初始問答 → ② 選擇配色方案 → ③ 驗收成果。

**中斷後恢復** → 告訴 AI：`請讀 checkpoint.md，繼續上次未完成的工作。`

---

## Meridian 能做什麼

| 工作項 | 產出物 |
|--------|--------|
| **品牌命名** | 有歷史/文化內涵的英文專案名，附命名說明 |
| **i18n 多語言化** | 简中/英/日/繁中 四語言文件，含翻譯狀態注釋頭 |
| **VitePress 文件站** | 多語言 docs/ 站點 + GitHub Pages 自動部署 |
| **專案 Logo** | SVG 漸層光效 logo，配色與用戶選擇的方案一致 |
| **AI 工具適配** | CLAUDE.md / AGENTS.md / .cursor/rules / .windsurf/rules |
| **QUICK_START.md** | AI 編排入口：一句話啟動，AI 自主運行全程 |
| **Quick Start Guide** | 四語言人類可讀文件，三步上手 |
| **README 運營化** | 徽章組 + 語言切換 + Quick Start 前置 + 文件站連結 |

---

## 背景

Meridian 從 [Scriptorium](https://github.com/lordmos/tech-editorial) 的運營工作中提煉而來。Scriptorium 是一個多 Agent 技術書籍編寫框架，其運營工作涵蓋：

1. 給專案取名（Scriptorium）
2. 翻譯全部文件為 4 種語言（25 個 Markdown 文件 × 4 語言）
3. 搭建 VitePress 文件站 + GitHub Pages 自動部署
4. 設計漸層光效 SVG Logo
5. 為 Claude Code / OpenCode / Amp / Cursor / Windsurf 建立 AI 工具上下文文件
6. 建立 `QUICK_START.md`：AI 編排入口，實現「說一句話，AI 跑全程」的 UX
7. 完善 README（徽章、語言切換、Quick Start 前置、文件站入口）

---

## 文件說明

| 文件 | 說明 |
|------|------|
| `PROMPT.md` | 可複用的運營提示詞（核心產出物，包含 10 項任務） |
| `QUICK_START.md` | AI 編排入口，寫給 AI 助手讀 |
| `templates/` | 提示詞引用的模板文件（VitePress 設定、GitHub Actions、Logo SVG、AI 工具文件等） |
