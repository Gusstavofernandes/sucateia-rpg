import re

def aplicar_correcao(scene_path):
    print(f"Aplicando correção de colisão e z-index em {scene_path}...")
    with open(scene_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Adicionar SubResources de colisão se não existirem
    sub_res_defs = """[sub_resource type="RectangleShape2D" id="RectangleShape2D_canal_oeste_extremo"]
size = Vector2(250, 75)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_canal_oeste_transicao"]
size = Vector2(110, 75)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_ponte_bloqueio_vao"]
size = Vector2(150, 85)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_ponte_bloqueio_corpo"]
size = Vector2(140, 160)
"""
    if 'RectangleShape2D_canal_oeste_extremo' not in text:
        idx = text.find('[node name="FundoFerroMaster"')
        text = text[:idx] + sub_res_defs + '\n' + text[idx:]

    # 2. Adicionar colisões de canal no setor oeste dentro de CanalDeEsgoto
    old_canal_pattern = r'(\[node name="ColisaoCanal_1" type="StaticBody2D" parent="CanalDeEsgoto"\])'
    new_canal_nodes = """[node name="ColisaoCanal_OesteExtremo" type="StaticBody2D" parent="CanalDeEsgoto"]
position = Vector2(-400, 525)

[node name="Col" type="CollisionShape2D" parent="CanalDeEsgoto/ColisaoCanal_OesteExtremo"]
shape = SubResource("RectangleShape2D_canal_oeste_extremo")

[node name="ColisaoCanal_OesteTransicao" type="StaticBody2D" parent="CanalDeEsgoto"]
position = Vector2(-25, 525)

[node name="Col" type="CollisionShape2D" parent="CanalDeEsgoto/ColisaoCanal_OesteTransicao"]
shape = SubResource("RectangleShape2D_canal_oeste_transicao")

[node name="ColisaoCanal_1" type="StaticBody2D" parent="CanalDeEsgoto"]"""
    
    if 'ColisaoCanal_OesteExtremo' not in text:
        text = re.sub(old_canal_pattern, new_canal_nodes, text, count=1)

    # 3. Atualizar CavaleteElevadoCanal:
    # - Adicionar colisão de bloqueio do vão do canal e do corpo da ponte
    # - Remover z_index = 1 de TrilhosSobreCavalete (para respeitar Y-sort e não desenhar sobre o player)
    old_cavalete_pattern = r'\[node name="CavaleteElevadoCanal" type="StaticBody2D" parent="RedeFerroviariaMina"\][\s\S]*?(?=\[node name="Player")'
    new_cavalete_block = """[node name="CavaleteElevadoCanal" type="StaticBody2D" parent="RedeFerroviariaMina"]
y_sort_enabled = true
position = Vector2(-188, 593.5)

[node name="ColBloqueioVaoCanal" type="CollisionShape2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
position = Vector2(0, -68.5)
shape = SubResource("RectangleShape2D_ponte_bloqueio_vao")

[node name="ColBloqueioCorpoPonte" type="CollisionShape2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
position = Vector2(0, 50)
shape = SubResource("RectangleShape2D_ponte_bloqueio_corpo")

[node name="ColPilarOeste" type="CollisionShape2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
position = Vector2(-95, 135)
shape = SubResource("RectangleShape2D_cavalete_pilar")

[node name="ColPilarLeste" type="CollisionShape2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
position = Vector2(95, 135)
shape = SubResource("RectangleShape2D_cavalete_pilar")

[node name="SombraContato" type="Sprite2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
z_index = -6
position = Vector2(0, 10)
scale = Vector2(0.40, 0.40)
texture = ExtResource("74_cavalete_alto_sombra")

[node name="CavaleteSprite" type="Sprite2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
scale = Vector2(0.40, 0.40)
texture = ExtResource("73_cavalete_alto")

[node name="TrilhosSobreCavalete" type="Sprite2D" parent="RedeFerroviariaMina/CavaleteElevadoCanal"]
position = Vector2(0, -93.75)
scale = Vector2(0.25, 0.25)
texture = ExtResource("75_trilho_vertical")

"""
    text = re.sub(old_cavalete_pattern, new_cavalete_block, text)

    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Sucesso: {scene_path}")

aplicar_correcao('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn')
aplicar_correcao('scenes/fundo_ferro_master.tscn')
