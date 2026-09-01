$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
python "$Root\script\build.py"
& "$Root\build\preview\.venv\Scripts\mkdocs.exe" serve -f "$Root\script\mkdocs.yml" -a 127.0.0.1:8000
