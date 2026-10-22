"""Pilar e canto montados por codigo (Fase 1B). Projecao oblíqua: frente 1:1, profundidade x0.5.
Pilar 16x16 de base, altura 112 (+8 de tela da face superior) -> final 64 x 480. S=8 na montagem, reduz por 2."""
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
OUT = r"c:\Users\Usuario\Documents\jogo\tools\arena_1b"
A = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b"
S = 8
LINE = (22, 16, 12, 255)
pil = Image.open(A + r"\arena_pilar_v1_1792511483229.jpg").convert("RGB")
shaft_tex = pil.crop((308, 480, 382, 900))                     # face esquerda lisa
dark_tex  = ImageEnhance.Brightness(shaft_tex).enhance(0.72)
cap_top   = ImageEnhance.Brightness(shaft_tex).enhance(1.35)
W, H = 16*S, (112+8)*S                                         # 128 x 960

def tex(im, t, x0, y0, x1, y1, line=True):
    im.alpha_composite(t.resize((x1-x0, y1-y0), Image.LANCZOS).convert("RGBA"), (x0, y0))
    if line: ImageDraw.Draw(im).rectangle([x0, y0, x1-1, y1-1], outline=LINE, width=2)

def rivets(im, y, n=4, r=5):
    d = ImageDraw.Draw(im)
    for i in range(n):
        x = int((i+0.5) * W / n)
        d.ellipse([x-r, y-r, x+r, y+r], fill=(70, 52, 40, 255), outline=LINE, width=2)
        d.ellipse([x-r+2, y-r+2, x, y], fill=(150, 110, 80, 255))

def pilar(canto=False):
    im = Image.new("RGBA", (W, H), (0,0,0,0))
    tex(im, cap_top,  0, 0, W, 64)                            # face superior (profundidade 16 -> 8 de tela)
    tex(im, dark_tex, 0, 64, W, 192);   rivets(im, 128)       # capitel z96-112
    tex(im, shaft_tex, 0, 192, W, 832)                        # fuste
    for z in (80, 40):                                        # dois colares z+0..8
        y = H - z*S - 8*S + 0
        tex(im, dark_tex, 0, y, W, y+8*S); rivets(im, y+4*S, 4, 4)
    if canto:                                                 # chapa de reforco z16-56, 4 de reentrancia visual
        y0, y1 = H - 56*S, H - 16*S
        tex(im, dark_tex, 0, y0, W, y1); rivets(im, y0+16, 4, 4); rivets(im, y1-16, 4, 4)
        tex(im, dark_tex, 0, y0+8*S, W, y0+8*S+8, line=False)
    tex(im, dark_tex, 0, H-16*S, W, H); rivets(im, H-8*S, 4, 5)   # base z0-16
    return im

def finalize(im, name):
    im = im.resize((64, 480), Image.LANCZOS)
    a = np.array(im).astype(np.float32); a[..., 3] = np.clip((a[..., 3] - 64) * 2, 0, 255); a[a[..., 3] == 0] = 0
    im = Image.fromarray(a.astype(np.uint8))
    im.save(f"{OUT}\\{name}.png"); print(name, im.size, im.getbbox())

finalize(pilar(False), "arena_pilar_v1")
finalize(pilar(True),  "arena_canto_v1")

