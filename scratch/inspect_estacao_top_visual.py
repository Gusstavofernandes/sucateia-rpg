from PIL import Image

img = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png')
w, h = img.size

# Recortar o topo dos trilhos (x de 350 a 850, y de 0 a 150)
crop = img.crop((350, 0, 850, 150))
crop.save('scratch/crop_estacao_top_raw.png')
print("Salvo scratch/crop_estacao_top_raw.png")
