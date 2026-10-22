import os
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion

def process_metal_bridge(src_path: str, out_png_path: str):
    img = Image.open(src_path).convert("RGB")
    arr = np.array(img, dtype=np.float32)
    
    h, w, _ = arr.shape
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Detecção de magenta refinada (incluindo transições de compressão)
    avg_rb = (r + b) / 2.0
    magenta_diff = avg_rb - g
    is_magenta = (r > 105) & (b > 105) & (g < 130) & (magenta_diff > 25)
    
    # Região do deck (passadiço central)
    # y ~ 160 até 445, x ~ 195 até 1175
    deck_mask = np.zeros((h, w), dtype=bool)
    deck_mask[160:445, 195:1175] = True
    
    # Na grelha do deck interno: preencher os vazados com fundo de fosso escuro
    internal_grate = is_magenta & deck_mask
    
    # Criar tom escuro de chapa/profundidade industrial
    np.random.seed(42)
    noise = np.random.uniform(-4, 4, size=(h, w))
    arr[internal_grate, 0] = np.clip(38.0 + noise[internal_grate], 25, 50)
    arr[internal_grate, 1] = np.clip(32.0 + noise[internal_grate], 22, 42)
    arr[internal_grate, 2] = np.clip(28.0 + noise[internal_grate], 18, 38)
    
    # Atualizar canais
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    avg_rb = (r + b) / 2.0
    magenta_diff = avg_rb - g
    
    # O que resta de magenta é estritamente externo (ao redor do objeto e entre as correntes)
    external_bg = (r > 95) & (b > 95) & (g < 140) & (magenta_diff > 18)
    
    # Máscara do objeto: True onde é sólido/visível, False onde é fundo
    obj_mask = ~external_bg
    
    # Despill completo: onde ainda houver qualquer excesso de magenta (ex: reflexo em bordas de ferro e correntes)
    excess = np.maximum(0.0, np.minimum(r, b) - g)
    r = np.clip(r - excess * 1.05, 0, 255)
    b = np.clip(b - excess * 1.05, 0, 255)
    
    # Se ainda tiver R e B muito acima de G (magenta residual em semi-transparência)
    still_magenta = (r > 100) & (b > 100) & ((np.minimum(r, b) - g) > 20)
    # Forçar tonalidade neutra/ferrugem escura (B igual a G, R levemente quente)
    b[still_magenta] = g[still_magenta]
    r[still_magenta] = np.clip(g[still_magenta] * 1.2 + 10, 0, 180)
    
    # Alpha: suavizado nas bordas
    alpha = (obj_mask.astype(np.float32) * 255.0)
    
    # Suave erosão de 1 pixel apenas nas bordas externas do objeto para eliminar franjas
    # mantendo os detalhes finos das correntes
    eroded_mask = binary_erosion(obj_mask, iterations=1)
    # Transição suave entre eroded e obj_mask
    alpha = np.where(eroded_mask, 255.0, np.where(obj_mask, 140.0, 0.0))
    
    # Desfoque muito sutil no alpha (0.5px) para antialiasing perfeito
    alpha_img = Image.fromarray(alpha.astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.4))
    final_alpha = np.array(alpha_img, dtype=np.uint8)
    
    # Garantir que fundo externo seja 0 absoluto
    final_alpha[~obj_mask] = 0
    
    # Limpeza final dos pixels semi-transparentes para garantir zero magenta residual
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
    print(f"Sucesso: {out_png_path} ({out_img.size[0]}x{out_img.size[1]})")

if __name__ == "__main__":
    process_metal_bridge(sys.argv[1], sys.argv[2])
