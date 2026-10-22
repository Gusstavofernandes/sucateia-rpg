import re
import os

ext_resources_text = """[ext_resource type="Texture2D" path="res://assets/reconstruction/forjas_recycler.png" id="157_forjas_recycler"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/forjas_recycler_sombra.png" id="158_forjas_recycler_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/cloth_stall.png" id="159_cloth_stall"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/cloth_stall_sombra.png" id="160_cloth_stall_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/market_salvage_cart.png" id="161_market_salvage_cart"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/market_salvage_cart_sombra.png" id="162_market_salvage_cart_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/exchange_pavilion.png" id="163_exchange_pavilion"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/exchange_pavilion_sombra.png" id="164_exchange_pavilion_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/forjas_workshop.png" id="165_forjas_workshop"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/forjas_workshop_sombra.png" id="166_forjas_workshop_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/wholesale_arcade.png" id="167_wholesale_arcade"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/wholesale_arcade_sombra.png" id="168_wholesale_arcade_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_sorting_bank.png" id="169_fundo_sorting_bank"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_sorting_bank_sombra.png" id="170_fundo_sorting_bank_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_abandoned_engine.png" id="171_fundo_abandoned_engine"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_abandoned_engine_sombra.png" id="172_fundo_abandoned_engine_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_collapsed_corner.png" id="173_fundo_collapsed_corner"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_collapsed_corner_sombra.png" id="174_fundo_collapsed_corner_sombra"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/alto_cistern.png" id="175_alto_cistern"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/alto_cistern_sombra.png" id="176_alto_cistern_sombra"]
"""

sub_resources_text = """[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_forjas_recycler"]
size = Vector2(1150, 180)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_cloth_stall"]
size = Vector2(1100, 180)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_market_salvage_cart"]
size = Vector2(850, 220)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_exchange_pavilion"]
size = Vector2(1150, 180)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_forjas_workshop"]
size = Vector2(1050, 190)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_wholesale_arcade"]
size = Vector2(1150, 180)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_fundo_sorting_bank"]
size = Vector2(1500, 140)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_fundo_abandoned_engine"]
size = Vector2(1100, 180)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_fundo_collapsed_corner"]
size = Vector2(1250, 170)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_alto_cistern"]
size = Vector2(950, 210)
"""

