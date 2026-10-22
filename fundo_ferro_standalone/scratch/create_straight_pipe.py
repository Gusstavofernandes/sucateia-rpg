import os
from PIL import Image, ImageFilter
import numpy as np

w, h = 160, 36
y, x = np.mgrid[:h, :w]

norm_y = y / float(h)
top_rim = np.exp(-((norm_y - 0.28) / 0.14) ** 2)

base_r = 105.0 + top_rim * 50.0 - (norm_y * 40.0)
base_g = 82.0 + top_rim * 38.0 - (norm_y * 32.0)
base_b = 65.0 + top_rim * 28.0 - (norm_y * 28.0)

np.random.seed(42)
noise = np.random.normal(0, 3, (h, w))
r = np.clip(base_r + noise, 35, 220)
g = np.clip(base_g + noise, 30, 190)
b = np.clip(base_b + noise, 25, 160)

# Flange collar bands at the ends
for fx in [14, w - 14]:
    band = np.abs(x - fx) <= 4
    r[band] = np.clip(r[band] * 1.25, 0, 255)
    g[band] = np.clip(g[band] * 1.22, 0, 255)
    b[band] = np.clip(b[band] * 1.18, 0, 255)

alpha = np.full((h, w), 255, dtype=np.uint8)
alpha[0, :] = 0
alpha[-1, :] = 0
alpha[1, :] = 180
alpha[-2, :] = 180

img_arr = np.dstack([r.astype(np.uint8), g.astype(np.uint8), b.astype(np.uint8), alpha])
pipe_img = Image.fromarray(img_arr).filter(ImageFilter.GaussianBlur(radius=0.4))

# Create contact shadow
sh_h = int(h * 0.45)
shadow_arr = np.zeros((sh_h, w, 4), dtype=np.uint8)
sh_alpha = np.full((sh_h, w), 110, dtype=np.uint8)
shadow_arr[:, :, 3] = sh_alpha
sh_img = Image.fromarray(shadow_arr).filter(ImageFilter.GaussianBlur(radius=4))

dirs = ['assets/pipes', 'fundo_ferro_standalone/assets/pipes']
for d in dirs:
    os.makedirs(d, exist_ok=True)
    pipe_img.save(os.path.join(d, 'tubo_segmento_reto.png'))
    sh_img.save(os.path.join(d, 'tubo_segmento_reto_sombra.png'))

print("tubo_segmento_reto.png e sombra gerados com sucesso!")
