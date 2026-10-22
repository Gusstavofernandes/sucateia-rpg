import re
import os

boiler_ext = """[ext_resource type="Texture2D" path="res://assets/reconstruction/forjas_boiler_hall.png" id="177_forjas_boiler_hall"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/forjas_boiler_hall_sombra.png" id="178_forjas_boiler_hall_sombra"]
"""

boiler_sub = """[sub_resource type="RectangleShape2D" id="RectangleShape2D_base_forjas_boiler_hall"]
size = Vector2(1150, 180)
"""

boiler_node = """
[node name="SalaCaldeiras_ForjasRasas" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(5450, 1480)
scale = Vector2(0.28, 0.28)

[node name="SombraContato" type="Sprite2D" parent="FeiraClandestinaFundoFerro/SalaCaldeiras_ForjasRasas"]
z_index = -3
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("178_forjas_boiler_hall_sombra")
offset = Vector2(0, -498)

[node name="Sprite" type="Sprite2D" parent="FeiraClandestinaFundoFerro/SalaCaldeiras_ForjasRasas"]
texture = ExtResource("177_forjas_boiler_hall")
offset = Vector2(0, -498)

[node name="LuzFornalhaCaldeira" type="PointLight2D" parent="FeiraClandestinaFundoFerro/SalaCaldeiras_ForjasRasas"]
position = Vector2(-150, -380)
color = Color(1, 0.45, 0.12, 1)
energy = 2.4
texture = SubResource("GradientTexture2D_light")
texture_scale = 6.5

[node name="ColisaoCaldeira" type="StaticBody2D" parent="FeiraClandestinaFundoFerro/SalaCaldeiras_ForjasRasas"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="FeiraClandestinaFundoFerro/SalaCaldeiras_ForjasRasas/ColisaoCaldeira"]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_base_forjas_boiler_hall")
"""

def refine_scene(file_path):
    print(f"Refinando {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inserir boiler ext_resources se não houver
    if '177_forjas_boiler_hall' not in content:
        m = list(re.finditer(r'\[ext_resource[^\]]+\]', content))
        last_ext_end = m[-1].end()
        content = content[:last_ext_end] + "\n" + boiler_ext + content[last_ext_end:]

    # 2. Inserir boiler sub_resource se não houver
    if 'RectangleShape2D_base_forjas_boiler_hall' not in content:
        m_node = re.search(r'\[node name="FundoFerroMaster"', content)
        node_start = m_node.start()
        content = content[:node_start] + boiler_sub + "\n" + content[node_start:]

    # 3. Inserir boiler node se não houver
    if 'SalaCaldeiras_ForjasRasas' not in content:
        m_arena = re.search(r'\[node name="ArenaColiseu"', content)
        arena_start = m_arena.start()
        content = content[:arena_start] + boiler_node + "\n" + content[arena_start:]

    # 4. Ajustar coordenadas e escalas
    # Reciclador: scale de 0.26 para 0.30, posição para Vector2(4500, 1260)
    content = re.sub(
        r'(\[node name="RecicladorPesado_Sucateia"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\)\nscale = Vector2\()[^)]+(\))',
        r'\g<1>4500, 1260\g<2>0.30, 0.30\3',
        content
    )

    # Pavilhão de câmbio: abaixar para Vector2(4340, 970)
    content = re.sub(
        r'(\[node name="PavilhaoCambio_AvaliacaoReliquias"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
        r'\g<1>4340, 970\2',
        content
    )

    # Cisterna: mover para Vector2(5950, 1120)
    content = re.sub(
        r'(\[node name="CisternaElevada_Residuos"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
        r'\g<1>5950, 1120\2',
        content
    )

    # Cantoneira: mover para Vector2(5980, 1420)
    content = re.sub(
        r'(\[node name="CantoneiraAlvenaria_Rompida"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
        r'\g<1>5980, 1420\2',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Sucesso refinando {file_path}!")

refine_scene(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn')
refine_scene(r'c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn')
