import re

def atualizar_ponte(scene_path):
    print(f"Atualizando ponte em {scene_path}...")
    with open(scene_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Bloco CavaleteElevadoCanal atualizado
    old_cavalete_pattern = r'\[node name="CavaleteElevadoCanal" type="StaticBody2D" parent="RedeFerroviariaMina"\][\s\S]*?(?=\[node name="Player")'
    new_cavalete_block = """[node name="CavaleteElevadoCanal" type="StaticBody2D" parent="RedeFerroviariaMina"]
y_sort_enabled = true
position = Vector2(-188, 593.5)

[node name="ColPilarOeste" type="CollisionShape2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
position = Vector2(-95, 135)
shape = SubResource("RectangleShape2D_cavalete_pilar")

[node name="ColPilarLeste" type="CollisionShape2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
position = Vector2(95, 135)
shape = SubResource("RectangleShape2D_cavalete_pilar")

[node name="SombraContato" type="Sprite2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
z_index = -6
position = Vector2(0, 10)
scale = Vector2(0.40, 0.40)
texture = ExtResource("74_cavalete_alto_sombra")

[node name="CavaleteSprite" type="Sprite2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
scale = Vector2(0.40, 0.40)
texture = ExtResource("73_cavalete_alto")

[node name="TrilhosSobreCavalete" type="Sprite2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
z_index = 1
position = Vector2(0, -93.75)
scale = Vector2(0.25, 0.25)
texture = ExtResource("75_trilho_vertical")

"""
    text = re.sub(old_cavalete_pattern, new_cavalete_block, text)
    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Pronto: {scene_path}")

atualizar_ponte('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn')
atualizar_ponte('scenes/fundo_ferro_master.tscn')
