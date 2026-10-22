from PIL import Image
import numpy as np

# A imagem media_1791569706976.jpg foi tirada com uma câmera do Godot
# Vamos encontrar os pontos-chave na imagem:
# 1. Lanterna do bueiro (luz amarela à direita do tubo vertical)
# 2. Bueiro com grade e água verde caindo (Bueiro_1 em mundo X=550, Y=240)
# 3. Lanterna da estação (em mundo X=175, Y=305)
# 4. Carrinho de minerio (em mundo X=220, Y=480)
# 5. Goblin (cabelo vermelho)
# 6. Pilha de sucata Sucata_1 (em mundo X=-180, Y=420)

im = Image.open('C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/.user_uploaded/media_1791569706976.jpg')
arr = np.array(im)
h, w, _ = arr.shape

# Posição do carrinho na imagem:
# Minerio verde
green_mask = (arr[:, :, 1] > 200) & (arr[:, :, 0] < 100) & (arr[:, :, 2] < 120)
yg, xg = np.where(green_mask)
cx_cart = np.mean(xg)
cy_cart = np.mean(yg)

# Posição do goblin:
red_mask = (arr[:, :, 0] > 180) & (arr[:, :, 1] < 60) & (arr[:, :, 2] < 60)
y_gob, x_gob = np.where(red_mask)
cx_gob = np.mean(x_gob)
cy_gob = np.mean(y_gob)

# Posição da sucata Sucata_1 (à esquerda):
# Sucata à esquerda está abaixo do goblin
print(f"Dimensões da imagem: {w}x{h}")
print(f"Carrinho na imagem: X={cx_cart:.1f}, Y={cy_cart:.1f} (Mundo: X=220, Y=480)")
print(f"Goblin na imagem: X={cx_gob:.1f}, Y={cy_gob:.1f}")

# Escala px/mundo:
# Sabemos que o carrinho está em X=220 mundo
# Na captura 1 que geramos antes, a camera estava em X_cam = 280, Y_cam = 380
# Viewport: 1152x648 ou 1280x720, com zoom 1.15
# Delta X pixels entre carrinho e goblin = cx_cart - cx_gob = 478 - 98 = 380 px
# Se a imagem é 1024x575 (redimensionada de 1152x648, fator 1024/1152 = 0.8888)
# Então em viewport original: delta X = 380 / 0.8888 = 427.5 px
# No mundo (dividido por zoom 1.15): delta X mundo = 427.5 / 1.15 = 371.7 unidades de mundo!
# Logo, X_mundo do goblin = 220 - 371.7 = -151.7 !
print(f"Estimativa de X mundo do Goblin: {220 - (cx_cart - cx_gob) * (1152/w) / 1.15:.1f}")
