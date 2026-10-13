"""Check that a style pass changed only prose.

`sync.py align` proves the block structure survived and `check_english.py` proves no
German came back, but neither notices if an editor quietly rewrote a formula, renamed a
link, or reached into a code cell whose stored output no longer matches. This compares a
file against a git ref and asserts that everything which is not prose is byte-identical.

    python3 tools/check_untouched.py HEAD descriptive-statistics.md
    python3 tools/check_untouched.py HEAD~1 *.md *.ipynb

What must not change: inline and display maths, fenced code blocks, link texts and link
targets, directive and admonition lines, MyST targets, citation keys, and -- in a notebook
-- every code cell, in full.

Maths, links and citations are compared as multisets, not in order: rewriting a sentence
to put its clauses the other way round moves the formulas in it without changing any of
them, and that is exactly what a style pass is for. A reordering is reported, not failed.
Code cells and the sequence of block kinds are compared in order, because there no
reordering is innocent.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from segment import segment_text  # noqa: E402

ORDERED = {"code cells", "block kinds"}

MATHS = re.compile(r"\$\$?[^$]*\$\$?", re.S)
LINKS = re.compile(r"\[([^\]\n]{0,120})\]\(([^)\s]+)\)")
DIRECTIVE = re.compile(r"^\s*(?::{3,}|`{3,})\{[^}]*\}.*$|^\s*\([a-z0-9_-]+\)=\s*$", re.M)
CITES = re.compile(r"\{cite\}`[^`]*`")


def _facets(name: str, text: str) -> dict[str, list]:
    """The parts of a file a style pass may not touch."""
    if name.endswith(".ipynb"):
        nb = json.loads(text)
        prose = "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "markdown")
        code = ["".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"]
    else:
        prose, code = text, []
    return {
        "maths": MATHS.findall(prose),
        "links": LINKS.findall(prose),
        "directives": DIRECTIVE.findall(prose),
        "citations": CITES.findall(prose),
        "code cells": code,
        "block kinds": [b.kind for b in segment_text(name, text)],
    }


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    ref, files = sys.argv[1], sys.argv[2:]
    bad = 0
    for name in files:
        try:
            old = subprocess.run(["git", "show", f"{ref}:{name}"],
                                 capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            print(f"· {name}: not in {ref}, skipped")
            continue
        new = Path(name).read_text()
        before, after = _facets(name, old), _facets(name, new)
        problems, reordered = [], []
        for key in before:
            if before[key] == after[key]:
                continue
            if key not in ORDERED and sorted(map(str, before[key])) == sorted(map(str, after[key])):
                reordered.append(key)
            else:
                problems.append(key)
        for key in reordered:
            print(f"· {name}: {key} reordered but unchanged – a restructured sentence")
        if problems:
            bad += 1
            print(f"✗ {name}: changed {', '.join(problems)}")
            for key in problems:
                a, b = before[key], after[key]
                if len(a) != len(b):
                    print(f"    {key}: {len(a)} before, {len(b)} after")
                else:
                    for x, y in zip(a, b):
                        if x != y:
                            print(f"    {key}: {str(x)[:70]!r}\n          -> {str(y)[:70]!r}")
                            break
        elif not reordered:
            print(f"✓ {name}: prose only")
        else:
            print(f"✓ {name}: prose only (with reordering)")
    print(f"-- {len(files) - bad}/{len(files)} changed prose only")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
