import os
from PIL import Image, ImageFilter
import numpy as np
from scipy.ndimage import label, find_objects

def process_small_rocks():
    raw_path = "C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/pequenas_pedras_solo_costeiro_1792611222001.jpg"
    img = Image.open(raw_path).convert("RGB")
    arr = np.array(img, dtype=np.float32)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    
    # 1. Detecção rigorosa de magenta
    is_magenta = (b - g > 20.0) & (r - g > 30.0) & (g < 130.0)
    
    # 2. Alfa suave
    rb_excess = np.minimum(b - g, r - g)
    alpha = np.clip(1.0 - (rb_excess - 10.0) / 14.0, 0.0, 1.0)
    alpha[is_magenta] = 0.0
    
    # 3. Descontaminação de cor magenta nas bordas
    semi = (alpha > 0.0) & (alpha < 0.98) & (b > g)
    if np.any(semi):
        arr[:,:,2][semi] = np.clip(g[semi] * 0.95, 0, 255)
        arr[:,:,0][semi] = np.clip((arr[:,:,0][semi] + g[semi]) * 0.5, 0, 255)
        
    # Zera bordas de 3px
    alpha[:3, :] = 0.0
    alpha[-3:, :] = 0.0
    alpha[:, :3] = 0.0
    alpha[:, -3:] = 0.0
    
    out_arr = np.dstack([np.clip(arr, 0, 255).astype(np.uint8), (alpha * 255.0).astype(np.uint8)])
    clean_img = Image.fromarray(out_arr, "RGBA")
    
    # Bounding box
    bbox = clean_img.getbbox()
    if bbox:
        pad = 2
        w, h = clean_img.size
        box = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad))
        clean_img = clean_img.crop(box)
        
    out_dir = "assets/reconstruction/"
    os.makedirs(out_dir, exist_ok=True)
    
    # Salvar asset completo
    main_path = os.path.join(out_dir, "pequenas_pedras_solo_costeiro.png")
    clean_img.save(main_path, "PNG")
    print(f"Salvo main: {main_path} ({clean_img.size})")
    
    # Salvar sombra do asset completo
    save_shadow(clean_img, os.path.join(out_dir, "pequenas_pedras_solo_costeiro_sombra.png"))
    
    # Agora extrair 3 variações menores a partir das diferentes áreas horizontais (esquerda, centro, direita)
    cw, ch = clean_img.size
    
    # Variação A (Terço esquerdo)
    sub_a = clean_img.crop((0, 0, int(cw * 0.38), ch))
    save_cropped_subpiece(sub_a, os.path.join(out_dir, "pequenas_pedras_var_a.png"), os.path.join(out_dir, "pequenas_pedras_var_a_sombra.png"))
    
    # Variação B (Centro)
    sub_b = clean_img.crop((int(cw * 0.30), 0, int(cw * 0.72), ch))
    save_cropped_subpiece(sub_b, os.path.join(out_dir, "pequenas_pedras_var_b.png"), os.path.join(out_dir, "pequenas_pedras_var_b_sombra.png"))
    
    # Variação C (Terço direito)
    sub_c = clean_img.crop((int(cw * 0.64), 0, cw, ch))
    save_cropped_subpiece(sub_c, os.path.join(out_dir, "pequenas_pedras_var_c.png"), os.path.join(out_dir, "pequenas_pedras_var_c_sombra.png"))

def save_cropped_subpiece(img, path, shadow_path):
    bbox = img.getbbox()
    if bbox:
        cropped = img.crop(bbox)
        # Garantir fade de borda de 2px
        arr = np.array(cropped, dtype=np.float32)
        h, w = arr.shape[:2]
        arr[0, :, 3] = 0
        arr[-1, :, 3] = 0
        arr[:, 0, 3] = 0
        arr[:, -1, 3] = 0
        final_img = Image.fromarray(np.uint8(arr), "RGBA")
        final_img.save(path, "PNG")
        print(f"Salvo subpiece: {path} ({final_img.size})")
        save_shadow(final_img, shadow_path)

def save_shadow(img, shadow_path):
    sw, sh = img.size
    arr = np.array(img, dtype=np.float32)
    a = arr[:, :, 3] / 255.0
    
    # Sombra na base do objeto
    y_weight = np.linspace(0.0, 1.0, sh)[:, None]
    base_weight = np.clip((y_weight - 0.35) / 0.55, 0.0, 1.0)
    sh_alpha = a * base_weight * 90.0 # ~35%
    
    # Fade suave nas 4 bordas para nunca encostar nas extremidades
    y, x = np.mgrid[0:sh, 0:sw]
    d = np.minimum(np.minimum(x, sw - 1 - x), np.minimum(y, sh - 1 - y))
    fade = np.clip(d / 8.0, 0.0, 1.0)
    sh_alpha = sh_alpha * fade
    
    sh_arr = np.zeros((sh, sw, 4), dtype=np.uint8)
    sh_arr[:, :, 3] = np.uint8(sh_alpha)
    
    sh_img = Image.fromarray(sh_arr, "RGBA").filter(ImageFilter.GaussianBlur(radius=4))
    sh_img.save(shadow_path, "PNG")
    print(f"Sombra salva: {shadow_path}")

if __name__ == "__main__":
    process_small_rocks()
