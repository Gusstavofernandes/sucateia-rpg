import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\[node name="FutureExits"[^\]]*\](.*?)(?=\n\[node name="[^"]+" type="[^"]+" parent="AltoLixoDistrict"|\Z)', text, re.DOTALL)
if m:
    print("=== FutureExits ===")
    print(m.group(0)[:800])

m_front = re.search(r'\[node name="Frontiers"[^\]]*\](.*?)(?=\n\[node name="[^"]+" type="[^"]+" parent="AltoLixoDistrict"|\Z)', text, re.DOTALL)
if m_front:
    print("=== Frontiers ===")
    print(m_front.group(0)[:800])
