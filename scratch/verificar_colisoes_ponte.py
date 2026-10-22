with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Buscar pontes e canal
print("--- PONTES NA CENA ---")
for m in re.finditer(r'\[node name="([^"]*Ponte[^"]*|[^"]*Cavalete[^"]*)" type="([^"]*)" parent="([^"]*)"\]([\s\S]*?)(?=\[node name=)', text):
    name, node_type, parent, body = m.group(1), m.group(2), m.group(3), m.group(4)
    print(f"\nNode: {name} ({node_type}) parent: {parent}")
    for l in body.splitlines()[:15]:
        print("  ", l)

print("\n--- COLISÕES DO CANAL DE ESGOTO ---")
m_canal = re.search(r'\[node name="CanalDeEsgoto"[\s\S]*?(?=\[node name="MuretasCanal")', text)
if m_canal:
    for l in m_canal.group(0).splitlines():
        if 'node name=' in l or 'shape = ' in l or 'position = ' in l:
            print("  ", l)
