import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Print top-level nodes (parent=".")
top_nodes = re.findall(r'\[node name="([^"]+)" type="([^"]+)" parent="\."\]', text)
print("Top-level nodes (parent='.'):")
for name, ntype in top_nodes:
    print(f"  {name} ({ntype})")

# Also root node
root_node = re.findall(r'\[node name="([^"]+)" type="([^"]+)"\]', text)
print("Root node:", root_node[:3])
