from PIL import Image
import os

img_path = 'assets/terrain/floor_atlas.png'
if os.path.exists(img_path):
    img = Image.open(img_path)
    print("floor_atlas size:", img.size, img.mode)
    # Amostra de cor média
    colors = img.resize((1, 1)).getpixel((0, 0))
    print("floor_atlas average color:", colors)
