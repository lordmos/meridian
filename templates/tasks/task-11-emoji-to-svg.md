# 任务 11：Emoji → SVG 替换（收尾后执行）

所有产出物完成、VitePress 构建通过、`{{ }}` 占位符已校验之后，统一把产出物中的 emoji 替换为 Lucide outline 风格的 inline SVG，风格适配当前主题色（通过 `currentColor` 跟随 `--vp-c-brand-1` / `--vp-c-text-1`）。

**⚠️ 只处理 Meridian 本任务流程产出的文件，不要改目标项目原有源代码或注释。**

---

## Step 1 — 复制图标库到目标项目

把 `templates/icons/` 整个目录复制到目标项目的 `docs/public/icons/`：

```bash
cp -r templates/icons 目标项目/docs/public/icons
```

`docs/public/` 是 VitePress 的静态资源目录，部署后路径为 `/{{REPO_NAME}}/icons/xxx.svg`。

---

## Step 2 — 在 style.css 注入 `.md-icon` 规则

在 `docs/.vitepress/theme/style.css` 末尾追加：

```css
/* Inline SVG icons (replaces emoji in markdown) */
.md-icon {
  display: inline-block;
  width: 1.1em;
  height: 1.1em;
  vertical-align: -0.18em;
  color: var(--vp-c-brand-1);
  stroke: currentColor;
}

/* Heading 场景略大 */
h1 .md-icon, h2 .md-icon, h3 .md-icon {
  width: 0.95em;
  height: 0.95em;
  vertical-align: -0.12em;
  margin-right: 0.15em;
}

/* 状态类图标语义色 */
.md-icon.is-success { color: var(--vp-c-success-1, #10b981); }
.md-icon.is-danger  { color: var(--vp-c-danger-1,  #ef4444); }
.md-icon.is-warning { color: var(--vp-c-warning-1, #f59e0b); }
```

---

## Step 3 — Emoji → SVG 映射表

扫描以下文件中的 emoji 并替换：

**处理范围**：
- `README.md` + `README.{en,ja,zh-TW}.md`
- `docs/**/*.md`（含 `index.md` / `quick-start.md` 四语言）
- `CLAUDE.md` / `AGENTS.md`
- `QUICK_START.md`
- `.cursor/rules/project.mdc` / `.windsurf/rules/project.md`

**不处理**：`checkpoint.md`、`templates/`、目标项目原有源代码、徽章 URL 内的 emoji。

所有替换写法的统一模板（下表省略 `<img>` 前缀与 `alt=""` 后缀，只列文件名与可选 class）：

```html
<img src="/{{REPO_NAME}}/icons/[文件名]" class="md-icon [状态类]" alt="" />
```

### 核心图标（结构/状态）

| Emoji | 文件名 | 额外 class |
|-------|--------|-----------|
| ⚡ | `bolt.svg` | |
| 📖 | `book-open.svg` | |
| 🏗️ | `layers.svg` | |
| 📁 | `folder.svg` | |
| 🔑 | `key.svg` | |
| 🤖 | `bot.svg` | |
| 🔄 | `refresh.svg` | |
| 🎯 | `target.svg` | |
| ✅ | `check-circle.svg` | `is-success` |
| ❌ | `x-circle.svg` | `is-danger` |
| ⚠️ | `alert-triangle.svg` | `is-warning` |

### 扩展图标（内容/功能）

| Emoji | 文件名 | 典型语义 |
|-------|--------|---------|
| 💡 | `lightbulb.svg` | Tip / 提示 / 灵感 |
| 🚀 | `rocket.svg` | 启动 / 部署 / 发布 |
| 📦 | `package.svg` | 依赖 / 模块 / 包 |
| 🔧 🛠️ | `wrench.svg` | 配置 / 调试 / 工具 |
| ⚙️ | `settings.svg` | 设置 / 选项 |
| 🎨 | `palette.svg` | 主题 / 配色 / 设计 |
| 🌐 | `globe.svg` | i18n / 多语言 / Web |
| 🔒 | `lock.svg` | 安全 / 权限 / 加密 |
| 📝 📄 | `file-text.svg` | 文档 / 笔记 / 协议 |
| 🐛 | `bug.svg` | 调试 / 缺陷 / 错误 |
| ✨ | `sparkles.svg` | 新特性 / 亮点 / 增强 |
| 🔍 | `search.svg` | 搜索 / 查找 |
| ℹ️ | `info.svg` | 信息 / 说明 |
| ❓ | `help-circle.svg` | FAQ / 疑问 |
| ⭐ 🌟 | `star.svg` | 推荐 / 亮点 / Star |
| 🎉 | `party-popper.svg` | 发布 / 庆祝 |
| 💻 🖥️ | `terminal.svg` | 命令行 / 代码 / 开发 |
| 🤝 | `handshake.svg` | 贡献 / 合作 / Contributing |
| 📊 📈 | `bar-chart.svg` | 数据 / 统计 / 指标 |

