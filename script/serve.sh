#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$ROOT/script/build.py"
exec "$ROOT/build/preview/.venv/bin/mkdocs" serve -f "$ROOT/script/mkdocs.yml" -a 127.0.0.1:8000
