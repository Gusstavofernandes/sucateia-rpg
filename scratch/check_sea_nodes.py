import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for line in lines:
    if any(k in line.lower() for k in ['sea', 'water', 'ocean', 'canal', 'channel']):
        if line.startswith('[node') or 'shader' in line:
            print(line[:120])
