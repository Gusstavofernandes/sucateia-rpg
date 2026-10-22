from PIL import Image
import numpy as np

# Carregar imagens
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
arr_tunel = np.array(img_tunel)

img_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr_trilho = np.array(img_trilho)

print("--- MEDIÇÃO 1: TÚNEL DA MINA (tunel_mina_norte_v1.png) ---")
# Na base do túnel:
# Vamos encontrar os pixels da cabeça/haste dos trilhos na linha Y = 950 e Y = 970 (local da imagem)
# No crop tunel_rails_crop (X de 200 a 700, Y de 850 a 1000):
# Vamos analisar a linha Y = 950 da imagem original do túnel:
y_t = 950
row_t = arr_tunel[y_t, :, :]

# Vamos encontrar os trilhos esquerdo e direito analisando a imagem recortada
# No crop de X=200 a X=700:
# Trilho esquerdo está por volta de X ~ 220..320
# Trilho direito está por volta de X ~ 500..650

# Vamos imprimir as colunas onde os trilhos estão:
# Olhando a imagem tunel_rails_crop.png:
# Trilho esquerdo ponta final: Y ~ 970..990
# Trilho direito ponta final: Y ~ 970..990

# Vamos achar o perfil horizontal exato na linha Y=940 da imagem original:
for x in range(200, 700):
    # Se alfa > 100
    if arr_tunel[940, x, 3] > 100:
        pass

# Vamos fazer uma medição visual exata detectando o centro da cabeça do trilho em Y=940 e Y=960:
# Vamos salvar uma imagem ampliada com régua graduada a cada 1 pixel!
crop_t_rule = arr_tunel[920:980, 200:700, :].copy()
# Criar imagem com grid para ver cada pixel exato
Image.fromarray(crop_t_rule).save('scratch/tunel_measure_zoom.png')

# Para o trilho vertical (trilho_reto_vertical_v1.png):
# No topo do trilho (Y = 20 a Y = 80)
crop_r_rule = arr_trilho[10:80, 150:650, :].copy()
Image.fromarray(crop_r_rule).save('scratch/trilho_measure_zoom.png')

print("Fatias com zoom salvas para inspeção pixel a pixel.")
