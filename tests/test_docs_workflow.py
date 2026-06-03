import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class DocsWorkflowTests(unittest.TestCase):
    def assert_workflow_has_post_deploy_verify(self, path: Path):
        text = path.read_text(encoding="utf-8")

        self.assertIn("outputs:", text)
        self.assertIn("page_url: ${{ steps.deployment.outputs.page_url }}", text)
        self.assertIn("verify:", text)
        self.assertIn("needs: deploy", text)
        self.assertIn("python3 scripts/verify-deployed-site.py", text)
        self.assertIn("${{ needs.deploy.outputs.page_url }}", text)

    def test_project_workflow_verifies_live_pages_after_deploy(self):
        self.assert_workflow_has_post_deploy_verify(ROOT / ".github" / "workflows" / "docs.yml")

    def test_template_workflow_verifies_live_pages_after_deploy(self):
        self.assert_workflow_has_post_deploy_verify(ROOT / "templates" / "docs-workflow.yml")


if __name__ == "__main__":
    unittest.main()
