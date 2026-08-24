#!/usr/bin/env python3

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from route_context import is_applicable  # noqa: E402


class ActivationTests(unittest.TestCase):
    def test_route_fixtures_activate(self):
        cases = json.loads((ROOT / "tests" / "fixtures" / "routes.json").read_text())
        for case in cases:
            with self.subTest(case=case["name"]):
                self.assertEqual(is_applicable(case["prompt"]), case["applicable"])

    def test_non_software_requests_do_not_activate(self):
        prompts = (
            "Write a marketing email for a product launch.",
            "Create a travel itinerary for Kyoto.",
            "Translate this paragraph into French.",
            "Write a creative story about the sea.",
        )
        for prompt in prompts:
            with self.subTest(prompt=prompt):
                self.assertFalse(is_applicable(prompt))

    def test_description_names_use_and_boundary(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        description = skill.split("description:", 1)[1].splitlines()[0].lower()
        self.assertIn("software", description)
        self.assertIn("do not use", description)


if __name__ == "__main__":
    unittest.main()
