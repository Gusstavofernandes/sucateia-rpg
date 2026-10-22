from PIL import Image

wall = Image.open('fundo_ferro_standalone/assets/fundo_wall.png')
print("Wall size:", wall.size)

# Cortar os primeiros 400 pixels da esquerda de fundo_wall
crop_left = wall.crop((0, 0, 400, wall.size[1]))
crop_left.save('scratch/wall_left_400.png')
print("Salvo scratch/wall_left_400.png!")
