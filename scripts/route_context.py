#!/usr/bin/env python3
"""Suggest a small context route for tests, demos, and benchmark fixtures."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config" / "routing.json"


def load_config(path: Path = DEFAULT_CONFIG) -> Dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _normalize(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9_+-]+", value.lower()))


def _score(text: str, signals: Iterable[str]) -> int:
    normalized = _normalize(text)
    padded = f" {normalized} "
    score = 0
    for signal in signals:
        needle = _normalize(signal)
        if needle and f" {needle} " in padded:
            score += max(1, len(needle.split()))
    return score


def is_applicable(prompt: str, config: Optional[Dict[str, Any]] = None) -> bool:
    cfg = config or load_config()
    positive = _score(prompt, cfg["activation"]["positive"])
    negative = _score(prompt, cfg["activation"]["negative"])
    return positive > 0 and positive > negative


def _rank(prompt: str, entries: Iterable[Dict[str, Any]]) -> List[Tuple[int, int, str]]:
    ranked = []
    for entry in entries:
        score = _score(prompt, entry["signals"])
        if score:
            ranked.append((score, int(entry.get("priority", 0)), entry["path"]))
    return sorted(ranked, key=lambda item: (-item[0], -item[1], item[2]))


def route(
    prompt: str,
    config: Optional[Dict[str, Any]] = None,
    max_references: int = 2,
    max_modules: int = 1,
) -> Dict[str, Any]:
    cfg = config or load_config()
    references = [item[2] for item in _rank(prompt, cfg["references"])[:max_references]]
    modules = [item[2] for item in _rank(prompt, cfg["modules"])[:max_modules]]
    return {
        "applicable": is_applicable(prompt, cfg),
        "references": references,
        "modules": modules,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Suggest conditional LeanCode Engineer context for a prompt."
    )
    parser.add_argument("prompt", help="Software task to route")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    result = route(args.prompt)
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Applicable: {'yes' if result['applicable'] else 'no'}")
        print("References:")
        for path in result["references"] or ["(core only)"]:
            print(f"  - {path}")
        print("Modules:")
        for path in result["modules"] or ["(none)"]:
            print(f"  - {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
