import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion

def process_cavalete(src, out_paths):
    im = Image.open(src).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    # Magenta: R e B altos e G bem baixo
    is_mag = (r > 120) & (b > 120) & ((np.minimum(r, b) - g) > 50)
    
    # Objeto sólido = não magenta (SEM preencher buracos internos, para o arco ficar oco e transparente!)
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

    # Sombra de contato sob as sapatas dos pilares
    w, h = out.size
    sh = out.split()[-1].resize((w, max(8, int(h * 0.2))), Image.Resampling.BILINEAR)
    sh_a = (np.array(sh, dtype=np.float32) * 0.6).astype(np.uint8)
    z = np.zeros_like(sh_a)
    shadow = Image.fromarray(np.dstack([z, z, z, sh_a])).filter(ImageFilter.GaussianBlur(5))

    prompt = open(r"c:\Users\Usuario\Documents\jogo\scratch\prompts\cavalete_alto_v2.txt", encoding="utf-8").read()

    for p in out_paths:
        out.save(p)
        shadow.save(p.replace(".png", "_sombra.png"))
        with open(p.replace(".png", ".txt"), "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"Salvo: {p}")

paths = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\rails\cavalete_alto_v1.png",
    r"c:\Users\Usuario\Documents\jogo\assets\rails\cavalete_alto_v1.png"
]
process_cavalete(r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\cavalete_alto_v2_1791562222640.jpg", paths)
