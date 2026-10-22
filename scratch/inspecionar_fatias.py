from PIL import Image
import numpy as np

def inspect_rows(img_path, y_values):
    im = Image.open(img_path).convert("RGBA")
    arr = np.array(im)
    print(f"\n--- Inspecionando {img_path} ---")
    for y in y_values:
        row = arr[y, :, :]
        # Encontrar onde alfa > 50
        opaque = np.where(row[:, 3] > 50)[0]
        if len(opaque) == 0:
            print(f"Y={y}: linha vazia")
            continue
        print(f"Y={y}: opaco de X={opaque[0]} a X={opaque[-1]} (W={opaque[-1]-opaque[0]+1})")

inspect_rows("assets/rails/estacao_trilho_v2.png", [10, 200, 400, 600, 800])
inspect_rows("assets/rails/trilho_reto_vertical_v1.png", [10, 100, 200, 500, 800, 970])
