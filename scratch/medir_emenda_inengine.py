from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/captura_boca_tunel_v2_closeup_emenda.png')
w, h = img.size
arr = np.array(img)

# A câmera está em zoom 2.5x, centrada em (-190, 244).
# Vamos procurar a ponta de baixo dos trilhos do túnel (y antes da emenda)
# e a ponta de cima dos trilhos da estação (y logo após a emenda).
# No centro da imagem (x em torno de w/2):
center_x = w // 2
center_y = h // 2

print(f"Dimensões da imagem: {w} x {h}, centro = ({center_x}, {center_y})")

# Vamos inspecionar as linhas verticais em torno de center_y (por exemplo, y de 200 a 450)
# Para cada linha, vamos achar onde estão os trilhos de ferro
for y in range(260, 420, 5):
    # Recorte horizontal de center_x - 120 a center_x + 120
    row_slice = arr[y, center_x - 120 : center_x + 120, :3]
    # Lum
    lum = np.mean(row_slice, axis=1)
    # Detectar trilhos (ferro enferrujado/brilhante ou dormentes)
    print(f"y={y}: min lum={np.min(lum):.1f}, max lum={np.max(lum):.1f}, mean lum={np.mean(lum):.1f}")
