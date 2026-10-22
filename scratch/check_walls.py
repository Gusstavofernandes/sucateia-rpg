import os
from PIL import Image

for f in ['scratch/wall_left_400.png', 'fundo_ferro_standalone/assets/fundo_wall.png', 'fundo_ferro_standalone/assets/parede_norte_ferro.png']:
    if os.path.exists(f):
        img = Image.open(f)
        print(f"{f}: {img.size}, mode={img.mode}")
