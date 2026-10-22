from PIL import Image

img = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
w, h = img.size

# Recortar o topo dos trilhos da ponte
crop = img.crop((100, 0, 650, 200))
crop.save('scratch/crop_ponte_top.png')
print("Salvo scratch/crop_ponte_top.png")
