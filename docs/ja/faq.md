<!--
  Translation status:
  Source file : docs/faq.md
  Source commit: (pending)
  Translated  : 2026-04-21
  Status      : up-to-date
-->

# FAQ

### Meridian は何をするツールですか？

Meridian はオープンソースプロジェクト運営ツールキットです。任意のオープンソースプロジェクトを入力として、1 回の AI アシスタントセッション内で "推進キット" を丸ごと生成します——ブランド名、多言語 README、VitePress ドキュメントサイト、ロゴ、AI ツールのコンテキストファイル、SEO/GEO 資産。

### 具体的に何を解決しますか？

「コードは書き終わったが、README / 多言語化 / ドキュメントサイト / ロゴ / プロモーション資料はゼロから構築」という作業は通常、メンテナが 1〜2 日かけます。Meridian はそれを 1 回の AI セッションに圧縮します：ひとこと話す、スタイルを選ぶ、成果物を確認。

### どのような人に向いていますか？

オープンソースプロジェクトのメンテナ全般、特に：

- 複数のプロジェクトを一人で維持している開発者
- オープンソース化したばかりで、推進資料を早く揃えたい内部ツール
- VitePress / GitHub Actions / i18n の作法を学びたくない一回きりのユーザー

### create-next-app / cookiecutter / copier との違いは？

それらは**コードのスキャフォールド**——実行可能なコードリポジトリを生成します。Meridian は**運営資料ジェネレータ**——入力はすでに動くプロジェクト、出力はその周辺の README / ドキュメントサイト / ロゴ / SEO 資産です。

プロジェクトのソースコードには**一切触れず**、外周にのみ追加します。

### どう始めますか？

1. Meridian をローカルにクローン
2. AI コーディングアシスタント（Claude Code / Cursor / Windsurf）で Meridian ディレクトリを開く
3. 次の 1 行を貼り付け：

> 私のプロジェクトを読んでください。プロジェクトディレクトリは `[プロジェクトパス]` です。プロジェクトを理解して、運営基盤を整えてください。

AI が自律的に探索 → スタイル提案 → 確認を待つ → 全タスクを実行。詳細は [Quick Start](/ja/quick-start)。

### 4 つのビジュアルスタイルの違いは？

| スタイル | 適用 |
|---|---|
| Glow | AI / Agent / 生成系 |
| Minimalist | CLI / ライブラリ / docs-first |
| Dev-native | shell / SDK / インフラ |
| Enterprise | B2B / プラットフォーム / コンプライアンス |

AI がプロジェクトタイプに応じて推薦し、ユーザーは受け入れ / 変更 / 「ランダム」と答えられます。各スタイルは視覚言語一式を定義：パレット、ロゴ、タイプスタック、VitePress テーマ変数、アイコンスタイル。

### 対応言語は？

i18n はデフォルトで 4 言語：**簡体字中国語 / 英語 / 日本語 / 繁體字中国語**。翻訳は `i18n/glossary.md` を唯一の権威とし、`scripts/check-i18n-drift.py` でドリフト検出を実行します。

### 生成されたページは検索エンジンや AI の回答で引用されますか？

はい。Meridian のタスク 12 が SEO + GEO 資産一式を生成します：

- **SEO**：`robots.txt` + `sitemap.xml` + OG/Twitter Card meta + JSON-LD SoftwareApplication schema
- **GEO**：`llms.txt`（[llms.txt](https://llmstxt.org) 標準準拠）+ `llms-full.txt` + 構造化 FAQ ページ

これにより Google/Bing にインデックスされ、ChatGPT / Claude / Perplexity が質問に答える際に引用可能になります。

### 中断後の再開方法は？

実行中、Meridian は対象プロジェクトのルートに `checkpoint.md` を維持します。中断後、AI に伝える：

> checkpoint.md を読んで、未完了の作業を続けてください。

AI が完了したタスクをスキップし、次のステップから続行します。

### カスタムスタイルや新しいタスクを追加できますか？

はい。

- **スタイル追加**：`templates/styles/` に新しいディレクトリを作成し、`hero.svg` / `preview.svg` / `palette.svg` / `style.md` / `vitepress-theme.css` を入れ、`PROMPT.md` / `QUICK_START.md` のスタイル表に一行追加
- **タスク追加**：`templates/tasks/task-NN-xxx.md` を作成し、`PROMPT.md` のタスクリストに参照セクションを追加

Meridian は「プロンプト + テンプレート」構成で、すべての拡張点は Markdown ファイルです。

### Meridian のデモページは本当に Meridian 自身が作ったのですか？

はい。このドキュメントサイト（[lordmos.github.io/meridian](https://lordmos.github.io/meridian/)）、4 言語の README、バッジ、ロゴ（`hero.svg`）、AI ツールのコンテキストファイル（`CLAUDE.md` / `AGENTS.md` / `.cursor/` / `.windsurf/`）、SEO 資産（OG 画像、sitemap、llms.txt、この FAQ ページ）——これらすべてが Meridian が自身を 1 回走らせて生成したものです。このリポジトリは、それ自体がデモです。
