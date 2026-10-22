from PIL import Image

wall = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")

# Em fundo_wall:
# Colunas 800 a 1600: como é essa parede?
crop_mid = wall.crop((800, 14, 1500, 600))
crop_mid.save('scratch/wall_mid_pure.png')
print("Salvo scratch/wall_mid_pure.png")
