from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
w, h = img.size
arr = np.array(img)

print(f"Altura estacao_trilho_v2 h = {h}")
for y in range(0, 100, 5):
    alpha_row = arr[y, :, 3]
    opaque_indices = np.where(alpha_row > 100)[0]
    if len(opaque_indices) > 0:
        print(f"Linha y={y}: opaco de x={opaque_indices[0]} a x={opaque_indices[-1]} (total {len(opaque_indices)} px)")
    else:
        print(f"Linha y={y}: totalmente transparente!")
