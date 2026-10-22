with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

start = text.find('[node name="Player"')
if start != -1:
    print(text[start:start+1200])
