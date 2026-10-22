extends RefCounted

# =============================================================================
# REGIÃO 2: GRANDE DESERTO DE KHEMET-RA (IMPÉRIO SEPULTADO)
# Arquitetura avançada de terreno do império ancestral a oeste de Sucateia.
# Shader de solo contínuo com dunas eólicas monumentais, micro-ripples de vento,
# cânions de arenito solar esculpido, chapadas e mesas rochosas, vales de caravana
# e talus de seixos de deserto. Zero repetição de malha, zero bordas quadradas.
# Totalmente fiel à lore de "sobre.txt" (Seção 17.11).
# =============================================================================

const DESERT_GROUND_SHADER    := "res://assets/reconstruction/kemet_desert_ground.gdshader"
const SALVAGE_GROUND_TEX      := "res://assets/region/salvage_ground.png"
const BEACH_SAND_PATCH        := "res://assets/reconstruction/areia_praia_litoranea.png"

const YELLOW_CLIFF            := "res://assets/reconstruction/falesia_maritima_amarelada.png"
const YELLOW_CLIFF_SHD        := "res://assets/reconstruction/falesia_maritima_amarelada_sombra.png"
const PROMONTORY_CLIFF        := "res://assets/reconstruction/falesia_promontorio_costeiro.png"
const PROMONTORY_CLIFF_SHD    := "res://assets/reconstruction/falesia_promontorio_costeiro_sombra.png"
const BOULDERS_TEX            := "res://assets/reconstruction/rochedos_praia_maritima.png"
const BOULDERS_SHD            := "res://assets/reconstruction/rochedos_praia_maritima_sombra.png"

const SMALL_ROCKS_MAIN        := "res://assets/reconstruction/pequenas_pedras_solo_costeiro.png"
const SMALL_ROCKS_MAIN_SHD    := "res://assets/reconstruction/pequenas_pedras_solo_costeiro_sombra.png"
const SMALL_ROCKS_A           := "res://assets/reconstruction/pequenas_pedras_var_a.png"
const SMALL_ROCKS_A_SHD       := "res://assets/reconstruction/pequenas_pedras_var_a_sombra.png"
const SMALL_ROCKS_B           := "res://assets/reconstruction/pequenas_pedras_var_b.png"
const SMALL_ROCKS_B_SHD       := "res://assets/reconstruction/pequenas_pedras_var_b_sombra.png"
const SMALL_ROCKS_C           := "res://assets/reconstruction/pequenas_pedras_var_c.png"
const SMALL_ROCKS_C_SHD       := "res://assets/reconstruction/pequenas_pedras_var_c_sombra.png"

func get_tide_y_at(x: float) -> float:
	var t: float = clampf((-x - 700.0) / 12300.0, 0.0, 1.0)
	var base_y: float = 120.0 - t * 950.0
	var wave1: float = sin(x * 0.0018) * 85.0
	var wave2: float = cos(x * 0.0045) * 40.0
	var wave3: float = sin(x * 0.012) * 15.0
	return base_y + wave1 + wave2 + wave3

