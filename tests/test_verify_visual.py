import importlib.util
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "verify-visual.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verify_visual", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class VerifyVisualTests(unittest.TestCase):
    def test_reads_vitepress_base_from_config(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp) / "docs"
            config = docs / ".vitepress" / "config.mts"
            config.parent.mkdir(parents=True)
            config.write_text(
                textwrap.dedent(
                    """
                    export default defineConfig({
                      title: 'Example Project',
                      base: '/example-project/',
                    })
                    """
                ),
                encoding="utf-8",
            )

            self.assertEqual(module.read_base_path(docs), "/example-project/")

    def test_builds_dev_url_with_dynamic_base(self):
        module = load_module()

        self.assertEqual(
            module.build_dev_url(5173, "/example-project/"),
            "http://127.0.0.1:5173/example-project/",
        )

    def test_reports_missing_playwright_before_spawning_dev_server(self):
        module = load_module()

        with patch("importlib.util.find_spec", return_value=None):
            message = module.playwright_dependency_error()

        self.assertIn("python3 -m pip install playwright", message)
        self.assertIn("python3 -m playwright install chromium", message)

    def test_static_dist_checks_catch_docs_nav_and_feature_regressions(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "dist"
            assets = dist / "assets"
            assets.mkdir(parents=True)
            for name in ("robots.txt", "sitemap.xml", "og.png", "llms.txt", "llms-full.txt"):
                (dist / name).write_text("", encoding="utf-8")
            dist.joinpath("index.html").write_text(
                textwrap.dedent(
                    """
                    <html>
                      <head>
                        <meta property="og:title" content="Example">
                        <meta name="twitter:card" content="summary_large_image">
                        <link rel="canonical" href="https://example.test/">
                        <link rel="alternate" title="llms.txt" href="/llms.txt">
                        <script type="application/ld+json">{}</script>
                      </head>
                      <body>
                        <section class="VPFeature"></section>
                        <section class="VPFeature"></section>
                        <section class="VPFeature"></section>
                        <section class="VPFeature"></section>
                        <section class="VPFeature"></section>
                      </body>
                    </html>
                    """
                ),
                encoding="utf-8",
            )
            assets.joinpath("style.css").write_text(
                ".VPNavBarTranslations{}"
                ".VPNavBarAppearance .VPSwitchAppearance{}"
                ".VPNavBarAppearance .VPSwitchAppearance .check{}"
                ".VPNavBarAppearance .VPSwitchAppearance .icon{}"
                ".VPNavBarSocialLinks{}"
                ".VPHomeFeatures{}"
                ".VPHome .vp-doc.container{}",
                encoding="utf-8",
            )

            fail = module.Fail()
            module.check_sitemap_and_meta(dist, fail)

        self.assertTrue(
            any("4 feature cards" in error for error in fail.errors),
            fail.errors,
        )
        self.assertTrue(
            any('VPSwitchAppearance[aria-checked="true"] .check' in error for error in fail.errors),
            fail.errors,
        )
        self.assertTrue(
            any('[class^="vpi-social-"]' in error for error in fail.errors),
            fail.errors,
        )

    def test_enterprise_theme_contains_docs_nav_regression_fixes(self):
        css = (ROOT / "templates" / "styles" / "enterprise" / "vitepress-theme.css").read_text(
            encoding="utf-8"
        )

        self.assertIn('.VPNavBarAppearance .VPSwitchAppearance[aria-checked="true"] .check', css)
        self.assertIn('.VPNavBar .VPSocialLink [class^="vpi-social-"]', css)
        self.assertIn("--vp-c-bg:", css)
        self.assertIn(".dark .VPHero", css)
        self.assertIn(".dark .VPFeature", css)
        self.assertIn(".dark .VPButton.alt", css)
        self.assertIn(".VPHomeFeatures", css)


if __name__ == "__main__":
    unittest.main()
