#!/usr/bin/env python3
"""Measure structural context cost without external tokenizer dependencies."""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from route_context import load_config, route  # noqa: E402


def estimate_tokens(paths: Iterable[Path]) -> int:
    characters = sum(len(path.read_text(encoding="utf-8")) for path in paths)
    return math.ceil(characters / 4)


def instruction_files() -> List[Path]:
    files = [ROOT / "SKILL.md"]
    for directory in (ROOT / "references", ROOT / "modules"):
        files.extend(sorted(directory.rglob("*.md")))
    return files


def load_cases() -> List[Dict[str, Any]]:
    path = ROOT / "tests" / "fixtures" / "routes.json"
    return json.loads(path.read_text(encoding="utf-8"))


def build_report() -> Dict[str, Any]:
    cfg = load_config()
    core_path = ROOT / "SKILL.md"
    full_paths = instruction_files()
    core = estimate_tokens([core_path])
    full = estimate_tokens(full_paths)
    cases = []

    for case in load_cases():
        selected = route(case["prompt"], cfg)
        routed_paths = [core_path]
        if selected["modules"]:
            routed_paths.append(ROOT / "modules" / "README.md")
        routed_paths.extend(ROOT / item for item in selected["references"])
        routed_paths.extend(ROOT / item for item in selected["modules"])
        routed = estimate_tokens(dict.fromkeys(routed_paths))
        savings = 1 - (routed / full)
        cases.append(
            {
                "name": case["name"],
                "estimated_tokens": routed,
                "estimated_savings": round(savings, 4),
                "references": selected["references"],
                "modules": selected["modules"],
            }
        )

    median_savings = statistics.median(
        item["estimated_savings"] for item in cases
    )
    return {
        "method": "ceil(UTF-8 text characters / 4)",
        "core_estimated_tokens": core,
        "full_estimated_tokens": full,
        "median_route_savings": round(median_savings, 4),
        "budget": cfg["budgets"],
        "routes": cases,
    }


def check_report(report: Dict[str, Any]) -> List[str]:
    errors = []
    budget = report["budget"]
    if report["core_estimated_tokens"] > budget["core_estimated_tokens"]:
        errors.append(
            f"core estimate {report['core_estimated_tokens']} exceeds "
            f"budget {budget['core_estimated_tokens']}"
        )
    if report["median_route_savings"] < budget["minimum_median_route_savings"]:
        errors.append(
            f"median route savings {report['median_route_savings']:.1%} is below "
            f"minimum {budget['minimum_median_route_savings']:.1%}"
        )
    return errors


def _print_text(report: Dict[str, Any]) -> None:
    print("LeanCode Engineer context benchmark")
    print(f"Method: {report['method']}")
    print(f"Core: {report['core_estimated_tokens']} estimated tokens")
    print(f"Full eager load: {report['full_estimated_tokens']} estimated tokens")
    print(f"Median route savings: {report['median_route_savings']:.1%}")
    print("Routes:")
    for item in report["routes"]:
        print(
            f"  - {item['name']}: {item['estimated_tokens']} tokens, "
            f"{item['estimated_savings']:.1%} savings"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--check", action="store_true", help="Enforce configured gates")
    args = parser.parse_args()

    report = build_report()
    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        _print_text(report)

    if args.check:
        errors = check_report(report)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print("Benchmark gates: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
