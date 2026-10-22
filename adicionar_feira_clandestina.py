import os

def integrate_feira_clandestina():
    master_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
    with open(master_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add ext_resources for the 4 bazaar assets
    ext_target = '[ext_resource type="PackedScene" path="res://scenes/ArenaColiseu.tscn" id="148_arena_coliseu_scene"]'
    ext_addition = '''[ext_resource type="PackedScene" path="res://scenes/ArenaColiseu.tscn" id="148_arena_coliseu_scene"]
[ext_resource type="Texture2D" path="res://assets/props/feira_barraca_apostas_v1.png" id="149_feira_barraca_apostas"]
[ext_resource type="Texture2D" path="res://assets/props/feira_barraca_apostas_v1_sombra.png" id="150_feira_barraca_apostas_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/feira_barraca_pecas_raras_v1.png" id="151_feira_barraca_pecas"]
[ext_resource type="Texture2D" path="res://assets/props/feira_barraca_pecas_raras_v1_sombra.png" id="152_feira_barraca_pecas_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/feira_jaula_humanoides_v1.png" id="153_feira_jaula_humanoides"]
[ext_resource type="Texture2D" path="res://assets/props/feira_jaula_humanoides_v1_sombra.png" id="154_feira_jaula_humanoides_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/feira_tapete_troca_sucata_v1.png" id="155_feira_tapete_sucata"]
[ext_resource type="Texture2D" path="res://assets/props/feira_tapete_troca_sucata_v1_sombra.png" id="156_feira_tapete_sucata_sombra"]'''

    if ext_target in content:
        content = content.replace(ext_target, ext_addition, 1)
        print("1. Added ext_resources for feira clandestina")
    else:
        print("WARNING: ext_target not found")

    # 2. Add collision sub_resources
    subres_target = '[sub_resource type="CapsuleShape2D" id="CapsuleShape2D_player"]'
    subres_addition = '''[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_barraca_apostas"]
size = Vector2(190, 80)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_barraca_pecas"]
size = Vector2(210, 95)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_jaula_humanoides"]
size = Vector2(200, 100)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_bau_tapete"]
size = Vector2(60, 45)

[sub_resource type="CapsuleShape2D" id="CapsuleShape2D_player"]'''

    if subres_target in content:
        content = content.replace(subres_target, subres_addition, 1)
        print("2. Added sub_resources for feira clandestina")
    else:
        print("WARNING: subres_target not found")

    # 3. Add FeiraClandestinaFundoFerro node right before ArenaColiseu
    node_target = '[node name="ArenaColiseu" parent="." instance=ExtResource("148_arena_coliseu_scene")]'
    feira_nodes = '''[node name="FeiraClandestinaFundoFerro" type="Node2D" parent="."]
y_sort_enabled = true

[node name="BarracaApostas_Principal" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3980, 830)
scale = Vector2(0.24, 0.24)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Principal"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("150_feira_barraca_apostas_sombra")
offset = Vector2(0, -475)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Principal"]
texture = ExtResource("149_feira_barraca_apostas")
offset = Vector2(0, -475)

[node name="LuzLanternaApostas" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Principal"]
position = Vector2(95, -150)
color = Color(1, 0.65, 0.28, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.5

[node name="ColisaoBalcao" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Principal"]
scale = Vector2(4.166, 4.166)

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Principal/ColisaoBalcao"]
position = Vector2(-2, -25)
shape = SubResource("RectangleShape2D_base_barraca_apostas")


[node name="BarracaPecasRaras" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3440, 890)
scale = Vector2(0.25, 0.25)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("152_feira_barraca_pecas_sombra")
offset = Vector2(0, -470)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
texture = ExtResource("151_feira_barraca_pecas")
offset = Vector2(0, -470)

[node name="LuzCristaisArcanos" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
position = Vector2(-30, -180)
color = Color(0.2, 0.9, 0.95, 1)
energy = 2.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.2

[node name="LuzLanternaBanca" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
position = Vector2(250, -380)
color = Color(1, 0.72, 0.35, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.8

[node name="ColisaoBanca" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
scale = Vector2(4.0, 4.0)

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras/ColisaoBanca"]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_base_barraca_pecas")


[node name="TapeteTrocaSucata_1" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3720, 970)
scale = Vector2(0.22, 0.22)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_1"]
z_index = -12
position = Vector2(5, 10)
texture = ExtResource("156_feira_tapete_sucata_sombra")
offset = Vector2(0, -425)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_1"]
z_index = -10
texture = ExtResource("155_feira_tapete_sucata")
offset = Vector2(0, -425)

[node name="LuzLamparinaChao" type="PointLight2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_1"]
position = Vector2(130, -320)
color = Color(1, 0.8, 0.42, 1)
energy = 1.5
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5

[node name="ColisaoBau" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_1"]
scale = Vector2(4.545, 4.545)

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_1/ColisaoBau"]
position = Vector2(-75, -60)
shape = SubResource("RectangleShape2D_base_bau_tapete")


[node name="JaulaHumanoidesMercadoria" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3980, 1140)
scale = Vector2(0.26, 0.26)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/JaulaHumanoidesMercadoria"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("154_feira_jaula_humanoides_sombra")
offset = Vector2(0, -465)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/JaulaHumanoidesMercadoria"]
texture = ExtResource("153_feira_jaula_humanoides")
offset = Vector2(0, -465)

[node name="LuzLanternaJaula" type="PointLight2D" parent="FeiraClandestinaFundoFerro/JaulaHumanoidesMercadoria"]
position = Vector2(380, -360)
color = Color(0.95, 0.55, 0.22, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.0

[node name="ColisaoJaula" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/JaulaHumanoidesMercadoria"]
scale = Vector2(3.846, 3.846)

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/JaulaHumanoidesMercadoria/ColisaoJaula"]
position = Vector2(0, -35)
shape = SubResource("RectangleShape2D_base_jaula_humanoides")


[node name="TapeteTrocaSucata_2" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3420, 1180)
scale = Vector2(-0.21, 0.21)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_2"]
z_index = -12
position = Vector2(5, 10)
texture = ExtResource("156_feira_tapete_sucata_sombra")
offset = Vector2(0, -425)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_2"]
z_index = -10
texture = ExtResource("155_feira_tapete_sucata")
offset = Vector2(0, -425)

[node name="LuzLamparinaChao" type="PointLight2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_2"]
position = Vector2(130, -320)
color = Color(1, 0.75, 0.38, 1)
energy = 1.4
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.2


[node name="BarracaApostas_Secundaria" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3700, 1280)
scale = Vector2(0.22, 0.22)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Secundaria"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("150_feira_barraca_apostas_sombra")
offset = Vector2(0, -475)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Secundaria"]
texture = ExtResource("149_feira_barraca_apostas")
offset = Vector2(0, -475)

[node name="LuzLanternaApostas" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Secundaria"]
position = Vector2(95, -150)
color = Color(1, 0.65, 0.28, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.0

[node name="ColisaoBalcao" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Secundaria"]
scale = Vector2(4.545, 4.545)

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Secundaria/ColisaoBalcao"]
position = Vector2(-2, -25)
shape = SubResource("RectangleShape2D_base_barraca_apostas")

[node name="ArenaColiseu" parent="." instance=ExtResource("148_arena_coliseu_scene")]'''

    if node_target in content:
        content = content.replace(node_target, feira_nodes, 1)
        print("3. Added FeiraClandestinaFundoFerro nodes to master scene")
    else:
        print("WARNING: node_target not found")

    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("fundo_ferro_master.tscn updated successfully with Feira Clandestina!")

if __name__ == '__main__':
    integrate_feira_clandestina()
