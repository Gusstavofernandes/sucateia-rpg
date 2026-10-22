from PIL import Image
import numpy as np
import scipy.signal

img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
arr_est = np.array(img_est)

# Na linha y = 780 da estação:
# Trilhos estão entre 450 e 850
row = arr_est[780, :, :]
lum = np.mean(row[:, :3], axis=1) * (row[:, 3] > 100)

# Procurar picos entre 450 e 850
peaks, _ = scipy.signal.find_peaks(lum[450:850], height=35, distance=50)
peaks = peaks + 450
print(f"Picos de trilho na base da estação (x=450..850): {peaks}")

t_esq = peaks[0]
t_dir = peaks[-1]
bitola_tex = t_dir - t_esq
centro_tex = (t_esq + t_dir) / 2.0

bitola_world = bitola_tex * 0.20
# Nó em -215.9, centro imagem 504
centro_world = -215.9 + (centro_tex - 504.0) * 0.20
print(f"Estação Base Trilho: Esq={t_esq}, Dir={t_dir}")
print(f"Estação Base: Bitola na textura = {bitola_tex:.1f} px | Bitola no mundo = {bitola_world:.2f} px")
print(f"Estação Base: Centro X na textura = {centro_tex:.1f} px | Centro X no mundo = {centro_world:.2f} px")

# E no topo da estação (y = 20):
row_top = arr_est[20, :, :]
lum_top = np.mean(row_top[:, :3], axis=1) * (row_top[:, 3] > 100)
peaks_top, _ = scipy.signal.find_peaks(lum_top[450:850], height=35, distance=50)
peaks_top = peaks_top + 450
t_esq_t = peaks_top[0]
t_dir_t = peaks_top[-1]
bitola_top_tex = t_dir_t - t_esq_t
centro_top_tex = (t_esq_t + t_dir_t) / 2.0
print(f"\nEstação Topo: Bitola no mundo = {bitola_top_tex * 0.20:.2f} px | Centro X no mundo = {-215.9 + (centro_top_tex - 504)*0.20:.2f} px")
