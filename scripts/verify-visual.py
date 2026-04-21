#!/usr/bin/env python3
# Meridian · visual regression smoke test
"""Local smoke test: boot VitePress dev, screenshot key pages, assert
critical visual contract holds.

Catches the class of bugs we just shipped three times in a row:
  - features icon rendering as plain text URL (VitePress YAML pitfall)
  - /{{REPO_NAME}}/ double-prefix → 404 → broken image
  - Hero text stuck on stale copy
  - Alt buttons (FAQ / GitHub) invisible against dark background
  - Light/dark mode toggle leaving one mode unstyled

Runs against the target project's `docs/` directory. Meant to be copied
into each target project that Meridian operates on (task 10 收尾 step
is a good place to invoke it before declaring the task pipeline done).

Usage:
  python3 scripts/verify-visual.py                      # all checks, exit 1 on fail
  python3 scripts/verify-visual.py --output /tmp/viz/   # save screenshots there
  python3 scripts/verify-visual.py --open               # open screenshots when done

Requires: playwright + chromium (pip install playwright && playwright install chromium)
and the `docs/` subproject to have `npm install` completed.
"""

from __future__ import annotations

import argparse
import os
import re
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BASE_PATH = "/meridian/"  # VitePress base; read from config in a future version


def find_free_port() -> int:
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def wait_for_server(url: str, timeout_s: float = 45.0) -> None:
    import urllib.request
    start = time.monotonic()
    while time.monotonic() - start < timeout_s:
        try:
            with urllib.request.urlopen(url, timeout=1) as r:
                if r.status == 200:
                    return
        except Exception:
            pass
        time.sleep(0.5)
    raise RuntimeError(f"timeout waiting for {url}")


class Fail:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def add(self, msg: str) -> None:
        self.errors.append(msg)

    def report(self) -> int:
        if not self.errors:
            print("\n\x1b[32m[PASS]\x1b[0m no visual regressions detected")
            return 0
        print(f"\n\x1b[31m[FAIL]\x1b[0m {len(self.errors)} issue(s):")
        for e in self.errors:
            print(f"  - {e}")
        return 1


def check_home(page: Any, url: str, fail: Fail, out_dir: Path, mode: str = "dark") -> None:
    """Assert the home page renders features as images, not text URLs.

    `mode` ∈ {'light', 'dark'} — screenshots are saved per mode so you
    can eyeball both. Mode is toggled via `html.classList` (VitePress
    uses a `.dark` class on <html>)."""
    print(f"  checking: {url}  [{mode}]")
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(1500)
    if mode == "light":
        page.evaluate("document.documentElement.classList.remove('dark')")
    else:
        page.evaluate("document.documentElement.classList.add('dark')")
    page.wait_for_timeout(500)
    page.screenshot(path=str(out_dir / f"home-{mode}.png"),
                    clip={"x": 0, "y": 0, "width": 1440, "height": 900})

    # 1) features must render as <img>, not literal text URL.
    # VitePress with `icon: { src }` renders `<img class="VPImage">` directly
    # inside `.VPFeature > .box` — NOT in a `.icon` wrapper. Be selector-safe.
    feat_cards = page.locator(".VPFeature").count()
    feat_imgs = page.locator(".VPFeature img").count()
    if feat_cards == 0:
        fail.add("no .VPFeature cards found — features block did not render")
    elif feat_imgs != feat_cards:
        fail.add(
            f"feature icon count mismatch: {feat_cards} cards but {feat_imgs} <img> — "
            "likely rendering icon as text URL (use `icon: {{ src: ... }}` object form)"
        )

    # 2) every feature icon <img> must load, and its color must track the
    # brand variable. SVGs loaded as <img> don't honor currentColor — we
    # render them as CSS masks filled with background-color: var(--vp-c-brand-1).
    # Assert: mask-image is set AND background-color resolves to the brand color.
    brand = page.evaluate(
        "getComputedStyle(document.documentElement).getPropertyValue('--vp-c-brand-1').trim()"
    )
    imgs = page.locator(".VPFeature img").all()
    for i, img in enumerate(imgs):
        info = img.evaluate("""el => {
            const s = getComputedStyle(el);
            return {
                natural: el.naturalWidth,
                src:     el.getAttribute('src'),
                mask:    s.maskImage || s.webkitMaskImage || 'none',
                bg:      s.backgroundColor,
            };
        }""")
        if info["natural"] == 0:
            fail.add(f"feature icon #{i} src={info['src']!r} failed to load (404 or broken)")
        if info["src"] and info["src"].count("meridian/") > 1:
            fail.add(f"feature icon #{i} has double base prefix: {info['src']!r}")
        if info["mask"] == "none":
            fail.add(
                f"feature icon #{i} [{mode}] has no mask-image — SVG will render "
                f"as raw black stroke. Check .VPFeature img.VPImage[src$=...] rules."
            )
        # background-color must be a visible color, not transparent/black fallback
        bg = info["bg"]
        if bg in ("rgba(0, 0, 0, 0)", "transparent", "rgb(0, 0, 0)"):
            fail.add(
                f"feature icon #{i} [{mode}] background-color={bg} — icon would "
                f"render invisible through the mask. Expected brand color."
            )

    # 3) hero text should not contain stale v3.1 scope-lock copy
    hero_text = page.locator(".VPHero .text").inner_text()
    if "Agent 项目" in hero_text or "Agent Project" in hero_text:
        fail.add(
            f"hero text still contains stale 'Agent 项目' scope: {hero_text!r}"
        )

    # 4) alt buttons (FAQ / GitHub) must be visible.
    # A button is visible if EITHER its bg opacity is ≥ 0.18 OR its border
    # is clearly delineated (border width ≥ 1px with alpha ≥ 0.3). Light
    # mode uses subtle bg + strong border; dark mode uses stronger bg.
    alt_buttons = page.locator(".VPButton.alt").all()
    for i, btn in enumerate(alt_buttons):
        label = btn.inner_text().strip()
        vis = btn.evaluate(
            """el => {
              const s = getComputedStyle(el);
              const bg = s.backgroundColor;
              const bd = s.borderColor;
              const bw = parseFloat(s.borderTopWidth) || 0;
              const parse = (c) => {
                const m = c.match(/rgba?\\(([^)]+)\\)/);
                if (!m) return 1.0;
                const parts = m[1].split(',').map(x => x.trim());
                return parts.length >= 4 ? parseFloat(parts[3]) : 1.0;
              };
              return { bgAlpha: parse(bg), borderAlpha: parse(bd), borderWidth: bw };
            }"""
        )
        bg_ok = vis["bgAlpha"] >= 0.18
        border_ok = vis["borderWidth"] >= 1 and vis["borderAlpha"] >= 0.3
        if not (bg_ok or border_ok):
            fail.add(
                f"alt button {label!r} [{mode}] fails visibility — "
                f"bg_alpha={vis['bgAlpha']:.2f}, border_alpha={vis['borderAlpha']:.2f}, "
                f"border_width={vis['borderWidth']}px. Need ≥ 0.18 bg OR "
                f"(≥ 1px border ∧ ≥ 0.3 border alpha)."
            )


