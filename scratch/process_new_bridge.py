import os
import shutil
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion

src_path = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\ponte_travessia_unificada_arena_1792595041626.jpg"
im = Image.open(src_path).convert("RGBA")
arr = np.array(im, dtype=np.float32)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

# 1. Detectar magenta rigorosamente
# R e B altos, G baixo
is_mag = (r > 120) & (b > 120) & ((np.minimum(r, b) - g) > 50)
mask = ~is_mag

# Erosao de 2 pixels para remover qualquer franja de compressao
mask_clean = binary_erosion(mask, iterations=2)

# Despill: onde R e B dominam G, atenuar para remover reflexo magenta
excess = np.maximum(0.0, np.minimum(r, b) - g)
r_clean = np.clip(r - excess * 0.98, 0, 255)
b_clean = np.clip(b - excess * 0.98, 0, 255)

out_arr = np.dstack([
    r_clean.astype(np.uint8),
    g.astype(np.uint8),
    b_clean.astype(np.uint8),
    (mask_clean * 255).astype(np.uint8)
])

out_img = Image.fromarray(out_arr)

# Crop na bounding box
bbox = out_img.split()[-1].getbbox()
out_cropped = out_img.crop(bbox)
w, h = out_cropped.size
print(f"Ponte recortada: {w}x{h}")

# 2. Gerar sombra de contato suave
alpha = np.array(out_cropped.split()[-1], dtype=np.float32)
# Sombra projetada levemente para baixo e para os lados (base da ponte)
shadow_arr = np.zeros((h, w, 4), dtype=np.uint8)
shadow_alpha = (alpha * 0.65).astype(np.uint8)
shadow_img = Image.fromarray(shadow_alpha, mode='L')
shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(radius=8))

shadow_final = Image.new("RGBA", (w, h), (0, 0, 0, 0))
shadow_final.paste(Image.new("RGBA", (w, h), (10, 10, 15, 255)), (0, 0), shadow_blurred)

# Salvar nos dois destinos
targets = [
    r"c:\Users\Usuario\Documents\jogo\assets\pipes",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes"
]

for t in targets:
    os.makedirs(t, exist_ok=True)
    img_path = os.path.join(t, "ponte_travessia_unificada_arena.png")
    shadow_path = os.path.join(t, "ponte_travessia_unificada_arena_sombra.png")
    out_cropped.save(img_path)
    shadow_final.save(shadow_path)
    print(f"Salvo em: {img_path}")
    print(f"Salvo em: {shadow_path}")

print("Processamento concluído com sucesso!")
