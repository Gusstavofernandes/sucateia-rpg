import os
import shutil

def aplicar_cena(tscn_path):
    print(f"Aplicando atualizações em: {tscn_path}")
    shutil.copy2(tscn_path, tscn_path + ".bak2")
    
    with open(tscn_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. ExtResources
    text = text.replace(
        'res://assets/machines/maquina_caldeira_vapor_v1.png',
        'res://assets/machines/maquina_caldeira_fornalha_v2.png'
    )
    text = text.replace(
        'res://assets/machines/maquina_caldeira_vapor_v1_sombra.png',
        'res://assets/machines/maquina_caldeira_fornalha_v2_sombra.png'
    )
    text = text.replace(
        'res://assets/pipes/passagem_parede_flange.png',
        'res://assets/pipes/tubo_bocal_parede_v2.png'
    )
    text = text.replace(
        'res://assets/pipes/passagem_parede_flange_sombra.png',
        'res://assets/pipes/tubo_bocal_parede_v2_sombra.png'
    )
    text = text.replace(
        'res://assets/pipes/boca_bocal_conexao.png',
        'res://assets/pipes/tubo_boca_encaixe_nova_v1.png'
    )
    text = text.replace(
        'res://assets/pipes/boca_bocal_conexao_sombra.png',
        'res://assets/pipes/tubo_boca_encaixe_nova_v1_sombra.png'
    )
    text = text.replace(
        'res://assets/pipes/cano_longo_valvula.png',
        'res://assets/pipes/cano_valvula_v2.png'
    )
    text = text.replace(
        'res://assets/pipes/cano_longo_valvula_sombra.png',
        'res://assets/pipes/cano_valvula_v2_sombra.png'
    )

    if 'cano_modular_cotovelo.png' not in text:
        ext_addition = """[ext_resource type="Texture2D" path="res://assets/pipes/cano_modular_cotovelo.png" id="62_cano_cotovelo"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_modular_cotovelo_sombra.png" id="63_cano_cotovelo_sombra"]
"""
        pos = text.find('[sub_resource type=')
        if pos != -1:
            text = text[:pos] + ext_addition + "\n" + text[pos:]

    # 2. Localizar RedeIndustrialMaquinas até Player
    start_marker = '[node name="RedeIndustrialMaquinas" type="Node2D" parent="."]'
    end_marker = '[node name="Player" type="CharacterBody2D" parent="."]'

    p_start = text.find(start_marker)
    p_end = text.find(end_marker)

    if p_start == -1 or p_end == -1:
        raise Exception(f"Marcadores não encontrados em {tscn_path}!")

    bloco_industrial = """[node name="RedeIndustrialMaquinas" type="Node2D" parent="."]
y_sort_enabled = true

[node name="DutoDecantadorSombra" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -3
points = PackedVector2Array(1058, 345, 1030, 345, 1030, 488)
width = 18.0
default_color = Color(0, 0, 0, 0.4)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

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

[node name="TuboParedeOesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="FlangeParedeOeste" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
position = Vector2(120, 680)
scale = Vector2(0.12, 0.12)
texture = ExtResource("37_tubo_vertical")

[node name="TuboParedeOesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
z_index = -2
position = Vector2(195, 687)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="TuboParedeOeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
position = Vector2(195, 680)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="TuboParedeOesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
z_index = -2
position = Vector2(345, 687)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="TuboParedeOeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
position = Vector2(345, 680)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="TuboParedeOesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
z_index = -2
position = Vector2(495, 687)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="TuboParedeOeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
position = Vector2(495, 680)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="TuboParedeOesteSombra_4" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
z_index = -2
position = Vector2(615, 687)
scale = Vector2(0.09, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="TuboParedeOeste_4" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]
position = Vector2(615, 680)
scale = Vector2(0.09, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoOesteManifoldBomba" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="CanoOesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(917, 687)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(917, 680)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoOesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(1067, 687)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(1067, 680)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="ValvulaSulSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(1189, 684)
scale = Vector2(0.11, 0.11)
texture = ExtResource("55_cano_valvula_sombra")

[node name="ValvulaSul" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(1189, 677)
scale = Vector2(0.11, 0.11)
texture = ExtResource("54_cano_valvula")

[node name="CanoOesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(1311, 687)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(1311, 680)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoOesteSombra_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(1401, 687)
scale = Vector2(0.08, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(1401, 680)
scale = Vector2(0.08, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CotoveloSubidaSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(1442, 672)
rotation = 3.14159
scale = Vector2(0.09, 0.09)
texture = ExtResource("63_cano_cotovelo_sombra")

[node name="CotoveloSubida_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(1442, 665)
rotation = 3.14159
scale = Vector2(0.09, 0.09)
texture = ExtResource("62_cano_cotovelo")

[node name="CotoveloSubidaSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(1470, 649)
scale = Vector2(0.09, 0.09)
texture = ExtResource("63_cano_cotovelo_sombra")

[node name="CotoveloSubida_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(1470, 642)
scale = Vector2(0.09, 0.09)
texture = ExtResource("62_cano_cotovelo")

[node name="BocaEncaixeBombaOesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
z_index = -2
position = Vector2(1507, 649)
scale = Vector2(0.115, 0.115)
texture = ExtResource("61_bocal_conexao_sombra")
flip_h = true

[node name="BocaEncaixeBombaOeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteManifoldBomba"]
position = Vector2(1507, 642)
scale = Vector2(0.115, 0.115)
texture = ExtResource("60_bocal_conexao")
flip_h = true

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

[node name="CanoBombaCaldeiraModular" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="BocaEncaixeBombaLesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
z_index = -2
position = Vector2(1993, 649)
scale = Vector2(0.115, 0.115)
texture = ExtResource("61_bocal_conexao_sombra")

[node name="BocaEncaixeBombaLeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
position = Vector2(1993, 642)
scale = Vector2(0.115, 0.115)
texture = ExtResource("60_bocal_conexao")

[node name="CanoBombaLesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
z_index = -2
position = Vector2(2140, 649)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoBombaLeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
position = Vector2(2140, 642)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="PonteTravessiaSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
z_index = -2
position = Vector2(2210, 656)
scale = Vector2(0.15, 0.15)
texture = ExtResource("59_cano_ponte_sombra")

[node name="PonteTravessia" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
z_index = 1
position = Vector2(2210, 642)
scale = Vector2(0.15, 0.15)
texture = ExtResource("58_cano_ponte")

[node name="ValvulaLesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
z_index = -2
position = Vector2(2305, 646)
scale = Vector2(0.11, 0.11)
texture = ExtResource("55_cano_valvula_sombra")

[node name="ValvulaLeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
position = Vector2(2305, 639)
scale = Vector2(0.11, 0.11)
texture = ExtResource("54_cano_valvula")

[node name="CanoBombaLesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
z_index = -2
position = Vector2(2427, 649)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoBombaLeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
position = Vector2(2427, 642)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoBombaLesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
z_index = -2
position = Vector2(2527, 649)
scale = Vector2(0.08, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoBombaLeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"]
position = Vector2(2527, 642)
scale = Vector2(0.08, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CaldeiraVaporLeste" type="StaticBody2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true
position = Vector2(2650, 732)

[node name="Col" type="CollisionPolygon2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
polygon = PackedVector2Array(-95, -20, 0, -35, 95, -20, 95, 30, 0, 48, -95, 30)

[node name="SombraContato" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
modulate = Color(0, 0, 0, 0.5)
position = Vector2(0, 15)
scale = Vector2(0.24, 0.24)
texture = ExtResource("26_caldeira_sombra")

[node name="Sprite" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
position = Vector2(0, -95)
scale = Vector2(0.24, 0.24)
texture = ExtResource("25_caldeira")

[node name="LuzFornalha" type="PointLight2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
position = Vector2(0, -65)
color = Color(1, 0.55, 0.18, 1)
energy = 2.5
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.0

[node name="VaporCaldeira" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste" instance=ExtResource("43_vapor_valvula")]
position = Vector2(0, -185)

[node name="CanoLesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="CanoLesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2810, 652)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(2810, 645)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2955, 652)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(2955, 645)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3100, 652)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3100, 645)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3245, 652)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3245, 645)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3350, 652)
scale = Vector2(0.09, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3350, 645)
scale = Vector2(0.09, 0.11)
texture = ExtResource("50_cano_longo")

[node name="PassagemParedeLesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3440, 650)
scale = Vector2(0.12, 0.12)
texture = ExtResource("53_cano_passagem_sombra")

[node name="PassagemParedeLeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3440, 643)
scale = Vector2(0.12, 0.12)
texture = ExtResource("52_cano_passagem")

"""

    text = text[:p_start] + bloco_industrial + "\n" + text[p_end:]

    with open(tscn_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Sucesso ao gravar {tscn_path}")

aplicar_cena('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn')
