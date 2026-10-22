import os
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion

src_path = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\falesia_maritima_amarelada_1792604845461.jpg"
im = Image.open(src_path).convert("RGBA")
arr = np.array(im, dtype=np.float32)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

is_mag = (r > 120) & (b > 120) & ((np.minimum(r, b) - g) > 45)
mask = ~is_mag

mask_clean = binary_erosion(mask, iterations=2)

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
bbox = out_img.split()[-1].getbbox()
out_cropped = out_img.crop(bbox)
w, h = out_cropped.size
print(f"Falésia amarelada recortada: {w}x{h}")

alpha = np.array(out_cropped.split()[-1], dtype=np.float32)
shadow_alpha = (alpha * 0.55).astype(np.uint8)
shadow_img = Image.fromarray(shadow_alpha, mode='L')
shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(radius=10))

shadow_final = Image.new("RGBA", (w, h), (0, 0, 0, 0))
shadow_final.paste(Image.new("RGBA", (w, h), (10, 10, 15, 255)), (0, 0), shadow_blurred)

dst_dir = r"c:\Users\Usuario\Documents\jogo\assets\reconstruction"
img_dst = os.path.join(dst_dir, "falesia_maritima_amarelada.png")
shd_dst = os.path.join(dst_dir, "falesia_maritima_amarelada_sombra.png")

out_cropped.save(img_dst)
shadow_final.save(shd_dst)
print("Salvo em:", img_dst)
