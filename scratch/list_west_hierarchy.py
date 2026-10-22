import re

with open(r'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'\[node name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\](.*?)(?=\[node|\Z)', re.DOTALL)
pos_pattern = re.compile(r'position\s*=\s*Vector2\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)')

for match in pattern.finditer(text):
    node_name = match.group(1)
    node_type = match.group(2) or ""
    parent = match.group(3) or "."
    content = match.group(4)
    pos_match = pos_pattern.search(content)
    if pos_match:
        x, y = float(pos_match.group(1)), float(pos_match.group(2))
        if -600 < x < 350 and parent in [".", "MuralhaNorte", "EntulhoESucataNoChao", "RedeFerroviariaMina"]:
            print(f"[{parent}] {node_name} ({node_type}) -> position: ({x}, {y})")
