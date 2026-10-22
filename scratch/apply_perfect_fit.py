import re

def update_fit(scene_path):
    print(f"Aplicando encaixe final validado em {scene_path}...")
    with open(scene_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Atualizar bloco TunelMinaEntrada com Y = 142.0
    old_pattern = r'\[node name="TunelMinaEntrada" type="[^"]*" parent="RedeFerroviariaMina"\][\s\S]*?(?=\[node name="EstacaoCarga")'
    new_block = """[node name="TunelMinaEntrada" type="StaticBody2D" parent="RedeFerroviariaMina"]
z_index = -11
position = Vector2(-190.41, 142.0)

[node name="ColisaoAsaOeste" type="CollisionShape2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
position = Vector2(-115, 35)
shape = SubResource("RectangleShape2D_tunel_parede_oeste")

[node name="ColisaoAsaLeste" type="CollisionShape2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
position = Vector2(125, 35)
shape = SubResource("RectangleShape2D_tunel_parede_leste")

[node name="SombraContato" type="Sprite2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
z_index = -12
position = Vector2(0, 8)
scale = Vector2(0.39021, 0.39021)
texture = ExtResource("70_tunel_mina_sombra")

[node name="TunelSprite" type="Sprite2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
scale = Vector2(0.39021, 0.39021)
texture = ExtResource("69_tunel_mina")

[node name="LuzLanternaTunel" type="PointLight2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
position = Vector2(-61, -45)
color = Color(1, 0.75, 0.38, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5

"""
    text = re.sub(old_pattern, new_block, text)
    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Pronto: {scene_path}")

update_fit('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn')
update_fit('scenes/fundo_ferro_master.tscn')
