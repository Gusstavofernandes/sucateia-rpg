from PIL import Image
import numpy as np

img_est = Image.open("assets/rails/estacao_trilho_v2.png").convert("RGBA")
img_ponte = Image.open("assets/rails/trilho_reto_vertical_v1.png").convert("RGBA")

arr_est = np.array(img_est)
arr_ponte = np.array(img_ponte)

# Vamos inspecionar as fatias Y=805 da estacao e Y=116 da ponte
row_est = arr_est[805, :, :]
row_ponte = arr_ponte[116, :, :]

lum_est = 0.299 * row_est[:, 0] + 0.587 * row_est[:, 1] + 0.114 * row_est[:, 2]
lum_ponte = 0.299 * row_ponte[:, 0] + 0.587 * row_ponte[:, 1] + 0.114 * row_ponte[:, 2]

print("--- ESTAÇÃO EM Y=805 ---")
# Trilho esquerdo e direito
for x in range(380, 480):
    if row_est[x, 3] > 100:
        print(f"Esq X={x}: Lum={lum_est[x]:.1f}, RGB=({row_est[x,0]},{row_est[x,1]},{row_est[x,2]})")

for x in range(800, 880):
    if row_est[x, 3] > 100:
        print(f"Dir X={x}: Lum={lum_est[x]:.1f}, RGB=({row_est[x,0]},{row_est[x,1]},{row_est[x,2]})")

print("\n--- PONTE EM Y=116 ---")
for x in range(160, 260):
    if row_ponte[x, 3] > 100:
        print(f"Esq X={x}: Lum={lum_ponte[x]:.1f}, RGB=({row_ponte[x,0]},{row_ponte[x,1]},{row_ponte[x,2]})")

for x in range(480, 580):
    if row_ponte[x, 3] > 100:
        print(f"Dir X={x}: Lum={lum_ponte[x]:.1f}, RGB=({row_ponte[x,0]},{row_ponte[x,1]},{row_ponte[x,2]})")
