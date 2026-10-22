import os
from PIL import Image, ImageFilter
import numpy as np

atlas_paths = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\floor_atlas.png",
    r"c:\Users\Usuario\Documents\jogo\assets\floor_atlas.png"
]

for p in atlas_paths:
    if not os.path.exists(p):
        continue
    img = Image.open(p).convert('RGB')
    arr = np.array(img).astype(float)
    h, w, c = arr.shape
    
    # 1. Modify the right half (x >= 384) to break exact mirror reflection
    # Add subtle variations: shifted cobblestone luminance, dirt patinas, cracked mortar
    np.random.seed(1337)
    
    # Create smooth perlin-like dirt/wear noise
    noise_low = np.random.normal(0, 15, (h // 16, w // 16))
    noise_img = Image.fromarray(noise_low).resize((w, h), Image.Resampling.BICUBIC)
    noise_arr = np.array(noise_img)
    
    # On the right half (x >= 384), add variation to stones
    right_mask = np.zeros((h, w), dtype=float)
    right_mask[:, 384:] = 1.0
    # Soft transition around 384
    right_mask[:, 360:408] = np.linspace(0, 1, 48)
    
    # Vary hue and luminance on right half: shift stones, add iron oxide patina
    variation = np.zeros_like(arr)
    variation[:, :, 0] = noise_arr * 0.85 + 4.0   # warm rust dirt
    variation[:, :, 1] = noise_arr * 0.60 - 2.0   # slight greenish moss
    variation[:, :, 2] = noise_arr * 0.35 - 8.0   # darker shadow in mortar
    
    # Also add some local cobblestone patches to completely break identical stone shapes
    patch_y, patch_x = np.ogrid[:h, :w]
    patch1 = np.exp(-((patch_x - 550)**2 + (patch_y - 280)**2) / (70.0**2))
    patch2 = np.exp(-((patch_x - 620)**2 + (patch_y - 520)**2) / (85.0**2))
    patch_mortar = (patch1 + patch2)[:, :, np.newaxis] * 22.0
    
    arr += variation * right_mask[:, :, np.newaxis]
    arr -= patch_mortar
    
    # 2. Moisture / damp gradient near canal edge (y around 300..450)
    # Darken and add deep green-black dampness
    damp_y = np.exp(-((patch_y - 380) / 120.0)**2)[:, :, np.newaxis]
    arr -= damp_y * 14.0
    
    arr_clean = np.clip(arr, 0, 255).astype(np.uint8)
    Image.fromarray(arr_clean).save(p)
    print(f"floor_atlas atualizado sem simetria de espelho: {p}")
