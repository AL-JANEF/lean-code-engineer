#!/usr/bin/env python3
"""Validate repository structure and low-cost skill invariants."""

from __future__ import annotations

import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".claude-plugin/plugin.json",
    "agents/openai.yaml",
    "config/routing.json",
    "references/engineering.md",
    "references/debugging.md",
    "references/security.md",
    "references/verification.md",
    "references/context-efficiency.md",
    "references/architecture.md",
    "references/agent-orchestration.md",
    "modules/README.md",
    "assets/logo.svg",
    "assets/icon.svg",
    "assets/social-preview.png",
)
EXECUTABLES = (
    "scripts/install.sh",
    "scripts/validate.sh",
    "scripts/test.sh",
    "scripts/benchmark.sh",
    "scripts/route_context.py",
    "scripts/validate.py",
    "scripts/benchmark.py",
)


def _frontmatter(text: str) -> Tuple[dict, str]:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    raw, body = text[4:].split("\n---\n", 1)
    data = {}
    for line in raw.splitlines():
        if line.startswith("  ") or not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data, body


def _markdown_links(path: Path) -> Iterable[Tuple[str, Path]]:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if clean:
            yield target, (path.parent / clean).resolve()


def validate() -> List[str]:
    errors: List[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        try:
            meta, body = _frontmatter(text)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            if meta.get("name") != "lean-code-engineer":
                errors.append("SKILL.md name must be lean-code-engineer")
            if len(meta.get("description", "")) < 80:
                errors.append("SKILL.md description is not discriminating enough")
            if len(meta.get("description", "")) > 1536:
                errors.append("SKILL.md description exceeds Claude Code listing limit")
            if meta.get("license") != "MIT":
                errors.append("SKILL.md license must be MIT")
            if not body.strip():
                errors.append("SKILL.md body is empty")

    for path in ROOT.rglob("*"):
        if path.is_symlink():
            errors.append(f"symlink not allowed in release: {path.relative_to(ROOT)}")
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".sh", ".json", ".yaml", ".yml"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            if re.search(r"\[(?:TODO|FIXME)\]|(?:TODO|FIXME):", text, re.IGNORECASE):
                errors.append(f"unfinished placeholder: {path.relative_to(ROOT)}")

    for markdown in ROOT.rglob("*.md"):
        for target, resolved in _markdown_links(markdown):
            if not resolved.exists():
                errors.append(
                    f"broken link in {markdown.relative_to(ROOT)}: {target}"
                )

    for relative in EXECUTABLES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing executable: {relative}")
        elif not path.stat().st_mode & 0o111:
            errors.append(f"script is not executable: {relative}")

    for relative in ("assets/icon.svg", "assets/logo.svg"):
        try:
            ET.parse(ROOT / relative)
        except (OSError, ET.ParseError) as exc:
            errors.append(f"invalid SVG {relative}: {exc}")

    preview = ROOT / "assets" / "social-preview.png"
    if preview.is_file():
        data = preview.read_bytes()[:24]
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append("assets/social-preview.png is not a valid PNG header")
        else:
            width, height = struct.unpack(">II", data[16:24])
            if (width, height) != (1280, 640):
                errors.append(
                    f"social preview must be 1280x640, got {width}x{height}"
                )

    try:
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        routing = json.loads((ROOT / "config" / "routing.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON: {exc}")
    else:
        if plugin.get("name") != "lean-code-engineer":
            errors.append("plugin name must be lean-code-engineer")
        if plugin.get("version") != "0.1.0":
            errors.append("plugin version must match the current release")
        for collection in ("references", "modules"):
            for item in routing.get(collection, []):
                if not (ROOT / item.get("path", "")).is_file():
                    errors.append(f"routing target missing: {item.get('path')}")
    return sorted(set(errors))


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Repository validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