func install(world: Node2D) -> void:
	if world.has_node("KemetDesertExpansion"):
		world.get_node("KemetDesertExpansion").free()

	var root := Node2D.new()
	root.name = "KemetDesertExpansion"
	root.z_index = 0
	world.add_child(root)

	# -------------------------------------------------------------------------
	# 1. BASE MESH CONTINUA DE SOLO DESÉRTICO (Shader Procedural de Dunas)
	# -------------------------------------------------------------------------
	var base_mesh := Polygon2D.new()
	base_mesh.name = "DesertBaseMesh"
	base_mesh.z_index = -14
	var desert_mat := ShaderMaterial.new()
	desert_mat.shader = load(DESERT_GROUND_SHADER) as Shader
	desert_mat.set_shader_parameter("sand_texture", load(SALVAGE_GROUND_TEX))
	base_mesh.material = desert_mat

	var poly_pts := PackedVector2Array()
	# Topo Norte profundo de Khemet-Ra (Planalto Imperial Superior)
	poly_pts.append(Vector2(-1200, -4600))
	poly_pts.append(Vector2(-16500, -4600))

	# Limite Oeste Extremo
	poly_pts.append(Vector2(-16500, -1250))
	poly_pts.append(Vector2(-14000, -1200))

	# Borda Sul: segue fielmente a linha da maré da praia
	for x in range(-14000, -700, 250):
		var y_t: float = get_tide_y_at(float(x))
		poly_pts.append(Vector2(float(x), y_t + 50.0))

	# Conexão Leste com Sucateia (penetra sob o solo de minério de ferro)
	poly_pts.append(Vector2(-700, 140))
	poly_pts.append(Vector2(-400, 140))
	poly_pts.append(Vector2(-100, 200))
	poly_pts.append(Vector2(360, 200))
	poly_pts.append(Vector2(360, -800))
	poly_pts.append(Vector2(-1200, -800))
	poly_pts.append(Vector2(-1200, -4600))

	base_mesh.polygon = poly_pts
	root.add_child(base_mesh)

	# -------------------------------------------------------------------------
	# 2. DETALHES DE AREIA DOURADA E DEDOS DE DUNA ORGÂNICOS (Esparsos e Variados)
	# -------------------------------------------------------------------------
	var sand_accents := Node2D.new()
	sand_accents.name = "SandDuneAccents"
	sand_accents.z_index = -12
	root.add_child(sand_accents)
	_build_organic_dune_crests(sand_accents)

	# -------------------------------------------------------------------------
	# 3. DETALHES DE CHÃO: SEIXOS, CASCALHO E PEDRAS DE DESERTO (Quebrando o solo)
	# -------------------------------------------------------------------------
	var gravel_group := Node2D.new()
	gravel_group.name = "DesertGravelAndBoulders"
	gravel_group.z_index = -8
	root.add_child(gravel_group)
	_build_gravel_and_talus(gravel_group)

	# -------------------------------------------------------------------------
	# 4. FORMAÇÕES GEOLÓGICAS: CÂNYONS, MESAS E CHAPADAS DE ARENITO (Y-Sorted)
	# -------------------------------------------------------------------------
	var canyons_group := Node2D.new()
	canyons_group.name = "CanyonsAndPlateaus"
	canyons_group.y_sort_enabled = true
	canyons_group.z_index = 1
	root.add_child(canyons_group)
	_build_canyons_and_plateaus(canyons_group, root)

	# -------------------------------------------------------------------------
	# 5. EXPANDIR ÁREA DE CAMINHADA DO JOGADOR
	# -------------------------------------------------------------------------
	_expand_desert_walkability(world)


# -----------------------------------------------------------------------------
# DEDOS DE DUNA E CRISTAS ORGÂNICAS ESPARSAS (SEM REPETIÇÃO DE GRADE)
# -----------------------------------------------------------------------------
func _build_organic_dune_crests(parent: Node2D) -> void:
	var sand_tex: Texture2D = load(BEACH_SAND_PATCH) as Texture2D

	# Posicionamento orgânico curvilíneo ao longo de 4 cordilheiras diagonais principais de duna
	var dune_ridges: Array[Dictionary] = [
		{"start": Vector2(-3600, -800),  "end": Vector2(-5500, -2200), "count": 8, "base_scl": 0.65},
		{"start": Vector2(-6200, -900),  "end": Vector2(-8800, -2600), "count": 9, "base_scl": 0.70},
		{"start": Vector2(-9200, -1100), "end": Vector2(-12200, -3100), "count": 10, "base_scl": 0.75},
		{"start": Vector2(-4500, -2600), "end": Vector2(-9500, -3600), "count": 11, "base_scl": 0.72}
	]

	for ridge in dune_ridges:
		var st: Vector2 = ridge["start"]
		var en: Vector2 = ridge["end"]
		var count: int = ridge["count"]
		var b_scl: float = ridge["base_scl"]

		for i in range(count):
			var frac: float = float(i) / float(count - 1)
			var base_pos: Vector2 = st.lerp(en, frac)
			# Perturbação senoidal orgânica
			var j_x: float = sin(frac * 6.28 + base_pos.x * 0.01) * 75.0
			var j_y: float = cos(frac * 4.5 + base_pos.y * 0.012) * 55.0
			var pos := base_pos + Vector2(j_x, j_y)

			var spr := Sprite2D.new()
			spr.texture = sand_tex
			spr.position = pos
			var scl_x: float = b_scl * (0.85 + sin(frac * 5.0) * 0.20) * (1.0 if i % 2 == 0 else -1.0)
			var scl_y: float = b_scl * 0.78
			spr.scale = Vector2(scl_x, scl_y)
			spr.rotation = 0.22 + sin(frac * 3.14) * 0.15
			# Modulação solar dourada suave para fusão perfeita
			spr.modulate = Color(1.22, 1.04, 0.68, 0.68)
			parent.add_child(spr)


