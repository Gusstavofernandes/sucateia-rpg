# -*- coding: utf-8 -*-
with open("scripts/world/alto_west_cais.gd", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Constantes
const_target = 'const KHEMET_RUINED_COLUMNS_SHD   := "res://assets/reconstruction/khemet_ruined_columns_cluster_sombra.png"'
new_consts = '''const KHEMET_RUINED_COLUMNS_SHD   := "res://assets/reconstruction/khemet_ruined_columns_cluster_sombra.png"
const KHEMET_GLYPH_STELE          := "res://assets/reconstruction/khemet_glyph_stele_crystal.png"
const KHEMET_GLYPH_STELE_SHD      := "res://assets/reconstruction/khemet_glyph_stele_crystal_sombra.png"
const KHEMET_AVENUE_SPHINX        := "res://assets/reconstruction/khemet_avenue_sphinx_statue.png"
const KHEMET_AVENUE_SPHINX_SHD    := "res://assets/reconstruction/khemet_avenue_sphinx_statue_sombra.png"
const KHEMET_BRAZIER              := "res://assets/reconstruction/khemet_bronze_brazier_altar.png"
const KHEMET_BRAZIER_SHD          := "res://assets/reconstruction/khemet_bronze_brazier_altar_sombra.png"
const KHEMET_SARCOPHAGUS          := "res://assets/reconstruction/khemet_automaton_sarcophagus.png"
const KHEMET_SARCOPHAGUS_SHD      := "res://assets/reconstruction/khemet_automaton_sarcophagus_sombra.png"'''

text = text.replace(const_target, new_consts)

# 2. Substituir a seção 8 (Sítios e Lajes) por uma pavimentação muito mais densa
old_ruins = '''\t# -------------------------------------------------------------------------
\t# 8. SÍTIOS ARQUEOLÓGICOS E LAJES PRECURSORAS DE KHEMET-RA
\t# -------------------------------------------------------------------------
\tvar ruins_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-6200, -1150),  "scale": Vector2(0.68, 0.62), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-10800, -1450), "scale": Vector2(0.82, 0.74), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-12000, -1520), "scale": Vector2(0.78, 0.70), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-12800, -1480), "scale": Vector2(0.85, 0.76), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-13800, -1560), "scale": Vector2(0.88, 0.78), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-14600, -1620), "scale": Vector2(0.92, 0.82), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-15700, -1950), "scale": Vector2(0.95, 0.85), "rot": 0.03,  "flip": false}
\t]
\tfor r_info in ruins_data:
\t\t_place_khemet_ruins(ruins_group, root, r_info["pos"], r_info["scale"], r_info["rot"], r_info["flip"])'''

new_ruins = '''\t# -------------------------------------------------------------------------
\t# 8. SÍTIOS ARQUEOLÓGICOS & CALÇADA IMPERIAL PAVIMENTADA DE KHEMET-RA
\t# -------------------------------------------------------------------------
\tvar ruins_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-6200, -1150),  "scale": Vector2(0.68, 0.62), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-9600, -1350),  "scale": Vector2(0.75, 0.68), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-10800, -1450), "scale": Vector2(0.82, 0.74), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-11400, -1520), "scale": Vector2(0.86, 0.78), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-11800, -1530), "scale": Vector2(0.88, 0.80), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-12200, -1500), "scale": Vector2(0.85, 0.76), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-12600, -1490), "scale": Vector2(0.88, 0.78), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-13000, -1470), "scale": Vector2(0.90, 0.80), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-13400, -1520), "scale": Vector2(0.88, 0.78), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-13800, -1560), "scale": Vector2(0.92, 0.82), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-14250, -1580), "scale": Vector2(0.95, 0.85), "rot": 0.00,  "flip": false},
\t\t{"pos": Vector2(-14650, -1620), "scale": Vector2(0.92, 0.82), "rot": 0.02,  "flip": true},
\t\t{"pos": Vector2(-15000, -1720), "scale": Vector2(0.90, 0.80), "rot": -0.02, "flip": false},
\t\t{"pos": Vector2(-15400, -1850), "scale": Vector2(0.92, 0.82), "rot": 0.03,  "flip": true},
\t\t{"pos": Vector2(-15800, -1960), "scale": Vector2(0.95, 0.85), "rot": -0.02, "flip": false},
\t\t{"pos": Vector2(-16250, -2000), "scale": Vector2(1.00, 0.88), "rot": 0.02,  "flip": true}
\t]
\tfor r_info in ruins_data:
\t\t_place_khemet_ruins(ruins_group, root, r_info["pos"], r_info["scale"], r_info["rot"], r_info["flip"])'''

text = text.replace(old_ruins, new_ruins)

# 3. Densificação dos props de Khemet-Ra (Esfinges, Estelas, Braseiros, Sarcófagos, Colunas)
old_khemet_section = '''\t# -------------------------------------------------------------------------
\t# 11. POÇO DE MEMÓRIA SOLAR & NEXUS PRECURSOR DE KHEMET-RA
\t# -------------------------------------------------------------------------
\t_place_khemet_memory_well(cliffs_group, root, Vector2(-11600, -1550), Vector2(0.95, 0.90))

\t# -------------------------------------------------------------------------
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
\t# 12. A ESFINGE GUARDIÃ DE PEDRA E BRONZE
\t# -------------------------------------------------------------------------
\t_place_khemet_sphinx(cliffs_group, root, Vector2(-13100, -1460), Vector2(0.92, 0.86), false)

\t# -------------------------------------------------------------------------
\t# 13. O PILONE / PORTAL MONUMENTAL DO TEMPLO DE KHEMET-RA
\t# -------------------------------------------------------------------------
\t_place_khemet_temple_gate(cliffs_group, root, Vector2(-14250, -1580), Vector2(1.05, 0.98))

\t# -------------------------------------------------------------------------
\t# 14. A RAMPA CERIMONIAL DA NECRÓPOLE SUBTERRÂNEA
\t# -------------------------------------------------------------------------
\t_place_khemet_necropolis_ramp(cliffs_group, root, Vector2(-15100, -2100), Vector2(0.95, 0.90))

\t# -------------------------------------------------------------------------
\t# 15. A GRANDE PIRÂMIDE PRECURSORA SOTERRADA DE KHEMET-RA (MONUMENTO TITÂNICO)
\t# -------------------------------------------------------------------------
\t_place_khemet_great_pyramid(cliffs_group, root, Vector2(-16300, -2020), Vector2(1.35, 1.25))'''

new_khemet_section = '''\t# -------------------------------------------------------------------------
\t# 11. POÇO DE MEMÓRIA SOLAR & NEXUS PRECURSOR DE KHEMET-RA
\t# -------------------------------------------------------------------------
\t_place_khemet_memory_well(cliffs_group, root, Vector2(-11600, -1550), Vector2(0.95, 0.90))

\t# 4 Braseiros Cerimoniais em volta do Poço de Memória Solar
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11820, -1650), Vector2(0.62, 0.58))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11380, -1650), Vector2(0.62, 0.58))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11820, -1450), Vector2(0.62, 0.58))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-11380, -1450), Vector2(0.62, 0.58))

\t# -------------------------------------------------------------------------
\t# 12. AVENIDA DAS ESFINGES PROCESSIONAIS (Flanqueando a Calçada Imperial)
\t# -------------------------------------------------------------------------
\tvar avenue_sphinxes: Array[Dictionary] = [
\t\t# Par 1: Entrada da Avenida
\t\t{"pos": Vector2(-12150, -1640), "scale": Vector2(0.65, 0.60), "flip": false},
\t\t{"pos": Vector2(-12150, -1360), "scale": Vector2(0.65, 0.60), "flip": true},
\t\t# Par 2: Meio da Avenida
\t\t{"pos": Vector2(-12750, -1640), "scale": Vector2(0.68, 0.62), "flip": false},
\t\t{"pos": Vector2(-12750, -1350), "scale": Vector2(0.68, 0.62), "flip": true},
\t\t# Par 3: Próximo à Grande Esfinge
\t\t{"pos": Vector2(-13450, -1670), "scale": Vector2(0.70, 0.64), "flip": false},
\t\t{"pos": Vector2(-13450, -1370), "scale": Vector2(0.70, 0.64), "flip": true},
\t\t# Par 4: Antes do Portal do Pilone
\t\t{"pos": Vector2(-13980, -1690), "scale": Vector2(0.72, 0.65), "flip": false},
\t\t{"pos": Vector2(-13980, -1390), "scale": Vector2(0.72, 0.65), "flip": true}
\t]
\tfor s_data in avenue_sphinxes:
\t\t_place_khemet_avenue_sphinx(cliffs_group, root, s_data["pos"], s_data["scale"], s_data["flip"])

\t# -------------------------------------------------------------------------
\t# 13. ESTELAS SAGRADAS COM CRISTAIS SOLARES (Balizas Luminosas na Calçada)
\t# -------------------------------------------------------------------------
\tvar steles_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-11900, -1620), "scale": Vector2(0.65, 0.60), "flip": false},
\t\t{"pos": Vector2(-12450, -1370), "scale": Vector2(0.68, 0.62), "flip": true},
\t\t{"pos": Vector2(-13100, -1650), "scale": Vector2(0.70, 0.64), "flip": false},
\t\t{"pos": Vector2(-13700, -1380), "scale": Vector2(0.72, 0.65), "flip": true},
\t\t{"pos": Vector2(-14550, -1720), "scale": Vector2(0.72, 0.65), "flip": false},
\t\t{"pos": Vector2(-15250, -1850), "scale": Vector2(0.75, 0.68), "flip": true},
\t\t{"pos": Vector2(-15950, -2100), "scale": Vector2(0.78, 0.70), "flip": false}
\t]
\tfor st_data in steles_data:
\t\t_place_khemet_stele(cliffs_group, root, st_data["pos"], st_data["scale"], st_data["flip"])

\t# -------------------------------------------------------------------------
\t# 14. COLUNATAS E PÓRTICOS EM RUÍNAS
\t# -------------------------------------------------------------------------
\tvar columns_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-12350, -1720), "scale": Vector2(0.76, 0.72), "rot": 0.02,  "flip": false},
\t\t{"pos": Vector2(-12950, -1310), "scale": Vector2(0.78, 0.74), "rot": -0.03, "flip": true},
\t\t{"pos": Vector2(-13600, -1740), "scale": Vector2(0.82, 0.76), "rot": 0.04,  "flip": false},
\t\t{"pos": Vector2(-14550, -1450), "scale": Vector2(0.84, 0.78), "rot": -0.02, "flip": true},
\t\t{"pos": Vector2(-14800, -1820), "scale": Vector2(0.86, 0.80), "rot": 0.03,  "flip": false},
\t\t{"pos": Vector2(-15600, -1750), "scale": Vector2(0.90, 0.82), "rot": -0.03, "flip": true}
\t]
\tfor col_info in columns_data:
\t\t_place_khemet_columns(cliffs_group, root, col_info["pos"], col_info["scale"], col_info["rot"], col_info["flip"])

\t# -------------------------------------------------------------------------
\t# 15. A GRANDE ESFINGE GUARDIÃ COLOSSAL (O Coração da Praça Imperial)
\t# -------------------------------------------------------------------------
\t_place_khemet_sphinx(cliffs_group, root, Vector2(-13050, -1480), Vector2(0.95, 0.88), false)
\t_place_khemet_brazier(cliffs_group, root, Vector2(-13280, -1420), Vector2(0.68, 0.62))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-12820, -1420), Vector2(0.68, 0.62))

\t# -------------------------------------------------------------------------
\t# 16. O PILONE / PORTAL MONUMENTAL DO TEMPLO DE KHEMET-RA
\t# -------------------------------------------------------------------------
\t_place_khemet_temple_gate(cliffs_group, root, Vector2(-14250, -1580), Vector2(1.05, 0.98))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-14480, -1530), Vector2(0.72, 0.66))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-14020, -1530), Vector2(0.72, 0.66))

\t# -------------------------------------------------------------------------
\t# 17. SARCÓFAGOS E RELICÁRIOS DE AUTÔMATOS (Mecânica e Tumbas Pré-Cataclismo)
\t# -------------------------------------------------------------------------
\tvar sarcophagus_data: Array[Dictionary] = [
\t\t{"pos": Vector2(-10600, -1420), "scale": Vector2(0.68, 0.62), "rot": 0.05,  "flip": false},
\t\t{"pos": Vector2(-11750, -1720), "scale": Vector2(0.72, 0.66), "rot": -0.04, "flip": true},
\t\t{"pos": Vector2(-14850, -2120), "scale": Vector2(0.75, 0.68), "rot": 0.06,  "flip": false},
\t\t{"pos": Vector2(-15350, -2050), "scale": Vector2(0.78, 0.70), "rot": -0.05, "flip": true},
\t\t{"pos": Vector2(-16050, -1880), "scale": Vector2(0.82, 0.74), "rot": 0.04,  "flip": false},
\t\t{"pos": Vector2(-16650, -1960), "scale": Vector2(0.85, 0.76), "rot": -0.06, "flip": true}
\t]
\tfor sarc_info in sarcophagus_data:
\t\t_place_khemet_sarcophagus(cliffs_group, root, sarc_info["pos"], sarc_info["scale"], sarc_info["rot"], sarc_info["flip"])

\t# -------------------------------------------------------------------------
\t# 18. A RAMPA CERIMONIAL DA NECRÓPOLE SUBTERRÂNEA
\t# -------------------------------------------------------------------------
\t_place_khemet_necropolis_ramp(cliffs_group, root, Vector2(-15100, -2100), Vector2(0.95, 0.90))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-15320, -2040), Vector2(0.70, 0.64))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-14880, -2040), Vector2(0.70, 0.64))

\t# -------------------------------------------------------------------------
\t# 19. A GRANDE PIRÂMIDE PRECURSORA SOTERRADA DE KHEMET-RA (MONUMENTO TITÂNICO)
\t# -------------------------------------------------------------------------
\t_place_khemet_great_pyramid(cliffs_group, root, Vector2(-16300, -2020), Vector2(1.35, 1.25))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-16650, -1880), Vector2(0.78, 0.70))
\t_place_khemet_brazier(cliffs_group, root, Vector2(-15950, -1880), Vector2(0.78, 0.70))'''

text = text.replace(old_khemet_section, new_khemet_section)

# 4. Adicionar os novos métodos
methods_to_add = '''func _place_khemet_stele(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, flip: bool = false) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(KHEMET_GLYPH_STELE_SHD) as Texture2D
\tshd.position = pos + Vector2(10.0, 14.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(KHEMET_GLYPH_STELE) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tparent.add_child(spr)

\t# Luz azul arcana no cristal solar do topo
\tvar crystal_light := PointLight2D.new()
\tcrystal_light.texture = load(LIGHT_TEX) as Texture2D
\tcrystal_light.position = pos + Vector2(12.0 * (-1.0 if flip else 1.0), -130.0) * scale.y
\tcrystal_light.color = Color(0.25, 0.70, 1.0, 0.95)
\tcrystal_light.energy = 0.75
\tcrystal_light.texture_scale = 0.55
\tparent.add_child(crystal_light)

\t# Luz dourada suave nos glifos iluminados da placa
\tvar glyph_light := PointLight2D.new()
\tglyph_light.texture = load(LIGHT_TEX) as Texture2D
\tglyph_light.position = pos + Vector2(0.0, 20.0) * scale.y
\tglyph_light.color = Color(1.0, 0.85, 0.40, 0.70)
\tglyph_light.energy = 0.45
\tglyph_light.texture_scale = 0.45
\tparent.add_child(glyph_light)

\t_build_rock_collision(col_root, pos + Vector2(0.0, 40.0) * scale.y, Vector2(120, 70) * absf(scale.x))

func _place_khemet_avenue_sphinx(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, flip: bool = false) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(KHEMET_AVENUE_SPHINX_SHD) as Texture2D
\tshd.position = pos + Vector2(12.0, 16.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(KHEMET_AVENUE_SPHINX) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tparent.add_child(spr)

\t# Brilho de bronze sutil no peito
\tvar chest_light := PointLight2D.new()
\tchest_light.texture = load(LIGHT_TEX) as Texture2D
\tchest_light.position = pos + Vector2(-30.0 * (-1.0 if flip else 1.0), -20.0) * scale.y
\tchest_light.color = Color(0.35, 0.75, 0.90, 0.70)
\tchest_light.energy = 0.40
\tchest_light.texture_scale = 0.35
\tparent.add_child(chest_light)

\t_build_rock_collision(col_root, pos + Vector2(0.0, 25.0) * scale.y, Vector2(220, 110) * absf(scale.x))

func _place_khemet_brazier(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2) -> void:
\tvar shd := Sprite2D.new()
\tshd.texture = load(KHEMET_BRAZIER_SHD) as Texture2D
\tshd.position = pos + Vector2(10.0, 14.0)
\tshd.scale = scale
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(KHEMET_BRAZIER) as Texture2D
\tspr.position = pos
\tspr.scale = scale
\tparent.add_child(spr)

\t# Fogo solar dourado radiante
\tvar fire_light := PointLight2D.new()
\tfire_light.texture = load(LIGHT_TEX) as Texture2D
\tfire_light.position = pos + Vector2(0.0, -35.0) * scale.y
\tfire_light.color = Color(1.0, 0.75, 0.35, 1.0)
\tfire_light.energy = 0.95
\tfire_light.texture_scale = 0.85
\tparent.add_child(fire_light)

\t# Chama azul arcana no topo das brasas
\tvar blue_wisp := PointLight2D.new()
\tblue_wisp.texture = load(LIGHT_TEX) as Texture2D
\tblue_wisp.position = pos + Vector2(0.0, -75.0) * scale.y
\tblue_wisp.color = Color(0.30, 0.65, 1.0, 0.85)
\tblue_wisp.energy = 0.55
\tblue_wisp.texture_scale = 0.45
\tparent.add_child(blue_wisp)

\t_build_rock_collision(col_root, pos + Vector2(0.0, 15.0) * scale.y, Vector2(160, 90) * scale.x)

func _place_khemet_sarcophagus(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool = false) -> void:
\tvar final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

\tvar shd := Sprite2D.new()
\tshd.texture = load(KHEMET_SARCOPHAGUS_SHD) as Texture2D
\tshd.position = pos + Vector2(12.0, 18.0)
\tshd.scale = Vector2(absf(final_scale.x), final_scale.y)
\tshd.rotation = rot
\tshd.z_index = -1
\tparent.add_child(shd)

\tvar spr := Sprite2D.new()
\tspr.texture = load(KHEMET_SARCOPHAGUS) as Texture2D
\tspr.position = pos
\tspr.scale = final_scale
\tspr.rotation = rot
\tparent.add_child(spr)

\t# Brilho mecânico/arcano nas engrenagens e fechaduras de bronze
\tvar lock_light := PointLight2D.new()
\tlock_light.texture = load(LIGHT_TEX) as Texture2D
\tlock_light.position = pos + Vector2(25.0 * (-1.0 if flip else 1.0), -10.0) * scale.y
\tlock_light.color = Color(0.40, 0.75, 0.95, 0.70)
\tlock_light.energy = 0.45
\tlock_light.texture_scale = 0.35
\tparent.add_child(lock_light)

\t_build_rock_collision(col_root, pos + Vector2(0.0, 15.0) * scale.y, Vector2(240, 120) * absf(scale.x))

'''

target_place_columns = 'func _place_khemet_columns('
text = text.replace(target_place_columns, methods_to_add + target_place_columns)

with open("scripts/world/alto_west_cais.gd", "w", encoding="utf-8") as f:
    f.write(text)

print("scripts/world/alto_west_cais.gd enriquecido com a arquitetura sagrada e densa de Khemet-Ra!")
