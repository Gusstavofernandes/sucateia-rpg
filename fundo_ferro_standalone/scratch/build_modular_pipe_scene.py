import re

def update_master():
    scene_path = 'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn'
    with open(scene_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_exts = """[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_industrial.png" id="50_cano_longo"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_industrial_sombra.png" id="51_cano_longo_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_valvula.png" id="54_cano_valvula"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_valvula_sombra.png" id="55_cano_valvula_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_berco_apoio.png" id="56_cano_berco"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_berco_apoio_sombra.png" id="57_cano_berco_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_travessia_ponte.png" id="58_cano_ponte"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_travessia_ponte_sombra.png" id="59_cano_ponte_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/passagem_parede_flange.png" id="60_passagem_parede"]
[ext_resource type="Texture2D" path="res://assets/pipes/passagem_parede_flange_sombra.png" id="61_passagem_parede_sombra"]
"""

    for r_id in ["48_cano_reto", "49_cano_reto_sombra", "50_cano_horizontal", "51_cano_horizontal_sombra",
                 "50_cano_longo", "51_cano_longo_sombra",
                 "52_cano_cotovelo", "53_cano_cotovelo_sombra", "54_cano_valvula", "55_cano_valvula_sombra",
                 "56_cano_berco", "57_cano_berco_sombra", "58_cano_ponte", "59_cano_ponte_sombra",
                 "60_passagem_parede", "61_passagem_parede_sombra"]:
        content = re.sub(rf'\[ext_resource[^\]]*id="{r_id}"\]\r?\n?', '', content)

    target_token = '[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]'
    target_pos = content.find(target_token)
    content = content[:target_pos] + new_exts + "\n" + content[target_pos:]

    # Mover PilhaSucata_1 para fora da rota do cano (para Y=780, ao sul)
    content = re.sub(
        r'(\[node name="PilhaSucata_1"[^\]]*\]\s*position = Vector2\()2100,\s*718\)',
        r'\g<1>2080, 780)',
        content
    )

    # Ajustar posição da CaldeiraVaporLeste para Vector2(2650, 732)
    content = re.sub(
        r'(\[node name="CaldeiraVaporLeste"[^\]]*\]\s*y_sort_enabled = true\s*position = Vector2\()2650,\s*\d+\)',
        r'\g<1>2650, 732)',
        content
    )

    # Trecho Oeste: Bomba (1932, 642) -> Caldeira (2558, 642)
    # 4 segmentos longos contínuos de 156.8px (cobrindo 627px sem frestas)
    oeste_str = """[node name="CanoOesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="BercoApoioSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2088, 656)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -1
position = Vector2(2088, 648)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="CanoOesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2010, 649)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2010, 642)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoOesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2167, 649)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2167, 642)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="PonteTravessiaSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2200, 654)
scale = Vector2(0.15, 0.15)
texture = ExtResource("59_cano_ponte_sombra")

[node name="PonteTravessia" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = 1
position = Vector2(2200, 638)
scale = Vector2(0.15, 0.15)
texture = ExtResource("58_cano_ponte")

[node name="ValvulaRegistroSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2324, 641)
scale = Vector2(0.114, 0.11)
texture = ExtResource("55_cano_valvula_sombra")

[node name="ValvulaRegistro" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2324, 634)
scale = Vector2(0.114, 0.11)
texture = ExtResource("54_cano_valvula")

[node name="BercoApoioSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2450, 656)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -1
position = Vector2(2450, 648)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="CanoOesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2500, 649)
scale = Vector2(0.125, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2500, 642)
scale = Vector2(0.125, 0.11)
texture = ExtResource("50_cano_longo")
"""

    # Trecho Leste: Caldeira (2732, 622) -> Parede Leste (3440, 622)
    # 5 segmentos longos contínuos de 158px
    leste_str = """[node name="CanoLesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="CanoLesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2811, 629)
scale = Vector2(0.115, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(2811, 622)
scale = Vector2(0.115, 0.11)
texture = ExtResource("50_cano_longo")

[node name="BercoApoioSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2969, 636)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -1
position = Vector2(2969, 628)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="CanoLesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2969, 629)
scale = Vector2(0.115, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(2969, 622)
scale = Vector2(0.115, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3127, 629)
scale = Vector2(0.115, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3127, 622)
scale = Vector2(0.115, 0.11)
texture = ExtResource("50_cano_longo")

[node name="BercoApoioSombra_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3285, 636)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -1
position = Vector2(3285, 628)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="CanoLesteSombra_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3285, 629)
scale = Vector2(0.115, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3285, 622)
scale = Vector2(0.115, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3410, 629)
scale = Vector2(0.115, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3410, 622)
scale = Vector2(0.115, 0.11)
texture = ExtResource("50_cano_longo")

[node name="PassagemParedeLesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3440, 630)
scale = Vector2(0.09, 0.09)
texture = ExtResource("61_passagem_parede_sombra")

[node name="PassagemParedeLeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = 1
position = Vector2(3440, 622)
scale = Vector2(0.09, 0.09)
texture = ExtResource("60_passagem_parede")
"""

    novo_bloco = f"""[node name="RedeIndustrialMaquinas" type="Node2D" parent="."]
y_sort_enabled = true

[node name="DutoOesteSombra" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(120, 688, 665, 688)
width = 22.0
default_color = Color(0, 0, 0, 0.4)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoManifoldBombaSombra" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(835, 686, 1510, 686, 1568, 648)
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

{oeste_str}

[node name="CaldeiraVaporLeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(2650, 732)

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

{leste_str}

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

    pattern = r'\[node name="RedeIndustrialMaquinas" type="Node2D" parent="\."\].*?(?=\[node name="LanternasMuralha")'
    content = re.sub(pattern, novo_bloco, content, flags=re.DOTALL)

    ext_count = content.count('[ext_resource')
    sub_count = content.count('[sub_resource')
    total_steps = ext_count + sub_count + 1
    content = re.sub(r'load_steps=\d+', f'load_steps={total_steps}', content, count=1)

    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Sucesso! Tubulacao refeita com canos perfeitamente alinhados e sem vãos, load_steps={total_steps}")

if __name__ == '__main__':
    update_master()
