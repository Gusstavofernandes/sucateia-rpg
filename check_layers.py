with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find TileMapLayer or TileMap or Bridge nodes
for line in text.split('\n'):
    if '[node name=' in line and any(k in line for k in ['TileMap', 'Bridge', 'Ponte', 'Passarela', 'Ground', 'Floor']):
        print(line)
