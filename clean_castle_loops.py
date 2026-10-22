from PIL import Image
import numpy as np

src_path = r"assets\generated\structures\monumental_clock_castle.png"
im = Image.open(src_path).convert("RGBA")
arr = np.array(im)

# Verificar pixels brancos restantes
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
white_pixels = (r > 230) & (g > 230) & (b > 230) & (a > 100)
print("Pixels brancos opacos restantes:", np.sum(white_pixels))

# Remover qualquer pixel que seja branco puro/fundo nos laços das correntes
# Como o castelo é de pedra escura e metal enferrujado, não há pedra branca pura no topo
arr[white_pixels, 3] = 0

cleaned_im = Image.fromarray(arr, mode='RGBA')
cleaned_im.save(src_path, format="PNG")
print("Limpeza de brancos entre as correntes concluída!")
