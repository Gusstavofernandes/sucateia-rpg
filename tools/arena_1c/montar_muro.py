"""Montagem dos módulos do Muro de Contenção do Fosso (Fase 1C).
Escala: 4 px de arquivo = 1 px de mundo.
Módulos:
  - arena_muro_interno_norte_v1: face norte interna do fosso, 64x80 de mundo (256x320 px). Tiling perfeito no eixo X.
  - arena_muro_borda_topo_x_v1: borda superior do muro em X, 64x32 de mundo (256x128 px).
  - arena_muro_borda_topo_y_v1: borda superior do muro em Y, 32x64 de mundo (128x256 px).
  - arena_muro_canto_interno_v1: canto do muro, 32x32 de mundo (128x128 px).
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

SRC = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c\test_muro_cut.png"
OUT_DIR = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c"

im = Image.open(SRC)

# Extrair textura do fuste do muro (chapas rebitadas)
# y=200 a 700, x=300 a 850
wall_crop = im.crop((280, 200, 840, 720))
wall_face = wall_crop.resize((256, 320), Image.LANCZOS)

# Ajustar bordas esquerda e direita do wall_face para tiling sem costura
arr = np.array(wall_face).astype(np.float32)
# Misturar bordas esquerda e direita (8 px de transição) para costura perfeita de 0 px
seam_w = 12
for i in range(seam_w):
    alpha = i / float(seam_w)
    avg = arr[:, i, :] * (1 - alpha) + arr[:, 255 - seam_w + i, :] * alpha
    arr[:, i, :] = avg
    arr[:, 255 - seam_w + i, :] = avg

# Cantoneira de ferro escura nas extremidades verticais
wall_face_tiled = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
d = ImageDraw.Draw(wall_face_tiled)
# Reforço de cantoneira com rebites a cada 64 px
for ry in range(32, 320, 64):
    d.ellipse([1, ry-3, 7, ry+3], fill=(130, 100, 75, 255), outline=(20, 16, 12, 255))
    d.ellipse([249, ry-3, 255, ry+3], fill=(130, 100, 75, 255), outline=(20, 16, 12, 255))

wall_face_tiled.save(os.path.join(OUT_DIR, "arena_muro_interno_norte_v1.png"))
print("Muro interno norte salvo:", wall_face_tiled.size)

# 2. Borda superior reta em X (curb ledge com parafusos)
# y=52 a 160, x=250 a 1050
curb_crop = im.crop((260, 52, 1040, 160))
curb_x = curb_crop.resize((256, 128), Image.LANCZOS)
# Mistura para tiling no eixo X
arr_cx = np.array(curb_x).astype(np.float32)
for i in range(seam_w):
    alpha = i / float(seam_w)
    avg = arr_cx[:, i, :] * (1 - alpha) + arr_cx[:, 255 - seam_w + i, :] * alpha
    arr_cx[:, i, :] = avg
    arr_cx[:, 255 - seam_w + i, :] = avg
curb_x_tiled = Image.fromarray(arr_cx.clip(0, 255).astype(np.uint8))
curb_x_tiled.save(os.path.join(OUT_DIR, "arena_muro_borda_topo_x_v1.png"))
print("Muro borda topo X salvo:", curb_x_tiled.size)

# 3. Borda superior reta em Y (rotacionada e ajustada para 128x256 px)
curb_y = curb_x_tiled.rotate(90, expand=True).resize((128, 256), Image.LANCZOS)
curb_y.save(os.path.join(OUT_DIR, "arena_muro_borda_topo_y_v1.png"))
print("Muro borda topo Y salvo:", curb_y.size)

# 4. Canto do muro (128x128 px)
canto_muro = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
canto_muro.alpha_composite(curb_x_tiled.crop((0, 0, 128, 128)))
d_canto = ImageDraw.Draw(canto_muro)
# cantoneira em L de reforço no canto
d_canto.line([(0, 0), (127, 0)], fill=(30, 24, 20, 255), width=4)
d_canto.line([(0, 0), (0, 127)], fill=(30, 24, 20, 255), width=4)
d_canto.ellipse([10, 10, 20, 20], fill=(140, 110, 80, 255), outline=(20, 16, 12, 255))
canto_muro.save(os.path.join(OUT_DIR, "arena_muro_canto_interno_v1.png"))
print("Muro canto salvo:", canto_muro.size)
