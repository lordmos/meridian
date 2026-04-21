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

## Step 8 — Search Console 验证 + Sitemap 提交（引导用户手动完成）

**这一步无法自动化**——需要用户登录搜索引擎的站长后台生成验证 token。AI 的职责是**把操作流程打印出来，收到 token 后帮用户写入 config、commit、push**。

### 8a. 打印给用户的指引（AI 照念）

```
✅ 站点已部署到 {{SITE_URL}}。
搜索引擎现在可以自动爬取（robots.txt 已声明 sitemap），但要看到索引状态 /
手动提交 sitemap / 请求优先索引，需要验证站点所有权。请按下面操作：

【Google Search Console（最重要）】
1. 打开 https://search.google.com/search-console
2. 左上角 Add Property → 选 "URL prefix" → 输入：{{SITE_URL}}/
3. 验证方法选 "HTML tag"
4. 复制给你的 <meta name="google-site-verification" content="..."> 里面的 content 字符串
5. **把那串字符发给我**

【Bing Webmaster（可选但建议）】
1. 打开 https://www.bing.com/webmasters
2. Add a site → 输入 {{SITE_URL}}/
3. 选 "HTML Meta Tag" → 复制 content 字符串发给我
4. 或者用 "Import from Google Search Console"（更快）

【Baidu 站长（国内用户）】
⚠️ GH Pages IP 在国内索引率极低，建议自建 CN 域名后再做。跳过或留后续。
```

### 8b. 收到 token 后 — AI 直接操作

用户返回 content 串后，AI：

1. 把 `templates/seo/verification-meta.snippet.mts` 复制到 `docs/.vitepress/verification-meta.mts`
2. 按 token 对应**取消注释**一行或多行，填入 content 值
3. 在 `docs/.vitepress/config.mts` 顶部 `import { verificationHead } from './verification-meta'`
4. `head` 数组里 spread 进去：`head: [...seoHead, ...verificationHead]`
5. commit、push、等待 CI 重新部署
6. 通知用户："已部署，现在回 Search Console 点 **Verify**"
7. 验证成功后，继续引导：
   ```
   左侧菜单 Sitemaps → 输入 "sitemap.xml" → Submit
   URL Inspection → 输入 {{SITE_URL}}/ → Request indexing（首页优先）
   ```

### 8c. 不验证行不行？

行——Google 依然会通过 `robots.txt` 的 `Sitemap:` 指令发现你的 sitemap 并爬取。验证只是**额外**打开站长后台的数据面板（索引覆盖率、URL inspection、手动 request indexing）。若用户说"暂时不搞"就跳过此步，记录到 checkpoint.md 备注。

---

## Step 9 — 更新 checkpoint.md

```markdown
## [任务 12] 完成
- 时间：[ISO 时间]
- 产出：
  - docs/public/{robots.txt, og.png, llms.txt, llms-full.txt}
  - llms.txt, llms-full.txt（仓库根）
  - docs/.vitepress/config.mts（OG/Twitter/JSON-LD/sitemap 注入）
  - docs/.vitepress/verification-meta.mts（Search Console 验证 meta，若已填充）
  - docs/faq.md + 四语言版
  - scripts/generate-llms-full.py
- Search Console 验证状态：
  - [ ] Google Search Console: 已验证 / 用户暂缓 / token 待返回
  - [ ] Bing Webmaster: 已验证 / 用户暂缓 / token 待返回
  - [ ] Sitemap 提交: Google / Bing
- 状态：✅
```

---

## 注意事项

- **别提交 `docs/.vitepress/dist/`**——是构建产物，gitignore 已覆盖
- **OG 图 1200×630** 是 Facebook/Twitter 推荐尺寸；不要用其他比例
- **llms.txt 不超过 ~10KB**——超过 LLM 可能截断。超量内容放 llms-full.txt
- **FAQ 是 GEO 的杀手锏**——LLM 在答 "X 是什么？" 时最喜欢引 FAQ；FAQ 质量 > 数量
- **Twitter handle 可选**——没有就不要塞占位符，直接删掉那行
