import os
import shutil
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion, binary_fill_holes, label

ROOTS = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes",
    r"c:\Users\Usuario\Documents\jogo\assets\pipes",
]

src_path = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\passarela_travessia_v1_1791341778952.jpg"
im = Image.open(src_path).convert("RGBA")
arr = np.array(im, dtype=np.float32)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

# 1. Detectar magenta rigorosamente
# R e B altos, G bem baixo
is_mag = (r > 115) & (b > 115) & ((np.minimum(r, b) - g) > 50)

# Mascara do objeto
mask = ~is_mag

# Erosao de 2 pixels para eliminar halos de compressao
mask_clean = binary_erosion(mask, iterations=2)

# Despill: onde R e B dominam G, atenuar R e B para remover qualquer fringe rosado
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
print(f"Passarela recortada: {w}x{h}")

# 2. Gerar sombra de contato suave separada
# A sombra deve se concentrar nas bases dos pilares e sob a plataforma
# Criar mapa de sombra a partir do canal alpha
alpha_arr = np.array(out_cropped.split()[-1], dtype=np.float32)
# Sombra projetada: achatada verticalmente e concentrada no chao (na base dos pilares e rampas)
sh_img = out_cropped.split()[-1].resize((w, int(h * 0.28)), Image.Resampling.BILINEAR)
sh_arr = np.array(sh_img, dtype=np.float32) * 0.50
z = np.zeros_like(sh_arr, dtype=np.uint8)
shadow = Image.fromarray(np.dstack([z, z, z, sh_arr.astype(np.uint8)])).filter(ImageFilter.GaussianBlur(4))

prompt_text = open(r"scratch/prompts/passarela_travessia_v1.txt", "w", encoding="utf-8")
p_content = """A short steel walkway bridge crossing over a large horizontal pipe, isometric 3/4 view. Two ramped approaches with chevron-patterned plates, a central grated platform raised above the pipe, riveted side railings with posts and cross bars, two heavy iron pillars bolted to the floor. The pipe passes underneath, visible through the grate gaps. Rusted dark iron, aged brass bolts, pure magenta background #FF00FF."""
prompt_text.write(p_content)
prompt_text.close()

asset_name = "passarela_travessia_completa_v1.png"
sombra_name = "passarela_travessia_completa_v1_sombra.png"
txt_name = "passarela_travessia_completa_v1.txt"

for root in ROOTS:
    os.makedirs(root, exist_ok=True)
    out_cropped.save(os.path.join(root, asset_name))
    shadow.save(os.path.join(root, sombra_name))
    with open(os.path.join(root, txt_name), "w", encoding="utf-8") as f:
        f.write(p_content)

print("Passarela salva em ambas as pastas de assets!")
