"""Generate the Open Graph social card: images/social-card.png, 1200x630.

The card is committed to the repository; this script exists so it can be regenerated
when the title or the brand colour changes, rather than redrawn by hand. It is never
run in CI -- CI only copies the committed PNG.

    python3 tools/social_card.py            # write images/social-card.png
    python3 tools/social_card.py --check    # byte-exact: needs Pillow, for local use
    python3 tools/social_card.py --verify   # shape only, stdlib: what CI can rely on

Why two checks. `--check` re-renders and compares bytes, which catches an edited PNG or a
changed generator -- but only where the rendering is identical, i.e. on a machine with the
same Pillow, zlib, freetype and fonts. It is useless in CI, where none of that is pinned.
`--verify` reads the PNG header with the standard library and asserts the card is present
and still 1200x630, which is the property that actually matters: an undersized card is the
bug this file exists to prevent, and it needs no dependency to detect.

Why a card at all: MyST derives og:image from the first image of a page, and where a page
has none it reaches for the first image of the project -- which was the CC BY-SA licence
button, 267x50, far below the 200x200 that Facebook and LinkedIn require and the 1200x630
they recommend. Most chapters therefore offered the licence badge as their preview card,
and at that size no card rendered at all. See SEO-NOTES.md.

Brand colour and the AA guarantee for white-on-petrol come from the German original's
BRANDING.md (#007d7e = oklch(0.52 0.12 195), white text 5.0:1).
"""

from __future__ import annotations

import sys
from pathlib import Path



ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images" / "social-card.png"

W, H = 1200, 630
BRAND = (0, 125, 126)        # #007d7e
TINT = (216, 245, 245)       # #d8f5f5, the light surface of the same hue
WHITE = (255, 255, 255)

# DejaVu ships with the system and covers "Völkel"; the site's Inter is a webfont and
# not needed here, because the card is rendered once and committed as a PNG.
FONTS = Path("/usr/share/fonts/truetype/dejavu")


def _png_size(data: bytes) -> tuple[int, int]:
    """Width and height out of a PNG's IHDR, without Pillow."""
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("not a PNG")
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def draw_card() -> Image.Image:
    img = Image.new("RGB", (W, H), BRAND)
    d = ImageDraw.Draw(img)

    pad = 76

    # Eyebrow: says "textbook", not "lecture notes of a particular course".
    f_eyebrow = font("DejaVuSans-Bold.ttf", 23)
    d.text((pad, pad), "OPEN TEXTBOOK  ·  CC BY-SA 4.0", font=f_eyebrow,
           fill=TINT)

    # Title, two lines, the second one lighter so the first reads as the name.
    f_t1 = font("DejaVuSans-Bold.ttf", 82)
    f_t2 = font("DejaVuSans.ttf", 46)
    d.text((pad, pad + 66), "Data Science", font=f_t1, fill=WHITE)
    d.text((pad, pad + 176), "from stochastics to machine", font=f_t2, fill=WHITE)
    d.text((pad, pad + 232), "learning with Python", font=f_t2, fill=WHITE)

    # The claim that distinguishes the book, in the words the reader would search for.
    f_claim = font("DejaVuSans-Bold.ttf", 34)
    y = pad + 330
    d.rectangle([pad, y, pad + 92, y + 5], fill=TINT)
    d.text((pad, y + 34), "Probability  ·  NumPy  ·  ML from scratch",
           font=f_claim, fill=TINT)

    # Byline at the foot: the author belongs here, not in the title. Deliberately the
    # author's own domain and not the site URL -- the edition moves hosts, and a URL
    # baked into a PNG goes stale silently.
    f_foot = font("DejaVuSans.ttf", 26)
    d.text((pad, H - pad - 30), "Konrad Völkel   ·   konradvoelkel.com",
           font=f_foot, fill=TINT)

    return img


def main() -> int:
    if "--verify" in sys.argv:
        if not OUT.exists():
            print(f"✗ {OUT.relative_to(ROOT)} is missing; run tools/social_card.py")
            return 1
        try:
            size = _png_size(OUT.read_bytes())
        except ValueError as exc:
            print(f"✗ {OUT.relative_to(ROOT)}: {exc}")
            return 1
        if size != (W, H):
            print(f"✗ {OUT.relative_to(ROOT)} is {size[0]}x{size[1]}, expected {W}x{H}. "
                  "Below 200x200 no platform renders a preview card at all.")
            return 1
        print(f"✓ {OUT.relative_to(ROOT)} is a {W}x{H} PNG")
        return 0

    from PIL import Image, ImageDraw, ImageFont  # noqa: F401  (only the two render paths)
    globals().update(Image=Image, ImageDraw=ImageDraw, ImageFont=ImageFont)
    img = draw_card()
    if "--check" in sys.argv:
        if not OUT.exists():
            print(f"✗ {OUT.relative_to(ROOT)} is missing; run tools/social_card.py")
            return 1
        from io import BytesIO
        buf = BytesIO()
        img.save(buf, "PNG")
        if buf.getvalue() != OUT.read_bytes():
            print(f"✗ {OUT.relative_to(ROOT)} is out of date; run tools/social_card.py")
            return 1
        print(f"✓ {OUT.relative_to(ROOT)} matches tools/social_card.py")
        return 0
    img.save(OUT, "PNG")
    print(f"✓ wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes, {W}x{H})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
