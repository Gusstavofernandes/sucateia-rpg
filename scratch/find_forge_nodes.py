import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource type="[^"]+" path="([^"]+)" id="([^"]+)"\]', content):
    ext_map[m.group(2)] = m.group(1).split('/')[-1]

print("--- SEARCHING REGIONPORTALS/TO_FORJAS ---")
for m in re.finditer(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]*)"[^\]]*\](.*?)(?=\n\[node|\Z)', content, re.DOTALL):
    parent = m.group(3)
    name = m.group(1)
    block = m.group(0)
    if "To_forjas" in parent or name == "To_forjas":
        pos_m = re.search(r'position = Vector2\(([^)]+)\)', block)
        tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', block)
        tex_name = ext_map.get(tex_m.group(1), "") if tex_m else ""
        print(f'{parent:35} | {name:20} | Pos: {pos_m.group(1) if pos_m else "None":20} | Tex: {tex_name}')

print("\n--- SEARCHING PIPES IN FORGE / BRIDGE AREA ---")
for m in re.finditer(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]*)"[^\]]*\](.*?)(?=\n\[node|\Z)', content, re.DOTALL):
    parent = m.group(3)
    name = m.group(1)
    block = m.group(0)
    tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', block)
    tex_name = ext_map.get(tex_m.group(1), "") if tex_m else ""
    if "pipe" in tex_name:
        pos_m = re.search(r'position = Vector2\(([^)]+)\)', block)
        rot_m = re.search(r'rotation = ([^\n]+)', block)
        scale_m = re.search(r'scale = Vector2\(([^)]+)\)', block)
        if pos_m:
            coords = [float(x.strip()) for x in pos_m.group(1).split(',')]
            if 1400 <= coords[0] <= 2400 and 700 <= coords[1] <= 1300:
                print(f'{parent:35} | {name:20} | Pos: {coords} | Rot: {rot_m.group(1) if rot_m else "0"} | Scale: {scale_m.group(1) if scale_m else "1"}')
