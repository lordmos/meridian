<!--
  Translation status:
  Source file : README.md
  Source commit: 34750fd
  Translated  : 2026-04-04
  Status      : up-to-date
-->

> **语言 / Language**: [简体中文](README.md) · **English** · [日本語](README.ja.md) · [繁體中文](README.zh-TW.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/lordmos/meridian?style=flat-square&color=gold)](https://github.com/lordmos/meridian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/lordmos/meridian?style=flat-square)](https://github.com/lordmos/meridian/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/lordmos/meridian/pulls)
[![Docs](https://img.shields.io/badge/Docs-online-4a9eff?style=flat-square&logo=vitepress&logoColor=white)](https://lordmos.github.io/meridian/)

<div align="center">
  <img src=".github/assets/hero.svg" alt="Meridian" width="120" />
</div>

# Meridian

A reusable open-source Agent project operations toolkit. Given any open-source Agent project, build a complete operations infrastructure in a single AI session.

---

## Quick Start

Open the Meridian directory in an AI tool (Claude Code / Cursor / Windsurf, etc.) and say:

> Please read my project. The project directory is at `[your project path]`. Understand the project and set up the operations infrastructure for it.

The AI will first explore your project autonomously, then propose 3 color schemes for you to choose from, and list existing README issues. After your confirmation, the AI completes all operations work automatically.

You only need to do three things: ① Answer initial questions → ② Choose a color scheme → ③ Review the results.

**Resume after interruption** → Tell the AI: `Please read checkpoint.md and continue the unfinished work.`

---

## Style Library

Meridian ships 5 preset visual styles. The AI recommends one based on your project type; you can pick any:

<table>
<tr>
<td align="center" width="20%">
<img src="templates/styles/glow/preview.svg" width="96" alt="Glow"/><br/>
<strong>Glow</strong><br/>
<sub>Gradient aura · deep space</sub><br/>
<sub>AI / Agent / generative</sub>
</td>
<td align="center" width="20%">
<img src="templates/styles/minimalist/preview.svg" width="96" alt="Minimalist"/><br/>
<strong>Minimalist</strong><br/>
<sub>Monochrome ink · geometry</sub><br/>
<sub>CLI / libraries / docs-first</sub>
</td>
<td align="center" width="20%">
<img src="templates/styles/dev-native/preview.svg" width="96" alt="Dev-native"/><br/>
<strong>Dev-native</strong><br/>
<sub>Terminal · neon cyan</sub><br/>
<sub>shells / SDKs / infra</sub>
</td>
<td align="center" width="20%">
<img src="templates/styles/retro-terminal/preview.svg" width="96" alt="Retro-Terminal"/><br/>
<strong>Retro-Terminal</strong><br/>
<sub>Amber CRT · dashed frame</sub><br/>
<sub>games / emulators / retro</sub>
</td>
<td align="center" width="20%">
<img src="templates/styles/enterprise/preview.svg" width="96" alt="Enterprise"/><br/>
<strong>Enterprise</strong><br/>
<sub>Navy medallion · rigid geometry</sub><br/>
<sub>B2B / platforms / compliance</sub>
</td>
</tr>
</table>

Each style defines a full visual system — palette, logo, type stack, VitePress theme vars, icon style — not just colors. See [`templates/styles/`](templates/styles/).

---

## What Meridian Does

| Task | Output |
|------|--------|
| **Brand Naming** | English project name with historical/cultural significance, with naming rationale |
| **i18n Localization** | Simplified Chinese / English / Japanese / Traditional Chinese docs with translation status headers |
| **VitePress Docs Site** | Multilingual docs/ site + GitHub Pages auto-deployment |
| **Project Logo** | SVG gradient-glow logo matching the user's chosen color scheme |
| **AI Tool Integration** | CLAUDE.md / AGENTS.md / .cursor/rules / .windsurf/rules |
| **QUICK_START.md** | AI orchestration entry: one-liner launch, AI runs the full workflow autonomously |
| **Quick Start Guide** | Four-language human-readable docs, three-step setup |
| **README Operationalization** | Badge group + language switcher + Quick Start first + docs site link |

---

## Background

Meridian was distilled from the operations work done for [Scriptorium](https://github.com/lordmos/tech-editorial), a multi-Agent technical book writing framework. That work covered:

1. Naming the project (Scriptorium)
2. Translating all docs into 4 languages (25 Markdown files × 4 languages)
3. Setting up VitePress docs site + GitHub Pages auto-deployment
4. Designing a gradient-glow SVG Logo
5. Creating AI tool context files for Claude Code / OpenCode / Amp / Cursor / Windsurf
6. Creating `QUICK_START.md`: AI orchestration entry for "say one sentence, AI runs everything"
7. Polishing README (badges, language switcher, Quick Start first, docs site link)

---

## File Reference

| File | Description |
|------|-------------|
| `PROMPT.md` | Reusable operations prompt (the primary deliverable, contains 10 tasks) |
| `QUICK_START.md` | AI orchestration entry, written for AI assistants to read |
| `templates/` | Template files referenced by the prompt (VitePress config, GitHub Actions, Logo SVG, AI tool files, etc.) |

---

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit for Agent projects</sub>
