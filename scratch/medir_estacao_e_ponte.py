from PIL import Image
import numpy as np
import scipy.signal

print("=== MEDIÇÕES EM PIXELS: TRILHO DE LIGAÇÃO (ESTAÇÃO V2) vs PONTE DO TRILHO ===")

# 1. TRILHO DE LIGAÇÃO (ESTAÇÃO V2)
img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
arr_est = np.array(img_est)
# Estação: nó em (-215.9, 325.0), escala 0.20
# Dimensões da textura: 1008 x 810
# Vamos analisar as últimas linhas da estação (base dos trilhos, y de 750 a 808)
print(f"Estação textura: {img_est.size}")

# Achar última linha opaca com trilhos na estação:
opaque_rows_est = np.where(np.any(arr_est[:, :, 3] > 100, axis=1))[0]
last_row_est = opaque_rows_est[-1]
print(f"Estação: última linha opaca na textura = {last_row_est}")

# Vamos analisar a linha y = 780 na estação (dormente/trilho da base):
row_est_base = arr_est[780, :, :]
lum_est_base = np.mean(row_est_base[:, :3], axis=1) * (row_est_base[:, 3] > 100)
peaks_est, _ = scipy.signal.find_peaks(lum_est_base, height=35, distance=50)
print(f"Picos na linha y=780 da estação: {peaks_est}")

# Trilhos na base da estação:
t_esq_est = peaks_est[0]
t_dir_est = peaks_est[-1]
bitola_tex_est = t_dir_est - t_esq_est
centro_tex_est = (t_esq_est + t_dir_est) / 2.0
bitola_world_est = bitola_tex_est * 0.20

# Centro X no mundo da estação:
# Nó em pos_x = -215.9, pivô do sprite = (504, 405)
centro_world_est = -215.9 + (centro_tex_est - 504.0) * 0.20
y_base_world_est = 325.0 + (last_row_est - 405.0) * 0.20

print(f"Estação Base: Bitola na textura = {bitola_tex_est:.1f} px | Bitola no mundo = {bitola_world_est:.2f} px")
print(f"Estação Base: Centro X na textura = {centro_tex_est:.1f} px | Centro X no mundo = {centro_world_est:.2f} px")
print(f"Estação Base: Y no mundo = {y_base_world_est:.2f} px")

# Passo de dormentes na estação:
# Achar linhas dos dormentes ao longo de y
dormentes_est_y = []
for y in range(50, 800, 5):
    # Fatia no meio dos trilhos
    slice_m = arr_est[y, int(centro_tex_est)-20 : int(centro_tex_est)+20, :3]
    if np.mean(slice_m) > 40: # madeira clara
        pass
# Vamos calcular passo médio pela autocorrelação ou picos verticais ao longo do trilho
lum_vert_est = np.mean(arr_est[:, int(t_esq_est)-10:int(t_esq_est)+10, :3], axis=(1,2))
peaks_dor_est, _ = scipy.signal.find_peaks(lum_vert_est, height=30, distance=60)
print(f"Picos de dormentes na estação (y textura): {peaks_dor_est}")
if len(peaks_dor_est) > 1:
    passo_tex_est = np.mean(np.diff(peaks_dor_est))
    passo_world_est = passo_tex_est * 0.20
    print(f"Passo médio dos dormentes na estação: {passo_tex_est:.1f} px na textura = {passo_world_est:.2f} px no mundo")


# 2. PONTE DO TRILHO (trilho_reto_vertical_v1.png)
img_ponte_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr_pt = np.array(img_ponte_trilho)
print(f"\nPonte Trilho textura: {img_ponte_trilho.size}")

# Topo da textura da ponte (onde ela encosta na estação):
opaque_rows_pt = np.where(np.any(arr_pt[:, :, 3] > 100, axis=1))[0]
first_row_pt = opaque_rows_pt[0]
print(f"Ponte Trilho: primeira linha opaca na textura = {first_row_pt}")

# Linha y = 50 (topo dos trilhos da ponte):
row_pt_top = arr_pt[50, :, :]
lum_pt_top = np.mean(row_pt_top[:, :3], axis=1) * (row_pt_top[:, 3] > 100)
peaks_pt, _ = scipy.signal.find_peaks(lum_pt_top, height=35, distance=50)
print(f"Picos na linha y=50 da ponte: {peaks_pt}")
t_esq_pt = peaks_pt[0]
t_dir_pt = peaks_pt[-1]
bitola_tex_pt = t_dir_pt - t_esq_pt
centro_tex_pt = (t_esq_pt + t_dir_pt) / 2.0

print(f"Ponte Trilho Topo: Bitola na textura = {bitola_tex_pt:.1f} px, Centro X na textura = {centro_tex_pt:.1f} px")

# Na configuração atual da cena:
# [node name="CavaleteElevadoCanal" type="StaticBody2D" parent="RedeFerroviariaMina"]
# position = Vector2(-190, 560)
# [node name="TrilhosSobreCavalete" type="Sprite2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
# position = Vector2(0, -75), scale = Vector2(0.20, 0.20)
# Com essa escala 0.20:
bitola_world_pt_atual = bitola_tex_pt * 0.20
# Centro do trilho da ponte no mundo:
# Nó em -190, offset do sprite 0, centro do trilho relativo ao centro da textura: (centro_tex_pt - 745/2) * 0.20
rel_centro_pt = (centro_tex_pt - img_ponte_trilho.width / 2.0) * 0.20
centro_world_pt_atual = -190.0 + 0.0 + rel_centro_pt
y_top_world_pt_atual = 560.0 - 75.0 + (first_row_pt - img_ponte_trilho.height / 2.0) * 0.20

print(f"Ponte Atual: Bitola no mundo = {bitola_world_pt_atual:.2f} px")
print(f"Ponte Atual: Centro X no mundo = {centro_world_pt_atual:.2f} px")
print(f"Ponte Atual: Topo Y no mundo = {y_top_world_pt_atual:.2f} px")

# Passo dos dormentes na ponte:
lum_vert_pt = np.mean(arr_pt[:, int(t_esq_pt)-10:int(t_esq_pt)+10, :3], axis=(1,2))
peaks_dor_pt, _ = scipy.signal.find_peaks(lum_vert_pt, height=30, distance=60)
print(f"Picos de dormentes na ponte (y textura): {peaks_dor_pt}")
if len(peaks_dor_pt) > 1:
    passo_tex_pt = np.mean(np.diff(peaks_dor_pt))
    passo_world_pt = passo_tex_pt * 0.20
    print(f"Passo médio dos dormentes na ponte: {passo_tex_pt:.1f} px na textura = {passo_world_pt:.2f} px no mundo")
