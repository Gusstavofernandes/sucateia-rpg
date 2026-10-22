import os
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion

def process_crane(src_path: str, out_png_path: str):
    img = Image.open(src_path).convert("RGB")
    arr = np.array(img, dtype=np.float32)
    
    h, w, _ = arr.shape
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Detecção de magenta
    avg_rb = (r + b) / 2.0
    magenta_diff = avg_rb - g
    
    # Pixel é fundo magenta se R e B forem altos, G for baixo e a diferença for clara
    is_magenta = (r > 100) & (b > 100) & (g < 140) & (magenta_diff > 22)
    
    # Máscara do objeto
    obj_mask = ~is_magenta
    
    # Despill: remover reflexo magenta em bordas de metal, cabos e dentes de engrenagens
    excess = np.maximum(0.0, np.minimum(r, b) - g)
    r = np.clip(r - excess * 1.05, 0, 255)
    b = np.clip(b - excess * 1.05, 0, 255)
    
    # Corrigir qualquer pixel onde R e B ainda sejam muito superiores a G
    still_magenta = (r > 100) & (b > 100) & ((np.minimum(r, b) - g) > 20)
    b[still_magenta] = g[still_magenta]
    r[still_magenta] = np.clip(g[still_magenta] * 1.15 + 10, 0, 220)
    
    # Suave erosão de 1 pixel na máscara externa para eliminar franja
    eroded_mask = binary_erosion(obj_mask, iterations=1)
    alpha = np.where(eroded_mask, 255.0, np.where(obj_mask, 140.0, 0.0))
    
    # Suavização muito sutil nas bordas
    alpha_img = Image.fromarray(alpha.astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.4))
    final_alpha = np.array(alpha_img, dtype=np.uint8)
    
    # Garantir que o fundo seja 0 absoluto
    final_alpha[~obj_mask] = 0
    
    # Limpeza final estrita para o teste verify_no_magenta_fringe
    semi = final_alpha > 0
    mag_check = semi & (r > 120) & (b > 120) & (g < 100) & (((r.astype(int) + b.astype(int)) / 2) - g.astype(int) > 30)
    b[mag_check] = g[mag_check]
    r[mag_check] = np.clip(g[mag_check] + 15, 0, 255)
    
    rgba = np.dstack([r, g, b, final_alpha]).astype(np.uint8)
    out_img = Image.fromarray(rgba, mode="RGBA")
    
    # Crop na bounding box
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        
    os.makedirs(os.path.dirname(out_png_path), exist_ok=True)
    out_img.save(out_png_path, "PNG")
    print(f"Guindaste salvo: {out_png_path} ({out_img.size[0]}x{out_img.size[1]})")

if __name__ == "__main__":
    process_crane(sys.argv[1], sys.argv[2])
