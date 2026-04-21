#!/usr/bin/env python3
# Meridian · OG image generator (1200×630 per style)
"""Generate Open Graph social cards for each Meridian style preset.

For each style:
  1. Reuse templates/styles/_demo/ VitePress project
  2. Swap per-style theme css + hero.svg
  3. Launch vitepress dev
  4. Playwright with 1200×630 viewport (the OG social-card canonical size)
  5. Screenshot the hero region only (crop so social thumbnails look right)
  6. Save PNG to templates/styles/<id>/og.png
  7. Also copy the default (Glow) to docs/public/og.png for the main Meridian site

Usage:
  python3 scripts/generate-og-images.py              # all 4 styles
  python3 scripts/generate-og-images.py glow         # single style

Requires the same deps as scripts/screenshot-styles.py
(playwright + chromium + templates/styles/_demo/node_modules).
"""

from __future__ import annotations

import os
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEMO = ROOT / "templates" / "styles" / "_demo"
STYLES_DIR = ROOT / "templates" / "styles"
VIEWPORT = {"width": 1200, "height": 630}
# OG cards are recommended 1200×630; capture the full viewport
CLIP = {"x": 0, "y": 0, "width": 1200, "height": 630}

STYLES = ["glow", "minimalist", "dev-native", "enterprise"]
# Default style → gets copied as the main Meridian site's og.png
DEFAULT_STYLE = "glow"


def find_free_port() -> int:
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def wait_for_server(url: str, timeout_s: float = 30.0) -> None:
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


def render_og(style_id: str) -> Path:
    print(f"\n--- {style_id} ---")
    style_dir = STYLES_DIR / style_id
    if not style_dir.is_dir():
        raise SystemExit(f"unknown style: {style_id}")

    shutil.copy(style_dir / "vitepress-theme.css", DEMO / ".vitepress" / "theme" / "style.css")
    shutil.copy(style_dir / "preview.svg", DEMO / "public" / "hero.svg")

    port = find_free_port()
    proc = subprocess.Popen(
        ["npx", "vitepress", "dev", "--port", str(port), "--host", "127.0.0.1"],
        cwd=str(DEMO),
        env={**os.environ},
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    out_png = style_dir / "og.png"
    try:
        url = f"http://127.0.0.1:{port}/"
        wait_for_server(url, timeout_s=45.0)
        time.sleep(2.0)

        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            # Use device_scale_factor=1 for OG (exact pixels, no retina upscale)
            page = browser.new_page(viewport=VIEWPORT, device_scale_factor=1)
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(1000)
            page.screenshot(path=str(out_png), clip=CLIP)
            browser.close()
        print(f"  saved: {out_png.relative_to(ROOT)} ({out_png.stat().st_size // 1024} KB)")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    return out_png


def main() -> None:
    targets = sys.argv[1:] or STYLES
    rendered = {}
    for style_id in targets:
        rendered[style_id] = render_og(style_id)

    # Also place the default style's OG image at docs/public/og.png
    # so it's served at {SITE_URL}/og.png (easy reference in meta tags).
    if DEFAULT_STYLE in rendered:
        docs_og = ROOT / "docs" / "public" / "og.png"
        docs_og.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(rendered[DEFAULT_STYLE], docs_og)
        print(f"\ncopied default ({DEFAULT_STYLE}) → {docs_og.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
