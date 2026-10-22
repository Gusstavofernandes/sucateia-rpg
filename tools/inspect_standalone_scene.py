from pathlib import Path
import re

tscn_path = Path("fundo_ferro_standalone/scenes/fundo_ferro_master.tscn")
text = tscn_path.read_text(encoding="utf-8")

nodes = re.findall(r'\[node name="([^"]+)" type="([^"]+)"(?: parent="([^"]*)")?\]', text)
for name, typ, parent in nodes:
    if any(k in name.lower() for k in ["colis", "static", "block", "wall", "limite"]):
        print(f"Parent: {parent} | Node: {name} ({typ})")
