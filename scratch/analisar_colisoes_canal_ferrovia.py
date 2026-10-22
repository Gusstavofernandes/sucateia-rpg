with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Buscar todas as colisões do canal de esgoto
print("--- CANAL DE ESGOTO SHAPES ---")
m = re.search(r'\[node name="CanalDeEsgoto"[\s\S]*?(?=\[node name="MuretasCanal")', text)
if m:
    print(m.group(0))

# Buscar SubResource de canal
sub_shapes = re.findall(r'\[sub_resource type="RectangleShape2D" id="([^"]*channel[^"]*)"\][\s\S]*?size = Vector2\(([^)]+)\)', text)
for s_id, s_size in sub_shapes:
    print(f"SubResource {s_id}: size = {s_size}")

# Buscar colisões da RedeFerroviariaMina
print("\n--- REDE FERROVIARIA MINA ---")
m_rede = re.search(r'\[node name="RedeFerroviariaMina"[\s\S]*?(?=\[node name="Player")', text)
if m_rede:
    lines = m_rede.group(0).splitlines()
    for l in lines:
        if 'node name=' in l or 'shape = ' in l or 'position = ' in l or 'z_index = ' in l:
            print("  ", l)
