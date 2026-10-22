from PIL import Image
import os

files = {
    "tunel": "assets/rails/boca_tunel_v2.png",
    "estacao": "assets/rails/estacao_trilho_v2.png",
    "cavalete": "assets/rails/cavalete_alto_v1.png",
    "trilho_vertical": "assets/rails/trilho_reto_vertical_v1.png"
}

for k, path in files.items():
    if os.path.exists(path):
        im = Image.open(path)
        print(f"[{k}] {path} -> Size: {im.size}, Mode: {im.mode}")
    else:
        print(f"[{k}] {path} NOT FOUND")
