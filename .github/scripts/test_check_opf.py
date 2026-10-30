#!/usr/bin/env python3
"""Planted-marker tests for check_opf.py. Run: python3 .github/scripts/test_check_opf.py"""
import os, shutil, sys, tempfile, unittest
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import check_opf  # noqa: E402

# Planted terms are assembled at runtime so this file carries no plaintext marker.
def _term(*codes):
    return "".join(chr(c) for c in codes)


class PlantedMarker(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = os.path.join(self.tmp, "repo")
        shutil.copytree(REPO, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def plant(self, rel, text):
        p = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(text)

    def test_clean_tree_passes(self):
        bad, links = check_opf.scan(self.root)
        self.assertEqual(bad, [])
        self.assertGreater(links, 0)

    def test_hashed_marker_caught_any_case(self):
        # A hashed local-only path marker, planted in mixed case mid-line.
        term = _term(68, 117, 110, 118, 97, 114, 105, 99, 75, 105, 110, 103, 100, 111, 109, 47)
        self.plant("components/planted.md", f"see ~/{term.upper()}notes for detail\n")
        bad, _ = check_opf.scan(self.root)
        self.assertTrue(any("local-only marker: components/planted.md:1" in b for b in bad), bad)

    def test_hashed_component_caught(self):
        comp = _term(68, 117, 110, 118, 97, 114, 105, 99, 75, 105, 110, 103, 100, 111, 109)
        self.plant(f"examples/{comp}/x.md", "plain\n")
        bad, _ = check_opf.scan(self.root)
        self.assertTrue(any(b.startswith("prohibited component:") for b in bad), bad)

    def test_legacy_name_caught_outside_migration(self):
        self.plant("components/legacy.md", "cite " + _term(79, 83, 80, 84) + "-0001 here\n")
        bad, _ = check_opf.scan(self.root)
        self.assertTrue(any("legacy name: components/legacy.md:1" in b for b in bad), bad)

    def test_plain_marker_caught(self):
        self.plant("components/plain.md", "Remove before " + "public release\n")
        bad, _ = check_opf.scan(self.root)
        self.assertTrue(any("local-only marker: components/plain.md:1" in b for b in bad), bad)

    def test_profile_has_no_plaintext_sensitive_terms(self):
        raw = open(os.path.join(REPO, check_opf.PROFILE), encoding="utf-8").read().casefold()
        for t in (_term(101, 109, 112, 108, 111, 121, 101, 114), _term(118, 97, 108, 101, 110, 99, 101)):
            self.assertNotIn(t, raw)


if __name__ == "__main__":
    unittest.main(verbosity=2)
