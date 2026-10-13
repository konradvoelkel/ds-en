"""Compare how often each chapter is named, in German and in English.

Chapters refer to each other by writing a link text by hand: `[Expected value and
variance](expectation-variance.md)`. With a chapter per translator and most targets still
German when a translator reaches them, those names are guesses, and they drift.

A plain "every link to a file must use the same text" rule would be wrong, because the
German original varies on purpose: it writes "Kovarianz" where the sentence wants the
topic and "Kovarianz und Abhängigkeit" where it wants the chapter. So the check is
relative: if the German calls a chapter by two names, the English may too; if the German
calls it by one and the English by two, somebody guessed.

    python3 tools/check_links.py

Fewer English labels than German is normal and usually right: German inflects its link
texts ("kontaminierte" / "kontaminierten Normalverteilung") where English has one name, and
a dropped block takes its link with it. That is reported and does not fail. More English
labels than German is the real signal -- it means two translators guessed differently at a
chapter whose title neither of them could see -- and that fails.

Only translated files are compared; the rest are still German by definition.
"""

from __future__ import annotations

import collections
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sync import german, pairs, translated  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# A link label: short, single-line, no maths. The narrowness matters -- `[5,8)$ ... [x](y)`
# in a formula otherwise reads as a link label the width of a paragraph.
LINK = re.compile(r"\[([^\]\n$]{1,70})\]\(([a-zäöüß0-9_-]+\.(?:md|ipynb))\)")


def _text(raw: str, notebook: bool) -> str:
    if not notebook:
        return raw
    return "\n".join("".join(c["source"]) for c in json.loads(raw)["cells"])


def main() -> int:
    filemap = json.loads((ROOT / "sync" / "filemap.json").read_text())["map"]
    commit = json.loads((ROOT / "sync" / "upstream.json").read_text())["commit"]
    done = translated()

    en_labels: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    de_labels: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)

    for de_file, en_file in pairs():
        if en_file not in done:
            continue
        english = _text((ROOT / en_file).read_text(), en_file.endswith(".ipynb"))
        original = _text(german(de_file, commit), de_file.endswith(".ipynb"))
        for label, target in LINK.findall(english):
            en_labels[target][label] += 1
        for label, target in LINK.findall(original):
            mapped = filemap.get(target)
            if mapped:
                de_labels[mapped][label] += 1

    bad = noted = 0
    for target in sorted(set(en_labels) | set(de_labels)):
        n_de, n_en = len(de_labels[target]), len(en_labels[target])
        if n_de == n_en:
            continue
        if n_en < n_de:
            noted += 1
            print(f"· {target}: German {n_de} labels, English {n_en} – German inflection or a "
                  f"dropped block, normally fine")
        else:
            bad += 1
            print(f"✗ {target}: German {n_de} label(s), English {n_en} – two translators named "
                  f"the same chapter differently")
        print(f"    German : " + "; ".join(repr(x) for x in de_labels[target]))
        print(f"    English: " + "; ".join(repr(x) for x in en_labels[target]))
    total = len(set(en_labels) | set(de_labels))
    print(f"-- {total - bad - noted} target(s) match exactly, {noted} collapsed, {bad} to fix")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
