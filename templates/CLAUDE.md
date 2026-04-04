# {{PROJECT_NAME}} — AI Coding Assistant Context

## ⚡ Quick Reference

一句话启动：
> {{PROJECT_NAME}} 的源码在 {{LOCAL_REPO_PATH}}。请读 QUICK_START.md，然后向我提问。没有问题就开始工作。

中断后恢复：
> 请读 checkpoint.md，继续上次未完成的工作。

---

## 📖 About This Project

- **Name**: {{PROJECT_NAME}}
- **Description**: {{DESCRIPTION}}
- **GitHub**: https://github.com/{{GITHUB_OWNER}}/{{REPO_NAME}}

---

## 🏗️ Architecture

<!-- 必填：简述项目的核心设计原则 -->
<!-- 示例："Agents are stateless; the file system is stateful." -->
[TODO: 填写核心架构说明]

---

## 📁 Key Files

<!-- 必填：列出最重要的文件及其作用（必须包含 QUICK_START.md） -->

| 文件 | 说明 |
|------|------|
| `QUICK_START.md` | AI 编排入口，一句话启动整个工作流 |
| `checkpoint.md` | 进度追踪文件，中断后恢复用 |
| [其他关键文件] | [说明] |

---

## 🔑 Rules

<!-- 必填：列出工作规则（如 File Pointer 机制、禁止操作等） -->
1. 每步骤完成后更新 `checkpoint.md`
2. [其他规则]

---

<!-- 可选节：仅在项目有明确 Agent 分工时填写 -->
<!--
## 🤖 Agent Roster

| Agent | 职责 |
|-------|------|
| [agent-name] | [职责描述] |
-->

<!-- 可选节：仅在项目有明确工作流阶段时填写 -->
<!--
## 🔄 Workflow

[工作流步骤]
-->
