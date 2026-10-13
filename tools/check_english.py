"""Catch the things a translator misses.

Not a style checker and not a spell checker: this only looks for the handful of mistakes
that are mechanical, frequent, and invisible on a quick read -- a German sentence left
behind in a long chapter, a decimal comma that should be a point, German quotation marks,
a Genderstern, an em dash where the book uses a spaced en dash.

    python3 tools/check_english.py            # every file listed in sync/progress.json
    python3 tools/check_english.py <file>...  # just these

Findings are heuristics. Quoted German is legitimate (see TRANSLATION.md section 3), so a
hit is a question, not a verdict. Silence a deliberate one by putting the German in
backticks or quotation marks, which this tool skips, or -- when the German has to stand in
the open -- by recording it with a reason in sync/check-ignore/<file>.json.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from segment import segment  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# Function words: common enough that a surviving German sentence almost always contains one,
# rare enough as English words that false positives stay manageable. ("die", "war", "man",
# "bei" and friends are left out precisely because they collide with English.)
GERMAN_WORDS = re.compile(
    r"\b(der|das|und|ist|sind|nicht|mit|von|wir|auch|noch|eine|einen|einem|einer|"
    r"dass|werden|wurde|haben|hatte|kann|können|sich|oder|aber|wie|nach|über|durch|"
    r"zum|zur|dem|den|des|sowie|damit|wenn|dann|schon|immer|sehr|mehr|hier|diese|"
    r"dieser|dieses|jede|jeder|jedes|beim|einfach|möglich|zwischen|gegen|ohne|um)\b",
    re.IGNORECASE,
)
DECIMAL_COMMA = re.compile(r"(?<=\d),(?=\d{1,2}(?!\d))|\{,\}")
GERMAN_QUOTES = re.compile(r"[„“‚‘»«]|,,")
GENDERSTERN = re.compile(r"\\?\*innen\b")
EM_DASH = re.compile(r"—")
SHARP_S = re.compile(r"ß")

CHECKS = [
    (GERMAN_WORDS, "German function word"),
    (DECIMAL_COMMA, "decimal comma (English uses a point)"),
    (GERMAN_QUOTES, "German quotation marks"),
    (GENDERSTERN, "Genderstern"),
    (EM_DASH, "em dash (this book uses a spaced en dash)"),
    (SHARP_S, "ß"),
]

# Inline code, fenced code, maths, link targets and quoted German are all places where
# German is allowed to survive. Blanking them before the search keeps the noise down.
MASK = [
    re.compile(r"`[^`]*`"),
    re.compile(r"\$\$?[^$]*\$\$?"),
    re.compile(r"\]\([^)]*\)"),
    re.compile(r"https?://\S+"),
    re.compile(r'"[^"]{0,80}"'),
]


def _mask(text: str) -> str:
    for pattern in MASK:
        text = pattern.sub(lambda m: " " * len(m.group(0)), text)
    return text


def ignored(name: str) -> set[tuple[str, str]]:
    path = ROOT / "sync" / "check-ignore" / f"{name}.json"
    if not path.exists():
        return set()
    return {(e["block"], e["label"]) for e in json.loads(path.read_text())["ignore"]}


def check(path: Path) -> list[tuple[str, str, str]]:
    skip = ignored(path.name)
    findings = []
    for block in segment(path):
        if block.kind == "code":
            continue
        masked = _mask(block.text)
        for pattern, label in CHECKS:
            if (block.bid, label) in skip:
                continue
            for m in pattern.finditer(masked):
                findings.append((block.bid, label, block.text[max(0, m.start() - 40):m.end() + 40]))
    return findings


def translated_files() -> list[str]:
    progress = json.loads((ROOT / "sync" / "progress.json").read_text())
    return [f for f, state in progress["files"].items() if state.get("translated")]


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    files = args or translated_files()
    total = 0
    for name in files:
        path = ROOT / name
        if not path.exists():
            print(f"{name}: missing")
            continue
        findings = check(path)
        total += len(findings)
        if findings:
            print(f"\n{name}: {len(findings)} finding(s)")
            for bid, label, context in findings:
                print(f"  block {bid:>8s}  {label}")
                print(f"      …{' '.join(context.split())}…")
        else:
            print(f"{name}: clean")
    print(f"\n-- {total} finding(s) across {len(files)} file(s)")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
