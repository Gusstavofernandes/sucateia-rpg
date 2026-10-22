with open(r'c:\Users\Usuario\Documents\jogo\scripts\world\alto_lixo_builder.gd', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see how floor was created in alto_lixo_builder.gd
for line in text.splitlines()[:60]:
    if any(k in line for k in ['floor', 'TileMap', 'Ground', 'outline', 'Polygon2D', 'salvage_ground']):
        print(line)
