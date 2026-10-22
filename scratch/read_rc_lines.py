with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '@Sprite2D@37' in line and 'RegionalContinuity' in line:
        start_idx = max(0, i - 2)
        end_idx = min(len(lines), i + 80)
        for j in range(start_idx, end_idx):
            print(f"{j+1}: {lines[j]}", end='')
        break
