import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect RedeFerroviariaMina and all its children
pattern = r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?\](.*?)(?=\n\[|$)'
matches = re.findall(pattern, text, re.DOTALL)

for name, ntype, parent, body in matches:
    if "ferroviaria" in parent.lower() or "ferroviaria" in name.lower() or "cavalete" in parent.lower() or "cavalete" in name.lower() or "estacao" in name.lower():
        print(f"--- Node: {name} (type: {ntype}, parent: {parent}) ---")
        for line in body.strip().splitlines()[:15]:
            print(f"    {line}")
