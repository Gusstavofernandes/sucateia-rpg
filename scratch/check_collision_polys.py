with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if 'CollisionPolygon2D' in line:
        print(f"Line {i+1}: {line}")
        for j in range(i, min(len(lines), i+15)):
            if 'polygon =' in lines[j]:
                print(f"  {lines[j][:120]}")
