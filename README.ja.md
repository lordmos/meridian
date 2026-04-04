<!--
  Translation status:
  Source file : README.md
  Source commit: (uncommitted)
  Translated  : 2026-04-04
  Status      : up-to-date
-->

> **語言 / Language**: [简体中文](README.md) · [English](README.en.md) · **日本語** · [繁體中文](README.zh-TW.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/lordmos/meridian?style=flat-square&color=gold)](https://github.com/lordmos/meridian/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/lordmos/meridian?style=flat-square)](https://github.com/lordmos/meridian/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/lordmos/meridian/pulls)
[![Docs](https://img.shields.io/badge/Docs-online-4a9eff?style=flat-square&logo=vitepress&logoColor=white)](https://lordmos.github.io/meridian/)

# Meridian

再利用可能なオープンソース Agent プロジェクト運営ツールキット。任意のオープンソース Agent プロジェクトに対して、1 回の AI セッションで完全な運営基盤を構築できます。

---

## Quick Start

AI ツール（Claude Code / Cursor / Windsurf など）で Meridian ディレクトリを開き、次の一文を入力してください：

> 私のプロジェクトを読んでください。プロジェクトディレクトリは `[プロジェクトパス]` です。プロジェクトを理解して、運営基盤を整えてください。

AI がプロジェクトを自律的に探索した後、3 つのカラースキームを提案し、README の既存の問題点をリストアップします。確認後、AI がすべての運営作業を自動的に完了します。

あなたが行う作業は 3 つだけ：① 初期質問に回答 → ② カラースキームを選択 → ③ 成果物を確認

**中断後の再開** → AI に伝える：`checkpoint.md を読んで、未完了の作業を続けてください。`

---

## Meridian でできること

| 作業項目 | 成果物 |
|----------|--------|
| **ブランド命名** | 歴史・文化的背景を持つ英語プロジェクト名（命名理由付き） |
| **i18n 多言語化** | 简体中文 / English / 日本語 / 繁體中文 の4言語ドキュメント |
| **VitePress ドキュメントサイト** | 多言語 docs/ サイト + GitHub Pages 自動デプロイ |
| **プロジェクトロゴ** | SVG グラデーション発光ロゴ（選択したカラースキームに対応） |
| **AI ツール連携** | CLAUDE.md / AGENTS.md / .cursor/rules / .windsurf/rules |
| **QUICK_START.md** | AI オーケストレーションエントリポイント：1文で起動、AI が全プロセスを自律実行 |
| **クイックスタートガイド** | 4言語の人間向けドキュメント、3ステップでセットアップ |
| **README 運営化** | バッジ + 言語切替 + Quick Start 優先配置 + ドキュメントサイトリンク |

---

## 背景

Meridian は [Scriptorium](https://github.com/lordmos/tech-editorial)（マルチ Agent 技術書執筆フレームワーク）の運営作業から抽出されました。その作業には以下が含まれます：

1. プロジェクト名の命名（Scriptorium）
2. 全ドキュメントの4言語翻訳（25個の Markdown ファイル × 4言語）
3. VitePress ドキュメントサイト + GitHub Pages 自動デプロイの構築
4. グラデーション発光 SVG ロゴの制作
5. Claude Code / OpenCode / Amp / Cursor / Windsurf 向け AI ツールコンテキストファイルの作成
6. `QUICK_START.md` の作成：「1文で起動、AI が全プロセスを実行」の AI オーケストレーション基盤
7. README の整備（バッジ、言語切替、Quick Start 優先配置、ドキュメントサイトリンク）

---

## ファイル一覧

| ファイル | 説明 |
|----------|------|
| `PROMPT.md` | 再利用可能な運営プロンプト（主要成果物、10項目のタスクを含む） |
| `QUICK_START.md` | AI オーケストレーションエントリポイント、AI アシスタント向け |
| `templates/` | プロンプトで参照するテンプレートファイル（VitePress 設定、GitHub Actions、ロゴ SVG、AI ツールファイル等） |

---

<sub>Built with [Meridian](https://github.com/lordmos/meridian) · open-source ops toolkit for Agent projects</sub>
