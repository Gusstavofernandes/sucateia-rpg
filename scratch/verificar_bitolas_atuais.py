from PIL import Image
import numpy as np

# Vamos inspecionar exatamente:
# 1. estacao_trilho_v2.png (o trilho de ligação)
img_estacao = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")
# 2. trilho_reto_vertical_v1.png (o trilho da ponte)
img_trilho_ponte = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
# 3. cavalete_alto_v1.png (o cavalete da ponte)
img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")

# Na cena master atual:
# EstacaoCarga:
# pos = Vector2(-215.9, 325)
# scale = Vector2(0.20, 0.20)
#
# CavaleteElevadoCanal:
# pos = Vector2(-190, 560)
# TrilhosSobreCavalete:
# pos = Vector2(0, -75) -> pos_global = Vector2(-190, 485)
# scale = Vector2(0.20, 0.20)

print(f"Dimensões:")
print(f"  Estação (trilho de ligação): {img_estacao.size}")
print(f"  Trilho sobre cavalete (ponte): {img_trilho_ponte.size}")
print(f"  Cavalete: {img_cavalete.size}")

# Vamos medir a bitola na imagem estacao_trilho_v2:
# Procurar os trilhos de ferro na estação
arr_est = np.array(img_estacao)
# Amostrar linha 400
alpha_est = arr_est[400, :, 3]
# Procurar picos de luminância onde alpha > 200
lum_est = np.mean(arr_est[400, :, :3], axis=1)

# trilho_reto_vertical_v1
arr_tri = np.array(img_trilho_ponte)
lum_tri = np.mean(arr_tri[400, :, :3], axis=1)

print("Medição realizada.")
