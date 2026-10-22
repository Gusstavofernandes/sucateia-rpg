from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np

# 1. Carregar texturas oficiais
wall_mid = Image.open('scratch/wall_mid_pure.png').convert("RGBA")
wall_full = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")
tunel_base = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
rails_master = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

# Dimensões da boca de túnel:
# Largura no mundo: 290 px (de X = -395 a X = -105)
# Altura no mundo: 224 px (de Y = 20 a Y = 244)
# Na escala 0.20:
W_TEX = 1450
H_TEX = 1120
X_CENTER = 1025  # Centro do par de trilhos na textura

canvas = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))

# 2. TOPO CONTÍNUO DE CANTARIA CHANFRADA (Muralha 3/4 Isométrica)
# Redimensionar e montar a faixa superior da muralha cobrindo toda a largura (0 a W_TEX)
# Usar wall_mid (que tem a cantaria e viga de ferro pura perfeita)
# A imagem wall_mid tem 700x586. Vamos compor para cobrir 1450 de largura.
part1 = wall_mid.crop((0, 0, 600, wall_mid.height))
part2 = wall_mid.crop((100, 0, 700, wall_mid.height))
part3 = wall_mid.crop((50, 0, 550, wall_mid.height))

# Colar a faixa superior de cantaria chanfrada ao longo de todo o topo
masonry_strip = Image.new("RGBA", (1700, wall_mid.height), (0, 0, 0, 0))
masonry_strip.paste(part1, (0, 0))
masonry_strip.paste(part2, (550, 0))
masonry_strip.paste(part3, (1100, 0))

# Redimensionar para cobrir o topo da textura com a proporção exata da cantaria da cena
masonry_resized = masonry_strip.resize((W_TEX, 450), Image.Resampling.LANCZOS)
canvas.paste(masonry_resized, (0, 0), masonry_resized)

# 3. PAREDES LATERAIS (ASAS OESTE E LESTE)
# Asa Oeste (esquerda do portal: x de 0 a X_CENTER - 320 = 705 px)
asa_esq_crop = wall_full.crop((600, 150, 1100, 750))
asa_esq = asa_esq_crop.resize((720, H_TEX - 350), Image.Resampling.LANCZOS)
canvas.paste(asa_esq, (0, 350), asa_esq)

# Asa Leste (direita do portal: x de X_CENTER + 320 = 1345 a W_TEX = 1450 px)
asa_dir_crop = wall_full.crop((1000, 150, 1400, 750))
asa_dir = asa_dir_crop.resize((W_TEX - 1320, H_TEX - 350), Image.Resampling.LANCZOS)
canvas.paste(asa_dir, (1320, 350), asa_dir)

# 4. ABERTURA CENTRAL E INTERIOR PROFUNDO DA CAVERNA
# Largura do portal: 640 px (128 px no mundo).
# Centrado em X_CENTER = 1025.
# Vão do portal vai de x = 705 a x = 1345.
# Criar o breu interno do túnel com cantaria arqueada no topo:
portal_w = 640
portal_h = 750
portal_x0 = X_CENTER - portal_w // 2
portal_y0 = 370

# Escuridão do fundo da mina
tunnel_dark = Image.new("RGBA", (portal_w, portal_h), (0, 0, 0, 0))
dark_draw = ImageDraw.Draw(tunnel_dark)
# Preencher com arco em abóbada escura
dark_draw.pieslice([40, 0, portal_w - 40, 300], 180, 360, fill=(10, 12, 15, 255))
dark_draw.rectangle([40, 150, portal_w - 40, portal_h], fill=(10, 12, 15, 255))
canvas.paste(tunnel_dark, (portal_x0, portal_y0), tunnel_dark)

# 5. ESTRUTURA DO PORTAL DA MINA: VIGAS DE MADEIRA, FERRO REBITADO E LANTERNA
# De tunel_base (tunel_mina_norte_v1):
# Extrair o arco interno com as escoras diagonais, ombreiras de madeira com placas de ferro rebitadas e a lanterna
# Em tunel_base (1024x1024):
# Portal fica de x=180 a x=820, y=200 a y=850.
# Extrair a moldura estrutural do portal
portal_frame = tunel_base.crop((180, 200, 820, 850)) # 640x650
portal_frame_resized = portal_frame.resize((portal_w, portal_h - 50), Image.Resampling.LANCZOS)
canvas.paste(portal_frame_resized, (portal_x0, portal_y0 + 50), portal_frame_resized)

