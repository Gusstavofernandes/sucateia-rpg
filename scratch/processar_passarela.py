import os
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion, binary_fill_holes, label

src_path = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\passarela_travessia_v1_1791341778952.jpg"
im = Image.open(src_path).convert("RGBA")
arr = np.array(im, dtype=np.float32)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

# 1. Identificar magenta do fundo e dos furinhos
is_mag = (r > 120) & (b > 120) & ((np.minimum(r, b) - g) > 55)

# Separar o fundo externo dos furinhos internos:
# Fundo externo toca as bordas da imagem
mask_obj = ~is_mag

# Fazer erosao para eliminar halos magenta
mask_obj_clean = binary_erosion(mask_obj, iterations=2)

# Despill: remover excesso de magenta nas bordas
excess = np.maximum(0.0, np.minimum(r, b) - g)
r_clean = np.clip(r - excess * 0.98, 0, 255)
b_clean = np.clip(b - excess * 0.98, 0, 255)

out_arr = np.dstack([
    r_clean.astype(np.uint8),
    g.astype(np.uint8),
    b_clean.astype(np.uint8),
    (mask_obj_clean * 255).astype(np.uint8)
])

out_img = Image.fromarray(out_arr)

# Crop na bounding box
bbox = out_img.split()[-1].getbbox()
out_img_cropped = out_img.crop(bbox)

# Salvar versao completa
out_img_cropped.save("C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/preview_passarela_recortada.png")
print("Salvo preview_passarela_recortada.png, tamanho:", out_img_cropped.size)
