#!/usr/bin/env bash
# Builds the throwaway demo repo for the Claude Code review video. Touches nothing outside $1.
# Usage: ./setup_demo.sh /tmp/cc-review-demo
set -euo pipefail
DEST="${1:?usage: setup_demo.sh <empty throwaway dir>}"
SRC="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DEST" && cd "$DEST"
[ -z "$(ls -A .)" ] || { echo "refusing: $DEST is not empty"; exit 1; }
git init -q --bare origin.git
git init -q -b main work && cd work
git config user.name "demo"; git config user.email "demo@example.invalid"
cp -R "$SRC/base/." .
git add -A && git commit -qm "Invoice service: list + customer lookup"
git remote add origin ../origin.git
git push -q -u origin main
git remote set-head origin main          # /security-review needs origin/HEAD
git switch -q -c add-customer-search
cp -R "$SRC/feature/." .
git add -A && git commit -qm "Add customer search and fix paging"
echo "Ready: cd $DEST/work  (branch add-customer-search, 1 commit ahead of origin/main)"
python3 -m unittest -q 2>&1 | tail -2 || true
