from pathlib import Path
import re
s=Path('maps/sucateia/sucateia.tscn').read_text(encoding='utf-8')
ids=[m[1] for m in re.findall(r'\[ext_resource type="Texture2D" path="([^"]*pipe[^"]*)" id="([^"]+)"\]',s)]
for block in s.split('[node ')[1:]:
    if 'Forjas' in block.split(']')[0] and any(f'texture = ExtResource("{i}")' in block for i in ids):
        at=re.search(r'position = Vector2\(([-\d.]+), ([-\d.]+)\)',block)
        if at and 2750<float(at[1])<3300 and -100<float(at[2])<150:
            print(block[:450])
