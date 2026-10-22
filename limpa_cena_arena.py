def update_clean_monumental_arena():
    # Nova cena ArenaColiseu.tscn sem os assets jogados em volta
    # Posição: Vector2(4350, 680), Escala: Vector2(0.68, 0.68)
    tscn_content = """[gd_scene load_steps=7 format=3 uid="uid://arena_coliseu_fundo_ferro_v1"]

[ext_resource type="Script" path="res://scripts/arena_coliseu.gd" id="1_arena_script"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_norte_v3.png" id="2_coliseu_norte"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_sul_v3.png" id="3_coliseu_sul"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_piso_v3.png" id="4_coliseu_piso"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_sombra_v3.png" id="5_coliseu_sombra"]

[sub_resource type="CapsuleShape2D" id="CapsuleShape2D_muralha_sul"]
radius = 45.0
height = 680.0

[node name="ArenaColiseu" type="Node2D"]
y_sort_enabled = true
script = ExtResource("1_arena_script")

[node name="PisoFosso" type="Node2D" parent="."]
z_index = -20

[node name="PisoFossoRebaixado" type="Sprite2D" parent="PisoFosso"]
position = Vector2(4350, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("4_coliseu_piso")

[node name="SombraFossoProfundo" type="Sprite2D" parent="PisoFosso"]
z_index = 2
position = Vector2(4350, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("5_coliseu_sombra")

[node name="ArquibancadaMeiaLuaNorte" type="Sprite2D" parent="."]
z_index = -15
position = Vector2(4350, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("2_coliseu_norte")

[node name="MuralhaSulArredondada" type="Sprite2D" parent="."]
z_index = 0
y_sort_enabled = true
position = Vector2(4350, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("3_coliseu_sul")
"""
    dest_files = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\ArenaColiseu.tscn',
        r'c:\Users\Usuario\Documents\jogo\scenes\ArenaColiseu.tscn'
    ]
    for df in dest_files:
        with open(df, "w", encoding="utf-8") as f:
            f.write(tscn_content)
    print("ArenaColiseu.tscn atualizada de forma limpa e monumental!")

update_clean_monumental_arena()
