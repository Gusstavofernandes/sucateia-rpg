import os

tscn_path = 'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn'
with open(tscn_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace RedeIndustrialMaquinas block with an ultra-coherent, fully connected pipeline network
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '[node name="RedeIndustrialMaquinas"' in line:
        start_idx = i
    if start_idx != -1 and i > start_idx and '[node name="LanternasMuralha"' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    refined_network = """[node name="RedeIndustrialMaquinas" type="Node2D" parent="."]
y_sort_enabled = true

[node name="PocaOleoBomba" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -2
position = Vector2(1750, 755)
scale = Vector2(0.26, 0.26)
texture = ExtResource("39_poca_oleo")

[node name="VazamentoGotaBomba" parent="RedeIndustrialMaquinas" instance=ExtResource("42_vazamento_gota")]
position = Vector2(1610, 710)

[node name="TuboSuccaoCanal" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = 1
position = Vector2(1750, 520)
scale = Vector2(0.12, 0.12)
texture = ExtResource("37_tubo_vertical")

[node name="TuboSuccaoCanalSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboSuccaoCanal"]
modulate = Color(0, 0, 0, 0.45)
position = Vector2(0, 18)
texture = ExtResource("38_tubo_vertical_sombra")

[node name="CotoveloSuccaoCanal" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = 1
position = Vector2(1750, 570)
rotation = 3.14159
scale = Vector2(0.12, 0.12)
texture = ExtResource("35_tubo_cotovelo")

[node name="ManifoldOeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(750, 750)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
polygon = PackedVector2Array(-80, -10, 0, -25, 80, -10, 80, 25, 0, 35, -80, 25)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
modulate = Color(0, 0, 0, 0.5)
position = Vector2(0, 6)
scale = Vector2(0.24, 0.24)
texture = ExtResource("28_manifold_sombra")

[node name="Sprite" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
position = Vector2(0, -68)
scale = Vector2(0.24, 0.24)
texture = ExtResource("27_manifold")

[node name="PocaCondensado" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
z_index = -2
position = Vector2(0, 10)
scale = Vector2(0.24, 0.24)
texture = ExtResource("39_poca_oleo")

[node name="VaporManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("43_vapor_valvula")]
position = Vector2(15, -95)

[node name="VazamentoManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("42_vazamento_gota")]
position = Vector2(80, -35)

[node name="TuboEntradaManifold" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(675, 735)
rotation = 1.5708
scale = Vector2(0.11, 0.11)
texture = ExtResource("37_tubo_vertical")

[node name="CaldeiraVaporLeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(2650, 750)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
polygon = PackedVector2Array(-90, -15, 0, -30, 90, -15, 90, 30, 0, 45, -90, 30)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
modulate = Color(0, 0, 0, 0.5)
position = Vector2(0, 8)
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
z_index = -2
position = Vector2(-15, 12)
scale = Vector2(0.26, 0.26)
texture = ExtResource("41_poca_ferrugem")

[node name="TanqueDecantadorNorte" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(1150, 380)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
polygon = PackedVector2Array(-80, -10, 0, -25, 80, -10, 80, 25, 0, 35, -80, 25)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
modulate = Color(0, 0, 0, 0.5)
position = Vector2(0, 8)
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
z_index = -2
position = Vector2(0, 15)
scale = Vector2(0.26, 0.26)
texture = ExtResource("40_poca_limo")

[node name="VazamentoLimo" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte" instance=ExtResource("42_vazamento_gota")]
position = Vector2(0, -20)

[node name="LinhaVaporCaldeiraParaBomba" type="Node2D" parent="RedeIndustrialMaquinas"]
z_index = -1

[node name="ValvulaCaldeira" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaVaporCaldeiraParaBomba"]
position = Vector2(2550, 715)
scale = Vector2(0.11, 0.11)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteLeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaVaporCaldeiraParaBomba"]
position = Vector2(2350, 715)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaLeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaVaporCaldeiraParaBomba"]
position = Vector2(2150, 715)
scale = Vector2(0.11, 0.11)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteLeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaVaporCaldeiraParaBomba"]
position = Vector2(1950, 715)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

[node name="LinhaAguaBombaParaManifold" type="Node2D" parent="RedeIndustrialMaquinas"]
z_index = -1

[node name="SuporteOeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaAguaBombaParaManifold"]
position = Vector2(1500, 715)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaOeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaAguaBombaParaManifold"]
position = Vector2(1250, 715)
scale = Vector2(0.11, 0.11)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteOeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaAguaBombaParaManifold"]
position = Vector2(1000, 715)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

[node name="CotoveloEntradaManifold" type="Sprite2D" parent="RedeIndustrialMaquinas/LinhaAguaBombaParaManifold"]
position = Vector2(835, 715)
rotation = 3.14159
scale = Vector2(0.11, 0.11)
texture = ExtResource("35_tubo_cotovelo")
"""
    new_content = "".join(lines[:start_idx]) + refined_network.strip() + "\n\n" + "".join(lines[end_idx:])
    with open(tscn_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Refinamento de conexoes industriais aplicado com sucesso!")
else:
    print(f"Indices invalidos: start={start_idx}, end={end_idx}")
