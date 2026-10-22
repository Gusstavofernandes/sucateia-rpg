import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines[:120]):
    print(f"{i+1}: {line}")
