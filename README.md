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

给 AI 助手用的开源项目推广工具包。在 Claude Code / Cursor / Windsurf 里对着它说一句「给我的项目做推广配套」，AI 自动生成 README、多语言、文档站、Logo、AI 工具上下文、SEO + GEO 资产。

[快速开始](#quick-start) · [文档站](https://lordmos.github.io/meridian/) · [FAQ](https://lordmos.github.io/meridian/faq) · [GitHub](https://github.com/lordmos/meridian)

---

## Quick Start

用 AI 工具（Claude Code / Cursor / Windsurf 等）打开 Meridian 目录，说这一句话：

> 请你阅读我的项目，项目目录在 `[你的项目路径]`，理解这个项目，给这个项目做一下运营配套。

AI 会先自主探索你的项目，再提案 3 个配色方案供你选择，并列出 README 现存问题。你确认后，AI 自动完成所有运营工作。

你只需要做三件事：① 回答初始问答 → ② 选择配色方案 → ③ 验收成果。

**中断后恢复** → 告诉 AI：`请读 checkpoint.md，继续上次未完成的工作。`

---

## 风格库

Meridian 提供 4 种预设视觉风格。AI 会根据你的项目类型推荐一种，你也可以自己挑。下面每张图是真实 VitePress 首页在该风格下的渲染：

<table>
<tr>
<td align="center" width="50%">
<a href="templates/styles/minimalist/"><img src="templates/styles/minimalist/screenshot.png" alt="Minimalist VitePress 首页截图"/></a><br/>
<strong>Minimalist</strong> — 墨色 · 几何 outline<br/>
<sub>CLI / 库 / docs-first</sub>
</td>
<td align="center" width="50%">
<a href="templates/styles/enterprise/"><img src="templates/styles/enterprise/screenshot.png" alt="Enterprise VitePress 首页截图"/></a><br/>
<strong>Enterprise</strong> — 海军蓝医章 · 几何刚硬<br/>
<sub>B2B / 平台 / 合规</sub>
</td>
</tr>
<tr>
<td align="center" width="50%">
<a href="templates/styles/glow/"><img src="templates/styles/glow/screenshot.png" alt="Glow VitePress 首页截图"/></a><br/>
<strong>Glow</strong> — 渐变光晕 · 深空背景<br/>
<sub>AI / Agent / 生成式</sub>
</td>
<td align="center" width="50%">
<a href="templates/styles/dev-native/"><img src="templates/styles/dev-native/screenshot.png" alt="Dev-native VitePress 首页截图"/></a><br/>
<strong>Dev-native</strong> — 终端美学 · 霓虹青<br/>
<sub>shell / SDK / 基建</sub>
</td>
</tr>
</table>

每种风格定义一整套视觉语言——配色、logo、字体栈、VitePress 主题变量、图标风格，不只是颜色。详见 [`templates/styles/`](templates/styles/)。

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

**推广（SEO + GEO）**
- SEO：Open Graph / Twitter Card / JSON-LD SoftwareApplication / sitemap.xml（含 hreflang）/ robots.txt — Google / Bing 检索友好
- GEO：[llms.txt](https://llmstxt.org) + llms-full.txt + 结构化 FAQ 页 — ChatGPT / Claude / Perplexity 答案引用友好
- 每风格一张 1200×630 OG 社交卡片（Facebook / Twitter / LinkedIn 链接预览）

<details>
<summary>完整 12 项任务清单</summary>

| # | 任务 | 主要产出 |
|---|------|---------|
| 1 | 品牌命名 | 项目英文名 + 命名说明 |
| 2 | i18n 多语言化 | `i18n/glossary.md` + `i18n/{en,ja,zh-TW}/` + `README.*.md` |
| 3 | VitePress 文档站 | `docs/`（主题变量来自用户选定风格）|
| 4 | GitHub Pages 部署 | `.github/workflows/docs.yml` |
| 5 | 项目 Logo | `docs/public/hero.svg` + `.github/assets/hero.svg` |
| 6 | AI 工具上下文 | `CLAUDE.md` / `AGENTS.md` / `.cursor/` / `.windsurf/` |
| 7 | QUICK_START.md | 根目录 `QUICK_START.md` |
| 8 | Quick Start Guide | `docs/quick-start.md`（四语言）|
| 9 | README 运营化 | 所有语言 README |
| 10 | 收尾一致性检查 | `.gitignore` + 构建验证 + i18n drift 检测 |
| 11 | Emoji → SVG 替换 | `docs/public/icons/` + 全部 md 替换 |
| 12 | Discoverability (SEO + GEO) | `robots.txt` + `og.png` + `llms.txt` + `llms-full.txt` + FAQ |

每项任务的详细操作在 [`PROMPT.md`](PROMPT.md)，分片说明在 [`templates/tasks/`](templates/tasks/)。

</details>

---

## 文件说明

| 文件 | 说明 |
|------|------|
| `PROMPT.md` | 可复用的运营提示词（核心产出物，包含 10 项任务） |
| `QUICK_START.md` | AI 编排入口，写给 AI 助手读 |
| `templates/` | 提示词引用的模板文件（VitePress 配置、GitHub Actions、Logo SVG、AI 工具文件等） |

---

**Meridian 自己给自己做的 Meridian。** README、徽章、语言切换、[文档站](https://lordmos.github.io/meridian/)、Logo、AI 工具上下文——你看到的一切都是它自己生成的。

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit</sub>
