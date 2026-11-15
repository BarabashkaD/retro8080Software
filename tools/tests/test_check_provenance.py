# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileCopyrightText: 2026 Dmitry Veremeev (BarabashkaD), https://github.com/BarabashkaD
import hashlib
import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check_provenance as cp  # noqa: E402

GAME = b"\xe6\x00\x01\x02\x03\x00\xff"  # a tape image: binary, NUL bytes
DIZ = b"\x8f\xe0\xa8\xac\xa5\xe0 1999\r\n"  # CP866 with CR LF, kept as it is


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def provenance(rows: dict[str, bytes]) -> bytes:
    lines = ["# Provenance", "", "| File | Size | SHA-256 |", "|---|---|---|"]
    lines += ["| `%s` | %d | `%s` |" % (n, len(d), sha(d)) for n, d in rows.items()]
    return ("\n".join(lines) + "\n").encode()


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        self.write("README.md", b"# test\n")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name: str, data: bytes) -> None:
        p = self.repo / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    def problems(self) -> list[str]:
        return cp.check(self.repo)


class TestCheckProvenance(Base):
    def test_listed_files_pass(self):
        self.write("rk86/collections/set/A.GAM", GAME)
        self.write("rk86/collections/set/PROVENANCE.md", provenance({"A.GAM": GAME}))
        self.assertEqual(self.problems(), [])

    def test_unlisted_file_fails(self):
        self.write("rk86/collections/set/A.GAM", GAME)
        self.write("rk86/collections/set/B.GAM", GAME)
        self.write("rk86/collections/set/PROVENANCE.md", provenance({"A.GAM": GAME}))
        out = self.problems()
        self.assertEqual(len(out), 1, out)
        self.assertIn("rk86/collections/set/B.GAM", out[0])
        self.assertIn("not listed", out[0])

    def test_folder_without_provenance_fails(self):
        self.write("rk86/system/loader/loader.asm", b"; loader\n")
        out = self.problems()
        self.assertEqual(len(out), 1, out)
        self.assertIn("rk86/system/loader/loader.asm", out[0])

    def test_hash_mismatch_fails(self):
        self.write("rk86/collections/set/A.GAM", GAME + b"\x00")
        self.write("rk86/collections/set/PROVENANCE.md", provenance({"A.GAM": GAME}))
        out = self.problems()
        self.assertTrue(any("A.GAM" in p and "SHA-256" in p for p in out), out)

    def test_size_mismatch_fails(self):
        self.write("rk86/collections/set/A.GAM", GAME)
        text = provenance({"A.GAM": GAME}).replace(b"| 7 |", b"| 8 |")
        self.write("rk86/collections/set/PROVENANCE.md", text)
        out = self.problems()
        self.assertTrue(any("A.GAM" in p and "size" in p for p in out), out)

    def test_listed_missing_file_fails(self):
        self.write("rk86/collections/set/PROVENANCE.md", provenance({"A.GAM": GAME}))
        out = self.problems()
        self.assertTrue(any("A.GAM" in p and "missing" in p for p in out), out)

    def test_crlf_listed_file_passes(self):
        self.write("rk86/collections/set/FILE_ID.DIZ", DIZ)
        self.write("rk86/collections/set/PROVENANCE.md", provenance({"FILE_ID.DIZ": DIZ}))
        self.assertEqual(self.problems(), [])

    def test_crlf_unlisted_text_fails(self):
        self.write("docs/note.md", b"line one\r\nline two\r\n")
        out = self.problems()
        self.assertEqual(len(out), 1, out)
        self.assertIn("docs/note.md", out[0])
        self.assertIn("CR", out[0])

    def test_missing_final_newline_fails(self):
        self.write("docs/note.md", b"no newline")
        out = self.problems()
        self.assertEqual(len(out), 1, out)
        self.assertIn("final newline", out[0])

    def test_unlisted_binary_outside_collections_passes_lf_rule(self):
        self.write("tools/data.bin", GAME)
        self.assertEqual(self.problems(), [])

    def test_crlf_provenance_md_fails(self):
        self.write("rk86/collections/set/A.GAM", GAME)
        self.write("rk86/collections/set/PROVENANCE.md",
                   provenance({"A.GAM": GAME}).replace(b"\n", b"\r\n"))
        out = self.problems()
        self.assertTrue(any("PROVENANCE.md" in p and "CR" in p for p in out), out)

    def test_ignored_file_skipped(self):
        self.write(".gitignore", b"build/\n")
        self.write("build/junk.txt", b"crlf\r\n")
        self.assertEqual(self.problems(), [])

    def test_main_prints_pass(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = cp.main(["--repo", str(self.repo)])
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "PASS provenance")

    def test_main_fails(self):
        self.write("docs/note.md", b"x\r\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = cp.main(["--repo", str(self.repo)])
        self.assertEqual(rc, 1)
        self.assertNotIn("PASS", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
