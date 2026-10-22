import os
import re

SCENE_FILES = [
    r"c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn"
]

NEW_EXT_RESOURCES = """[ext_resource type="Texture2D" path="res://assets/pipes/ponte_travessia_unificada_arena.png" id="70_ponte_unificada"]
[ext_resource type="Texture2D" path="res://assets/pipes/ponte_travessia_unificada_arena_sombra.png" id="71_ponte_unificada_sombra"]
"""

NEW_SUB_RESOURCES = """[sub_resource type="RectangleShape2D" id="RectangleShape2D_ponte_arena_area"]
size = Vector2(76, 110)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_ponte_arena_railing"]
size = Vector2(18, 295)
"""

NEW_BRIDGE_NODE = """[node name="PonteTravessiaArena" type="Node2D" parent="."]
position = Vector2(3680, 565)

[node name="SombraContato" type="Sprite2D" parent="PonteTravessiaArena"]
z_index = -3
position = Vector2(0, 4)
scale = Vector2(0.25, 0.25)
texture = ExtResource("71_ponte_unificada_sombra")

[node name="PonteSprite" type="Sprite2D" parent="PonteTravessiaArena"]
z_index = -1
scale = Vector2(0.25, 0.25)
texture = ExtResource("70_ponte_unificada")

[node name="AreaElevacao" type="Area2D" parent="PonteTravessiaArena"]
position = Vector2(0, 77)
script = ExtResource("68_passarela_script")

[node name="ShapeElevacao" type="CollisionShape2D" parent="PonteTravessiaArena/AreaElevacao"]
shape = SubResource("RectangleShape2D_ponte_arena_area")

[node name="CorrimoesPilaresColisao" type="StaticBody2D" parent="PonteTravessiaArena"]

[node name="ColCorrimaoOeste" type="CollisionShape2D" parent="PonteTravessiaArena/CorrimoesPilaresColisao"]
position = Vector2(-54, -15)
shape = SubResource("RectangleShape2D_ponte_arena_railing")

[node name="ColCorrimaoLeste" type="CollisionShape2D" parent="PonteTravessiaArena/CorrimoesPilaresColisao"]
position = Vector2(54, -15)
shape = SubResource("RectangleShape2D_ponte_arena_railing")

[node name="LanternaPonte" type="Sprite2D" parent="PonteTravessiaArena"]
position = Vector2(54, -85)
scale = Vector2(0.6, 0.6)
texture = ExtResource("10_lantern")

[node name="LuzLanternaPonte" type="PointLight2D" parent="PonteTravessiaArena/LanternaPonte"]
color = Color(1, 0.74, 0.38, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.5
"""

for path in SCENE_FILES:
    if not os.path.exists(path):
        print(f"Arquivo não existe: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inserir ext_resources se não existirem
    if 'id="70_ponte_unificada"' not in content:
        # inserir logo antes do primeiro [sub_resource
        idx = content.find('[sub_resource')
        if idx != -1:
            content = content[:idx] + NEW_EXT_RESOURCES + '\n' + content[idx:]
        else:
            print("Erro ao encontrar ponto para ext_resources")

    # 2. Inserir sub_resources se não existirem
    if 'id="RectangleShape2D_ponte_arena_area"' not in content:
        idx = content.find('[node name="FundoFerro"')
        if idx == -1:
            idx = content.find('[node name="')
        if idx != -1:
            content = content[:idx] + NEW_SUB_RESOURCES + '\n' + content[idx:]

    # 3. Remover PonteServicoArena
    # Localizar bloco PonteServicoArena
    ponte_arena_start = content.find('[node name="PonteServicoArena"')
    if ponte_arena_start != -1:
        # vai até o próximo nó raiz (parent=".")
        next_root = content.find('\n[node name="PonteServico_1"', ponte_arena_start)
        if next_root != -1:
            content = content[:ponte_arena_start] + content[next_root+1:]
            print("Removido PonteServicoArena antigo.")

    # 4. Remover PassarelaTravessiaCano_4
    p4_start = content.find('[node name="PassarelaTravessiaCano_4"')
    if p4_start != -1:
        next_node = content.find('\n[node name="RedeFerroviariaMina"', p4_start)
        if next_node != -1:
            content = content[:p4_start] + NEW_BRIDGE_NODE + '\n' + content[next_node+1:]
            print("Substituído PassarelaTravessiaCano_4 por PonteTravessiaArena unificada.")
        else:
            print("Aviso: não encontrou RedeFerroviariaMina após PassarelaTravessiaCano_4")

    # 5. Ajustar CanoLesteModular para z_index = -2 para ficar atrás da ponte (-1)
    content = content.replace('[node name="CanoLesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]\nz_index = -1',
                              '[node name="CanoLesteModular" type="Node2D" parent="RedeIndustrialMaquinas"]\nz_index = -2')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cena atualizada com sucesso: {path}")

print("Concluído!")
