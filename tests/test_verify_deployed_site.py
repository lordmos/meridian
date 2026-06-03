import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "verify-deployed-site.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verify_deployed_site", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class FakeResponse:
    def __init__(self, body: str, status: int = 200, content_type: str = "text/html"):
        self.body = body.encode("utf-8")
        self.status = status
        self.headers = {"content-type": content_type}

    def read(self):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class VerifyDeployedSiteTests(unittest.TestCase):
    def test_template_script_matches_project_script(self):
        template = ROOT / "templates" / "scripts" / "verify-deployed-site.py"

        self.assertEqual(SCRIPT.read_text(encoding="utf-8"), template.read_text(encoding="utf-8"))

    def test_join_url_keeps_github_pages_base_path(self):
        module = load_module()

        self.assertEqual(
            module.join_url("https://example.github.io/project/", "robots.txt"),
            "https://example.github.io/project/robots.txt",
        )
        self.assertEqual(
            module.join_url("https://example.github.io/project", "/en/"),
            "https://example.github.io/project/en/",
        )

    def test_verifier_checks_core_pages_assets_and_metadata(self):
        module = load_module()
        calls = []
        html = """
        <html>
          <head>
            <meta property="og:title" content="Example">
            <meta name="twitter:card" content="summary_large_image">
            <link rel="canonical" href="https://example.github.io/project/">
            <link rel="alternate" title="llms.txt" href="/project/llms.txt">
            <script type="application/ld+json">{}</script>
          </head>
          <body>Example</body>
        </html>
        """
        bodies = {
            "/project/": html,
            "/project/quick-start.html": "<html>Quick Start</html>",
            "/project/faq.html": "<html>FAQ</html>",
            "/project/en/": "<html>English</html>",
            "/project/ja/": "<html>Japanese</html>",
            "/project/zh-TW/": "<html>Traditional Chinese</html>",
            "/project/robots.txt": "User-agent: *\nSitemap: https://example.github.io/project/sitemap.xml",
            "/project/sitemap.xml": "<urlset><loc>https://example.github.io/project/</loc></urlset>",
            "/project/llms.txt": "# Example\n",
            "/project/llms-full.txt": "# Full\n" + ("content\n" * 80),
            "/project/og.png": "PNG",
        }

        def fetcher(url, timeout=10):
            calls.append(url)
            path = "/" + url.split("github.io/", 1)[1]
            content_type = "image/png" if path.endswith(".png") else "text/html"
            return FakeResponse(bodies[path], content_type=content_type)

        fail = module.Fail()
        verifier = module.DeployedSiteVerifier("https://example.github.io/project/", fetcher=fetcher)
        verifier.run(fail)

        self.assertEqual(fail.errors, [])
        self.assertIn("https://example.github.io/project/robots.txt", calls)
        self.assertIn("https://example.github.io/project/en/", calls)

    def test_verifier_reports_missing_metadata_and_placeholders(self):
        module = load_module()

        def fetcher(url, timeout=10):
            if url.endswith("og.png"):
                return FakeResponse("PNG", content_type="image/png")
            return FakeResponse("<html>{{PROJECT_NAME}}</html>")

        fail = module.Fail()
        verifier = module.DeployedSiteVerifier("https://example.github.io/project/", fetcher=fetcher)
        verifier.run(fail)

        self.assertTrue(any("missing og:title" in error for error in fail.errors), fail.errors)
        self.assertTrue(any("unreplaced template placeholder" in error for error in fail.errors), fail.errors)

    def test_verifier_reports_http_errors(self):
        module = load_module()

        def fetcher(url, timeout=10):
            return FakeResponse("not found", status=404)

        fail = module.Fail()
        verifier = module.DeployedSiteVerifier("https://example.github.io/project/", fetcher=fetcher)
        verifier.run(fail)

        self.assertTrue(any("HTTP 404" in error for error in fail.errors), fail.errors)


if __name__ == "__main__":
    unittest.main()
