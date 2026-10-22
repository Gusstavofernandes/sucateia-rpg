import sys
import os
from PIL import Image, ImageFilter
import numpy as np

def remove_magenta_and_crop(input_path, output_path, shadow_path=None):
    if not os.path.exists(input_path):
        print(f"Error: input not found {input_path}")
        return False
        
    img = Image.open(input_path).convert("RGBA")
    arr = np.array(img, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Distância Euclidiana em relação ao Magenta puro (255, 0, 255)
    # Magenta puro: R=255, G=0, B=255
    # Fator de exclusão para magenta: alta intensidade de R e B, baixa de G
    diff_r = np.abs(r - 255.0)
    diff_g = g
    diff_b = np.abs(b - 255.0)
    
    # Cor magenta típica de chroma: R > 180, B > 180, G < 120 e (R+B)/2 - G > 70
    is_magenta = (r > 160) & (b > 160) & (g < 130) & ((r + b) * 0.5 - g > 60)
    
    # Calcular alfa baseado na semelhança com magenta
    dist = np.sqrt(diff_r**2 + diff_g**2 + diff_b**2)
    
    # Transição suave de borda (antialiasing) entre dist 60 e dist 140
    alpha = np.clip((dist - 65.0) / 75.0, 0.0, 1.0)
    
    # Zera onde é definitivamente magenta
    alpha[is_magenta & (dist < 110.0)] = 0.0
    
    # Descontaminação de cor magenta nas bordas (onde alfa < 1.0)
    # Se ainda houver excesso de magenta nos pixels semitransparentes, removemos o tom arroxeado
    edge_mask = (alpha > 0.0) & (alpha < 0.95) & (is_magenta | ((r > g) & (b > g)))
    avg_rb = (r[edge_mask] + b[edge_mask]) * 0.5
    excess = np.maximum(0.0, avg_rb - g[edge_mask])
    arr[:, :, 0][edge_mask] = np.clip(r[edge_mask] - excess * 0.6, 0, 255)
    arr[:, :, 2][edge_mask] = np.clip(b[edge_mask] - excess * 0.6, 0, 255)
    
    arr[:, :, 3] = alpha * 255.0
    
    clean_img = Image.fromarray(np.uint8(arr), mode="RGBA")
    
    # Recorte (Crop) para o Bounding Box onde alpha > 10
    bbox = clean_img.getbbox()
    if bbox:
        # Adicionar padding de 2px se possível
        pad = 2
        w, h = clean_img.size
        box = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad))
        clean_img = clean_img.crop(box)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    clean_img.save(output_path, "PNG")
    print(f"Salvo asset limpo: {output_path} ({clean_img.size[0]}x{clean_img.size[1]})")
    
    # Se solicitado caminho de sombra
    if shadow_path:
        # Criar silhueta de sombra
        shadow_arr = np.array(clean_img, dtype=np.float32)
        sh_alpha = shadow_arr[:, :, 3] / 255.0
        
        # Sombra preta com opacidade máxima de 45%
        shadow_arr[:, :, 0] = 0
        shadow_arr[:, :, 1] = 0
        shadow_arr[:, :, 2] = 0
        shadow_arr[:, :, 3] = sh_alpha * 115.0 # ~45% de 255
        
        shadow_img = Image.fromarray(np.uint8(shadow_arr), mode="RGBA")
        shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius=5))
        
        os.makedirs(os.path.dirname(os.path.abspath(shadow_path)), exist_ok=True)
        shadow_img.save(shadow_path, "PNG")
        print(f"Salva sombra suave: {shadow_path}")
        
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_coastal_terrain_assets.py <input> <output> [shadow_output]")
        sys.exit(1)
    shadow = sys.argv[3] if len(sys.argv) > 3 else None
    remove_magenta_and_crop(sys.argv[1], sys.argv[2], shadow)
