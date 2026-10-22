import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\[ext_resource\s+type="Shader"\s+path="res://assets/reconstruction/alto_ground\.gdshader"\s+id="([^"]+)"\]', text)
if m:
    shader_id = m.group(1)
    print(f"alto_ground shader id: {shader_id}")
    sub_matches = re.findall(r'\[sub_resource type="ShaderMaterial" id="([^"]+)"\]\nshader = ExtResource\("' + shader_id + '"\)', text)
    print(f"Subresources: {sub_matches}")
    for sub in sub_matches:
        for node in re.finditer(r'\[node name="([^"]+)"(?: type="([^"]+)")?(?: parent="([^"]+)")?[^\]]*\]\n(?:[^\n]*\n)*?material = SubResource\("' + sub + '"\)', text):
            print(f"Node: {node.group(1)} parent={node.group(3)}")
else:
    print("alto_ground not found in ext_resource")