# -----------------------------------------------------------------------------
# CÂNYONS, DESFILADEIROS E CHAPADAS DE ARENITO
# -----------------------------------------------------------------------------
func _build_canyons_and_plateaus(parent: Node2D, col_root: Node2D) -> void:
	# 1. DESFILADEIRO DO SOL POENTE (Cânion Oriental que sobe de Sucateia)
	# Entrada suave em X = -2600 a -3200, Y = -400 a -1500
	var east_canyon_rocks: Array[Dictionary] = [
		{"pos": Vector2(-2350, -450),  "scale": Vector2(0.55, 0.50), "rot": 0.25, "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-2420, -780),  "scale": Vector2(0.58, 0.52), "rot": 0.15, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-2500, -1120), "scale": Vector2(0.62, 0.54), "rot": 0.18, "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-2580, -1450), "scale": Vector2(0.60, 0.50), "rot": 0.10, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		
		# Parede Oeste do Desfiladeiro (corredor livre central largo de 600px)
		{"pos": Vector2(-3080, -550),  "scale": Vector2(0.56, 0.50), "rot": -0.20, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-3160, -900),  "scale": Vector2(0.60, 0.52), "rot": -0.12, "flip": false, "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-3240, -1250), "scale": Vector2(0.64, 0.55), "rot": -0.15, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-3320, -1580), "scale": Vector2(0.62, 0.52), "rot": -0.08, "flip": false, "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD}
	]
	for data in east_canyon_rocks:
		_place_desert_rock(parent, col_root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(280, 75))

	# 2. CÂNYON CENTRAL DE ÂMBAR (Sobe do litoral para o coração das Dunas)
	var amber_canyon_rocks: Array[Dictionary] = [
		{"pos": Vector2(-5300, -720),  "scale": Vector2(0.60, 0.52), "rot": 0.22, "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-5400, -1080), "scale": Vector2(0.62, 0.54), "rot": 0.12, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-5480, -1450), "scale": Vector2(0.66, 0.56), "rot": 0.16, "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-5550, -1820), "scale": Vector2(0.64, 0.52), "rot": 0.08, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},

		{"pos": Vector2(-6180, -780),  "scale": Vector2(0.58, 0.50), "rot": -0.18, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-6280, -1150), "scale": Vector2(0.64, 0.55), "rot": -0.14, "flip": false, "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-6360, -1520), "scale": Vector2(0.68, 0.58), "rot": -0.10, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-6440, -1880), "scale": Vector2(0.65, 0.54), "rot": -0.05, "flip": false, "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD}
	]
	for data in amber_canyon_rocks:
		_place_desert_rock(parent, col_root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(300, 80))

	# 3. A GRANDE MESA DOS REIS ANTIGOS (Platô Central Elevado com degraus)
	var mesa_plateau_rocks: Array[Dictionary] = [
		{"pos": Vector2(-7100, -1950), "scale": Vector2(0.70, 0.60), "rot": 0.05,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-7520, -2050), "scale": Vector2(0.74, 0.62), "rot": -0.06, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-7980, -2100), "scale": Vector2(0.78, 0.64), "rot": 0.04,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-8420, -2080), "scale": Vector2(0.72, 0.60), "rot": -0.08, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-8820, -2000), "scale": Vector2(0.68, 0.58), "rot": 0.10,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},

		{"pos": Vector2(-7320, -2480), "scale": Vector2(0.68, 0.58), "rot": -0.05, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-7780, -2540), "scale": Vector2(0.75, 0.62), "rot": 0.06,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-8280, -2520), "scale": Vector2(0.70, 0.60), "rot": -0.04, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-8680, -2440), "scale": Vector2(0.66, 0.56), "rot": 0.08,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD}
	]
	for data in mesa_plateau_rocks:
		_place_desert_rock(parent, col_root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(320, 85))

	# 4. GARGANTA DOS VENTOS OCIDENTAIS
	var west_gorge_rocks: Array[Dictionary] = [
		{"pos": Vector2(-9450, -1050), "scale": Vector2(0.65, 0.55), "rot": 0.18, "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-9550, -1450), "scale": Vector2(0.70, 0.58), "rot": 0.12, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-9630, -1820), "scale": Vector2(0.72, 0.60), "rot": 0.15, "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-9710, -2180), "scale": Vector2(0.68, 0.56), "rot": 0.08, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},

		{"pos": Vector2(-10320, -1150), "scale": Vector2(0.64, 0.54), "rot": -0.16, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-10420, -1550), "scale": Vector2(0.68, 0.56), "rot": -0.10, "flip": false, "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-10500, -1920), "scale": Vector2(0.74, 0.60), "rot": -0.14, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-10580, -2260), "scale": Vector2(0.70, 0.58), "rot": -0.06, "flip": false, "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD}
	]
	for data in west_gorge_rocks:
		_place_desert_rock(parent, col_root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(310, 80))

	# 5. O GRANDE PLANALTO IMPERIAL SUPERIOR (Norte Profundo de Khemet-Ra)
	var north_imperial_plateau: Array[Dictionary] = [
		{"pos": Vector2(-3600, -3300),  "scale": Vector2(0.72, 0.60), "rot": 0.05,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-4250, -3500),  "scale": Vector2(0.75, 0.62), "rot": -0.04, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-4900, -3650),  "scale": Vector2(0.80, 0.65), "rot": 0.06,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-5600, -3780),  "scale": Vector2(0.78, 0.64), "rot": -0.05, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-6350, -3900),  "scale": Vector2(0.82, 0.66), "rot": 0.08,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-7150, -4000),  "scale": Vector2(0.85, 0.68), "rot": -0.06, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-8050, -4080),  "scale": Vector2(0.88, 0.70), "rot": 0.04,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-9000, -4120),  "scale": Vector2(0.86, 0.68), "rot": -0.07, "flip": true,  "tex": YELLOW_CLIFF,      "shd": YELLOW_CLIFF_SHD},
		{"pos": Vector2(-10000, -4140), "scale": Vector2(0.84, 0.66), "rot": 0.05,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-11050, -4150), "scale": Vector2(0.86, 0.68), "rot": -0.06, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-12150, -4140), "scale": Vector2(0.85, 0.67), "rot": 0.04,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-13250, -4100), "scale": Vector2(0.88, 0.70), "rot": -0.05, "flip": true,  "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD},
		{"pos": Vector2(-14350, -4020), "scale": Vector2(0.90, 0.72), "rot": 0.06,  "flip": false, "tex": PROMONTORY_CLIFF, "shd": PROMONTORY_CLIFF_SHD}
	]
	for data in north_imperial_plateau:
		_place_desert_rock(parent, col_root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(350, 95))

	# 6. ROCHAS EÓLICAS E MONÓLITOS ISOLADOS
	var monoliths: Array[Dictionary] = [
		{"pos": Vector2(-4300, -1250), "scale": Vector2(0.48, 0.42), "rot": 0.12,  "flip": false, "tex": BOULDERS_TEX, "shd": BOULDERS_SHD},
		{"pos": Vector2(-4900, -2100), "scale": Vector2(0.52, 0.45), "rot": -0.08, "flip": true,  "tex": BOULDERS_TEX, "shd": BOULDERS_SHD},
		{"pos": Vector2(-6700, -1350), "scale": Vector2(0.55, 0.46), "rot": 0.15,  "flip": false, "tex": BOULDERS_TEX, "shd": BOULDERS_SHD},
		{"pos": Vector2(-8300, -1200), "scale": Vector2(0.50, 0.44), "rot": -0.14, "flip": true,  "tex": BOULDERS_TEX, "shd": BOULDERS_SHD},
		{"pos": Vector2(-11300, -1650), "scale": Vector2(0.54, 0.46), "rot": 0.10, "flip": false, "tex": BOULDERS_TEX, "shd": BOULDERS_SHD},
		{"pos": Vector2(-12900, -2200), "scale": Vector2(0.58, 0.48), "rot": -0.09, "flip": true,  "tex": BOULDERS_TEX, "shd": BOULDERS_SHD},
		{"pos": Vector2(-13900, -2900), "scale": Vector2(0.62, 0.50), "rot": 0.12, "flip": false, "tex": BOULDERS_TEX, "shd": BOULDERS_SHD}
	]
	for data in monoliths:
		_place_desert_rock(parent, col_root, data["tex"], data["shd"], data["pos"], data["scale"], data["rot"], data["flip"], Vector2(200, 60))


