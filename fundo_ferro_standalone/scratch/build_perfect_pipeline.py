import re

tscn_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(tscn_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Assegurar que os ExtResources de boca_bocal_conexao estao no cabecalho
ext_bocal = '[ext_resource type="Texture2D" path="res://assets/pipes/boca_bocal_conexao.png" id="60_bocal_conexao"]\n[ext_resource type="Texture2D" path="res://assets/pipes/boca_bocal_conexao_sombra.png" id="61_bocal_conexao_sombra"]\n'

if '60_bocal_conexao' not in content:
    content = content.replace('[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_valvula.png" id="54_cano_valvula"]',
                            ext_bocal + '[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_valvula.png" id="54_cano_valvula"]')

# 2. Atualizar load_steps se necessario
m_steps = re.search(r'load_steps=(\d+)', content)
if m_steps:
    cur_steps = int(m_steps.group(1))
    content = content.replace(f'load_steps={cur_steps}', f'load_steps={cur_steps + 2}')

# 3. Bloco do CanoOesteModular
oeste_nodes = """[node name="CanoOesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="CanoOesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2010, 653)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2010, 646)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="BercoApoioSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2088, 660)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2088, 652)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="CanoOesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2167, 653)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2167, 646)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="PonteTravessiaSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2185, 658)
scale = Vector2(0.15, 0.15)
texture = ExtResource("59_cano_ponte_sombra")

[node name="PonteTravessia" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2185, 642)
scale = Vector2(0.15, 0.15)
texture = ExtResource("58_cano_ponte")

[node name="ValvulaRegistroSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2324, 645)
scale = Vector2(0.114, 0.11)
texture = ExtResource("55_cano_valvula_sombra")

[node name="ValvulaRegistro" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2324, 638)
scale = Vector2(0.114, 0.11)
texture = ExtResource("54_cano_valvula")

[node name="CanoOesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2481, 653)
scale = Vector2(0.114, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoOeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2481, 646)
scale = Vector2(0.114, 0.11)
texture = ExtResource("50_cano_longo")

[node name="BercoApoioSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2481, 660)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
position = Vector2(2481, 652)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="BocalConexaoOesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = -2
position = Vector2(2558, 653)
scale = Vector2(0.114, 0.11)
texture = ExtResource("61_bocal_conexao_sombra")

[node name="BocalConexaoOeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoOesteModular"]
z_index = 1
position = Vector2(2558, 646)
scale = Vector2(0.114, 0.11)
texture = ExtResource("60_bocal_conexao")"""

# 4. Bloco do CanoLesteModular
leste_nodes = """[node name="CanoLesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]
y_sort_enabled = true

[node name="BocalConexaoLesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2732, 625)
scale = Vector2(0.103, 0.11)
texture = ExtResource("61_bocal_conexao_sombra")

[node name="BocalConexaoLeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = 1
position = Vector2(2732, 618)
scale = Vector2(0.103, 0.11)
texture = ExtResource("60_bocal_conexao")

[node name="CanoLesteSombra_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2803, 625)
scale = Vector2(0.103, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_1" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(2803, 618)
scale = Vector2(0.103, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2945, 625)
scale = Vector2(0.103, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_2" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(2945, 618)
scale = Vector2(0.103, 0.11)
texture = ExtResource("50_cano_longo")

[node name="BercoApoioSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(2945, 632)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(2945, 624)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="CanoLesteSombra_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3087, 625)
scale = Vector2(0.103, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_3" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3087, 618)
scale = Vector2(0.103, 0.11)
texture = ExtResource("50_cano_longo")

[node name="CanoLesteSombra_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3229, 625)
scale = Vector2(0.103, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3229, 618)
scale = Vector2(0.103, 0.11)
texture = ExtResource("50_cano_longo")

[node name="BercoApoioSombra_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3229, 632)
scale = Vector2(0.08, 0.08)
texture = ExtResource("57_cano_berco_sombra")

[node name="BercoApoio_4" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3229, 624)
scale = Vector2(0.08, 0.08)
texture = ExtResource("56_cano_berco")

[node name="CanoLesteSombra_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3371, 625)
scale = Vector2(0.103, 0.11)
texture = ExtResource("51_cano_longo_sombra")

[node name="CanoLeste_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3371, 618)
scale = Vector2(0.103, 0.11)
texture = ExtResource("50_cano_longo")

[node name="PassagemParedeLesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
z_index = -2
position = Vector2(3440, 625)
scale = Vector2(0.09, 0.09)
texture = ExtResource("53_cano_passagem_sombra")

[node name="PassagemParedeLeste" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoLesteModular"]
position = Vector2(3440, 618)
scale = Vector2(0.09, 0.09)
texture = ExtResource("52_cano_passagem")"""

# Substituir CanoOesteModular existente
content = re.sub(r'\[node name="CanoOesteModular"[\s\S]*?(?=\[node name="CaldeiraVaporLeste"|\Z)', oeste_nodes + '\n\n', content)

# Substituir CanoLesteModular existente
content = re.sub(r'\[node name="CanoLesteModular"[\s\S]*?(?=\[node name="PassagemLeste"|\[node name="Player"|\Z)', leste_nodes + '\n\n', content)

with open(tscn_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("fundo_ferro_master.tscn atualizado com geometria milimétrica perfeita!")