nodes_text = """
[node name="BarracaPanosRoupas_Clandestina" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3580, 1080)
scale = Vector2(0.26, 0.26)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaPanosRoupas_Clandestina"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("160_cloth_stall_sombra")
offset = Vector2(0, -470)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BarracaPanosRoupas_Clandestina"]
texture = ExtResource("159_cloth_stall")
offset = Vector2(0, -470)

[node name="LuzLanternaTecidos" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaPanosRoupas_Clandestina"]
position = Vector2(-60, -300)
color = Color(1, 0.82, 0.45, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.0

[node name="ColisaoBarraca" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/BarracaPanosRoupas_Clandestina"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/BarracaPanosRoupas_Clandestina/ColisaoBarraca"]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_base_cloth_stall")


[node name="CarrocaoSucateiro_Ambulante" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(4180, 1060)
scale = Vector2(0.22, 0.22)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/CarrocaoSucateiro_Ambulante"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("162_market_salvage_cart_sombra")
offset = Vector2(0, -643)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/CarrocaoSucateiro_Ambulante"]
texture = ExtResource("161_market_salvage_cart")
offset = Vector2(0, -643)

[node name="LuzLanternaCarrocao" type="PointLight2D" parent="FeiraClandestinaFundoFerro/CarrocaoSucateiro_Ambulante"]
position = Vector2(40, -420)
color = Color(1, 0.70, 0.28, 1)
energy = 1.4
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.0

[node name="ColisaoCarrocao" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/CarrocaoSucateiro_Ambulante"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/CarrocaoSucateiro_Ambulante/ColisaoCarrocao"]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_base_market_salvage_cart")


[node name="PavilhaoCambio_AvaliacaoReliquias" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(4380, 920)
scale = Vector2(0.27, 0.27)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/PavilhaoCambio_AvaliacaoReliquias"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("164_exchange_pavilion_sombra")
offset = Vector2(0, -478)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/PavilhaoCambio_AvaliacaoReliquias"]
texture = ExtResource("163_exchange_pavilion")
offset = Vector2(0, -478)

[node name="LuzDouradaCambio" type="PointLight2D" parent="FeiraClandestinaFundoFerro/PavilhaoCambio_AvaliacaoReliquias"]
position = Vector2(0, -350)
color = Color(1, 0.82, 0.35, 1)
energy = 2.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 6.0

[node name="ColisaoPavilhao" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/PavilhaoCambio_AvaliacaoReliquias"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/PavilhaoCambio_AvaliacaoReliquias/ColisaoPavilhao"]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_base_exchange_pavilion")


[node name="RecicladorPesado_Sucateia" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(4520, 1260)
scale = Vector2(0.26, 0.26)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/RecicladorPesado_Sucateia"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("158_forjas_recycler_sombra")
offset = Vector2(0, -492)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/RecicladorPesado_Sucateia"]
texture = ExtResource("157_forjas_recycler")
offset = Vector2(0, -492)

[node name="LuzFornalhaReciclador" type="PointLight2D" parent="FeiraClandestinaFundoFerro/RecicladorPesado_Sucateia"]
position = Vector2(-350, -600)
color = Color(1, 0.65, 0.25, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.5

[node name="LuzBobinaCiano" type="PointLight2D" parent="FeiraClandestinaFundoFerro/RecicladorPesado_Sucateia"]
position = Vector2(260, -620)
color = Color(0.2, 0.85, 1.0, 1)
energy = 2.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.0

[node name="ColisaoReciclador" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/RecicladorPesado_Sucateia"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/RecicladorPesado_Sucateia/ColisaoReciclador"]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_base_forjas_recycler")


[node name="OficinaArmeiros_Gladiadores" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(4950, 1380)
scale = Vector2(0.27, 0.27)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/OficinaArmeiros_Gladiadores"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("166_forjas_workshop_sombra")
offset = Vector2(0, -545)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/OficinaArmeiros_Gladiadores"]
texture = ExtResource("165_forjas_workshop")
offset = Vector2(0, -545)

[node name="LuzForjaArmeiro" type="PointLight2D" parent="FeiraClandestinaFundoFerro/OficinaArmeiros_Gladiadores"]
position = Vector2(-80, -320)
color = Color(1, 0.48, 0.15, 1)
energy = 2.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 6.5

[node name="ColisaoOficina" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/OficinaArmeiros_Gladiadores"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/OficinaArmeiros_Gladiadores/ColisaoOficina"]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_base_forjas_workshop")


[node name="ArcadaAtacadista_MercadoRestos" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3850, 1480)
scale = Vector2(0.28, 0.28)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/ArcadaAtacadista_MercadoRestos"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("168_wholesale_arcade_sombra")
offset = Vector2(0, -496)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/ArcadaAtacadista_MercadoRestos"]
texture = ExtResource("167_wholesale_arcade")
offset = Vector2(0, -496)

[node name="LuzLanternaEsquerda" type="PointLight2D" parent="FeiraClandestinaFundoFerro/ArcadaAtacadista_MercadoRestos"]
position = Vector2(-280, -360)
color = Color(0.98, 0.72, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.0

[node name="LuzLanternaDireita" type="PointLight2D" parent="FeiraClandestinaFundoFerro/ArcadaAtacadista_MercadoRestos"]
position = Vector2(280, -360)
color = Color(0.98, 0.72, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.0

[node name="ColisaoArcada" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/ArcadaAtacadista_MercadoRestos"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/ArcadaAtacadista_MercadoRestos/ColisaoArcada"]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_base_wholesale_arcade")


[node name="BancadaTriagem_Metais" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3350, 1420)
scale = Vector2(0.26, 0.26)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BancadaTriagem_Metais"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("170_fundo_sorting_bank_sombra")
offset = Vector2(0, -385)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/BancadaTriagem_Metais"]
texture = ExtResource("169_fundo_sorting_bank")
offset = Vector2(0, -385)

[node name="LuzLamparinaTriagem" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BancadaTriagem_Metais"]
position = Vector2(0, -220)
color = Color(0.92, 0.78, 0.45, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.5

[node name="ColisaoBancada" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/BancadaTriagem_Metais"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/BancadaTriagem_Metais/ColisaoBancada"]
position = Vector2(0, -20)
shape = SubResource("RectangleShape2D_base_fundo_sorting_bank")


[node name="MotorSubterraneo_Ancestral" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(5480, 1220)
scale = Vector2(0.28, 0.28)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/MotorSubterraneo_Ancestral"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("172_fundo_abandoned_engine_sombra")
offset = Vector2(0, -496)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/MotorSubterraneo_Ancestral"]
texture = ExtResource("171_fundo_abandoned_engine")
offset = Vector2(0, -496)

[node name="LuzVaporToxico" type="PointLight2D" parent="FeiraClandestinaFundoFerro/MotorSubterraneo_Ancestral"]
position = Vector2(120, -380)
color = Color(0.25, 0.95, 0.45, 1)
energy = 2.0
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.5

[node name="ColisaoMotor" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/MotorSubterraneo_Ancestral"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/MotorSubterraneo_Ancestral/ColisaoMotor"]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_base_fundo_abandoned_engine")


[node name="CantoneiraAlvenaria_Rompida" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(5820, 1400)
scale = Vector2(0.28, 0.28)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/CantoneiraAlvenaria_Rompida"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("174_fundo_collapsed_corner_sombra")
offset = Vector2(0, -463)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/CantoneiraAlvenaria_Rompida"]
texture = ExtResource("173_fundo_collapsed_corner")
offset = Vector2(0, -463)

[node name="ColisaoCantoneira" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/CantoneiraAlvenaria_Rompida"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/CantoneiraAlvenaria_Rompida/ColisaoCantoneira"]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_base_fundo_collapsed_corner")


[node name="CisternaElevada_Residuos" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(5520, 940)
scale = Vector2(0.24, 0.24)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/CisternaElevada_Residuos"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("176_alto_cistern_sombra")
offset = Vector2(0, -599)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/CisternaElevada_Residuos"]
texture = ExtResource("175_alto_cistern")
offset = Vector2(0, -599)

[node name="LuzCisternaResiduos" type="PointLight2D" parent="FeiraClandestinaFundoFerro/CisternaElevada_Residuos"]
position = Vector2(-30, -450)
color = Color(0.95, 0.60, 0.18, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.5

[node name="ColisaoCisterna" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/CisternaElevada_Residuos"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/CisternaElevada_Residuos/ColisaoCisterna"]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_base_alto_cistern")
"""

