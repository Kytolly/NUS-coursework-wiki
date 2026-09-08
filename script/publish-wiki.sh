#!/usr/bin/env bash
set -euo pipefail
WIKI_URL="https://github.com/Kytolly/NUS-coursework-wiki.wiki.git"
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PAGE_DIR="$REPO_DIR/page"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
git init -b master "$TMP_DIR" >/dev/null
declare -A seen
while IFS= read -r f; do
  base="$(basename "$f")"
  if [[ -n "${seen[$base]:-}" ]]; then
    echo "duplicate Wiki page basename: $base" >&2
    exit 1
  fi
  seen[$base]=1
  cp "$f" "$TMP_DIR/$base"
done < <(find "$PAGE_DIR" -type f -name '*.md' | sort)

# copy image assets (page/assets/**) so images resolve in the Wiki repo
if [ -d "$PAGE_DIR/assets" ]; then
  cp -r "$PAGE_DIR/assets" "$TMP_DIR/assets"
  echo "copied assets/"
fi
cd "$TMP_DIR"
git add -A
git -c user.name="${GIT_AUTHOR_NAME:-your-name}" -c user.email="${GIT_AUTHOR_EMAIL:-you@example.com}" commit -m "publish wiki" >/dev/null
git remote add origin "$WIKI_URL"
git push -u origin master
echo "完成：$WIKI_URL"
