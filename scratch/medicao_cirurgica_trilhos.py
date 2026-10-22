from PIL import Image
import numpy as np

# 1. Base da estação (y = 800)
img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
arr_est = np.array(img_est)

# Na linha y = 800 (última linha antes do fim, h = 810):
# Vamos plotar o perfil de luminosidade dos trilhos de metal
row_est = arr_est[800, :, :]
# Achar os dois trilhos de metal:
# Trilho esquerdo e trilho direito
# Vamos achar os centros exatos dos trilhos na base
# O trilho esquerdo tem ferro em torno de x=470..530
col_esq_est = np.arange(460, 520)
lum_esq_est = np.mean(row_est[col_esq_est, :3], axis=1) * (row_est[col_esq_est, 3] > 100)
x_esq_est = np.sum(col_esq_est * lum_esq_est) / np.sum(lum_esq_est)

col_dir_est = np.arange(810, 880)
lum_dir_est = np.mean(row_est[col_dir_est, :3], axis=1) * (row_est[col_dir_est, 3] > 100)
x_dir_est = np.sum(col_dir_est * lum_dir_est) / np.sum(lum_dir_est)

bitola_tex_est_base = x_dir_est - x_esq_est
centro_tex_est_base = (x_esq_est + x_dir_est) / 2.0

# No mundo com escala 0.20 e pos_x = -215.9:
# Centro da imagem da estação = 504
bitola_world_est_base = bitola_tex_est_base * 0.20
centro_world_est_base = -215.9 + (centro_tex_est_base - 504.0) * 0.20

print("--- ESTAÇÃO (TRILHO DE LIGAÇÃO) NA BASE (y = 800 da textura) ---")
print(f"Trilho Esq = {x_esq_est:.2f} px, Trilho Dir = {x_dir_est:.2f} px")
print(f"Bitola textura = {bitola_tex_est_base:.2f} px | Bitola no mundo = {bitola_world_est_base:.2f} px")
print(f"Centro X textura = {centro_tex_est_base:.2f} px | Centro X no mundo = {centro_world_est_base:.2f} px")

# 2. Topo da ponte (trilho_reto_vertical_v1.png, y = 20)
img_ponte = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr_ponte = np.array(img_ponte)

row_ponte = arr_ponte[20, :, :]
# Achar os dois trilhos na linha y = 20:
# Trilho esquerdo em torno de x=200..250, trilho direito em torno de x=500..550
col_esq_pt = np.arange(190, 250)
lum_esq_pt = np.mean(row_ponte[col_esq_pt, :3], axis=1) * (row_ponte[col_esq_pt, 3] > 100)
x_esq_pt = np.sum(col_esq_pt * lum_esq_pt) / np.sum(lum_esq_pt)

col_dir_pt = np.arange(500, 560)
lum_dir_pt = np.mean(row_ponte[col_dir_pt, :3], axis=1) * (row_ponte[col_dir_pt, 3] > 100)
x_dir_pt = np.sum(col_dir_pt * lum_dir_pt) / np.sum(lum_dir_pt)

bitola_tex_pt_top = x_dir_pt - x_esq_pt
centro_tex_pt_top = (x_esq_pt + x_dir_pt) / 2.0

print("\n--- PONTE DO TRILHO NO TOPO (y = 20 da textura) ---")
print(f"Trilho Esq = {x_esq_pt:.2f} px, Trilho Dir = {x_dir_pt:.2f} px")
print(f"Bitola textura = {bitola_tex_pt_top:.2f} px")
print(f"Centro X textura = {centro_tex_pt_top:.2f} px")

# 3. CÁLCULO DO FATOR DE ESCALA EXATO
# Fator de escala = bitola do trilho de ligação ÷ bitola da ponte
# No mundo: a bitola do trilho de ligação na base é bitola_world_est_base.
# A bitola da textura da ponte é bitola_tex_pt_top.
# Logo, a escala da ponte no Godot deve ser:
escala_ponte_world = bitola_world_est_base / bitola_tex_pt_top
fator_escala_relativo = escala_ponte_world / 0.20 # comparado à escala original de 0.20
print(f"\n---> ESCALA EXATA DA PONTE NO GODOT: {escala_ponte_world:.6f}")
print(f"---> Fator de escala em relação a 0.20: {fator_escala_relativo:.4f}")
print(f"Está no intervalo [0.87, 1.15]? {'SIM' if 0.87 <= fator_escala_relativo <= 1.15 else 'NÃO'}")

# 4. ALINHAMENTO DO CENTRO X
# Queremos que o centro do trilho da ponte no mundo seja igual a centro_world_est_base!
# centro_world_pt = pos_x_ponte + offset_sprite_x + (centro_tex_pt_top - img_ponte.width / 2.0) * escala_ponte_world
# pos_x_trilho = centro_world_est_base - (centro_tex_pt_top - img_ponte.width / 2.0) * escala_ponte_world
pos_x_trilho = centro_world_est_base - (centro_tex_pt_top - img_ponte.width / 2.0) * escala_ponte_world
print(f"\n---> POSIÇÃO X DO TRILHO DA PONTE NO MUNDO: {pos_x_trilho:.2f} px")
print(f"Centro X resultante da ponte: {pos_x_trilho + (centro_tex_pt_top - img_ponte.width/2.0)*escala_ponte_world:.2f} px (Erro = 0.00 px!)")
