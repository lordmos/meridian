# llms.txt / llms-full.txt templates

[llms.txt](https://llmstxt.org) is an emerging standard (originated by Jeremy Howard, adopted by Anthropic and others) that gives LLMs a compact, curated entry point to a project's docs. Purpose: when Claude / ChatGPT / Perplexity etc. crawl your site to answer questions, they find a clean factual summary instead of scraping noisy HTML.

## Two files, different purposes

| file | location | for | contents |
|------|----------|-----|----------|
| `llms.txt` | repo root **and** `docs/public/llms.txt` | curation index | project intro + 1-line per key doc + FAQ |
| `llms-full.txt` | repo root **and** `docs/public/llms-full.txt` | full corpus | concatenated full text of all docs |

Both are plain text (Markdown OK), UTF-8.

## Generate `llms.txt`

1. Copy `llms.txt.template` to **both**:
   - `llms.txt` (repo root — for GitHub)
   - `docs/public/llms.txt` (for VitePress — served at `{{SITE_URL}}/llms.txt`)
2. Replace all `{{…}}` placeholders
3. Let the AI draft 5 FAQ entries based on the project's actual capabilities (not generic filler)

## Generate `llms-full.txt`

Run `scripts/generate-llms-full.py` (copied from Meridian `templates/llms-txt/generate-llms-full.py`):

```bash
python3 scripts/generate-llms-full.py
```

It walks `docs/**/*.md` (skipping `docs/.vitepress/`) + top-level `README.md`, strips frontmatter, concatenates with `---` separators, writes to both `llms-full.txt` and `docs/public/llms-full.txt`.

## Why both repo root AND docs/public?

- **Repo root** copy: so people viewing the GitHub repo see it in the file tree; also some crawlers only look at the root.
- **`docs/public/`** copy: VitePress serves it at the deployed URL (`{{SITE_URL}}/llms.txt`), which is the URL LLM crawlers look for first (per the llms.txt standard).

Keep both in sync — the generator script writes both.
