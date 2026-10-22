import filecmp

for f in ['scenes/fundo_ferro_master.tscn', 'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'maps/fundo_ferro/fundo_ferro.tscn']:
    import os
    print(f, 'exists:', os.path.exists(f), 'size:', os.path.getsize(f) if os.path.exists(f) else 0)

same = filecmp.cmp('scenes/fundo_ferro_master.tscn', 'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn')
print("scenes/fundo_ferro_master.tscn == fundo_ferro_standalone/scenes/fundo_ferro_master.tscn:", same)
