<!--
  Translation status:
  Source file : README.md
  Source commit: 13c198b
  Translated  : 2026-04-21
  Status      : up-to-date
-->

> **語言 / Language**: [简体中文](README.md) · [English](README.en.md) · [日本語](README.ja.md) · **繁體中文**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/lordmos/meridian?style=flat-square&color=gold)](https://github.com/lordmos/meridian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/lordmos/meridian?style=flat-square)](https://github.com/lordmos/meridian/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/lordmos/meridian/pulls)
[![Docs](https://img.shields.io/badge/Docs-online-4a9eff?style=flat-square&logo=vitepress&logoColor=white)](https://lordmos.github.io/meridian/)

<div align="center">
  <img src=".github/assets/hero.svg" alt="Meridian" width="120" />
</div>

# Meridian

把專案的 README、多語言、文件站、Logo、AI 工具上下文——這些重複勞動——壓縮成一次 AI 對話。

---

## Quick Start

用 AI 工具（Claude Code / Cursor / Windsurf 等）開啟 Meridian 目錄，說這一句話：

> 請你閱讀我的專案，專案目錄在 `[你的專案路徑]`，理解這個專案，給這個專案做一下運營配套。

AI 會先自主探索你的專案，再提案 3 個配色方案供你選擇，並列出 README 現存問題。你確認後，AI 自動完成所有運營工作。

你只需要做三件事：① 回答初始問答 → ② 選擇配色方案 → ③ 驗收成果。

**中斷後恢復** → 告訴 AI：`請讀 checkpoint.md，繼續上次未完成的工作。`

---

## Meridian 能做什麼

**視覺**
- 專案 Logo：SVG 漸層光效，配色跟隨用戶選定方案
- 統一主題：logo / 文件站 / 圖示共用一套配色

**內容**
- 品牌命名：有歷史/文化內涵的英文名 + 命名說明
- i18n 多語言化：简中/英/日/繁中 四語言 + 翻譯狀態追蹤
- README 運營化：徽章組 + 語言切換 + Quick Start 前置 + 文件站連結

**文件站**
- VitePress 多語言站 + GitHub Pages 自動部署

**AI 適配**
- 上下文文件：CLAUDE.md / AGENTS.md / .cursor/rules / .windsurf/rules
- 編排入口：QUICK_START.md（一句話啟動，AI 自主跑全程）

---

## 文件說明

| 文件 | 說明 |
|------|------|
| `PROMPT.md` | 可複用的運營提示詞（核心產出物，包含 10 項任務） |
| `QUICK_START.md` | AI 編排入口，寫給 AI 助手讀 |
| `templates/` | 提示詞引用的模板文件（VitePress 設定、GitHub Actions、Logo SVG、AI 工具文件等） |

---

**這個專案就是 Meridian，它的展示頁是用自己做的。** README、徽章、語言切換、[文件站](https://lordmos.github.io/meridian/)、Logo、AI 工具上下文——你看到的一切都是 Meridian 跑過自身一次後的產出。

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit</sub>
