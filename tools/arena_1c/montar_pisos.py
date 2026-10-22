"""Montagem dos Pisos do Fosso e da Galeria (Fase 1C).
Escala: 4 px de arquivo = 1 px de mundo. Módulos de 64x64 de mundo (256x256 px de arquivo).
Módulos:
  - arena_piso_fosso_chapa_v1: piso do fosso em chapas de ferro rebitadas com solda e fuligem, seamless tiling.
  - arena_piso_fosso_grelha_v1: módulo do fosso com grelha central de drenagem e ralo para efluente.
  - arena_piso_galeria_tabuas_v1: piso da galeria em tábuas de madeira e chapas de ferro rebitadas.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

SRC_PISO = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c\test_piso_cut.png"
OUT_DIR = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c"

im_piso = Image.open(SRC_PISO)
# Crop central do piso (64, 64, 960, 960)
piso_crop = im_piso.crop((64, 64, 960, 960)).resize((256, 256), Image.LANCZOS)

# 1. Piso do Fosso (Chapa rebitada) com Seamless Tiling
arr = np.array(piso_crop).astype(np.float32)
seam = 16
# Blend horizontal edges
for i in range(seam):
    a = i / float(seam)
    arr[:, i, :] = arr[:, i, :] * a + arr[:, 256 - seam + i, :] * (1 - a)
    arr[:, 256 - seam + i, :] = arr[:, i, :]
# Blend vertical edges
for j in range(seam):
    a = j / float(seam)
    arr[j, :, :] = arr[j, :, :] * a + arr[256 - seam + j, :, :] * (1 - a)
    arr[256 - seam + j, :, :] = arr[j, :, :]

piso_chapa = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
piso_chapa.save(os.path.join(OUT_DIR, "arena_piso_fosso_chapa_v1.png"))
print("Piso fosso chapa salvo:", piso_chapa.size)

# 2. Piso do Fosso com Grelha / Ralo (Central 128x128 px)
piso_grelha = piso_chapa.copy()
d_gr = ImageDraw.Draw(piso_grelha)
# Moldura quadrada de ferro escuro no centro (64 a 192)
d_gr.rectangle([64, 64, 192, 192], fill=(25, 20, 16, 255), outline=(15, 12, 10, 255), width=3)
# Poço escuro do ralo
d_gr.ellipse([88, 88, 168, 168], fill=(5, 4, 3, 255))
# Barras da grelha de ferro (ranhuras de escoamento)
for gx in range(74, 186, 12):
    d_gr.line([(gx, 66), (gx, 190)], fill=(80, 68, 55, 255), width=4)
    d_gr.line([(gx-1, 66), (gx-1, 190)], fill=(40, 32, 25, 255), width=2)
# Parafusos nos 4 cantos da moldura da grelha
for bx in (68, 188):
    for by in (68, 188):
        d_gr.ellipse([bx-3, by-3, bx+3, by+3], fill=(150, 120, 90, 255), outline=(20, 16, 12, 255))

piso_grelha.save(os.path.join(OUT_DIR, "arena_piso_fosso_grelha_v1.png"))
print("Piso fosso grelha salvo:", piso_grelha.size)

# 3. Piso da Galeria (Tábuas de madeira escura com cinta de ferro)
im_galeria = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
d_gal = ImageDraw.Draw(im_galeria)

# Tábuas de madeira escura horizontais (4 tábuas de 64 px de altura)
wood_tones = [
    (48, 38, 30, 255),
    (42, 34, 26, 255),
    (52, 42, 32, 255),
    (38, 30, 24, 255)
]
for idx, wy in enumerate(range(0, 256, 64)):
    c = wood_tones[idx % 4]
    d_gal.rectangle([0, wy, 255, wy+63], fill=c, outline=(18, 14, 10, 255), width=2)
    # Textura sutil de veios da madeira
    for ly in range(wy+8, wy+60, 12):
        d_gal.line([(0, ly), (255, ly)], fill=(c[0]+12, c[1]+10, c[2]+8, 255), width=1)

# Cintas de ferro verticais nas extremidades e centro com rebites
for fx in (8, 128, 248):
    d_gal.rectangle([fx-8, 0, fx+7, 255], fill=(35, 28, 22, 255), outline=(15, 12, 10, 255), width=2)
    d_gal.line([(fx, 0), (fx, 255)], fill=(70, 58, 46, 255), width=2)
    for ry in range(16, 256, 32):
        d_gal.ellipse([fx-3, ry-3, fx+3, ry+3], fill=(140, 110, 80, 255), outline=(15, 12, 10, 255))

im_galeria.save(os.path.join(OUT_DIR, "arena_piso_galeria_tabuas_v1.png"))
print("Piso galeria tabuas salvo:", im_galeria.size)
