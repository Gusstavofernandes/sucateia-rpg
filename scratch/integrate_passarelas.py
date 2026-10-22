import os
import re

EXT_RESOURCES_BLOCK = """[ext_resource type="Texture2D" path="res://assets/pipes/passarela_travessia_completa_v1.png" id="66_passarela"]
[ext_resource type="Texture2D" path="res://assets/pipes/passarela_travessia_completa_v1_sombra.png" id="67_passarela_sombra"]
[ext_resource type="Script" path="res://scripts/passarela_cano.gd" id="68_passarela_script"]
"""

SUB_RESOURCES_BLOCK = """[sub_resource type="RectangleShape2D" id="RectangleShape2D_passarela_area"]
size = Vector2(60, 110)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_passarela_railing"]
size = Vector2(22, 100)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_w1"]
size = Vector2(850, 22)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_w2"]
size = Vector2(530, 22)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_c1"]
size = Vector2(240, 22)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_c2"]
size = Vector2(315, 22)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_e1"]
size = Vector2(225, 22)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_e2"]
size = Vector2(410, 22)
"""

NODES_BLOCK = """[node name="ColisaoTubulacaoIndustrial" type="StaticBody2D" parent="."]

[node name="ColTubo_Oeste1" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(545, 642)
shape = SubResource("RectangleShape2D_pipe_block_w1")

[node name="ColTubo_Oeste2" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(1295, 642)
shape = SubResource("RectangleShape2D_pipe_block_w2")

[node name="ColTubo_Centro1" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(2060, 642)
shape = SubResource("RectangleShape2D_pipe_block_c1")

[node name="ColTubo_Centro2" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(2397.5, 642)
shape = SubResource("RectangleShape2D_pipe_block_c2")

[node name="ColTubo_Leste1" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(2857.5, 642)
shape = SubResource("RectangleShape2D_pipe_block_e1")

[node name="ColTubo_Leste2" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"]
position = Vector2(3235, 642)
shape = SubResource("RectangleShape2D_pipe_block_e2")

[node name="PassarelaTravessiaCano_1" type="Node2D" parent="."]
y_sort_enabled = true
position = Vector2(1000, 642)

[node name="SombraContato" type="Sprite2D" parent="PassarelaTravessiaCano_1"]
z_index = -3
position = Vector2(0, 8)
scale = Vector2(0.12, 0.12)
texture = ExtResource("67_passarela_sombra")

[node name="PassarelaSprite" type="Sprite2D" parent="PassarelaTravessiaCano_1"]
scale = Vector2(0.12, 0.12)
texture = ExtResource("66_passarela")

[node name="AreaElevacao" type="Area2D" parent="PassarelaTravessiaCano_1"]
script = ExtResource("68_passarela_script")

[node name="ShapeElevacao" type="CollisionShape2D" parent="PassarelaTravessiaCano_1/AreaElevacao"]
shape = SubResource("RectangleShape2D_passarela_area")

[node name="CorrimoesPilaresColisao" type="StaticBody2D" parent="PassarelaTravessiaCano_1"]

[node name="ColCorrimaoOeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_1/CorrimoesPilaresColisao"]
position = Vector2(-38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="ColCorrimaoLeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_1/CorrimoesPilaresColisao"]
position = Vector2(38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="LanternaPassarela" type="Sprite2D" parent="PassarelaTravessiaCano_1"]
position = Vector2(38, -35)
scale = Vector2(0.45, 0.45)
texture = ExtResource("10_lantern")

[node name="LuzLanternaPassarela" type="PointLight2D" parent="PassarelaTravessiaCano_1/LanternaPassarela"]
color = Color(1, 0.74, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5

[node name="PassarelaTravessiaCano_2" type="Node2D" parent="."]
y_sort_enabled = true
position = Vector2(2210, 642)

[node name="SombraContato" type="Sprite2D" parent="PassarelaTravessiaCano_2"]
z_index = -3
position = Vector2(0, 8)
scale = Vector2(0.12, 0.12)
texture = ExtResource("67_passarela_sombra")

[node name="PassarelaSprite" type="Sprite2D" parent="PassarelaTravessiaCano_2"]
scale = Vector2(0.12, 0.12)
texture = ExtResource("66_passarela")

[node name="AreaElevacao" type="Area2D" parent="PassarelaTravessiaCano_2"]
script = ExtResource("68_passarela_script")

[node name="ShapeElevacao" type="CollisionShape2D" parent="PassarelaTravessiaCano_2/AreaElevacao"]
shape = SubResource("RectangleShape2D_passarela_area")

[node name="CorrimoesPilaresColisao" type="StaticBody2D" parent="PassarelaTravessiaCano_2"]

[node name="ColCorrimaoOeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_2/CorrimoesPilaresColisao"]
position = Vector2(-38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="ColCorrimaoLeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_2/CorrimoesPilaresColisao"]
position = Vector2(38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="LanternaPassarela" type="Sprite2D" parent="PassarelaTravessiaCano_2"]
position = Vector2(38, -35)
scale = Vector2(0.45, 0.45)
texture = ExtResource("10_lantern")

[node name="LuzLanternaPassarela" type="PointLight2D" parent="PassarelaTravessiaCano_2/LanternaPassarela"]
color = Color(1, 0.74, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5

[node name="PassarelaTravessiaCano_3" type="Node2D" parent="."]
y_sort_enabled = true
position = Vector2(3000, 642)

[node name="SombraContato" type="Sprite2D" parent="PassarelaTravessiaCano_3"]
z_index = -3
position = Vector2(0, 8)
scale = Vector2(0.12, 0.12)
texture = ExtResource("67_passarela_sombra")

[node name="PassarelaSprite" type="Sprite2D" parent="PassarelaTravessiaCano_3"]
scale = Vector2(0.12, 0.12)
texture = ExtResource("66_passarela")

[node name="AreaElevacao" type="Area2D" parent="PassarelaTravessiaCano_3"]
script = ExtResource("68_passarela_script")

[node name="ShapeElevacao" type="CollisionShape2D" parent="PassarelaTravessiaCano_3/AreaElevacao"]
shape = SubResource("RectangleShape2D_passarela_area")

[node name="CorrimoesPilaresColisao" type="StaticBody2D" parent="PassarelaTravessiaCano_3"]

[node name="ColCorrimaoOeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_3/CorrimoesPilaresColisao"]
position = Vector2(-38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="ColCorrimaoLeste" type="CollisionShape2D" parent="PassarelaTravessiaCano_3/CorrimoesPilaresColisao"]
position = Vector2(38, 0)
shape = SubResource("RectangleShape2D_passarela_railing")

[node name="LanternaPassarela" type="Sprite2D" parent="PassarelaTravessiaCano_3"]
position = Vector2(38, -35)
scale = Vector2(0.45, 0.45)
texture = ExtResource("10_lantern")

[node name="LuzLanternaPassarela" type="PointLight2D" parent="PassarelaTravessiaCano_3/LanternaPassarela"]
color = Color(1, 0.74, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5
"""

