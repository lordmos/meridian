<!--
  Translation status:
  Source file : README.md
  Source commit: 4c9b514
  Translated  : 2026-04-21
  Status      : up-to-date
-->

> **語言 / Language**: [简体中文](README.md) · [English](README.en.md) · **日本語** · [繁體中文](README.zh-TW.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/lordmos/meridian?style=flat-square&color=gold)](https://github.com/lordmos/meridian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/lordmos/meridian?style=flat-square)](https://github.com/lordmos/meridian/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/lordmos/meridian/pulls)
[![Docs](https://img.shields.io/badge/Docs-online-4a9eff?style=flat-square&logo=vitepress&logoColor=white)](https://lordmos.github.io/meridian/)

<div align="center">
  <img src=".github/assets/hero.svg" alt="Meridian" width="120" />
</div>

# Meridian

プロジェクトの README、多言語化、ドキュメントサイト、ロゴ、AI ツールのコンテキスト、SEO / GEO 資産——プロモーションキット全部——を 1 回の AI セッションに圧縮します。

[クイックスタート](#quick-start) · [ドキュメント](https://lordmos.github.io/meridian/ja/) · [FAQ](https://lordmos.github.io/meridian/ja/faq) · [GitHub](https://github.com/lordmos/meridian)

---

## Quick Start

AI ツール（Claude Code / Cursor / Windsurf など）で Meridian ディレクトリを開き、次の一文を入力してください：

> 私のプロジェクトを読んでください。プロジェクトディレクトリは `[プロジェクトパス]` です。プロジェクトを理解して、運営基盤を整えてください。

AI がプロジェクトを自律的に探索した後、3 つのカラースキームを提案し、README の既存の問題点をリストアップします。確認後、AI がすべての運営作業を自動的に完了します。

あなたが行う作業は 3 つだけ：① 初期質問に回答 → ② カラースキームを選択 → ③ 成果物を確認

**中断後の再開** → AI に伝える：`checkpoint.md を読んで、未完了の作業を続けてください。`

---

## スタイルライブラリ

Meridian は 4 種類のプリセットビジュアルスタイルを用意しています。AI がプロジェクトタイプに応じて 1 つ推薦し、ユーザーは自由に選べます。下の各画像は実際の VitePress ホームページがそのスタイルで描画されたものです：

<table>
<tr>
<td align="center" width="50%">
<a href="templates/styles/minimalist/"><img src="templates/styles/minimalist/screenshot.png" alt="Minimalist VitePress ホーム"/></a><br/>
<strong>Minimalist</strong> — モノクロ · 幾何 outline<br/>
<sub>CLI / ライブラリ / docs-first</sub>
</td>
<td align="center" width="50%">
<a href="templates/styles/enterprise/"><img src="templates/styles/enterprise/screenshot.png" alt="Enterprise VitePress ホーム"/></a><br/>
<strong>Enterprise</strong> — ネイビーメダル · 剛性幾何<br/>
<sub>B2B / プラットフォーム / コンプライアンス</sub>
</td>
</tr>
<tr>
<td align="center" width="50%">
<a href="templates/styles/glow/"><img src="templates/styles/glow/screenshot.png" alt="Glow VitePress ホーム"/></a><br/>
<strong>Glow</strong> — グラデーションオーラ · 深宇宙<br/>
<sub>AI / Agent / 生成系</sub>
</td>
<td align="center" width="50%">
<a href="templates/styles/dev-native/"><img src="templates/styles/dev-native/screenshot.png" alt="Dev-native VitePress ホーム"/></a><br/>
<strong>Dev-native</strong> — ターミナル美学 · ネオンシアン<br/>
<sub>shell / SDK / インフラ</sub>
</td>
</tr>
</table>

各スタイルは視覚言語一式——パレット、ロゴ、タイプスタック、VitePress テーマ変数、アイコンスタイル——を定義します（色だけではありません）。詳細は [`templates/styles/`](templates/styles/) 参照。

---

## Meridian でできること

**ビジュアル**
- プロジェクトロゴ：SVG グラデーショングロー、配色はユーザーが選んだパレットに追従
- 統一テーマ：ロゴ / ドキュメントサイト / アイコンが 1 つの配色体系を共有

**コンテンツ**
- ブランド命名：歴史・文化的背景のある英語プロジェクト名 + 命名理由
- i18n 多言語化：简中 / en / ja / 繁中 の 4 言語 + 翻訳状況の追跡
- README の運営化：バッジ + 言語切替 + Quick Start 優先配置 + ドキュメントサイトリンク

**ドキュメントサイト**
- VitePress 多言語サイト + GitHub Pages 自動デプロイ

**AI 連携**
- コンテキストファイル：CLAUDE.md / AGENTS.md / .cursor/rules / .windsurf/rules
- オーケストレーションエントリ：QUICK_START.md（1 行で起動、AI が全プロセスを自律実行）

**プロモーション (SEO + GEO)**
- SEO：Open Graph / Twitter Card / JSON-LD SoftwareApplication / hreflang 付き sitemap.xml / robots.txt — Google / Bing にインデックス
- GEO：[llms.txt](https://llmstxt.org) + llms-full.txt + 構造化 FAQ ページ — ChatGPT / Claude / Perplexity の回答で引用可能
- スタイルごとに 1 枚 1200×630 の OG ソーシャルカード（Facebook / Twitter / LinkedIn のリンクプレビュー対応）

<details>
<summary>完全な 12 項目タスクリスト</summary>

| # | タスク | 主な成果物 |
|---|------|-----------|
| 1 | ブランド命名 | プロジェクト英語名 + 命名理由 |
| 2 | i18n 多言語化 | `i18n/glossary.md` + `i18n/{en,ja,zh-TW}/` + `README.*.md` |
| 3 | VitePress ドキュメントサイト | `docs/`（選定スタイルからテーマ変数を派生）|
| 4 | GitHub Pages デプロイ | `.github/workflows/docs.yml` |
| 5 | プロジェクトロゴ | `docs/public/hero.svg` + `.github/assets/hero.svg` |
| 6 | AI ツールのコンテキスト | `CLAUDE.md` / `AGENTS.md` / `.cursor/` / `.windsurf/` |
| 7 | QUICK_START.md | ルートの `QUICK_START.md` |
| 8 | Quick Start Guide | `docs/quick-start.md`（4 言語）|
| 9 | README 運営化 | 全言語の README |
| 10 | 整合性チェック | `.gitignore` + ビルド検証 + i18n ドリフトチェック |
| 11 | Emoji → SVG 置換 | `docs/public/icons/` + 全 md ファイル置換 |
| 12 | Discoverability (SEO + GEO) | `robots.txt` + `og.png` + `llms.txt` + `llms-full.txt` + FAQ |

各タスクの操作詳細は [`PROMPT.md`](PROMPT.md)、分割説明は [`templates/tasks/`](templates/tasks/)。

</details>

---

## ファイル一覧

| ファイル | 説明 |
|----------|------|
| `PROMPT.md` | 再利用可能な運営プロンプト（主要成果物、10項目のタスクを含む） |
| `QUICK_START.md` | AI オーケストレーションエントリポイント、AI アシスタント向け |
| `templates/` | プロンプトで参照するテンプレートファイル（VitePress 設定、GitHub Actions、ロゴ SVG、AI ツールファイル等） |

---

**Meridian が自分で作った Meridian。** README、バッジ、言語切替、[ドキュメントサイト](https://lordmos.github.io/meridian/)、ロゴ、AI ツールのコンテキスト——ここに見えるすべてが、Meridian 自身の手で生成されたものです。

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit</sub>
