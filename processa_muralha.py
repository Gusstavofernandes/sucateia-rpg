from PIL import Image
import numpy as np

def remove_magenta(img_path, threshold=60):
    im = Image.open(img_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Magenta puro: R alto, B alto, G baixo
    # Distancia de (255, 0, 255) ou (R > G + 40 e B > G + 40)
    diff_rg = r - g
    diff_bg = b - g
    magenta_intensity = np.minimum(diff_rg, diff_bg)
    
    # Mascara binaria / alpha suave
    # onde magenta_intensity > threshold -> transparente
    alpha = np.clip(1.0 - (magenta_intensity - 30) / (threshold - 30 + 1e-5), 0.0, 1.0)
    
    # Despill: remover componente magenta onde ha transicao
    # Substituir R e B em excesso pela media com G
    despill_mask = magenta_intensity > 10
    arr[:, :, 0] = np.where(despill_mask, np.minimum(r, np.maximum(g * 1.1, b * 0.5)), r)
    arr[:, :, 2] = np.where(despill_mask, np.minimum(b, np.maximum(g * 1.1, r * 0.5)), b)
    
    arr[:, :, 3] = arr[:, :, 3] * alpha
    
    return Image.fromarray(np.uint8(np.clip(arr, 0, 255)), mode="RGBA")

# 1. Processar Imagem 1 (Muralha Norte Curva)
im1_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_muralha_norte_curva_raw_1792526009524.jpg'
clean_im1 = remove_magenta(im1_path, threshold=60)
clean_im1.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_muralha_norte_curva_clean.png')
print("Muralha Norte salva.")

# 2. Processar Imagem 2 (Anel Completo e Mureta Sul)
im2_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_muralha_sul_curva_raw_1792526103046.jpg'
clean_im2 = remove_magenta(im2_path, threshold=60)
clean_im2.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_muralha_sul_clean.png')
print("Muralha Sul salva.")
