from PIL import Image
import numpy as np

# Carregar imagens
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
arr_t = np.array(img_tunel)

img_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr_r = np.array(img_trilho)

print("=====================================================")
print("MEDIÇÃO PRECISA DOS TRILHOS")
print("=====================================================")

# 1. TÚNEL (ponta inferior)
# Na imagem tunel_mina_norte_v1.png (1024x1024)
# Na linha Y = 950:
# A cabeça do trilho esquerdo e a cabeça do trilho direito têm destaques de iluminação (brilho metálico cinza claro / ferro)
# Vamos inspecionar os canais R, G, B ao longo de X em Y=950:
row_t = arr_t[950, :, :]
# Trilho esquerdo fica em torno de X in [220, 270]
# Trilho direito fica em torno de X in [580, 640]
# Vamos encontrar os centros de massa / centro da cabeça de cada trilho:
# O topo do trilho tem destaque de brilho
# Vamos pegar a fatia do trilho esquerdo e direito:
# Trilho esquerdo:
# Vamos ver onde a coluna tem o trilho
# Em tunel_rails_crop.png, olhamos Y de 850 a 1000.
# A ponta do trilho esquerdo corta em Y ~ 972, ponta do direito corta em Y ~ 975.
# Na linha Y = 960 (onde ambos os trilhos ainda existem inteiros):
# Trilho esquerdo:
x_left_t = []
for x in range(200, 320):
    # Se alfa > 100
    if arr_t[960, x, 3] > 100:
        # A cabeça do trilho tem cor de metal cinza/marrom
        x_left_t.append(x)

# Trilho direito:
x_right_t = []
for x in range(550, 680):
    if arr_t[960, x, 3] > 100:
        x_right_t.append(x)

print(f"Tunel (Y=960 img): X_esq = [{min(x_left_t)}, {max(x_left_t)}], largura={max(x_left_t)-min(x_left_t)+1}")
print(f"Tunel (Y=960 img): X_dir = [{min(x_right_t)}, {max(x_right_t)}], largura={max(x_right_t)-min(x_right_t)+1}")

center_left_t = (min(x_left_t) + max(x_left_t)) / 2.0
center_right_t = (min(x_right_t) + max(x_right_t)) / 2.0
gauge_t_img = center_right_t - center_left_t
center_t_img = (center_left_t + center_right_t) / 2.0

print(f"Tunel (imagem 1024x1024):")
print(f"  Centro trilho esquerdo = {center_left_t:.2f} px")
print(f"  Centro trilho direito = {center_right_t:.2f} px")
print(f"  Centro do par de trilhos = {center_t_img:.2f} px (offset do centro da imagem {1024/2} = {center_t_img - 512:.2f} px)")
print(f"  Bitola na imagem = {gauge_t_img:.2f} px")

# 2. PONTE DO TRILHO (topo do trilho_reto_vertical_v1.png, 745x982)
# No topo do trilho vertical, linha Y = 30:
# Trilho esquerdo e trilho direito sobem livres
x_left_r = []
for x in range(50, 250):
    if arr_r[30, x, 3] > 100:
        x_left_r.append(x)

x_right_r = []
for x in range(500, 700):
    if arr_r[30, x, 3] > 100:
        x_right_r.append(x)

center_left_r = (min(x_left_r) + max(x_left_r)) / 2.0
center_right_r = (min(x_right_r) + max(x_right_r)) / 2.0
gauge_r_img = center_right_r - center_left_r
center_r_img = (center_left_r + center_right_r) / 2.0

print(f"\nTrilho Vertical (imagem 745x982):")
print(f"  Centro trilho esquerdo = {center_left_r:.2f} px")
print(f"  Centro trilho direito = {center_right_r:.2f} px")
print(f"  Centro do par de trilhos = {center_r_img:.2f} px (offset do centro da imagem {745/2} = {center_r_img - 372.5:.2f} px)")
print(f"  Bitola na imagem = {gauge_r_img:.2f} px")

# AGORA NO ESPAÇO DE MUNDO DO GODOT (CONSIDERANDO ESCALAS E POSIÇÕES DA CENA):
# Tunel:
# position = Vector2(-190, 150), scale = Vector2(0.26, 0.26)
# Centro da imagem é (512, 512)
scale_t = 0.26
world_x_center_t = -190.0 + (center_t_img - 512.0) * scale_t
world_gauge_t = gauge_t_img * scale_t
# Ponta inferior do túnel: Y_img ~ 975
# world_y_bottom_t = 150 + (975 - 512) * scale_t
world_y_bottom_t = 150.0 + (975.0 - 512.0) * scale_t

print(f"\n--- NO MUNDO DO GODOT (ESCALA REAL DO JOGO) ---")
print(f"TÚNEL (Ponta Inferior):")
print(f"  Centro X do par de trilhos no mundo = {world_x_center_t:.2f} px")
print(f"  Bitola no mundo = {world_gauge_t:.2f} px")
print(f"  Y da ponta inferior no mundo = {world_y_bottom_t:.2f} px")

# Ponte do Trilho:
# TrilhosSobreCavalete: position = Vector2(0, -30) em CavaleteElevadoCanal (mundo X=-190, Y=560)
# Ou seja: mundo do nó TrilhosSobreCavalete = Vector2(-190, 530)
# Escala do TrilhosSobreCavalete = Vector2(0.20, 0.20)
# Centro da imagem 745x982 é (372.5, 491)
scale_r = 0.20
world_x_center_r = -190.0 + (center_r_img - 372.5) * scale_r
world_gauge_r = gauge_r_img * scale_r
# Ponta superior do trilho vertical: Y_img ~ 2 (top_y_r)
world_y_top_r = 530.0 + (2.0 - 491.0) * scale_r

print(f"\nPONTE DO TRILHO (Ponta Superior):")
print(f"  Centro X do par de trilhos no mundo = {world_x_center_r:.2f} px")
print(f"  Bitola no mundo = {world_gauge_r:.2f} px")
print(f"  Y da ponta superior no mundo = {world_y_top_r:.2f} px")

# Distância vertical entre a ponta de baixo do túnel e a ponta de cima da ponte:
dist_y_gap = world_y_top_r - world_y_bottom_t
print(f"\nDISTÂNCIA VERTICAL LIVRE ENTRE TÚNEL E PONTE = {dist_y_gap:.2f} px")
print(f"Diferença de Bitola (Túnel vs Ponte): {abs(world_gauge_t - world_gauge_r):.2f} px")
print(f"Diferença de Centro X (Túnel vs Ponte): {abs(world_x_center_t - world_x_center_r):.2f} px")
