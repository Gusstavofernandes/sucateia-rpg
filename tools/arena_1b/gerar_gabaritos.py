"""Gabaritos da Fase 1B (Arena). Canvas 1152x2048 (9:16), fundo #FF00FF, guias de 1 px.
Convencao: tela_y = y_mundo (plano) ; z sobe 1:1 na tela. Escala S px de arquivo por px de mundo."""
from PIL import Image, ImageDraw
import json, os
OUT = r"c:\Users\Usuario\Documents\jogo\tools\arena_1b"
CW, CH = 1152, 2048
MAG = (255, 0, 255)

def canvas(): 
    im = Image.new("RGB", (CW, CH), MAG); return im, ImageDraw.Draw(im)

def box(d, x0, y0, x1, y1, c): d.rectangle([x0, y0, x1, y1], outline=c, width=1)

specs = {}

# ---------- GRADE X : footprint 64 x 16, altura 96, S=16 ----------
S = 16
im, d = canvas()
pw, ph = 64*S, (96+16)*S            # 1024 x 1792
x0, y0 = (CW-pw)//2, (CH-ph)//2     # 64, 128
x1, y1 = x0+pw, y0+ph               # 1088, 1920
box(d, x0, y0, x1-1, y1-1, (255,255,255))                       # caixa total
box(d, x0, y1-16*S, x1-1, y1-1, (0,255,255))                    # pegada 64x16
box(d, x0, y0, x0+8*S, y1-1, (255,80,80)); box(d, x1-8*S, y0, x1-1, y1-1, (255,80,80))  # zonas de pilar (8 de cada lado)
top_front = y1 - 96*S                                           # 384
box(d, x0, top_front, x1-1, top_front+8*S, (255,255,0))         # trilho topo (frente)
box(d, x0, y1-8*S, x1-1, y1-1, (255,255,0))                     # trilho base (frente)
bars = [19, 32, 45]
for c in bars:
    bx = x0 + c*S - 2*S
    box(d, bx, top_front+8*S, bx+4*S, y1-8*S, (0,255,0))
im.save(f"{OUT}\\gabarito_grade_x.png")
specs["grade_x"] = dict(canvas=(CW,CH), S=S, piece_box=(x0,y0,x1,y1), final_px=(256,448), world=(64,112),
                        bars_center_world=bars, bar_w_world=4, rail_h_world=8, pillar_zone_world=8)

# ---------- PILAR : footprint 16x16, altura 112, S=12 ----------
S = 12
im, d = canvas()
pw, ph = 16*S, (112+16)*S            # 192 x 1536
x0, y0 = (CW-pw)//2, (CH-ph)//2
x1, y1 = x0+pw, y0+ph
box(d, x0, y0, x1-1, y1-1, (255,255,255))
box(d, x0, y1-16*S, x1-1, y1-1, (0,255,255))                    # pegada 16x16
box(d, x0, y0+16*S, x1-1, y0+16*S+16*S, (255,255,0))            # capitel (16 de altura, ultimos 16 de z)
im.save(f"{OUT}\\gabarito_pilar.png")
specs["pilar"] = dict(canvas=(CW,CH), S=S, piece_box=(x0,y0,x1,y1), final_px=(64,512), world=(16,128))

# ---------- CANTO (NO) : pilar 16x16x112 + gusset de canto nas faces N e O, S=12 ----------
im, d = canvas()
box(d, x0, y0, x1-1, y1-1, (255,255,255))
box(d, x0, y1-16*S, x1-1, y1-1, (0,255,255))
box(d, x0, y0+16*S, x1-1, y0+16*S+16*S, (255,255,0))
box(d, x0, y1-16*S-24*S, x1-1, y1-16*S, (255,150,0))            # chapa de reforco (24 de altura) acima da base
im.save(f"{OUT}\\gabarito_canto_no.png")
specs["canto_no"] = dict(canvas=(CW,CH), S=S, piece_box=(x0,y0,x1,y1), final_px=(64,512), world=(16,128))

# ---------- GRADE Y : footprint 16 x 64, altura 96, S=12 ----------
S = 12
im, d = canvas()
pw, ph = 16*S, (96+64)*S             # 192 x 1920
x0, y0 = (CW-pw)//2, (CH-ph)//2
x1, y1 = x0+pw, y0+ph
box(d, x0, y0, x1-1, y1-1, (255,255,255))
box(d, x0, y1-64*S, x1-1, y1-1, (0,255,255))                    # pegada 16x64
box(d, x0, y1-8*S, x1-1, y1-1, (255,80,80)); box(d, x0, y1-64*S, x1-1, y1-56*S, (255,80,80))  # zonas de pilar
for c in bars:                                                  # barras: 4x4 de base, 96 de altura, em y = 19/32/45 a partir do norte
    by = y1 - 64*S + c*S
    box(d, x0+6*S, by-96*S, x0+10*S, by, (0,255,0))
im.save(f"{OUT}\\gabarito_grade_y.png")
specs["grade_y"] = dict(canvas=(CW,CH), S=S, piece_box=(x0,y0,x1,y1), final_px=(64,640), world=(16,160))

json.dump(specs, open(f"{OUT}\\fichas.json","w"), indent=1)
print(json.dumps(specs, indent=1))
