"""Montagem da Escada dos Lutadores (Fase 1C).
5 degraus de 16x16 de mundo, largura 64 de mundo (256 px de arquivo).
Conecta o topo da galeria (+80) em Y=736 à base (0) em Y=816 no pátio.
Tamanho final: 256 x 480 px de arquivo.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c\test_escada_cut.png"
OUT_DIR = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c"

im = Image.open(SRC)
# O crop original tem largura 800 e altura 1120
escada_crop = im.crop((54, 34, 854, 1153))

# Redimensionar para a largura exata de 256 px (64 de mundo) e altura 480 px
escada_final = escada_crop.resize((256, 480), Image.LANCZOS)

# Garantir 0 resíduo de magenta
arr = np.array(escada_final).astype(np.float32)
r, g, b, a = arr[...,0], arr[...,1], arr[...,2], arr[...,3]
mag_mask = (r > 150) & (b > 150) & (g < 100) & (a > 0)
arr[mag_mask, 0] = arr[mag_mask, 1] * 1.1
arr[mag_mask, 2] = arr[mag_mask, 1] * 0.9

# Verificar apoio da base (os dois suportes inferiores tocam a base y=478..479)
escada_final = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
escada_final.save(os.path.join(OUT_DIR, "arena_escada_lutadores_v1.png"))
print("Escada dos lutadores salva:", escada_final.size, "bbox:", escada_final.getbbox())
