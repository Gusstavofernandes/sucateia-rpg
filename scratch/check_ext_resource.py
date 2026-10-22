with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', encoding='utf-8') as f:
    text = f.read()

for l in text.splitlines():
    if '69_tunel_mina' in l or '70_tunel_mina' in l:
        print(l)