def update_scene(scene_path):
    print(f"Processando {scene_path}...")
    with open(scene_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Adicionar ext_resources se nao existirem
    if 'id="66_passarela"' not in content:
        # Encontra o ultimo ext_resource
        match = re.search(r'(\[ext_resource [^\]]+\]\n)(?=\n|\[sub_resource)', content)
        if match:
            # Encontra todos ext_resource
            last_ext = list(re.finditer(r'\[ext_resource [^\]]+\]\n', content))[-1]
            pos = last_ext.end()
            content = content[:pos] + EXT_RESOURCES_BLOCK + content[pos:]
            print("Ext resources adicionados.")

    # 2. Adicionar sub_resources se nao existirem
    if 'id="RectangleShape2D_passarela_area"' not in content:
        match = re.search(r'(\[node name="FundoFerroMaster")', content)
        if match:
            pos = match.start()
            content = content[:pos] + SUB_RESOURCES_BLOCK + "\n" + content[pos:]
            print("Sub resources adicionados.")

    # 3. Remover PonteTravessia antiga em 2210 se existir
    content = re.sub(
        r'\[node name="PonteTravessiaSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"\].*?texture = ExtResource\("59_cano_ponte_sombra"\)\n\n?',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'\[node name="PonteTravessia" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"\].*?texture = ExtResource\("58_cano_ponte"\)\n\n?',
        '',
        content,
        flags=re.DOTALL
    )

    # 4. Ajustar Z-index dos canos e cabos para z_index = -1 (e sombras para -3)
    # TuboParedeOeste, CanoOeste, CanoBombaLeste, CanoLeste, CaboOeste, CaboLeste
    # Ajustar cada Sprite2D de cano/cabo que nao seja sombra para ter z_index = -1
    def adjust_pipe_node(m):
        node_txt = m.group(0)
        name = m.group(1)
        if "Sombra" in name:
            # Sombra de cano/cabo: z_index = -3
            if "z_index = -2" in node_txt:
                node_txt = node_txt.replace("z_index = -2", "z_index = -3")
            elif "z_index" not in node_txt:
                node_txt = node_txt.replace(f'[node name="{name}" type="Sprite2D"', f'[node name="{name}" type="Sprite2D"\nz_index = -3')
        else:
            # Tubo ou cabo real: z_index = -1
            if "z_index = 1" in node_txt:
                pass # manter bocal/cotovelo de sucção especial se houver
            elif "z_index = -1" not in node_txt:
                # Inserir z_index = -1 logo apos a definicao do node
                node_txt = node_txt.replace(f'type="Sprite2D" parent="RedeIndustrialMaquinas', f'type="Sprite2D" parent="RedeIndustrialMaquinas')
                # Adicionar z_index = -1 antes de position
                node_txt = re.sub(r'(\nposition = Vector2)', r'\nz_index = -1\1', node_txt)
        return node_txt

    # Aplicar nos subnós da RedeIndustrialMaquinas
    # 5. Adicionar nós das passarelas e colisão antes de [node name="Player"
    if '[node name="PassarelaTravessiaCano_1"' not in content:
        player_match = re.search(r'(\[node name="Player" type="CharacterBody2D")', content)
        if player_match:
            pos = player_match.start()
            content = content[:pos] + NODES_BLOCK + "\n" + content[pos:]
            print("Nós de colisão e passarelas inseridos antes do Player.")

    with open(scene_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Salvo {scene_path} com sucesso.")

if __name__ == "__main__":
    update_scene(r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn")
    update_scene(r"c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn")
