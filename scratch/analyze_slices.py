from PIL import Image
import numpy as np

# 1. TUNEL
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
arr_tunel = np.array(img_tunel)
h_t, w_t, _ = arr_tunel.shape

# Achar a última linha com pixels visíveis (alfa > 50)
alpha_t = arr_tunel[:, :, 3]
y_indices_t, x_indices_t = np.where(alpha_t > 50)
bottom_y_t = np.max(y_indices_t)
print(f"Tunel: Y max com alfa > 50 = {bottom_y_t} (altura total: {h_t})")

# Vamos inspecionar as últimas linhas do túnel (por exemplo, y de bottom_y_t - 50 até bottom_y_t)
# Onde estão os dois trilhos de ferro na base do túnel?
# Em cada linha y, podemos olhar os pixels de cor de ferro/trilho ou salvar um recorte para inspecionar.
slice_tunel = arr_tunel[bottom_y_t-100:bottom_y_t, :, :]
# Salvar recorte da base do túnel para visualização precisa
Image.fromarray(slice_tunel).save('scratch/slice_base_tunel.png')
print("Salvo scratch/slice_base_tunel.png")

# 2. PONTE DO TRILHO (TRILHO VERTICAL QUE FICA NA PONTE)
img_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
arr_trilho = np.array(img_trilho)
h_r, w_r, _ = arr_trilho.shape

alpha_r = arr_trilho[:, :, 3]
y_indices_r, x_indices_r = np.where(alpha_r > 50)
top_y_r = np.min(y_indices_r)
bottom_y_r = np.max(y_indices_r)
print(f"Trilho Vertical: Y min com alfa > 50 = {top_y_r}, Y max = {bottom_y_r} (altura total: {h_r})")

slice_trilho_top = arr_trilho[top_y_r:top_y_r+100, :, :]
Image.fromarray(slice_trilho_top).save('scratch/slice_topo_trilho.png')
print("Salvo scratch/slice_topo_trilho.png")
