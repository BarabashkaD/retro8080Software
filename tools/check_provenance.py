# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileCopyrightText: 2026 Dmitry Veremeev (BarabashkaD), https://github.com/BarabashkaD
"""Provenance and line-ending check of the repo.

Usage: python -B tools/check_provenance.py [--repo PATH]

Files: every tracked and untracked-not-ignored file of the working tree (git ls-files).

- Every file under <machine>/collections/<name>/ and <machine>/system/<name>/ (but the folder's
  PROVENANCE.md) is listed in that folder's PROVENANCE.md, with its size and SHA-256; every
  listed file exists. A row of the table: | `<path in the folder>` | <size> | `<sha256>` | ...
- Files listed in a PROVENANCE.md keep their bytes as they are and are exempt from the LF rule.
  Every other text file (no NUL byte in its first 8192 bytes) has LF line ends (no CR) and a
  final newline.

Prints "PASS provenance" and exits 0, or prints each problem and exits 1.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

FOLDER_KINDS = ("collections", "system")
PROVENANCE = "PROVENANCE.md"
ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|(.*)$")
SHA256 = re.compile(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])")
SIZE = re.compile(r"^\s*(\d+)\s*$")


def list_files(repo: Path) -> list[str]:
    r = subprocess.run(["git", "-C", str(repo), "ls-files", "-z", "--cached", "--others",
                        "--exclude-standard"], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git ls-files failed: %s" % r.stderr.decode(errors="replace"))
    names = sorted({n.decode("utf-8") for n in r.stdout.split(b"\0") if n})
    return [n for n in names if (repo / n).is_file()]


def folder_of(name: str) -> str | None:
    """The provenance folder (<machine>/<kind>/<name>) a repo path belongs to, or None."""
    parts = name.split("/")
    if len(parts) >= 4 and parts[1] in FOLDER_KINDS:
        return "/".join(parts[:3])
    return None


def parse_provenance(text: str) -> tuple[dict[str, tuple[int | None, str]], list[str]]:
    """Rows of a PROVENANCE.md: {file: (size or None, sha256)}, and the parse problems."""
    rows: dict[str, tuple[int | None, str]] = {}
    problems: list[str] = []
    for n, line in enumerate(text.splitlines(), 1):
        m = ROW.match(line.strip())
        if not m:
            continue
        rest = m.group(2)
        h = SHA256.search(rest)
        if not h:
            continue  # a table without hashes (e.g. a list of sources)
        name = m.group(1)
        if name in rows:
            problems.append("line %d: %s listed twice" % (n, name))
            continue
        size = None
        for cell in rest.split("|"):
            s = SIZE.match(cell)
            if s:
                size = int(s.group(1))
                break
        rows[name] = (size, h.group(0))
    return rows, problems


def lf_problems(name: str, data: bytes) -> list[str]:
    if b"\0" in data[:8192]:
        return []
    out = []
    if b"\r" in data:
        out.append("%s: CR in line ends (LF only)" % name)
    if data and not data.endswith(b"\n"):
        out.append("%s: no final newline" % name)
    return out


def check(repo: Path) -> list[str]:
    repo = Path(repo)
    files = list_files(repo)
    out: list[str] = []
    folders: dict[str, list[str]] = {}
    for name in files:
        f = folder_of(name)
        if f is not None:
            members = folders.setdefault(f, [])
            if name != f + "/" + PROVENANCE:
                members.append(name[len(f) + 1:])
    exempt: set[str] = set()
    for folder in sorted(folders):
        prov = repo / folder / PROVENANCE
        if not prov.is_file():
            for rel in folders[folder]:
                out.append("%s/%s: not listed (no %s/%s)" % (folder, rel, folder, PROVENANCE))
            continue
        rows, parse = parse_provenance(prov.read_bytes().decode("utf-8", errors="replace"))
        out += ["%s/%s: %s" % (folder, PROVENANCE, p) for p in parse]
        present = set(folders[folder])
        for rel in sorted(present):
            path = folder + "/" + rel
            if rel not in rows:
                out.append("%s: not listed in %s/%s" % (path, folder, PROVENANCE))
                continue
            exempt.add(path)
            data = (repo / path).read_bytes()
            size, digest = rows[rel]
            if size is not None and size != len(data):
                out.append("%s: size %d, listed %d" % (path, len(data), size))
            if hashlib.sha256(data).hexdigest() != digest:
                out.append("%s: SHA-256 differs from %s" % (path, PROVENANCE))
        for rel in sorted(set(rows) - present):
            out.append("%s/%s: listed in %s but missing" % (folder, rel, PROVENANCE))
    for name in files:
        if name not in exempt:
            out += lf_problems(name, (repo / name).read_bytes())
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    args = ap.parse_args(argv)
    out = check(args.repo)
    for line in out:
        print(line)
    if out:
        return 1
    print("PASS provenance")
    return 0


if __name__ == "__main__":
    sys.exit(main())
