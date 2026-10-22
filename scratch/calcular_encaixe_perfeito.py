from PIL import Image
import numpy as np

# 1. Carregar texturas
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
img_estacao = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')

# Medições exatas na textura da estação:
# Escala fixa da estação: 0.20
# Posição fixa da estação: Y = 325.0, topo da estação no mundo = 325.0 - (810 * 0.20 / 2) = 244.00 px
# Na linha y = 10 da estação (pontas dos trilhos que sobem):
arr_est = np.array(img_estacao)
# Encontrar o topo exato dos trilhos na estação:
opaque_rows_est = np.where(np.any(arr_est[:, :, 3] > 100, axis=1))[0]
first_row_est = opaque_rows_est[0]
print(f"Estação: primeira linha opaca na textura = {first_row_est}")

# Coordenada Y no mundo do topo dos trilhos da estação:
est_pos_y = 325.0
est_top_world_y = est_pos_y + (first_row_est - 810 / 2.0) * 0.20
print(f"Estação: Y topo no mundo = {est_top_world_y:.2f} px")

# Colunas dos trilhos na primeira linha com trilhos completos (y = 20):
lum_est = np.mean(arr_est[20, :, :3], axis=1) * (arr_est[20, :, 3] > 100)
# Picos exatos:
import scipy.signal
peaks_est, _ = scipy.signal.find_peaks(lum_est, height=35, distance=50)
t_esq_est = peaks_est[0]
t_dir_est = peaks_est[-1]
bitola_tex_est = t_dir_est - t_esq_est
centro_tex_est = (t_esq_est + t_dir_est) / 2.0

bitola_world_est = bitola_tex_est * 0.20
# Centro no mundo da estação com nó em pos_x = -215.9:
rel_center_est = (centro_tex_est - 1008 / 2.0) * 0.20
est_center_world_x = -215.9 + rel_center_est
print(f"Estação: Bitola no mundo = {bitola_world_est:.2f} px, Centro X no mundo = {est_center_world_x:.2f} px")

# Agora para o TÚNEL V2:
arr_tun = np.array(img_tunel)
opaque_rows_tun = np.where(np.any(arr_tun[:, :, 3] > 100, axis=1))[0]
last_row_tun = opaque_rows_tun[-1]
print(f"\nTúnel: última linha opaca na textura = {last_row_tun} (de {img_tunel.height})")

# Na linha de baixo do túnel (y = 580):
lum_tun = np.mean(arr_tun[580, :, :3], axis=1) * (arr_tun[580, :, 3] > 100)
# Achar os dois trilhos de metal (picos em torno de 430 e 580):
peaks_tun, _ = scipy.signal.find_peaks(lum_tun, height=35, distance=30)
print(f"Túnel: picos em y=580: {peaks_tun}")
# Os dois trilhos são peaks_tun[1]=430 e peaks_tun[2]=574 ou 580:
# Vamos achar o centro de massa de cada trilho:
col_esq = np.arange(410, 445)
w_esq = lum_tun[col_esq]
t_esq_tun = np.sum(col_esq * w_esq) / np.sum(w_esq)

col_dir = np.arange(565, 595)
w_dir = lum_tun[col_dir]
t_dir_tun = np.sum(col_dir * w_dir) / np.sum(w_dir)

bitola_tex_tun = t_dir_tun - t_esq_tun
centro_tex_tun = (t_esq_tun + t_dir_tun) / 2.0
print(f"Túnel textura: Trilho Esq = {t_esq_tun:.2f}, Trilho Dir = {t_dir_tun:.2f}")
print(f"Túnel textura: Bitola = {bitola_tex_tun:.2f} px, Centro = {centro_tex_tun:.2f} px")

# 1. CÁLCULO DA ESCALA EXATA DO TÚNEL:
# Queremos bitola_world_tun == bitola_world_est!
escala_tun = bitola_world_est / bitola_tex_tun
print(f"\n---> ESCALA EXATA DO TÚNEL: {escala_tun:.6f}")
print(f"Bitola resultante no mundo: {bitola_tex_tun * escala_tun:.2f} px (Erro = 0.00 px!)")

# 2. CÁLCULO DA POSIÇÃO X DO TÚNEL:
# Queremos tun_center_world_x == est_center_world_x!
# tun_center_world_x = tun_pos_x + (centro_tex_tun - 1008 / 2.0) * escala_tun
# tun_pos_x = est_center_world_x - (centro_tex_tun - 504.0) * escala_tun
tun_pos_x = est_center_world_x - (centro_tex_tun - 504.0) * escala_tun
print(f"---> POSIÇÃO X DO TÚNEL: {tun_pos_x:.4f} px (Centro do trilho cai exatamente em {est_center_world_x:.2f} px)")

# 3. CÁLCULO DA POSIÇÃO Y DO TÚNEL:
# Queremos que a base opaca do túnel (last_row_tun) termine exatamente onde o topo opaco da estação começa (est_top_world_y)!
# tun_bottom_world_y = tun_pos_y + (last_row_tun - 602 / 2.0) * escala_tun
# tun_pos_y = est_top_world_y - (last_row_tun - 301.0) * escala_tun
# Podemos deixar 1 pixel de sobreposição para não ter qualquer fresta sub-pixel:
tun_pos_y = (est_top_world_y + 1.0) - (last_row_tun - 301.0) * escala_tun
print(f"---> POSIÇÃO Y DO TÚNEL: {tun_pos_y:.4f} px")

tun_bottom_final = tun_pos_y + (last_row_tun - 301.0) * escala_tun
print(f"Base do túnel no mundo: {tun_bottom_final:.2f} px vs Topo estação no mundo: {est_top_world_y:.2f} px (Sobreposição: {tun_bottom_final - est_top_world_y:.2f} px)")
