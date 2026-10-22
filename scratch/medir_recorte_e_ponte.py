import re

with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

nodes = re.findall(r'\[node name="([^"]+)" type="([^"]+)"(?:\s+parent="([^"]*)")?\]', text)
print(f"Total de nós: {len(nodes)}")
for name, ntype, parent in nodes:
    if parent in ['', '.'] or any(k in name for k in ['Parede', 'Canal', 'Cano', 'Bg', 'Fundo', 'Tile', 'Ambiente', 'Dreno', 'Bueiro']):
        print(f"  {name} ({ntype}, parent={parent})")
