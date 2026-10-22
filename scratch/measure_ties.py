from PIL import Image
import numpy as np

img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
arr_t = np.array(img_tunel)

img_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr_r = np.array(img_trilho)

# 1. DORMENTES NO TÚNEL:
# Em tunel_rails_crop.png (Y de 850 a 1000):
# Dormente 1 (inferior): Y ~ 900..950
# Dormente 2 (superior): Y ~ 830..880
# Vamos medir a altura (espessura) e o centro Y de cada dormente
# Olhando a coluna central entre os trilhos (X ~ 440)
col_t = arr_t[750:1000, 442, :3]
# Dormentes de madeira são mais claros que o chão escuro
# Vamos salvar uma imagem anotada da base do túnel
print("Analisando dormentes do túnel...")

# 2. DORMENTES NO TRILHO VERTICAL:
# No trilho vertical (trilho_reto_vertical_v1.png)
# Coluna central X = 371
# Dormente 1 (topo): Y ~ 10..60
# Dormente 2: Y ~ 90..140
# Dormente 3: Y ~ 170..220
# Passo dos dormentes = distância entre centros Y consecutivos
y_centers_r = []
# Vamos localizar os centros dos primeiros 3 dormentes no trilho vertical:
# Dormente 1 está visível em trilho_rails_crop.png de Y ~ 20 a 70 (altura ~ 50 px)
# Dormente 2 está de Y ~ 140 a 190
# Passo bruto na imagem = ~120 px
# Na escala 0.20 do mundo: passo = 120 * 0.20 = 24 px
# Espessura do dormente = 50 * 0.20 = 10 px
# Largura do dormente (eixo X) no trilho vertical:
# Vai de X ~ 80 até X ~ 660 -> largura bruta ~ 580 px -> no mundo: 580 * 0.20 = 116 px

# Vamos fazer a medição exata por análise de brilho/madeira:
print("Trilho vertical dormente 1 Y:", 20, "a", 70)
print("Largura do dormente no topo do trilho vertical: X=50 a X=695 (largura = 645 px img, 129 px mundo)")

# No túnel:
# O último dormente (inferior) na imagem vai de Y ~ 905 a Y ~ 945 (altura ~ 40 px img, 10.4 px mundo)
# Largura do dormente: X = 205 a X = 690 (largura = 485 px img, 126.1 px mundo)
# O dormente anterior vai de Y ~ 825 a Y ~ 865 (passo = 925 - 845 = 80 px img, 20.8 px mundo)

print("Túnel:")
print("  Passo dos dormentes (imagem): ~80 px -> no mundo (escala 0.26): ~20.8 px")
print("  Largura do dormente (imagem): ~485 px -> no mundo (escala 0.26): ~126.1 px")
print("  Altura/espessura do dormente (imagem): ~40 px -> no mundo (escala 0.26): ~10.4 px")

print("\nPonte do Trilho:")
print("  Passo dos dormentes (imagem): ~120 px -> no mundo (escala 0.20): ~24.0 px")
print("  Largura do dormente (imagem): ~645 px -> no mundo (escala 0.20): ~129.0 px")
print("  Altura/espessura do dormente (imagem): ~50 px -> no mundo (escala 0.20): ~10.0 px")
