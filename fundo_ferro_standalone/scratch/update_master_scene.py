import os

tscn_path = 'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn'
with open(tscn_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update load_steps in the header
if 'load_steps=33' in content:
    content = content.replace('load_steps=33', 'load_steps=53', 1)

# 2. Insert new ExtResources before [sub_resource
new_resources = """
[ext_resource type="Texture2D" path="res://assets/machines/maquina_caldeira_vapor_v1.png" id="25_caldeira"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_caldeira_vapor_v1_sombra.png" id="26_caldeira_sombra"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_manifold_valvulas_v1.png" id="27_manifold"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_manifold_valvulas_v1_sombra.png" id="28_manifold_sombra"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_tanque_decantador_v1.png" id="29_decantador"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_tanque_decantador_v1_sombra.png" id="30_decantador_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_horizontal_valvula.png" id="31_tubo_valvula"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_horizontal_valvula_sombra.png" id="32_tubo_valvula_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_suporte_piso.png" id="33_tubo_suporte"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_suporte_piso_sombra.png" id="34_tubo_suporte_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_cotovelo_90.png" id="35_tubo_cotovelo"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_cotovelo_90_sombra.png" id="36_tubo_cotovelo_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_vertical_flange.png" id="37_tubo_vertical"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_vertical_flange_sombra.png" id="38_tubo_vertical_sombra"]
[ext_resource type="Texture2D" path="res://assets/puddles/poca_oleo_ambar.png" id="39_poca_oleo"]
[ext_resource type="Texture2D" path="res://assets/puddles/poca_toxica_limo.png" id="40_poca_limo"]
[ext_resource type="Texture2D" path="res://assets/puddles/poca_ferrugem_lodo.png" id="41_poca_ferrugem"]
[ext_resource type="PackedScene" path="res://scenes/VazamentoGota.tscn" id="42_vazamento_gota"]
[ext_resource type="PackedScene" path="res://scenes/VaporValvula.tscn" id="43_vapor_valvula"]
"""

if '[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]' in content:
    content = content.replace('[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]', new_resources.strip() + '\n\n[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]', 1)

# 3. Add the industrial nodes right after EstacaoBombeamento
new_nodes = """
[node name="RedeIndustrialMaquinas" type="Node2D" parent="."]
y_sort_enabled = true

[node name="PocaOleoBomba" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(1750, 770)
scale = Vector2(0.28, 0.28)
texture = ExtResource("39_poca_oleo")

[node name="VazamentoGotaBomba" parent="RedeIndustrialMaquinas" instance=ExtResource("42_vazamento_gota")]
position = Vector2(1750, 740)

[node name="TuboSuccaoCanal" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(1750, 600)
scale = Vector2(0.14, 0.14)
texture = ExtResource("37_tubo_vertical")

[node name="TuboSuccaoCanalSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboSuccaoCanal"]
modulate = Color(0, 0, 0, 0.45)
position = Vector2(0, 18)
texture = ExtResource("38_tubo_vertical_sombra")

[node name="CotoveloSuccaoCanal" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(1750, 645)
rotation = 1.5708
scale = Vector2(0.13, 0.13)
texture = ExtResource("35_tubo_cotovelo")

[node name="ManifoldOeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(750, 750)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
polygon = PackedVector2Array(-80, -10, 0, -25, 80, -10, 80, 25, 0, 35, -80, 25)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
modulate = Color(0, 0, 0, 0.5)
position = Vector2(0, 12)
scale = Vector2(0.24, 0.24)
texture = ExtResource("28_manifold_sombra")

[node name="Sprite" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
position = Vector2(0, -68)
scale = Vector2(0.24, 0.24)
texture = ExtResource("27_manifold")

[node name="PocaCondensado" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
z_index = -1
position = Vector2(0, 22)
scale = Vector2(0.25, 0.25)
texture = ExtResource("39_poca_oleo")

[node name="VaporManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("43_vapor_valvula")]
position = Vector2(15, -95)

[node name="VazamentoManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("42_vazamento_gota")]
position = Vector2(0, -10)

[node name="TuboEntradaManifold" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(750, 630)
scale = Vector2(0.13, 0.13)
texture = ExtResource("37_tubo_vertical")

[node name="CaldeiraVaporLeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(2650, 750)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
polygon = PackedVector2Array(-90, -15, 0, -30, 90, -15, 90, 30, 0, 45, -90, 30)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
modulate = Color(0, 0, 0, 0.5)
position = Vector2(0, 12)
scale = Vector2(0.24, 0.24)
texture = ExtResource("26_caldeira_sombra")

[node name="Sprite" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
position = Vector2(0, -95)
scale = Vector2(0.24, 0.24)
texture = ExtResource("25_caldeira")

[node name="LuzFornalha" type="PointLight2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
position = Vector2(0, -55)
color = Color(1, 0.58, 0.2, 1)
energy = 2.4
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.0

[node name="VaporCaldeira" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste" instance=ExtResource("43_vapor_valvula")]
position = Vector2(-25, -180)

[node name="PocaEscoria" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
z_index = -1
position = Vector2(-20, 25)
scale = Vector2(0.28, 0.28)
texture = ExtResource("41_poca_ferrugem")

[node name="TanqueDecantadorNorte" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(1150, 370)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
polygon = PackedVector2Array(-80, -10, 0, -25, 80, -10, 80, 25, 0, 35, -80, 25)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
modulate = Color(0, 0, 0, 0.5)
position = Vector2(0, 10)
scale = Vector2(0.24, 0.24)
texture = ExtResource("30_decantador_sombra")

[node name="Sprite" type="Sprite2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
position = Vector2(0, -80)
scale = Vector2(0.24, 0.24)
texture = ExtResource("29_decantador")

[node name="LuzVisorLimo" type="PointLight2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
position = Vector2(0, -70)
color = Color(0.25, 0.95, 0.45, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.5

[node name="PocaLimo" type="Sprite2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
z_index = -1
position = Vector2(0, 25)
scale = Vector2(0.28, 0.28)
texture = ExtResource("40_poca_limo")

[node name="VazamentoLimo" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte" instance=ExtResource("42_vazamento_gota")]
position = Vector2(0, 10)

[node name="TubosInterligacaoSul" type="Node2D" parent="RedeIndustrialMaquinas"]
z_index = -1

[node name="SuporteSul_1" type="Sprite2D" parent="RedeIndustrialMaquinas/TubosInterligacaoSul"]
position = Vector2(1000, 750)
scale = Vector2(0.1, 0.1)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaSul_1" type="Sprite2D" parent="RedeIndustrialMaquinas/TubosInterligacaoSul"]
position = Vector2(1250, 750)
scale = Vector2(0.11, 0.11)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteSul_2" type="Sprite2D" parent="RedeIndustrialMaquinas/TubosInterligacaoSul"]
position = Vector2(1500, 750)
scale = Vector2(0.1, 0.1)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaSul_2" type="Sprite2D" parent="RedeIndustrialMaquinas/TubosInterligacaoSul"]
position = Vector2(2050, 750)
scale = Vector2(0.11, 0.11)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteSul_3" type="Sprite2D" parent="RedeIndustrialMaquinas/TubosInterligacaoSul"]
position = Vector2(2350, 750)
scale = Vector2(0.1, 0.1)
texture = ExtResource("33_tubo_suporte")
"""

target = '[node name="LanternasMuralha" type="Node2D" parent="."]'
if target in content:
    content = content.replace(target, new_nodes.strip() + '\n\n' + target, 1)
    with open(tscn_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("fundo_ferro_master.tscn atualizado com sucesso!")
else:
    print("ERRO: target não encontrado!")
