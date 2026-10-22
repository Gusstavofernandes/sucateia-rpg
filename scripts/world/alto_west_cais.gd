extends RefCounted

# =============================================================================
# REGIÃO 1: A GRANDE CHAPADA DE ARENITO & O IMPÉRIO SEPULTADO DE KHEMET-RA
# Platô elevado de rocha sedimentar de arenito com escarpas de falésia voltadas
# para o mar, escadarias naturais de estratos rochosos, grutas, acampamento avançado
# de catadores goblins, monólitos, a Esfinge Guardiã, o Portal do Templo de Pilones,
# o Poço de Memória Solar, a Rampa da Necrópole Subterrânea e a Grande Pirâmide Precursora.
# =============================================================================

const RED_ROCKS_CLUSTER       := "res://assets/reconstruction/red_iron_rocks_cluster.png"
const RED_CLIFF_EDGE          := "res://assets/reconstruction/red_rock_cliff_edge.png"
const RED_SOIL_PATCH          := "res://assets/reconstruction/red_soil_transition_patch.png"
const YELLOW_SOIL_PATCH       := "res://assets/reconstruction/yellow_coastal_soil_patch.png"
const BEACH_SAND_PATCH        := "res://assets/reconstruction/areia_praia_litoranea.png"

# --- ASSETS DA CHAPADA DE ARENITO & MARCOS ARQUEOLÓGICOS DE KHEMET-RA ---
const CHAPADA_PLATEAU_GROUND   := "res://assets/reconstruction/chapada_plateau_ground.png"
const CHAPADA_ROCK_STAIRS      := "res://assets/reconstruction/chapada_rock_stairs.png"
const CHAPADA_ROCK_STAIRS_SHD  := "res://assets/reconstruction/chapada_rock_stairs_sombra.png"
const CHAPADA_CLIFF_WALL       := "res://assets/reconstruction/chapada_cliff_wall.png"
const CHAPADA_CLIFF_WALL_SHD   := "res://assets/reconstruction/chapada_cliff_wall_sombra.png"
const KHEMET_RUINS_SLAB        := "res://assets/reconstruction/khemet_ancient_ruins_slab.png"
const KHEMET_RUINS_SLAB_SHD    := "res://assets/reconstruction/khemet_ancient_ruins_slab_sombra.png"
const CHAPADA_CAVE             := "res://assets/reconstruction/chapada_sandstone_cave.png"
const CHAPADA_CAVE_SHD         := "res://assets/reconstruction/chapada_sandstone_cave_sombra.png"

const KHEMET_OBELISK           := "res://assets/reconstruction/khemet_broken_obelisk.png"
const KHEMET_OBELISK_SHD       := "res://assets/reconstruction/khemet_broken_obelisk_sombra.png"
const GOBLIN_EXPEDITION_CAMP   := "res://assets/reconstruction/chapada_goblin_expedition_camp.png"
const GOBLIN_EXPEDITION_CAMP_SHD:= "res://assets/reconstruction/chapada_goblin_expedition_camp_sombra.png"
const CHAPADA_DESERT_VEG       := "res://assets/reconstruction/chapada_desert_vegetation.png"
const CHAPADA_DESERT_VEG_SHD   := "res://assets/reconstruction/chapada_desert_vegetation_sombra.png"
const CHAPADA_PILLAR_MONOLITH  := "res://assets/reconstruction/chapada_sandstone_pillar_monolith.png"
const CHAPADA_PILLAR_MONOLITH_SHD:= "res://assets/reconstruction/chapada_sandstone_pillar_monolith_sombra.png"
const KHEMET_COLOSSUS          := "res://assets/reconstruction/khemet_buried_automaton_colossus.png"
const KHEMET_COLOSSUS_SHD      := "res://assets/reconstruction/khemet_buried_automaton_colossus_sombra.png"

# --- OS MARCOS MONUMENTAIS SUPREMOS DE KHEMET-RA ---
const KHEMET_GREAT_PYRAMID       := "res://assets/reconstruction/khemet_great_pyramid.png"
const KHEMET_GREAT_PYRAMID_SHD   := "res://assets/reconstruction/khemet_great_pyramid_sombra.png"
const KHEMET_TEMPLE_GATE         := "res://assets/reconstruction/khemet_temple_pylon_gate.png"
const KHEMET_TEMPLE_GATE_SHD     := "res://assets/reconstruction/khemet_temple_pylon_gate_sombra.png"
const KHEMET_GUARDIAN_SPHINX     := "res://assets/reconstruction/khemet_guardian_sphinx.png"
const KHEMET_GUARDIAN_SPHINX_SHD := "res://assets/reconstruction/khemet_guardian_sphinx_sombra.png"
const KHEMET_NECROPOLIS_RAMP     := "res://assets/reconstruction/khemet_necropolis_ramp.png"
const KHEMET_NECROPOLIS_RAMP_SHD := "res://assets/reconstruction/khemet_necropolis_ramp_sombra.png"
const KHEMET_MEMORY_WELL         := "res://assets/reconstruction/khemet_memory_nexus_well.png"
const KHEMET_MEMORY_WELL_SHD     := "res://assets/reconstruction/khemet_memory_nexus_well_sombra.png"

# --- FALÉSIAS E ROCHAS LITORÂNEAS ---
const YELLOW_CLIFF            := "res://assets/reconstruction/falesia_maritima_amarelada.png"
const YELLOW_CLIFF_SHD        := "res://assets/reconstruction/falesia_maritima_amarelada_sombra.png"
const PROMONTORY_CLIFF        := "res://assets/reconstruction/falesia_promontorio_costeiro.png"
const PROMONTORY_CLIFF_SHD    := "res://assets/reconstruction/falesia_promontorio_costeiro_sombra.png"

const COASTAL_REEF            := "res://assets/reconstruction/rochas_maritimas_recife_costeiro.png"
const COASTAL_REEF_SHD        := "res://assets/reconstruction/rochas_maritimas_recife_costeiro_sombra.png"
const BEACH_BOULDERS          := "res://assets/reconstruction/rochedos_praia_maritima.png"
const BEACH_BOULDERS_SHD      := "res://assets/reconstruction/rochedos_praia_maritima_sombra.png"

const SMALL_ROCKS_MAIN        := "res://assets/reconstruction/pequenas_pedras_solo_costeiro.png"
const SMALL_ROCKS_MAIN_SHD    := "res://assets/reconstruction/pequenas_pedras_solo_costeiro_sombra.png"
const SMALL_ROCKS_A           := "res://assets/reconstruction/pequenas_pedras_var_a.png"
const SMALL_ROCKS_A_SHD       := "res://assets/reconstruction/pequenas_pedras_var_a_sombra.png"
const SMALL_ROCKS_B           := "res://assets/reconstruction/pequenas_pedras_var_b.png"
const SMALL_ROCKS_B_SHD       := "res://assets/reconstruction/pequenas_pedras_var_b_sombra.png"
const SMALL_ROCKS_C           := "res://assets/reconstruction/pequenas_pedras_var_c.png"
const SMALL_ROCKS_C_SHD       := "res://assets/reconstruction/pequenas_pedras_var_c_sombra.png"

const SHORE_WAVES_SHADER      := "res://assets/reconstruction/coastal_shore_waves.gdshader"

const COASTAL_WALL            := "res://assets/infrastructure/coastal_wall.png"
const RETAINING_EDGE          := "res://assets/infrastructure/retaining_edge.png"
const FOUNDATION_TEX          := "res://assets/terrain/foundation.png"
const WALKWAY_TEX             := "res://assets/infrastructure/walkway.png"
const LANTERN_TEX             := "res://assets/infrastructure/lantern.png"
const LIGHT_TEX               := "res://assets/fx/light.svg"

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
const CHAPADA_MESA_BUTTE_SHD   := "res://assets/reconstruction/chapada_sandstone_mesa_butte_sombra.png"

