"""Draw the small, transparent valve manifold needed by Fundo-Ferro.

This deliberately creates only the documented missing distribution assembly.
It is an RGBA fixture with declared pipe sockets and foot contacts; scene
placement and world-coordinate validation remain separate responsibilities.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/reconstruction/fundo_finish"
SCALE = 3
W, H = 256, 224


def q(points: list[tuple[float, float]]) -> list[tuple[int, int]]:
    return [(round(x * SCALE), round(y * SCALE)) for x, y in points]


def ellipse(draw: ImageDraw.ImageDraw, box: tuple[float, float, float, float], fill: str,
            outline: str | None = None, width: float = 1) -> None:
    draw.ellipse(tuple(round(v * SCALE) for v in box), fill=fill, outline=outline,
                 width=max(1, round(width * SCALE)))


def line(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], fill: str,
         width: float, joint: str = "curve") -> None:
    draw.line(q(points), fill=fill, width=max(1, round(width * SCALE)), joint=joint)


def valve_wheel(draw: ImageDraw.ImageDraw, cx: float, cy: float) -> None:
    # Three small gate wheels, with dark iron rims and restrained copper wear.
    ellipse(draw, (cx - 15, cy - 15, cx + 15, cy + 15), "#211f1c", "#171615", 2)
    ellipse(draw, (cx - 12, cy - 12, cx + 12, cy + 12), "#59432f", "#a46b3e", 2)
    ellipse(draw, (cx - 8, cy - 8, cx + 8, cy + 8), "#282522", "#c08a52", 1)
    for angle in (0, 60, 120):
        import math
        rad = math.radians(angle)
        dx, dy = math.cos(rad) * 9, math.sin(rad) * 9
        line(draw, [(cx - dx, cy - dy), (cx + dx, cy + dy)], "#c08a52", 2)
    ellipse(draw, (cx - 3, cy - 3, cx + 3, cy + 3), "#d1a166", "#2b2824", 1)


def gauge(draw: ImageDraw.ImageDraw, cx: float, cy: float, accent: str) -> None:
    ellipse(draw, (cx - 12, cy - 13, cx + 12, cy + 13), "#171716", "#b7844e", 2)
    ellipse(draw, (cx - 8, cy - 9, cx + 8, cy + 9), "#c3b59b", "#51473a", 1)
    line(draw, [(cx, cy), (cx + 4, cy - 5)], accent, 1.6)
    ellipse(draw, (cx - 1.5, cy - 1.5, cx + 1.5, cy + 1.5), "#3a332b")
    for x, y in ((-5, -5), (0, -7), (5, -5)):
        ellipse(draw, (cx + x - 0.7, cy + y - 0.7, cx + x + 0.7, cy + y + 0.7), "#51473a")


def make_asset() -> Image.Image:
    # Supersampling keeps the small pipe collars and gauge marks crisp in-game.
    size = (W * SCALE, H * SCALE)
    shadow = Image.new("RGBA", size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse((20 * SCALE, 181 * SCALE, 238 * SCALE, 216 * SCALE), fill=(5, 6, 6, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(5 * SCALE))

    im = Image.new("RGBA", size, (0, 0, 0, 0))
    im.alpha_composite(shadow)
    d = ImageDraw.Draw(im)

    # Four stone-and-iron bearing feet. Their lower edges are the contact row.
    for x, y, w, h in ((27, 176, 48, 28), (181, 176, 48, 28),
                       (79, 187, 44, 26), (133, 187, 44, 26)):
        d.polygon(q([(x + 2, y + 5), (x + w // 2, y), (x + w, y + 7),
                     (x + w - 3, y + h), (x + w // 2, y + h + 3), (x, y + h - 2)]),
                  fill="#292724", outline="#151514")
        d.polygon(q([(x + 6, y + 7), (x + w // 2, y + 3), (x + w - 5, y + 9),
                     (x + w - 8, y + 16), (x + 7, y + 15)]), fill="#6c604e")
        d.line(q([(x + 6, y + 8), (x + w // 2, y + 4), (x + w - 5, y + 10)]),
               fill="#a0835c", width=2 * SCALE)
        for bx in (x + 8, x + w - 8):
            ellipse(d, (bx - 2, y + 11, bx + 2, y + 15), "#b27a45", "#251f1b", 1)

    # Low salvage-steel deck, deliberately narrow and legible at game scale.
    d.polygon(q([(19, 167), (47, 149), (126, 141), (208, 151), (238, 169),
                 (210, 187), (127, 195), (47, 185)]), fill="#252321", outline="#111111")
    d.polygon(q([(28, 166), (52, 153), (127, 146), (202, 155), (229, 169),
                 (207, 181), (128, 188), (51, 179)]), fill="#514439", outline="#a16c41")
    d.line(q([(35, 166), (54, 157), (126, 151), (197, 159)]), fill="#a17c57", width=2*SCALE)
    d.line(q([(52, 179), (126, 186), (207, 177)]), fill="#2b2823", width=2*SCALE)
    for x, y in ((42, 168), (73, 158), (125, 154), (178, 161), (215, 170),
                 (65, 178), (126, 181), (189, 176)):
        ellipse(d, (x - 2, y - 2, x + 2, y + 2), "#c08a52", "#27221d", 1)

    # Feed trunk: the flange face is an explicit 18 px left inlet socket.
    line(d, [(1, 48), (27, 48), (48, 58), (208, 58)], "#171716", 20)
    line(d, [(1, 46), (27, 46), (49, 56), (207, 56)], "#5a432f", 15)
    line(d, [(2, 44), (28, 44), (50, 54), (207, 54)], "#a56a3c", 7)
    line(d, [(25, 41), (27, 47), (29, 53)], "#cc9a61", 2)
    line(d, [(205, 50), (207, 56), (209, 62)], "#c8955d", 2)
    for x in (28, 207):
        d.rounded_rectangle((round((x - 5) * SCALE), 39*SCALE, round((x + 5) * SCALE), 60*SCALE),
                            radius=2*SCALE, fill="#302c26", outline="#b47a47", width=2*SCALE)

    # Three controlled branches and a distinct low return header.
    for x in (72, 128, 184):
        line(d, [(x, 57), (x, 75)], "#191817", 13)
        line(d, [(x - 1, 57), (x - 1, 74)], "#9a653a", 7)
        line(d, [(x, 120), (x, 150)], "#181716", 14)
        line(d, [(x - 1, 121), (x - 1, 149)], "#a16b3d", 7)
        # Pipe saddle ties the vertical run back to the raised deck.
        d.polygon(q([(x - 11, 151), (x - 7, 145), (x + 7, 145), (x + 11, 151),
                     (x + 9, 157), (x - 9, 157)]), fill="#332f29", outline="#9a6e47")
        valve_wheel(d, x, 99)
        for yy in (76, 119):
            d.rounded_rectangle((round((x - 6) * SCALE), (yy - 3)*SCALE,
                                 round((x + 6) * SCALE), (yy + 3)*SCALE),
                                radius=2*SCALE, fill="#43372b", outline="#c28a50", width=SCALE)

    line(d, [(49, 150), (72, 158), (128, 163), (184, 158), (207, 151)], "#171716", 17)
    line(d, [(50, 148), (73, 156), (128, 161), (183, 156), (205, 149)], "#66503a", 11)
    line(d, [(56, 146), (78, 154), (128, 158), (178, 154), (200, 147)], "#a87547", 4)
    # The return run exits through its own right-hand coupling.
    line(d, [(202, 149), (235, 151)], "#171716", 17)
    line(d, [(203, 147), (235, 149)], "#66503a", 11)
    line(d, [(205, 145), (235, 147)], "#a87547", 4)

    # Gauge pods sit above the trunk; cyan and amber needles carry function,
    # while the restrained dials remain readable at the target zoom.
    for x, y in ((53, 30), (203, 32)):
        line(d, [(x, 43), (x, 48)], "#261f19", 7)
        line(d, [(x, 41), (x, 48)], "#9f6d43", 3)
    gauge(d, 53, 28, "#58a7a2")
    gauge(d, 203, 30, "#cb9049")

    # Sockets remain unobstructed on the silhouette edge for real placement.
    for x, y in ((10, 46), (246, 151)):
        ellipse(d, (x - 10, y - 10, x + 10, y + 10), "#171615", "#c18a52", 3)
        ellipse(d, (x - 5, y - 5, x + 5, y + 5), "#090b0b", "#564334", 1)
        ellipse(d, (x - 1.5, y - 1.5, x + 1.5, y + 1.5), "#40524d")

    # A few local mineral and oil flecks, confined to the assembly footprint.
    for x, y, color in ((53, 190, "#67715b"), (202, 190, "#6e6948"),
                        (31, 181, "#805738"), (226, 181, "#574b3b")):
        ellipse(d, (x - 2, y - 1, x + 2, y + 1), color)

    # Irregular oxidation and edge wear keep broad plates from reading as flat
    # vector fills; these flecks are clipped to the deck's real silhouette.
    deck_mask = Image.new("L", size, 0)
    ImageDraw.Draw(deck_mask).polygon(q([(19, 167), (47, 149), (126, 141), (208, 151),
                                         (238, 169), (210, 187), (127, 195), (47, 185)]), fill=255)
    wear = Image.new("RGBA", size, (0, 0, 0, 0))
    wd = ImageDraw.Draw(wear)
    random.seed(8361)
    for _ in range(180):
        x, y = random.randint(25, 232), random.randint(147, 190)
        color = random.choice(((169, 103, 54, 32), (36, 77, 72, 38),
                              (201, 157, 103, 24), (28, 26, 23, 48)))
        if random.random() < 0.68:
            wd.ellipse((x*SCALE, y*SCALE, (x+1)*SCALE, (y+1)*SCALE), fill=color)
        else:
            wd.line(((x*SCALE, y*SCALE), ((x+random.randint(2, 6))*SCALE,
                                          (y+random.choice((-1, 0, 1)))*SCALE)),
                    fill=color, width=SCALE)
    wear.putalpha(ImageChops.multiply(wear.getchannel("A"), deck_mask))
    im.alpha_composite(wear)

    return im.resize((W, H), Image.Resampling.LANCZOS)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    image = make_asset()
    target = OUT / "valve_manifold.png"
    image.save(target, optimize=True)
    alpha_bbox = image.getchannel("A").getbbox()
    from hashlib import sha256

    digest = sha256(target.read_bytes()).hexdigest()
    manifest = {
        "asset": "assets/reconstruction/fundo_finish/valve_manifold.png",
        "source": "tools/create_fundo_finish_assets.py",
        "role": "low hydraulic distribution manifold for existing Valvulas room",
        "canvas_px": [W, H],
        "alpha_bbox_px": list(alpha_bbox or ()),
        "anchor": "bottom_center; bearing foot row y=213",
        "sockets_px": {
            "feed_in": {"point": [10, 46], "diameter": 18, "direction": "west edge, eastbound"},
            "return_out": {"point": [246, 151], "diameter": 18, "direction": "east edge, eastbound"},
        },
        "bearing_footboxes_px": [
            [27, 176, 75, 204], [181, 176, 229, 204],
            [79, 187, 123, 213], [133, 187, 177, 213],
        ],
        "flow": "feed trunk -> three hand-wheel branches -> low return header",
        "new_collision": False,
        "sha256": digest,
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
