"""Montagem dos módulos da Plateia (bancadas norte e camarote) e Casa de Controle (mesa de alavancas e painel).
Fase 1D da Arena de Fundo-Ferro.
Escala: 4 px de arquivo = 1 px de mundo.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance

DIR_1D = r"c:\Users\Usuario\Documents\jogo\tools\arena_1d"

# 1. BANCADAS NORTE ESCALONADAS (arena_plateia_bancada_modulo_v1.png)
# Módulo de 64 px de mundo (256 px de arquivo) de largura x 384 px de altura (3 degraus de 32 de mundo)
im_bancada = Image.new("RGBA", (256, 384), (0, 0, 0, 0))
d_b = ImageDraw.Draw(im_bancada)

# 3 degraus escalonados (Degrau 3 ao fundo, Degrau 2 no meio, Degrau 1 à frente)
# Degrau 3 (cota +128): Y tela 0 a 128
# Degrau 2 (cota +112): Y tela 128 a 256
# Degrau 1 (cota +96): Y tela 256 a 384
steps = [
    (0, 128, (42, 34, 28, 255), (85, 68, 52, 255)),    # Degrau 3 (+128)
    (128, 256, (48, 38, 30, 255), (95, 78, 60, 255)),  # Degrau 2 (+112)
    (256, 384, (54, 44, 34, 255), (105, 86, 68, 255))  # Degrau 1 (+96)
]

for y0, y1, riser_col, tread_col in steps:
    # Espelho vertical do degrau (tábua / chapa de ferro)
    d_b.rectangle([0, y1 - 48, 255, y1 - 1], fill=riser_col, outline=(20, 16, 12, 255), width=2)
    # Suportes verticais de ferro com rebites
    for sx in (16, 128, 240):
        d_b.rectangle([sx - 6, y1 - 48, sx + 5, y1 - 1], fill=(30, 24, 20, 255), outline=(15, 12, 10, 255), width=1)
        d_b.ellipse([sx - 3, y1 - 36, sx + 2, y1 - 30], fill=(130, 105, 80, 255))
        d_b.ellipse([sx - 3, y1 - 16, sx + 2, y1 - 10], fill=(130, 105, 80, 255))
    
    # Assento / Piso do degrau (madeira envelhecida com veios)
    d_b.rectangle([0, y0, 255, y1 - 48], fill=tread_col, outline=(22, 16, 12, 255), width=2)
    for vy in range(y0 + 12, y1 - 48, 16):
        d_b.line([(0, vy), (255, vy)], fill=(tread_col[0] + 12, tread_col[1] + 10, tread_col[2] + 8, 255), width=1)
    # Cintas de reforço de ferro nos assentos
    for sx in (16, 128, 240):
        d_b.rectangle([sx - 6, y0, sx + 5, y1 - 48], fill=(35, 28, 22, 255), outline=(15, 12, 10, 255), width=1)

# Seamless tiling horizontal: garantir que as bordas esquerda e direita coincidam exatamente
arr_b = np.array(im_bancada).astype(np.float32)
seam = 12
for i in range(seam):
    alpha = i / float(seam)
    avg = arr_b[:, i, :] * (1 - alpha) + arr_b[:, 255 - seam + i, :] * alpha
    arr_b[:, i, :] = avg
    arr_b[:, 255 - seam + i, :] = avg
im_bancada = Image.fromarray(arr_b.clip(0, 255).astype(np.uint8))
im_bancada.save(os.path.join(DIR_1D, "arena_plateia_bancada_modulo_v1.png"))
print("Bancada norte salva:", im_bancada.size)

# 2. CAMAROTE VIP DOS APOSTADORES (arena_plateia_camarote_guarda_corpo_v1.png)
# 96x64 de mundo -> 384x256 px de arquivo
im_camarote = Image.new("RGBA", (384, 256), (0, 0, 0, 0))
d_cam = ImageDraw.Draw(im_camarote)

# Piso elevado de madeira nobre escura
d_cam.rectangle([0, 100, 383, 255], fill=(45, 34, 26, 255), outline=(18, 14, 10, 255), width=2)

# Guarda-corpo de ferro trabalhado com acolchoamento de couro carmesim desgastado
# Base de ferro
d_cam.rectangle([10, 120, 373, 220], fill=(32, 26, 20, 255), outline=(15, 12, 10, 255), width=2)
# Grades ornamentadas do camarote
for cx in range(30, 360, 24):
    d_cam.line([(cx, 130), (cx, 210)], fill=(75, 62, 50, 255), width=4)
    d_cam.ellipse([cx - 4, 165, cx + 4, 175], fill=(135, 110, 80, 255))
# Apoio acolchoado de couro superior (estofado vermelho escuro com costuras capitonê)
d_cam.rectangle([6, 100, 377, 130], fill=(95, 32, 28, 255), outline=(25, 12, 10, 255), width=3)
d_cam.rectangle([10, 103, 373, 112], fill=(130, 48, 40, 255))
for tx in range(20, 365, 32):
    d_cam.ellipse([tx - 2, 112, tx + 2, 118], fill=(50, 15, 12, 255)) # Botões de capitonê

im_camarote.save(os.path.join(DIR_1D, "arena_plateia_camarote_guarda_corpo_v1.png"))
print("Camarote salvo:", im_camarote.size)

# 3. MESA DE ALAVANCAS DE CONTROLE (arena_controle_mesa_alavancas_v1.png)
# 64x32 de mundo -> 256x128 px de arquivo. 4 alavancas industriais pesadas.
im_mesa = Image.new("RGBA", (256, 128), (0, 0, 0, 0))
d_m = ImageDraw.Draw(im_mesa)

# Corpo da bancada de ferro fundido com pés aparafusados
d_m.rectangle([16, 60, 239, 120], fill=(40, 34, 28, 255), outline=(18, 14, 10, 255), width=3)
d_m.rectangle([24, 66, 231, 80], fill=(65, 54, 45, 255))
for bx in (24, 88, 152, 216):
    d_m.ellipse([bx - 3, 110, bx + 3, 116], fill=(140, 110, 80, 255))

# 4 ranhuras mecânicas onde as alavancas deslizam
lever_x_positions = [48, 104, 160, 216]
lever_labels = ["AGUA", "ELETR", "DRENO", "VAPOR"]
lever_colors = [(50, 120, 180), (70, 200, 220), (80, 140, 70), (220, 140, 50)]

for idx, lx in enumerate(lever_x_positions):
    # Ranhura vertical
    d_m.rectangle([lx - 6, 45, lx + 6, 85], fill=(12, 10, 8, 255), outline=(25, 20, 16, 255), width=1)
    
    # Haste da alavanca de ferro (inclinada, em posição DESLIGADA / neutra)
    d_m.line([(lx, 75), (lx - 8, 20)], fill=(120, 105, 90, 255), width=5)
    d_m.line([(lx - 1, 75), (lx - 9, 20)], fill=(160, 145, 130, 255), width=2)
    
    # Manopla de latão / esfera no topo com indicador de cor do sistema
    c = lever_colors[idx]
    d_m.ellipse([lx - 14, 12, lx - 2, 24], fill=c, outline=(20, 16, 12, 255), width=2)
    d_m.ellipse([lx - 11, 14, lx - 6, 19], fill=(240, 240, 240, 255)) # Reflexo

im_mesa.save(os.path.join(DIR_1D, "arena_controle_mesa_alavancas_v1.png"))
print("Mesa de alavancas salva:", im_mesa.size)

# 4. PAINEL DE MANÔMETROS E MOSTRADORES (arena_controle_painel_manometros_v1.png)
# 64x48 de mundo -> 256x192 px de arquivo
im_painel = Image.new("RGBA", (256, 192), (0, 0, 0, 0))
d_p = ImageDraw.Draw(im_painel)

# Caixa de ferro do painel
d_p.rectangle([12, 12, 243, 179], fill=(35, 30, 24, 255), outline=(16, 12, 10, 255), width=3)
# Parafusos no perímetro
for px in (20, 128, 235):
    for py in (20, 171):
        d_p.ellipse([px-3, py-3, px+3, py+3], fill=(130, 105, 80, 255))

# 4 manômetros circulares de pressão e voltagem
gauges = [(56, 60), (128, 60), (200, 60), (92, 130)]
for gx, gy in gauges:
    # Borda de latão
    d_p.ellipse([gx - 26, gy - 26, gx + 26, gy + 26], fill=(140, 110, 60, 255), outline=(20, 16, 12, 255), width=2)
    # Fundo do mostrador de papel envelhecido
    d_p.ellipse([gx - 22, gy - 22, gx + 22, gy + 22], fill=(225, 215, 190, 255), outline=(40, 30, 20, 255), width=1)
    # Marcas da escala
    d_p.arc([gx - 18, gy - 18, gx + 18, gy + 18], start=135, end=405, fill=(40, 30, 20, 255), width=2)
    # Agulha indicadora em zero (desligado)
    d_p.line([(gx, gy), (gx - 14, gy + 4)], fill=(160, 20, 20, 255), width=2)
    # Pino central
    d_p.ellipse([gx - 3, gy - 3, gx + 3, gy + 3], fill=(20, 16, 12, 255))

# Tubo de vidro de nível de fluido vertical
d_p.rectangle([170, 105, 190, 165], fill=(20, 25, 30, 255), outline=(130, 105, 60, 255), width=2)
# Menisco de líquido âmbar baixo
d_p.rectangle([173, 140, 187, 162], fill=(190, 120, 40, 200))

im_painel.save(os.path.join(DIR_1D, "arena_controle_painel_manometros_v1.png"))
print("Painel de manômetros salvo:", im_painel.size)
