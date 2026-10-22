with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'WestWaterline' in l or 'WestCoastalBarrier' in l:
        print("".join(lines[max(0, i-2):min(len(lines), i+25)]))
        print("="*60)
