with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

start = text.find('[node name="AltoLixoCais"')
if start != -1:
    print(text[start:start+1200])