func get_tide_y_at(x: float) -> float:
	if x > -750.0:
		var t: float = clampf((x + 750.0) / 1150.0, 0.0, 1.0)
		return lerpf(115.0, 1500.0, t)
	
	var t: float = clampf((-x - 750.0) / 16750.0, 0.0, 1.0)
	var base_rise: float = -t * 1350.0
	var drift: float = 120.0 + base_rise
	var var_wave: float = sin(x * 0.004) * 22.0 + sin(x * 0.009) * 14.0 + sin(x * 0.0015) * 32.0
	return drift + var_wave

func get_cliff_base_y_at(x: float) -> float:
	if x > -750.0:
		return 115.0
	var t: float = clampf((-x - 750.0) / 16750.0, 0.0, 1.0)
	var base_rise: float = -t * 1350.0
	var cliff_offset: float = -320.0 + (sin(x * 0.003) * 18.0 + cos(x * 0.008) * 12.0)
	return 120.0 + base_rise + cliff_offset

func get_soil_color_at(x: float) -> Color:
	var c_natural_earth := Color(1.00, 0.96, 0.88, 0.65)
	var c_soft_earth    := Color(1.04, 0.92, 0.80, 0.72)
	var c_amber_ochre   := Color(1.06, 0.90, 0.74, 0.85)
	var c_yellow_sand   := Color(1.08, 0.88, 0.70, 0.88)
	var c_beach_gold    := Color(1.10, 0.94, 0.74, 0.92)

	var t1: float = clampf((-x - 200.0) / 1200.0, 0.0, 1.0)
	var t2: float = clampf((-x - 1400.0) / 1800.0, 0.0, 1.0)
	var t3: float = clampf((-x - 3200.0) / 2300.0, 0.0, 1.0)
	var t4: float = clampf((-x - 5500.0) / 3000.0, 0.0, 1.0)

	var c: Color = c_natural_earth.lerp(c_soft_earth, t1)
	c = c.lerp(c_amber_ochre, t2)
	c = c.lerp(c_yellow_sand, t3)
	c = c.lerp(c_beach_gold, t4)
	return c