# -----------------------------------------------------------------------------
# SEIXOS, CASCALHO E TALUS DE ARENITO
# -----------------------------------------------------------------------------
func _build_gravel_and_talus(parent: Node2D) -> void:
	var small_stone_assets: Array[Dictionary] = [
		{"tex": SMALL_ROCKS_MAIN, "shd": SMALL_ROCKS_MAIN_SHD, "base_scale": 0.38},
		{"tex": SMALL_ROCKS_A,    "shd": SMALL_ROCKS_A_SHD,    "base_scale": 0.44},
		{"tex": SMALL_ROCKS_B,    "shd": SMALL_ROCKS_B_SHD,    "base_scale": 0.40},
		{"tex": SMALL_ROCKS_C,    "shd": SMALL_ROCKS_C_SHD,    "base_scale": 0.45}
	]

	# Dispersão orgânica de cascalho e seixos nos desfiladeiros e sopés
	for x in range(-2400, -14500, -160):
		var x_val: float = float(x)
		var asset_idx: int = abs(x / 160) % small_stone_assets.size()
		var stone_data: Dictionary = small_stone_assets[asset_idx]

		# Cascalho ao longo da rota imperial oriental
		if x_val > -4800:
			var y_trail: float = lerpf(-480.0, -1900.0, clampf((-x_val - 2400.0) / 2400.0, 0.0, 1.0))
			var pos_t := Vector2(x_val + sin(x_val * 0.025) * 35.0, y_trail + cos(x_val * 0.035) * 25.0)
			_place_desert_stone(parent, stone_data["tex"], stone_data["shd"], pos_t, stone_data["base_scale"] * 0.80, sin(x_val * 0.02) * 0.20, Color(1.22, 0.94, 0.54, 0.95))

		# Seixos e cascalho no sopé das chapadas centrais
		var y_talus: float = -1850.0 + sin(x_val * 0.002) * 120.0
		var pos_talus := Vector2(x_val + 20.0, y_talus + cos(x_val * 0.015) * 15.0)
		var sub_idx: int = (asset_idx + 1) % small_stone_assets.size()
		var sub_stone: Dictionary = small_stone_assets[sub_idx]
		_place_desert_stone(parent, sub_stone["tex"], sub_stone["shd"], pos_talus, sub_stone["base_scale"] * 0.85, cos(x_val * 0.018) * 0.25, Color(1.24, 1.02, 0.60, 0.95))


