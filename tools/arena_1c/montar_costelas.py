"""Montagem das Costelas de Cobertura da Redoma (Fase 1C).
- Costela transversal: arco fino de ferro rebitado cobrindo o vão de Y=384 a Y=640 (profundidade 256 de mundo -> 128 px de tela; 512 px de arquivo). Pé em +176, coroa em +224 (elevação 48 de mundo -> 192 px de arquivo).
- Espinha longitudinal: viga fina superior em Y=512 que amarra as costelas.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

OUT_DIR = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c"
cut_col = Image.open(r"c:\Users\Usuario\Documents\jogo\tools\arena_1c\test_coluna_arco_cut.png")
# Pega textura do arco curvo da coluna
arch_tex = cut_col.crop((400, 300, 780, 800))

# 1. Costela transversal (arco fino em 2.5D)
# Largura no arquivo: 16 de mundo (64 px)
# Altura no arquivo: profundidade 128 px de tela + elevação 192 px = 320 px de tela (80 de mundo).
# Mas como ela vai de Y=384 a Y=640 (256 de mundo = 128 px de tela) e sobe 192 px:
W, H = 64, 400
im_arco = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(im_arco)

# Traçar arco parabólico fino
# Base norte em y=208, topo em y=16, base sul em y=336
points = []
for t in np.linspace(0, 1, 60):
    # Projeção oblíqua de Y (0 a 1 -> tela Y_base a Y_sul) e Z (arco parabólico)
    y_screen = 208 + t * 128 - 4 * t * (1 - t) * 192
    x_screen = 32 + np.sin(t * np.pi) * 2
    points.append((x_screen, y_screen))

# Desenhar costela com espessura 6 px de ferro escuro com rebites
for i in range(len(points) - 1):
    p1, p2 = points[i], points[i+1]
    d.line([p1, p2], fill=(45, 38, 32, 255), width=8)
    d.line([p1, p2], fill=(85, 70, 58, 255), width=4)
    if i % 8 == 0:
        # rebite
        d.ellipse([p1[0]-3, p1[1]-3, p1[0]+3, p1[1]+3], fill=(140, 110, 85, 255))

im_arco.save(os.path.join(OUT_DIR, "arena_costela_arco_v1.png"))
print("Costela arco salva:", im_arco.size)

# 2. Espinha longitudinal (módulo de 64 px de mundo -> 256 px de arquivo)
# Barra fina de ferro rebitada de 256 x 32 px
im_espinha = Image.new("RGBA", (256, 32), (0, 0, 0, 0))
d_esp = ImageDraw.Draw(im_espinha)
d_esp.rectangle([0, 8, 255, 23], fill=(45, 38, 32, 255), outline=(25, 20, 16, 255), width=2)
d_esp.rectangle([0, 11, 255, 17], fill=(85, 72, 60, 255))
# Rebites espaçados a cada 32 px
for rx in range(16, 256, 32):
    d_esp.ellipse([rx-3, 13, rx+3, 19], fill=(140, 110, 85, 255))

im_espinha.save(os.path.join(OUT_DIR, "arena_costela_espinha_v1.png"))
print("Costela espinha salva:", im_espinha.size)
