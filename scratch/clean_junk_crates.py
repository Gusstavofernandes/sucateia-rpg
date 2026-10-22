from PIL import Image, ImageFilter
import numpy as np
import os

src_path = r'c:\Users\Usuario\Documents\jogo\assets\reconstruction\market_junk_crates.png'
if os.path.exists(src_path):
    img = Image.open(src_path).convert("RGBA")
    arr = np.array(img, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    # White background distance
    white_dist = np.sqrt((255.0 - r)**2 + (255.0 - g)**2 + (255.0 - b)**2)
    alpha = np.clip((white_dist - 20.0) / 35.0, 0.0, 1.0)
    arr[:, :, 3] = (alpha * 255.0).astype(np.uint8)
    clean = Image.fromarray(arr.astype(np.uint8), mode="RGBA")
    
    out_dirs = [
        r'c:\Users\Usuario\Documents\jogo\assets\props',
        r'c:\Users\Usuario\Documents\jogo\assets\reconstruction'
    ]
    for od in out_dirs:
        clean.save(os.path.join(od, 'lixao_caixotes_engrenagens.png'))
    print("Salvo lixao_caixotes_engrenagens.png com fundo transparente!")
