import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\[node name="AltoLixoDistrict"[^\]]*\](.*?)(?=\n\[node name="[^"]+" type="[^"]+" parent="\."|\Z)', text, re.DOTALL)
if m:
    block = m.group(0)
    # Find all position = Vector2(x, y)
    pos_matches = re.findall(r'position = Vector2\(([^,]+),\s*([^)]+)\)', block)
    xs = [float(x) for x, y in pos_matches]
    ys = [float(y) for x, y in pos_matches]
    print(f"AltoLixo positions: count={len(pos_matches)}")
    print(f"X range: min={min(xs):.1f}, max={max(xs):.1f}")
    print(f"Y range: min={min(ys):.1f}, max={max(ys):.1f}")

    # Let's check groups inside AltoLixoDistrict
    groups = re.findall(r'\[node name="([^"]+)" type="Node2D" parent="AltoLixoDistrict"[^\]]*\]', block)
    print("Direct sub-groups of AltoLixoDistrict:", groups)
