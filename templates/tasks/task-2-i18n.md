# 任务 2：i18n 多语言化

目标语言：**简体中文（原版）/ English / 日本語 / 繁體中文**

## 文件结构

```
i18n/
  en/       ← 英文翻译（按 DOCS_TO_TRANSLATE 目录结构镜像）
  ja/       ← 日文翻译
  zh-TW/    ← 繁中翻译
README.en.md
README.ja.md
README.zh-TW.md
```

## 每个译文文件头部

```markdown
<!--
  Translation status:
  Source file : 原文件路径
  Source commit: git commit hash（执行 `git rev-parse --short HEAD`）
  Translated  : 翻译日期（YYYY-MM-DD）
  Status      : up-to-date
-->

> **语言 / Language**: [简体中文](../../原文件) · **English** · [日本語](...) · [繁體中文](...)
```

## 翻译规则

- `{{变量名}}` 占位符**不翻译**，保持原样
- 代码块、文件路径**不翻译**
- HTML 注释**不翻译**
- 日文翻译用自然的技术日语，不要机器翻译腔
- 繁中可基于简中用 OpenCC 转换，再人工校对
- 语言切换链接中当前语言加粗，其余为普通链接
