import os
from PIL import Image
import numpy as np

# Texture do Coliseu sul
col_sul_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_coliseu_imponente_sul_v4.png'
im = Image.open(col_sul_path).convert("RGBA")
w, h = im.size
print(f"Coliseu sul image size: {w}x{h}")

# The Colosseum is at position Vector2(4940, 545) with scale Vector2(1.32, 1.32)
# Center of the texture is at (w/2, h/2).
# In world coordinates:
# world_x = 4940 + (img_x - w/2) * 1.32
# world_y = 545 + (img_y - h/2) * 1.32

# Let's find for each world_x column, what is the maximum world_y that has alpha > 20
arr = np.array(im)
alpha = arr[:, :, 3]

# Let's sample world_x every 100 pixels from 3800 to 6000
for wx in range(3800, 6100, 150):
    # calculate corresponding img_x
    img_x = int((wx - 4940) / 1.32 + w / 2)
    if 0 <= img_x < w:
        col_alpha = alpha[:, img_x]
        non_zero = np.where(col_alpha > 20)[0]
        if len(non_zero) > 0:
            max_img_y = non_zero.max()
            max_world_y = 545 + (max_img_y - h / 2.0) * 1.32
            print(f"World X: {wx} -> Coliseu Wall lowest Y: {max_world_y:6.1f} (buffer floor starts at Y > {max_world_y + 80:6.1f})")
        else:
            print(f"World X: {wx} -> No Coliseu wall at this X")
    else:
        print(f"World X: {wx} -> Outside texture")
