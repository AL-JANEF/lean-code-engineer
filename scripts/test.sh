#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
project_root=$(dirname -- "$script_dir")
python3 "$project_root/tests/run.py"
