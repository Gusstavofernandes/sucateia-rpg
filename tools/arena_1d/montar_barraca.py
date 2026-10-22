"""Montagem da Barraca de Apostas e seus componentes (Fase 1D).
Regras estritas:
  - Dimensões em múltiplos de 16 px de mundo (escala 4x para arquivo).
  - SEM texto/números desenhados na imagem do quadro de odds (serão Labels no Godot).
  - Fundo transparente, 0% magenta.
  - Toldo de pano remendado, balcão de madeira e ferro com janela de atendimento.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

DIR_1D = r"c:\Users\Usuario\Documents\jogo\tools\arena_1d"
OUT_PROPS = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props"

# 1. BARRACA DE APOSTAS PRINCIPAL (arena_barraca_apostas_v1.png)
# Largura: 96 de mundo (384 px de arquivo), Altura: 96 de mundo (384 px de arquivo)
im_barraca = Image.new("RGBA", (384, 384), (0, 0, 0, 0))
d = ImageDraw.Draw(im_barraca)

# 1.1 Base e Balcão de Madeira Escura (X: 32 a 352, Y: 180 a 340)
# Pilares de canto da barraca (troncos / vigas de ferro)
for px in (32, 336):
    d.rectangle([px, 60, px + 24, 350], fill=(42, 34, 28, 255), outline=(18, 14, 10, 255), width=2)
    # Rebites e cantoneiras
    for ry in (120, 200, 280, 340):
        d.ellipse([px + 4, ry, px + 20, ry + 8], fill=(130, 105, 80, 255))

# Painel frontal do balcão (chapas de ferro e tábuas)
d.rectangle([56, 210, 336, 350], fill=(48, 38, 30, 255), outline=(18, 14, 10, 255), width=3)
for ty in (240, 275, 310):
    d.line([(56, ty), (336, ty)], fill=(25, 20, 15, 255), width=2)
# Reforço em X no painel frontal
d.line([(60, 215), (332, 345)], fill=(32, 26, 20, 255), width=4)
d.line([(60, 345), (332, 215)], fill=(32, 26, 20, 255), width=4)

# Tampo do Balcão (Madeira reforçada com chapa de latão desgastada)
d.rectangle([48, 195, 344, 220], fill=(85, 68, 50, 255), outline=(22, 16, 12, 255), width=2)
d.rectangle([52, 198, 340, 206], fill=(120, 95, 68, 255))

# 1.2 Janela Gradeada de Atendimento (Teller Window)
# Fundo escuro do interior da barraca
d.rectangle([80, 80, 312, 195], fill=(15, 12, 10, 255))
# Moldura da janela de atendimento
d.rectangle([80, 80, 312, 195], outline=(55, 45, 35, 255), width=4)
# Barras verticais da grade da janela (espaçamento de 16 px)
for bx in range(96, 304, 18):
    d.line([(bx, 84), (bx, 195)], fill=(80, 70, 60, 255), width=4)
    d.line([(bx - 1, 84), (bx - 1, 195)], fill=(40, 32, 25, 255), width=2)
# Pequena portinhola de atendimento no centro da grade
d.rectangle([160, 150, 232, 195], fill=(20, 16, 12, 255), outline=(140, 110, 80, 255), width=2)

# 1.3 Toldo de Pano Remendado (Awning no topo da barraca)
# Pano em listras desgastadas verde-musgo e bege/marrom com remendos
awning_pts = [(20, 70), (372, 70), (356, 20), (36, 20)]
d.polygon(awning_pts, fill=(90, 80, 60, 255), outline=(20, 16, 12, 255))
# Listras diagonais no toldo
for lx in range(40, 360, 40):
    d.polygon([(lx, 22), (lx + 20, 22), (lx + 10, 68), (lx - 10, 68)], fill=(125, 105, 75, 255))
# Remendos de pano com costuras
d.rectangle([120, 30, 165, 55], fill=(110, 50, 40, 255), outline=(30, 20, 15, 255), width=1)
d.rectangle([240, 25, 290, 58], fill=(60, 75, 85, 255), outline=(30, 20, 15, 255), width=1)
# Borda recortada / franjas do toldo na frente
for fx in range(24, 368, 24):
    d.polygon([(fx, 70), (fx + 12, 85), (fx + 24, 70)], fill=(75, 65, 50, 255), outline=(20, 16, 12, 255))

# Lanterna suspensa no canto esquerdo da barraca
d.line([(56, 75), (56, 110)], fill=(30, 25, 20, 255), width=2)
d.rectangle([48, 110, 64, 135], fill=(160, 120, 50, 255), outline=(30, 20, 15, 255), width=2)
d.ellipse([51, 115, 61, 125], fill=(255, 220, 130, 255)) # Brilho quente da lanterna

im_barraca.save(os.path.join(DIR_1D, "arena_barraca_apostas_v1.png"))
print("Barraca de apostas salva:", im_barraca.size)

# 2. QUADRO DE ODDS (arena_barraca_quadro_odds_v1.png)
# Moldura com encaixes/trilhos para placas intercambiáveis (32x32 de mundo -> 128x128 px)
# SEM NÚMEROS na imagem!
im_odds = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
d_o = ImageDraw.Draw(im_odds)
# Moldura de ferro escuro com parafusos
d_o.rectangle([8, 8, 119, 119], fill=(28, 24, 20, 255), outline=(15, 12, 10, 255), width=3)
# 4 trilhos horizontais para encaixe das placas de odds
for oy in (24, 48, 72, 96):
    # Trilho de fundo escuro
    d_o.rectangle([16, oy, 111, oy + 16], fill=(15, 12, 10, 255), outline=(45, 38, 30, 255), width=1)
    # Placa de metal fosco onde o texto/número do Godot será renderizado por cima
    d_o.rectangle([20, oy + 2, 107, oy + 14], fill=(40, 35, 30, 255))
    # Parafusos laterais
    d_o.ellipse([10, oy + 4, 14, oy + 8], fill=(140, 110, 80, 255))
    d_o.ellipse([113, oy + 4, 117, oy + 8], fill=(140, 110, 80, 255))

im_odds.save(os.path.join(DIR_1D, "arena_barraca_quadro_odds_v1.png"))
print("Quadro de odds salvo:", im_odds.size)

# 3. COFRE REFORÇADO (arena_barraca_cofre_v1.png)
# 24x24 de mundo -> 96x96 px de arquivo
im_cofre = Image.new("RGBA", (96, 96), (0, 0, 0, 0))
d_c = ImageDraw.Draw(im_cofre)
d_c.rectangle([12, 16, 83, 87], fill=(45, 38, 32, 255), outline=(18, 14, 10, 255), width=3)
# Cantoneiras e rebites nos 4 cantos
for cx in (16, 76):
    for cy in (20, 80):
        d_c.ellipse([cx-2, cy-2, cx+2, cy+2], fill=(140, 110, 80, 255))
# Fechadura redonda e volante central
d_c.ellipse([40, 44, 56, 60], fill=(120, 95, 65, 255), outline=(20, 16, 12, 255), width=2)
d_c.line([(48, 40), (48, 64)], fill=(160, 130, 90, 255), width=3)
d_c.line([(36, 52), (60, 52)], fill=(160, 130, 90, 255), width=3)
d_c.ellipse([46, 50, 50, 54], fill=(20, 16, 12, 255)) # Buraco da fechadura

im_cofre.save(os.path.join(DIR_1D, "arena_barraca_cofre_v1.png"))
print("Cofre salvo:", im_cofre.size)

# 4. FICHAS E CAIXA DE APOSTAS (arena_barraca_fichas_v1.png)
# 24x16 de mundo -> 96x64 px de arquivo
im_fichas = Image.new("RGBA", (96, 64), (0, 0, 0, 0))
d_f = ImageDraw.Draw(im_fichas)
# Caixa de madeira aberta
d_f.rectangle([10, 16, 85, 55], fill=(55, 42, 30, 255), outline=(20, 16, 12, 255), width=2)
# Pilhas de fichas de latão e ferro
chip_colors = [(180, 140, 60, 255), (140, 60, 50, 255), (60, 110, 140, 255)]
for idx, fx in enumerate(range(20, 75, 18)):
    c = chip_colors[idx % 3]
    for fy in range(45, 22, -4):
        d_f.ellipse([fx, fy, fx + 14, fy + 6], fill=c, outline=(20, 16, 10, 255), width=1)

im_fichas.save(os.path.join(DIR_1D, "arena_barraca_fichas_v1.png"))
print("Fichas salvas:", im_fichas.size)

# 5. DECAL DE FILA MARCADA NO PISO (arena_barraca_fila_decal_v1.png)
# Profundidade mínima de 48 px de mundo (192 px de arquivo) x 64 px de mundo (256 px de arquivo)
im_fila = Image.new("RGBA", (256, 192), (0, 0, 0, 0))
d_fila = ImageDraw.Draw(im_fila)
# Faixas amarelas industriais desbotadas e desgastadas marcando a área de fila
d_fila.line([(32, 20), (32, 170)], fill=(160, 130, 40, 160), width=6)
d_fila.line([(224, 20), (224, 170)], fill=(160, 130, 40, 160), width=6)
# Linhas horizontais de marcação de espera a cada 48 px de tela
for fy in (50, 98, 146):
    d_fila.line([(40, fy), (216, fy)], fill=(150, 120, 35, 140), width=4)
    # Marcas de desgaste / pisadas
    d_fila.ellipse([100, fy - 6, 116, fy + 2], fill=(20, 16, 12, 100))
    d_fila.ellipse([136, fy - 4, 152, fy + 4], fill=(20, 16, 12, 100))

im_fila.save(os.path.join(DIR_1D, "arena_barraca_fila_decal_v1.png"))
print("Fila decal salva:", im_fila.size)
