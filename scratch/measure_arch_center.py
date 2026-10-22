from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
arr = np.array(img)
alpha = arr[:, :, 3]

# Na metade superior (onde fica o portal de pedra e madeira, por exemplo Y = 300 a 600)
# Qual é o centro horizontal da alvenaria e das vigas de madeira?
y_test = 400
row = alpha[y_test, :]
visible_x = np.where(row > 50)[0]
x_min, x_max = np.min(visible_x), np.max(visible_x)
center_arch = (x_min + x_max) / 2.0

print(f"Portal de pedra em Y={y_test}: X_min={x_min}, X_max={x_max}, Centro={center_arch:.2f}")

# Na viga superior (Y=250):
row_top = alpha[250, :]
vis_top = np.where(row_top > 50)[0]
print(f"Portal de pedra em Y=250: X_min={np.min(vis_top)}, X_max={np.max(vis_top)}, Centro={(np.min(vis_top) + np.max(vis_top))/2.0:.2f}")

# No vão interno do túnel (a escuridão entre as vigas em Y=500):
# Vamos achar os limites das duas colunas de madeira em Y=500:
# Coluna esquerda vai até X ~ 300, coluna direita começa em X ~ 700
# Escuridão no meio:
print(f"Largura total da alvenaria do portal: {x_max - x_min + 1} px")
