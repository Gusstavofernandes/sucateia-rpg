from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
w, h = img.size
print(f"boca_tunel_v2 tamanho: {w} x {h}")

scale = 0.422378
pos_x = -188.94
pos_y = 116.86

world_w = w * scale
world_h = h * scale
print(f"Tamanho no mundo: {world_w:.2f} x {world_h:.2f}")

top_y = pos_y - world_h / 2
bottom_y = pos_y + world_h / 2
print(f"Y topo no mundo: {top_y:.2f} px")
print(f"Y base no mundo: {bottom_y:.2f} px")

# Analisar onde estão os pixels não-transparentes na base da imagem
arr = np.array(img)
alpha = arr[:, :, 3]
opaque_rows = np.where(np.any(alpha > 20, axis=1))[0]
first_row = opaque_rows[0]
last_row = opaque_rows[-1]
print(f"Primeira linha opaca na textura: {first_row}, Última linha opaca: {last_row} (de {h})")

# A base do sprite está em y = last_row.
# O centro do sprite na textura é (w/2, h/2) = (504, 301).
# A coordenada Y no mundo da última linha opaca é:
base_y_world = pos_y + (last_row - h / 2) * scale
print(f"Y da base opaca do túnel no mundo: {base_y_world:.2f} px")

# E onde a Estação V2 começa?
estacao_top_y = 244.00
gap = estacao_top_y - base_y_world
print(f"GAP entre túnel e estação: {gap:.2f} px")
