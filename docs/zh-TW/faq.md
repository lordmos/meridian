<!--
  Translation status:
  Source file : docs/faq.md
  Source commit: f603973
  Translated  : 2026-04-21
  Status      : up-to-date
-->

# FAQ

### Meridian 是做什麼的？

Meridian 是一個開源專案運營工具包。它接受任意開源專案作為輸入，在一次 AI 編程助手對話內產出一整套"推廣配套"——品牌名、多語言 README、VitePress 文件站、Logo、AI 工具上下文檔案、SEO/GEO 資產。

### 它解決了什麼具體問題？

"專案程式碼寫完了，但 README / 多語言 / 文件站 / Logo / 推廣資產全要從零搭"這件事通常要花維護者一兩天。Meridian 把這一兩天壓縮成一次 AI 對話：使用者只需說一句話、選一個視覺風格、驗收成果。

### 適合誰用？

任何開源專案維護者，特別是：

- 獨自維護多個專案的開發者
- 剛開源的內部工具，需要快速補推廣配套
- 不想學 VitePress / GitHub Actions / i18n 約定的一次性使用者

### 和 create-next-app / cookiecutter / copier 這類工具有什麼區別？

那些是**程式碼鷹架**——產出是能運行的程式碼倉庫。Meridian 是**運營物料**生成器——輸入是已經能運行的專案，產出是圍繞專案的 README / 文件站 / Logo / SEO 資產。

它**不改專案原始碼**，只往倉庫外圍加。

### 怎麼快速開始？

1. 複製 Meridian 到本機
2. 在 AI 編程助手（Claude Code / Cursor / Windsurf）中開啟 Meridian 目錄
3. 貼上這一句：

> 請你閱讀我的專案，專案目錄在 `[你的專案路徑]`，理解這個專案，給這個專案做一下運營配套。

AI 會自主探索 → 提案風格 → 等你確認 → 執行全部任務。詳見 [Quick Start](/zh-TW/quick-start)。

### 4 種視覺風格有什麼區別？

| 風格 | 適合 |
|---|---|
| Glow | AI / Agent / 生成式 |
| Minimalist | CLI / 函式庫 / docs-first |
| Dev-native | shell / SDK / 基建 |
| Enterprise | B2B / 平台 / 合規 |

AI 會根據目標專案類型推薦一個預設風格，使用者可接受、換一個或說"隨機"。每種風格包含完整視覺語言：配色、Logo、字型棧、VitePress 主題變數、圖示風格。

### 支援哪些語言？

i18n 預設產出四語言：**簡體中文 / English / 日本語 / 繁體中文**。翻譯基於 `i18n/glossary.md` 作為單一權威來源，`scripts/check-i18n-drift.py` 做漂移檢測。

### 生成的頁面能被搜尋引擎和 AI 答案引用嗎？

可以。Meridian 的任務 12 會產出完整的 SEO + GEO 資產：

- **SEO**：`robots.txt` + `sitemap.xml` + OG/Twitter Card meta + JSON-LD SoftwareApplication schema
- **GEO**：`llms.txt`（按 [llms.txt](https://llmstxt.org) 標準）+ `llms-full.txt` + 結構化 FAQ 頁面

這些讓頁面既能被 Google/Bing 索引，也能被 ChatGPT / Claude / Perplexity 作答時引用。

### 中斷後怎麼恢復？

Meridian 執行過程中在目標專案根目錄維護 `checkpoint.md`。中斷後告訴 AI：

> 請讀 checkpoint.md，繼續上次未完成的工作。

AI 會自動跳過已完成的任務，從下一步繼續。

### 我能自訂風格或加新任務嗎？

可以。

- **新增風格**：在 `templates/styles/` 新建目錄，含 `hero.svg` / `preview.svg` / `palette.svg` / `style.md` / `vitepress-theme.css`，然後在 `PROMPT.md` / `QUICK_START.md` 的風格表裡加一行
- **新增任務**：在 `templates/tasks/` 加 `task-NN-xxx.md`，然後在 `PROMPT.md` 的任務列表中加一節引用

Meridian 本身就是 "提示詞 + 範本" 組合，所有擴展點都是 Markdown 檔案。

### Meridian 的展示頁真的是它自己做的嗎？

是。本文件站（[lordmos.github.io/meridian](https://lordmos.github.io/meridian/)）、倉庫 README 四語言版、徽章、Logo（`hero.svg`）、AI 工具上下文檔案（`CLAUDE.md` / `AGENTS.md` / `.cursor/` / `.windsurf/`）、SEO 資產（OG 圖、sitemap、llms.txt、本 FAQ 頁）全部由 Meridian 跑自己一次生成。這個倉庫就是它自己的 demo。
