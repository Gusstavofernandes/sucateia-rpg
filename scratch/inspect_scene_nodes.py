with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'\[node name="([^"]+)"[^\]]*\]', text)
west_nodes = [m for m in matches if 'West' in m or 'Water' in m or 'Barrier' in m or 'Cais' in m]
print('Nos relacionados a West/Cais/Water:', west_nodes)
