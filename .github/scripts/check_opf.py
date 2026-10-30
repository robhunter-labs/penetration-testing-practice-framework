#!/usr/bin/env python3
"""Open Practice Framework repo check.

Fails on: a retired legacy name anywhere, a local-only marker or
prohibited path component from .github/REPOSITORY_PROFILE.json, or a broken
relative link.

Sensitive terms are never stored in plaintext. A profile entry may be
  "sha256:<length>:<hex>"  -> marker: sha256 of the casefolded term, matched as a substring
  "sha256:<hex>"           -> component: sha256 of the casefolded path component
The checker hashes every casefolded window of <length> characters (and every
path component) and compares. Plain entries are matched as plain substrings.
"""
import hashlib, json, os, re, subprocess, sys, zipfile

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
SELF = ".github/scripts/check_opf.py"
PROFILE = ".github/REPOSITORY_PROFILE.json"
ALLOW_LEGACY = set()
# Retired framework name (4 chars), allowed nowhere.
LEGACY = (4, "ca91303abfb72d5ca36e1b2112e5e22446329f5ff8721707a45127dd7fdb409c")
LINK = re.compile(r'(?:\]\(|href="|src=")([^)"\s]+)')


def _h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_policy(root):
    plain, hashed, comp_plain, comp_hashed = [], {}, set(), set()
    path = os.path.join(root, PROFILE)
    if os.path.exists(path):
        policy = json.load(open(path, encoding="utf-8"))["content_policy"]
        for m in policy.get("local_only_markers", []):
            parts = m.split(":")
            if m.startswith("sha256:") and len(parts) == 3 and parts[1].isdigit():
                hashed.setdefault(int(parts[1]), set()).add(parts[2])
            else:
                plain.append(m.casefold())
        for c in policy.get("prohibited_components", []):
            (comp_hashed.add(c[7:]) if c.startswith("sha256:") else comp_plain.add(c.casefold()))
    return plain, hashed, comp_plain, comp_hashed


def window_hit(text, length, digests):
    if len(text) < length:
        return False
    for i in range(len(text) - length + 1):
        if _h(text[i:i + length]) in digests:
            return True
    return False


def scan(root):
    plain, hashed, comp_plain, comp_hashed = load_policy(root)
    bad, links = [], 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d != ".git"]
        for f in fn:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root).replace(os.sep, "/")
            for part in rel.split("/"):
                cf = part.casefold()
                if cf in comp_plain or _h(cf) in comp_hashed:
                    bad.append(f"prohibited component: {rel}")
            if rel not in ALLOW_LEGACY and rel != SELF and window_hit(rel.casefold(), *LEGACY[:1], {LEGACY[1]}):
                bad.append(f"legacy name in filename: {rel}")
            if rel in (SELF, PROFILE):
                continue
            texts = []
            if f.endswith((".md", ".json", ".svg", ".txt", ".yml", ".yaml", ".py", ".csv", ".html")) or ("/" not in rel and "." not in f):
                texts.append(open(p, encoding="utf-8", errors="replace").read())
            elif f.endswith((".xlsx", ".pptx", ".docx")):
                z = zipfile.ZipFile(p)
                texts += [z.read(n).decode("utf-8", "replace") for n in z.namelist() if n.endswith((".xml", ".rels"))]
            elif f.endswith(".pdf"):
                texts.append(subprocess.run(["pdftotext", p, "-"], capture_output=True, text=True).stdout)
            for t in texts:
                for i, line in enumerate(t.splitlines(), 1):
                    cf = line.casefold()
                    if rel not in ALLOW_LEGACY and window_hit(cf, LEGACY[0], {LEGACY[1]}):
                        bad.append(f"legacy name: {rel}:{i}")
                    if any(m in cf for m in plain) or any(window_hit(cf, n, d) for n, d in hashed.items()):
                        bad.append(f"local-only marker: {rel}:{i}")
            if f.endswith(".md"):
                for m in LINK.finditer(texts[0]):
                    tgt = m.group(1).split("#")[0]
                    if not tgt or re.match(r"^[a-z]+:", tgt) or tgt.startswith("/"):
                        continue
                    links += 1
                    if not os.path.exists(os.path.normpath(os.path.join(dp, tgt))):
                        bad.append(f"broken link: {rel} -> {m.group(1)}")
    return bad, links


if __name__ == "__main__":
    bad, links = scan(ROOT)
    for b in bad:
        print("FAIL", b)
    print(f"checked {links} relative links; {len(bad)} problem(s)")
    sys.exit(1 if bad else 0)
