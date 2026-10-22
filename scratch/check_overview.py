with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if 'overview' in line or 'full' in line or 'zoom' in line:
        if 'capture_mode' in line:
            print(f"Line {i+1}: {line}")
            for j in range(i, min(len(lines), i+6)):
                print(f"  {lines[j]}")
