from PIL import Image
import numpy as np

arch = Image.open('fundo_ferro_standalone/assets/service_arch.png').convert("RGBA")
print("service_arch size:", arch.size)

# Vamos inspecionar a imagem service_arch original
# Ela tem 200x190 px.
# Onde fica o arco de pedra?
# Onde ficam as grades?
# As grades de ferro estão na parte inferior interna do arco:
# y de ~80 a 170, x de ~50 a 150.
# Se aumentarmos service_arch com super-resolução para o tamanho do portal:
# Digamos 700x665 px.
# Vamos ver onde está a curvatura do arco!