def check_sitemap_and_meta(dist: Path, fail: Fail) -> None:
    """Smoke-check the static build output."""
    idx = dist / "index.html"
    if not idx.exists():
        fail.add(f"missing {idx}")
        return
    html = idx.read_text()

    required = [
        ("og:title",          r'og:title'),
        ("twitter:card",      r'twitter:card'),
        ("canonical",         r'rel="canonical"'),
        ("JSON-LD",           r'application/ld\+json'),
        ("llms.txt rel",      r'title="llms\.txt"'),
    ]
    for name, pat in required:
        if not re.search(pat, html):
            fail.add(f"index.html missing {name} ({pat!r})")

    for static in ("robots.txt", "sitemap.xml", "og.png", "llms.txt", "llms-full.txt"):
        if not (dist / static).exists():
            fail.add(f"dist missing static asset: {static}")


def run() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None, help="screenshot output dir (default: /tmp/meridian-viz)")
    ap.add_argument("--open", action="store_true", help="open screenshots when done")
    ap.add_argument("--skip-dev", action="store_true", help="skip dev-server checks (build-only)")
    args = ap.parse_args()

    out_dir = Path(args.output or "/tmp/meridian-viz")
    out_dir.mkdir(parents=True, exist_ok=True)

    fail = Fail()

    # Step 1: build + inspect static output
    print("→ running `npm run docs:build` …")
    r = subprocess.run(
        ["npm", "run", "docs:build"], cwd=str(DOCS),
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        fail.add(f"build failed:\n{r.stderr[-800:]}")
        return fail.report()
    dist = DOCS / ".vitepress" / "dist"
    check_sitemap_and_meta(dist, fail)

    # Step 2: dev server + playwright checks
    if not args.skip_dev:
        port = find_free_port()
        print(f"→ spawning `vitepress dev --port {port}` …")
        proc = subprocess.Popen(
            ["npx", "vitepress", "dev", "--port", str(port), "--host", "127.0.0.1"],
            cwd=str(DOCS),
            env={**os.environ},
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            url = f"http://127.0.0.1:{port}{BASE_PATH}"
            wait_for_server(url)
            time.sleep(1.5)
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page(
                    viewport={"width": 1440, "height": 900},
                    device_scale_factor=2,
                )
                # Check both modes — catches single-mode styling bugs
                check_home(page, url, fail, out_dir, mode="light")
                check_home(page, url, fail, out_dir, mode="dark")
                browser.close()
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()

    print(f"\nscreenshots saved to: {out_dir}")
    if args.open:
        subprocess.run(["open", str(out_dir / "home.png")], check=False)
    return fail.report()


if __name__ == "__main__":
    sys.exit(run())
