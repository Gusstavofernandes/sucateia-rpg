from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
arr = np.array(img)

# Olhar as colunas com alfa > 100 na linha y = 780
row = arr[780, :, :]
opaque_cols = np.where(row[:, 3] > 100)[0]
print(f"Colunas opacas na linha y = 780 da estação: {opaque_cols[0]} a {opaque_cols[-1]}")

# Onde estão os pixels de trilho (ferro)?
# Vamos ver a imagem recortada entre y=750 e 800
# Olhar as intensidades
for x in range(350, 950, 20):
    val = np.mean(row[x, :3])
    a = row[x, 3]
    if a > 50:
        print(f"x={x}: lum={val:.1f}, a={a}")
