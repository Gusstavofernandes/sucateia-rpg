from PIL import Image, ImageFilter
import numpy as np
import os
import shutil

BRAIN_DIR = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b"
DEST_STANDALONE = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\rails"
DEST_ROOT = r"c:\Users\Usuario\Documents\jogo\assets\rails"

os.makedirs(DEST_STANDALONE, exist_ok=True)
os.makedirs(DEST_ROOT, exist_ok=True)

assets = [
    {
        "name": "tunel_mina_norte_v1",
        "raw_file": os.path.join(BRAIN_DIR, "tunel_mina_norte_v1_1791566014187.jpg"),
        "prompt": "A rugged underground mine tunnel entrance portal built into an old dark stone wall, front 3/4 perspective view facing directly south, perfectly aligned with orthogonal grid without any diagonal 45 degree tilt."
    },
    {
        "name": "estacao_guincho_vertical_v1",
        "raw_file": os.path.join(BRAIN_DIR, "estacao_guincho_vertical_v1_1791566083303.jpg"),
        "prompt": "A single underground railway terminal buffer stop station platform, top-down 3/4 perspective strictly aligned with the vertical North-South axis without any diagonal 45 degree tilt."
    },
    {
        "name": "carrinho_mina_vertical_v1",
        "raw_file": os.path.join(BRAIN_DIR, "carrinho_mina_vertical_v1_1791566155303.jpg"),
        "prompt": "A single underground industrial mining cart loaded with glowing green ore, top-down 3/4 perspective strictly aligned with the vertical North-South axis without any diagonal 45 degree tilt."
    }
]

for item in assets:
    name = item["name"]
    raw_path = item["raw_file"]
    print(f"\n--- Processando {name} ---")
    
    img = Image.open(raw_path).convert("RGBA")
    arr = np.array(img, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Detecção de magenta (#FF00FF): R alto, B alto, G muito baixo
    # Distância Euclidiana da cor até o magenta puro (255, 0, 255)
    dist_magenta = np.sqrt((r - 255)**2 + g**2 + (b - 255)**2)
    is_magenta = (dist_magenta < 155) | ((r > 160) & (b > 160) & (g < 110))
    
    # Máscara binária
    alpha = np.where(is_magenta, 0, 255).astype(np.uint8)
    mask_img = Image.fromarray(alpha, mode="L")
    
    # Erosão de 1px usando filtro MinFilter (remover borda residual)
    eroded_mask = mask_img.filter(ImageFilter.MinFilter(3))
    eroded_arr = np.array(eroded_mask)
    
    # Despill: remover reflexo magenta nas bordas do sprite
    # Onde r > g + 20 e b > g + 20, reduzir r e b para perto de g
    is_fringe = (r > g + 20) & (b > g + 20)
    arr[:, :, 0][is_fringe] = np.minimum(r[is_fringe], g[is_fringe] + 15)
    arr[:, :, 2][is_fringe] = np.minimum(b[is_fringe], g[is_fringe] + 15)
    
    arr[:, :, 3] = eroded_arr
    final_img = Image.fromarray(arr.astype(np.uint8), mode="RGBA")
    
    # Sombra de contato suave
    shadow_mask = eroded_mask.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(8))
    shadow_arr = np.zeros_like(arr, dtype=np.uint8)
    shadow_arr[:, :, 3] = (np.array(shadow_mask, dtype=np.float32) * 0.55).astype(np.uint8)
    shadow_img = Image.fromarray(shadow_arr, mode="RGBA")
    
    # Salvar
    out_main = os.path.join(DEST_STANDALONE, f"{name}.png")
    out_shadow = os.path.join(DEST_STANDALONE, f"{name}_sombra.png")
    out_txt = os.path.join(DEST_STANDALONE, f"{name}.txt")
    
    final_img.save(out_main)
    shadow_img.save(out_shadow)
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(item["prompt"])
        
    print(f"Salvo {out_main} ({final_img.size[0]}x{final_img.size[1]})")
    
    # Sincronizar com root
    shutil.copy2(out_main, os.path.join(DEST_ROOT, f"{name}.png"))
    shutil.copy2(out_shadow, os.path.join(DEST_ROOT, f"{name}_sombra.png"))
    shutil.copy2(out_txt, os.path.join(DEST_ROOT, f"{name}.txt"))

print("\n--- Concluído com sucesso! ---")
