from PIL import Image
import numpy as np

img_path = 'C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/.user_uploaded/media_1791602107053.jpg'
img = Image.open(img_path).convert("RGBA")
print(f"Resolução da imagem enviada: {img.size}")

# Analisar a cor do fundo
arr = np.array(img)
# Amostrar os 4 cantos
cantos = [arr[10, 10], arr[10, img.size[0]-10], arr[img.size[1]-10, 10], arr[img.size[1]-10, img.size[0]-10]]
print("Cores dos cantos (RGB):", [c[:3].tolist() for c in cantos])

# Encontrar os trilhos na base da imagem (linha perto do fundo, ex: y = altura - 50)
row_base = arr[img.size[1] - 50, :, :]
# Onde não é magenta
# Magenta é R alto, G baixo, B alto
is_magenta = (row_base[:, 0] > 200) & (row_base[:, 1] < 50) & (row_base[:, 2] > 200)
rails_indices = np.where(~is_magenta)[0]

if len(rails_indices) > 0:
    min_x, max_x = rails_indices[0], rails_indices[-1]
    center_x = (min_x + max_x) / 2
    print(f"Base dos trilhos (x de {min_x} a {max_x}): largura = {max_x - min_x} px, centro = {center_x:.1f} px")
    print(f"Offset em relação ao centro da imagem ({img.size[0]/2}): {center_x - img.size[0]/2:.1f} px")
