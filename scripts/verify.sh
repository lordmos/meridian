#!/usr/bin/env bash
set -euo pipefail

python3 -m unittest discover -s tests
python3 scripts/check-i18n-drift.py
(cd docs && npm run docs:build)
python3 scripts/verify-visual.py --skip-dev
