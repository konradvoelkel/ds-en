#!/usr/bin/env python3
"""Give the LaTeX export a raster it can read, for the four figures that are WebP.

    python3 tools/webp_for_pdf.py prepare   # before `myst build --pdf`
    python3 tools/webp_for_pdf.py restore   # after it, before `myst build --html`

`prepare` writes a PNG beside each WebP the book references and repoints the
references at it; `restore` puts the references back and deletes the PNGs. The web
build must never see the PNGs -- the WebP is 89% smaller and that is why §9d chose
it -- so this runs either side of the PDF export only.


Why this exists
---------------

xelatex cannot read WebP, and mystmd does not convert it for the LaTeX export. It
converts the other two awkward formats in this book: in the export directory
`pca-variation-<hash>.gif` sits beside a `.png` twin MyST made, and the four SVGs
each have a `.pdf` twin. The four WebPs get no twin at all and are handed to
`\\includegraphics` as `.webp`, which fails as

    ./ds-en-descriptive-statistics.tex:7: LaTeX Error: Cannot determine size of graphic

four times, once per WebP. latexmk runs in force mode, so it carries on and emits a
stub; MyST reports success over it. That is how `c8c48bc` turned a complete 15 MB
PDF into 1642 kB on 2026-10-18 without failing anything -- see SEO-NOTES.md §28,
and the floor in `pages.yml` that now fails on it.

ImageMagick is deliberately not used, although `pages.yml` installs it and the TeX
step's comment credits it with exactly this job. Locally it does the conversion
fine, but its WebP support on Ubuntu is a delegate to the `dwebp` binary from the
`webp` package, which `--no-install-recommends` does not pull in -- so whether it
works on the runner depends on a package nobody listed. That is the shape of bug
that cost this repository the librsvg2-bin run, and once is enough. Pillow carries
libwebp inside its own wheel, is already pinned in requirements.txt for
`optimize_images.py`, and so cannot be absent on a runner where this step ran.


What it refuses to do
---------------------

* Touch a WebP that already has a committed PNG twin. That twin would be a figure
  in its own right, and `restore` deletes what `prepare` wrote -- so it must only
  ever write files that did not exist.
* Guess which files to edit. The sources come from the `toc` in myst.yml, the same
  list the build uses, so a chapter added later is covered without editing a list
  here.
* Leave the tree half-converted. `restore` re-reads the manifest `prepare` wrote and
  fails if a source file changed underneath it, rather than pasting a stale copy
  back over someone's edit.
"""
import hashlib
import json
import pathlib
import sys

MANIFEST = pathlib.Path("_build/webp-for-pdf.json")


def toc_sources(root: pathlib.Path) -> list[pathlib.Path]:
    """Every source file the book is built from, read out of myst.yml's toc."""
    import yaml

    cfg = yaml.safe_load((root / "myst.yml").read_text(encoding="utf-8"))
    files: list[pathlib.Path] = []

    def walk(entries):
        for entry in entries or []:
            if not isinstance(entry, dict):
                continue
            if "file" in entry:
                files.append(root / entry["file"])
            walk(entry.get("children"))

    walk(cfg.get("project", {}).get("toc"))
    if not files:
        sys.exit("::error::myst.yml has no toc entries with a `file`; refusing to guess")
    return files


