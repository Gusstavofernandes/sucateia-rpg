import cv2
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
        "open_holes": False, # Portal chumbado na pedra
        "prompt": "A rugged underground mine tunnel entrance portal built into an old dark stone wall, front 3/4 perspective view facing directly south, perfectly aligned with orthogonal grid without any diagonal 45 degree tilt."
    },
    {
        "name": "estacao_guincho_vertical_v1",
        "raw_file": os.path.join(BRAIN_DIR, "estacao_guincho_vertical_v1_1791566083303.jpg"),
        "open_holes": True, # Grades e vãos vazados
        "prompt": "A single underground railway terminal buffer stop station platform, top-down 3/4 perspective strictly aligned with the vertical North-South axis without any diagonal 45 degree tilt."
    },
    {
        "name": "carrinho_mina_vertical_v1",
        "raw_file": os.path.join(BRAIN_DIR, "carrinho_mina_vertical_v1_1791566155303.jpg"),
        "open_holes": True, # Vãos entre rodas e caçamba
        "prompt": "A single underground industrial mining cart loaded with glowing green ore, top-down 3/4 perspective strictly aligned with the vertical North-South axis without any diagonal 45 degree tilt."
    }
]

for item in assets:
    name = item["name"]
    raw_path = item["raw_file"]
    print(f"\n--- Processando {name} ---")
    
    img = cv2.imread(raw_path)
    if img is None:
        print(f"Erro ao carregar {raw_path}")
        continue
        
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Magenta puro em HSV: H ~ [135, 175], S > 60, V > 60
    lower_magenta = np.array([135, 60, 60])
    upper_magenta = np.array([175, 255, 255])
    magenta_mask = cv2.inRange(hsv, lower_magenta, upper_magenta)
    
    # Sujeira / tons avermelhados de magenta
    lower_magenta2 = np.array([140, 40, 40])
    upper_magenta2 = np.array([170, 255, 255])
    magenta_mask2 = cv2.inRange(hsv, lower_magenta2, upper_magenta2)
    full_magenta = cv2.bitwise_or(magenta_mask, magenta_mask2)
    
    # Máscara do objeto = onde NÃO é magenta
    object_mask = cv2.bitwise_not(full_magenta)
    
    # Erosão suave na máscara para remover fringe de borda
    kernel = np.ones((3, 3), np.uint8)
    eroded_mask = cv2.erode(object_mask, kernel, iterations=1)
    
    # Despill: remover componente magenta residual nas bordas
    b, g, r = cv2.split(img)
    # Onde r > g e b > g e r ~ b (magenta fringe), limitar r e b
    is_fringe = (r > g + 25) & (b > g + 25)
    r[is_fringe] = np.minimum(r[is_fringe], g[is_fringe] + 15)
    b[is_fringe] = np.minimum(b[is_fringe], g[is_fringe] + 15)
    clean_bgr = cv2.merge([b, g, r])
    
    # Aplicar canal alfa
    rgba = cv2.cvtColor(clean_bgr, cv2.COLOR_BGR2BGRA)
    rgba[:, :, 3] = eroded_mask
    
    # Criar sombra de contato suave
    shadow_mask = cv2.dilate(eroded_mask, kernel, iterations=2)
    shadow_blurred = cv2.GaussianBlur(shadow_mask, (15, 15), 0)
    shadow_rgba = np.zeros_like(rgba)
    shadow_rgba[:, :, :3] = 0 # Preto
    shadow_rgba[:, :, 3] = (shadow_blurred * 0.55).astype(np.uint8)
    
    # Salvar nos diretórios
    out_main = os.path.join(DEST_STANDALONE, f"{name}.png")
    out_shadow = os.path.join(DEST_STANDALONE, f"{name}_sombra.png")
    out_txt = os.path.join(DEST_STANDALONE, f"{name}.txt")
    
    cv2.imwrite(out_main, rgba)
    cv2.imwrite(out_shadow, shadow_rgba)
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(item["prompt"])
        
    print(f"Salvo {out_main} ({rgba.shape[1]}x{rgba.shape[0]})")
    
    # Sincronizar com root
    shutil.copy2(out_main, os.path.join(DEST_ROOT, f"{name}.png"))
    shutil.copy2(out_shadow, os.path.join(DEST_ROOT, f"{name}_sombra.png"))
    shutil.copy2(out_txt, os.path.join(DEST_ROOT, f"{name}.txt"))

print("\n--- Todos os 3 assets foram processados e sincronizados com sucesso! ---")
