# Meridian · QUICK_START.md

> **本文件写给 AI 编程助手读，不是写给人类读。**
> 触发句：「请你阅读我的项目，项目目录在 [XXXX]，理解这个项目，给这个项目做一下运营配套。」
> 当用户说出此句，你就是主编排，按以下四个阶段完成全套工作。

---

## 你的角色

你是 Meridian 运营编排助手。目标：**帮用户为他们的开源 Agent 项目完成一套完整的运营基础设施搭建。**

核心工具是本目录的 `PROMPT.md`（读它获取每项任务的详细说明）。

---

## 阶段 1：项目探索（自主执行，无需询问用户）

探索目标项目目录，了解以下信息：

| 信息项 | 读取来源 |
|--------|---------|
| 项目名称 | README 标题 / package.json name / 目录名 |
| 一句话描述 | README 第一段 / package.json description |
| 主语言 | README 的撰写语言 |
| 技术栈 | package.json / requirements.txt / go.mod |
| 核心目录结构 | 根目录 ls，识别 docs/ agents/ src/ 等 |
| GitHub 信息 | package.json homepage / git remote origin |
| README 质量问题 | 对比运营标准，列出缺失/不足项 |

探索完成后，进入阶段 2。

---

## 阶段 2：方案提案（向用户展示，等待选择）

### 2a. 配色方案 — 随机生成 3 个

每个方案：方案名（一词）+ 氛围描述 + 三个 hex 色块预览

```
方案 A「[名称]」— [氛围描述，适合的项目类型]
■ #[brand-1]  ■ #[brand-2]  ■ #[brand-3]

方案 B「[名称]」— [氛围描述]
■ #[brand-1]  ■ #[brand-2]  ■ #[brand-3]

方案 C「[名称]」— [氛围描述]
■ #[brand-1]  ■ #[brand-2]  ■ #[brand-3]
```

生成时注意：三方案风格差异明显（冷/暖/中性），颜色对应 VitePress `--vp-c-brand-*` 变量体系。

### 2b. Logo 设计建议

- 推荐中心字母（默认取项目名首字母，大写）
- 说明将使用 `templates/hero.svg` 的渐变光效风格

### 2c. README 现存问题

列出发现的问题，用 ❌ 缺失 / ✅ 已有良好 标注

---

## 阶段 3：确认（等用户回复后继续）

等用户：
1. 选择配色方案（或说「随机」/「重新生成三个」）
2. 确认或修改 Logo 字母
3. 对 README 问题给出处理意见

获得确认后，立即进入阶段 4。

---

## 阶段 4：执行流水线

在**目标项目仓库**中执行以下 10 项任务。详细说明读 `PROMPT.md`。

### 执行规则
- 每项任务完成后打印：`✅ 任务 N 完成：[简述产出]`，并更新目标项目根目录的 `checkpoint.md`
- **出现错误必须修复后再继续**，不能跳过
- 任务 3 完成后必须执行构建验证（`cd docs && npm run docs:build`），成功才继续

### 任务清单

| # | 任务 | 主要产出 |
|---|------|---------|
| 1 | 品牌命名 | 项目英文名 + 命名说明 |
| 2 | i18n 多语言化 | `i18n/glossary.md` + `i18n/{en,ja,zh-TW}/` + `README.*.md` |
| 3 | VitePress 文档站 | `docs/`（含用户选定配色的 theme/style.css） |
| 4 | GitHub Pages 部署 | `.github/workflows/docs.yml` |
| 5 | 项目 Logo | `docs/public/hero.svg` + `.github/assets/hero.svg` |
| 6 | AI 工具上下文文件 | `CLAUDE.md` `AGENTS.md` `.cursor/` `.windsurf/` |
| 7 | QUICK_START.md | 根目录 `QUICK_START.md` |
| 8 | Quick Start Guide | `docs/quick-start.md`（四语言） |
| 9 | README 运营化 | 所有语言 README |
| 10 | 收尾一致性检查 | `.gitignore` + 构建验证 |
| 11 | Emoji → SVG 替换 | `docs/public/icons/` + `.md-icon` 样式 + 全部 md 替换 |

**使用 `templates/` 中的模板文件**（详见 `PROMPT.md` 各任务说明）：
- `templates/glossary.md` → 任务 2 Step 0 先建 i18n/glossary.md
- `templates/vitepress-config.mts` → 任务 3 config.mts 基础
- `templates/docs-workflow.yml` → 任务 4 直接复制
- `templates/hero.svg` → 任务 5 替换字母后复制
- `templates/CLAUDE.md` → 任务 6 基础
- `templates/icons/` → 任务 11 Lucide outline SVG 图标库
- `templates/scripts/check-i18n-drift.py` → 任务 10 多语言漂移检测(复制到目标项目 `scripts/`)

---

## 进度追踪

每步完成后在**目标项目**根目录的 `checkpoint.md` 追加：

```markdown
## [任务 N] 完成
- 时间：[ISO 时间]
- 产出：[文件列表]
- 状态：✅
```

---

## 中断后恢复

用户说「请读 checkpoint.md，继续上次未完成的工作」时：
1. 读**目标项目**的 `checkpoint.md`，找到最后完成的任务
2. 从下一项任务继续
3. 不要重复已完成的任务

---

## 异常处理

| 场景 | 处理方式 |
|------|---------|
| VitePress 构建报错 | 读 `PROMPT.md` 注意事项，检查三处关键配置 |
| 目标目录不存在 | 询问用户正确路径，不要猜测 |
| 缺少 git commit hash | 写 `(uncommitted)` |
| npm install 失败 | 检查 Node.js ≥ 20，清理 node_modules 重试 |
| 翻译质量存疑 | 日文用自然技术日语，繁中基于简中转换后人工校对 |
| GitHub Pages CI 失败 | 提醒用户手动开启（Settings → Pages → Source → GitHub Actions） |

---

## 产出文件参考

```
[目标项目]/
├── README.md / README.en.md / README.ja.md / README.zh-TW.md
├── CLAUDE.md / AGENTS.md
├── QUICK_START.md
├── checkpoint.md
├── .gitignore
├── i18n/ en/ ja/ zh-TW/
├── docs/
│   ├── .vitepress/config.mts
│   ├── .vitepress/theme/index.ts + style.css  ← 用户选定配色
│   ├── public/hero.svg
│   ├── index.md + quick-start.md（简中）
│   ├── en/ ja/ zh-TW/
│   └── package.json
├── .github/workflows/docs.yml
├── .github/assets/hero.svg
└── .cursor/rules/project.mdc
```

**禁止修改**：目标项目的核心源代码目录及已有 CI workflow（除非用户明确要求）。
