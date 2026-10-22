import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r'\[ext_resource[^\]]+path="res://assets/region/([^"]+)"[^\]]+id="([^"]+)"', text)
for path, eid in m:
    print(f"{path} -> {eid}")
