import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for line in lines:
    if any(k in line for k in ['CanvasModulate', 'DirectionalLight2D', 'ColorRect', 'Atmosphere', 'modulate']):
        if line.startswith('[node') or 'color' in line or 'modulate' in line:
            print(line[:120])