# -----------------------------------------------------------------------------
# EXPANSÃO DA CAMINHADA DO JOGADOR (LAND POLYGON)
# -----------------------------------------------------------------------------
func _expand_desert_walkability(world: Node2D) -> void:
	var cais: Node2D = world.get_node_or_null("AltoLixoCais")
	if not cais:
		return

	var full_land: PackedVector2Array = []

	# Topo Norte profundo de Khemet-Ra
	full_land.append(Vector2(-1200, -3200))
	for x in range(-1200, -15500, -400):
		var y_north: float = -3850.0 + sin(float(x) * 0.0012) * 150.0
		full_land.append(Vector2(float(x), y_north))

	# Extremo Oeste
	full_land.append(Vector2(-15500, -3850))
	full_land.append(Vector2(-15500, -1200))
	full_land.append(Vector2(-13500, -1180))

	# Linha costeira sul
	for x in range(-13300, -750, 400):
		var y_tide: float = get_tide_y_at(float(x))
		full_land.append(Vector2(float(x), y_tide + 15.0))

	# Cais urbano e leste de Sucateia
	var urban_pts: Array[Vector2] = [
		Vector2(-735, 115), Vector2(-440, 120), Vector2(-125, 120),
		Vector2(38, 238), Vector2(148, 435), Vector2(360, 435),
		Vector2(360, -800), Vector2(-1200, -800), Vector2(-1200, -3200)
	]
	for pt in urban_pts:
		full_land.append(pt)

	cais.set_meta("land_polygon", full_land)


