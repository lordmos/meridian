#!/usr/bin/env python3
"""Screenshot each Meridian style via real VitePress dev server + headless Chromium.

For each style in STYLES:
  1. Copy its vitepress-theme.css  -> templates/styles/_demo/.vitepress/theme/style.css
  2. Copy its preview.svg          -> templates/styles/_demo/public/hero.svg
  3. Start vitepress dev server    (background process)
  4. Wait for server ready
  5. Playwright: open http://localhost:<port>/, screenshot home page
  6. Save PNG                      -> templates/styles/<id>/screenshot.png
  7. Kill dev server, next style

Requires:
  - npm + node (nvm) + vitepress installed in templates/styles/_demo/
    (run `cd templates/styles/_demo && npm install` once before this script)
  - Python playwright + chromium: `pip install playwright && playwright install chromium`

Usage:
  python3 scripts/screenshot-styles.py              # all 4 styles
  python3 scripts/screenshot-styles.py glow         # single style
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
VIEWPORT = {"width": 1440, "height": 900}
SCREENSHOT_CLIP = {"x": 0, "y": 0, "width": 1440, "height": 900}

STYLES = ["glow", "minimalist", "dev-native", "enterprise"]


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


def screenshot_style(style_id: str) -> None:
    print(f"\n--- {style_id} ---")
    style_dir = STYLES_DIR / style_id
    if not style_dir.is_dir():
        raise SystemExit(f"unknown style: {style_id}")

    # 1. Swap theme css
    shutil.copy(style_dir / "vitepress-theme.css", DEMO / ".vitepress" / "theme" / "style.css")
    # 2. Swap hero.svg (M-substituted preview)
    shutil.copy(style_dir / "preview.svg", DEMO / "public" / "hero.svg")

    port = find_free_port()
    # 3. Spawn dev server
    env = {**os.environ}
    proc = subprocess.Popen(
        ["npx", "vitepress", "dev", "--port", str(port), "--host", "127.0.0.1"],
        cwd=str(DEMO),
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        url = f"http://127.0.0.1:{port}/"
        wait_for_server(url, timeout_s=45.0)
        # Small grace period for CSS/font loading
        time.sleep(2.0)

        # 4-5. Playwright screenshot
        from playwright.sync_api import sync_playwright
        out_png = style_dir / "screenshot.png"
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport=VIEWPORT, device_scale_factor=2)
            page.goto(url, wait_until="networkidle")
            # Extra wait for font swap
            page.wait_for_timeout(1000)
            page.screenshot(path=str(out_png), clip=SCREENSHOT_CLIP)
            browser.close()
        print(f"  saved: {out_png.relative_to(ROOT)} ({out_png.stat().st_size // 1024} KB)")
    finally:
        # 6. Kill dev server
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


def main() -> None:
    targets = sys.argv[1:] or STYLES
    for style_id in targets:
        screenshot_style(style_id)


if __name__ == "__main__":
    main()
