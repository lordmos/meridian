# Post-Deploy Verification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a reusable GitHub Pages post-deploy verification workflow that checks the live site after deployment.

**Architecture:** Add a Python verifier that fetches the deployed base URL and key static/document pages, then wire it into the GitHub Pages workflow as a `verify` job after `deploy`. Keep a copy in `templates/scripts/` so Meridian-generated projects inherit the same checks.

**Tech Stack:** Python standard library, GitHub Actions, VitePress static output.

---

### Task 1: Add Post-Deploy Verifier

**Files:**
- Create: `scripts/verify-deployed-site.py`
- Create: `templates/scripts/verify-deployed-site.py`
- Test: `tests/test_verify_deployed_site.py`

- [x] Write unit tests for URL joining, required page/static checks, metadata checks, placeholder detection, and retryable fetch failures.
- [x] Implement the verifier with no third-party dependencies.
- [x] Run `python3 -m unittest tests.test_verify_deployed_site`.

### Task 2: Wire GitHub Actions

**Files:**
- Modify: `.github/workflows/docs.yml`
- Modify: `templates/docs-workflow.yml`
- Test: `tests/test_docs_workflow.py`

- [x] Write tests that assert `deploy` exposes `page_url` and `verify` depends on `deploy`.
- [x] Add a `verify` job that checks out the repo and runs `python3 scripts/verify-deployed-site.py "$&#123;&#123; needs.deploy.outputs.page_url &#125;&#125;"`.
- [x] Run `python3 -m unittest tests.test_docs_workflow`.

### Task 3: Update Meridian Instructions

**Files:**
- Modify: `PROMPT.md`
- Modify: `QUICK_START.md`

- [x] Document copying `templates/scripts/verify-deployed-site.py` into generated projects.
- [x] Mention the post-deploy workflow in the Pages task and troubleshooting notes.

### Task 4: Verify And Publish

- [x] Run `./scripts/verify.sh`.
- [ ] Commit and push to `main`.
- [ ] Watch GitHub Pages workflow until build, deploy, and verify jobs pass.
