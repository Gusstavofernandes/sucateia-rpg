import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for all nodes having position or shapes, especially Walls, Floor, Boundaries
pattern = r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?\](.*?)(?=\n\[|$)'
matches = re.findall(pattern, text, re.DOTALL)

for name, ntype, parent, body in matches:
    if any(k in name.lower() for k in ["piso", "parede", "muralha", "limite", "borda", "colisao", "area", "sala"]):
        pos = re.search(r'position = Vector2\(([^)]+)\)', body)
        shape = re.search(r'shape = (SubResource\([^)]+\)|ExtResource\([^)]+\))', body)
        polygon = re.search(r'polygon = PackedVector2Array\(([^)]+)\)', body)
        print(f"Node: {name} | type: {ntype} | parent: {parent}")
        if pos: print(f"   pos: {pos.group(1)}")
        if shape: print(f"   shape: {shape.group(1)}")
        if polygon: print(f"   polygon points: {polygon.group(1)[:120]}...")
