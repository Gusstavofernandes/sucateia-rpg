import re

with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for shape_id in ['RectangleShape2D_pipe_block_e3', 'RectangleShape2D_pipe_block_e4']:
    idx = text.find(f'id="{shape_id}"')
    if idx != -1:
        print(text[idx-50:idx+150])
