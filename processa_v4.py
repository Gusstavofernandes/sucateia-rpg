from PIL import Image
import numpy as np

def process_v4():
    raw_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_coliseu_imponente_completo_raw_1792544793988.jpg'
    im = Image.open(raw_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Chroma key
    diff_rg = r - g
    diff_bg = b - g
    magenta_intensity = np.minimum(diff_rg, diff_bg)
    
    threshold = 55.0
    alpha = np.clip(1.0 - (magenta_intensity - 25.0) / (threshold - 25.0 + 1e-5), 0.0, 1.0)
    
    # Despill
    despill_mask = magenta_intensity > 8.0
    arr[:, :, 0] = np.where(despill_mask, np.minimum(r, np.maximum(g * 1.1, b * 0.5)), r)
    arr[:, :, 2] = np.where(despill_mask, np.minimum(b, np.maximum(g * 1.1, r * 0.5)), b)
    
    arr[:, :, 3] = arr[:, :, 3] * alpha
    clean_arr = np.uint8(np.clip(arr, 0, 255))
    h, w, _ = clean_arr.shape
    
    im_clean = Image.fromarray(clean_arr, mode="RGBA")
    
    # Geometria do fosso rebaixado na imagem:
    # cx = 688, cy = 555, rx = 365, ry = 125
    cx = 688
    cy = 555
    rx = 365
    ry = 125
    
    y_indices, x_indices = np.indices((h, w))
    dist_elipse_fosso = ((x_indices - cx) / rx) ** 2 + ((y_indices - cy) / ry) ** 2
    
    # 1. PISO DO FOSSO REBAIXADO
    mask_piso = (dist_elipse_fosso <= 0.98) & (y_indices >= 430) & (y_indices <= 685) & (clean_arr[:, :, 3] > 0)
    
    # 2. MURETA FRONTAL SUL
    mask_sul = np.zeros((h, w), dtype=bool)
    mask_sul[(x_indices >= 530) & (x_indices <= 845) & (y_indices >= 540) & (clean_arr[:, :, 3] > 0)] = True
    mask_sul[(dist_elipse_fosso >= 0.94) & (y_indices >= 500) & (clean_arr[:, :, 3] > 0)] = True
    mask_sul[(x_indices <= 330) & (y_indices >= 340) & (clean_arr[:, :, 3] > 0)] = True
    mask_sul[(x_indices >= 1045) & (y_indices >= 340) & (clean_arr[:, :, 3] > 0)] = True
    mask_sul &= ~mask_piso
    
    # 3. CAMADA NORTE (Arquibancada em Meia-Lua com torres e muralha de fundo)
    mask_norte = (clean_arr[:, :, 3] > 0) & (~mask_sul) & (~mask_piso)
    
    arr_norte = np.zeros_like(clean_arr)
    arr_norte[mask_norte] = clean_arr[mask_norte]
    
    arr_piso = np.zeros_like(clean_arr)
    arr_piso[mask_piso] = clean_arr[mask_piso]
    
    arr_sul = np.zeros_like(clean_arr)
    arr_sul[mask_sul] = clean_arr[mask_sul]
    
    # Sombra profunda do fosso
    arr_sombra = np.zeros_like(clean_arr)
    mask_sombra = mask_piso & (y_indices < cy - 10)
    arr_sombra[mask_sombra, 3] = 115
    
    im_norte = Image.fromarray(arr_norte)
    im_piso = Image.fromarray(arr_piso)
    im_sul = Image.fromarray(arr_sul)
    im_sombra = Image.fromarray(arr_sombra)
    
    dest_dirs = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props',
        r'c:\Users\Usuario\Documents\jogo\assets\props',
        r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'
    ]
    
    files = {
        'arena_coliseu_imponente_completo_v4.png': im_clean,
        'arena_coliseu_imponente_norte_v4.png': im_norte,
        'arena_coliseu_imponente_piso_v4.png': im_piso,
        'arena_coliseu_imponente_sul_v4.png': im_sul,
        'arena_coliseu_imponente_sombra_v4.png': im_sombra
    }
    
    for d in dest_dirs:
        for fname, img_obj in files.items():
            path = f"{d}\\{fname}"
            img_obj.save(path)
            
    print("Versao v4 salva com sucesso em todos os diretorios!")

process_v4()
