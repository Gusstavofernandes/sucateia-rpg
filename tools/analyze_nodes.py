import re
import json

scene_path = 'maps/sucateia/sucateia.tscn'
with open(scene_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

nodes = re.findall(r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?', content)
print(f"Total node definitions in {scene_path}: {len(nodes)}")

type_counts = {}
parent_tree = {}

for name, ntype, parent in nodes:
    t = ntype if ntype else "Instance/PackedScene"
    p = parent if parent else "."
    type_counts[t] = type_counts.get(t, 0) + 1
    if p not in parent_tree:
        parent_tree[p] = []
    parent_tree[p].append((name, t))

print("\n--- DISTRIBUIÇÃO DE TIPOS DE NÓS ---")
for t, count in sorted(type_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{t}: {count} nós")

print("\n--- PRINCIPAIS RAMOS DA ÁRVORE (HIERARQUIA) ---")
for p, children in sorted(parent_tree.items(), key=lambda x: len(x[1]), reverse=True)[:30]:
    print(f"Pai: '{p}' -> {len(children)} nós filhos")

with open('tools/node_tree_dump.json', 'w', encoding='utf-8') as out:
    json.dump(parent_tree, out, indent=2, ensure_ascii=False)
print("\nDump completo salvo em tools/node_tree_dump.json")
