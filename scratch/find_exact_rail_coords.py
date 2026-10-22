from PIL import Image
import numpy as np

# Vamos carregar tunel e trilho vertical
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
arr_t = np.array(img_tunel)

# Na ponta de baixo do túnel:
# Onde terminam os trilhos de ferro?
# Vamos encontrar os trilhos na linha Y = 950
# Vamos procurar os picos de gradiente ou intensidade da cabeça do trilho
# Para visualização inequívoca, vamos criar uma imagem com marcadores verticais a cada 10 pixels
# nas fatias relevantes.

slice_t = img_tunel.crop((200, 850, 700, 1000))
slice_t.save('scratch/tunel_rails_crop.png')

# No trilho vertical:
# Topo do trilho vertical (Y de 0 a 150)
img_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
slice_r = img_trilho.crop((150, 0, 600, 150))
slice_r.save('scratch/trilho_rails_crop.png')

print("Crops salvos.")
