import re

with open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

nodes = re.findall(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]*)"\]', text)
print(f"Total de nós encontrados: {len(nodes)}")
for name, ntype, parent in nodes:
    print(f"[{parent}] -> {name} ({ntype})")
