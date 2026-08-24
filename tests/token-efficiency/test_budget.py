#!/usr/bin/env python3

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from benchmark import build_report, check_report  # noqa: E402


class TokenBudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_configured_gates(self):
        self.assertEqual(check_report(self.report), [])

    def test_progressive_routes_are_smaller_than_eager_load(self):
        full = self.report["full_estimated_tokens"]
        for route in self.report["routes"]:
            with self.subTest(route=route["name"]):
                self.assertLess(route["estimated_tokens"], full)

    def test_core_is_the_smallest_context(self):
        core = self.report["core_estimated_tokens"]
        self.assertTrue(
            all(item["estimated_tokens"] >= core for item in self.report["routes"])
        )


if __name__ == "__main__":
    unittest.main()
