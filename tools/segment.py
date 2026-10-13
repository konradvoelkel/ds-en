"""Split a chapter into translation blocks.

One definition of "block", used by everything else: the translation itself (English
and German are kept in strict block alignment), the alignment check, and the upstream
staleness check. If this function changes, every file in sync/segments/ has to be
regenerated, so prefer adding a new block kind over changing how an existing one is cut.

A block is the smallest unit a translator may rewrite freely inside and may never
rewrite across. Paragraph-sized, mostly:

* Markdown: top-level blank lines separate blocks. Fenced code (``` / ~~~) and display
  math ($$) stay whole, because they are not prose. Directive delimiters (:::, ::::)
  are blocks of their own, so an admonition contributes an opening block, its inner
  paragraphs, and a closing block -- that keeps "Definition" and the sentences under it
  separately trackable without any nesting logic.
* Notebooks: code cells are one block each (never split -- a diff inside code is the
  translator's problem, not the segmenter's). Markdown cells go through the Markdown
  rules above, so a long cell is still tracked paragraph by paragraph.

Usage:
    python3 tools/segment.py <file> [--json]
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

FENCE = re.compile(r"^\s*(```+|~~~+)")
DIRECTIVE_DELIM = re.compile(r"^\s*(:{3,})")
MATH_DELIM = re.compile(r"^\s*\$\$")


@dataclass
class Block:
    bid: str  # stable within a file: "12" for Markdown, "c3.4" for notebook cell 3, block 4
    kind: str  # prose | code | math | directive | heading | table
    text: str
    digest: str  # sha256 of the normalised text, first 16 hex chars

    def preview(self, n: int = 72) -> str:
        flat = " ".join(self.text.split())
        return flat[:n] + ("…" if len(flat) > n else "")


def _normalise(text: str) -> str:
    """Trailing whitespace is noise; everything else is signal."""
    return "\n".join(line.rstrip() for line in text.strip("\n").split("\n"))


def _digest(text: str) -> str:
    return hashlib.sha256(_normalise(text).encode("utf-8")).hexdigest()[:16]


def _classify(text: str) -> str:
    head = text.lstrip()
    m = FENCE.match(head)
    if m:
        # ```{figure} / ```{mermaid} are directives with translatable content inside;
        # ```python and friends are code and mostly stay as they are.
        rest = head[m.end():].lstrip()
        return "directive" if rest.startswith("{") else "code"
    if MATH_DELIM.match(head):
        return "math"
    if DIRECTIVE_DELIM.match(head):
        return "directive"
    if head.startswith("#"):
        return "heading"
    if head.startswith("|"):
        return "table"
    return "prose"


def split_markdown(source: str, prefix: str = "") -> list[Block]:
    """Cut Markdown text into blocks. `prefix` namespaces ids inside a notebook cell."""
    lines = source.split("\n")
    blocks: list[list[str]] = []
    current: list[str] = []
    fence: str | None = None  # the opening fence string we are waiting to see closed
    in_math = False

    def flush() -> None:
        nonlocal current
        if any(line.strip() for line in current):
            blocks.append(current)
        current = []

    for line in lines:
        if fence is not None:
            current.append(line)
            # A closing fence is at least as long as the opening one and carries no info.
            m = FENCE.match(line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
                flush()
            continue

        if in_math:
            current.append(line)
            if MATH_DELIM.match(line):
                in_math = False
                flush()
            continue

        m = FENCE.match(line)
        if m:
            flush()
            current.append(line)
            fence = m.group(1)
            continue

        if MATH_DELIM.match(line) and line.strip() == "$$":
            flush()
            current.append(line)
            in_math = True
            continue

        if DIRECTIVE_DELIM.match(line):
            # ::: lines stand alone, opening and closing alike.
            flush()
            blocks.append([line])
            continue

        if not line.strip():
            flush()
            continue

        current.append(line)

    flush()

    out = []
    for i, body in enumerate(blocks):
        text = "\n".join(body)
        bid = f"{prefix}{i}" if prefix else str(i)
        out.append(Block(bid=bid, kind=_classify(text), text=_normalise(text), digest=_digest(text)))
    return out


def split_notebook(path: Path) -> list[Block]:
    nb = json.loads(path.read_text())
    out: list[Block] = []
    for ci, cell in enumerate(nb["cells"]):
        source = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            out.extend(split_markdown(source, prefix=f"c{ci}."))
        elif cell["cell_type"] == "code":
            text = _normalise(source)
            if not text.strip():
                continue
            out.append(Block(bid=f"c{ci}", kind="code", text=text, digest=_digest(text)))
    return out


def segment(path: Path) -> list[Block]:
    if path.suffix == ".ipynb":
        return split_notebook(path)
    return split_markdown(path.read_text())


def segment_text(name: str, source: str) -> list[Block]:
    """Same as segment(), for content that is not on disk (e.g. `git show` output)."""
    if name.endswith(".ipynb"):
        nb = json.loads(source)
        out: list[Block] = []
        for ci, cell in enumerate(nb["cells"]):
            text = "".join(cell["source"])
            if cell["cell_type"] == "markdown":
                out.extend(split_markdown(text, prefix=f"c{ci}."))
            elif cell["cell_type"] == "code":
                norm = _normalise(text)
                if norm.strip():
                    out.append(Block(bid=f"c{ci}", kind="code", text=norm, digest=_digest(norm)))
        return out
    return split_markdown(source)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    as_json = "--json" in sys.argv
    if not args:
        print(__doc__)
        return 2
    path = Path(args[0])
    blocks = segment(path)
    if as_json:
        print(json.dumps([asdict(b) for b in blocks], ensure_ascii=False, indent=1))
    else:
        for b in blocks:
            print(f"{b.bid:>8s}  {b.kind:9s}  {b.digest}  {b.preview()}")
        print(f"-- {len(blocks)} blocks in {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
