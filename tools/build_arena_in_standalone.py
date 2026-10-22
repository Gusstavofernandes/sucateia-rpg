"""Injeta a sala da Arena do Coliseu e o túnel ortogonal na cena fundo_ferro_master.tscn do standalone."""
import shutil
import re
from pathlib import Path

tscn_path = Path("fundo_ferro_standalone/scenes/fundo_ferro_master.tscn")
bak_path = Path("fundo_ferro_standalone/scenes/fundo_ferro_master.tscn.bak_pre_arena")

if not bak_path.exists():
    shutil.copyfile(tscn_path, bak_path)
    print("Backup criado:", bak_path)

content = tscn_path.read_text(encoding="utf-8")

# 1. Atualizar load_steps
content = re.sub(r'load_steps=\d+', 'load_steps=165', content, count=1)

# 2. Inserir novos ExtResources antes de [sub_resource
new_ext_resources = """[ext_resource type="Texture2D" path="res://assets/machines/maquina_bomba_recalque_arena_v1.png" id="132_arena_bomba"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_bomba_recalque_arena_v1_sombra.png" id="133_arena_bomba_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/comporta_inundacao_arena_v1.png" id="134_arena_comporta"]
[ext_resource type="Texture2D" path="res://assets/props/comporta_inundacao_arena_v1_sombra.png" id="135_arena_comporta_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/portao_grade_arena_v1.png" id="136_arena_portao"]
[ext_resource type="Texture2D" path="res://assets/props/portao_grade_arena_v1_sombra.png" id="137_arena_portao_sombra"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_reator_eletrodo_arena_v1.png" id="138_arena_reator"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_reator_eletrodo_arena_v1_sombra.png" id="139_arena_reator_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_reto_industrial_v4.png" id="140_cano_reto_v4"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_reto_industrial_v4_sombra.png" id="141_cano_reto_v4_sombra"]
"""

if 'id="132_arena_bomba"' not in content:
    content = content.replace(
        '[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]',
        new_ext_resources + '\n[sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]'
    )

# 3. Inserir novas SubResources para colisões da Arena
new_sub_resources = """[sub_resource type="RectangleShape2D" id="RectangleShape2D_tunel_parede_oeste_novo"]
size = Vector2(28, 290)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_tunel_parede_leste_novo"]
size = Vector2(28, 140)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_tunel_parede_sul_novo"]
size = Vector2(170, 28)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_arena_parede_norte"]
size = Vector2(660, 40)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_arena_parede_sul"]
size = Vector2(660, 40)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_arena_parede_leste"]
size = Vector2(40, 540)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_arena_parede_oeste_norte"]
size = Vector2(40, 150)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_arena_parede_oeste_sul"]
size = Vector2(40, 290)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_bomba_arena"]
size = Vector2(190, 75)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_reator_arena"]
size = Vector2(165, 75)
"""

if 'id="RectangleShape2D_arena_parede_norte"' not in content:
    content = content.replace(
        '[node name="FundoFerroMaster" type="Node2D"]',
        new_sub_resources + '\n[node name="FundoFerroMaster" type="Node2D"]'
    )

# 4. Ajustar limites da câmera do Player
content = re.sub(r'limit_right = \d+', 'limit_right = 4400', content)
content = re.sub(r'limit_bottom = \d+', 'limit_bottom = 1500', content)

