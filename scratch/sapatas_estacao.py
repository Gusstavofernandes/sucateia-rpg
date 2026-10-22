from PIL import Image
import numpy as np

img_est = Image.open("assets/rails/estacao_trilho_v2.png").convert("RGBA")
arr_est = np.array(img_est)

for y in [805, 808]:
    row = arr_est[y, :, :]
    lum = 0.299 * row[:, 0] + 0.587 * row[:, 1] + 0.114 * row[:, 2]
    print(f"\n--- ESTAÇÃO Y={y} ---")
    # Achar onde a sapata externa esquerda começa (transicao de escuro para metal)
    for x in range(390, 440):
        print(f"Esq X={x}: Lum={lum[x]:.1f}, A={row[x,3]}, RGB=({row[x,0]},{row[x,1]},{row[x,2]})")
    # Achar onde a sapata externa direita termina
    for x in range(830, 875):
        print(f"Dir X={x}: Lum={lum[x]:.1f}, A={row[x,3]}, RGB=({row[x,0]},{row[x,1]},{row[x,2]})")
