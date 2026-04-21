# 任务 12：Discoverability（SEO + GEO）

让生成的站点在 Google / Bing（SEO）和 ChatGPT / Claude / Perplexity（GEO）里都能被检索到、被引用。

**⚠️ 只处理 Meridian 本任务流程产出的目标项目文件，不要改目标项目原有源代码。**

---

## Step 1 — robots.txt

复制 `templates/seo/robots.txt` 到 `docs/public/robots.txt`，把 `{{SITE_URL}}` 替换为目标项目部署地址（通常 `https://<GITHUB_OWNER>.github.io/<REPO_NAME>`）。

---

## Step 2 — VitePress head 注入（OG + Twitter Card + Canonical + JSON-LD + llms.txt 链接）

在 `docs/.vitepress/config.mts` 中：

1. 参照 `templates/seo/vitepress-head.snippet.mts` 填入 `SITE_URL / PROJECT_NAME / DESCRIPTION / OG_IMAGE_PATH / TWITTER_HANDLE / GITHUB_URL / LICENSE` 六个常量
2. 把 `seoHead` 数组合并到 `defineConfig({ head: [...existingHead, ...seoHead] })`

**OG_IMAGE_PATH** 通常是 `/{{REPO_NAME}}/og.png`（GitHub Pages base 已有）。Meridian 各风格的 OG 图生成模板在 `templates/styles/{id}/og.png`，默认风格复制到 `docs/public/og.png`。

---

## Step 3 — Sitemap

VitePress 1.3+ 内建。在 `config.mts` 添加：

```ts
sitemap: {
  hostname: '{{SITE_URL}}',
  transformItems(items) {
    return items.map(item => ({
      ...item,
      changefreq: item.url === '' ? 'weekly' : 'monthly',
      priority:   item.url === '' ? 1.0 : 0.7,
    }))
  },
},
```

构建时自动生成 `docs/.vitepress/dist/sitemap.xml`。详见 `templates/seo/sitemap.md`。

---

## Step 4 — llms.txt + llms-full.txt（GEO 核心）

### 4a. llms.txt（curation index）

1. 复制 `templates/llms-txt/llms.txt.template` 到**两处**：
   - `llms.txt`（仓库根目录 — GitHub 展示用）
   - `docs/public/llms.txt`（VitePress 静态资源 — 部署后在 `{{SITE_URL}}/llms.txt`）
2. 替换 `{{PROJECT_NAME}} / {{DESCRIPTION}} / {{SITE_URL}} / {{GITHUB_OWNER}} / {{REPO_NAME}} / {{LICENSE}}`
3. **AI 起草 5 条 FAQ**（根据目标项目实际能力，不要模板化）：
   - Q1：「这个项目是做什么的？」
   - Q2：「解决了什么具体问题？」
   - Q3：「适合谁用？」
   - Q4：「和 X / Y 类似工具相比优势是什么？」（X/Y 由 AI 识别的常见对标）
   - Q5：「怎么快速开始？」
   - 每问答都要**能独立引用**——开头一句就讲清楚，不依赖上下文

### 4b. llms-full.txt（full corpus）

复制 `templates/llms-txt/generate-llms-full.py` 到目标项目 `scripts/generate-llms-full.py`，运行：

```bash
python3 scripts/generate-llms-full.py              # zh-CN + README
python3 scripts/generate-llms-full.py --all-langs  # 含 en/ja/zh-TW
```

输出到仓库根 `llms-full.txt` + `docs/public/llms-full.txt`。

---

## Step 5 — FAQ 章节

在 `docs/faq.md` + 四语言版本（`docs/{en,ja,zh-TW}/faq.md`）新增 FAQ 页。内容与 llms.txt 的 5 条 FAQ 对齐但扩展为完整段落。

在 VitePress sidebar 加入 FAQ 入口。

**结构要求（GEO 友好）**：
- 每个问题用 **H3**
- 答案第一句话就**自包含**（读者不用读上下文就能懂）
- 避免"见上文"、"如前所述"
- 长答案后可加"更多细节"链接到深度文档

---

## Step 6 — OG 图片

- Meridian 产出的 OG 图（1200×630）在 `templates/styles/<id>/og.png`（每风格一张）
- 复制用户选定风格的 OG 到目标项目 `docs/public/og.png`
- **不要**把不同风格的都复制——一个项目只用一个风格的 OG

如需重新生成（比如主色改了），跑 `scripts/generate-og-images.py`（从 Meridian 复制到目标项目，方法同 llms-full.py）。

---

## Step 7 — 校验

构建站点 + 抓取生成的 HTML 确认 meta 注入成功：

```bash
cd docs && npm run docs:build
cat .vitepress/dist/sitemap.xml | head -10       # sitemap 含全页面
grep -o 'og:title\|twitter:card\|application/ld+json' .vitepress/dist/index.html  # head 注入
ls .vitepress/dist/llms.txt .vitepress/dist/llms-full.txt   # llms 文件已 copy
```

部署后验证：

```bash
curl -s {{SITE_URL}}/robots.txt | head -5
curl -s {{SITE_URL}}/llms.txt | head -20
curl -s {{SITE_URL}}/sitemap.xml | head -10
curl -s {{SITE_URL}}/og.png -o /tmp/og.png && file /tmp/og.png   # should be PNG 1200×630
```

社交预览实测（任选一）：
- Facebook: https://developers.facebook.com/tools/debug/ 输入站点 URL
- Twitter/X: https://cards-dev.twitter.com/validator
- LinkedIn: https://www.linkedin.com/post-inspector/

---

## Step 8 — 更新 checkpoint.md

```markdown
## [任务 12] 完成
- 时间：[ISO 时间]
- 产出：
  - docs/public/{robots.txt, og.png, llms.txt, llms-full.txt}
  - llms.txt, llms-full.txt（仓库根）
  - docs/.vitepress/config.mts（OG/Twitter/JSON-LD/sitemap 注入）
  - docs/faq.md + 四语言版
  - scripts/generate-llms-full.py
- 状态：✅
```

---

## 注意事项

- **别提交 `docs/.vitepress/dist/`**——是构建产物，gitignore 已覆盖
- **OG 图 1200×630** 是 Facebook/Twitter 推荐尺寸；不要用其他比例
- **llms.txt 不超过 ~10KB**——超过 LLM 可能截断。超量内容放 llms-full.txt
- **FAQ 是 GEO 的杀手锏**——LLM 在答 "X 是什么？" 时最喜欢引 FAQ；FAQ 质量 > 数量
- **Twitter handle 可选**——没有就不要塞占位符，直接删掉那行
