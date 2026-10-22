with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Inserir WallSegOeste em MuralhaNorte se não existir
if 'WallSegOeste' not in text:
    old_wall = '[node name="WallSeg1" type="Sprite2D" parent="MuralhaNorte"]'
    new_wall = """[node name="WallSegOeste" type="Sprite2D" parent="MuralhaNorte"]
position = Vector2(-450, 140)
scale = Vector2(0.85, 0.85)
texture = ExtResource("3_fundo_wall")

[node name="WallSeg1" type="Sprite2D" parent="MuralhaNorte"]"""
    text = text.replace(old_wall, new_wall)
    with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'w', encoding='utf-8') as f:
        f.write(text)
    print("WallSegOeste adicionado em standalone!")
else:
    print("WallSegOeste já existe!")
