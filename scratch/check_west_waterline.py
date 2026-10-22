with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('WestWaterline')
if idx != -1:
    print(text[idx-50:idx+600])
else:
    print("WestWaterline NOT found in sucateia.tscn")