def digest(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(root: pathlib.Path) -> None:
    from PIL import Image

    sources = [f for f in toc_sources(root) if f.exists()]
    # Which WebPs are actually referenced, and from where. Matched as the literal
    # `images/<name>.webp` that appears in the Markdown and, identically, inside the
    # JSON of a notebook cell -- so one replacement covers both file types.
    webps = sorted({p for p in (root / "images").glob("*.webp")})
    referenced: dict[pathlib.Path, list[pathlib.Path]] = {}
    for webp in webps:
        ref = f"images/{webp.name}"
        users = [f for f in sources if ref in f.read_text(encoding="utf-8")]
        if users:
            referenced[webp] = users

    if not referenced:
        print("webp_for_pdf: no WebP is referenced by the book; nothing to do")
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps({"sources": {}, "written": []}), encoding="utf-8")
        return

    written: list[str] = []
    for webp in referenced:
        png = webp.with_suffix(".png")
        if png.exists():
            sys.exit(
                f"::error::{png} already exists, so it is a committed figure and not "
                f"ours to overwrite; {webp.name} needs a different name for its twin"
            )
        with Image.open(webp) as im:
            # The alpha channel goes: a PDF figure is composited on white paper, and
            # optimize_images.py's own finding is that RGBA costs size for nothing in
            # a plot. Flattened explicitly rather than by `convert("RGB")`, which
            # would multiply by a black background wherever the figure is transparent.
            if im.mode in ("RGBA", "LA", "P"):
                im = im.convert("RGBA")
                flat = Image.new("RGB", im.size, (255, 255, 255))
                flat.paste(im, mask=im.split()[-1])
                out = flat
            else:
                out = im.convert("RGB")
            out.save(png, format="PNG", optimize=True)
        written.append(str(png.relative_to(root)))
        print(f"  {webp.name} -> {png.name}  ({out.width}x{out.height}, "
              f"{png.stat().st_size // 1024} kB)")

    # The sources, with the references repointed and their pre-edit digests recorded
    # so `restore` can prove it is putting back what it took.
    manifest: dict[str, dict] = {"sources": {}, "written": written}
    edited = 0
    for f in sorted({u for users in referenced.values() for u in users}):
        text = f.read_text(encoding="utf-8")
        before = digest(f)
        for webp in referenced:
            text = text.replace(f"images/{webp.name}", f"images/{webp.stem}.png")
        rel = str(f.relative_to(root))
        manifest["sources"][rel] = {"before": before, "after": None}
        f.write_text(text, encoding="utf-8")
        manifest["sources"][rel]["after"] = digest(f)
        edited += 1

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(f"webp_for_pdf: {len(written)} PNG twins written, {edited} source files "
          f"repointed; manifest at {MANIFEST}")


def restore(root: pathlib.Path) -> None:
    if not MANIFEST.exists():
        sys.exit(f"::error::{MANIFEST} is missing; `prepare` did not run, or ran in "
                 f"another working directory")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    for rel, state in sorted(manifest["sources"].items()):
        f = root / rel
        if digest(f) != state["after"]:
            sys.exit(f"::error::{rel} changed after `prepare` rewrote it; refusing to "
                     f"paste a stale copy over it. Restore it with "
                     f"`git checkout -- {rel}` and check what else edited it.")
        text = f.read_text(encoding="utf-8")
        for png in manifest["written"]:
            stem = pathlib.Path(png).stem
            text = text.replace(f"images/{stem}.png", f"images/{stem}.webp")
        f.write_text(text, encoding="utf-8")
        if digest(f) != state["before"]:
            sys.exit(f"::error::{rel} did not come back byte-identical; it is now "
                     f"{digest(f)[:12]} and was {state['before'][:12]}")

    for png in manifest["written"]:
        (root / png).unlink(missing_ok=True)

    # The postcondition that matters to the next step: the web build must find no
    # trace of this, because a PNG where the HTML expects a WebP is 89% of a figure's
    # weight back, and a reference to a file we just deleted is a 404.
    for f in toc_sources(root):
        if f.exists():
            text = f.read_text(encoding="utf-8")
            for png in manifest["written"]:
                if f"images/{pathlib.Path(png).stem}.png" in text:
                    sys.exit(f"::error::{f.name} still points at "
                             f"images/{pathlib.Path(png).stem}.png after restore")
    MANIFEST.unlink()
    print(f"webp_for_pdf: {len(manifest['sources'])} source files restored byte-"
          f"identical, {len(manifest['written'])} PNG twins deleted")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "restore"):
        sys.exit(__doc__)
    {"prepare": prepare, "restore": restore}[sys.argv[1]](pathlib.Path.cwd())
