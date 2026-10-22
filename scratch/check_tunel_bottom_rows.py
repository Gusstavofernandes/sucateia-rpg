from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
w, h = img.size
arr = np.array(img)

# Vamos analisar as últimas 50 linhas da imagem (y de 550 a 601)
print(f"Altura h = {h}")
for y in range(h - 30, h):
    alpha_row = arr[y, :, 3]
    opaque_indices = np.where(alpha_row > 100)[0]
    if len(opaque_indices) > 0:
        print(f"Linha y={y}: opaco de x={opaque_indices[0]} a x={opaque_indices[-1]} (total {len(opaque_indices)} px)")
    else:
        print(f"Linha y={y}: totalmente transparente!")
