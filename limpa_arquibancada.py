from PIL import Image
import numpy as np

def clean_bleachers():
    raw_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_arquibancada_meia_lua_raw_1792536396530.jpg'
    im = Image.open(raw_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Chroma key magenta
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
    
    clean_im = Image.fromarray(np.uint8(np.clip(arr, 0, 255)), mode="RGBA")
    clean_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_arquibancada_meia_lua_clean.png'
    clean_im.save(clean_path)
    
    print("Arquibancada limpa salva:", clean_im.size)

clean_bleachers()
