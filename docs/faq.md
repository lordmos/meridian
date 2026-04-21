# FAQ

### Meridian 是做什么的？

Meridian 是一个开源项目运营工具包。它接受任意开源项目作为输入，在一次 AI 编程助手会话内产出一整套"推广配套"——品牌名、多语言 README、VitePress 文档站、Logo、AI 工具上下文文件、SEO/GEO 资产。

### 它解决了什么具体问题？

"项目代码写完了，但 README / 多语言 / 文档站 / Logo / 推广资产全要从零搭"这件事通常要花维护者一两天。Meridian 把这一两天压缩成一次 AI 会话：用户只需说一句话、选一个视觉风格、验收成果。

### 适合谁用？

任何开源项目维护者，特别是：

- 独自维护多个项目的开发者
- 刚开源的内部工具，需要快速补推广配套
- 不想学 VitePress / GitHub Actions / i18n 约定的一次性使用者

### 和 create-next-app / cookiecutter / copier 这类工具有什么区别？

那些是**代码脚手架**——产出是能运行的代码仓库。Meridian 是**运营物料**生成器——输入是已经能运行的项目，产出是围绕项目的 README / 文档站 / Logo / SEO 资产。

它**不改项目源代码**，只往仓库外围加。

### 怎么快速开始？

1. 克隆 Meridian 到本地
2. 在 AI 编程助手（Claude Code / Cursor / Windsurf）中打开 Meridian 目录
3. 粘贴这一句：

> 请你阅读我的项目，项目目录在 `[你的项目路径]`，理解这个项目，给这个项目做一下运营配套。

AI 会自主探索 → 提案风格 → 等你确认 → 执行全部任务。详见 [Quick Start](/quick-start)。

### 4 种视觉风格有什么区别？

| 风格 | 适合 |
|---|---|
| Glow | AI / Agent / 生成式项目 |
| Minimalist | CLI / 库 / docs-first |
| Dev-native | shell / SDK / 基建 |
| Enterprise | B2B / 平台 / 合规 |

AI 会根据目标项目类型推荐一个默认风格，用户可接受、换一个或说"随机"。每种风格包含完整视觉语言：配色、Logo、字体栈、VitePress 主题变量、图标风格。

### 支持哪些语言？

i18n 默认产出四语言：**简体中文 / English / 日本語 / 繁體中文**。翻译基于 `i18n/glossary.md` 作为单一权威来源，`scripts/check-i18n-drift.py` 做漂移检测。

### 生成的页面能被搜索引擎和 AI 答案引用吗？

可以。Meridian 的任务 12 会产出完整的 SEO + GEO 资产：

- **SEO**：`robots.txt` + `sitemap.xml` + OG/Twitter Card meta + JSON-LD SoftwareApplication schema
- **GEO**：`llms.txt`（按 [llms.txt](https://llmstxt.org) 标准）+ `llms-full.txt` + 结构化 FAQ 页面

这些让页面既能被 Google/Bing 索引，也能被 ChatGPT / Claude / Perplexity 作答时引用。

### 中断后怎么恢复？

Meridian 执行过程中在目标项目根目录维护 `checkpoint.md`。中断后告诉 AI：

> 请读 checkpoint.md，继续上次未完成的工作。

AI 会自动跳过已完成的任务，从下一步继续。

### 我能自定义风格或加新任务吗？

可以。

- **新增风格**：在 `templates/styles/` 新建目录，含 `hero.svg` / `preview.svg` / `palette.svg` / `style.md` / `vitepress-theme.css`，然后在 `PROMPT.md` / `QUICK_START.md` 的风格表里加一行
- **新增任务**：在 `templates/tasks/` 加 `task-NN-xxx.md`，然后在 `PROMPT.md` 的任务列表中加一节引用

Meridian 本身就是 "提示词 + 模板" 组合，所有扩展点都是 Markdown 文件。

### Meridian 的展示页真的是它自己做的吗？

是。本文档站（[lordmos.github.io/meridian](https://lordmos.github.io/meridian/)）、仓库 README 四语言版、徽章、Logo（`hero.svg`）、AI 工具上下文文件（`CLAUDE.md` / `AGENTS.md` / `.cursor/` / `.windsurf/`）、SEO 资产（OG 图、sitemap、llms.txt、本 FAQ 页）全部由 Meridian 跑自己一次生成。这个仓库就是它自己的 demo。
