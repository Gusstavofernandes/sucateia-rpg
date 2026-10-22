from PIL import Image
import numpy as np

def analyze_rail_profile(img_path, y, x_range):
    im = Image.open(img_path).convert("RGBA")
    arr = np.array(im)
    row_rgb = arr[y, :, :3]
    row_a = arr[y, :, 3]
    
    lum = 0.299 * row_rgb[:, 0] + 0.587 * row_rgb[:, 1] + 0.114 * row_rgb[:, 2]
    
    print(f"\n[{img_path}] Y={y}")
    for x in range(x_range[0], x_range[1]):
        if row_a[x] > 50:
            print(f"X={x:3d} | A={row_a[x]:3d} | RGB=({row_rgb[x,0]:3d},{row_rgb[x,1]:3d},{row_rgb[x,2]:3d}) | Lum={lum[x]:5.1f}")

# No sprite da estacao em Y=800 (perto da emenda inferior):
# O trilho esquerdo e direito estao entre X=400 e X=900
print("--- ESCANEANDO TRILHOS NA EMENDA INFERIOR DA ESTAÇÃO ---")
im_est = Image.open("assets/rails/estacao_trilho_v2.png").convert("RGBA")
arr_est = np.array(im_est)
lum_est = 0.299 * arr_est[800, :, 0] + 0.587 * arr_est[800, :, 1] + 0.114 * arr_est[800, :, 2]
# Achar derivadas/gradientes de luminancia
grad = np.diff(lum_est)
for x in range(350, 900):
    if abs(grad[x]) > 25 and arr_est[800, x, 3] > 100:
        print(f"X={x}: Lum={lum_est[x]:.1f}, Grad={grad[x]:.1f}, RGB={arr_est[800, x, :3]}")
