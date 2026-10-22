import re

def update():
    with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
        content = f.read()

    # Localizar o bloco [node name="RedeIndustrialMaquinas" ... até [node name="LanternasMuralha"
    pattern = r'\[node name="RedeIndustrialMaquinas" type="Node2D" parent="\."\].*?(?=\[node name="LanternasMuralha")'

    novo_bloco = """[node name="RedeIndustrialMaquinas" type="Node2D" parent="."]
y_sort_enabled = true

[node name="DutoSulSombra_1" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(120, 688, 665, 688)
width = 22.0
default_color = Color(0, 0, 0, 0.4)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoSulSombra_2" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(835, 686, 1510, 686, 1568, 648)
width = 22.0
default_color = Color(0, 0, 0, 0.4)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoSulSombra_3" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(1932, 648, 1990, 689, 2520, 689, 2565, 716)
width = 22.0
default_color = Color(0, 0, 0, 0.4)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoSulSombra_4" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(2715, 693, 3500, 693)
width = 22.0
default_color = Color(0, 0, 0, 0.4)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoDecantadorSombra" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(1058, 345, 1030, 345, 1030, 488)
width = 18.0
default_color = Color(0, 0, 0, 0.4)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoParedeOesteManifold" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(120, 682, 665, 682)
width = 24.0
texture = ExtResource("47_tubo_duto")
texture_mode = 2
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoManifoldBomba" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(835, 680, 1510, 680, 1568, 642)
width = 24.0
texture = ExtResource("47_tubo_duto")
texture_mode = 2
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoBombaCaldeira" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(1932, 642, 1990, 683, 2520, 683, 2565, 710)
width = 24.0
texture = ExtResource("47_tubo_duto")
texture_mode = 2
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoCaldeiraParedeLeste" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(2715, 687, 3500, 687)
width = 24.0
texture = ExtResource("47_tubo_duto")
texture_mode = 2
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="FlangeParedeOeste" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(120, 682)
scale = Vector2(0.12, 0.12)
texture = ExtResource("37_tubo_vertical")

[node name="SuporteOeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(400, 682)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="SuporteSul_1" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(1060, 682)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaSul_1" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(1240, 680)
scale = Vector2(0.12, 0.12)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteSul_2" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(1420, 682)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="SuporteSul_3" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(2130, 685)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaSul_2" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(2290, 683)
scale = Vector2(0.12, 0.12)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteSul_4" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(2450, 685)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="SuporteSul_5" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(2860, 689)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="SuporteSul_6" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(3100, 689)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaSul_3" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(3250, 687)
scale = Vector2(0.12, 0.12)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteSul_7" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(3400, 689)
scale = Vector2(0.11, 0.11)
texture = ExtResource("33_tubo_suporte")

[node name="FlangeParedeLeste" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(3500, 687)
scale = Vector2(0.12, 0.12)
texture = ExtResource("37_tubo_vertical")

[node name="DutoEntradaDecantador" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(1153, 160, 1153, 209)
width = 20.0
texture = ExtResource("47_tubo_duto")
texture_mode = 2
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoSaidaDecantadorCanal" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(1058, 339, 1030, 339, 1030, 485)
width = 20.0
texture = ExtResource("47_tubo_duto")
texture_mode = 2
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="SuporteDecantador" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = -1
position = Vector2(1030, 410)
scale = Vector2(0.10, 0.10)
texture = ExtResource("33_tubo_suporte")

[node name="ManifoldOeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(750, 750)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
polygon = PackedVector2Array(-80, -10, 0, -25, 80, -10, 80, 25, 0, 35, -80, 25)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
modulate = Color(0, 0, 0, 0.45)
position = Vector2(0, 4)
scale = Vector2(0.24, 0.24)
texture = ExtResource("28_manifold_sombra")

[node name="Sprite" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
position = Vector2(0, -68)
scale = Vector2(0.24, 0.24)
texture = ExtResource("27_manifold")

[node name="VaporManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("43_vapor_valvula")]
position = Vector2(15, -95)

[node name="VazamentoManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("42_vazamento_gota")]
position = Vector2(40, -25)

[node name="TuboSuccaoCanal" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = 1
position = Vector2(1750, 520)
scale = Vector2(0.12, 0.12)
texture = ExtResource("37_tubo_vertical")

[node name="CotoveloSuccaoCanal" type="Sprite2D" parent="RedeIndustrialMaquinas"]
z_index = 1
position = Vector2(1750, 570)
rotation = 3.14159
scale = Vector2(0.12, 0.12)
texture = ExtResource("35_tubo_cotovelo")

[node name="VazamentoGotaBomba" parent="RedeIndustrialMaquinas" instance=ExtResource("42_vazamento_gota")]
position = Vector2(1610, 715)

[node name="CaldeiraVaporLeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(2650, 750)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
polygon = PackedVector2Array(-90, -15, 0, -30, 90, -15, 90, 30, 0, 45, -90, 30)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
modulate = Color(0, 0, 0, 0.45)
position = Vector2(0, 6)
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

[node name="VazamentoGotaCaldeira" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste" instance=ExtResource("42_vazamento_gota")]
position = Vector2(-85, -35)

[node name="TanqueDecantadorNorte" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(1150, 380)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
polygon = PackedVector2Array(-80, -10, 0, -25, 80, -10, 80, 25, 0, 35, -80, 25)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
modulate = Color(0, 0, 0, 0.45)
position = Vector2(0, 6)
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

[node name="VazamentoLimo" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte" instance=ExtResource("42_vazamento_gota")]
position = Vector2(0, -15)

"""

    content = re.sub(pattern, novo_bloco, content, flags=re.DOTALL)

    # Recalcular load_steps
    ext_count = content.count('[ext_resource')
    sub_count = content.count('[sub_resource')
    total_steps = ext_count + sub_count + 1
    content = re.sub(r'load_steps=\d+', f'load_steps={total_steps}', content, count=1)

    with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Sucesso! Conexão milimétrica da caldeira aplicada, load_steps={total_steps}")

if __name__ == '__main__':
    update()
