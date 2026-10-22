from PIL import Image
import numpy as np

img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
arr_est = np.array(img_est)

# Na estação: o nó está em Vector2(-215.9, 325) com escala 0.20
# O sprite da estação tem tamanho 1008 x 810.
# O centro do sprite é (504, 405).
# Vamos ver em que linha Y da textura da estação estão:
# 1. As pontas de ferro que sobem
# 2. O primeiro dormente de madeira
# 3. O guincho metálico à esquerda

# 1. Pontas de ferro que sobem:
opaque_y = np.where(np.any(arr_est[:, :, 3] > 100, axis=1))[0]
first_y = opaque_y[0]
print(f"Primeira linha opaca na estação: y = {first_y}")
world_first_y = 325.0 + (first_y - 405) * 0.20
print(f"Y no mundo da primeira linha opaca da estação: {world_first_y:.2f} px")

# 2. Primeiro dormente de madeira (onde a madeira começa):
# Olhar a coluna dos trilhos (x de 500 a 700)
for y in range(0, 150):
    row_slice = arr_est[y, 500:700, 3]
    if np.sum(row_slice > 100) > 100: # dormente largo opaco
        print(f"Primeiro dormente de madeira na estação: linha y = {y}")
        world_dormente_y = 325.0 + (y - 405) * 0.20
        print(f"Y no mundo do primeiro dormente da estação: {world_dormente_y:.2f} px")
        break

# E no túnel:
img_tun = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
arr_tun = np.array(img_tun)
print(f"\nTúnel tamanho: {img_tun.size}")
# Último dormente de madeira no túnel:
for y in range(arr_tun.shape[0]-1, 350, -1):
    row_slice = arr_tun[y, 450:550, 3]
    if np.sum(row_slice > 100) > 50:
        print(f"Último dormente de madeira no túnel: linha y = {y}")
        break
