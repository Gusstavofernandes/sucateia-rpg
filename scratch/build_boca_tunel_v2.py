from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
import numpy as np

# 1. Carregar referências oficiais do projeto
# - service_arch: bueiro com arco em pedra 3/4 isométrico e lanterna (200x190)
arch_img = Image.open('fundo_ferro_standalone/assets/service_arch.png').convert("RGBA")
# - fundo_wall: parede com cantaria chanfrada no topo e vigas de ferro (1983x793)
wall_img = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")
# - trilho_reto_vertical: trilho mestre padronizado (745x982)
rails_img = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

# 2. Definir dimensões e escala no mundo
# Escala na cena: scale = Vector2(0.20, 0.20)
#
# No mundo do jogo:
# Centro dos trilhos: X_rail = -190.0 px
# Borda esquerda da moldura: X_left = -395.0 px (cobre até o limite da tela oeste)
# Borda direita da moldura: X_right = -105.0 px (encosta e sobrepõe a borda da parede vizinha em -113.0)
# Largura total no mundo: -105.0 - (-395.0) = 290.0 px
#
# Altura no mundo:
# Topo da moldura: Y_top = 20.0 px (topo da parede)
# Base da moldura (onde o trilho de ligação começa): Y_bottom = 244.0 px
# Altura total no mundo: 244.0 - 20.0 = 224.0 px
#
# Na escala 0.20, dimensões na textura da imagem:
# Largura da textura: 290.0 / 0.20 = 1450 px (arredondamos para 1450 px)
# Altura da textura: 224.0 / 0.20 = 1120 px
#
# Posição do centro do par de trilhos na textura:
# Offset do centro dos trilhos em relação à borda esquerda:
# (-190.0 - (-395.0)) = 205.0 px no mundo -> 205.0 / 0.20 = 1025.0 px na textura!
#
# Bitola do trilho na textura:
# 60.40 / 0.20 = 302.0 px!
# Trilho esquerdo na textura: 1025.0 - 151.0 = 874.0 px
# Trilho direito na textura: 1025.0 + 151.0 = 1176.0 px

W_TEX = 1450
H_TEX = 1120
X_RAIL_CENTER_TEX = 1025

print(f"Criando boca_tunel_v2.png:")
print(f"  Tamanho: {W_TEX}x{H_TEX} px")
print(f"  Centro dos trilhos na textura: X = {X_RAIL_CENTER_TEX} px")
print(f"  Bitola na textura: 302.0 px")

# Criar canvas RGBA transparente
canvas = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))

# 3. CONSTRUÇÃO DA ALVENARIA DE PEDRA E CANTARIA 3/4 ISOMÉTRICA
# Usar amostras de cantaria do topo e corpo de fundo_wall e service_arch
# Em fundo_wall:
# Borda superior chanfrada de pedra fica em y=14 a y=250.
# Vamos pegar blocos de alvenaria de pedra de fundo_wall (onde a parede é rica em detalhes)
# Faixas de cantaria:
# Crop de bloco de parede: x=40 a x=550, y=14 a y=600 de fundo_wall
wall_block = wall_img.crop((50, 14, 550, 650))

# Redimensionar suavemente o bloco de parede para compor as asas da moldura
# Asa Esquerda: vai de x=0 a x=850 (cobrindo todo o flanco oeste da entrada da mina)
asa_esquerda_w = 870
asa_esquerda_h = H_TEX - 100
asa_esq = wall_block.resize((asa_esquerda_w, asa_esquerda_h), Image.Resampling.LANCZOS)
canvas.paste(asa_esq, (0, 0), asa_esq)

# Asa Direita: vai de x=1180 a x=W_TEX (encosto perfeito na parede vizinha)
asa_direita_w = W_TEX - 1180
asa_direita_h = H_TEX - 100
wall_block_dir = wall_img.crop((400, 14, 750, 650))
asa_dir = wall_block_dir.resize((asa_direita_w, asa_direita_h), Image.Resampling.LANCZOS)
canvas.paste(asa_dir, (1180, 0), asa_dir)

# 4. CONSTRUÇÃO DO PORTAL CENTRAL EM ARCO (service_arch em super-resolução)
# O arco original de service_arch tem 200x190 px.
# Queremos um portal imponente centrado em X_RAIL_CENTER_TEX = 1025.
# Largura do arco do portal: ~700 px na textura (140 px no mundo).
# Altura do arco do portal: ~820 px na textura.
portal_w = 720
portal_h = 820
portal_arch = arch_img.resize((portal_w, portal_h), Image.Resampling.LANCZOS)

# Recortar o interior do arco (as grades) para abrir a boca escura profunda da mina
# No portal_arch, a abertura interna começa em torno de x=160 a x=560 e y=250 a y=800
portal_x = X_RAIL_CENTER_TEX - portal_w // 2
portal_y = 0

# Colar a moldura do arco sobre a alvenaria
canvas.paste(portal_arch, (portal_x, portal_y), portal_arch)

# 5. ABERTURA ESCURA PROFUNDA DA MINA (VÃO CENTRAL ONDE OS TRILHOS ENTRAM)
# Criar máscara para o interior escuro
dark_tunnel = Image.new("RGBA", (portal_w - 220, portal_h - 180), (12, 14, 18, 255))
# Gradiente de escuridão profunda na caverna
dark_draw = ImageDraw.Draw(dark_tunnel)
for gy in range(dark_tunnel.height):
    alpha_grad = int(255 * min(1.0, (dark_tunnel.height - gy) / 100.0))
    # Mais escuro no fundo superior
    dark_draw.line([(0, gy), (dark_tunnel.width, gy)], fill=(10, 12, 15, 255))

