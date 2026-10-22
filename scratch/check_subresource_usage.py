with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if 'ShaderMaterial_875h6' in line:
        print(f"Line {i+1}: {line}")
        # print surrounding lines
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"  {j+1}: {lines[j]}")