func install(world: Node2D) -> void:
	var player_cam: Camera2D = world.get_node_or_null("Structures/Player/Camera")
	if player_cam:
		player_cam.limit_left = -19500
		player_cam.limit_top = -4600
		player_cam.limit_right = 6650
		player_cam.limit_bottom = 3500

	if world.has_node("AltoWestCaisExpansion"):
		world.get_node("AltoWestCaisExpansion").free()
	if world.has_node("KemetDesertExpansion"):
		world.get_node("KemetDesertExpansion").free()
	if world.has_node("SucateiaWestGroundExpansion"):
		world.get_node("SucateiaWestGroundExpansion").free()

	var root := Node2D.new()
	root.name = "AltoWestCaisExpansion"
	root.z_index = -10
	world.add_child(root)

	var water_shallows := Node2D.new()
	water_shallows.name = "WaterShallowsAndReefs"
	water_shallows.z_as_relative = false
	water_shallows.z_index = -10
	root.add_child(water_shallows)

	# 1. Platô superior da Chapada de Arenito (cobre todo o norte até Y = -2850 de forma homogênea)
	var plato_north := Node2D.new()
	plato_north.name = "PlatoNorthSoil"
	plato_north.z_index = -14
	root.add_child(plato_north)

	var soil_group := Node2D.new()
	soil_group.name = "SoilTransition"
	soil_group.z_index = -13
	root.add_child(soil_group)

	var beach_sand_group := Node2D.new()
	beach_sand_group.name = "BeachSandLayer"
	beach_sand_group.z_index = -12
	root.add_child(beach_sand_group)

	# Camada de relevo de dunas onduladas e vales de areia
	var dunes_layer := Node2D.new()
	dunes_layer.name = "DesertDuneTopography"
	dunes_layer.z_index = -11
	root.add_child(dunes_layer)

	var pier_paving := Node2D.new()
	pier_paving.name = "PierPaving"
	pier_paving.z_index = -11
	root.add_child(pier_paving)

	# Calçadas, lajes e ruínas de Khemet-Ra integradas ao platô
	var ruins_group := Node2D.new()
	ruins_group.name = "KhemetPrecursorRuins"
	ruins_group.z_index = -10
	root.add_child(ruins_group)

	# Fita animada de arrebentação de ondas na praia com triangulação explícita de fita (zero ear-clipping)
	var shore_waves := Polygon2D.new()
	shore_waves.name = "ShoreWavesWash"
	shore_waves.z_as_relative = false
	shore_waves.z_index = -13
	var wave_mat := ShaderMaterial.new()
	wave_mat.shader = load(SHORE_WAVES_SHADER) as Shader
	shore_waves.material = wave_mat

	var wave_verts := PackedVector2Array()
	var wave_polys: Array[PackedInt32Array] = []
	var x_pts: Array[float] = []
	for x in range(-18500, -740, 40):
		x_pts.append(float(x))

	for i in range(x_pts.size()):
		var px: float = x_pts[i]
		var y_tide: float = get_tide_y_at(px)
		wave_verts.append(Vector2(px, y_tide - 72.0))
		wave_verts.append(Vector2(px, y_tide + 78.0))

	for i in range(x_pts.size() - 1):
		var tl: int = i * 2
		var bl: int = i * 2 + 1
		var tr: int = (i + 1) * 2
		var br: int = (i + 1) * 2 + 1
		wave_polys.append(PackedInt32Array([tl, tr, bl]))
		wave_polys.append(PackedInt32Array([tr, br, bl]))

	shore_waves.polygon = wave_verts
	shore_waves.polygons = wave_polys
	root.add_child(shore_waves)

	var ground_details := Node2D.new()
	ground_details.name = "GroundDetailsAndStones"
	ground_details.z_index = -8
	root.add_child(ground_details)

	# Vegetação do deserto (cactos e arbustos de chapada)
	var veg_group := Node2D.new()
	veg_group.name = "DesertVegetationGroup"
	veg_group.z_index = -6
	root.add_child(veg_group)

	# Escadarias naturais de arenito (transitáveis)
	var stairs_group := Node2D.new()
	stairs_group.name = "SandstoneStairs"
	stairs_group.z_index = 0
	root.add_child(stairs_group)

	var walls_group := Node2D.new()
	walls_group.name = "RetainingWalls"
	walls_group.z_index = 0
	root.add_child(walls_group)

	var cliffs_group := Node2D.new()
	cliffs_group.name = "CliffsAndRocks"
	cliffs_group.y_sort_enabled = true
	cliffs_group.z_index = 1
	root.add_child(cliffs_group)

	# -------------------------------------------------------------------------
	# 1. COBERTURA TOTAL DA CHAPADA DE ARENITO & MICRO-TOPOGRAFIA DO DESERTO
	# Base de laje de arenito + ondulações finas de vento (sand ripples) + 
	# fissuras térmicas no leito de rocha + seixos/cascalho espalhado
	# -------------------------------------------------------------------------
	var tex_plateau_ground: Texture2D = load(CHAPADA_PLATEAU_GROUND) as Texture2D
	var tex_sand_ripples: Texture2D   = load(BEACH_SAND_PATCH) as Texture2D
	var tex_chasm_fissure: Texture2D  = load(CHAPADA_ROCK_CHASM) as Texture2D

	for x in range(-200, -18200, -220):
		var y_cliff: float = get_cliff_base_y_at(float(x))
		var col: Color = get_soil_color_at(float(x))
		
		var y_start: float = y_cliff - 100.0
		var y_end: float = -2850.0
		var num_v_steps: int = int(ceilf((y_start - y_end) / 160.0)) + 1
		
		for p_step in range(num_v_steps):
			var frac: float = float(p_step) / float(max(1, num_v_steps - 1))
			var y_plateau: float = lerpf(y_start, y_end, frac)
			
			var j_x: float = sin(float(x) * 0.02 + float(p_step) * 1.8) * 45.0
			var j_y: float = cos(float(x) * 0.03 + float(p_step) * 2.1) * 30.0
			var rot: float = sin(float(x) * 0.015 + float(p_step) * 0.8) * 0.22
			var flip_h: bool = ((p_step + abs(x / 220)) % 2 == 1)
			var base_scl_x: float = 0.70 + sin(float(x) * 0.01 + float(p_step)) * 0.08
			var base_scl_y: float = 0.56 + cos(float(x) * 0.015 + float(p_step)) * 0.06
			
			var p_patch := Sprite2D.new()
			p_patch.texture = tex_plateau_ground
			p_patch.position = Vector2(float(x) + j_x, y_plateau + j_y)
			p_patch.scale = Vector2(base_scl_x * (-1.0 if flip_h else 1.0), base_scl_y)
			p_patch.rotation = rot
			
			var p_col := col
			p_col.a = 0.88
			p_patch.modulate = p_col
			plato_north.add_child(p_patch)

			# ITEM 3: Ondulações finas de areia de vento (sand ripples) sobre o platô
			if (p_step % 2 == 1 and abs(x % 340) < 220):
				var rip_patch := Sprite2D.new()
				rip_patch.texture = tex_sand_ripples
				rip_patch.position = Vector2(float(x) + j_x * 0.7, y_plateau + j_y * 0.7)
				rip_patch.scale = Vector2(0.52 * (1.0 if not flip_h else -1.0), 0.42)
				rip_patch.rotation = rot + 0.10
				rip_patch.modulate = Color(col.r * 1.03, col.g * 0.98, col.b * 0.90, 0.42)
				plato_north.add_child(rip_patch)

			# ITEM 3: Fissuras térmicas no leito rochoso em clareiras
			if (p_step == 2 and abs(x % 540) < 180):
				var fiss_patch := Sprite2D.new()
				fiss_patch.texture = tex_chasm_fissure
				fiss_patch.position = Vector2(float(x) - j_x * 0.5, y_plateau + 25.0)
				fiss_patch.scale = Vector2(0.35 * (-1.0 if flip_h else 1.0), 0.28)
				fiss_patch.rotation = rot - 0.15
				fiss_patch.modulate = Color(col.r * 0.90, col.g * 0.85, col.b * 0.80, 0.50)
				plato_north.add_child(fiss_patch)

	# -------------------------------------------------------------------------
	# 2. COBERTURA SUAVE E CONTÍNUA DO SOLO DA PRAIA
	# -------------------------------------------------------------------------
	for x in range(-200, -17600, -115):
		var y_tide: float = get_tide_y_at(float(x))
		var y_cliff: float = get_cliff_base_y_at(float(x))
		var col: Color = get_soil_color_at(float(x))

		var is_beach: bool = (x < -4500)
		var base_tex_path: String = BEACH_SAND_PATCH if is_beach else YELLOW_SOIL_PATCH
		var base_tex: Texture2D = load(base_tex_path) as Texture2D

		var y_steps: int = 3
		for step in range(y_steps):
			var frac: float = float(step) / float(y_steps - 1)
			var y_pos: float = lerpf(y_cliff + 40.0, y_tide - 25.0, frac)
			
			var j_x: float = sin(float(x) * 0.03 + float(step) * 1.7) * 32.0
			var j_y: float = cos(float(x) * 0.04 + float(step) * 2.3) * 22.0
			var rot: float = sin(float(x) * 0.015 + float(step)) * 0.20
			var scl_x: float = (0.55 + sin(float(x) * 0.02) * 0.08) * (1.0 if (step % 2 == 0) else -1.0)
			var scl_y: float = 0.44 + cos(float(x) * 0.02) * 0.06

			var patch := Sprite2D.new()
			patch.texture = base_tex
			patch.position = Vector2(float(x) + j_x, y_pos + j_y)
			patch.scale = Vector2(scl_x, scl_y)
			patch.rotation = rot
			
			var patch_col: Color = col
			patch_col.a = 0.62 if not is_beach else 0.85
			patch.modulate = patch_col

			if is_beach:
				beach_sand_group.add_child(patch)
			else:
				soil_group.add_child(patch)

	# -------------------------------------------------------------------------
	# 3. PEQUENAS PEDRAS E SEIXOS QUEBRANDO A MALHA
	# -------------------------------------------------------------------------
	var small_stone_assets: Array[Dictionary] = [
		{"tex": SMALL_ROCKS_MAIN, "shd": SMALL_ROCKS_MAIN_SHD, "base_scale": 0.38},
		{"tex": SMALL_ROCKS_A,    "shd": SMALL_ROCKS_A_SHD,    "base_scale": 0.45},
		{"tex": SMALL_ROCKS_B,    "shd": SMALL_ROCKS_B_SHD,    "base_scale": 0.42},
		{"tex": SMALL_ROCKS_C,    "shd": SMALL_ROCKS_C_SHD,    "base_scale": 0.46}
	]

	for x in range(-350, -17600, -85):
		var y_tide: float = get_tide_y_at(float(x))
		var y_cliff: float = get_cliff_base_y_at(float(x))
		var col: Color = get_soil_color_at(float(x))
		
		var asset_idx: int = abs(x / 85) % small_stone_assets.size()
		var stone_data: Dictionary = small_stone_assets[asset_idx]
		var flip_h: bool = ((abs(x) / 85) % 2 == 1)

		var mid_y: float = lerpf(y_cliff + 80.0, y_tide - 45.0, 0.45 + sin(float(x) * 0.015) * 0.25)
		var stone_pos := Vector2(float(x) + cos(float(x) * 0.05) * 25.0, mid_y)
		var scl_factor: float = stone_data["base_scale"] * (0.80 + sin(float(x) * 0.03) * 0.25)
		var final_scl := Vector2(scl_factor * (-1.0 if flip_h else 1.0), scl_factor)

		_place_small_stone(ground_details, stone_data["tex"], stone_data["shd"], stone_pos, final_scl, sin(float(x) * 0.02) * 0.25, col)

		if (abs(x) % 170 < 85):
			var tide_edge_pos := Vector2(float(x) + 30.0, y_tide - 15.0 + sin(float(x) * 0.04) * 8.0)
			var sub_idx: int = (asset_idx + 1) % small_stone_assets.size()
			var tide_stone_data: Dictionary = small_stone_assets[sub_idx]
			var tide_scl: float = tide_stone_data["base_scale"] * 0.70
			var wet_col := Color(col.r * 0.85, col.g * 0.85, col.b * 0.82, 0.95)
			_place_small_stone(ground_details, tide_stone_data["tex"], tide_stone_data["shd"], tide_edge_pos, Vector2(tide_scl, tide_scl), -0.10, wet_col)

		if (abs(x) % 190 < 85):
			var cliff_foot_pos := Vector2(float(x) - 20.0, y_cliff + 45.0 + cos(float(x) * 0.03) * 12.0)
			var foot_idx: int = (asset_idx + 2) % small_stone_assets.size()
			var foot_stone_data: Dictionary = small_stone_assets[foot_idx]
			var foot_scl: float = foot_stone_data["base_scale"] * 0.75
			_place_small_stone(ground_details, foot_stone_data["tex"], foot_stone_data["shd"], cliff_foot_pos, Vector2(foot_scl, foot_scl), 0.15, col)

		# Cascalho e seixos esparsos no platô superior da Chapada
		if (abs(x) % 220 < 85):
			var plat_stone_idx: int = (asset_idx + 3) % small_stone_assets.size()
			var plat_data: Dictionary = small_stone_assets[plat_stone_idx]
			var plat_y: float = y_cliff - 250.0 - sin(float(x) * 0.012) * 500.0 - cos(float(x) * 0.02) * 350.0
			var plat_scl: float = plat_data["base_scale"] * 0.65
			_place_small_stone(ground_details, plat_data["tex"], plat_data["shd"], Vector2(float(x) + 15.0, plat_y), Vector2(plat_scl * (-1.0 if flip_h else 1.0), plat_scl), sin(float(x) * 0.03) * 0.20, col)

	# -------------------------------------------------------------------------
	# 4. VEGETAÇÃO ÁRIDA DA CHAPADA (Cactos, capim seco e arbustos espinhosos)
	# -------------------------------------------------------------------------
	for x in range(-900, -17600, -380):
		var y_cliff: float = get_cliff_base_y_at(float(x))
		var veg_y: float = y_cliff - 220.0 - sin(float(x) * 0.018) * 350.0
		var veg_scl: float = 0.38 + cos(float(x) * 0.02) * 0.08
		var veg_flip: bool = (abs(x / 380) % 2 == 1)
		_place_desert_veg(veg_group, Vector2(float(x), veg_y), Vector2(veg_scl * (-1.0 if veg_flip else 1.0), veg_scl))

	# -------------------------------------------------------------------------
	# 5. CAIS URBANO DE PEDRA (X = -125 até X = -750)
	# -------------------------------------------------------------------------
	var pier_segments: Array[Vector2] = [
		Vector2(-125, 120), Vector2(-180, 120), Vector2(-245, 120),
		Vector2(-310, 120), Vector2(-375, 120), Vector2(-440, 120),
		Vector2(-505, 122), Vector2(-570, 122), Vector2(-635, 120),
		Vector2(-700, 118), Vector2(-750, 115)
	]

	for pt in pier_segments:
		var stone := Sprite2D.new()
		stone.texture = load(FOUNDATION_TEX) as Texture2D
		stone.position = pt + Vector2(0, -15)
		stone.scale = Vector2(0.48, 0.40)
		stone.modulate = Color(0.85, 0.78, 0.65, 0.95)
		pier_paving.add_child(stone)

		var walk := Sprite2D.new()
		walk.texture = load(WALKWAY_TEX) as Texture2D
		walk.position = pt + Vector2(0, -6)
		walk.scale = Vector2(0.32, 0.28)
		walk.rotation = 0.02
		pier_paving.add_child(walk)

		var wall := Sprite2D.new()
		wall.texture = load(COASTAL_WALL) as Texture2D
		wall.position = pt + Vector2(0, 10)
		wall.scale = Vector2(0.45, 0.38)
		walls_group.add_child(wall)

		var edge := Sprite2D.new()
		edge.texture = load(RETAINING_EDGE) as Texture2D
		edge.position = pt + Vector2(0, 2)
		edge.scale = Vector2(0.48, 0.35)
		walls_group.add_child(edge)

	for lamp_x in [-200, -380, -560, -700]:
		_build_cais_lamp(root, Vector2(lamp_x, 112))

	# -------------------------------------------------------------------------
	# 6. ACAMPAMENTO AVANÇADO DE CATADORES GOBLINS (Ponto inicial da Chapada)
	# -------------------------------------------------------------------------
	_place_goblin_camp(cliffs_group, root, Vector2(-1650, -850))

	# -------------------------------------------------------------------------
	# 7. ESCADARIAS NATURAIS DE ARENITO (Subidas transitáveis para a Chapada)
	# -------------------------------------------------------------------------
	var stairs_data: Array[Dictionary] = [
		{"pos": Vector2(-1050, 15),   "scale": Vector2(0.52, 0.48), "rot": 0.02,  "flip": false},
		{"pos": Vector2(-4820, -535), "scale": Vector2(0.60, 0.54), "rot": -0.04, "flip": true},
		{"pos": Vector2(-8250, -820), "scale": Vector2(0.65, 0.58), "rot": 0.03,  "flip": false},
		{"pos": Vector2(-12200, -1000),"scale": Vector2(0.70, 0.62), "rot": -0.03, "flip": true},
		{"pos": Vector2(-15400, -1180),"scale": Vector2(0.75, 0.66), "rot": 0.02,  "flip": false}
	]
	for s_info in stairs_data:
		_place_stairs(stairs_group, root, s_info["pos"], s_info["scale"], s_info["rot"], s_info["flip"])

	# -------------------------------------------------------------------------
	# 8. SÍTIOS ARQUEOLÓGICOS ISOLADOS (Lajes semi-soterradas pelo vento)
	# -------------------------------------------------------------------------
	var ruins_data: Array[Dictionary] = [
		{"pos": Vector2(-6200, -1150),  "scale": Vector2(0.68, 0.62), "rot": 0.03,  "flip": false},
		{"pos": Vector2(-10800, -1450), "scale": Vector2(0.82, 0.74), "rot": -0.02, "flip": true}
	]
	for r_info in ruins_data:
		_place_khemet_ruins(ruins_group, root, r_info["pos"], r_info["scale"], r_info["rot"], r_info["flip"])

	# -------------------------------------------------------------------------
	# 9. OBELISCO MONUMENTAL TOMBADO DE KHEMET-RA (Marco Solitário no Deserto)
	# -------------------------------------------------------------------------
	_place_khemet_obelisk(cliffs_group, root, Vector2(-6700, -1250), Vector2(0.72, 0.68), 0.02)

	# -------------------------------------------------------------------------
	# 9B. RELEVO GEOLÓGICO NATURAL DO DESERTO: CRISTAS DE DUNAS & VALES
	# -------------------------------------------------------------------------
	var dune_ridges: Array[Dictionary] = [
		{"pos": Vector2(-9500, -1700),  "scale": Vector2(1.15, 0.95), "rot": 0.04,  "flip": false},
		{"pos": Vector2(-11100, -1850), "scale": Vector2(1.20, 1.00), "rot": -0.03, "flip": true},
		{"pos": Vector2(-12500, -1950), "scale": Vector2(1.30, 1.05), "rot": 0.02,  "flip": false},
		{"pos": Vector2(-13900, -1900), "scale": Vector2(1.25, 1.00), "rot": -0.04, "flip": true},
		{"pos": Vector2(-15300, -1650), "scale": Vector2(1.35, 1.10), "rot": 0.03,  "flip": false},
		{"pos": Vector2(-16500, -1600), "scale": Vector2(1.40, 1.15), "rot": -0.02, "flip": true},
		{"pos": Vector2(-17300, -1900), "scale": Vector2(1.45, 1.15), "rot": 0.04,  "flip": false}
	]
	for d_info in dune_ridges:
		_place_dune_ridge(dunes_layer, d_info["pos"], d_info["scale"], d_info["rot"], d_info["flip"])

	var dune_valleys: Array[Dictionary] = [
		{"pos": Vector2(-10200, -1450), "scale": Vector2(1.10, 0.90), "rot": 0.02,  "flip": false},
		{"pos": Vector2(-11600, -1520), "scale": Vector2(1.15, 0.95), "rot": -0.03, "flip": true},
		{"pos": Vector2(-13000, -1450), "scale": Vector2(1.20, 0.95), "rot": 0.01,  "flip": false},
		{"pos": Vector2(-14400, -1560), "scale": Vector2(1.25, 1.00), "rot": -0.02, "flip": true},
		{"pos": Vector2(-16100, -1950), "scale": Vector2(1.30, 1.05), "rot": 0.03,  "flip": false}
	]
	for v_info in dune_valleys:
		_place_dune_valley(dunes_layer, v_info["pos"], v_info["scale"], v_info["rot"], v_info["flip"])

	# -------------------------------------------------------------------------
	# 9C. MESAS DE ARENITO & PAREDÕES DE CÂNION (ELEVAÇÃO GEOLÓGICA)
	# -------------------------------------------------------------------------
	var mesas_data: Array[Dictionary] = [
		{"pos": Vector2(-9800, -2200),  "scale": Vector2(1.15, 0.95), "rot": -0.02, "flip": false},
		{"pos": Vector2(-12200, -2350), "scale": Vector2(1.25, 1.05), "rot": 0.03,  "flip": true},
		{"pos": Vector2(-14800, -2400), "scale": Vector2(1.30, 1.10), "rot": -0.02, "flip": false},
		{"pos": Vector2(-16700, -2380), "scale": Vector2(1.35, 1.15), "rot": 0.02,  "flip": true}
	]
	for m_data in mesas_data:
		_place_mesa_butte(cliffs_group, root, m_data["pos"], m_data["scale"], m_data["rot"], m_data["flip"])

	var canyon_walls: Array[Dictionary] = [
		{"pos": Vector2(-11000, -2100), "scale": Vector2(1.05, 0.95), "rot": -0.02, "flip": false},
		{"pos": Vector2(-13500, -2180), "scale": Vector2(1.10, 0.98), "rot": 0.03,  "flip": true},
		{"pos": Vector2(-15600, -2250), "scale": Vector2(1.15, 1.00), "rot": -0.01, "flip": false},
		{"pos": Vector2(-17200, -2250), "scale": Vector2(1.20, 1.05), "rot": 0.02,  "flip": true}
	]
	for cw_data in canyon_walls:
		_place_canyon_wall(cliffs_group, root, cw_data["pos"], cw_data["scale"], cw_data["rot"], cw_data["flip"])

	var chasms_data: Array[Dictionary] = [
		{"pos": Vector2(-12600, -1650), "scale": Vector2(0.95, 0.85), "rot": 0.04,  "flip": false},
		{"pos": Vector2(-16100, -1680), "scale": Vector2(1.05, 0.90), "rot": -0.03, "flip": true}
	]
	for ch_data in chasms_data:
		_place_rock_chasm(cliffs_group, root, ch_data["pos"], ch_data["scale"], ch_data["rot"], ch_data["flip"])

	# -------------------------------------------------------------------------
	# 10. MARCO 1: COLOSSO AUTÔMATO SOTERRADO (O Guardião Ancestral na Areia)
	# -------------------------------------------------------------------------
	_place_khemet_colossus(cliffs_group, root, Vector2(-10400, -1480), Vector2(0.85, 0.80))

	# -------------------------------------------------------------------------
	# 11. MARCO 2: POÇO DE MEMÓRIA SOLAR (Santuário Místico Isolado nas Dunas)
	# -------------------------------------------------------------------------
	_place_khemet_memory_well(cliffs_group, root, Vector2(-11800, -1550), Vector2(0.92, 0.92))

	# -------------------------------------------------------------------------
	# 12. MARCO 3: A GRANDE ESFINGE GUARDIÃ (Escultura Colossal Solitária na Rocha)
	# -------------------------------------------------------------------------
	_place_khemet_sphinx(cliffs_group, root, Vector2(-13200, -1460), Vector2(0.95, 0.88), false)

	# -------------------------------------------------------------------------
	# 13. MARCO 4: O PILONE / PORTAL MONUMENTAL DO TEMPLO (Limiar Ciclópico)
	# -------------------------------------------------------------------------
	_place_khemet_temple_gate(cliffs_group, root, Vector2(-14600, -1580), Vector2(1.05, 0.98))

	# -------------------------------------------------------------------------
	# 14. MARCO 5: A RAMPA DA NECRÓPOLE SUBTERRÂNEA (Descida Sombria na Falésia)
	# -------------------------------------------------------------------------
	_place_khemet_necropolis_ramp(cliffs_group, root, Vector2(-15800, -2100), Vector2(0.95, 0.90))

	# -------------------------------------------------------------------------
	# 15. MARCO 6: A GRANDE PIRÂMIDE PRECURSORA SOTERRADA (O Ápice do Horizonte)
	# -------------------------------------------------------------------------
	_place_khemet_great_pyramid(cliffs_group, root, Vector2(-17000, -2020), Vector2(1.35, 1.25))

	# -------------------------------------------------------------------------
	# 16. MONÓLITOS E PILARES DE ARENITO (Marcos geográficos na Chapada)
	# -------------------------------------------------------------------------
	var monolith_data: Array[Dictionary] = [
		{"pos": Vector2(-2400, -1350),  "scale": Vector2(0.55, 0.50), "rot": -0.02, "flip": false},
		{"pos": Vector2(-5800, -1500),  "scale": Vector2(0.62, 0.56), "rot": 0.03,  "flip": true},
		{"pos": Vector2(-9100, -1650),  "scale": Vector2(0.68, 0.60), "rot": -0.04, "flip": false},
		{"pos": Vector2(-12400, -1750), "scale": Vector2(0.75, 0.65), "rot": 0.02,  "flip": true},
		{"pos": Vector2(-14100, -1880), "scale": Vector2(0.78, 0.68), "rot": -0.03, "flip": false},
		{"pos": Vector2(-16900, -1720), "scale": Vector2(0.82, 0.70), "rot": 0.04,  "flip": true}
	]
	for m_info in monolith_data:
		_place_monolith(cliffs_group, root, m_info["pos"], m_info["scale"], m_info["rot"], m_info["flip"])

	# -------------------------------------------------------------------------
	# 17. GRUTA NATURAL DE ARENITO NA FALÉSIA
	# -------------------------------------------------------------------------
	_place_cave(cliffs_group, root, Vector2(-3200, -420), Vector2(0.58, 0.52))

	# -------------------------------------------------------------------------
	# 18. MACIÇOS E FALÉSIAS DE ARENITO (Escarpa Sul da Chapada)
	# -------------------------------------------------------------------------
	var ruined_rocks: Array[Dictionary] = [
		{"pos": Vector2(-780, 110), "scale": Vector2(0.32, 0.30), "rot": 0.08, "flip": false},
		{"pos": Vector2(-860, 95),  "scale": Vector2(0.36, 0.32), "rot": -0.12, "flip": true},
		{"pos": Vector2(-940, 75),  "scale": Vector2(0.40, 0.36), "rot": 0.14, "flip": false},
		{"pos": Vector2(-1030, 45), "scale": Vector2(0.44, 0.38), "rot": -0.08, "flip": true}
	]
	for data in ruined_rocks:
		_place_rock(cliffs_group, root, RED_ROCKS_CLUSTER, "", data["pos"], data["scale"], data["rot"], data["flip"], Vector2(100, 45))

	var red_cliff_clusters: Array[Dictionary] = [
		{"pos": Vector2(-1180, -50),  "scale": Vector2(0.46, 0.42), "rot": 0.18,  "flip": false},
		{"pos": Vector2(-1380, -120), "scale": Vector2(0.50, 0.44), "rot": -0.10, "flip": true},
		{"pos": Vector2(-1580, -180), "scale": Vector2(0.52, 0.46), "rot": 0.15,  "flip": false},
		{"pos": Vector2(-1800, -240), "scale": Vector2(0.48, 0.42), "rot": -0.12, "flip": true},
		{"pos": Vector2(-2050, -300), "scale": Vector2(0.54, 0.48), "rot": 0.08,  "flip": false}
	]
	for data in red_cliff_clusters:
		_place_rock(cliffs_group, root, RED_CLIFF_EDGE, "", data["pos"], data["scale"], data["rot"], data["flip"], Vector2(160, 60))

	var ocher_promontories: Array[Dictionary] = [
		{"pos": Vector2(-3400, -420), "scale": Vector2(0.56, 0.50), "rot": 0.06,  "flip": false, "tex": YELLOW_CLIFF, "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-3680, -450), "scale": Vector2(0.60, 0.52), "rot": -0.05, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-3950, -480), "scale": Vector2(0.58, 0.50), "rot": 0.04,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-4320, -530), "scale": Vector2(0.64, 0.54), "rot": -0.06, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-4580, -550), "scale": Vector2(0.60, 0.52), "rot": 0.05,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-4950, -600), "scale": Vector2(0.62, 0.52), "rot": -0.08, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD}
	]
	for data in ocher_promontories:
		_place_rock(cliffs_group, root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(280, 75))

	var maresia_promontories: Array[Dictionary] = [
		{"pos": Vector2(-6900, -720), "scale": Vector2(0.62, 0.52), "rot": 0.07,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-7250, -760), "scale": Vector2(0.58, 0.48), "rot": -0.06, "flip": true,  "tex": YELLOW_CLIFF, "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-7550, -780), "scale": Vector2(0.62, 0.52), "rot": 0.05,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-7980, -820), "scale": Vector2(0.60, 0.50), "rot": -0.08, "flip": true,  "tex": YELLOW_CLIFF, "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-8380, -860), "scale": Vector2(0.66, 0.56), "rot": 0.06,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD}
	]
	for data in maresia_promontories:
		_place_rock(cliffs_group, root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(300, 80))

	var cape_promontories: Array[Dictionary] = [
		{"pos": Vector2(-11300, -960),  "scale": Vector2(0.68, 0.58), "rot": 0.05,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-11750, -1000), "scale": Vector2(0.72, 0.60), "rot": -0.04, "flip": true,  "tex": CHAPADA_CANYON_WALL, "shd": CHAPADA_CANYON_WALL_SHD},
		{"pos": Vector2(-12100, -1030), "scale": Vector2(0.74, 0.62), "rot": 0.03,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-12650, -1080), "scale": Vector2(0.78, 0.64), "rot": -0.05, "flip": true,  "tex": CHAPADA_CANYON_WALL, "shd": CHAPADA_CANYON_WALL_SHD},
		{"pos": Vector2(-13050, -1120), "scale": Vector2(0.82, 0.66), "rot": 0.04,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-13550, -1140), "scale": Vector2(0.80, 0.65), "rot": -0.04, "flip": true,  "tex": CHAPADA_CANYON_WALL, "shd": CHAPADA_CANYON_WALL_SHD},
		{"pos": Vector2(-14000, -1170), "scale": Vector2(0.84, 0.68), "rot": 0.05,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-14500, -1200), "scale": Vector2(0.82, 0.66), "rot": -0.05, "flip": true,  "tex": CHAPADA_CANYON_WALL, "shd": CHAPADA_CANYON_WALL_SHD},
		{"pos": Vector2(-15100, -1240), "scale": Vector2(0.86, 0.70), "rot": 0.04,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-15900, -1270), "scale": Vector2(0.88, 0.70), "rot": -0.05, "flip": true,  "tex": CHAPADA_CANYON_WALL, "shd": CHAPADA_CANYON_WALL_SHD},
		{"pos": Vector2(-16700, -1300), "scale": Vector2(0.90, 0.72), "rot": 0.05,  "flip": false, "tex": CHAPADA_CLIFF_WALL, "shd": CHAPADA_CLIFF_WALL_SHD},
		{"pos": Vector2(-17400, -1330), "scale": Vector2(0.92, 0.74), "rot": -0.04, "flip": true,  "tex": CHAPADA_CANYON_WALL, "shd": CHAPADA_CANYON_WALL_SHD}
	]
	for data in cape_promontories:
		_place_rock(cliffs_group, root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(340, 90))

	# -------------------------------------------------------------------------
	# 19. ARRECIFES MARÍTIMOS NA ÁGUA (QUEBRA-MAR COSTEIRO DENSO E AQUECIDO)
	# -------------------------------------------------------------------------
	var reef_assets: Array[Dictionary] = [
		{"tex": COASTAL_REEF,       "shd": COASTAL_REEF_SHD,       "base_scale": 0.44},
		{"tex": BEACH_BOULDERS,     "shd": BEACH_BOULDERS_SHD,     "base_scale": 0.42},
		{"tex": RED_ROCKS_CLUSTER,  "shd": "",                     "base_scale": 0.40}
	]

	for x in range(-750, -18200, -85):
		var y_tide: float = get_tide_y_at(float(x))
		var soil_col: Color = get_soil_color_at(float(x))
		var step_idx: int = abs(x / 85)
		var asset_idx: int = step_idx % reef_assets.size()
		var r_data: Dictionary = reef_assets[asset_idx]
		var flip_h: bool = (step_idx % 2 == 1)
		
		var t_dist: float = clampf((-x - 750.0) / 17000.0, 0.0, 1.0)
		var scl_factor: float = r_data["base_scale"] * (0.90 + sin(float(x) * 0.02) * 0.18 + t_dist * 0.12)
		var pos := Vector2(float(x) + cos(float(x) * 0.03) * 16.0, y_tide + 12.0 + sin(float(x) * 0.025) * 8.0)
		var rot: float = sin(float(x) * 0.015) * 0.16
		
		# Sombra da rocha na água
		if r_data["shd"] != "":
			var shd := Sprite2D.new()
			shd.texture = load(r_data["shd"]) as Texture2D
			shd.position = pos + Vector2(6, 12)
			shd.scale = Vector2(scl_factor, scl_factor * 0.85)
			shd.rotation = rot
			shd.modulate = Color(0.90, 0.70, 0.50, 0.35)
			shd.z_index = -1
			water_shallows.add_child(shd)

		# Rocha do recife aquecida para tons minerais de arenito (harmonia com Khemet-Ra)
		var rock := Sprite2D.new()
		rock.texture = load(r_data["tex"]) as Texture2D
		rock.position = pos
		rock.scale = Vector2(scl_factor * (-1.0 if flip_h else 1.0), scl_factor * 0.85)
		rock.rotation = rot
		rock.modulate = Color(soil_col.r * 1.05, soil_col.g * 0.95, soil_col.b * 0.85, 1.0)
		rock.z_index = 0
		water_shallows.add_child(rock)

		_build_rock_collision(root, pos + Vector2(0, 5), Vector2(190, 40) * scl_factor)

		# Linha de arrebentação secundária / ilhotas projetadas no mar
		if (step_idx % 2 == 0):
			var islet_x: float = float(x) + 40.0 + sin(float(x) * 0.03) * 20.0
			var islet_y: float = y_tide + 75.0 + sin(float(x) * 0.02) * 25.0
			var sub_asset: Dictionary = reef_assets[(asset_idx + 1) % reef_assets.size()]
			var sub_scl: float = sub_asset["base_scale"] * 0.75
			
			var islet := Sprite2D.new()
			islet.texture = load(sub_asset["tex"]) as Texture2D
			islet.position = Vector2(islet_x, islet_y)
			islet.scale = Vector2(sub_scl * (1.0 if not flip_h else -1.0), sub_scl * 0.80)
			islet.rotation = -0.10 + cos(float(x) * 0.02) * 0.12
			islet.modulate = Color(soil_col.r * 1.02, soil_col.g * 0.94, soil_col.b * 0.84, 0.95)
			islet.z_index = 0
			water_shallows.add_child(islet)

	# -------------------------------------------------------------------------
	# 20. EXPANSÃO DO OCEANO & POLÍGONOS DE COLISÃO DO CONTINENTE
	# -------------------------------------------------------------------------
	_update_waterline_and_barrier(world)