### 未覆盖的 emoji

若 Markdown 里出现映射表外的 emoji（如 🌙 ☀️ 🏷️ 🔔 🎁 💬 📅 等），按需在 `templates/icons/` 新建 Lucide outline SVG 并补进本映射表，命名沿用 Lucide 规范（小写+连字符）。

**路径说明**：`/{{REPO_NAME}}/` 前缀对应 VitePress `base` 子路径；本地 dev server 若不带 base 可临时用 `/icons/xxx.svg`。

---

## Step 4 — Heading 内的 emoji 特别处理

形如 `## ⚡ Quick Reference` 的 heading：
- 替换后 VitePress 自动生成的 anchor slug 会是 `#quick-reference`（干净）
- 而 emoji 原版的 slug 带 emoji 字符，URL 不美观

替换示例：
```markdown
## ⚡ Quick Reference
→
## <img src="/{{REPO_NAME}}/icons/bolt.svg" class="md-icon" alt="" /> Quick Reference
```

---

## Step 5 — 多语言同步

按 Meridian 既有规则，四语言 README 和 `docs/{en,ja,zh-TW}/` 下的页面必须同步替换，不能只改简中。

---

## Step 6 — 校验

替换完成后跑：

```bash
# 1. 产出物中应无功能性 emoji 残留（徽章 URL 除外）
#    推荐（跨平台，优先 ripgrep）：
rg '[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]' \
  README*.md docs CLAUDE.md AGENTS.md QUICK_START.md \
  .cursor .windsurf 2>/dev/null

#    无 rg 且在 Linux / GNU grep：
# grep -rP '[\x{1F300}-\x{1FAFF}\x{2600}-\x{27BF}]' README*.md docs CLAUDE.md ...

#    macOS 默认的 BSD grep 不支持 -P，用 ggrep（brew install grep）或 Python 兜底：
# python3 -c "import re,sys,pathlib;
# pat=re.compile(r'[\U0001F300-\U0001FAFF☀-➿]');
# [print(f'{p}:{i+1}:{l}') for p in pathlib.Path('.').rglob('*.md')
#  if 'node_modules' not in p.parts
#  for i,l in enumerate(p.read_text(errors='ignore').splitlines()) if pat.search(l)]"

# 2. VitePress 构建再次通过
cd docs && npm run docs:build

# 3. 本地起服务目测 light/dark 切换时图标跟随主题色
npm run docs:dev
```

预期：
- 第 1 条命令无输出（或只在徽章 URL 内命中）
- 第 2 条构建成功
- 第 3 条切换主题，图标颜色跟随 `--vp-c-brand-1` 变化

---

## Step 7 — 更新 checkpoint.md

```markdown
## [任务 11] 完成
- 时间：[ISO 时间]
- 产出：docs/public/icons/*.svg (11 个) + style.css .md-icon 规则 + 全部 md 文件 emoji 替换
- 状态：✅
```

---

## 注意事项

- **不要替换徽章 URL 内的 emoji**（如 `shields.io/badge/...` 参数中的 emoji），这些是第三方服务渲染，替换后徽章会坏
- **不要替换代码块内的 emoji**（` ``` ` 包裹的范围），可能是示例代码
- **不要改 `hero.svg`**，它是品牌 Logo，独立于图标体系
- 若目标项目 Markdown 不支持 inline HTML（极少见），降级为 `![](icons/bolt.svg)` + CSS 仍能生效
- 新 emoji 若不在映射表内，沿用 Lucide 命名规范添加到 `templates/icons/` 并补充映射表
