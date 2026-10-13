"""Keep the English edition honest about the German original.

Three jobs, three subcommands:

    python3 tools/sync.py align                 # English and German still block-aligned?
    python3 tools/sync.py manifest              # record the German block digests
    python3 tools/sync.py check [<new-commit>]  # what went stale since the pinned commit?

`align` is the cheap invariant check, meant for every commit and for CI. `manifest` is run
once per translated chapter, and again whenever the pin in sync/upstream.json moves.
`check` is the point of the whole exercise: it turns an upstream diff into a list of
English paragraphs that need re-translating.

The German text is read straight out of the ds-skript repository with `git show`, so no
copy of the original is kept here and the comparison is always against a named commit.
Point the tool at that repository with $DS_SKRIPT, or let it use the local_hint in
sync/upstream.json.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from segment import Block, segment, segment_text  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SYNC = ROOT / "sync"


def _load(name: str) -> dict:
    return json.loads((SYNC / name).read_text())


def upstream_repo() -> Path:
    cfg = _load("upstream.json")
    candidate = os.environ.get("DS_SKRIPT") or cfg.get("local_hint", "../ds-skript")
    path = (ROOT / candidate).resolve() if not Path(candidate).is_absolute() else Path(candidate)
    if not (path / ".git").exists():
        raise SystemExit(
            f"no git repository at {path}. Set $DS_SKRIPT to the ds-skript checkout, "
            "or fix local_hint in sync/upstream.json."
        )
    return path


def german(file: str, commit: str) -> str:
    repo = upstream_repo()
    out = subprocess.run(
        ["git", "-C", str(repo), "show", f"{commit}:{file}"],
        capture_output=True, text=True,
    )
    if out.returncode:
        raise SystemExit(f"cannot read {file} at {commit[:8]} in {repo}:\n{out.stderr.strip()}")
    return out.stdout


def pairs() -> list[tuple[str, str]]:
    """(german file, english file) for everything that is actually mirrored."""
    return [(de, en) for de, en in _load("filemap.json")["map"].items() if en]


def dropped(de_file: str) -> dict[str, str]:
    """block id -> reason, for blocks deliberately absent from the English edition."""
    return {d["block"]: d["reason"] for d in _load("drops.json")["drops"].get(de_file, [])}


def added(en_file: str) -> dict[str, str]:
    """block id -> reason, for English blocks with no German counterpart (translator's notes)."""
    return {a["block"]: a["reason"] for a in _load("additions.json")["additions"].get(en_file, [])}


def expected_blocks(de_file: str, commit: str) -> list[Block]:
    drops = dropped(de_file)
    return [b for b in segment_text(de_file, german(de_file, commit)) if b.bid not in drops]


# --------------------------------------------------------------------------- align

def cmd_align() -> int:
    commit = _load("upstream.json")["commit"]
    bad = 0
    for de_file, en_file in pairs():
        want = expected_blocks(de_file, commit)
        path = ROOT / en_file
        if not path.exists():
            print(f"✗ {en_file}: missing")
            bad += 1
            continue
        have = segment(path)
        extra = added(en_file)
        paired = [b for b in have if b.bid not in extra]
        if len(want) != len(paired):
            print(f"✗ {en_file}: {len(paired)} translated blocks, expected {len(want)} "
                  f"({len(want) + len(dropped(de_file))} in {de_file}, "
                  f"{len(dropped(de_file))} dropped, {len(extra)} English-only)")
            bad += 1
            continue
        kinds = [(i, w, h) for i, (w, h) in enumerate(zip(want, paired)) if w.kind != h.kind]
        if kinds:
            i, w, h = kinds[0]
            print(f"✗ {en_file}: block {h.bid} is {h.kind}, the German block {w.bid} is {w.kind}")
            print(f"    German:  {w.preview()}")
            print(f"    English: {h.preview()}")
            bad += 1
            continue
        note = f", {len(extra)} English-only" if extra else ""
        print(f"✓ {en_file}: {len(paired)} blocks aligned{note}")
    print(f"-- {len(pairs()) - bad}/{len(pairs())} files aligned")
    return 1 if bad else 0


# ------------------------------------------------------------------------ manifest

def cmd_manifest() -> int:
    commit = _load("upstream.json")["commit"]
    (SYNC / "segments").mkdir(exist_ok=True)
    for de_file, en_file in pairs():
        drops = dropped(de_file)
        de_blocks = segment_text(de_file, german(de_file, commit))
        extra = added(en_file)
        en_blocks = [b for b in segment(ROOT / en_file) if b.bid not in extra] \
            if (ROOT / en_file).exists() else []
        entries, pos = [], 0
        for b in de_blocks:
            if b.bid in drops:
                entries.append({"de": b.bid, "kind": b.kind, "digest": b.digest,
                                "en": None, "dropped": drops[b.bid], "preview": b.preview()})
                continue
            en_bid = en_blocks[pos].bid if pos < len(en_blocks) else None
            entries.append({"de": b.bid, "kind": b.kind, "digest": b.digest,
                            "en": en_bid, "preview": b.preview()})
            pos += 1
        out = {"source": de_file, "target": en_file, "upstream": commit, "blocks": entries}
        (SYNC / "segments" / f"{de_file}.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(f"-- wrote {len(pairs())} manifests for upstream {commit[:8]}")
    return 0


def _worddiff(old: str, new: str) -> list[str]:
    """A word-level diff, so a one-word correction does not look like a rewritten paragraph."""
    sm = SequenceMatcher(None, old.split(), new.split(), autojunk=False)
    minus, plus = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        chunk_old, chunk_new = old.split()[i1:i2], new.split()[j1:j2]
        if tag == "equal":
            minus.extend(chunk_old)
            plus.extend(chunk_new)
        else:
            if chunk_old:
                minus.extend(["[-"] + chunk_old + ["-]"])
            if chunk_new:
                plus.extend(["{+"] + chunk_new + ["+}"])
    return ["- " + " ".join(minus).replace("[- ", "[-").replace(" -]", "-]"),
            "+ " + " ".join(plus).replace("{+ ", "{+").replace(" +}", "+}")]


# --------------------------------------------------------------------------- check

def cmd_check(new_commit: str | None) -> int:
    cfg = _load("upstream.json")
    old = cfg["commit"]
    repo = upstream_repo()
    if new_commit is None:
        new_commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                                    capture_output=True, text=True, check=True).stdout.strip()
    if new_commit == old:
        print(f"up to date: upstream is still {old[:8]}")
        return 0

    lines = [f"# Upstream changes {old[:8]} → {new_commit[:8]}", ""]
    stale_total = 0
    for de_file, en_file in pairs():
        man_path = SYNC / "segments" / f"{de_file}.json"
        if not man_path.exists():
            lines.append(f"## {de_file}\n\nNo manifest yet – chapter not translated.\n")
            continue
        man = json.loads(man_path.read_text())
        # The old German text comes from the pinned commit, not from the manifest: the
        # manifest only has to carry the German-block -> English-block mapping, and its
        # digests are there to prove it still describes that commit.
        old_blocks = segment_text(de_file, german(de_file, old))
        old_digests = [b.digest for b in old_blocks]
        if old_digests != [b["digest"] for b in man["blocks"]]:
            lines.append(f"## {de_file}\n\n**Manifest is out of date** for the pinned commit – "
                         "run `tools/sync.py manifest` before trusting this report.\n")
        new_blocks = segment_text(de_file, german(de_file, new_commit))
        new_digests = [b.digest for b in new_blocks]
        if old_digests == new_digests:
            continue

        lines.append(f"## {de_file} → {en_file}\n")
        en_blocks = {b.bid: b for b in segment(ROOT / en_file)} if (ROOT / en_file).exists() else {}
        sm = SequenceMatcher(None, old_digests, new_digests, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            stale_total += 1
            old_entries = [man["blocks"][k] for k in range(i1, i2)]
            new_texts = [new_blocks[k] for k in range(j1, j2)]
            anchor = (", ".join(f"`{b['de']}`" for b in old_entries) if old_entries
                      else f"after `{man['blocks'][i1 - 1]['de']}`" if i1 else "at the start")
            targets = [b for b in old_entries if b["en"] is not None]
            if targets:
                where = "English block(s) " + ", ".join(f"**{b['en']}**" for b in targets)
            elif old_entries:
                where = "_dropped from this edition: " + \
                        "; ".join(b.get("dropped", "?") for b in old_entries) + "_"
            else:
                where = "**new** – decide whether it belongs in this edition"
            lines.append(f"### {tag} – German block {anchor} – {where}\n")

            old_texts = [old_blocks[k] for k in range(i1, i2)]
            if tag == "replace" and len(old_texts) == len(new_texts):
                lines.append("What changed in the German:\n")
                lines.append("```diff")
                for a, b in zip(old_texts, new_texts):
                    lines.extend(_worddiff(a.text, b.text))
                lines.append("```\n")

            if new_texts:
                lines.append("German now reads:\n")
                lines.append("```md")
                lines.extend(b.text for b in new_texts)
                lines.append("```\n")

            for b in targets:
                cur = en_blocks.get(b["en"])
                lines.append(f"Current English block {b['en']}:\n")
                lines.append("```md")
                lines.append(cur.text if cur else "(not found – is the file still aligned?)")
                lines.append("```\n")
        lines.append("")

    report = "\n".join(lines) + "\n"
    (SYNC / "reports").mkdir(exist_ok=True)
    out = SYNC / "reports" / f"{new_commit[:8]}.md"
    out.write_text(report)
    print(report)
    print(f"-- {stale_total} stale region(s); report written to {out.relative_to(ROOT)}")
    print("-- after re-translating: bump sync/upstream.json and run `tools/sync.py manifest`")
    return 1 if stale_total else 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd = sys.argv[1]
    if cmd == "align":
        return cmd_align()
    if cmd == "manifest":
        return cmd_manifest()
    if cmd == "check":
        return cmd_check(sys.argv[2] if len(sys.argv) > 2 else None)
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