func _place_small_stone(parent: Node2D, tex_path: String, shd_path: String, pos: Vector2, scale: Vector2, rot: float, tint: Color) -> void:
	if shd_path != "":
		var shd := Sprite2D.new()
		shd.texture = load(shd_path) as Texture2D
		shd.position = pos + Vector2(4.0, 6.0)
		shd.scale = Vector2(absf(scale.x), scale.y)
		shd.rotation = rot
		shd.modulate = Color(0.90, 0.70, 0.50, 0.35)
		shd.z_index = -1
		parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(tex_path) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.rotation = rot
	spr.modulate = Color(tint.r, tint.g, tint.b, 1.0)
	parent.add_child(spr)

func _place_desert_veg(parent: Node2D, pos: Vector2, scale: Vector2) -> void:
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_DESERT_VEG_SHD) as Texture2D
	shd.position = pos + Vector2(6.0, 8.0)
	shd.scale = Vector2(absf(scale.x), scale.y)
	shd.modulate = Color(0.90, 0.70, 0.50, 0.35)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_DESERT_VEG) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.modulate = Color(soil_col.r * 1.05, soil_col.g * 0.98, soil_col.b * 0.88, 1.0)
	parent.add_child(spr)

func _place_rock(parent: Node2D, col_root: Node2D, tex_path: String, shd_path: String, pos: Vector2, scale: Vector2, rot: float, flip: bool, col_size: Vector2) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	if shd_path != "":
		var shd := Sprite2D.new()
		shd.texture = load(shd_path) as Texture2D
		shd.position = pos + Vector2(10.0, 16.0)
		shd.scale = Vector2(absf(final_scale.x), final_scale.y)
		shd.rotation = rot
		shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
		shd.z_index = -1
		parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(tex_path) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(0.0, 20.0) * scale.y, col_size * absf(scale.x))

