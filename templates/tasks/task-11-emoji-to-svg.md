# 任务 11：Emoji → SVG 替换（收尾后执行）

所有产出物完成、VitePress 构建通过、`{{ }}` 占位符已校验之后，统一把产出物中的 emoji 替换为 Lucide outline 风格的 inline SVG。图标**双色**上色（主形状 + 装饰线），颜色由 `--icon-stroke` / `--icon-accent` 两个 CSS 变量驱动，每种视觉风格 × 明暗两种模式各自定义一对——Glow 紫+青、Minimalist 墨+石、Enterprise 海军+金、Dev-native 青+玫瑰。

**⚠️ 只处理 Meridian 本任务流程产出的文件，不要改目标项目原有源代码或注释。**

---

## ⚠️ 关键原理：`<img>` 加载的 SVG 不继承 CSS

VitePress `features.icon: { src }` 渲染为 `<img class="VPImage">`，正文里的 `.md-icon` 也是 `<img>`。CSS `color` / `stroke` 不会穿透到 `<img>` 内的 SVG——`stroke="currentColor"` 退回到默认黑色。

过去这里走过两条错路：
1. **CSS `filter` 链**（brightness+invert+sepia+hue-rotate）——硬编码色值，换主题色需重算滤镜
2. **CSS `mask-image`**——支持单色但限死一种颜色，做不出双色区分

**正路**：运行时把 `<img>` 替换成 inline `<svg>`。CSS 能直接 target `svg` 里的 `path`，`stroke: var(--icon-stroke)` 真正生效。

---

## Step 1 — 复制图标库到目标项目

把 `templates/icons/` 整个目录复制到目标项目的 `docs/public/icons/`：

```bash
cp -r templates/icons 目标项目/docs/public/icons
```

`docs/public/` 是 VitePress 的静态资源目录，部署后路径为 `/{{REPO_NAME}}/icons/xxx.svg`。

---

## Step 2 — 接入 inline-SVG 运行时

把 `templates/vitepress-inline-svg.ts` 复制为目标项目的 `docs/.vitepress/theme/inline-svg.ts`：

```bash
cp templates/vitepress-inline-svg.ts 目标项目/docs/.vitepress/theme/inline-svg.ts
```

这个模块做两件事：
1. 把每个 `<img class="VPImage">` 或 `<img class="md-icon">` 替换成 inline `<svg>`（保留 class、width、height）
2. 给 SVG 内第一个 `<path>` 之外的图形元素打上 `class="accent"`，让 CSS 能给主形状 + 装饰线分别上色

然后修改 `docs/.vitepress/theme/index.ts` 启用它：

```ts
import DefaultTheme from 'vitepress/theme'
import type { EnhanceAppContext } from 'vitepress'
import { startInlineIconsWatcher } from './inline-svg'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ router }: EnhanceAppContext) {
    if (typeof window === 'undefined') return
    const boot = () => startInlineIconsWatcher()
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', boot)
    } else {
      boot()
    }
    router.onAfterRouteChange = () => startInlineIconsWatcher()
  },
}
```

---

## Step 3 — 验证 CSS 已定义图标变量

每种视觉风格的 `templates/styles/<style>/vitepress-theme.css` 里已经定义了：

```css
:root {
  --icon-stroke: var(--vp-c-brand-1);   /* 主形状 */
  --icon-accent: <每风格自选>;           /* 装饰线 */
  --icon-glow:   <每风格自选>;
}
.dark {
  --icon-stroke: <明亮变体>;
  --icon-accent: <明亮变体>;
  --icon-glow:   <明亮变体>;
}

.md-icon, svg.md-icon { ... stroke: var(--icon-stroke); ... }
svg.md-icon .accent   { stroke: var(--icon-accent); }

.VPFeature svg.VPImage       { stroke: var(--icon-stroke); ... }
.VPFeature svg.VPImage .accent { stroke: var(--icon-accent); }
```

**不要自己写 `color: var(--vp-c-brand-1); stroke: currentColor`**——那是旧方案，对 `<img>` 加载的 SVG 无效。选定风格的 `vitepress-theme.css` 已经包含正确规则，直接使用。

---

## Step 3 — Emoji → SVG 映射表

扫描以下文件中的 emoji 并替换：

**处理范围**：
- `docs/**/*.md`（VitePress 渲染，`.md-icon` CSS 生效）——含 `index.md` features 块的 `icon:` 字段、`quick-start.md`、`faq.md`、四语言页面
- VitePress 渲染的其它自定义页面

**不处理**（GitHub 原生渲染，不加载 CSS，`<img class="md-icon">` 会失去样式）：
- `README.md` + `README.{en,ja,zh-TW}.md`
- `CLAUDE.md` / `AGENTS.md`
- `QUICK_START.md`
- `.cursor/rules/project.mdc` / `.windsurf/rules/project.md`
- `checkpoint.md`、`templates/`、目标项目原有源代码、徽章 URL 内的 emoji

**理由**：GitHub 把 Markdown 渲染为 HTML 但不加载站点 CSS——`class="md-icon"` 失效，SVG 会显示但无主题色跟随；emoji 在 GitHub 下原生渲染良好。两侧各取所长。

**VitePress `home` layout features 替换**（注意两个陷阱）：

1. `icon:` 必须用**对象形式** `icon: { src: ... }`；string 形式会被当作字面文本渲染出 URL 字符串
2. `src:` 路径**不要带 `/{{REPO_NAME}}/` 前缀**——VitePress 会自动 prepend `base`，手写前缀会造成 `/repo/repo/icons/x.svg` 双重路径

正确写法：

```yaml
features:
  - icon:
      src: /icons/bolt.svg    # VitePress 自动 prepend base，最终 /{{REPO_NAME}}/icons/bolt.svg
    title: 一句话启动
    details: ...
```

对比 body Markdown 内的普通 `<img>`：这里 `src` **必须**带 `/{{REPO_NAME}}/` 前缀，因为 VitePress 不对原生 HTML 做 base 注入。两种 src 写法不同，别弄混。

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
| 🧭 | `sparkles.svg` *(best-fit)* | 品牌命名 / 指南 / 方向（未来若新增 `compass.svg` 可切过去）|

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

# 2. VitePress 构建再次通过（括号避免改变当前 shell 目录）
(cd docs && npm run docs:build)

# 3. 本地起服务目测 light/dark 切换时图标跟随主题色
npm run docs:dev

# 4. 如果复制了 scripts/verify-visual.py，跑自动回归
python3 scripts/verify-visual.py
```

预期：
- 第 1 条命令无输出（或只在徽章 URL 内命中）
- 第 2 条构建成功
- 第 3 条切换主题，图标**两种颜色**都跟随 CSS 变量变化（主形状 + 装饰线都响应明暗切换）
- 第 4 条（可选）断言 `<img>` 全部 swap 为 inline `<svg>`、primary stroke ≠ 黑色、多 path 图标有 `.accent` 标签

**常见坑**：
- 如果 icon 仍然是黑色——`theme/inline-svg.ts` 没被 `enhanceApp` 激活，检查 Step 2 的 `index.ts` 改动
- 如果 icon 单色无装饰——`inline-svg.ts` 的 `decorate()` 没有给非首 path 打 `.accent`，检查运行时报错
- 如果只有 light 或只有 dark 正确——检查 `style.css` 或 `vitepress-theme.css` 里的 `.dark { --icon-stroke: ... }` 覆盖

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
