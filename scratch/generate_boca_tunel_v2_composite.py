from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np

# Carregar imagens base
t1 = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
wall = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")
rails_master = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

# Dimensões da boca de túnel no mundo:
# Escala de renderização na cena: 0.20
# Largura no mundo: de X = -395.0 a X = -105.0 -> 290.0 px no mundo
# Altura no mundo: de Y = 20.0 a Y = 244.0 -> 224.0 px no mundo
#
# Dimensões na textura da imagem (escala 0.20):
# W_TEX = 1450 px
# H_TEX = 1120 px
#
# Centro dos trilhos na textura:
# No mundo: X_centro = -190.0 px
# Borda esquerda da textura no mundo: -395.0 px
# Offset do centro dos trilhos = (-190.0 - (-395.0)) / 0.20 = 205.0 / 0.20 = 1025 px!
#
# Bitola dos trilhos na textura: 60.40 / 0.20 = 302.0 px!
# Passo dos dormentes na textura: 24.0 / 0.20 = 120.0 px!
# Largura dos dormentes na textura: 129.0 / 0.20 = 645.0 px!

W_TEX = 1450
H_TEX = 1120
X_CENTER = 1025

canvas = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))

# 1. PARTE SUPERIOR E ASAS LATERAIS (Cantaria em ângulo 3/4 isométrico da parede)
# Cortar seções de cantaria de pedra com o topo chanfrado de fundo_wall:
# Em fundo_wall:
# Topo chanfrado em y=14 até y=250.
# Vamos criar o fundo de alvenaria maciça que preenche 100% da largura de 0 a W_TEX
wall_crop1 = wall.crop((50, 14, 550, 600))  # 500x586
wall_crop2 = wall.crop((400, 14, 800, 600)) # 400x586
wall_crop3 = wall.crop((700, 14, 1100, 600))# 400x586

# Redimensionar para cobrir toda a parede superior
# Faixa superior de cantaria chanfrada (y de 0 a 350)
top_masonry = wall.crop((50, 14, 1500, 350)) # 1450x336
top_masonry_resized = top_masonry.resize((W_TEX, 380), Image.Resampling.LANCZOS)
canvas.paste(top_masonry_resized, (0, 0), top_masonry_resized)

# Preencher a asa esquerda (x de 0 a 700, y de 300 a H_TEX)
asa_esq_fill = wall.crop((50, 200, 550, 750))
asa_esq_resized = asa_esq_fill.resize((720, H_TEX - 300), Image.Resampling.LANCZOS)
canvas.paste(asa_esq_resized, (0, 300), asa_esq_resized)

# Preencher a asa direita (x de 1300 a W_TEX, y de 300 a H_TEX)
asa_dir_fill = wall.crop((400, 200, 800, 750))
asa_dir_resized = asa_dir_fill.resize((W_TEX - 1300, H_TEX - 300), Image.Resampling.LANCZOS)
canvas.paste(asa_dir_resized, (1300, 300), asa_dir_resized)

# 2. PORTAL DE MINA REFORÇADO (Abertura central, vigas de ferro e lanterna)
# O portal de t1 (tunel_mina_norte_v1) tem o vão interno e as vigas de madeira/ferro.
# O centro do portal de t1 está em x=442 na imagem 1024x1024.
# Queremos que o portal fique exatamente centrado em X_CENTER = 1025!
# Vamos extrair o portal de t1:
# x de 150 a 820 (largura 670), y de 160 a 900 (altura 740)
# Centro do portal de t1: 150 + 670/2 = 485
portal_crop = t1.crop((150, 180, 820, 880)) # 670x700
# Redimensionar para encaixar no vão da boca da mina
portal_w = 700
portal_h = 760
portal_resized = portal_crop.resize((portal_w, portal_h), Image.Resampling.LANCZOS)

# Colar o portal centrado em X_CENTER = 1025
portal_paste_x = X_CENTER - portal_w // 2
portal_paste_y = 220
canvas.paste(portal_resized, (portal_paste_x, portal_paste_y), portal_resized)

# 3. TRILHOS ENTRANDO NO TÚNEL COM BITOLA PADRONIZADA (302 px)
# No interior do túnel, os trilhos de rails_master entram na boca da caverna
# rails_master tem largura 745, centro em 371
# Trilho esquerdo em 220, direito em 522 (bitola = 302 px)
# Queremos os trilhos desde a caverna escura (y ~ 500) até a base (y = H_TEX)
rails_h = H_TEX - 500
rails_crop = rails_master.crop((0, 0, rails_master.width, min(rails_master.height, rails_h)))
rails_resized = rails_crop.resize((rails_master.width, rails_h), Image.Resampling.LANCZOS)

# Gradiente de desvanecimento na ponta superior do trilho (entrando na escuridão)
rails_arr = np.array(rails_resized)
for y in range(min(150, rails_h)):
    factor = y / 150.0
    rails_arr[y, :, :3] = (rails_arr[y, :, :3] * factor).astype(np.uint8)

rails_faded = Image.fromarray(rails_arr)
rails_paste_x = X_CENTER - 371
rails_paste_y = 500
canvas.paste(rails_faded, (rails_paste_x, rails_paste_y), rails_faded)

# 4. REAPLICAR AS BASES DOS PILARES DE PEDRA/FERRO LATERAIS SOBRE AS PONTAS DOS DORMENTES
# Para que os dormentes fiquem entre os pilares e a boca do túnel tenha profundidade real
pilar_esq = portal_resized.crop((0, 200, 160, portal_h))
pilar_dir = portal_resized.crop((portal_w - 160, 200, portal_w, portal_h))
canvas.paste(pilar_esq, (portal_paste_x, portal_paste_y + 200), pilar_esq)
canvas.paste(pilar_dir, (portal_paste_x + portal_w - 160, portal_paste_y + 200), pilar_dir)

# 5. GERAR SOMBRA DE CONTATO SEPARADA
sombra = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(sombra)
# Sombra sob as bases dos pilares e paredes
sdraw.ellipse([portal_paste_x - 30, H_TEX - 70, portal_paste_x + 180, H_TEX + 15], fill=(0, 0, 0, 160))
sdraw.ellipse([portal_paste_x + portal_w - 180, H_TEX - 70, portal_paste_x + portal_w + 30, H_TEX + 15], fill=(0, 0, 0, 160))
sdraw.rectangle([10, H_TEX - 60, portal_paste_x - 20, H_TEX + 10], fill=(0, 0, 0, 120))
sdraw.rectangle([portal_paste_x + portal_w + 20, H_TEX - 60, W_TEX - 10, H_TEX + 10], fill=(0, 0, 0, 120))
sombra = sombra.filter(ImageFilter.GaussianBlur(14))

# 6. SALVAR ARQUIVOS FINAIS
canvas.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
sombra.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png')
canvas.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')
print("Salvo boca_tunel_v2.png e sombra com sucesso!")
