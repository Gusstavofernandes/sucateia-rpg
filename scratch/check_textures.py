with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
from PIL import Image

for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    if m.group(3) in ['7_walkway', '66_passarela', '67_passarela_sombra']:
        res_path = m.group(2).replace('res://', '')
        print(m.group(3), '->', res_path)
        try:
            im = Image.open(res_path)
            print('  size:', im.size)
        except Exception as e:
            print('  error:', e)
