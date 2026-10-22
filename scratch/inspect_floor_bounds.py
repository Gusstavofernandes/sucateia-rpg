import os

with open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for TileMapLayer or Floor elements
for line in text.splitlines():
    if any(k in line.lower() for k in ['tilemap', 'piso', 'floor', 'camera', 'limite', 'salvage_ground']):
        if len(line.strip()) < 120:
            print(line.strip())
