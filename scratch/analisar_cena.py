import re
import os

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

current_node = None
node_info = {}

for line in lines:
    m = re.match(r'\[node name="([^"]+)" type="([^"]+)"(?: parent="([^"]+)")?\]', line)
    if not m:
        m = re.match(r'\[node name="([^"]+)"(?: parent="([^"]+)")?\]', line)
    if m:
        name = m.group(1)
        parent = m.group(2) if len(m.groups()) >= 2 and m.group(2) else ""
        current_node = name
        node_info[current_node] = {"parent": parent, "props": []}
    elif current_node:
        if line.startswith("["):
            current_node = None
        else:
            line_str = line.strip()
            if any(k in line_str for k in ["position", "scale", "texture", "z_index", "offset"]):
                node_info[current_node]["props"].append(line_str)

keywords = ["ponte", "trilho", "tunel", "tanque", "caldeira", "verde", "canal", "estacao", "gerador", "bomba", "vapor", "cavalete"]
for name, data in node_info.items():
    if any(k in name.lower() for k in keywords):
        print(f"Node: {name} (parent: {data['parent']})")
        for p in data["props"]:
            print(f"   {p}")
