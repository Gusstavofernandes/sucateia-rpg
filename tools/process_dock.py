import os
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion

def process_dock(src_path: str, out_png_path: str):
    img = Image.open(src_path).convert("RGB")
    arr = np.array(img, dtype=np.float32)
    
    h, w, _ = arr.shape
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    avg_rb = (r + b) / 2.0
    magenta_diff = avg_rb - g
    
    # Detecção de magenta
    is_magenta = (r > 105) & (b > 105) & (g < 140) & (magenta_diff > 25)
    
    obj_mask = ~is_magenta
    
    # Despill: remover excesso de magenta das bordas e ferragens
    excess = np.maximum(0.0, np.minimum(r, b) - g)
    r = np.clip(r - excess * 1.05, 0, 255)
    b = np.clip(b - excess * 1.05, 0, 255)
    
    # Ajuste de cores para madeira/ferro onde ainda houver R/B elevados
    still_magenta = (r > 100) & (b > 100) & ((np.minimum(r, b) - g) > 20)
    b[still_magenta] = g[still_magenta]
    r[still_magenta] = np.clip(g[still_magenta] * 1.1 + 10, 0, 220)
    
    # Erosão de 1 pixel na borda externa
    eroded_mask = binary_erosion(obj_mask, iterations=1)
    alpha = np.where(eroded_mask, 255.0, np.where(obj_mask, 140.0, 0.0))
    
    alpha_img = Image.fromarray(alpha.astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.4))
    final_alpha = np.array(alpha_img, dtype=np.uint8)
    final_alpha[~obj_mask] = 0
    
    # Sanidade de magenta estrita
    semi = final_alpha > 0
    mag_check = semi & (r > 120) & (b > 120) & (g < 100) & (((r.astype(int) + b.astype(int)) / 2) - g.astype(int) > 30)
    b[mag_check] = g[mag_check]
    r[mag_check] = np.clip(g[mag_check] + 10, 0, 255)
    
    rgba = np.dstack([r, g, b, final_alpha]).astype(np.uint8)
    out_img = Image.fromarray(rgba, mode="RGBA")
    
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        
    os.makedirs(os.path.dirname(out_png_path), exist_ok=True)
    out_img.save(out_png_path, "PNG")
    print(f"Cais processado com sucesso: {out_png_path} ({out_img.size[0]}x{out_img.size[1]})")

    # Sombra de contato
    w_out, h_out = out_img.size
    sh = out_img.split()[-1].resize((w_out, max(8, int(h_out * 0.25))), Image.Resampling.BILINEAR)
    sh_a = (np.array(sh, dtype=np.float32) * 0.55).astype(np.uint8)
    z = np.zeros_like(sh_a)
    shadow = Image.fromarray(np.dstack([z, z, z, sh_a])).filter(ImageFilter.GaussianBlur(5))
    shadow_path = out_png_path.replace(".png", "_sombra.png")
    shadow.save(shadow_path)
    print(f"Sombra salva: {shadow_path}")

if __name__ == "__main__":
    process_dock(sys.argv[1], sys.argv[2])
