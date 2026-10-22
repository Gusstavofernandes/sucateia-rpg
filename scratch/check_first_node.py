with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if line.startswith('[node name='):
        print(f"Line {i+1}: {line}")
        for j in range(i+1, min(i+40, len(lines))):
            print(f"  {lines[j]}")
            if lines[j].startswith('[node name='):
                break
        break
