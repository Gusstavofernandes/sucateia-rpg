import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

pattern = r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?\](.*?)(?=\n\[|$)'
matches = re.findall(pattern, text, re.DOTALL)

for name, ntype, parent, body in matches:
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', body)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        if y > 500:
            print(f"{name:30} | pos: ({x:7.1f}, {y:7.1f}) | parent: {parent}")
