with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

# Find nodes under RegionalContinuity
start = text.find('[node name="RegionalContinuity"')
end = text.find('\n[node name="', start + 100)
# RegionalContinuity has children until next non-RegionalContinuity node
end_rc = text.find('\n[node name="', text.find('DockWarehouse', start) if 'DockWarehouse' in text else start + 5000)

rc_chunk = text[start:start+15000]
for block in rc_chunk.split('\n\n'):
    if any(k in block for k in ['@Sprite2D@38', '@Sprite2D@39', '@Sprite2D@40', '@Sprite2D@43', '@Line2D@41', '@Line2D@42', '@Line2D@44', '@Line2D@45']):
        print('--- BLOCK ---')
        print(block)
