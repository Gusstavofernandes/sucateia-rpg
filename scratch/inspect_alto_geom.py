import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see the metadata and children of AltoLixoDistrict
m = re.search(r'\[node name="AltoLixoDistrict"[^\]]*\](.*?)(?=\n\[node name="[^"]+" type="[^"]+" parent="\."|\Z)', text, re.DOTALL)
if m:
    block = m.group(0)
    lines = block.splitlines()
    print(f"AltoLixoDistrict block lines: {len(lines)}")
    # Print sub-nodes under AltoLixoDistrict
    subnodes = [l for l in lines if l.startswith('[node name=')]
    print(f"Total subnodes in AltoLixo: {len(subnodes)}")
    for sn in subnodes[:25]:
        print(" ", sn)
    # Print any polygons or markers
    polys = [l for l in lines if 'polygon = PackedVector2Array' in l]
    print(f"Polygons in AltoLixo: {len(polys)}")
    for p in polys[:5]:
        print(" ", p[:120])
else:
    print("AltoLixoDistrict block not found")
