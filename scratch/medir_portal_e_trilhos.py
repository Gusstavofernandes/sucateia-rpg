from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
arr = np.array(img)

# Achar a linha onde terminam as colunas de cantaria (pilares de pedra à esquerda e à direita do portal)
# Vamos olhar para x = 200 (asa oeste) e x = 800 (asa leste)
col_oeste = arr[:, 200, 3] > 100
col_leste = arr[:, 800, 3] > 100

y_base_oeste = np.where(col_oeste)[0][-1]
y_base_leste = np.where(col_leste)[0][-1]

print(f"Base da alvenaria (pilar oeste): linha y = {y_base_oeste}")
print(f"Base da alvenaria (pilar leste): linha y = {y_base_leste}")

# E onde termina o trilho do túnel?
print(f"Base dos trilhos do túnel: linha y = {arr.shape[0] - 1} (total h = {arr.shape[0]})")
print(f"Comprimento do trecho de trilho visível abaixo do portal: {arr.shape[0] - 1 - max(y_base_oeste, y_base_leste)} pixels na textura")
