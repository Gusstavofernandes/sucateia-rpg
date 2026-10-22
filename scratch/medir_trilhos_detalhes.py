import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

ext_resources = re.findall(r'\[ext_resource type="([^"]+)" path="([^"]+)" id="([^"]+)"\]', text)
res_dict = {i: p for t, p, i in ext_resources}

print("--- RECURSOS DE TRILHOS / ESTAÇÃO / CAVALETE ---")
for i, p in res_dict.items():
    if any(k in p.lower() for k in ["trilho", "cavalete", "estacao", "tunel", "guincho"]):
        print(f"ID {i} -> {p}")

print("\n--- NÓS DE REDE FERROVIÁRIA ---")
pattern = r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?\](.*?)(?=\n\[|$)'
for name, ntype, parent, body in re.findall(pattern, text, re.DOTALL):
    if "ferroviaria" in parent.lower() or "cavalete" in name.lower() or "tunel" in name.lower() or "estacao" in name.lower():
        tex = re.search(r'texture = ExtResource\("([^"]+)"\)', body)
        tex_path = res_dict.get(tex.group(1), "") if tex else ""
        pos = re.search(r'position = Vector2\(([^)]+)\)', body)
        scale = re.search(r'scale = Vector2\(([^)]+)\)', body)
        print(f"Node: {name} (parent: {parent})")
        if pos: print(f"   pos: {pos.group(1)}")
        if scale: print(f"   scale: {scale.group(1)}")
        if tex_path: print(f"   tex: {tex_path}")