# -----------------------------------------------------------------------------
# HELPERS DE INSTANCIAÇÃO
# -----------------------------------------------------------------------------
func _place_desert_rock(parent: Node2D, col_root: Node2D, tex_path: String, shd_path: String, pos: Vector2, scale: Vector2, rot: float, flip: bool, col_size: Vector2) -> void:
	var final_scale := Vector2(scale.x * (-1.0 if flip else 1.0), scale.y)

	if shd_path != "":
		var shd := Sprite2D.new()
		shd.texture = load(shd_path) as Texture2D
		shd.position = pos + Vector2(10.0, 18.0)
		shd.scale = Vector2(absf(final_scale.x), final_scale.y)
		shd.rotation = rot
		shd.z_index = -1
		parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(tex_path) as Texture2D
	spr.position = pos
	spr.scale = final_scale
	spr.rotation = rot
	spr.modulate = Color(1.08, 1.04, 0.95, 1.0)
	parent.add_child(spr)

	_build_desert_collision(col_root, pos + Vector2(0.0, 15.0), col_size * absf(scale.x))

func _place_desert_stone(parent: Node2D, tex_path: String, shd_path: String, pos: Vector2, scale_val: float, rot: float, tint: Color) -> void:
	if shd_path != "":
		var shd := Sprite2D.new()
		shd.texture = load(shd_path) as Texture2D
		shd.position = pos + Vector2(4.0, 6.0)
		shd.scale = Vector2(scale_val, scale_val)
		shd.rotation = rot
		shd.z_index = -1
		parent.add_child(shd)

	var spr := Sprite2D.new()
	spr.texture = load(tex_path) as Texture2D
	spr.position = pos
	spr.scale = Vector2(scale_val, scale_val)
	spr.rotation = rot
	spr.modulate = tint
	parent.add_child(spr)

func _build_desert_collision(parent: Node2D, pos: Vector2, size: Vector2) -> void:
	var body := StaticBody2D.new()
	body.position = pos
	body.collision_layer = 1
	body.collision_mask = 0

	var shape := CollisionShape2D.new()
	var rect := RectangleShape2D.new()
	rect.size = size
	shape.shape = rect
	body.add_child(shape)
	parent.add_child(body)
