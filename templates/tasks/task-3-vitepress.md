# 任务 3：VitePress 文档站

在 `docs/` 目录搭建 VitePress 多语言文档站。

## 目录结构

```
docs/
├── package.json               ← VitePress 依赖（vitepress: ^1.6.x）
├── .vitepress/
│   ├── config.mts             ← 多语言配置
│   └── theme/
│       ├── index.ts           ← 主题入口
│       └── style.css          ← 自定义配色（用户选择的方案）
├── public/
│   └── hero.svg               ← Logo（任务 5 产出）
├── index.md                   ← 简中首页（layout: home）
├── {原始文档目录}/              ← symlink → ../原始目录（如有）
├── en/ ja/ zh-TW/             ← 各语言首页 + symlink 到 i18n/
```

## config.mts

以 `templates/vitepress-config.mts` 为基础，替换占位符：

- `{{REPO_NAME}}` → 仓库名（`base` 子路径，**必须设置**）
- `{{PROJECT_NAME}}` → 项目名称（用于页面 `<title>`）
- `{{PROJECT_DESCRIPTION}}` → 一句话描述（用于 meta description）
- `{{GITHUB_OWNER}}` / `{{REPO_NAME}}` → 社交链接
- 各语言 `nav` 和 `sidebar` → 按项目实际文档目录补全
- `themeConfig.footer` → 加入 Powered by Meridian（见下方）

**三处关键配置（勿删）**：
- `escape_vue_interpolation` — 防止 `{{变量名}}` 被 Vue 编译器当作插值表达式报错
- `vite.resolve.preserveSymlinks: true` — 修复 symlink 指向 docs/ 外时 node_modules 无法解析
- `base: '/{{REPO_NAME}}/'` — 防止 GitHub Pages 子路径部署后静态资源全部 404

**⚠️ 常见错误**：`base` 已设置时，`image.src` 里**不要**再带仓库名路径。
```yaml
# ✅ 正确
image:
  src: /hero.svg

# ❌ 错误（会变成 /meridian/meridian/hero.svg）
image:
  src: /meridian/hero.svg
```

## theme/index.ts

```typescript
import DefaultTheme from 'vitepress/theme'
import './style.css'
export default DefaultTheme
```

## theme/style.css

填入阶段 3 用户选择的配色（`--vp-c-brand-*`）。

**⚠️ 注意**：VitePress 默认 brand 就是 indigo，若选择 indigo 配色视觉上不会有变化，务必使用与默认不同的颜色。

```css
:root {
  --vp-c-brand-1: [brand-1];
  --vp-c-brand-2: [brand-2];
  --vp-c-brand-3: [brand-3];
  --vp-c-brand-soft: rgba([brand-1 rgb], 0.14);
}
.dark {
  --vp-c-brand-1: [bright variant of brand-1];
  --vp-c-brand-2: [brand-1];
  --vp-c-brand-3: [brand-2];
  --vp-c-brand-soft: rgba([brand-1 rgb], 0.16);
}
```

## 首页（index.md）格式

首页不是技术目录，也不是架构摘要。它的第一屏要让第一次看到项目的人立刻明白：

- **谁会用**：目标用户、团队或工作角色
- **在哪里用**：日常工作流、业务流程、开发/运营/协作场景
- **解决什么痛点**：减少哪类摩擦、风险、重复劳动或信息断层
- **得到什么结果**：用户完成后获得的具体收益

技术架构、协议名、runtime、内部模块名可以出现，但必须服务于用户价值说明；不要让它们成为首页主卖点。

```yaml
---
layout: home
titleTemplate: ':title'   # 避免首页出现"项目名 | 项目名"重复
hero:
  name: "PROJECT_NAME"
  text: "面向目标用户的业务/应用定位"
  tagline: "说明它在什么场景下帮用户解决什么问题，并带来什么结果。"
  image:
    src: /hero.svg
    alt: PROJECT_NAME
  actions:
    - theme: brand
      text: 快速开始 →
      link: /quick-start
    - theme: alt
      text: GitHub
      link: https://github.com/OWNER/REPO
features:
  - icon:
      src: /icons/target.svg
    title: 场景或收益标题
    details: 用普通读者能理解的话说明这个场景下的价值，不写成模块名。
---
```

首页 frontmatter 下方建议补两段正文，让 LLM、搜索引擎和人类读者都能独立理解项目：

```markdown
## 适合这些场景

- 场景 1：说明谁在什么时候会需要它。
- 场景 2：说明它减少哪类重复劳动或风险。
- 场景 3：说明它如何接入已有工作流。

## 一句话理解

如果你只记住一件事：PROJECT_NAME 是一个……，它帮助……把……变成……。
```

**好坏对照**：

- 不要写：`基于 SQLite、MCP、runtime overlay 的自动化框架`
- 应该写：`让个人日程、提醒和 agent 执行记录在写入前先确认，避免私有生活状态被公开仓库污染`
- 不要写：`Feature: plugin system / docs workflow / i18n`
- 应该写：`给维护者一套可复用的发布页面、快速开始和多语言说明，让项目第一次被看到时就能被理解`

**⚠️ 注意**：首页必须加 `titleTemplate: ':title'`，否则页面标题会出现"项目名 | 项目名"的重复。子页面（quick-start.md 等）无需此设置，会自动显示"页面标题 | 项目名"。

**多语言要求**：四语言首页必须同步更新。不要只把业务场景写进简中首页，其他语言仍保留技术清单。

## Powered by Meridian（VitePress footer）

在 `config.mts` 的 `themeConfig` 中加入：

```typescript
themeConfig: {
  footer: {
    message: 'Built with <a href="https://github.com/lordmos/meridian" target="_blank">Meridian</a>',
  },
  // ...其他配置
}
```

## 安装 & 验证

```bash
cd docs
npm install        # 生成 package-lock.json
npm run docs:build # 必须构建成功再继续
```
