"""Get the text out of a notebook and back in, without touching the JSON by hand.

Editing .ipynb directly is how notebooks get corrupted: outputs are large, sources are
JSON arrays of lines, and a single stray escape breaks the file. So translation works on
a flat text export instead -- one marker line per cell, sources verbatim in between --
and this script writes it back, leaving outputs, metadata, execution counts and cell
order exactly as they were.

    python3 tools/nbtext.py export <notebook> [-o out.txt]
    python3 tools/nbtext.py import <notebook> <edited.txt>   # writes the notebook in place
    python3 tools/nbtext.py check  <notebook>                # export/import round-trips?

The import refuses to run if the number or the types of the cells changed: block
alignment with the German original is the invariant the whole sync machinery rests on,
and a translator who needs an extra cell has to say so out loud rather than silently
break it.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

MARKER = "@@@ cell {i} {kind} @@@"
MARKER_RE = re.compile(r"^@@@ cell (\d+) (markdown|code|raw) @@@$")


def _tail(source: str) -> str:
    """The run of newlines a cell ends with -- stripped for the export, restored on import,
    so a cell the translator never touched comes back byte for byte."""
    return source[len(source.rstrip("\n")):]


def _as_lines(text: str) -> list[str]:
    """Jupyter stores a source as a list of lines, each keeping its newline but the last."""
    if text == "":
        return []
    parts = text.split("\n")
    return [p + "\n" for p in parts[:-1]] + ([parts[-1]] if parts[-1] else [])


def export(nb_path: Path) -> str:
    nb = json.loads(nb_path.read_text())
    out: list[str] = []
    for i, cell in enumerate(nb["cells"]):
        out.append(MARKER.format(i=i, kind=cell["cell_type"]))
        out.append("".join(cell["source"]).rstrip("\n"))
    return "\n".join(out) + "\n"


def parse(flat: str) -> list[tuple[int, str, str]]:
    cells: list[tuple[int, str, str]] = []
    current: list[str] | None = None
    idx = kind = None
    for line in flat.split("\n"):
        m = MARKER_RE.match(line)
        if m:
            if current is not None:
                cells.append((idx, kind, "\n".join(current).rstrip("\n")))
            idx, kind, current = int(m.group(1)), m.group(2), []
        elif current is not None:
            current.append(line)
        elif line.strip():
            raise SystemExit(f"text before the first cell marker: {line[:60]!r}")
    if current is not None:
        cells.append((idx, kind, "\n".join(current).rstrip("\n")))
    return cells


def import_(nb_path: Path, flat_path: Path) -> None:
    nb = json.loads(nb_path.read_text())
    cells = parse(flat_path.read_text())
    if len(cells) != len(nb["cells"]):
        raise SystemExit(
            f"cell count changed: notebook has {len(nb['cells'])}, text has {len(cells)}. "
            "Cells may not be added, removed or merged."
        )
    for pos, (idx, kind, text) in enumerate(cells):
        if idx != pos:
            raise SystemExit(f"cell markers out of order at position {pos}: marker says {idx}")
        if kind != nb["cells"][pos]["cell_type"]:
            raise SystemExit(
                f"cell {pos} changed type: notebook has {nb['cells'][pos]['cell_type']}, text has {kind}"
            )
        nb["cells"][pos]["source"] = _as_lines(text + _tail("".join(nb["cells"][pos]["source"])))
    # Jupyter's own formatting: 1-space indent, trailing newline, non-ASCII kept as is.
    nb_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")


def check(nb_path: Path) -> int:
    before = nb_path.read_text()
    cells = parse(export(nb_path))
    nb = json.loads(before)
    bad = [
        i
        for i, (_, _, text) in enumerate(cells)
        if _as_lines(text + _tail("".join(nb["cells"][i]["source"]))) != nb["cells"][i]["source"]
    ]
    if bad:
        print(f"round-trip differs in cell(s): {bad}")
        return 1
    print(f"{nb_path}: {len(cells)} cells round-trip cleanly")
    return 0


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    cmd, nb_path = sys.argv[1], Path(sys.argv[2])
    if cmd == "export":
        text = export(nb_path)
        if "-o" in sys.argv:
            Path(sys.argv[sys.argv.index("-o") + 1]).write_text(text)
        else:
            sys.stdout.write(text)
        return 0
    if cmd == "import":
        import_(nb_path, Path(sys.argv[3]))
        print(f"{nb_path}: sources replaced, outputs untouched")
        return 0
    if cmd == "check":
        return check(nb_path)
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
