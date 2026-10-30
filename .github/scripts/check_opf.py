#!/usr/bin/env python3
"""Open Practice Framework repo check.

Usage:
  python3 .github/scripts/check_opf.py [ROOT] [--strict]

Fails on:
  - a broken relative link in a Markdown file;
  - a prohibited path component or a public local-only marker listed in
    .github/REPOSITORY_PROFILE.json;
  - a file type the checker cannot read;
  - a term from an optional private list (see below).

Private terms are never stored in this repository, hashed or plain. To check
for them, keep a list OUTSIDE the tree and point the checker at it:
  OPF_PRIVATE_TERMS=/path/outside/repo/terms.txt python3 .github/scripts/check_opf.py .
One term per line; blank lines and lines starting with # are ignored. A term
matches case-insensitively anywhere in a file's text, including across line
wraps and across the text runs inside Office files.

PDF text needs `pdftotext` (poppler-utils). Without it, PDFs are reported as
unscanned: a warning by default, a failure with --strict.
"""
import html, os, re, shutil, subprocess, sys, zipfile

SELF = ".github/scripts/check_opf.py"
PROFILE = ".github/REPOSITORY_PROFILE.json"
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}
TEXT_EXT = (".md", ".json", ".svg", ".txt", ".yml", ".yaml", ".py", ".csv", ".html", ".toml", ".xml", ".sh")
OFFICE_EXT = (".xlsx", ".pptx", ".docx")
LINK = re.compile(r'(?:\]\(|href="|src=")([^)"\s]+)')
TAG = re.compile(r"<[^>]+>")
SPACE = re.compile(r"\s+")


def load_policy(root):
    """Public markers and prohibited components from the repo profile."""
    import json
    markers, comps = [], set()
    path = os.path.join(root, PROFILE)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            policy = json.load(fh).get("content_policy", {})
        markers = [m.casefold() for m in policy.get("local_only_markers", [])]
        comps = {c.casefold() for c in policy.get("prohibited_components", [])}
    return markers, comps


def load_private_terms(root):
    """Optional private terms, read from a file that must live outside ROOT."""
    path = os.environ.get("OPF_PRIVATE_TERMS")
    if not path:
        return []
    real, top = os.path.realpath(path), os.path.realpath(root)
    if real == top or real.startswith(top + os.sep):
        sys.exit("refusing: OPF_PRIVATE_TERMS must point outside the repository")
    with open(real, encoding="utf-8") as fh:
        return [l.strip().casefold() for l in fh if l.strip() and not l.lstrip().startswith("#")]


def flat(text):
    """Casefold and collapse whitespace so a term wrapped across lines still matches."""
    return SPACE.sub(" ", text).casefold()


def file_texts(path, name, warn):
    """Return the readable text of a file, or None if the checker can't read it."""
    if name.endswith(OFFICE_EXT):
        with zipfile.ZipFile(path) as z:
            parts = [z.read(n).decode("utf-8", "replace") for n in z.namelist() if n.endswith((".xml", ".rels"))]
        # Strip tags and join, so a term split across PowerPoint/Word text runs is whole again.
        return [html.unescape(TAG.sub("", p)) for p in parts] + parts
    if name.endswith(".pdf"):
        if not shutil.which("pdftotext"):
            warn.append(f"unscanned PDF (install poppler-utils for pdftotext): {path}")
            return []
        r = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True)
        if r.returncode != 0:
            return None
        return [r.stdout]
    try:
        with open(path, encoding="utf-8") as fh:
            return [fh.read()]
    except UnicodeDecodeError:
        return None


def scan(root, strict=False):
    markers, comps = load_policy(root)
    private = load_private_terms(root)
    bad, warn, links = [], [], 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root).replace(os.sep, "/")
            if any(part.casefold() in comps for part in rel.split("/")):
                bad.append(f"prohibited component: {rel}")
            if any(t in flat(rel) for t in private):
                bad.append(f"private term in path: {rel}")
            if rel in (SELF, PROFILE):
                continue
            texts = file_texts(p, f, warn)
            if texts is None:
                bad.append(f"unscanned file type: {rel}")
                continue
            for t in texts:
                for i, line in enumerate(t.splitlines(), 1):
                    cf = line.casefold()
                    if any(m in cf for m in markers):
                        bad.append(f"local-only marker: {rel}:{i}")
                    if any(term in cf for term in private):
                        bad.append(f"private term: {rel}:{i}")
                whole = flat(t)
                if any(m in whole for m in markers + private) and not any(b.startswith(("local-only marker: " + rel + ":", "private term: " + rel + ":")) for b in bad):
                    bad.append(f"marker split across lines or text runs: {rel}")
            if f.endswith(".md") and texts:
                for m in LINK.finditer(texts[0]):
                    tgt = m.group(1).split("#")[0]
                    if not tgt or re.match(r"^[a-z]+:", tgt) or tgt.startswith("/"):
                        continue
                    links += 1
                    if not os.path.exists(os.path.normpath(os.path.join(dp, tgt))):
                        bad.append(f"broken link: {rel} -> {m.group(1)}")
    if strict:
        bad += warn
        warn = []
    return bad, links, warn


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = args[0] if args else "."
    bad, links, warn = scan(root, strict="--strict" in sys.argv)
    for w in warn:
        print("WARN", w)
    for b in bad:
        print("FAIL", b)
    print(f"checked {links} relative links; {len(bad)} problem(s)")
    sys.exit(1 if bad else 0)
