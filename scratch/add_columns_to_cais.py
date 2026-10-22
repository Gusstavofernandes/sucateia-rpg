# -*- coding: utf-8 -*-
with open("scripts/world/alto_west_cais.gd", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Adicionar constantes
target_const = 'const KHEMET_MEMORY_WELL_SHD     := "res://assets/reconstruction/khemet_memory_nexus_well_sombra.png"'
new_const = '''const KHEMET_MEMORY_WELL_SHD     := "res://assets/reconstruction/khemet_memory_nexus_well_sombra.png"
const KHEMET_RUINED_COLUMNS       := "res://assets/reconstruction/khemet_ruined_columns_cluster.png"
const KHEMET_RUINED_COLUMNS_SHD   := "res://assets/reconstruction/khemet_ruined_columns_cluster_sombra.png"'''

text = text.replace(target_const, new_const)

# 2. Adicionar chamadas de posicionamento
target_place = '\t# -------------------------------------------------------------------------\n\t# 12. A ESFINGE GUARDIÃ DE PEDRA E BRONZE'
new_place = '''\t# -------------------------------------------------------------------------
\t# 11B. COLUNATAS E TAMBORES DE COLUNAS EM RUÍNAS (AVENIDA IMPERIAL)
\t# -------------------------------------------------------------------------
\tvar columns_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-12400, -1480), "scale": Vector2(0.75, 0.70), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-13600, -1530), "scale": Vector2(0.80, 0.74), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-14600, -1650), "scale": Vector2(0.82, 0.76), "rot": 0.04,  "flip": false},
\t\t{"pos": Vector2(-15500, -1920), "scale": Vector2(0.88, 0.80), "rot": -0.02, "flip": true}
\t]
\tfor col_info in columns_data:
\t\t_place_khemet_columns(cliffs_group, root, col_info["pos"], col_info["scale"], col_info["rot"], col_info["flip"])

\t# -------------------------------------------------------------------------
\t# 12. A ESFINGE GUARDIÃ DE PEDRA E BRONZE'''

text = text.replace(target_place, new_place)

# 3. Adicionar método _place_khemet_columns
target_func = 'func _place_khemet_memory_well('
new_func = '''func _place_khemet_columns(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(KHEMET_RUINED_COLUMNS_SHD) as Texture2D
\tshd.position = pos + Vector2(14.0, 20.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.rotation = rot
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(KHEMET_RUINED_COLUMNS) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tspr.rotation = rot
\tparent.add_child(spr)

\t_build_rock_collision(col_root, pos + Vector2(0.0, 20.0) * scale.y, Vector2(240, 140) * absf(scale.x))

func _place_khemet_memory_well('''

text = text.replace(target_func, new_func)

with open("scripts/world/alto_west_cais.gd", "w", encoding="utf-8") as f:
    f.write(text)

print("alto_west_cais.gd atualizado com as colunas em ruínas!")