func _place_stairs(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_ROCK_STAIRS_SHD) as Texture2D
	shd.position = pos + Vector2(8.0, 12.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_ROCK_STAIRS) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

func _place_khemet_ruins(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_RUINS_SLAB_SHD) as Texture2D
	shd.position = pos + Vector2(10.0, 14.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_RUINS_SLAB) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 0.95)
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(final_scale.x * 220.0, -final_scale.y * 60.0), Vector2(90, 80) * absf(scale.x))

func _place_khemet_obelisk(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float) -> void:
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_OBELISK_SHD) as Texture2D
	shd.position = pos + Vector2(14.0, 20.0)
	shd.scale = scale
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_OBELISK) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(120.0, 10.0) * scale.x, Vector2(380, 80) * scale.x)

func _place_khemet_colossus(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2) -> void:
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_COLOSSUS_SHD) as Texture2D
	shd.position = pos + Vector2(14.0, 20.0)
	shd.scale = scale
	shd.modulate = Color(0.90, 0.70, 0.50, 0.45)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_COLOSSUS) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	var light := PointLight2D.new()
	light.texture = load(LIGHT_TEX) as Texture2D
	light.position = pos + Vector2(-40, -110) * scale.y
	light.color = Color(0.2, 0.65, 1.0, 0.85)
	light.energy = 0.8
	light.texture_scale = 0.65
	parent.add_child(light)

	_build_rock_collision(col_root, pos + Vector2(0, 30.0) * scale.y, Vector2(280, 140) * scale.x)

