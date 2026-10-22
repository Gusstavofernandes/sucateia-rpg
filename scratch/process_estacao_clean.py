import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion

def process_estacao_clean(src, out_paths):
    im = Image.open(src).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    # Magenta
    is_mag = (r > 120) & (b > 120) & ((np.minimum(r, b) - g) > 50)
    
    # Sem binary_fill_holes para que os vãos do corrimão fiquem 100% transparentes
    mask = ~is_mag
    mask = binary_erosion(mask, iterations=2)

    # Despill
    excess = np.maximum(0.0, np.minimum(r, b) - g)
    r = np.clip(r - excess * 0.95, 0, 255)
    b = np.clip(b - excess * 0.95, 0, 255)

    alpha = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
    out = Image.fromarray(np.dstack([r, g, b, np.array(alpha, dtype=np.float32)]).astype(np.uint8))
    bbox = out.getbbox()
    if bbox:
        out = out.crop(bbox)

    w, h = out.size
    sh = out.split()[-1].resize((w, max(8, int(h * 0.25))), Image.Resampling.BILINEAR)
    sh_a = (np.array(sh, dtype=np.float32) * 0.55).astype(np.uint8)
    z = np.zeros_like(sh_a)
    shadow = Image.fromarray(np.dstack([z, z, z, sh_a])).filter(ImageFilter.GaussianBlur(5))

    for p in out_paths:
        out.save(p)
        shadow.save(p.replace(".png", "_sombra.png"))
        print(f"Salvo limpo: {p}")

paths = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\rails\estacao_plataforma_v1.png",
    r"c:\Users\Usuario\Documents\jogo\assets\rails\estacao_plataforma_v1.png"
]
process_estacao_clean(r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\estacao_guindaste_v1_1791563188346.jpg", paths)
