import re

with open(r'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'\[node name="([^"]+)"[^\]]*\](.*?)(?=\[node|\Z)', re.DOTALL)
pos_pattern = re.compile(r'position\s*=\s*Vector2\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)')

for match in pattern.finditer(text):
    node_name = match.group(1)
    content = match.group(2)
    pos_match = pos_pattern.search(content)
    if pos_match:
        x, y = float(pos_match.group(1)), float(pos_match.group(2))
        if -600 < x < 200:
            print(f"{node_name}: position = ({x}, {y})")
