import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Procura nós que contêm 'ground', 'floor', 'terrain', 'terrace', 'land', 'soil', 'earth'
lines = text.split('\n')
for i, line in enumerate(lines):
    if line.startswith('[node name='):
        if any(k in line.lower() for k in ['ground', 'floor', 'terrain', 'terrace', 'land', 'soil', 'earth', 'sea', 'water']):
            print(f"Line {i+1}: {line}")
