#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
project_root=$(dirname -- "$script_dir")

python3 "$script_dir/validate.py"

for script in "$script_dir"/*.sh; do
  sh -n "$script"
done

python3 -m py_compile "$script_dir"/*.py
printf '%s\n' "Shell and Python syntax: PASS"

if command -v git >/dev/null 2>&1 && git -C "$project_root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if git -C "$project_root" diff --check -- .; then
    printf '%s\n' "Git whitespace check: PASS"
  fi
fi
