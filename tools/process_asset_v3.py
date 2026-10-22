"""Pós-processamento padrão dos assets gerados (Nano Banana, fundo magenta #FF00FF).

Uso: python process_asset_v3.py <arquivo_fonte> <subpasta assets> <nome_saida.png> <arquivo_prompt.txt>
- Chroma key magenta + despill (reduz R e B quando dominam G)
- Erosão de 2 px da máscara (remove halo)
- Crop na bounding box
- Sombra de contato separada (<nome>_sombra.png), achatada e desfocada
- Prompt salvo ao lado (<nome>.txt)
- Copia para o standalone e para o projeto raiz
"""
import os
import sys
import shutil
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion, binary_fill_holes, label

ROOTS = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets",
    r"c:\Users\Usuario\Documents\jogo\assets",
]


def process(src: str, sub: str, out_name: str, prompt_file: str, shadow_ratio: float = 0.30) -> None:
    im = Image.open(src).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    # Magenta: R e B altos e G bem abaixo (inclui variações de compressão JPG)
    is_mag = (r > 120) & (b > 120) & ((np.minimum(r, b) - g) > 60)
    mask = ~is_mag
    # Mantém apenas o maior componente conectado (objeto único) e fecha buracos internos
    lab, n = label(mask)
    if n > 1:
        sizes = np.bincount(lab.ravel())
        sizes[0] = 0
        mask = lab == sizes.argmax()
    mask = binary_fill_holes(mask)
    mask = binary_erosion(mask, iterations=2)

    # Despill
    excess = np.maximum(0.0, np.minimum(r, b) - g)
    r = np.clip(r - excess * 0.95, 0, 255)
    b = np.clip(b - excess * 0.95, 0, 255)

    alpha = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
    out = Image.fromarray(np.dstack([r, g, b, np.array(alpha, dtype=np.float32)]).astype(np.uint8))
    out = out.crop(out.getbbox())

    # Sombra de contato separada
    w, h = out.size
    sh = out.split()[-1].resize((w, max(8, int(h * shadow_ratio))), Image.Resampling.BILINEAR)
    sh_a = (np.array(sh, dtype=np.float32) * 0.6).astype(np.uint8)
    z = np.zeros_like(sh_a)
    shadow = Image.fromarray(np.dstack([z, z, z, sh_a])).filter(ImageFilter.GaussianBlur(4))

    prompt = open(prompt_file, encoding="utf-8").read()
    for root in ROOTS:
        d = os.path.join(root, sub)
        os.makedirs(d, exist_ok=True)
        out.save(os.path.join(d, out_name))
        shadow.save(os.path.join(d, out_name.replace(".png", "_sombra.png")))
        with open(os.path.join(d, out_name.replace(".png", ".txt")), "w", encoding="utf-8") as f:
            f.write(prompt)
    print(f"OK {out_name}: {out.size}")


if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], float(sys.argv[5]) if len(sys.argv) > 5 else 0.30)
