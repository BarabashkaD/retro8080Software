# AGENTS.md

Instructions for coding agents in `retro8080Software`. The family rules of `retroICs`
(`docs/agents/global.md`, `docs/agents/review-checklist.md` of a sibling checkout `../retroICs`)
apply here too.

## Repository

- Programs for 8080-family machines: binaries kept as they are, asm and C sources. No image
  builders (ROM disk, card or tape writers, assemblers, emulators): those are platform tooling.
- `<machine>/collections/<name>/`: a third-party set as it was found. `<machine>/system/<name>/`:
  loaders, menus, boot code. `cpm/` later.
- Not a dependency of `retroICs` or `retroMachines`; platform repos pin it as a submodule.

## Commands

From the repo root, in PowerShell 7 (`pwsh`); never `bash`, `sh` or Linux utilities. Python 3,
standard library only, always with `-B`.

```text
python -B -m unittest discover -s tools/tests -v                    the tools' tests
python -B tools/check_provenance.py                                 provenance and LF rule
python -B ../retroICs/tools/check_privacy.py --repo . --all         privacy, every commit
```

CI (`.github/workflows/checks.yml`, job `lint`) runs the same, with the privacy checker of
`retroICs` at a pinned commit.

## Adding a collection

1. Copy the files as they were found, in one commit of this repo; the source's history is not
   brought in. Where the source is a repository, its URL, the commit the files were copied from and
   their path go into `PROVENANCE.md` (step 3), which is the record of where they came from.
2. Keep every byte: no line-ending, encoding or name changes. `.gitattributes` is `* -text`.
3. Write `<machine>/collections/<name>/PROVENANCE.md` (CC BY 4.0, the owner's doc): origin
   (repo URL, commit, path, or the site and date), where it was copied from, the licence status as
   stated by the authors (or "none stated"), the collection's own notes, and a table with one row
   per file: `` | `<file>` | <size> | `<sha256>` | ``.
4. Run the three checks. Anything the privacy checker flags in the copied files (an email or path
   kept byte for byte, already public in the source) gets an exact `allow` line in
   `privacy-allow.txt` with its reason, or stops the copy.
5. A line in `CHANGELOG.md` under `## Unreleased`.

## Provenance rules

- Every file under a collection or system folder is listed in its `PROVENANCE.md` with its size and
  SHA-256 (`tools/check_provenance.py`). Listed files are exempt from the LF rule; every other text
  file has LF line ends and a final newline.
- Never claim a licence the authors did not state. Third-party terms are stated per folder; they are
  not relicensed by `NOTICE`.
- A program that is changed on purpose (a fix, a port) becomes a new file or folder with its own
  provenance row naming the original; the original stays as it was.

## Rules

- No absolute local paths, user or host names, IPs or emails in committed files or commit messages,
  except the exact lines of `privacy-allow.txt` (each with its reason).
- The owner's code has SPDX lines (BSD-3-Clause); the owner's files use LF and a final newline.
- Commit or push only when the maintainer asks. `main` changes by pull request ("Rebase and
  merge"); the maintainer merges and tags (`vX.Y.Z`, semver) by hand. An agent never creates a tag
  or a release.
- CHANGELOG and release notes list features, changes, fixes and known issues only.
