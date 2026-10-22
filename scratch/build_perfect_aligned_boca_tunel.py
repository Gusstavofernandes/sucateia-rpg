from PIL import Image, ImageFilter, ImageDraw
import numpy as np

# 1. Carregar texturas oficiais
wall_full = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")
tunel_base = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
rails_master = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

W_TEX = 1450
H_TEX = 1120
X_CENTER = 1025  # Centro do par de trilhos na textura

canvas = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))

# 2. MONTAR ALVENARIA BASE CONTÍNUA (Cantaria de pedra e vigas de ferro 3/4 isométrico)
wall_pure_crop = wall_full.crop((850, 160, 1450, 750))
wall_pure_resized = wall_pure_crop.resize((650, H_TEX), Image.Resampling.LANCZOS)

muralha = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
muralha.paste(wall_pure_resized, (0, 0))
muralha.paste(wall_pure_resized, (500, 0))
muralha.paste(wall_pure_resized, (1000, 0))
muralha.paste(wall_pure_resized, (W_TEX - 650, 0))

canvas.paste(muralha, (0, 0))

# 3. EXTRAIR PORTAL DA MINA COM VÃO AMPLO
# Em tunel_base (1024x1024):
# Cortar de x=110 a 910, y=70 a 900 (largura 800, altura 830)
portal_full = tunel_base.crop((110, 70, 910, 900))
# Redimensionar com vão amplo para acomodar os dormentes entre as ombreiras
portal_w = 950
portal_h = H_TEX
portal_resized = portal_full.resize((portal_w, portal_h), Image.Resampling.LANCZOS)

# Limpar o chão central velho (trilhos antigos de tunel_base)
portal_arr = np.array(portal_resized)
for py in range(int(portal_h * 0.45), portal_h):
    for px in range(int(portal_w * 0.20), int(portal_w * 0.80)):
        portal_arr[py, px, 3] = 0

portal_clean = Image.fromarray(portal_arr)

# Posição na textura para que o centro do portal fique exatamente em X_CENTER = 1025
# O centro do túnel em portal_full fica em 332 -> em portal_resized: 332 * (950/800) = 394 px
portal_x = X_CENTER - 394
portal_y = 0

# 4. ABERTURA INTERNA DA CAVERNA PROFUNDA DA MINA (Fundo escuro profundo)
dark_w = int(portal_w * 0.65)
dark_h = int(portal_h * 0.70)
dark_tunnel = Image.new("RGBA", (dark_w, dark_h), (10, 12, 14, 255))
dark_mask = Image.new("L", dark_tunnel.size, 255)
dark_draw = ImageDraw.Draw(dark_mask)
dark_draw.pieslice([0, 0, dark_w, 240], 180, 360, fill=255)
dark_mask = dark_mask.filter(ImageFilter.GaussianBlur(8))

dark_x = X_CENTER - dark_w // 2
dark_y = int(portal_h * 0.25)
canvas.paste(dark_tunnel, (dark_x, dark_y), dark_mask)

# 5. TRILHOS OFICIAIS ENTRANDO NO TÚNEL COM BITOLA PADRONIZADA (302 px)
# rails_master: largura 745, centro em 371
rails_h = H_TEX - (dark_y + 40)
rails_crop = rails_master.crop((0, 0, rails_master.width, min(rails_master.height, rails_h)))
rails_resized = rails_crop.resize((rails_master.width, rails_h), Image.Resampling.LANCZOS)

rails_arr = np.array(rails_resized)
for y in range(min(140, rails_h)):
    f = y / 140.0
    rails_arr[y, :, :3] = (rails_arr[y, :, :3] * f).astype(np.uint8)

rails_faded = Image.fromarray(rails_arr)
rails_paste_x = X_CENTER - 371
rails_paste_y = dark_y + 40

# Colar trilhos no chão do túnel
canvas.paste(rails_faded, (rails_paste_x, rails_paste_y), rails_faded)

# 6. COLAR A ESTRUTURA DO PORTAL POR CIMA (Ombreiras ficam dos lados dos trilhos!)
canvas.paste(portal_clean, (portal_x, portal_y), portal_clean)

# 7. SOMBRA DE CONTATO SUAVE E SEPARADA
sombra = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(sombra)
sdraw.ellipse([portal_x + 30, H_TEX - 80, portal_x + 240, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.ellipse([portal_x + portal_w - 240, H_TEX - 80, portal_x + portal_w - 30, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.rectangle([10, H_TEX - 70, portal_x + 20, H_TEX + 15], fill=(0, 0, 0, 120))
if portal_x + portal_w - 20 < W_TEX - 10:
    sdraw.rectangle([portal_x + portal_w - 20, H_TEX - 70, W_TEX - 10, H_TEX + 15], fill=(0, 0, 0, 120))
sombra = sombra.filter(ImageFilter.GaussianBlur(16))

# 8. SALVAR ARQUIVOS OFICIAIS
canvas.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
sombra.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png')
canvas.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')

print("boca_tunel_v2.png com vão amplo e trilhos passando entre as ombreiras salva!")