func _place_khemet_memory_well(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2) -> void:
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_MEMORY_WELL_SHD) as Texture2D
	shd.position = pos + Vector2(18.0, 22.0)
	shd.scale = scale
	shd.modulate = Color(0.90, 0.70, 0.50, 0.45)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_MEMORY_WELL) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	# Luz turquesa mística sobre o espelho d'água sagrado
	var light_water := PointLight2D.new()
	light_water.texture = load(LIGHT_TEX) as Texture2D
	light_water.position = pos + Vector2(0.0, 48.0) * scale.y
	light_water.color = Color(0.25, 0.88, 1.0, 0.95)
	light_water.energy = 1.15
	light_water.texture_scale = 0.90
	parent.add_child(light_water)

	# Luz âmbar/dourada dos raios solares que emanam do fundo do poço
	var light_solar := PointLight2D.new()
	light_solar.texture = load(LIGHT_TEX) as Texture2D
	light_solar.position = pos + Vector2(0.0, 48.0) * scale.y
	light_solar.color = Color(1.0, 0.85, 0.45, 0.85)
	light_solar.energy = 0.80
	light_solar.texture_scale = 0.70
	parent.add_child(light_solar)

	# 4 Orbes de quartzo azul solar nos pilares cardinais (Norte, Sul, Oeste, Leste)
	var crystal_offsets: Array[Vector2] = [
		Vector2(0, -220),   # Pilar Norte
		Vector2(8, 28),     # Pilar Sul
		Vector2(-215, -112),# Pilar Oeste
		Vector2(235, -112)  # Pilar Leste
	]
	for c_offset in crystal_offsets:
		var c_light := PointLight2D.new()
		c_light.texture = load(LIGHT_TEX) as Texture2D
		c_light.position = pos + Vector2(c_offset.x * scale.x, c_offset.y * scale.y)
		c_light.color = Color(0.22, 0.72, 1.0, 0.95)
		c_light.energy = 0.70
		c_light.texture_scale = 0.50
		parent.add_child(c_light)

	# Colisão física: espelho d'água central profundo
	_build_rock_collision(col_root, pos + Vector2(0.0, 48.0) * scale.y, Vector2(170, 75) * scale.x)
	# Colisão física: bases dos 4 pilares monolíticos de sustentação
	_build_rock_collision(col_root, pos + Vector2(0.0, -180.0) * scale.y, Vector2(60, 40) * scale.x)
	_build_rock_collision(col_root, pos + Vector2(-215.0, -80.0) * scale.y, Vector2(65, 45) * scale.x)
	_build_rock_collision(col_root, pos + Vector2(235.0, -80.0) * scale.y, Vector2(65, 45) * scale.x)
	_build_rock_collision(col_root, pos + Vector2(8.0, 60.0) * scale.y, Vector2(50, 35) * scale.x)

