with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
shaders = re.findall(r'\[ext_resource\s+type="Shader"\s+path="([^"]+)"\s+id="([^"]+)"\]', text)
print("Shaders in sucateia.tscn:")
for p, id_ in shaders:
    print(id_, '->', p)
