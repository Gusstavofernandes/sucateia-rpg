def apply_v4_updates():
    # 1. Atualizar ArenaColiseu.tscn
    arena_tscn = """[gd_scene load_steps=6 format=3 uid="uid://arena_coliseu_fundo_ferro_v1"]

[ext_resource type="Script" path="res://scripts/arena_coliseu.gd" id="1_arena_script"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_norte_v4.png" id="2_coliseu_norte"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_sul_v4.png" id="3_coliseu_sul"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_piso_v4.png" id="4_coliseu_piso"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_sombra_v4.png" id="5_coliseu_sombra"]

[node name="ArenaColiseu" type="Node2D"]
y_sort_enabled = true
script = ExtResource("1_arena_script")

[node name="PisoFosso" type="Node2D" parent="."]
z_index = -20

[node name="PisoFossoRebaixado" type="Sprite2D" parent="PisoFosso"]
position = Vector2(4380, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("4_coliseu_piso")

[node name="SombraFossoProfundo" type="Sprite2D" parent="PisoFosso"]
z_index = 2
position = Vector2(4380, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("5_coliseu_sombra")

[node name="ArquibancadaMeiaLuaNorte" type="Sprite2D" parent="."]
z_index = -15
position = Vector2(4380, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("2_coliseu_norte")

[node name="MuralhaSulArredondada" type="Sprite2D" parent="."]
z_index = 0
y_sort_enabled = true
position = Vector2(4380, 680)
scale = Vector2(0.68, 0.68)
texture = ExtResource("3_coliseu_sul")
"""
    dest_arena = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\ArenaColiseu.tscn',
        r'c:\Users\Usuario\Documents\jogo\scenes\ArenaColiseu.tscn'
    ]
    for p in dest_arena:
        with open(p, "w", encoding="utf-8") as f:
            f.write(arena_tscn)
            
    # 2. Atualizar fundo_ferro_master.tscn (expansão do chão e muralha de fundo contínua)
    master_paths = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn',
        r'c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn'
    ]
    for mp in master_paths:
        with open(mp, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Expansão do chão
        content = content.replace("offset_right = 4450.0\noffset_bottom = 1100.0", "offset_right = 5400.0\noffset_bottom = 1300.0")
        
        # Adicionar WallSegArena2 se ainda não existir
        if "WallSegArena2" not in content:
            target_str = """[node name="WallSegArena" type="Sprite2D" parent="MuralhaNorte"]
position = Vector2(3850, 140)
scale = Vector2(0.85, 0.85)
texture = ExtResource("3_fundo_wall")"""
            replacement_str = """[node name="WallSegArena" type="Sprite2D" parent="MuralhaNorte"]
position = Vector2(3850, 140)
scale = Vector2(0.85, 0.85)
texture = ExtResource("3_fundo_wall")

[node name="WallSegArena2" type="Sprite2D" parent="MuralhaNorte"]
position = Vector2(4680, 140)
scale = Vector2(0.85, 0.85)
texture = ExtResource("3_fundo_wall")"""
            content = content.replace(target_str, replacement_str)
            
        with open(mp, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Atualizações v4 aplicadas com sucesso!")

apply_v4_updates()