func _place_khemet_sphinx(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, flip: bool = false) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_GUARDIAN_SPHINX_SHD) as Texture2D
	shd.position = pos + Vector2(18.0, 26.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.modulate = Color(0.90, 0.70, 0.50, 0.45)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_GUARDIAN_SPHINX) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	var eye_light := PointLight2D.new()
	eye_light.texture = load(LIGHT_TEX) as Texture2D
	eye_light.position = pos + Vector2(final_scale.x * 240.0, -140.0) * scale.y
	eye_light.color = Color(0.3, 0.75, 1.0, 0.85)
	eye_light.energy = 0.75
	eye_light.texture_scale = 0.55
	parent.add_child(eye_light)

	_build_rock_collision(col_root, pos + Vector2(0, 20.0) * scale.y, Vector2(480, 180) * absf(scale.x))

func _place_khemet_temple_gate(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2) -> void:
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_TEMPLE_GATE_SHD) as Texture2D
	shd.position = pos + Vector2(16.0, 25.0)
	shd.scale = scale
	shd.modulate = Color(0.90, 0.70, 0.50, 0.45)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_TEMPLE_GATE) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	for pylon_side in [-260.0, 260.0]:
		var gate_light := PointLight2D.new()
		gate_light.texture = load(LIGHT_TEX) as Texture2D
		gate_light.position = pos + Vector2(pylon_side * scale.x, -160.0 * scale.y)
		gate_light.color = Color(1.0, 0.80, 0.40, 0.85)
		gate_light.energy = 0.70
		gate_light.texture_scale = 0.60
		parent.add_child(gate_light)

	_build_rock_collision(col_root, pos + Vector2(-280.0 * scale.x, 20.0 * scale.y), Vector2(180, 150) * scale.x)
	_build_rock_collision(col_root, pos + Vector2(280.0 * scale.x, 20.0 * scale.y), Vector2(180, 150) * scale.x)

func _place_khemet_necropolis_ramp(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2) -> void:
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_NECROPOLIS_RAMP_SHD) as Texture2D
	shd.position = pos + Vector2(16.0, 24.0)
	shd.scale = scale
	shd.modulate = Color(0.90, 0.70, 0.50, 0.45)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_NECROPOLIS_RAMP) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	var dark_abyss := PointLight2D.new()
	dark_abyss.texture = load(LIGHT_TEX) as Texture2D
	dark_abyss.position = pos + Vector2(0, 10) * scale.y
	dark_abyss.color = Color(0.15, 0.45, 0.9, 0.7)
	dark_abyss.energy = 0.55
	dark_abyss.texture_scale = 0.65
	parent.add_child(dark_abyss)

	_build_rock_collision(col_root, pos + Vector2(-200.0 * scale.x, 0.0), Vector2(120, 240) * scale.x)
	_build_rock_collision(col_root, pos + Vector2(200.0 * scale.x, 0.0), Vector2(120, 240) * scale.x)

func _place_khemet_great_pyramid(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2) -> void:
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(KHEMET_GREAT_PYRAMID_SHD) as Texture2D
	shd.position = pos + Vector2(20.0, 30.0)
	shd.scale = scale
	shd.modulate = Color(0.90, 0.70, 0.50, 0.45)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(KHEMET_GREAT_PYRAMID) as Texture2D
	spr.position = pos
	spr.scale = scale
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	var apex_beacon := PointLight2D.new()
	apex_beacon.texture = load(LIGHT_TEX) as Texture2D
	apex_beacon.position = pos + Vector2(0, -220.0) * scale.y
	apex_beacon.color = Color(1.0, 0.90, 0.55, 1.0)
	apex_beacon.energy = 1.3
	apex_beacon.texture_scale = 1.10
	parent.add_child(apex_beacon)

	_build_rock_collision(col_root, pos + Vector2(0, 40.0) * scale.y, Vector2(560, 280) * scale.x)

