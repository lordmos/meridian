<!--
  Translation status:
  Source file : README.md
  Source commit: b05cb92
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

給 AI 助手用的開源專案推廣工具包。在 Claude Code / Cursor / Windsurf 裡對它說一句「給我的專案做推廣配套」，AI 自動產生 README、多語言、文件站、Logo、AI 工具上下文、SEO + GEO 資產。

[快速開始](#quick-start) · [文件站](https://lordmos.github.io/meridian/zh-TW/) · [FAQ](https://lordmos.github.io/meridian/zh-TW/faq) · [GitHub](https://github.com/lordmos/meridian)

---

## Quick Start

用 AI 工具（Claude Code / Cursor / Windsurf 等）開啟 Meridian 目錄，說這一句話：

> 請你閱讀我的專案，專案目錄在 `[你的專案路徑]`，理解這個專案，給這個專案做一下運營配套。

AI 會先自主探索你的專案，再提案 3 個配色方案供你選擇，並列出 README 現存問題。你確認後，AI 自動完成所有運營工作。

你只需要做三件事：① 回答初始問答 → ② 選擇配色方案 → ③ 驗收成果。

**中斷後恢復** → 告訴 AI：`請讀 checkpoint.md，繼續上次未完成的工作。`

---

## 風格庫

Meridian 提供 4 種預設視覺風格。AI 會根據你的專案類型推薦一種，你也可以自己挑。下面每張圖是真實 VitePress 首頁在該風格下的渲染：

<table>
<tr>
<td align="center" width="50%">
<a href="templates/styles/minimalist/"><img src="templates/styles/minimalist/screenshot.png" alt="Minimalist VitePress 首頁截圖"/></a><br/>
<strong>Minimalist</strong> — 墨色 · 幾何 outline<br/>
<sub>CLI / 函式庫 / docs-first</sub>
</td>
<td align="center" width="50%">
<a href="templates/styles/enterprise/"><img src="templates/styles/enterprise/screenshot.png" alt="Enterprise VitePress 首頁截圖"/></a><br/>
<strong>Enterprise</strong> — 海軍藍醫章 · 幾何剛硬<br/>
<sub>B2B / 平台 / 合規</sub>
</td>
</tr>
<tr>
<td align="center" width="50%">
<a href="templates/styles/glow/"><img src="templates/styles/glow/screenshot.png" alt="Glow VitePress 首頁截圖"/></a><br/>
<strong>Glow</strong> — 漸層光暈 · 深空背景<br/>
<sub>AI / Agent / 生成式</sub>
</td>
<td align="center" width="50%">
<a href="templates/styles/dev-native/"><img src="templates/styles/dev-native/screenshot.png" alt="Dev-native VitePress 首頁截圖"/></a><br/>
<strong>Dev-native</strong> — 終端美學 · 霓虹青<br/>
<sub>shell / SDK / 基建</sub>
</td>
</tr>
</table>

每種風格定義一整套視覺語言——配色、logo、字型棧、VitePress 主題變數、圖示風格，不只是顏色。詳見 [`templates/styles/`](templates/styles/)。

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

**推廣（SEO + GEO）**
- SEO：Open Graph / Twitter Card / JSON-LD SoftwareApplication / sitemap.xml（含 hreflang）/ robots.txt — Google / Bing 檢索友好
- GEO：[llms.txt](https://llmstxt.org) + llms-full.txt + 結構化 FAQ 頁 — ChatGPT / Claude / Perplexity 答案引用友好
- 每風格一張 1200×630 OG 社交卡片（Facebook / Twitter / LinkedIn 連結預覽）

<details>
<summary>完整 12 項任務清單</summary>

| # | 任務 | 主要產出 |
|---|------|---------|
| 1 | 品牌命名 | 專案英文名 + 命名說明 |
| 2 | i18n 多語言化 | `i18n/glossary.md` + `i18n/{en,ja,zh-TW}/` + `README.*.md` |
| 3 | VitePress 文件站 | `docs/`（主題變數來自用戶選定風格）|
| 4 | GitHub Pages 部署 | `.github/workflows/docs.yml` |
| 5 | 專案 Logo | `docs/public/hero.svg` + `.github/assets/hero.svg` |
| 6 | AI 工具上下文 | `CLAUDE.md` / `AGENTS.md` / `.cursor/` / `.windsurf/` |
| 7 | QUICK_START.md | 根目錄 `QUICK_START.md` |
| 8 | Quick Start Guide | `docs/quick-start.md`（四語言）|
| 9 | README 運營化 | 所有語言 README |
| 10 | 收尾一致性檢查 | `.gitignore` + 建置驗證 + i18n drift 檢測 |
| 11 | Emoji → SVG 替換 | `docs/public/icons/` + 全部 md 替換 |
| 12 | Discoverability (SEO + GEO) | `robots.txt` + `og.png` + `llms.txt` + `llms-full.txt` + FAQ |

每項任務的詳細操作在 [`PROMPT.md`](PROMPT.md)，分片說明在 [`templates/tasks/`](templates/tasks/)。

</details>

---

## 檔案說明

| 檔案 | 說明 |
|------|------|
| `PROMPT.md` | 可複用的運營提示詞（核心產出物，包含 10 項任務） |
| `QUICK_START.md` | AI 編排入口，寫給 AI 助手讀 |
| `templates/` | 提示詞引用的範本檔（VitePress 設定、GitHub Actions、Logo SVG、AI 工具檔案等） |

---

**Meridian 自己給自己做的 Meridian。** README、徽章、語言切換、[文件站](https://lordmos.github.io/meridian/)、Logo、AI 工具上下文——你看到的一切都是它自己生成的。

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit</sub>
