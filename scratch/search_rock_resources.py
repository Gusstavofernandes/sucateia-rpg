import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_resources = re.findall(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text)
print("Matching ext_resources in sucateia.tscn:")
for t, p, id_ in ext_resources:
    if any(k in p.lower() for k in ['rock', 'cliff', 'crag', 'stone', 'rocha', 'pedra', 'coastal', 'salvage', 'coast']):
        print(f"id={id_} | path={p}")
