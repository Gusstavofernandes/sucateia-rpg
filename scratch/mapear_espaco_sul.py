import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

pattern = r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?\](.*?)(?=\n\[|$)'
matches = re.findall(pattern, text, re.DOTALL)

print("=== ELEMENTOS NA MARGEM SUL (Y > 520) NO SETOR OESTE (X < 1200) ===")
for name, ntype, parent, body in matches:
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', body)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        if y >= 500 and x < 1200:
            scale_m = re.search(r'scale = Vector2\(([^,]+),\s*([^)]+)\)', body)
            sc = scale_m.group(0) if scale_m else ""
            print(f"{name:32} | pos: ({x:7.1f}, {y:7.1f}) | {sc:22} | parent: {parent}")

# Vamos ver as paredes sul e limites da camera
print("\n=== LIMITES GLOBAIS DA CENA ===")
for name, ntype, parent, body in matches:
    if "camera" in name.lower() or "bedrock" in name.lower() or "limite" in name.lower() or "parede_sul" in name.lower():
        print(f"{name} ({ntype}):")
        for l in body.strip().splitlines()[:8]:
            print(f"   {l}")
