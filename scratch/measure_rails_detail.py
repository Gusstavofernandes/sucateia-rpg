from PIL import Image
import numpy as np

# 1. TÚNEL
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
arr_t = np.array(img_tunel)
# Na base do túnel, vamos olhar a linha Y = 950 (perto da ponta inferior onde os dois trilhos saem da moldura)
# e Y = 980 (bem na ponta)
for y_test in [920, 940, 960, 980]:
    row = arr_t[y_test, :, :]
    # Achar colunas onde há ferro do trilho
    # O ferro do trilho tem perfil metálico cinza escuro / marrom escuro enferrujado com destaque
    # Vamos salvar os valores ou plotar um perfil
    print(f"Tunel linha Y={y_test}: largura total da imagem={arr_t.shape[1]}")

# 2. TRILHO VERTICAL
img_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr_r = np.array(img_trilho)
for y_test in [10, 30, 50, 70]:
    row = arr_r[y_test, :, :]
    print(f"Trilho linha Y={y_test}: largura total da imagem={arr_r.shape[1]}")
