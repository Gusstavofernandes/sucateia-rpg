with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('CanoLesteModular')
if idx != -1:
    print(text[idx-50:idx+1500])
