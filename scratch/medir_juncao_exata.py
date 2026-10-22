from PIL import Image
import numpy as np

img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
img_pt = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')

arr_est = np.array(img_est)
arr_pt = np.array(img_pt)

# 1. Ponta de baixo da Estação (trilho de ligação)
# Último dormente da estação: onde ele termina?
# Vamos achar a linha exata dos trilhos na base
opaque_rows_est = np.where(np.any(arr_est[:, :, 3] > 100, axis=1))[0]
last_row_est = opaque_rows_est[-1]

# Linha do último dormente/trilho na base da estação:
row_est = arr_est[last_row_est - 5, :, :]
# Achar os dois trilhos de metal
# Coluna esquerda entre 380 e 460
lum_esq = np.mean(row_est[380:460, :3], axis=1) * (row_est[380:460, 3] > 100)
x_esq_est = 380 + np.argmax(lum_esq)

# Coluna direita entre 800 e 900
lum_dir = np.mean(row_est[800:900, :3], axis=1) * (row_est[800:900, 3] > 100)
x_dir_est = 800 + np.argmax(lum_dir)

bitola_est_base_tex = x_dir_est - x_esq_est
centro_est_base_tex = (x_esq_est + x_dir_est) / 2.0

# Na escala da estação (0.20):
bitola_est_base_world = bitola_est_base_tex * 0.20
centro_est_base_world = -215.9 + (centro_est_base_tex - 504.0) * 0.20

print("=== TRILHO DE LIGAÇÃO (BASE DA ESTAÇÃO V2) ===")
print(f"Última linha: y = {last_row_est}")
print(f"Trilho Esq = {x_esq_est} px, Trilho Dir = {x_dir_est} px")
print(f"Bitola na textura = {bitola_est_base_tex} px | Bitola no mundo = {bitola_est_base_world:.2f} px")
print(f"Centro X na textura = {centro_est_base_tex:.1f} px | Centro X no mundo = {centro_est_base_world:.2f} px")


# 2. Ponta de cima da Ponte (trilho_reto_vertical_v1.png)
opaque_rows_pt = np.where(np.any(arr_pt[:, :, 3] > 100, axis=1))[0]
first_row_pt = opaque_rows_pt[0]

# Linha do primeiro dormente/trilho no topo da ponte:
row_pt = arr_pt[first_row_pt + 15, :, :]
lum_esq_pt = np.mean(row_pt[180:260, :3], axis=1) * (row_pt[180:260, 3] > 100)
x_esq_pt = 180 + np.argmax(lum_esq_pt)

lum_dir_pt = np.mean(row_pt[480:560, :3], axis=1) * (row_pt[480:560, 3] > 100)
x_dir_pt = 480 + np.argmax(lum_dir_pt)

bitola_pt_top_tex = x_dir_pt - x_esq_pt
centro_pt_top_tex = (x_esq_pt + x_dir_pt) / 2.0

# Na escala atual da ponte (0.20):
bitola_pt_top_world_atual = bitola_pt_top_tex * 0.20
centro_pt_top_world_atual = -190.0 + (centro_pt_top_tex - arr_pt.shape[1] / 2.0) * 0.20

print("\n=== PONTE DO TRILHO (TOPO DO TRILHO DA PONTE) ===")
print(f"Primeira linha: y = {first_row_pt}")
print(f"Trilho Esq = {x_esq_pt} px, Trilho Dir = {x_dir_pt} px")
print(f"Bitola na textura = {bitola_pt_top_tex} px | Bitola no mundo (escala 0.20) = {bitola_pt_top_world_atual:.2f} px")
print(f"Centro X na textura = {centro_pt_top_tex:.1f} px | Centro X no mundo = {centro_pt_top_world_atual:.2f} px")

# 3. FATOR DE ESCALA
fator_escala = bitola_est_base_world / bitola_pt_top_world_atual
print(f"\n=== FATOR DE ESCALA CALCULADO ===")
print(f"Fator de escala = bitola_ligacao ({bitola_est_base_world:.2f}) / bitola_ponte ({bitola_pt_top_world_atual:.2f}) = {fator_escala:.4f}")
