import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

scenes = re.findall(r'\[ext_resource\s+type="PackedScene"\s+path="([^"]+)"\s+id="([^"]+)"\]', text)
print(f"Total PackedScenes in sucateia.tscn: {len(scenes)}")
for path, id_ in scenes:
    print(f"PackedScene: id={id_}, path={path}")
