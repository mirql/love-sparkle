"""The love-sparkle logo: a sparkling pixel heart, and the word in a pixel font.

    python3 assets/logo/wordmark.py    # writes love-sparkle-{dark,light}.svg (heart and word),
                                       # love-sparkle-icon.svg (the heart alone) and social-preview.svg here
    rsvg-convert assets/logo/social-preview.svg -o assets/logo/social-preview.png
                                       # (or: magick assets/logo/social-preview.svg assets/logo/social-preview.png)

social-preview.png is the repository's social preview (Settings -> Social
preview: 1280x640, a PNG with its own background).

Letters (as appzones' wordmark): x-height rows 3-9, ascenders from row 0,
descenders rows 10-11, 2-pixel strokes, one empty column between letters,
a 2x2 dot on the baseline.
"""
from pathlib import Path

NAME = "love-sparkle"

GLYPHS = {  # rows 0..11, '#' = a pixel
    "l": ["##.", "##.", "##.", "##.", "##.", "##.", "##.", "##.", "###", ".##", "", ""],
    "o": ["", "", "", ".####.", "######", "##..##", "##..##", "##..##", "######", ".####.", "", ""],
    "v": ["", "", "", "##..##", "##..##", "##..##", "##..##", "######", ".####.", "..##..", "", ""],
    "e": ["", "", "", ".####.", "######", "##..##", "######", "##....", "######", ".#####", "", ""],
    "-": ["", "", "", "", "", "####", "####", "", "", "", "", ""],
    "s": ["", "", "", ".#####", "######", "##....", ".####.", "....##", "######", "#####.", "", ""],
    "p": ["", "", "", "#####.", "######", "##..##", "##..##", "##..##", "######", "#####.", "##", "##"],
    "a": ["", "", "", "#####.", "######", "....##", ".#####", "##..##", "######", ".#####", "", ""],
    "r": ["", "", "", "#####.", "######", "##..##", "##....", "##....", "##....", "##....", "", ""],
    "k": ["##....", "##....", "##....", "##..##", "##.##.", "####..", "####..", "##.##.", "##..##", "##..##", "", ""],
}

HEART = ["..####....####..", ".######..######.", "################", "################", "################",
         "################", ".##############.", "..############..", "...##########...", "....########....",
         ".....######.....", "......####......", ".......##......."]
SHINE = ["##.", "#..", "#.."]
SPARKLE_BIG = [".....#.....", ".....#.....", ".....#.....", "....###....", "...#####...", "###########",
               "...#####...", "....###....", ".....#.....", ".....#.....", ".....#....."]
SPARKLE_MID = ["..#..", "..#..", "#####", "..#..", "..#.."]
SPARKLE_SMALL = [".#.", "###", ".#."]

# "love" and the heart in pink (deeper on the heart's lower right), "-" muted,
# "sparkle" in the text colour, gold sparkles, the pink dot
THEMES = {
    "dark": {"pink": "#ff7cc6", "deep": "#e0499b", "shine": "#ffffff", "gold": "#f9e2af",
             "dash": "#8a7fa8", "text": "#f2ebff"},
    "light": {"pink": "#e0499b", "deep": "#b8327a", "shine": "#ffffff", "gold": "#df8e1d",
              "dash": "#8a7fa8", "text": "#2a2540"},
}

HEART_W, HEART_H = 26, 22  # the heart with its sparkles, in cells
WORD_X, WORD_Y = 28, 9     # where the word starts, next to the heart


def put(rects: list[str], rows: list[str], x: int, y: int, fill: str) -> None:
    for dy, row in enumerate(rows):
        for dx, c in enumerate(row):
            if c == "#":
                rects.append(f'<rect x="{x + dx}" y="{y + dy}" width="1.02" height="1.02" fill="{fill}"/>')


def heart(t: dict) -> list[str]:
    """The sparkling heart, in a HEART_W x HEART_H box."""
    rects, hx, hy = [], 4, 8
    for dy, row in enumerate(HEART):
        cells = [i for i, c in enumerate(row) if c == "#"]
        for i in cells:
            deep = (i in cells[-3:] and dy > 1) or dy >= 10
            rects.append(f'<rect x="{hx + i}" y="{hy + dy}" width="1.02" height="1.02" '
                         f'fill="{t["deep"] if deep else t["pink"]}"/>')
    put(rects, SHINE, hx + 3, hy + 2, t["shine"])
    put(rects, SPARKLE_BIG, hx + 11, hy - 7, t["gold"])
    put(rects, SPARKLE_MID, hx - 4, hy + 9, t["gold"])
    put(rects, SPARKLE_SMALL, hx - 3, hy - 3, t["gold"])
    put(rects, SPARKLE_SMALL, hx + 18, hy + 9, t["gold"])
    return rects


def logo(theme: str) -> tuple[list[str], int]:
    """The heart and the word: rects and width in cells (HEART_H high)."""
    t = THEMES[theme]
    rects, x = heart(t), WORD_X
    fills = [t["pink"]] * 4 + [t["dash"]] + [t["text"]] * 7
    for ch, fill in zip(NAME, fills):
        put(rects, GLYPHS[ch], x, WORD_Y, fill)
        x += max(len(r) for r in GLYPHS[ch]) + 1
    put(rects, ["##", "##"], x, WORD_Y + 8, t["pink"])
    return rects, x + 2


def svg(theme: str) -> str:
    rects, width = logo(theme)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {width + 2} {HEART_H + 2}" '
            f'width="{(width + 2) * 8}" height="{(HEART_H + 2) * 8}" role="img" aria-label="{NAME}" '
            f'shape-rendering="crispEdges">{"".join(rects)}</svg>\n')


def icon() -> str:
    """The heart alone, square, on no background (works on dark and light)."""
    side = HEART_H + 4
    x0, y0 = (HEART_W - side) / 2, -2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {side} {side}" width="{side * 8}" '
            f'height="{side * 8}" role="img" aria-label="{NAME}" shape-rendering="crispEdges">'
            f'{"".join(heart(THEMES["light"]))}</svg>\n')


TAGLINE = "A tiny sparkle of love, the same text in every language"


def social() -> str:
    """1280x640, dark background: the logo and the tagline."""
    rects, width = logo("dark")
    cell = 10
    x0 = (1280 - width * cell) / 2
    y0 = 170
    font = "'JetBrains Mono', 'Cascadia Code', monospace"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="640" viewBox="0 0 1280 640">'
            f'<rect width="1280" height="640" fill="#0d1117"/>'
            f'<g transform="translate({x0} {y0}) scale({cell})" shape-rendering="crispEdges">{"".join(rects)}</g>'
            f'<text x="640" y="490" text-anchor="middle" font-family="{font}" font-size="26" '
            f'fill="#c9d1d9">{TAGLINE}</text></svg>\n')


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    for theme in THEMES:
        (here / f"{NAME}-{theme}.svg").write_text(svg(theme))
    (here / f"{NAME}-icon.svg").write_text(icon())
    (here / "social-preview.svg").write_text(social())
