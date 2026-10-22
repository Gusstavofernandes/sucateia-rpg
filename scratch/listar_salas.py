import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's find all node definitions and their positions
pattern = r'\[node name="([^"]+)" type="([^"]+)"(?: parent="([^"]+)")?\]\s*(.*?)(?=\n\[|$)'
matches = re.findall(pattern, text, re.DOTALL)

print(f"Total matched nodes: {len(matches)}")
for name, ntype, parent, body in matches:
    pos_m = re.search(r'position = Vector2\(([^)]+)\)', body)
    pos = pos_m.group(1) if pos_m else ""
    # if parent is root or top-level container:
    if parent in [".", "", "Node2D"] or any(k in name.lower() for k in ["tanque", "quimic", "verde", "parede", "sala", "galeria", "dreno", "bueiro", "limite"]):
        print(f"{name:30} | {ntype:20} | parent: {parent:15} | pos: {pos}")
