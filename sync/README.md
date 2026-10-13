# sync/

What keeps this edition tied to the German original.

| | |
|---|---|
| `upstream.json` | the ds-skript commit this edition corresponds to |
| `filemap.json` | German file -> English file; `null` means deliberately not mirrored |
| `progress.json` | per file: translated yet? style pass done yet? |
| `segments/` | the German block digests and the German -> English block mapping |
| `drops/<german-file>.json` | German blocks deliberately absent here, each with a reason |
| `additions/<english-file>.json` | English-only blocks (translator's notes), each with a reason |
| `check-ignore/<english-file>.json` | deliberate findings of `tools/check_english.py` |
| `notes/<english-file>.md` | what a chapter's translator wants merged: new glossary terms, figures to redraw, questions |
| `reports/` | staleness reports from `tools/sync.py check` |

One file per chapter on purpose: several translators work in parallel, and a shared JSON
file would be a merge conflict waiting to happen.
