with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'\[node name="Player"[\s\S]*?(?=\[node name=)', text)
if m:
    print(m.group(0))

m_cam = re.search(r'\[node name="Camera2D"[\s\S]*?(?=\[node name=)', text)
if m_cam:
    print(m_cam.group(0))
