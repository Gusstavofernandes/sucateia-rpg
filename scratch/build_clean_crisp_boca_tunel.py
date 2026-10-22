from PIL import Image, ImageFilter, ImageDraw
import numpy as np

# 1. Carregar texturas oficiais
wall_mid = Image.open('scratch/wall_mid_pure.png').convert("RGBA")
tunel_base = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
rails_master = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

W_TEX = 1450
H_TEX = 1120
X_CENTER = 1025  # Eixo central único e padronizado dos trilhos

canvas = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))

# 2. MONTAR MURALHA DE ALVENARIA BASE CONTÍNUA DE CIMA A BAIXO
p1 = wall_mid.crop((0, 0, 600, wall_mid.height)).resize((650, H_TEX), Image.Resampling.LANCZOS)
p2 = wall_mid.crop((100, 0, 700, wall_mid.height)).resize((650, H_TEX), Image.Resampling.LANCZOS)
p3 = wall_mid.crop((50, 0, 450, wall_mid.height)).resize((400, H_TEX), Image.Resampling.LANCZOS)

muralha = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
muralha.paste(p1, (0, 0))
muralha.paste(p2, (550, 0))
muralha.paste(p3, (1100, 0))

canvas.paste(muralha, (0, 0))

# 3. ABERTURA CENTRAL DA CAVERNA PROFUNDA DA MINA (Vão escuro sob o arco)
portal_w = 640
portal_x = X_CENTER - portal_w // 2
portal_y = 220  # Encaixe perfeito sob a cantaria chanfrada do topo!
portal_h = H_TEX - portal_y

dark_w = portal_w - 180
dark_h = portal_h - 100
dark_tunnel = Image.new("RGBA", (dark_w, dark_h), (10, 12, 14, 255))
dark_mask = Image.new("L", dark_tunnel.size, 255)
dark_draw = ImageDraw.Draw(dark_mask)
dark_draw.pieslice([0, 0, dark_w, 200], 180, 360, fill=255)
dark_mask = dark_mask.filter(ImageFilter.GaussianBlur(8))

dark_x = X_CENTER - dark_w // 2
dark_y = portal_y + 100
canvas.paste(dark_tunnel, (dark_x, dark_y), dark_mask)

# 4. TRILHOS OFICIAIS ENTRANDO NO TÚNEL COM BITOLA PADRONIZADA (302 px)
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
canvas.paste(rails_faded, (rails_paste_x, rails_paste_y), rails_faded)

# 5. ESTRUTURA LIMPA DO PORTAL DE MADEIRA E FERRO (SEM TRILHOS VELHOS)
portal_clean = tunel_base.crop((220, 200, 780, 860)).convert("RGBA")
portal_arr = np.array(portal_clean)

# Apagar a área do chão central de tunel_base onde ficavam os trilhos velhos
for py in range(450, 660):
    for px in range(100, 460):
        portal_arr[py, px, 3] = 0

portal_clean_no_rails = Image.fromarray(portal_arr)
portal_resized = portal_clean_no_rails.resize((portal_w, portal_h), Image.Resampling.LANCZOS)

canvas.paste(portal_resized, (portal_x, portal_y), portal_resized)

# 6. CANTARIA CHANFRADA DO TOPO COBRINDO DE PONTA A PONTA
top_strip = muralha.crop((0, 0, W_TEX, 250))
top_mask = Image.new("L", top_strip.size, 255)
t_draw = ImageDraw.Draw(top_mask)
for y in range(60):
    a = int(255 * (1.0 - y / 60.0))
    t_draw.line([(0, 190 + y), (W_TEX, 190 + y)], fill=a)
top_mask = top_mask.filter(ImageFilter.GaussianBlur(3))
canvas.paste(top_strip, (0, 0), top_mask)

# 7. SOMBRA DE CONTATO SUAVE E SEPARADA
sombra = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(sombra)
sdraw.ellipse([portal_x - 30, H_TEX - 80, portal_x + 180, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.ellipse([portal_x + portal_w - 180, H_TEX - 80, portal_x + portal_w + 30, H_TEX + 20], fill=(0, 0, 0, 150))
sdraw.rectangle([10, H_TEX - 70, portal_x - 10, H_TEX + 15], fill=(0, 0, 0, 120))
sdraw.rectangle([portal_x + portal_w + 10, H_TEX - 70, W_TEX - 10, H_TEX + 15], fill=(0, 0, 0, 120))
sombra = sombra.filter(ImageFilter.GaussianBlur(16))

# 8. SALVAR ARQUIVOS OFICIAIS
canvas.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
sombra.save('fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png')
canvas.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')

print("boca_tunel_v2.png definitiva salva com sucesso!")
