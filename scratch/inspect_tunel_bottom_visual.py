from PIL import Image

img = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png')
w, h = img.size

# Recortar a base dos trilhos (x de 350 a 650, y de 450 a 602)
crop = img.crop((350, 450, 650, h))
crop.save('scratch/crop_tunel_bottom_raw.png')
print("Salvo scratch/crop_tunel_bottom_raw.png")
