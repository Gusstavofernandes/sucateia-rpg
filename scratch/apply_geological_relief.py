# -*- coding: utf-8 -*-
with open("scripts/world/alto_west_cais.gd", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Constantes dos novos assets de terreno natural
const_target = 'const LIGHT_TEX               := "res://assets/fx/light.svg"'
new_consts = '''const LIGHT_TEX               := "res://assets/fx/light.svg"

# --- RELEVO GEOLÓGICO & FORMAÇÕES NATURAIS DO DESERTO ---
const CHAPADA_DUNE_RIDGE       := "res://assets/reconstruction/chapada_dune_ridge_crest.png"
const CHAPADA_DUNE_RIDGE_SHD   := "res://assets/reconstruction/chapada_dune_ridge_crest_sombra.png"
const CHAPADA_DUNE_VALLEY      := "res://assets/reconstruction/chapada_dune_hollow_valley.png"
const CHAPADA_DUNE_VALLEY_SHD  := "res://assets/reconstruction/chapada_dune_hollow_valley_sombra.png"
const CHAPADA_CANYON_WALL      := "res://assets/reconstruction/chapada_canyon_cliff_wall.png"
const CHAPADA_CANYON_WALL_SHD  := "res://assets/reconstruction/chapada_canyon_cliff_wall_sombra.png"
const CHAPADA_ROCK_CHASM       := "res://assets/reconstruction/chapada_rock_chasm_fissure.png"
const CHAPADA_ROCK_CHASM_SHD   := "res://assets/reconstruction/chapada_rock_chasm_fissure_sombra.png"
const CHAPADA_MESA_BUTTE       := "res://assets/reconstruction/chapada_sandstone_mesa_butte.png"
const CHAPADA_MESA_BUTTE_SHD   := "res://assets/reconstruction/chapada_sandstone_mesa_butte_sombra.png"'''

text = text.replace(const_target, new_consts, 1)

# 2. Adicionar o grupo de dunas e vales na árvore de nós
node_target = '\tvar beach_sand_group := Node2D.new()\n\tbeach_sand_group.name = "BeachSandLayer"\n\tbeach_sand_group.z_index = -12\n\troot.add_child(beach_sand_group)'
new_node = '''\tvar beach_sand_group := Node2D.new()
\tbeach_sand_group.name = "BeachSandLayer"
\tbeach_sand_group.z_index = -12
\troot.add_child(beach_sand_group)

\t# Camada de relevo de dunas onduladas e vales de areia
\tvar dunes_layer := Node2D.new()
\tdunes_layer.name = "DesertDuneTopography"
\tdunes_layer.z_index = -11
\troot.add_child(dunes_layer)'''

text = text.replace(node_target, new_node, 1)

# 3. Adicionar o posicionamento das formações geológicas em install()
# Inserir antes da seção 10 (Marco 1: Colosso)
place_target = '\t# -------------------------------------------------------------------------\n\t# 10. MARCO 1: COLOSSO AUTÔMATO SOTERRADO'
new_place = '''\t# -------------------------------------------------------------------------
\t# 9B. RELEVO GEOLÓGICO NATURAL DO DESERTO: CRISTAS DE DUNAS & VALES
\t# -------------------------------------------------------------------------
\t# Grandes cristas onduladas de dunas barchan (escultura pelo vento)
\tvar dune_ridges: Array[Dictionary] = [
\t\t{"pos": Vector2(-9500, -1700),  "scale": Vector2(1.15, 0.95), "rot": 0.04,  "flip": false},
\t\t{"pos": Vector2(-11100, -1850), "scale": Vector2(1.20, 1.00), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-12500, -1950), "scale": Vector2(1.30, 1.05), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-13900, -1900), "scale": Vector2(1.25, 1.00), "rot": -0.04, "flip": true},
\t\t{"pos": Vector2(-15300, -1650), "scale": Vector2(1.35, 1.10), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-16500, -1600), "scale": Vector2(1.40, 1.15), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-17300, -1900), "scale": Vector2(1.45, 1.15), "rot": 0.04,  "flip": false}
\t]
\tfor d_info in dune_ridges:
\t\t_place_dune_ridge(dunes_layer, d_info["pos"], d_info["scale"], d_info["rot"], d_info["flip"])

\t# Vales e depressões de areia com seixos (caminhos naturais)
\tvar dune_valleys: Array[Dictionary] = [
\t\t{"pos": Vector2(-10200, -1450), "scale": Vector2(1.10, 0.90), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-11600, -1520), "scale": Vector2(1.15, 0.95), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-13000, -1450), "scale": Vector2(1.20, 0.95), "rot": 0.01,  "flip": false},
\t\t{"pos": Vector2(-14400, -1560), "scale": Vector2(1.25, 1.00), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-16100, -1950), "scale": Vector2(1.30, 1.05), "rot": 0.03,  "flip": false}
\t]
\tfor v_info in dune_valleys:
\t\t_place_dune_valley(dunes_layer, v_info["pos"], v_info["scale"], v_info["rot"], v_info["flip"])

\t# -------------------------------------------------------------------------
\t# 9C. MESAS DE ARENITO & PAREDÕES DE CÂNION (ELEVAÇÃO GEOLÓGICA)
\t# -------------------------------------------------------------------------
\t# Mesas de arenito com topo plano ao fundo norte
\tvar mesas_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-9800, -2200),  "scale": Vector2(1.15, 0.95), "rot": -0.02, "flip": false},
\t\t{"pos": Vector2(-12200, -2350), "scale": Vector2(1.25, 1.05), "rot": 0.03,  "flip": true},
\t\t{"pos": Vector2(-14800, -2400), "scale": Vector2(1.30, 1.10), "rot": -0.02, "flip": false},
\t\t{"pos": Vector2(-16700, -2380), "scale": Vector2(1.35, 1.15), "rot": 0.02,  "flip": true}
\t]
\tfor m_data in mesas_data:
\t\t_place_mesa_butte(cliffs_group, root, m_data["pos"], m_data["scale"], m_data["rot"], m_data["flip"])

\t# Paredões de cânion com estratos sedimentares
\tvar canyon_walls: Array[Dictionary] = [
\t\t{"pos": Vector2(-11000, -2100), "scale": Vector2(1.05, 0.95), "rot": -0.02, "flip": false},
\t\t{"pos": Vector2(-13500, -2180), "scale": Vector2(1.10, 0.98), "rot": 0.03,  "flip": true},
\t\t{"pos": Vector2(-15600, -2250), "scale": Vector2(1.15, 1.00), "rot": -0.01, "flip": false},
\t\t{"pos": Vector2(-17200, -2250), "scale": Vector2(1.20, 1.05), "rot": 0.02,  "flip": true}
\t]
\tfor cw_data in canyon_walls:
\t\t_place_canyon_wall(cliffs_group, root, cw_data["pos"], cw_data["scale"], cw_data["rot"], cw_data["flip"])

\t# Fendas geológicas e abismos no solo rochoso
\tvar chasms_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-12600, -1650), "scale": Vector2(0.95, 0.85), "rot": 0.04,  "flip": false},
\t\t{"pos": Vector2(-16100, -1680), "scale": Vector2(1.05, 0.90), "rot": -0.03, "flip": true}
\t]
\tfor ch_data in chasms_data:
\t\t_place_rock_chasm(cliffs_group, root, ch_data["pos"], ch_data["scale"], ch_data["rot"], ch_data["flip"])

\t# -------------------------------------------------------------------------
\t# 10. MARCO 1: COLOSSO AUTÔMATO SOTERRADO'''

text = text.replace(place_target, new_place, 1)

# 4. Adicionar os métodos de instanciação no final
methods_code = '''
func _place_dune_ridge(parent: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(CHAPADA_DUNE_RIDGE_SHD) as Texture2D
\tshd.position = pos + Vector2(10.0, 14.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.rotation = rot
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(CHAPADA_DUNE_RIDGE) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tspr.rotation = rot
\tspr.modulate = Color(1.02, 0.98, 0.92, 0.95)
\tparent.add_child(spr)

func _place_dune_valley(parent: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(CHAPADA_DUNE_VALLEY_SHD) as Texture2D
\tshd.position = pos + Vector2(8.0, 12.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.rotation = rot
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(CHAPADA_DUNE_VALLEY) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tspr.rotation = rot
\tspr.modulate = Color(1.00, 0.96, 0.90, 0.92)
\tparent.add_child(spr)

func _place_canyon_wall(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(CHAPADA_CANYON_WALL_SHD) as Texture2D
\tshd.position = pos + Vector2(12.0, 20.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.rotation = rot
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(CHAPADA_CANYON_WALL) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tspr.rotation = rot
\tparent.add_child(spr)

\t_build_rock_collision(col_root, pos + Vector2(0.0, 40.0) * scale.y, Vector2(620, 120) * absf(scale.x))

func _place_mesa_butte(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(CHAPADA_MESA_BUTTE_SHD) as Texture2D
\tshd.position = pos + Vector2(16.0, 24.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.rotation = rot
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(CHAPADA_MESA_BUTTE) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tspr.rotation = rot
\tparent.add_child(spr)

\t_build_rock_collision(col_root, pos + Vector2(0.0, 60.0) * scale.y, Vector2(580, 200) * absf(scale.x))

func _place_rock_chasm(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(CHAPADA_ROCK_CHASM_SHD) as Texture2D
\tshd.position = pos + Vector2(10.0, 16.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.rotation = rot
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(CHAPADA_ROCK_CHASM) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tspr.rotation = rot
\tparent.add_child(spr)

\t# Colisão no interior da fenda para contornar o abismo
\t_build_rock_collision(col_root, pos + Vector2(0.0, 0.0), Vector2(380, 110) * absf(scale.x))
'''

text += methods_code

with open("scripts/world/alto_west_cais.gd", "w", encoding="utf-8") as f:
    f.write(text)

print("alto_west_cais.gd atualizado com o relevo geológico completo do deserto!")
