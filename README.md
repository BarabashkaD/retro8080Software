# retro8080Software

Software for 8080-family home computers (Radio-86RK first): program collections and system code,
each with its provenance. Binaries are kept as they are, byte for byte; asm and C sources sit next
to them when they exist.

No image builders: the tools that make ROM disk, card or tape images from these programs
(assemblers, emulators, image writers) are platform tooling and live in the platform repos.

## Layout

| Path | Content |
|---|---|
| `AGENTS.md` | rules for coding agents in this repo |
| `<machine>/collections/<name>/` | a third-party set of programs as it was found, with `PROVENANCE.md` |
| `<machine>/system/<name>/` | loaders, menus, boot code (later the monitors), with `PROVENANCE.md` |
| `tools/check_provenance.py` | every file of those folders listed with its SHA-256; LF rule for the rest |
| `tools/tests/` | the tools' tests |
| `LICENSE`, `NOTICE` | the owner's BSD-3-Clause licence and attribution line |
| `LICENSES/` | the licence texts of the owner's files |

## Status

| Machine | Folder | Content |
|---|---|---|
| Radio-86RK | `rk86/collections/pyhonin-1999/` | a 1999 game tape collection (26 `.GAM`, 22 `.RKR`, `bios.rk`, its own notes), copied from karabas-go-core-rk86 (`pk/`), bytes unchanged; licence: none stated |

## Checks

```text
python -B -m unittest discover -s tools/tests -v
python -B tools/check_provenance.py
python -B ../retroICs/tools/check_privacy.py --repo . --all
```

## Licences

- `LICENSE` (BSD-3-Clause, the owner's copyright line) covers the owner's files only, not the
  third-party programs.
- The owner's code (`tools/`): BSD-3-Clause (`LICENSE`, `LICENSES/BSD-3-Clause.txt`).
- The owner's docs (`README.md`, `AGENTS.md`, `CHANGELOG.md`, the `PROVENANCE.md` files): CC BY 4.0
  (`LICENSES/CC-BY-4.0.txt`).
- Third-party programs keep their own terms, stated per folder in its `PROVENANCE.md`; they are not
  relicensed.
- Credit to Dmitry Veremeev (BarabashkaD) must be kept in copies and derived works (`NOTICE`).
