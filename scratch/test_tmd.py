import struct
import base64
import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\[node name="AltoFloor" type="TileMapLayer"[^\]]*\](.*?)(?=\n\[node|\Z)', text, re.DOTALL)
body = m.group(1)
bm = re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)', body)
raw = base64.b64decode(bm.group(1))

header = struct.unpack('<h', raw[:2])[0]
print(f"Header: {header}")

cells = []
for i in range(2, len(raw), 12):
    x, y, src, ax, ay, alt = struct.unpack('<hhhhhh', raw[i:i+12])
    cells.append((x, y, src, ax, ay, alt))

xs = [c[0] for c in cells]
ys = [c[1] for c in cells]
print(f"Cell X range: {min(xs)} to {max(xs)} (pixels: {min(xs)*48} to {max(xs)*48})")
print(f"Cell Y range: {min(ys)} to {max(ys)} (pixels: {min(ys)*48} to {max(ys)*48})")

# Let's see the cells around the bottom-right of AltoFloor
bottom_cells = [c for c in cells if c[1] >= max(ys) - 3]
print(f"Bottom-most cells (max Y = {max(ys)}, Y px = {max(ys)*48}):")
for c in sorted(bottom_cells, key=lambda c: (c[1], c[0])):
    print(f"  cell ({c[0]}, {c[1]}) -> pixel pos ({c[0]*48}, {c[1]*48})")
