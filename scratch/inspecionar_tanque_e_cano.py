import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

pattern = r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?\](.*?)(?=\n\[|$)'
matches = re.findall(pattern, text, re.DOTALL)

print("=== BUSCA POR TANQUE VERDE OU ELEMENTOS VERDES NA MARGEM NORTE (Y < 500) ===")
for name, ntype, parent, body in matches:
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', body)
    pos_str = pos_m.group(0) if pos_m else ""
    if any(k in name.lower() for k in ["tanque", "verde", "quimic", "decant", "cisterna", "poco", "bueiro", "tubo"]):
        print(f"{name:30} | {pos_str:25} | parent: {parent}")

print("\n=== TUBULAÇÃO OESTE E FIAÇÃO (X entre 50 e 400) ===")
for name, ntype, parent, body in matches:
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', body)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        if 50 <= x <= 400 and 550 <= y <= 750:
            print(f"{name:30} | pos=({x:6.1f}, {y:6.1f}) | parent: {parent}")
