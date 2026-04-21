<!--
  Translation status:
  Source file : README.md
  Source commit: 13c198b
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

プロジェクトの README、多言語化、ドキュメントサイト、ロゴ、AI ツールのコンテキストファイル——これらの繰り返し作業を、1 回の AI セッションに圧縮します。

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

---

## ファイル一覧

| ファイル | 説明 |
|----------|------|
| `PROMPT.md` | 再利用可能な運営プロンプト（主要成果物、10項目のタスクを含む） |
| `QUICK_START.md` | AI オーケストレーションエントリポイント、AI アシスタント向け |
| `templates/` | プロンプトで参照するテンプレートファイル（VitePress 設定、GitHub Actions、ロゴ SVG、AI ツールファイル等） |

---

**このプロジェクトが Meridian 本体であり、そのショーケースページは自分自身で作ったものです。** README、バッジ、言語切替、[ドキュメントサイト](https://lordmos.github.io/meridian/)、ロゴ、AI ツールのコンテキスト——ここに見えるすべてが、Meridian が自身を 1 回走らせて生成したものです。

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit</sub>
