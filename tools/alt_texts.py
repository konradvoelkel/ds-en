#!/usr/bin/env python3
"""Write the figure descriptions from alt-texts.yml into the notebooks -- and check them.

    python3 tools/alt_texts.py              # report where we stand
    python3 tools/alt_texts.py --apply      # write the descriptions into the .ipynb files
    python3 tools/alt_texts.py --check      # CI: fail on drift, report what is still missing
    python3 tools/alt_texts.py --complete   # also fail while any figure still lacks a text
    python3 tools/alt_texts.py --skeleton <notebook>   # emit YAML stubs with context

**Why this is so roundabout.** MyST takes the `alt` of an image produced by a notebook
from that output's own `text/plain` representation, and matplotlib puts
`<Figure size 640x480 with 1 Axes>` there. That is not an empty alt, it is a *worse* one:
a check for "is alt missing?" passes cleanly while a screen reader reads out nonsense.
The German original tried every obvious alternative -- cell metadata in five spellings,
and `:alt:` on a `{figure}` directive wrapping a captioned code cell -- and this version
of MyST ignores all of them. Setting `text/plain` is what works.

**So the truth lives in alt-texts.yml, not in the notebook.** Re-executing a notebook
resets `text/plain` to the matplotlib repr. The order is: execute, then `--apply`, then
commit. `--check` runs in CI and catches a forgotten second step.

Keyed by **cell id** (nbformat 4.5), not by position: cells move, ids do not. The ids of
the four notebooks that had none were adopted from the German original, whose cells
correspond one to one, so a figure carries the same id in both editions.

Ported from ds-skript's `tools/alt_texts.py` (2026-10-16), with one deliberate
difference. Upstream finished the work in one go, so its `--check` fails on any figure
without a text. Here the descriptions arrive chapter by chapter, and a check that is red
until the last one lands is a check nobody reads. So `--check` fails on *drift* -- a
description that was written and has since been overwritten or orphaned -- and merely
reports what has not been written yet. `--complete` is the stricter gate, to be wired
into CI on the day the last chapter is done.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXTS = ROOT / "alt-texts.yml"
REPR_PREFIX = "<Figure size"


def load() -> dict:
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML is missing. Run: uv run --with pyyaml python tools/alt_texts.py …")
    return yaml.safe_load(TEXTS.read_text(encoding="utf-8")) or {}


def image_outputs(cell: dict) -> list:
    return [o for o in cell.get("outputs", [])
            if "image/png" in o.get("data", {}) or "image/svg+xml" in o.get("data", {})]


def is_placeholder(out: dict) -> bool:
    return "".join(out["data"].get("text/plain", [])).strip().startswith(REPR_PREFIX)


def skeleton(name: str) -> int:
    """Stubs for one notebook, with the code that drew each figure, as context."""
    nb = json.loads((ROOT / name).read_text(encoding="utf-8"))
    print(f"{name}:")
    for cell in nb["cells"]:
        outs = image_outputs(cell)
        if not outs or not any(is_placeholder(o) for o in outs):
            continue
        code = " ".join("".join(cell["source"]).split())[:150]
        print(f"  # {code}")
        print(f"  {cell['id']}:")
        for _ in outs:
            print('    - ""')
    return 0


def run(mode: str) -> int:
    texts = load()
    applied = drifted = orphaned = written = 0
    todo: dict[str, int] = {}
    notes: list[str] = []

    for name in sorted(p.name for p in ROOT.glob("*.ipynb")):
        path = ROOT / name
        nb = json.loads(path.read_text(encoding="utf-8"))
        by_cell = texts.get(name, {}) or {}
        ids = {c["id"] for c in nb["cells"] if "id" in c}
        for cid in by_cell:
            if str(cid) not in ids:
                notes.append(f"✗ {name}: cell {cid} is in alt-texts.yml but not in the notebook")
                orphaned += 1
        changed = False
        for cell in nb["cells"]:
            outs = image_outputs(cell)
            if not outs:
                continue
            wanted = by_cell.get(cell.get("id"))
            if wanted is None:
                todo[name] = todo.get(name, 0) + sum(1 for o in outs if is_placeholder(o))
                continue
            if len(wanted) != len(outs):
                notes.append(f"✗ {name}: cell {cell['id']} has {len(outs)} figures "
                             f"but {len(wanted)} descriptions")
                drifted += 1
                continue
            for out, text in zip(outs, wanted):
                written += 1
                if "".join(out["data"].get("text/plain", [])) == text:
                    continue
                if mode == "apply":
                    out["data"]["text/plain"] = [text]
                    changed = True
                    applied += 1
                else:
                    drifted += 1
                    why = ("still the matplotlib repr -- was the notebook re-executed "
                           "without a following --apply?" if is_placeholder(out)
                           else "a different text")
                    notes.append(f"✗ {name}: cell {cell['id']} carries {why}")
        if changed:
            path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n",
                            encoding="utf-8")

    if mode == "apply":
        print(f"✓ {applied} description(s) written")
        return 0

    for n in notes:
        print("  " + n)
    remaining = sum(todo.values())
    if drifted or orphaned:
        print(f"✗ {drifted} drifted, {orphaned} orphaned. After re-executing a notebook: "
              f"python3 tools/alt_texts.py --apply")
        return 1
    print(f"✓ {written} description(s) in place and current")
    if remaining:
        print(f"  {remaining} figure(s) still without one, in {len(todo)} notebook(s):")
        for name, n in sorted(todo.items(), key=lambda kv: -kv[1]):
            print(f"    {n:3d}  {name}")
        if mode == "complete":
            print("✗ --complete: every figure needs a description")
            return 1
    return 0


def main() -> int:
    if "--skeleton" in sys.argv:
        args = [a for a in sys.argv[1:] if not a.startswith("--")]
        if len(args) != 1:
            print(__doc__)
            return 2
        return skeleton(args[0])
    if "--apply" in sys.argv:
        return run("apply")
    if "--complete" in sys.argv:
        return run("complete")
    return run("check")


if __name__ == "__main__":
    raise SystemExit(main())
