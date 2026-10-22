import struct
import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\[node name="AltoFloor" type="TileMapLayer"[^\]]*\](.*?)(?=\n\[node|\Z)', text, re.DOTALL)
if m:
    body = m.group(1)
    bm = re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)', body)
    if bm:
        import base64
        raw = base64.b64decode(bm.group(1))
        # Each cell in Godot 4 TileMapLayer PackedByteArray:
        # 12 bytes per cell:
        # int16 x, int16 y, int16 layer, uint16 source_id, int16 atlas_x, int16 atlas_y, ...
        cells = []
        for i in range(0, len(raw), 12):
            if i + 12 <= len(raw):
                x, y, l, src, ax, ay = struct.unpack('<hhhhhh', raw[i:i+12])
                cells.append((x, y))
        min_x = min(c[0] for c in cells)
        max_x = max(c[0] for c in cells)
        min_y = min(c[1] for c in cells)
        max_y = max(c[1] for c in cells)
        print(f"AltoFloor cell count: {len(cells)}")
        print(f"Cell range: X in [{min_x}, {max_x}], Y in [{min_y}, {max_y}]")
        # Tile size: let's check tile_set ExtResource("44_cxu03")