# 5. Adicionar a árvore de nós da Arena e do Túnel antes do nó [node name="Player"
arena_node_tree = """
[node name="ArenaColiseu" type="Node2D" parent="."]
y_sort_enabled = true

[node name="Pisos" type="Node2D" parent="ArenaColiseu"]
z_index = -20

[node name="PisoTunelSul" type="TextureRect" parent="ArenaColiseu/Pisos"]
texture_repeat = 2
offset_left = 3390.0
offset_top = 700.0
offset_right = 3570.0
offset_bottom = 980.0
texture = ExtResource("2_floor_atlas")
stretch_mode = 1

[node name="PisoTunelLeste" type="TextureRect" parent="ArenaColiseu/Pisos"]
texture_repeat = 2
offset_left = 3480.0
offset_top = 870.0
offset_right = 3620.0
offset_bottom = 1050.0
texture = ExtResource("2_floor_atlas")
stretch_mode = 1

[node name="PisoArenaPerimetro" type="TextureRect" parent="ArenaColiseu/Pisos"]
texture_repeat = 2
offset_left = 3580.0
offset_top = 840.0
offset_right = 4220.0
offset_bottom = 1360.0
texture = ExtResource("2_floor_atlas")
stretch_mode = 1

[node name="FossoCombate" type="Polygon2D" parent="ArenaColiseu/Pisos"]
z_index = -19
color = Color(0.24, 0.22, 0.20, 1.0)
polygon = PackedVector2Array(3708, 956, 4092, 956, 4092, 1244, 3708, 1244)

[node name="PocaEsgotoFosso" type="Sprite2D" parent="ArenaColiseu"]
z_index = -18
position = Vector2(3860, 1100)
scale = Vector2(0.38, 0.38)
texture = ExtResource("41_poca_ferrugem")

[node name="PocaOleoFosso" type="Sprite2D" parent="ArenaColiseu"]
z_index = -18
position = Vector2(3960, 1120)
scale = Vector2(0.32, 0.32)
texture = ExtResource("39_poca_oleo")

[node name="ColisoesEstruturais" type="StaticBody2D" parent="ArenaColiseu"]

[node name="ColTunelOeste" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(3376, 845)
shape = SubResource("RectangleShape2D_tunel_parede_oeste_novo")

[node name="ColTunelLeste" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(3584, 770)
shape = SubResource("RectangleShape2D_tunel_parede_leste_novo")

[node name="ColTunelSul" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(3475, 1064)
shape = SubResource("RectangleShape2D_tunel_parede_sul_novo")

[node name="ColArenaNorte" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(3900, 820)
shape = SubResource("RectangleShape2D_arena_parede_norte")

[node name="ColArenaSul" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(3900, 1380)
shape = SubResource("RectangleShape2D_arena_parede_sul")

[node name="ColArenaLeste" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(4240, 1100)
shape = SubResource("RectangleShape2D_arena_parede_leste")

[node name="ColArenaOesteNorte" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(3560, 895)
shape = SubResource("RectangleShape2D_arena_parede_oeste_norte")

[node name="ColArenaOesteSul" type="CollisionShape2D" parent="ArenaColiseu/ColisoesEstruturais"]
position = Vector2(3560, 1215)
shape = SubResource("RectangleShape2D_arena_parede_oeste_sul")

[node name="PortaoLevadicoArena" type="Node2D" parent="ArenaColiseu"]
position = Vector2(3580, 960)
scale = Vector2(0.24, 0.24)

[node name="SombraContato" type="Sprite2D" parent="ArenaColiseu/PortaoLevadicoArena"]
z_index = -3
position = Vector2(0, 15)
texture = ExtResource("137_arena_portao_sombra")
offset = Vector2(0, -60)

[node name="SpritePortao" type="Sprite2D" parent="ArenaColiseu/PortaoLevadicoArena"]
texture = ExtResource("136_arena_portao")
offset = Vector2(0, -60)

[node name="LuzLanternaEsquerda" type="PointLight2D" parent="ArenaColiseu/PortaoLevadicoArena"]
position = Vector2(-340, -40)
color = Color(1, 0.85, 0.55, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.0

[node name="LuzLanternaDireita" type="PointLight2D" parent="ArenaColiseu/PortaoLevadicoArena"]
position = Vector2(340, -40)
color = Color(1, 0.85, 0.55, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.0

[node name="ComportaInundacaoNorte" type="Node2D" parent="ArenaColiseu"]
position = Vector2(3900, 950)
scale = Vector2(0.24, 0.24)

[node name="SombraContato" type="Sprite2D" parent="ArenaColiseu/ComportaInundacaoNorte"]
z_index = -3
position = Vector2(0, 20)
texture = ExtResource("135_arena_comporta_sombra")
offset = Vector2(0, -60)

[node name="SpriteComporta" type="Sprite2D" parent="ArenaColiseu/ComportaInundacaoNorte"]
texture = ExtResource("134_arena_comporta")
offset = Vector2(0, -60)

[node name="VazamentoGota" parent="ArenaColiseu/ComportaInundacaoNorte" instance=ExtResource("42_vazamento_gota")]
position = Vector2(0, 50)

[node name="BombaRecalqueArena" type="Node2D" parent="ArenaColiseu"]
position = Vector2(3900, 1250)
scale = Vector2(0.20, 0.20)

[node name="SombraContato" type="Sprite2D" parent="ArenaColiseu/BombaRecalqueArena"]
z_index = -3
position = Vector2(0, 20)
scale = Vector2(1.0, 1.0)
texture = ExtResource("133_arena_bomba_sombra")
offset = Vector2(0, -75)

[node name="SpriteBomba" type="Sprite2D" parent="ArenaColiseu/BombaRecalqueArena"]
texture = ExtResource("132_arena_bomba")
offset = Vector2(0, -75)

[node name="ColisaoBaseBomba" type="StaticBody2D" parent="ArenaColiseu/BombaRecalqueArena"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="ArenaColiseu/BombaRecalqueArena/ColisaoBaseBomba"]
position = Vector2(0, -10)
shape = SubResource("RectangleShape2D_base_bomba_arena")

[node name="CanoHorizontalOeste" type="Sprite2D" parent="ArenaColiseu"]
z_index = -2
position = Vector2(3745, 1246)
scale = Vector2(0.14, 0.14)
texture = ExtResource("140_cano_reto_v4")

[node name="Sombra" type="Sprite2D" parent="ArenaColiseu/CanoHorizontalOeste"]
position = Vector2(0, 18)
texture = ExtResource("141_cano_reto_v4_sombra")

[node name="CanoHorizontalLeste" type="Sprite2D" parent="ArenaColiseu"]
z_index = -2
position = Vector2(4055, 1246)
scale = Vector2(0.14, 0.14)
texture = ExtResource("140_cano_reto_v4")

[node name="Sombra" type="Sprite2D" parent="ArenaColiseu/CanoHorizontalLeste"]
position = Vector2(0, 18)
texture = ExtResource("141_cano_reto_v4_sombra")

[node name="ReatorChoqueCiano" type="Node2D" parent="ArenaColiseu"]
position = Vector2(4120, 1060)
scale = Vector2(0.22, 0.22)

[node name="SombraContato" type="Sprite2D" parent="ArenaColiseu/ReatorChoqueCiano"]
z_index = -3
position = Vector2(0, 20)
texture = ExtResource("139_arena_reator_sombra")
offset = Vector2(0, -70)

[node name="SpriteReator" type="Sprite2D" parent="ArenaColiseu/ReatorChoqueCiano"]
texture = ExtResource("138_arena_reator")
offset = Vector2(0, -70)

[node name="LuzArcoCiano" type="PointLight2D" parent="ArenaColiseu/ReatorChoqueCiano"]
position = Vector2(0, -50)
color = Color(0.2, 0.88, 1.0, 1.0)
energy = 2.4
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.5

[node name="ColisaoBaseReator" type="StaticBody2D" parent="ArenaColiseu/ReatorChoqueCiano"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="ArenaColiseu/ReatorChoqueCiano/ColisaoBaseReator"]
position = Vector2(0, -10)
shape = SubResource("RectangleShape2D_base_reator_arena")

[node name="VaporReator" parent="ArenaColiseu/ReatorChoqueCiano" instance=ExtResource("43_vapor_valvula")]
position = Vector2(0, -170)
"""

if '[node name="ArenaColiseu"' not in content:
    content = content.replace(
        '[node name="Player" type="CharacterBody2D" parent="."]',
        arena_node_tree + '\n[node name="Player" type="CharacterBody2D" parent="."]'
    )

tscn_path.write_text(content, encoding="utf-8")
print("Arena e Túnel injetados com sucesso em fundo_ferro_master.tscn!")
