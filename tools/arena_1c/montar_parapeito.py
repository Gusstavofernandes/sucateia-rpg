"""Montagem do Parapeito Gradeado da Galeria (Fase 1C).
Guarda-corpo metálico baixo montado no piso da galeria (cota +80, altura 32 de mundo).
Módulos:
  - arena_parapeito_grade_x_v1: 64x32 de mundo (256x128 px)
  - arena_parapeito_grade_y_v1: 16x64 de mundo (64x256 px)
  - arena_parapeito_canto_v1: 16x16 de mundo (64x64 px)
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

SRC_X = r"c:\Users\Usuario\Documents\jogo\tools\arena_1b\arena_grade_reta_x_v1.png"
OUT_DIR = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c"

grade_x = Image.open(SRC_X)
# grade_x tem tamanho 256 x 416 (topo y=0..64, base y=352..416)
# Extraímos o corrimão superior e o trilho inferior
top_rail = grade_x.crop((0, 0, 256, 48))
bot_rail = grade_x.crop((0, 368, 256, 416))
# Barra vertical
bar_tex = grade_x.crop((120, 64, 136, 350))

# 1. Parapeito Grade X (256 x 128 px)
im_px = Image.new("RGBA", (256, 128), (0, 0, 0, 0))
# Barras verticais mais curtas (centros em 76, 128, 180 px de arquivo -> 19, 32, 45 de mundo)
for cx in (76, 128, 180):
    b = bar_tex.resize((16, 80), Image.LANCZOS)
    im_px.alpha_composite(b, (cx - 8, 24))

im_px.alpha_composite(bot_rail.resize((256, 32), Image.LANCZOS), (0, 96))
im_px.alpha_composite(top_rail.resize((256, 32), Image.LANCZOS), (0, 0))

im_px.save(os.path.join(OUT_DIR, "arena_parapeito_grade_x_v1.png"))
print("Parapeito grade X salvo:", im_px.size)

# 2. Parapeito Grade Y (64 x 256 px)
im_py = Image.new("RGBA", (64, 256), (0, 0, 0, 0))
# Corrimão e trilho em perspectiva lateral
d = ImageDraw.Draw(im_py)
# Montante frontal e traseiro
d.rectangle([20, 20, 44, 235], fill=(45, 38, 32, 255), outline=(20, 16, 12, 255), width=2)
# Barra longitudinal intermediária
d.line([(32, 20), (32, 235)], fill=(120, 95, 75, 255), width=6)
# Rebites nos extremos
d.ellipse([26, 24, 38, 36], fill=(140, 110, 80, 255))
d.ellipse([26, 220, 38, 232], fill=(140, 110, 80, 255))
im_py.save(os.path.join(OUT_DIR, "arena_parapeito_grade_y_v1.png"))
print("Parapeito grade Y salvo:", im_py.size)

# 3. Parapeito Canto (64 x 64 px)
im_pc = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
d_c = ImageDraw.Draw(im_pc)
d_c.rectangle([16, 16, 48, 48], fill=(50, 42, 35, 255), outline=(20, 16, 12, 255), width=2)
d_c.ellipse([26, 26, 38, 38], fill=(140, 110, 80, 255), outline=(20, 16, 12, 255))
im_pc.save(os.path.join(OUT_DIR, "arena_parapeito_canto_v1.png"))
print("Parapeito canto salvo:", im_pc.size)