def update_scene_file(file_path):
    print(f"Atualizando {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Inserir ext_resources antes do primeiro [sub_resource
    # Localizar último ext_resource
    m = list(re.finditer(r'\[ext_resource[^\]]+\]', content))
    if not m:
        print("Erro: ext_resource não encontrado")
        return
    last_ext_end = m[-1].end()
    
    # Verificar se já foram adicionados
    if '157_forjas_recycler' not in content:
        content = content[:last_ext_end] + "\n" + ext_resources_text + content[last_ext_end:]
    
    # 2. Inserir sub_resources antes de [node name="FundoFerroMaster"
    m_node = re.search(r'\[node name="FundoFerroMaster"', content)
    if not m_node:
        print("Erro: node FundoFerroMaster não encontrado")
        return
    node_start = m_node.start()
    if 'RectangleShape2D_base_forjas_recycler' not in content:
        content = content[:node_start] + sub_resources_text + "\n" + content[node_start:]
        
    # 3. Inserir novos nós dentro de FeiraClandestinaFundoFerro, antes de [node name="ArenaColiseu"
    m_arena = re.search(r'\[node name="ArenaColiseu" parent="\." instance=ExtResource\("148_arena_coliseu_scene"\)\]', content)
    if not m_arena:
        print("Erro: node ArenaColiseu não encontrado")
        return
    arena_start = m_arena.start()
    if 'RecicladorPesado_Sucateia' not in content:
        content = content[:arena_start] + nodes_text + "\n" + content[arena_start:]
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Sucesso ao atualizar {file_path}!")

update_scene_file(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn')
update_scene_file(r'c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn')
