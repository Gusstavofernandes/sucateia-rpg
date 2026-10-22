from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np

# 1. Carregar texturas
wall = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")
t1 = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
rails_master = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

# Dimensões da textura:
# Largura no mundo: 290 px (de -395 a -105)
# Altura no mundo: 224 px (de 20 a 244)
# Escala: 0.20
W_TEX = 1450
H_TEX = 1120
X_CENTER = 1025

# 2. Criar a base contínua da muralha de pedras em 3/4 isométrico
# Pegar uma faixa contínua de parede de fundo_wall (colunas 300 a 1750, y=14 a 600)
# que já tem toda a cantaria superior, musgo e alvenaria coerente!
wall_strip = wall.crop((200, 14, 1850, 680)) # 1650 x 666 px
# Redimensionar para cobrir a largura total W_TEX x H_TEX com proporção natural
wall_base = wall_strip.resize((W_TEX, H_TEX), Image.Resampling.LANCZOS)

# 3. EXTRAIR O PORTAL DA MINA DE T1
# Em t1 (1024x1024):
# Portal com vigas de madeira, ombreiras, reforços de ferro, lanterna e abertura da caverna
# x de 180 a 820, y de 180 a 880 (largura 640, altura 700)
portal_raw = t1.crop((180, 180, 820, 880))
# Dimensões do portal na cena:
portal_w = 660
portal_h = 750
portal_resized = portal_raw.resize((portal_w, portal_h), Image.Resampling.LANCZOS)

# Criar máscara suave (feathered) nas bordas de pedra do portal para que ele se funda
# organicamente com a alvenaria da muralha sem nenhuma linha reta
p_mask = Image.new("L", (portal_w, portal_h), 255)
p_draw = ImageDraw.Draw(p_mask)
# Borda superior suave
for y in range(40):
    alpha = int(255 * (y / 40.0))
    p_draw.line([(0, y), (portal_w, y)], fill=alpha)
# Bordas laterais suaves
for x in range(35):
    alpha = int(255 * (x / 35.0))
    p_draw.line([(x, 0), (x, portal_h)], fill=alpha)
    p_draw.line([(portal_w - 1 - x, 0), (portal_w - 1 - x, portal_h)], fill=alpha)

p_mask = p_mask.filter(ImageFilter.GaussianBlur(6))

# Posição do portal: centrado em X_CENTER = 1025, base assentada na alvenaria
portal_x = X_CENTER - portal_w // 2
portal_y = H_TEX - portal_h - 40

# Colar portal sobre a muralha com a máscara suave
wall_base.paste(portal_resized, (portal_x, portal_y), p_mask)

# 4. ABERTURA INTERNA DA CAVERNA PROFUNDA
# Assegurar que o fundo do túnel dentro das vigas é escuro profundo
inner_dark = Image.new("RGBA", (portal_w - 240, portal_h - 220), (10, 12, 14, 255))
dark_mask = Image.new("L", inner_dark.size, 255)
dark_draw = ImageDraw.Draw(dark_mask)
# Arco superior da caverna
dark_draw.pieslice([0, 0, inner_dark.width, 160], 180, 360, fill=255)
inner_x = X_CENTER - inner_dark.width // 2
inner_y = portal_y + 180
# Colar escuridão dentro da boca da caverna
wall_base.paste(inner_dark, (inner_x, inner_y), dark_mask)

# 5. REAPLICAR AS VIGAS E LANTERNA POR CIMA DA ESCURIDÃO
# Extrair somente a estrutura de madeira, ferro e lanterna (reforço do túnel)
# As vigas de madeira/ferro e a lanterna ficam em volta do vão interno
frame_mask = Image.new("L", (portal_w, portal_h), 0)
f_draw = ImageDraw.Draw(frame_mask)
# Ombreira esquerda
f_draw.rectangle([20, 100, 150, portal_h], fill=255)
# Ombreira direita
f_draw.rectangle([portal_w - 150, 100, portal_w - 20, portal_h], fill=255)
# Trave superior com lanterna
f_draw.rectangle([100, 100, portal_w - 100, 260], fill=255)
frame_mask = frame_mask.filter(ImageFilter.GaussianBlur(4))
wall_base.paste(portal_resized, (portal_x, portal_y), frame_mask)

# 6. TRILHOS ENTRANDO NO TÚNEL COM BITOLA PADRONIZADA (302 px)
# rails_master: largura 745, centro em 371
rails_h = H_TEX - (inner_y + 60)
rails_crop = rails_master.crop((0, 0, rails_master.width, min(rails_master.height, rails_h)))
rails_resized = rails_crop.resize((rails_master.width, rails_h), Image.Resampling.LANCZOS)

# Desvanecimento na ponta que entra na caverna escura
rails_arr = np.array(rails_resized)
for y in range(min(130, rails_h)):
    f = y / 130.0
    rails_arr[y, :, :3] = (rails_arr[y, :, :3] * f).astype(np.uint8)

rails_faded = Image.fromarray(rails_arr)
rails_paste_x = X_CENTER - 371
rails_paste_y = inner_y + 60
wall_base.paste(rails_faded, (rails_paste_x, rails_paste_y), rails_faded)

# 7. BASES DOS PILARES SOBREPOSTAS ÀS BORDAS DOS DORMENTES
# Ombreiras na base:
pilar_base_esq = portal_resized.crop((30, 280, 150, portal_h))
pilar_base_dir = portal_resized.crop((portal_w - 150, 280, portal_w - 30, portal_h))
wall_base.paste(pilar_base_esq, (portal_x + 30, portal_y + 280), pilar_base_esq)
wall_base.paste(pilar_base_dir, (portal_x + portal_w - 150, portal_y + 280), pilar_base_dir)

# 8. SOMBRA DE CONTATO PROJETADA NO CHÃO
sombra = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(sombra)
sdraw.ellipse([portal_x - 30, H_TEX - 80, portal_x + 180, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.ellipse([portal_x + portal_w - 180, H_TEX - 80, portal_x + portal_w + 30, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.rectangle([10, H_TEX - 70, portal_x - 10, H_TEX + 15], fill=(0, 0, 0, 120))
sdraw.rectangle([portal_x + portal_w + 10, H_TEX - 70, W_TEX - 10, H_TEX + 15], fill=(0, 0, 0, 120))
sombra = sombra.filter(ImageFilter.GaussianBlur(16))

# 9. SALVAR AS TEXTURAS DEFINITIVAS
out_boca = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.png'
out_sombra = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png'

wall_base.save(out_boca)
sombra.save(out_sombra)
wall_base.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')

print("boca_tunel_v2.png e sombra salvas com sucesso!")
