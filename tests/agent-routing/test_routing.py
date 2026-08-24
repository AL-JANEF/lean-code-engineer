#!/usr/bin/env python3

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from route_context import route  # noqa: E402


class RoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads(
            (ROOT / "tests" / "fixtures" / "routes.json").read_text(encoding="utf-8")
        )

    def test_expected_routes(self):
        for case in self.cases:
            with self.subTest(case=case["name"]):
                actual = route(case["prompt"])
                self.assertEqual(actual["references"], case["expected_references"])
                self.assertEqual(actual["modules"], case["expected_modules"])

    def test_router_caps_loaded_context(self):
        noisy = route(
            "Fix and verify a security auth regression in a large repo, then delegate it."
        )
        self.assertLessEqual(len(noisy["references"]), 2)
        self.assertLessEqual(len(noisy["modules"]), 1)

    def test_all_routes_exist(self):
        for case in self.cases:
            actual = route(case["prompt"])
            for relative in actual["references"] + actual["modules"]:
                with self.subTest(path=relative):
                    self.assertTrue((ROOT / relative).is_file())


if __name__ == "__main__":
    unittest.main()
