from PIL import Image
import numpy as np

# 1. Analisar estacao_trilho_v2.png
img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
arr_est = np.array(img_est)
# No nó EstacaoCarga: scale = 0.20
# Onde estão os dois trilhos de ferro na linha y = 20 (topo da estação)?
row_est = arr_est[20, :, :]
# Vamos achar os dois trilhos de metal (picos)
# Trilhos têm brilho e ferro
print("ESTAÇÃO V2:")
print(f"Dimensões: {img_est.size}")
# Encontrar colunas dos trilhos
# Em y=20:
import scipy.signal
lum_est = np.mean(row_est[:, :3], axis=1) * (row_est[:, 3] > 100)
peaks_est, _ = scipy.signal.find_peaks(lum_est, height=35, distance=50)
print("Picos na linha y=20 da estação:", peaks_est)
if len(peaks_est) >= 2:
    # Dois trilhos principais
    t_esq_est = peaks_est[0]
    t_dir_est = peaks_est[-1]
    bitola_tex_est = t_dir_est - t_esq_est
    centro_tex_est = (t_dir_est + t_esq_est) / 2
    # No mundo com escala 0.20 e posição (-215.9, 325):
    # O pivô do sprite é o centro da imagem (img_est.width/2 = 504, img_est.height/2 = 405)
    bitola_mundo_est = bitola_tex_est * 0.20
    centro_mundo_est = -215.9 + (centro_tex_est - 504) * 0.20
    print(f"Estação: Trilho Esq = {t_esq_est}, Trilho Dir = {t_dir_est}")
    print(f"Estação: Bitola no mundo = {bitola_mundo_est:.2f} px")
    print(f"Estação: Centro no mundo = {centro_mundo_est:.2f} px")

# 2. Analisar boca_tunel_v2.png
print("\nBOCA TUNEL V2:")
img_tun = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
arr_tun = np.array(img_tun)
print(f"Dimensões: {img_tun.size}")
# No nó TunelMinaEntrada: scale = 0.422378, pos = (-188.94, 116.86)
# Na base do túnel: y = 580
row_tun = arr_tun[580, :, :]
lum_tun = np.mean(row_tun[:, :3], axis=1) * (row_tun[:, 3] > 100)
peaks_tun, _ = scipy.signal.find_peaks(lum_tun, height=35, distance=30)
print("Picos na linha y=580 do túnel:", peaks_tun)
# Vamos inspecionar as colunas dos trilhos na base do túnel
# Na base do túnel os trilhos são duas barras verticais
# Vamos achar os picos de gradiente ou intensidade
t_esq_tun = 430 # aproximado, vamos achar exatamente
# Procurar colunas de metal
rails_cols = []
for x in range(380, 630):
    col = arr_tun[550:600, x, :]
    # Média de alfa e intensidade
    if np.mean(col[:, 3]) > 150:
        rails_cols.append(x)
print(f"Colunas opacas na base do túnel: {rails_cols[0]} a {rails_cols[-1]}")

# Encontrar as duas barras de trilho exatas na base do túnel
# Na linha 580:
# Vamos ver os valores ao longo de x entre 400 e 620
for x in range(410, 610, 10):
    val = np.mean(arr_tun[580, x, :3])
    a = arr_tun[580, x, 3]
    print(f"x={x}: lum={val:.1f}, a={a}")
