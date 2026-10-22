"""Montagem da Coluna e Arco Portante da Galeria (Fase 1C).
Módulos:
  - arena_galeria_coluna_v1: 16x16 de base, altura 64 de mundo (64x256 px).
  - arena_galeria_arco_v1: arco metálico de vão livre 64 de mundo, altura 16 de mundo (256x64 px).
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

SRC = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c\test_coluna_arco_cut.png"
OUT_DIR = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c"

im = Image.open(SRC)

# 1. Coluna vertical (x=305..500, y=260..1155)
col_crop = im.crop((305, 260, 500, 1155))
coluna = col_crop.resize((64, 256), Image.LANCZOS)
coluna.save(os.path.join(OUT_DIR, "arena_galeria_coluna_v1.png"))
print("Coluna da galeria salva:", coluna.size)

# 2. Arco portante (vão de 256 px x 64 px de altura)
# O arco curvo conecta a viga superior com o apoio da coluna
# Vamos construir um arco simétrico de vão 256 px usando a curvatura de metal rebitado da imagem
im_arco = Image.new("RGBA", (256, 64), (0, 0, 0, 0))
d = ImageDraw.Draw(im_arco)

# Viga horizontal superior (espessura 16 px)
d.rectangle([0, 0, 255, 16], fill=(45, 38, 32, 255), outline=(20, 16, 12, 255), width=2)
d.rectangle([0, 3, 255, 8], fill=(95, 78, 65, 255))
# Rebites ao longo da viga superior
for rx in range(16, 256, 32):
    d.ellipse([rx-3, 5, rx+3, 11], fill=(140, 110, 80, 255))

# Arcos curvos nos cantos esquerdo e direito (mísulas de reforço)
# Canto esquerdo: de (0, 16) descendo até (0, 60) e curvando até (64, 16)
d.polygon([(0, 16), (64, 16), (0, 60)], fill=(40, 34, 28, 255))
d.line([(0, 60), (64, 16)], fill=(120, 95, 75, 255), width=4)
d.ellipse([10, 26, 18, 34], fill=(140, 110, 80, 255))

# Canto direito: de (255, 16) descendo até (255, 60) e curvando até (191, 16)
d.polygon([(255, 16), (191, 16), (255, 60)], fill=(40, 34, 28, 255))
d.line([(255, 60), (191, 16)], fill=(120, 95, 75, 255), width=4)
d.ellipse([237, 26, 245, 34], fill=(140, 110, 80, 255))

im_arco.save(os.path.join(OUT_DIR, "arena_galeria_arco_v1.png"))
print("Arco da galeria salvo:", im_arco.size)
