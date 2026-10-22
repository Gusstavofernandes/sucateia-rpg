from PIL import Image, ImageFilter, ImageDraw
import numpy as np

# 1. Carregar texturas
wall_mid = Image.open('scratch/wall_mid_pure.png').convert("RGBA")
tunel_base = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
rails_master = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

W_TEX = 1450
H_TEX = 1120
X_CENTER = 1025

canvas = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))

# 2. MONTAR MURALHA DE ALVENARIA BASE
muralha = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
tile1 = wall_mid.crop((0, 0, 600, wall_mid.height)).resize((600, H_TEX), Image.Resampling.LANCZOS)
tile2 = wall_mid.crop((100, 0, 700, wall_mid.height)).resize((600, H_TEX), Image.Resampling.LANCZOS)
tile3 = wall_mid.crop((50, 0, 450, wall_mid.height)).resize((400, H_TEX), Image.Resampling.LANCZOS)

muralha.paste(tile1, (0, 0))
muralha.paste(tile2, (550, 0))
muralha.paste(tile3, (1100, 0))

canvas.paste(muralha, (0, 0))

# 3. PORTAL DA MINA
portal_w = 660
portal_x = X_CENTER - portal_w // 2
portal_y = 150
portal_h = H_TEX - portal_y

# Extrair estrutura do portal de tunel_base
portal_raw = tunel_base.crop((180, 210, 820, 860))
portal_resized = portal_raw.resize((portal_w, portal_h), Image.Resampling.LANCZOS)

# 4. ABERTURA INTERNA DA CAVERNA PROFUNDA DA MINA (Fundo escuro sob o arco)
dark_w = portal_w - 220
dark_h = portal_h - 180
dark_tunnel = Image.new("RGBA", (dark_w, dark_h), (10, 12, 14, 255))
dark_mask = Image.new("L", dark_tunnel.size, 255)
dark_draw = ImageDraw.Draw(dark_mask)
dark_draw.pieslice([0, 0, dark_w, 180], 180, 360, fill=255)
dark_mask = dark_mask.filter(ImageFilter.GaussianBlur(8))

dark_x = X_CENTER - dark_w // 2
dark_y = portal_y + 140
canvas.paste(dark_tunnel, (dark_x, dark_y), dark_mask)

# 5. COLAR ESTRUTURA DO PORTAL (Ombreiras, reforços e lanterna)
p_mask = Image.new("L", portal_resized.size, 255)
p_draw = ImageDraw.Draw(p_mask)
for x in range(25):
    a = int(255 * (x / 25.0))
    p_draw.line([(x, 0), (x, portal_h)], fill=a)
    p_draw.line([(portal_w - 1 - x, 0), (portal_w - 1 - x, portal_h)], fill=a)
p_mask = p_mask.filter(ImageFilter.GaussianBlur(4))

canvas.paste(portal_resized, (portal_x, portal_y), p_mask)

# 6. CANTARIA CHANFRADA DO TOPO SOBREPOSTA AO TOPO DO PORTAL (MURALHA CONTÍNUA)
# Extrair faixa superior de cantaria de pedra (y=0 a 240) da muralha
top_stones = muralha.crop((0, 0, W_TEX, 240))
top_mask = Image.new("L", top_stones.size, 255)
t_draw = ImageDraw.Draw(top_mask)
# Transição suave na base das pedras superiores para descer sobre as traves de madeira
for y in range(60):
    a = int(255 * (1.0 - y / 60.0))
    t_draw.line([(0, 180 + y), (W_TEX, 180 + y)], fill=a)
top_mask = top_mask.filter(ImageFilter.GaussianBlur(3))
canvas.paste(top_stones, (0, 0), top_mask)

# 7. TRILHOS ENTRANDO NO TÚNEL COM BITOLA PADRONIZADA (302 px)
rails_h = H_TEX - (dark_y + 40)
rails_crop = rails_master.crop((0, 0, rails_master.width, min(rails_master.height, rails_h)))
rails_resized = rails_crop.resize((rails_master.width, rails_h), Image.Resampling.LANCZOS)

# Gradiente de escuridão na ponta dos trilhos que entram na caverna
rails_arr = np.array(rails_resized)
for y in range(min(140, rails_h)):
    f = y / 140.0
    rails_arr[y, :, :3] = (rails_arr[y, :, :3] * f).astype(np.uint8)

rails_faded = Image.fromarray(rails_arr)
rails_paste_x = X_CENTER - 371
rails_paste_y = dark_y + 40
canvas.paste(rails_faded, (rails_paste_x, rails_paste_y), rails_faded)

# 8. BASES DAS OMBREIRAS SOBREPOSTAS AOS DORMENTES
col_esq = portal_resized.crop((15, 230, 140, portal_h))
col_dir = portal_resized.crop((portal_w - 140, 230, portal_w - 15, portal_h))
canvas.paste(col_esq, (portal_x + 15, portal_y + 230), col_esq)
canvas.paste(col_dir, (portal_x + portal_w - 140, portal_y + 230), col_dir)

# 9. SOMBRA DE CONTATO SUAVE E SEPARADA
sombra = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(sombra)
sdraw.ellipse([portal_x - 30, H_TEX - 80, portal_x + 180, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.ellipse([portal_x + portal_w - 180, H_TEX - 80, portal_x + portal_w + 30, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.rectangle([10, H_TEX - 70, portal_x - 10, H_TEX + 15], fill=(0, 0, 0, 120))
sdraw.rectangle([portal_x + portal_w + 10, H_TEX - 70, W_TEX - 10, H_TEX + 15], fill=(0, 0, 0, 120))
sombra = sombra.filter(ImageFilter.GaussianBlur(16))

# 10. SALVAR ARQUIVOS OFICIAIS
canvas.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
sombra.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png')
canvas.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')

print("boca_tunel_v2.png com cantaria contínua de ponta a ponta gerada!")
