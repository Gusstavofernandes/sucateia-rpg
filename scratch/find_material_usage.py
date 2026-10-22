with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = 0
while True:
    idx = text.find('ShaderMaterial_nvhpu', idx)
    if idx == -1:
        break
    start = max(0, idx - 150)
    end = min(len(text), idx + 350)
    print("--- USAGE ---")
    print(text[start:end])
    idx += len('ShaderMaterial_nvhpu')
