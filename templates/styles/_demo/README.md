# Style demo VitePress project

Minimal VitePress site used **only** to screenshot each style preset for the
README gallery. Not deployed anywhere.

## Files that get swapped per screenshot run

- `.vitepress/theme/style.css` ← copied from `../<style-id>/vitepress-theme.css`
- `public/hero.svg`            ← copied from `../<style-id>/preview.svg`

Both files are committed to the repo (otherwise the demo won't build on a
fresh checkout), but their content at HEAD is arbitrary — currently
Minimalist as the alphabetical default. The [screenshot script](../../../scripts/screenshot-styles.py)
overwrites them before each render.

## Regenerate screenshots

```bash
cd templates/styles/_demo && npm install        # one-time
cd ../../..
python3 scripts/screenshot-styles.py            # all 4 styles
python3 scripts/screenshot-styles.py glow       # single style
```

Requires `playwright` Python package + Chromium installed:
```bash
pip install playwright && playwright install chromium
```

Outputs go to `templates/styles/<style-id>/screenshot.png`.
