with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if any(k in line for k in ['IndustrialSea', 'WestWaterline', 'SouthWaterline']):
        print(f"Line {i+1}: {line}")
        for j in range(i, min(len(lines), i+25)):
            print(f"  {lines[j]}")
            if lines[j].startswith('[node name=') and j > i:
                break
