"""Monta grade X e grade Y com cotas exatas (Fase 1B), texturas pintadas pelo gerador.
Projecao: frente 1:1 em z; profundidade projetada x0.5 na tela (16 de profundidade = 8 de tela).
S=8 px de arquivo por px de mundo na montagem; saida final = 4 px/mundo (reduz por 2)."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
SRC = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_grade_reta_x_v2_1792511279980.jpg"
OUT = r"c:\Users\Usuario\Documents\jogo\tools\arena_1b"
S = 8
src = Image.open(SRC).convert("RGB")      # 768 x 1376
rail_front = src.crop((70, 205, 690, 295))
rail_top   = ImageEnhance.Brightness(src.crop((70, 205, 690, 295))).enhance(1.30)
bar_tex    = src.crop((375, 420, 392, 1000))   # barra central
LINE = (22, 16, 12, 255)

def paste_tex(im, tex, x0, y0, x1, y1):
    t = tex.resize((x1-x0, y1-y0), Image.LANCZOS).convert("RGBA")
    im.alpha_composite(t, (x0, y0))

def outline(im, x0, y0, x1, y1, w=2):
    ImageDraw.Draw(im).rectangle([x0, y0, x1-1, y1-1], outline=LINE, width=w)

def grade_x():
    W, H = 64*S, (96+8)*S                         # 512 x 832
    im = Image.new("RGBA", (W, H), (0,0,0,0))
    # trilho de base: frente z0-8 -> y 768..832 ; topo (profundidade 16 -> 8) y 704..768
    paste_tex(im, rail_top,   0, 704, W, 768);  outline(im, 0, 704, W, 768)
    paste_tex(im, rail_front, 0, 768, W, 832);  outline(im, 0, 768, W, 832)
    # barras 4 de largura, centros 19/32/45, de y 128 a 736 (base apoiada no topo do trilho)
    for c in (19, 32, 45):
        x0 = (c-2)*S
        paste_tex(im, bar_tex, x0, 128, x0+4*S, 736)
        ImageDraw.Draw(im).rectangle([x0, 128, x0+4*S-1, 735], outline=LINE, width=2)
    # trilho de topo: frente z88-96 -> y 64..128 ; topo y 0..64
    paste_tex(im, rail_top,   0, 0,   W, 64);   outline(im, 0, 0, W, 64)
    paste_tex(im, rail_front, 0, 64,  W, 128);  outline(im, 0, 64, W, 128)
    return im

def grade_y():
    W, H = 16*S, (96+32)*S                        # 128 x 1024
    im = Image.new("RGBA", (W, H), (0,0,0,0))
    # trilho de base: topo y 704..960 (64 de comprimento -> 32 de tela), frente (extremo sul) y 960..1024
    paste_tex(im, rail_top,   0, 704, W, 960);  outline(im, 0, 704, W, 960)
    paste_tex(im, rail_front.resize((W, 64)), 0, 960, W, 1024); outline(im, 0, 960, W, 1024)
    # barras 4x4 em d = 19/32/45 do norte; base y = 704 + d*4 ; altura visivel 640
    for d in (19, 32, 45):
        yb = 704 + d*4
        paste_tex(im, bar_tex, 6*S, yb-640, 10*S, yb)
        ImageDraw.Draw(im).rectangle([6*S, yb-640, 10*S-1, yb-1], outline=LINE, width=2)
    # trilho de topo: topo y 0..256, frente (extremo sul) y 256..320
    paste_tex(im, rail_top,   0, 0,   W, 256);  outline(im, 0, 0, W, 256)
    paste_tex(im, rail_front.resize((W, 64)), 0, 256, W, 320); outline(im, 0, 256, W, 320)
    return im

def finalize(im, name, final):
    im = im.resize(final, Image.LANCZOS)
    a = np.array(im).astype(np.float32); a[..., 3] = np.clip((a[..., 3] - 64) * 2, 0, 255); a[a[..., 3] == 0] = 0
    im = Image.fromarray(a.astype(np.uint8))
    im.save(f"{OUT}\\{name}.png"); print(name, im.size, "bbox", im.getbbox())
    return im

finalize(grade_x(), "arena_grade_reta_x_v1", (256, 416))
finalize(grade_y(), "arena_grade_reta_y_v1", (64, 512))

