import re

def update_scene(scene_path):
    print(f"Atualizando {scene_path}...")
    with open(scene_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Atualizar ExtResource 69 e 70
    text = text.replace('path="res://assets/rails/tunel_mina_norte_v2.png"', 'path="res://assets/rails/boca_tunel_v2.png"')
    text = text.replace('path="res://assets/rails/tunel_mina_norte_v2_sombra.png"', 'path="res://assets/rails/boca_tunel_v2_sombra.png"')

    # 2. Adicionar SubResources de colisão da moldura do túnel se não existirem
    sub_res_def = """[sub_resource type="RectangleShape2D" id="RectangleShape2D_tunel_parede_oeste"]
size = Vector2(170, 70)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_tunel_parede_leste"]
size = Vector2(120, 70)
"""
    if 'RectangleShape2D_tunel_parede_oeste' not in text:
        # Inserir antes de [node name="FundoFerroMaster"
        idx = text.find('[node name="FundoFerroMaster"')
        text = text[:idx] + sub_res_def + '\n' + text[idx:]

    # 3. Atualizar bloco do nó TunelMinaEntrada
    old_tunel_pattern = r'\[node name="TunelMinaEntrada" type="[^"]*" parent="RedeFerroviariaMina"\][\s\S]*?(?=\[node name="EstacaoCarga")'
    new_tunel_block = """[node name="TunelMinaEntrada" type="StaticBody2D" parent="RedeFerroviariaMina"]
z_index = -11
position = Vector2(-188.94, 116.86)

[node name="ColisaoAsaOeste" type="CollisionShape2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
position = Vector2(-120, 45)
shape = SubResource("RectangleShape2D_tunel_parede_oeste")

[node name="ColisaoAsaLeste" type="CollisionShape2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
position = Vector2(130, 45)
shape = SubResource("RectangleShape2D_tunel_parede_leste")

[node name="SombraContato" type="Sprite2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
z_index = -12
position = Vector2(0, 8)
scale = Vector2(0.422378, 0.422378)
texture = ExtResource("70_tunel_mina_sombra")

[node name="TunelSprite" type="Sprite2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
scale = Vector2(0.422378, 0.422378)
texture = ExtResource("69_tunel_mina")

[node name="LuzLanternaTunel" type="PointLight2D" parent="RedeFerroviariaMina/TunelMinaEntrada"]
position = Vector2(-65, -30)
color = Color(1, 0.75, 0.38, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5

"""
    text = re.sub(old_tunel_pattern, new_tunel_block, text)

    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"{scene_path} atualizado com sucesso!")

update_scene('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn')
update_scene('scenes/fundo_ferro_master.tscn')
