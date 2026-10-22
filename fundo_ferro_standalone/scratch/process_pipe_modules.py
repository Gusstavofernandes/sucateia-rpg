import os
import glob
from PIL import Image, ImageFilter
import numpy as np
from scipy.ndimage import binary_erosion

def process_assets():
    artifact_dir = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b"
    target_dirs = [
        r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes",
        r"c:\Users\Usuario\Documents\jogo\assets\pipes"
    ]
    for td in target_dirs:
        os.makedirs(td, exist_ok=True)

    items = [
        ("cano_modular_reto_*.jpg", "cano_modular_reto.png"),
        ("cano_modular_cotovelo_*.jpg", "cano_modular_cotovelo.png"),
        ("cano_valvula_registro_*.jpg", "cano_valvula_registro.png"),
        ("cano_berco_apoio_*.jpg", "cano_berco_apoio.png"),
        ("cano_travessia_ponte_*.jpg", "cano_travessia_ponte.png"),
        ("passagem_parede_flange_*.jpg", "passagem_parede_flange.png"),
    ]

    for pattern, out_name in items:
        files = glob.glob(os.path.join(artifact_dir, pattern))
        if not files:
            print(f"ERRO: Nao encontrado arquivo para {pattern}")
            continue
        # Pega o arquivo mais recente
        files.sort(key=os.path.getmtime, reverse=True)
        src_path = files[0]
        print(f"Processando {src_path} -> {out_name}")

        im = Image.open(src_path).convert("RGBA")
        arr = np.array(im, dtype=np.float32)

        r = arr[:, :, 0]
        g = arr[:, :, 1]
        b = arr[:, :, 2]

        # Deteccao de magenta: R alto, B alto, G significativamente mais baixo
        # Magenta puro = (255, 0, 255)
        is_magenta = (r > 150) & (b > 150) & (g < 130) & ((r + b) / 2.0 - g > 45)

        # Mascara opaca
        mask = (~is_magenta).astype(bool)

        # Erosao de 2 pixels para remover halo
        mask = binary_erosion(mask, iterations=2)

        # Despill de magenta nas bordas
        # Onde R e B excedem G, atenuar R e B
        excess = np.maximum(0.0, np.minimum(r, b) - g)
        r = np.clip(r - excess * 0.95, 0, 255)
        b = np.clip(b - excess * 0.95, 0, 255)

        # Alpha final
        alpha = np.where(mask, 255.0, 0.0)

        # Suavizar levemente o contorno alpha
        alpha_img = Image.fromarray(alpha.astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=0.6))
        clean_alpha = np.array(alpha_img)

        # Montar imagem final limpa
        clean_arr = np.dstack([r.astype(np.uint8), g.astype(np.uint8), b.astype(np.uint8), clean_alpha])
        clean_img = Image.fromarray(clean_arr)

        # Crop inteligente na bounding box de pixels nao-transparentes
        bbox = clean_img.getbbox()
        if bbox:
            clean_img = clean_img.crop(bbox)

        # Gerar sombra de contato suave (losango/silhueta escura com GaussianBlur)
        sh_alpha = np.array(clean_img.split()[-1], dtype=np.float32)
        # Achatar verticalmente para 40% da altura para simular projecao isometrica no piso
        sh_w, sh_h = clean_img.size
        proj_h = max(10, int(sh_h * 0.38))
        sh_resized = clean_img.split()[-1].resize((sh_w, proj_h), Image.Resampling.BILINEAR)
        
        sh_arr = np.array(sh_resized, dtype=np.float32)
        sh_alpha_final = np.clip(sh_arr * 0.55, 0, 255).astype(np.uint8)
        zeros = np.zeros_like(sh_alpha_final)
        sh_rgba = np.dstack([zeros, zeros, zeros, sh_alpha_final])
        shadow_img = Image.fromarray(sh_rgba).filter(ImageFilter.GaussianBlur(radius=4.0))

        # Salvar nos destinos
        for td in target_dirs:
            out_path = os.path.join(td, out_name)
            clean_img.save(out_path)
            sh_path = os.path.join(td, out_name.replace(".png", "_sombra.png"))
            shadow_img.save(sh_path)

        print(f"OK: {out_name} e sombra salvos com sucesso! Dimensoes: {clean_img.size}")

if __name__ == "__main__":
    process_assets()