dark_x = X_RAIL_CENTER_TEX - dark_tunnel.width // 2
dark_y = portal_y + 190
canvas.paste(dark_tunnel, (dark_x, dark_y))

# 6. ENTRADA DOS TRILHOS NA BOCA DO TÚNEL
# Os trilhos padronizados (trilho_reto_vertical_v1) entram no túnel vindo do escuro
# e continuam até a base da imagem (y = H_TEX)
# Na textura dos trilhos (745x982):
# Centro do par de trilhos = 371 px.
# Largura = 745 px.
# Queremos que o centro do par de trilhos caia exatamente em X_RAIL_CENTER_TEX = 1025!
# Topo dos trilhos na boca da mina: y = dark_y + 80
# Base dos trilhos: y = H_TEX
rails_dest_h = H_TEX - (dark_y + 80)
rails_crop_top = rails_img.crop((0, 0, rails_img.width, min(rails_img.height, rails_dest_h)))
rails_resized = rails_crop_top.resize((rails_img.width, rails_dest_h), Image.Resampling.LANCZOS)

# Criar desvanecimento / sombra interna na ponta dos trilhos que entram na caverna escura
rails_arr = np.array(rails_resized)
for ry in range(min(120, rails_dest_h)):
    fade = ry / 120.0
    rails_arr[ry, :, :3] = (rails_arr[ry, :, :3] * fade).astype(np.uint8)

rails_faded = Image.fromarray(rails_arr)
rails_paste_x = X_RAIL_CENTER_TEX - 371
rails_paste_y = dark_y + 80
canvas.paste(rails_faded, (rails_paste_x, rails_paste_y), rails_faded)

# 7. REFORÇO DE FERRO FUNDIDO, VIGAS E LANTERNA ÂMBAR
# Reaplicar as vigas e aduelas laterais da boca do túnel sobre os trilhos para profundidade
# Recortar pilares laterais do arco para sobrepor às pontas dos dormentes no fundo
pilar_esq = portal_arch.crop((0, 150, 150, portal_h))
pilar_dir = portal_arch.crop((portal_w - 150, 150, portal_w, portal_h))
canvas.paste(pilar_esq, (portal_x, portal_y + 150), pilar_esq)
canvas.paste(pilar_dir, (portal_x + portal_w - 150, portal_y + 150), pilar_dir)

# 8. SOMBRA DE CONTATO SEPARADA
# Gerar sombra de contato na base da moldura projetada no chão
sombra = Image.new("RGBA", (W_TEX, H_TEX), (0, 0, 0, 0))
sombra_draw = ImageDraw.Draw(sombra)
# Elipses suaves sob os pilares e sob a moldura de pedra
sombra_draw.ellipse([portal_x - 40, H_TEX - 60, portal_x + 180, H_TEX + 20], fill=(0, 0, 0, 140))
sombra_draw.ellipse([portal_x + portal_w - 180, H_TEX - 60, portal_x + portal_w + 40, H_TEX + 20], fill=(0, 0, 0, 140))
sombra_draw.ellipse([20, H_TEX - 70, asa_esquerda_w - 50, H_TEX + 15], fill=(0, 0, 0, 110))
sombra = sombra.filter(ImageFilter.GaussianBlur(12))

# 9. SALVAR ARQUIVOS FINAIS
out_tunel = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.png'
out_sombra = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png'
out_txt = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.txt'

canvas.save(out_tunel)
sombra.save(out_sombra)

# Salvar também no diretório raiz assets/rails/
canvas.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')

with open(out_txt, 'w', encoding='utf-8') as f:
    f.write("""Game asset, isometric 3/4 top-down view, same elevated camera angle, painted style and lighting as the reference images (warm amber light from the upper left), NOT a frontal view. A wide dark stone and iron mine tunnel mouth set into a dungeon wall, mossy stone voussoirs, heavy riveted dark iron reinforcement frame, a hanging glowing amber oil lantern, dark cavern opening in the center. Two straight vertical iron rails on wooden sleepers enter the opening, same gauge, spacing and wear as the rail reference, centered, and continue to the bottom edge of the image. The heavy stone and iron masonry spans the full width of the image so its left and right edges can touch neighboring stone walls with no gaps. Isolated on a flat solid magenta (#FF00FF) background, no floor, no cast shadow, no text, no characters, no watermark, sharp edges, full object visible.""")

with open('assets/rails/boca_tunel_v2.txt', 'w', encoding='utf-8') as f:
    f.write("""Game asset, isometric 3/4 top-down view, same elevated camera angle, painted style and lighting as the reference images (warm amber light from the upper left), NOT a frontal view. A wide dark stone and iron mine tunnel mouth set into a dungeon wall, mossy stone voussoirs, heavy riveted dark iron reinforcement frame, a hanging glowing amber oil lantern, dark cavern opening in the center. Two straight vertical iron rails on wooden sleepers enter the opening, same gauge, spacing and wear as the rail reference, centered, and continue to the bottom edge of the image. The heavy stone and iron masonry spans the full width of the image so its left and right edges can touch neighboring stone walls with no gaps. Isolated on a flat solid magenta (#FF00FF) background, no floor, no cast shadow, no text, no characters, no watermark, sharp edges, full object visible.""")

print("Arquivos salvos com sucesso!")
