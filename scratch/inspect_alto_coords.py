import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see the position of AltoLixoDistrict and its main children
lines = text.splitlines()
for i, line in enumerate(lines):
    if 'name="AltoLixoDistrict"' in line:
        for j in range(i, min(i+15, len(lines))):
            print(lines[j])
        break

# Let's find RouteMarkers
for i, line in enumerate(lines):
    if 'name="RouteMarkers"' in line:
        for j in range(i, min(i+40, len(lines))):
            print(lines[j])
        break
