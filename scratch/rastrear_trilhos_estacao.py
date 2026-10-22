from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
arr = np.array(img)

print("Rastreando os trilhos de metal da estação ao longo de Y:")
for y in range(20, 800, 60):
    row = arr[y, :, :]
    # Achar colunas com maior luminosidade na metade esquerda (350 a 600) e na metade direita (600 a 950)
    lum_esq = np.mean(row[350:600, :3], axis=1) * (row[350:600, 3] > 100)
    lum_dir = np.mean(row[600:950, :3], axis=1) * (row[600:950, 3] > 100)
    
    peak_esq = 350 + np.argmax(lum_esq)
    peak_dir = 600 + np.argmax(lum_dir)
    bitola = peak_dir - peak_esq
    centro = (peak_esq + peak_dir) / 2.0
    
    print(f"y={y:3d}: Trilho Esq={peak_esq:3d}, Trilho Dir={peak_dir:3d} | Bitola tex={bitola:3d} (mundo {bitola*0.2:5.2f} px) | Centro tex={centro:5.1f} (mundo {-215.9 + (centro-504)*0.2:6.2f} px)")
