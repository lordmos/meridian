# 任务 2：i18n 多语言化

目标语言：**简体中文（原版）/ English / 日本語 / 繁體中文**

## 文件结构

```
i18n/
  glossary.md   ← 术语表（五节：品牌/技术/章节标题/惯用语/繁简转换），翻译的唯一权威
  en/           ← 英文翻译（按 DOCS_TO_TRANSLATE 目录结构镜像）
  ja/           ← 日文翻译
  zh-TW/        ← 繁中翻译
README.en.md
README.ja.md
README.zh-TW.md
```

## Step 0 — 先建 glossary（最优先）

以 `templates/glossary.md` 为基础，在目标项目生成 `i18n/glossary.md`：

1. 复制模板到 `i18n/glossary.md`
2. 替换 `{{PROJECT_NAME}}` 为项目英文名
3. 扫描源文件（README、docs）中的**专有名词、技术术语、重复出现的章节标题**，补充 A/B/C 节
4. 不确定的译法**留空**，翻译过程中首次遇到再回填
5. 繁中分节（E 节）保持模板内容，除非项目领域有特殊术语需增补

**所有后续翻译必须先查表再翻**。

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

- **先查 `i18n/glossary.md`**；已收录术语必须使用收录译法，不得替换
- 翻译中首次遇到未收录术语，立即加入 glossary 对应分类后再继续
- `{{变量名}}` 占位符**不翻译**，保持原样
- 代码块、文件路径**不翻译**
- HTML 注释**不翻译**
- 日文翻译用自然的技术日语，不要机器翻译腔
- 繁中按以下三步：(1) 直译 / OpenCC 简→繁转换 → (2) 对照 glossary E 节替换台湾惯用语 → (3) 人工校对
- 语言切换链接中当前语言加粗，其余为普通链接
- 所有章节标题（H1/H2）必须走 glossary C 节译法，不得自创

## 一致性校验（翻译完跑）

复制 `templates/scripts/check-i18n-drift.py` 到目标项目的 `scripts/check-i18n-drift.py`，然后：

```bash
python3 scripts/check-i18n-drift.py                 # 对当前目录
python3 scripts/check-i18n-drift.py --strict        # 告警也失败（用于 CI）
python3 scripts/check-i18n-drift.py --quiet         # 不列每组文件清单
```

**六项检查**：

| # | 检查 | 严重级 |
|---|------|-------|
| 1 | 结构对齐（H1/H2 数量 + 层级序列）| 错误 |
| 2 | 翻译状态头（`<!-- Translation status ... -->`）| 错误 |
| 3 | 语言切换行（`> **语言 / Language**: ...`，current 加粗）| 告警 |
| 4 | Source commit 新鲜度（git log 对比记录 commit 与 HEAD）| 错误（base 有新 commit）/ 告警（commit 无效）|
| 5 | glossary C 节覆盖率 + 术语一致性 | 错误（译文与 glossary 不符）/ 告警（base H2 未收录）|
| 6 | 占位符残留（`{{VAR}}`）| 错误 |

**退出码**：`0` 干净 / `1` 有错误 / `2` 参数错误。`--strict` 模式下告警也算失败。

**VitePress 子目录特例**：`docs/` 下文件靠 VitePress 原生 locale 下拉切换语言，脚本自动跳过切换行检查。
