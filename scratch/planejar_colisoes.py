with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Inspecionar as muretas do canal em X < 500
print("--- MURETAS E BORDAS DO CANAL ---")
for m in re.finditer(r'\[node name="Edge[^"]*" type="Sprite2D" parent="MuretasCanal"\][\s\S]*?(?=\[node name=)', text):
    lines = m.group(0).splitlines()
    pos = [l for l in lines if 'position = ' in l]
    print(lines[0], pos[0] if pos else "")

# Inspecionar colisões de canal existentes
print("\n--- COLISÕES DE CANAL EXISTENTES ---")
for m in re.finditer(r'\[node name="ColisaoCanal_[^"]*" type="StaticBody2D" parent="CanalDeEsgoto"\][\s\S]*?(?=\[node name=)', text):
    lines = m.group(0).splitlines()
    pos = [l for l in lines if 'position = ' in l]
    print(lines[0], pos[0] if pos else "")
