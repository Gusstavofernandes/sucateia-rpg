with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('id="ShaderMaterial_875h6"')
if idx != -1:
    print(text[idx-50:idx+800])
