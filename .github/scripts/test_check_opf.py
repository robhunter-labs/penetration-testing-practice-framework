#!/usr/bin/env python3
"""Planted-marker tests for check_opf.py.

Run: python3 .github/scripts/test_check_opf.py   (or: python3 -m unittest discover -s .github/scripts)
Each test copies the repo to a temp folder and scans it, so the suite takes ~10-30 s.
Every planted term here is made up; no real private term appears in this file.
"""
import os, shutil, sys, tempfile, unittest, zipfile
from unittest import mock

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import check_opf  # noqa: E402

FAKE_TERM = "zebra-" + "quokka-7731"  # synthetic stand-in; split so this file never matches itself


class PlantedMarker(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = os.path.join(self.tmp, "repo")
        shutil.copytree(REPO, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.terms = os.path.join(self.tmp, "terms.txt")  # outside the scanned root
        with open(self.terms, "w", encoding="utf-8") as fh:
            fh.write("# synthetic private list\n" + FAKE_TERM + "\n")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def plant(self, rel, text):
        p = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(text)
        return p

    def scan(self, **env):
        with mock.patch.dict(os.environ, env, clear=False):
            return check_opf.scan(self.root)

    def test_clean_tree_passes(self):
        bad, links, _ = self.scan(OPF_PRIVATE_TERMS=self.terms)
        self.assertEqual(bad, [])
        self.assertGreater(links, 0)

    def test_private_term_caught_any_case(self):
        self.plant("components/planted.md", f"see {FAKE_TERM.upper()} notes\n")
        bad, _, _ = self.scan(OPF_PRIVATE_TERMS=self.terms)
        self.assertIn("private term: components/planted.md:1", bad)

    def test_private_term_in_path_caught(self):
        self.plant(f"examples/{FAKE_TERM}/x.md", "plain\n")
        bad, _, _ = self.scan(OPF_PRIVATE_TERMS=self.terms)
        self.assertTrue(any(b.startswith("private term in path:") for b in bad), bad)

    def test_term_list_inside_repo_refused(self):
        inside = self.plant("terms.txt", FAKE_TERM + "\n")
        with self.assertRaises(SystemExit):
            self.scan(OPF_PRIVATE_TERMS=inside)

    def test_public_marker_caught(self):
        self.plant("components/plain.md", "Remove before " + "public release\n")
        bad, _, _ = self.scan()
        self.assertIn("local-only marker: components/plain.md:1", bad)

    def test_marker_wrapped_across_lines_caught(self):
        self.plant("components/wrap.md", "Remove before\npublic release\n")
        bad, _, _ = self.scan()
        self.assertIn("marker split across lines or text runs: components/wrap.md", bad)

    def test_marker_split_across_pptx_runs_caught(self):
        p = os.path.join(self.root, "downloads", "split.pptx")
        with zipfile.ZipFile(p, "w") as z:
            z.writestr("ppt/slides/slide1.xml",
                       "<p:sld><a:r><a:t>Remove before </a:t></a:r><a:r><a:t>public release</a:t></a:r></p:sld>")
        bad, _, _ = self.scan()
        self.assertTrue(any("downloads/split.pptx" in b for b in bad), bad)

    def test_pycache_is_ignored(self):
        self.plant(".github/scripts/__pycache__/x.cpython-311.pyc", "x")
        bad, _, _ = self.scan()
        self.assertEqual(bad, [])

    def test_missing_pdftotext_warns_not_crashes(self):
        with mock.patch.object(check_opf.shutil, "which", return_value=None):
            bad, _, warn = self.scan()
            self.assertEqual(bad, [])
            self.assertTrue(any("unscanned PDF" in w for w in warn), warn)
            strict_bad, _, _ = check_opf.scan(self.root, strict=True)
            self.assertTrue(any("unscanned PDF" in b for b in strict_bad), strict_bad)

    def test_unreadable_file_type_fails(self):
        with open(os.path.join(self.root, "downloads", "blob.bin"), "wb") as fh:
            fh.write(b"\xff\xfe\x00\x81")
        bad, _, _ = self.scan()
        self.assertIn("unscanned file type: downloads/blob.bin", bad)

    def test_profile_holds_no_hashed_or_private_terms(self):
        with open(os.path.join(REPO, check_opf.PROFILE), encoding="utf-8") as fh:
            raw = fh.read()
        self.assertNotRegex(raw, r"sha256:\d*:?[0-9a-f]{64}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