func _place_monolith(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_PILLAR_MONOLITH_SHD) as Texture2D
	shd.position = pos + Vector2(10.0, 16.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_PILLAR_MONOLITH) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(0.0, 30.0) * scale.y, Vector2(110, 80) * absf(scale.x))

func _place_goblin_camp(parent: Node2D, col_root: Node2D, pos: Vector2) -> void:
	var shd := Sprite2D.new()
	shd.texture = load(GOBLIN_EXPEDITION_CAMP_SHD) as Texture2D
	shd.position = pos + Vector2(14.0, 20.0)
	shd.scale = Vector2(0.65, 0.58)
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(GOBLIN_EXPEDITION_CAMP) as Texture2D
	spr.position = pos
	spr.scale = Vector2(0.65, 0.58)
	parent.add_child(spr)

	var campfire_light := PointLight2D.new()
	campfire_light.texture = load(LIGHT_TEX) as Texture2D
	campfire_light.position = pos + Vector2(15, 10)
	campfire_light.color = Color(1.0, 0.55, 0.15, 0.95)
	campfire_light.energy = 0.9
	campfire_light.texture_scale = 0.75
	parent.add_child(campfire_light)

	_build_rock_collision(col_root, pos + Vector2(-60, -30), Vector2(120, 70))
	_build_rock_collision(col_root, pos + Vector2(90, 20), Vector2(100, 60))

func _place_cave(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2) -> void:
	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_CAVE_SHD) as Texture2D
	shd.position = pos + Vector2(12.0, 18.0)
	shd.scale = scale
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_CAVE) as Texture2D
	spr.position = pos
	spr.scale = scale
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(-150 * scale.x, 0), Vector2(80, 140) * scale.x)
	_build_rock_collision(col_root, pos + Vector2(150 * scale.x, 0), Vector2(80, 140) * scale.x)

func _build_cais_lamp(root: Node2D, pos: Vector2) -> void:
	var lamp := Sprite2D.new()
	lamp.texture = load(LANTERN_TEX) as Texture2D
	lamp.position = pos
	lamp.scale = Vector2(0.6, 0.6)
	lamp.z_index = 2
	root.add_child(lamp)

	var light := PointLight2D.new()
	light.texture = load(LIGHT_TEX) as Texture2D
	light.position = pos + Vector2(0, -12)
	light.color = Color(1.0, 0.78, 0.45, 0.9)
	light.energy = 0.75
	light.texture_scale = 0.8
	root.add_child(light)

func _build_rock_collision(col_root: Node2D, pos: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	body.position = pos
	body.collision_layer = 1
	body.collision_mask = 0

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = size
	shape.shape = rect
	body.add_child(shape)
	col_root.add_child(body)

func _update_waterline_and_barrier(world: Node2D) -> void:
	var coast_points: Array[Vector2] = []
	for x in range(-19500, -750, 75):
		var y_tide: float = get_tide_y_at(float(x))
		coast_points.append(Vector2(float(x), y_tide))
	
	var east_coast: Array[Vector2] = [
		Vector2(-735, 115), Vector2(-695, 118), Vector2(-635, 120),
		Vector2(-570, 122), Vector2(-505, 122), Vector2(-440, 120),
		Vector2(-375, 120), Vector2(-245, 120),
		Vector2(-180, 120), Vector2(-125, 120), Vector2(-73, 166),
		Vector2(-18, 198),  Vector2(38, 238),   Vector2(94, 284),
		Vector2(138, 335),  Vector2(146, 385),  Vector2(148, 428),
		Vector2(148, 520),  Vector2(130, 610),  Vector2(143, 790),
		Vector2(159, 880),  Vector2(145, 1050),
		Vector2(200, 1250), Vector2(260, 1350), Vector2(290, 1415),
		Vector2(360, 1485), Vector2(395, 1535)
	]
	for pt in east_coast:
		coast_points.append(pt)

	var waterline: Polygon2D = world.get_node_or_null("WestWaterline")
	if waterline:
		var poly := PackedVector2Array()
		for pt in coast_points:
			poly.append(pt)
		poly.append(Vector2(395, 4500))
		poly.append(Vector2(-22000, 4500))
		poly.append(Vector2(-22000, get_tide_y_at(-19500)))
		poly.append(Vector2(-19500, get_tide_y_at(-19500)))
		waterline.polygon = poly

	var barrier: StaticBody2D = world.get_node_or_null("WestCoastalBarrier")
	if barrier:
		for child in barrier.get_children():
			if child is CollisionPolygon2D:
				var poly := PackedVector2Array()
				for pt in coast_points:
					poly.append(pt)
				poly.append(Vector2(395, 4500))
				poly.append(Vector2(-22000, 4500))
				poly.append(Vector2(-22000, get_tide_y_at(-19500)))
				poly.append(Vector2(-19500, get_tide_y_at(-19500)))
				child.polygon = poly
				child.build_mode = CollisionPolygon2D.BUILD_SEGMENTS

	var cais: Node2D = world.get_node_or_null("AltoLixoCais")
	if cais:
		var land_poly: PackedVector2Array = []
		
		# 1. Borda norte do platô superior da Chapada (no topo, Y = -2850):
		land_poly.append(Vector2(360, -2850))
		for x in range(360, -18200, -500):
			land_poly.append(Vector2(float(x), -2850.0))
		land_poly.append(Vector2(-18200, -2850))
		
		# 2. Borda oeste descendo até a linha do mar:
		land_poly.append(Vector2(-18200, get_tide_y_at(-18000) + 20.0))
		
		# 3. Borda sul acompanhando a linha de maré:
		for x in range(-18000, -750, 400):
			var y_tide: float = get_tide_y_at(float(x))
			land_poly.append(Vector2(float(x), y_tide + 20.0))
		
		# 4. Conexão urbana com Alto-Lixo e a cidade:
		var urban_pts: Array[Vector2] = [
			Vector2(-735, 115), Vector2(-440, 120), Vector2(-125, 120),
			Vector2(38, 238), Vector2(148, 435), Vector2(360, 435)
		]
		for pt in urban_pts:
			land_poly.append(pt)
		
		cais.set_meta("land_polygon", land_poly)

func _place_dune_ridge(parent: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_DUNE_RIDGE_SHD) as Texture2D
	shd.position = pos + Vector2(10.0, 14.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_DUNE_RIDGE) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 0.98)
	parent.add_child(spr)

func _place_dune_valley(parent: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_DUNE_VALLEY_SHD) as Texture2D
	shd.position = pos + Vector2(8.0, 12.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.35)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_DUNE_VALLEY) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 0.96)
	parent.add_child(spr)

func _place_canyon_wall(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_CANYON_WALL_SHD) as Texture2D
	shd.position = pos + Vector2(12.0, 20.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_CANYON_WALL) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(0.0, 40.0) * scale.y, Vector2(620, 120) * absf(scale.x))

func _place_mesa_butte(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_MESA_BUTTE_SHD) as Texture2D
	shd.position = pos + Vector2(16.0, 24.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_MESA_BUTTE) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(0.0, 20.0) * scale.y, Vector2(520, 140) * absf(scale.x))

func _place_rock_chasm(parent: Node2D, col_root: Node2D, pos: Vector2, scale: Vector2, rot: float, flip: bool) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)
	var soil_col := get_soil_color_at(pos.x)

	var shd := Sprite2D.new()
	shd.texture = load(CHAPADA_ROCK_CHASM_SHD) as Texture2D
	shd.position = pos + Vector2(10.0, 16.0)
	shd.scale = Vector2(absf(final_scale.x), final_scale.y)
	shd.rotation = rot
	shd.modulate = Color(0.90, 0.70, 0.50, 0.40)
	shd.z_index = -1
	parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(CHAPADA_ROCK_CHASM) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(soil_col.r, soil_col.g, soil_col.b, 1.0)
	parent.add_child(spr)

	_build_rock_collision(col_root, pos + Vector2(0.0, 0.0), Vector2(380, 110) * absf(scale.x))
