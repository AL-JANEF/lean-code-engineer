#!/usr/bin/env python3
"""Run tests from directories whose names mirror the documented test areas."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    tests = sorted((ROOT / "tests").glob("*/test_*.py"))
    if not tests:
        print("ERROR: no tests found", file=sys.stderr)
        return 1

    failures = []
    for test in tests:
        relative = test.relative_to(ROOT)
        print(f"==> {relative}", flush=True)
        result = subprocess.run([sys.executable, str(test)], cwd=ROOT, check=False)
        if result.returncode:
            failures.append(str(relative))

    if failures:
        print(f"FAILED: {', '.join(failures)}", file=sys.stderr)
        return 1
    print(f"All {len(tests)} test groups passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
