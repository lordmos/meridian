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
                      title: 'Nudge',
                      base: '/nudge/',
                    })
                    """
                ),
                encoding="utf-8",
            )

            self.assertEqual(module.read_base_path(docs), "/nudge/")

    def test_builds_dev_url_with_dynamic_base(self):
        module = load_module()

        self.assertEqual(
            module.build_dev_url(5173, "/nudge/"),
            "http://127.0.0.1:5173/nudge/",
        )

    def test_reports_missing_playwright_before_spawning_dev_server(self):
        module = load_module()

        with patch("importlib.util.find_spec", return_value=None):
            message = module.playwright_dependency_error()

        self.assertIn("python3 -m pip install playwright", message)
        self.assertIn("python3 -m playwright install chromium", message)


if __name__ == "__main__":
    unittest.main()
