from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
print("Tamanho estacao_trilho_v2:", img.size)

# Escala no nó EstacaoCarga é 0.20
scale = 0.20
world_w = img.width * scale
world_h = img.height * scale
print(f"Dimensões no mundo com escala {scale}: {world_w:.2f} x {world_h:.2f} px")

# Posição do nó EstacaoCarga: Vector2(-215.9, 325)
pos_x = -215.9
pos_y = 325.0
top_y = pos_y - world_h / 2
bottom_y = pos_y + world_h / 2
print(f"Y topo no mundo: {top_y:.2f} px, Y base no mundo: {bottom_y:.2f} px")

# Analisar a linha do topo (y = 0 até 20 na textura) e a linha da base (y = h-20 até h na textura)
arr = np.array(img)
# Encontrar colunas dos trilhos no topo
row_top = arr[10, :, 3] > 100
opaque_x_top = np.where(row_top)[0]
print("Top opaque x range:", opaque_x_top[0], "a", opaque_x_top[-1] if len(opaque_x_top) else "nenhum")

# Vamos encontrar os dois trilhos de metal (picos) no topo
# Olhar a linha y=10
lum_top = np.mean(arr[10, :, :3], axis=1) * (arr[10, :, 3] > 100)
# Vamos plotar ou encontrar picos
import scipy.signal
peaks_top, _ = scipy.signal.find_peaks(lum_top, height=40, distance=30)
print("Picos de trilho no topo (px textura):", peaks_top)
if len(peaks_top) >= 2:
    gauge_tex = peaks_top[-1] - peaks_top[0]
    center_tex = (peaks_top[-1] + peaks_top[0]) / 2
    gauge_world = gauge_tex * scale
    # Centro relativo ao nó: (center_tex - img.width/2) * scale
    rel_center_world = (center_tex - img.width / 2) * scale
    world_center_x = pos_x + rel_center_world
    print(f"Topo Estação: Bitola na textura = {gauge_tex:.1f} px, Bitola no mundo = {gauge_world:.2f} px")
    print(f"Centro do trilho no topo: textura = {center_tex:.1f} px, no mundo = {world_center_x:.2f} px")