# 6. TRILHOS ENTRANDO NO TÚNEL COM BITOLA PADRONIZADA (302 px)
# rails_master tem largura 745, centro em 371
# Trilhos entram da boca escura do túnel (y ~ 550) até a base (y = H_TEX)
rails_needed_h = H_TEX - 540
rails_crop = rails_master.crop((0, 0, rails_master.width, min(rails_master.height, rails_needed_h)))
rails_resized = rails_crop.resize((rails_master.width, rails_needed_h), Image.Resampling.LANCZOS)

# Criar gradiente de sombra no início dos trilhos (onde entram na caverna escura)
rails_arr = np.array(rails_resized)
for y in range(min(140, rails_needed_h)):
    f = y / 140.0
    rails_arr[y, :, :3] = (rails_arr[y, :, :3] * f).astype(np.uint8)

rails_faded = Image.fromarray(rails_arr)
rails_paste_x = X_CENTER - 371
rails_paste_y = 540
canvas.paste(rails_faded, (rails_paste_x, rails_paste_y), rails_faded)

# 7. BASES DOS PILARES DE MADEIRA/FERRO SOBREPOSTAS ÀS BORDAS DOS DORMENTES
# Para criar a profundidade física correta (trilhos passam entre os pilares)
col_esq = portal_frame_resized.crop((0, 250, 140, portal_frame_resized.height))
col_dir = portal_frame_resized.crop((portal_w - 140, 250, portal_w, portal_frame_resized.height))
canvas.paste(col_esq, (portal_x0, portal_y0 + 50 + 250), col_esq)
canvas.paste(col_dir, (portal_x0 + portal_w - 140, portal_y0 + 50 + 250), col_dir)

# 8. SOMBRA DE CONTATO SUAVE E SEPARADA
sombra = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(sombra)
# Sombra suave sob as bases das ombreiras e da muralha no chão
sdraw.ellipse([portal_x0 - 20, H_TEX - 70, portal_x0 + 170, H_TEX + 20], fill=(0, 0, 0, 160))
sdraw.ellipse([portal_x0 + portal_w - 170, H_TEX - 70, portal_x0 + portal_w + 20, H_TEX + 20], fill=(0, 0, 0, 160))
sdraw.rectangle([10, H_TEX - 60, portal_x0 - 10, H_TEX + 15], fill=(0, 0, 0, 130))
sdraw.rectangle([portal_x0 + portal_w + 10, H_TEX - 60, W_TEX - 10, H_TEX + 15], fill=(0, 0, 0, 130))
sombra = sombra.filter(ImageFilter.GaussianBlur(14))

# 9. SALVAR AS TEXTURAS FINAIS OFICIAIS
out_boca = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.png'
out_sombra = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png'
out_txt = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.txt'

canvas.save(out_boca)
sombra.save(out_sombra)

# Salvar também no diretório raiz assets/rails/
canvas.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')

with open(out_txt, 'w', encoding='utf-8') as f:
    f.write("""Game asset, isometric 3/4 top-down view, same elevated camera angle, painted style and lighting as the reference images (warm amber light from the upper left), NOT a frontal view. A wide dark stone and iron mine tunnel mouth set into a dungeon wall, mossy stone voussoirs, heavy riveted dark iron reinforcement frame, a hanging glowing amber oil lantern, dark cavern opening in the center. Two straight vertical iron rails on wooden sleepers enter the opening, same gauge, spacing and wear as the rail reference, centered, and continue to the bottom edge of the image. The heavy stone and iron masonry spans the full width of the image so its left and right edges can touch neighboring stone walls with no gaps. Isolated on a flat solid magenta (#FF00FF) background, no floor, no cast shadow, no text, no characters, no watermark, sharp edges, full object visible.""")

with open('assets/rails/boca_tunel_v2.txt', 'w', encoding='utf-8') as f:
    f.write("""Game asset, isometric 3/4 top-down view, same elevated camera angle, painted style and lighting as the reference images (warm amber light from the upper left), NOT a frontal view. A wide dark stone and iron mine tunnel mouth set into a dungeon wall, mossy stone voussoirs, heavy riveted dark iron reinforcement frame, a hanging glowing amber oil lantern, dark cavern opening in the center. Two straight vertical iron rails on wooden sleepers enter the opening, same gauge, spacing and wear as the rail reference, centered, and continue to the bottom edge of the image. The heavy stone and iron masonry spans the full width of the image so its left and right edges can touch neighboring stone walls with no gaps. Isolated on a flat solid magenta (#FF00FF) background, no floor, no cast shadow, no text, no characters, no watermark, sharp edges, full object visible.""")

print("Nova boca_tunel_v2.png gerada e salva com sucesso!")
