import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

pattern = r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?\]'
nodes = re.findall(pattern, text)
print(f"Total nodes: {len(nodes)}")

by_parent = {}
for name, ntype, parent in nodes:
    by_parent.setdefault(parent, []).append((name, ntype))

def print_tree(parent="", indent=0):
    for name, ntype in by_parent.get(parent, []):
        full_path = f"{parent}/{name}" if parent and parent != "." else name
        children = by_parent.get(full_path, by_parent.get(name, []))
        print("  " * indent + f"- {name} ({ntype}) [children: {len(children)}]")
        if len(children) > 0 and indent < 3:
            print_tree(full_path, indent + 1)

print("\n--- ÁRVORE DE NÓS DE FUNDO_FERRO_MASTER.TSCN ---")
print_tree(".", 0)
