from pathlib import Path
import re

tscn_path = Path("fundo_ferro_standalone/scenes/fundo_ferro_master.tscn")
text = tscn_path.read_text(encoding="utf-8")

root_children = re.findall(r'\[node name="([^"]+)" type="([^"]+)" parent="\."\]', text)
for name, typ in root_children:
    print(f"{name} ({typ})")
