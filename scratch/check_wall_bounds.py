with open('scenes/fundo_ferro_master.tscn', encoding='utf-8') as f:
    text = f.read()

import re
# Achar ExtResource 3_fundo_wall
m = re.search(r'\[ext_resource type="Texture2D" path="([^"]+)" id="3_fundo_wall"\]', text)
if m:
    print("Texture path:", m.group(1))
    from PIL import Image
    # Se path começa com res://, converter para local
    p = m.group(1).replace('res://', '')
    img = Image.open('fundo_ferro_standalone/' + p)
    print("Tamanho WallSeg1 textura:", img.size)
    # Escala 0.85, pos = Vector2(700, 140)
    w_world = img.width * 0.85
    left_x = 700 - w_world / 2.0
    right_x = 700 + w_world / 2.0
    print(f"WallSeg1 mundo: X vai de {left_x:.2f} a {right_x:.2f}")
