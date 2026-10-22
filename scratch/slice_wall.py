from PIL import Image

wall = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")
print("Wall size:", wall.size)

# Salvar seções de 400 em 400 px para ver os melhores elementos arquitetônicos
for i, x in enumerate(range(0, wall.size[0] - 300, 350)):
    crop_part = wall.crop((x, 14, min(wall.size[0], x + 400), 500))
    crop_part.save(f'scratch/wall_sec_{i}.png')
print(f"Salvas seções de parede em scratch/wall_sec_*.png")
