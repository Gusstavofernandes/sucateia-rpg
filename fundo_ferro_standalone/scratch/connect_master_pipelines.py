import os

tscn_path = 'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn'
with open(tscn_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ensure new pipe textures are declared in ext_resource
if 'id="44_tubo_reto"' not in content:
    ext_decl = """[ext_resource type="Texture2D" path="res://assets/pipes/tubo_segmento_reto.png" id="44_tubo_reto"]
[ext_resource type="Texture2D" path="res://assets/pipes/tubo_segmento_reto_sombra.png" id="45_tubo_reto_sombra"]
[ext_resource type="Texture2D" path="res://assets/fx/vapor_particula.png" id="46_vapor_puff"]
"""
    content = content.replace('[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]', ext_decl + '\n[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]', 1)

# 2. Update VaporBomba in EstacaoBombeamento to use vapor_particula texture
old_vapor_bomba = """[node name="VaporBomba" type="CPUParticles2D" parent="EstacaoBombeamento"]
position = Vector2(80, -220)
amount = 22
lifetime = 1.8
direction = Vector2(0, -1)
spread = 15.0
gravity = Vector2(12, -25)
initial_velocity_min = 25.0
initial_velocity_max = 50.0
scale_amount_min = 5.0
scale_amount_max = 12.0
color = Color(0.85, 0.88, 0.9, 0.38)"""

new_vapor_bomba = """[node name="VaporBomba" type="CPUParticles2D" parent="EstacaoBombeamento"]
position = Vector2(80, -220)
amount = 14
lifetime = 1.6
preprocess = 0.5
texture = ExtResource("46_vapor_puff")
direction = Vector2(0, -1)
spread = 18.0
gravity = Vector2(10, -22)
initial_velocity_min = 20.0
initial_velocity_max = 40.0
damping_min = 4.0
damping_max = 8.0
scale_amount_min = 0.3
scale_amount_max = 0.75
color = Color(0.88, 0.90, 0.92, 0.35)"""

if old_vapor_bomba in content:
    content = content.replace(old_vapor_bomba, new_vapor_bomba, 1)

# 3. Remove TampaInspecao nodes from DecalquesChao
for i in [1, 2, 3]:
    old_hatch = f"""[node name="TampaInspecao_{i}" type="Sprite2D" parent="DecalquesChao"]
position = Vector2("""
    if old_hatch in content:
        # Find start and end of this node block
        s_pos = content.find(f'[node name="TampaInspecao_{i}"')
        next_node = content.find('[node name=', s_pos + 10)
        if s_pos != -1 and next_node != -1:
            content = content[:s_pos] + content[next_node:]

# 4. Replace RedeIndustrialMaquinas with fully connected continuous pipelines
s_idx = content.find('[node name="RedeIndustrialMaquinas"')
e_idx = content.find('[node name="LanternasMuralha"', s_idx)

if s_idx != -1 and e_idx != -1:
    refined_network = """[node name="RedeIndustrialMaquinas" type="Node2D" parent="."]
y_sort_enabled = true

# =========================================================================
# 1. CANAIS E TUBULAÇÕES CONTÍNUAS DO PASSEIO SUL (Conexão 100% ininterrupta)
# =========================================================================
[node name="DutoPressaoManifoldBomba" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(830, 718, 1610, 718)
width = 14.0
default_color = Color(0.18, 0.20, 0.19, 1)
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoPressaoManifoldBombaTracer" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(830, 718, 1610, 718)
width = 4.0
default_color = Color(0.42, 0.50, 0.46, 1)

[node name="DutoVaporBombaCaldeira" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(1890, 718, 2565, 718)
width = 16.0
default_color = Color(0.20, 0.18, 0.16, 1)
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoVaporBombaCaldeiraTracer" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(1890, 718, 2565, 718)
width = 5.0
default_color = Color(0.65, 0.48, 0.30, 1)

[node name="DutoCaldeiraParede" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(2735, 718, 2820, 718, 2820, 790)
width = 14.0
default_color = Color(0.20, 0.18, 0.16, 1)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoManifoldCanal" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(675, 718, 560, 718, 560, 610)
width = 14.0
default_color = Color(0.18, 0.20, 0.19, 1)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

# =========================================================================
# 2. TUBULAÇÃO DO PASSEIO NORTE (Tanque Decantador conectado ao Bueiro 2 e Canal)
# =========================================================================
[node name="DutoEntradaDecantador" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(1550, 260, 1150, 260, 1150, 310)
width = 12.0
default_color = Color(0.16, 0.19, 0.17, 1)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

[node name="DutoSaidaDecantadorCanal" type="Line2D" parent="RedeIndustrialMaquinas"]
z_index = -1
points = PackedVector2Array(1220, 380, 1260, 380, 1260, 485)
width = 12.0
default_color = Color(0.16, 0.19, 0.17, 1)
joint_mode = 2
begin_cap_mode = 2
end_cap_mode = 2

# Suportes e conexões ao longo do duto sul
[node name="SuporteSul_1" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(1000, 718)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaSul_1" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(1200, 718)
scale = Vector2(0.11, 0.11)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteSul_2" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(1420, 718)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

[node name="SuporteSul_3" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(2120, 718)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

[node name="ValvulaSul_2" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(2280, 718)
scale = Vector2(0.11, 0.11)
texture = ExtResource("31_tubo_valvula")

[node name="SuporteSul_4" type="Sprite2D" parent="RedeIndustrialMaquinas"]
position = Vector2(2450, 718)
scale = Vector2(0.09, 0.09)
texture = ExtResource("33_tubo_suporte")

# =========================================================================
# 3. MÁQUINAS INDUSTRIAIS COM SOMBRAS DE CONTATO SUAVES
# =========================================================================
# A) Manifold Oeste
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

[node name="PocaCondensado" type="Sprite2D" parent="RedeIndustrialMaquinas/ManifoldOeste"]
z_index = -2
position = Vector2(20, 15)
scale = Vector2(0.22, 0.22)
texture = ExtResource("39_poca_oleo")

[node name="VaporManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("43_vapor_valvula")]
position = Vector2(15, -95)

[node name="VazamentoManifold" parent="RedeIndustrialMaquinas/ManifoldOeste" instance=ExtResource("42_vazamento_gota")]
position = Vector2(40, -25)

# B) Estação de Bombeamento - Sucção do Canal
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

# C) Caldeira de Vapor Leste
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

[node name="PocaCondensadoQuente" type="Sprite2D" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste"]
z_index = -2
position = Vector2(-15, 14)
scale = Vector2(0.26, 0.26)
texture = ExtResource("41_poca_ferrugem")

[node name="VazamentoGotaCaldeira" parent="RedeIndustrialMaquinas/CaldeiraVaporLeste" instance=ExtResource("42_vazamento_gota")]
position = Vector2(-85, -35)

# D) Tanque Decantador Norte
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

[node name="PocaLimo" type="Sprite2D" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte"]
z_index = -2
position = Vector2(0, 15)
scale = Vector2(0.26, 0.26)
texture = ExtResource("40_poca_limo")

[node name="VazamentoLimo" parent="RedeIndustrialMaquinas/TanqueDecantadorNorte" instance=ExtResource("42_vazamento_gota")]
position = Vector2(0, -15)
"""
    content = content[:s_idx] + refined_network.strip() + "\n\n" + content[e_idx:]
    with open(tscn_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("fundo_ferro_master.tscn atualizado com linhas contínuas e sem pontas soltas!")
else:
    print(f"Erro: indices invalidos s_idx={s_idx}, e_idx={e_idx}")
