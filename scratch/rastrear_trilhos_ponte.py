from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr = np.array(img)

print("Rastreando os trilhos de metal da PONTE ao longo de Y:")
for y in range(20, 950, 80):
    row = arr[y, :, :]
    lum_esq = np.mean(row[100:350, :3], axis=1) * (row[100:350, 3] > 100)
    lum_dir = np.mean(row[350:650, :3], axis=1) * (row[350:650, 3] > 100)
    
    peak_esq = 100 + np.argmax(lum_esq)
    peak_dir = 350 + np.argmax(lum_dir)
    bitola = peak_dir - peak_esq
    centro = (peak_esq + peak_dir) / 2.0
    
    print(f"y={y:3d}: Trilho Esq={peak_esq:3d}, Trilho Dir={peak_dir:3d} | Bitola tex={bitola:3d} (escala 0.2: {bitola*0.2:5.2f} px) | Centro tex={centro:5.1f}")
