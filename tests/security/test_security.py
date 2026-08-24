#!/usr/bin/env python3

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class SecurityTests(unittest.TestCase):
    def test_installer_avoids_command_construction_hazards(self):
        installer = (ROOT / "scripts" / "install.sh").read_text(encoding="utf-8")
        forbidden = ("eval " + '"', "curl" + " | sh", "wget" + " | sh", "rm -" + "rf")
        for fragment in forbidden:
            with self.subTest(fragment=fragment):
                self.assertNotIn(fragment, installer)

    def test_no_secret_shaped_values(self):
        patterns = (
            re.compile("AKIA" + r"[0-9A-Z]{16}"),
            re.compile("ghp_" + r"[A-Za-z0-9]{30,}"),
            re.compile("sk-" + r"[A-Za-z0-9]{24,}"),
            re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        )
        allowed_suffixes = {".md", ".py", ".sh", ".json", ".yaml", ".yml", ".svg"}
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in allowed_suffixes:
                continue
            if path == Path(__file__).resolve():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for pattern in patterns:
                with self.subTest(path=path.relative_to(ROOT), pattern=pattern.pattern):
                    self.assertIsNone(pattern.search(text))

    def test_installer_refuses_overwrite_and_preserves_backup(self):
        installer = ROOT / "scripts" / "install.sh"
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "lean-code-engineer"
            first = subprocess.run(
                [str(installer), "--dest", str(destination)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            marker = destination / "user-marker.txt"
            marker.write_text("preserve me", encoding="utf-8")

            refused = subprocess.run(
                [str(installer), "--dest", str(destination)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(refused.returncode, 0)
            self.assertTrue(marker.is_file())

            forced = subprocess.run(
                [str(installer), "--dest", str(destination), "--force"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(forced.returncode, 0, forced.stderr)
            backups = list(Path(temporary).glob("lean-code-engineer.backup.*"))
            self.assertEqual(len(backups), 1)
            self.assertEqual((backups[0] / "user-marker.txt").read_text(), "preserve me")

    def test_unsafe_custom_destination_is_rejected(self):
        installer = ROOT / "scripts" / "install.sh"
        result = subprocess.run(
            [str(installer), "--dest", "/"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
