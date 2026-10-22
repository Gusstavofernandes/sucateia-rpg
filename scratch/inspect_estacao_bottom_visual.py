from PIL import Image

img = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
w, h = img.size

# Recortar a base da estação
crop = img.crop((350, 600, 900, h))
crop.save('scratch/crop_estacao_bottom.png')
print("Salvo scratch/crop_estacao_bottom.png")
