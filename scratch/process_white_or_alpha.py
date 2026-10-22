import os
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import binary_erosion, binary_fill_holes, label

ROOTS = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets",
    r"c:\Users\Usuario\Documents\jogo\assets",
]

def process_asset(src_path, subfolder, out_name, prompt_text, is_white_bg=True, shadow_ratio=0.30):
    im = Image.open(src_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

    if is_white_bg:
        # Fundo branco ou quase branco / cinza claro do checkerboard
        # Branco puro: R > 240, G > 240, B > 240
        # Checkerboard claro: R > 230, G > 230, B > 230 e pouca variacao cromatica
        is_bg = (r > 235) & (g > 235) & (b > 235)
        # Se houver quadriculado cinza-claro (ex: r, g, b entre 220 e 240 com diferenca quase nula)
        diff = np.maximum(np.maximum(np.abs(r - g), np.abs(r - b)), np.abs(g - b))
        is_checker = (r > 215) & (g > 215) & (b > 215) & (diff < 8)
        mask = ~(is_bg | is_checker)
    else:
        # Magenta
        is_mag = (r > 120) & (b > 120) & ((np.minimum(r, b) - g) > 60)
        mask = ~is_mag

    # Manter maior componente conectado
    lab, n = label(mask)
    if n > 1:
        sizes = np.bincount(lab.ravel())
        sizes[0] = 0
        mask = lab == sizes.argmax()

    mask = binary_fill_holes(mask)
    mask = binary_erosion(mask, iterations=2)

    # Nova imagem RGBA
    out_arr = np.dstack([r.astype(np.uint8), g.astype(np.uint8), b.astype(np.uint8), (mask * 255).astype(np.uint8)])
    out_img = Image.fromarray(out_arr)

    # Crop na bounding box
    bbox = out_img.split()[-1].getbbox()
    if bbox:
        out_img = out_img.crop(bbox)

    # Sombra de contato suave
    w, h = out_img.size
    sh = out_img.split()[-1].resize((w, max(8, int(h * shadow_ratio))), Image.Resampling.BILINEAR)
    sh_a = (np.array(sh, dtype=np.float32) * 0.55).astype(np.uint8)
    z = np.zeros_like(sh_a)
    shadow = Image.fromarray(np.dstack([z, z, z, sh_a])).filter(ImageFilter.GaussianBlur(3))

    for root in ROOTS:
        d = os.path.join(root, subfolder)
        os.makedirs(d, exist_ok=True)
        out_img.save(os.path.join(d, out_name))
        shadow.save(os.path.join(d, out_name.replace(".png", "_sombra.png")))
        with open(os.path.join(d, out_name.replace(".png", ".txt")), "w", encoding="utf-8") as f:
            f.write(prompt_text)

    print(f"Sucesso: {out_name} - Tamanho final: {out_img.size}")

if __name__ == "__main__":
    # 1. Cano industrial reto v4
    p1 = "videogame asset sprite, transparent pure white background. Pure side orthographic profile view, exactly perpendicular to camera, 2.5D game tile. A seamless modular straight industrial pipe, symmetrical left and right ends. Both left and right ends terminate in vertical flat flanges with bolts seen from direct side profile with NO hollow interior visible, no hole, completely sealed flush flanges ready to tile horizontally. The pipe body is smooth dark cast iron and aged copper with greenish patina, rivets, long clean cylinder. High quality hand-painted texture, rim light on top, dark underbelly. Isolated on pure white."
    process_asset(
        r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\cano_industrial_perfil_reto_v4_1791338333460.jpg",
        "pipes",
        "cano_reto_industrial_v4.png",
        p1,
        is_white_bg=True,
        shadow_ratio=0.28
    )

    # 2. Colar de conexao da bomba v4
    p2 = "videogame asset sprite, transparent pure white background. Direct side orthographic profile view of a heavy circular pipe union collar and coupling flange. Made of cast iron and oxidized copper with bolts and rivets. Modest proportion, short compact sleeve coupling to join two pipes or connect a pipe to a pump socket. No giant funnel, no flared trumpet, no cone shape. Just a sturdy cylindrical coupling collar with twin bolt flanges and a black rubber gasket ring in between. Isolated on pure white."
    process_asset(
        r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\colar_conexao_bomba_v4_1791338437653.jpg",
        "pipes",
        "tubo_colar_conexao_v4.png",
        p2,
        is_white_bg=True,
        shadow_ratio=0.25
    )

    # 3. Cabos eleteicos industriais v1
    p3 = "videogame asset sprite, transparent pure white background. Bundle of thick industrial black electric cables and wires strapped together with rusty brass clamps, hanging slightly, sagging naturally along a straight horizontal path. Heavy duty electrical conduit and worn insulated wires, dark rubber texture, metal zip-ties and clamps every few feet. Isolated horizontal strip, side view in 2.5D game perspective. No background, pure white backdrop. Detailed gritty dieselpunk goblin technology."
    process_asset(
        r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\cabos_eletricos_tubo_v1_1791338231269.jpg",
        "pipes",
        "cabos_eletricos_industrial_v1.png",
        p3,
        is_white_bg=True,
        shadow_ratio=0.22
    )
