import re

master_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(master_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add sub_resources
subres_target = '[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_e2"]\nsize = Vector2(410, 22)'
subres_replacement = '''[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_e2"]
size = Vector2(410, 22)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_e3"]
size = Vector2(210, 22)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_e4"]
size = Vector2(405, 22)'''

if subres_target in content:
    content = content.replace(subres_target, subres_replacement, 1)
    print("1. Added sub_resources pipe_block_e3 and pipe_block_e4")
else:
    print("WARNING: subres_target not found")

# 2. Add pipe segments to CanoLesteModular
pipe_target = '''[node name="CanoLeste_7" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3580, 643)
scale = Vector2(0.11, 0.11)
texture = ExtResource("50_cano_longo")'''

pipe_replacement = '''[node name="CanoLeste_7" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3580, 643)
scale = Vector2(0.11, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_8" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3710, 652)
scale = Vector2(0.11, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_8" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3710, 643)
scale = Vector2(0.11, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_9" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3840, 652)
scale = Vector2(0.11, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_9" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3840, 643)
scale = Vector2(0.11, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_10" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3970, 652)
scale = Vector2(0.11, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_10" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3970, 643)
scale = Vector2(0.11, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_11" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(4070, 652)
scale = Vector2(0.11, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_11" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(4070, 643)
scale = Vector2(0.11, 0.11)
texture = ExtResource("50_cano_longo")

[node name="TuboBocalArenaSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(4115, 650)
scale = Vector2(0.12, 0.12)
texture = ExtResource("53_cano_passagem_sombra")

[node name="TuboBocalArena" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(4115, 643)
scale = Vector2(0.12, 0.12)
texture = ExtResource("52_cano_passagem")'''

if pipe_target in content:
    content = content.replace(pipe_target, pipe_replacement, 1)
    print("2. Added pipe segments 8..11 and TuboBocalArena")
else:
    print("WARNING: pipe_target not found")

# 3. Add collision shapes
col_target = '''[node name="ColTubo_Leste2" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(3235, 642)
shape = SubResource("RectangleShape2D_pipe_block_e2")'''

col_replacement = '''[node name="ColTubo_Leste2" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(3235, 642)
shape = SubResource("RectangleShape2D_pipe_block_e2")

[node name="ColTubo_Leste3" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(3545, 642)
shape = SubResource("RectangleShape2D_pipe_block_e3")

[node name="ColTubo_Leste4" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(3912.5, 642)
shape = SubResource("RectangleShape2D_pipe_block_e4")'''

if col_target in content:
    content = content.replace(col_target, col_replacement, 1)
    print("3. Added ColTubo_Leste3 and ColTubo_Leste4")
else:
    print("WARNING: col_target not found")

# 4. Add PassarelaTravessiaCano_4
passarela_target = '''[node name="LanternaPassarela" type="Sprite2D" parent="PassarelaTravessiaCano_3"]
position = Vector2(38, -35)
scale = Vector2(0.45, 0.45)
texture = ExtResource("10_lantern")

[node name="LuzLanternaPassarela" type="PointLight2D" parent="PassarelaTravessiaCano_3/LanternaPassarela"]
color = Color(1, 0.74, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5'''

passarela_replacement = '''[node name="LanternaPassarela" type="Sprite2D" parent="PassarelaTravessiaCano_3"]
position = Vector2(38, -35)
scale = Vector2(0.45, 0.45)
texture = ExtResource("10_lantern")

[node name="LuzLanternaPassarela" type="PointLight2D" parent="PassarelaTravessiaCano_3/LanternaPassarela"]
color = Color(1, 0.74, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5

[node name="PassarelaTravessiaCano_4" type="Node2D" parent="."]
y_sort_enabled = true
position = Vector2(3680, 642)

[node name="SombraContato" type="Sprite2D" parent="PassarelaTravessiaCano_4"]
z_index = -3
position = Vector2(0, 8)
scale = Vector2(0.12, 0.12)
texture = ExtResource("67_passarela_sombra")

[node name="PassarelaSprite" type="Sprite2D" parent="PassarelaTravessiaCano_4"]
scale = Vector2(0.12, 0.12)
texture = ExtResource("66_passarela")

[node name="AreaElevacao" type="Area2D" parent="PassarelaTravessiaCano_4"]
script = ExtResource("68_passarela_script")

[node name="ShapeElevacao" type="CollisionShape2D" parent="PassarelaTravessiaCano_4/AreaElevacao"]
shape = SubResource("RectangleShape2D_passarela_area")

[node name="CorrimoesPilaresColisao" type="StaticBody2D" parent="PassarelaTravessiaCano_4"]

[node name="ColCorrimaoOeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_4/CorrimoesPilaresColisao"]
position = Vector2(-38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="ColCorrimaoLeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_4/CorrimoesPilaresColisao"]
position = Vector2(38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="LanternaPassarela" type="Sprite2D" parent="PassarelaTravessiaCano_4"]
position = Vector2(38, -35)
scale = Vector2(0.45, 0.45)
texture = ExtResource("10_lantern")

[node name="LuzLanternaPassarela" type="PointLight2D" parent="PassarelaTravessiaCano_4/LanternaPassarela"]
color = Color(1, 0.74, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5'''

if passarela_target in content:
    content = content.replace(passarela_target, passarela_replacement, 1)
    print("4. Added PassarelaTravessiaCano_4")
else:
    print("WARNING: passarela_target not found")

with open(master_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("fundo_ferro_master.tscn updated successfully!")
