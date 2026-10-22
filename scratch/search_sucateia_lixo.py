import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern matching node header
pattern = re.compile(r'\[node name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]')
nodes = pattern.findall(text)
print(f"Total nodes in sucateia.tscn: {len(nodes)}")

lixo_nodes = []
for name, ntype, parent in nodes:
    if any(k in name.lower() or k in parent.lower() for k in ['lix', 'scrap', 'dump', 'sucat', 'entulho', 'rejeito']):
        lixo_nodes.append((name, ntype, parent))

print(f"Nodes mentioning lixo/scrap/sucata: {len(lixo_nodes)}")
for n in lixo_nodes[:40]:
    print("  ", n)
