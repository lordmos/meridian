# 任务 9：README 运营化

更新所有语言的 README（`.md` + `README.en.md` + `README.ja.md` + `README.zh-TW.md`）。

## README 编排模板

按以下顺序组织。**固定节**必须出现，**可选节**按项目实际情况保留。

```
[固定] 语言切换行
[固定] 徽章组（含 Powered by Meridian 徽章）
[固定] # 标题 + 一句话描述
[固定] ## Quick Start  ← 描述后第一节，必须
[固定] ## 能做什么 / Features
[可选] ## 背景 / Background
[可选] ## 系统架构 / Architecture
[可选] ## Agent 团队 / Agent Roster（仅多 Agent 项目）
[可选] ## 工作流 / Workflow（仅有明确阶段的项目）
[可选] ## 文件说明 / File Reference
[可选] ## 贡献 / Contributing
[可选] ## License
[固定] Powered by Meridian footer（最后一行）
```

**规则**：
- Quick Start **必须是正文第一节**，让用户立刻看到如何使用
- 不要删减项目原有技术内容
- 各语言版本章节顺序必须一致
- 不要有裸露的 `{{变量名}}` 占位符

---

## 语言切换行 + 徽章组

```markdown
> **语言 / Language**: [简体中文](README.md) · **当前语言** · [日本語](...) · [繁體中文](...)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/OWNER/REPO?style=flat-square&color=gold)](https://github.com/OWNER/REPO/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/OWNER/REPO?style=flat-square)](https://github.com/OWNER/REPO/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/OWNER/REPO/pulls)
[![Docs](https://img.shields.io/badge/Docs-online-4a9eff?style=flat-square&logo=vitepress&logoColor=white)](https://OWNER.github.io/REPO/)
[![Powered by Meridian](https://img.shields.io/badge/Powered%20by-Meridian-8b5cf6?style=flat-square)](https://github.com/lordmos/meridian)

<div align="center">
  <img src=".github/assets/hero.svg" alt="PROJECT_NAME" width="120" />
</div>

# PROJECT_NAME

一句话描述项目核心价值。
```

---

## Quick Start 节格式

```markdown
## Quick Start

> 📖 完整文档 → [在线阅读](https://OWNER.github.io/REPO/quick-start)

**Step 1** — 获取项目

\`\`\`bash
git clone https://github.com/OWNER/REPO.git
cd REPO
\`\`\`

**Step 2** — 用 AI 工具打开目录，说这一句话：

> [项目的触发句 / QUICK_START.md 中定义的启动命令]

AI 自主运行，完成后交付成果。你只需：① 回答初始问答 → ② 确认执行计划 → ③ 验收成果。

**中断后恢复** → 告诉 AI：`请读 checkpoint.md，继续上次未完成的工作。`
```

**写作规则**：
- 触发句/启动命令突出显示（blockquote 或代码块）
- 步骤极简，3 步以内
- 用户需要做的事不超过 3 件

---

## Powered by Meridian footer

README 最后一行加入（各语言版本均需加）：

```markdown
---

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit for Agent projects</sub>
```
