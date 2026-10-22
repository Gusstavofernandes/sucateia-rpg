import re

for bak in ['maps/sucateia/sucateia.tscn.bak', 'maps/sucateia/sucateia.tscn.bak2', 'maps/sucateia/sucateia.tscn.bak6', 'maps/sucateia/sucateia.tscn']:
    try:
        with open(bak, 'r', encoding='utf-8') as f:
            text = f.read()
        m = re.findall(r'\[node name="GrandeLixao"[^\n]*\nposition = Vector2\([^\)]+\)', text)
        print(bak, m)
    except Exception as e:
        print(bak, e)
