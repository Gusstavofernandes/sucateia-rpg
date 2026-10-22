code = '''extends RefCounted

const RED_ROCKS_CLUSTER := "res://assets/reconstruction/red_iron_rocks_cluster.png"
const RED_CLIFF_EDGE    := "res://assets/reconstruction/red_rock_cliff_edge.png"
const RED_SOIL_PATCH    := "res://assets/reconstruction/red_soil_transition_patch.png"
const YELLOW_SOIL_PATCH := "res://assets/reconstruction/yellow_coastal_soil_patch.png"
const YELLOW_CLIFF      := "res://assets/reconstruction/falesia_maritima_amarelada.png"
const YELLOW_CLIFF_SHD  := "res://assets/reconstruction/falesia_maritima_amarelada_sombra.png"
const COASTAL_REEF      := "res://assets/reconstruction/rochas_maritimas_recife_costeiro.png"
const COASTAL_REEF_SHD  := "res://assets/reconstruction/rochas_maritimas_recife_costeiro_sombra.png"

const COASTAL_WALL      := "res://assets/infrastructure/coastal_wall.png"
const RETAINING_EDGE    := "res://assets/infrastructure/retaining_edge.png"
const FOUNDATION_TEX    := "res://assets/terrain/foundation.png"
const WALKWAY_TEX       := "res://assets/infrastructure/walkway.png"
const LANTERN_TEX       := "res://assets/infrastructure/lantern.png"
const LIGHT_TEX         := "res://assets/fx/light.svg"
const SCRAP_TEX         := "res://assets/infrastructure/scrap.png"

func install(world: Node2D) -> void:
	if world.has_node("AltoWestCaisExpansion"):
		world.get_node("AltoWestCaisExpansion").free()

	var root := Node2D.new()
	root.name = "AltoWestCaisExpansion"
	root.z_index = -10
	world.add_child(root)

	var water_shallows := Node2D.new()
	water_shallows.name = "WaterShallowsAndReefs"
	water_shallows.z_index = -15
	root.add_child(water_shallows)

	var soil_group := Node2D.new()
	soil_group.name = "SoilTransition"
	soil_group.z_index = -13
	root.add_child(soil_group)

	var pier_paving := Node2D.new()
	pier_paving.name = "PierPaving"
	pier_paving.z_index = -11
	root.add_child(pier_paving)

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
	# 1. TRANSIÇÃO DE SOLO: TERRA VERMELHA PARA TERRA AMARELADA COSTEIRA
	# -------------------------------------------------------------------------
	# Faixa 1: Terra vermelha (Alto-Lixo urbano até início das rochas, X: -380 a -1100)
	var red_soil_coords: Array[Dictionary] = [
		{"pos": Vector2(-380, 110), "scale": Vector2(0.35, 0.30), "rot": 0.05,  "mod": Color(1.00, 0.95, 0.90, 0.45)},
		{"pos": Vector2(-480, 95),  "scale": Vector2(0.40, 0.34), "rot": -0.06, "mod": Color(1.05, 0.88, 0.82, 0.60)},
		{"pos": Vector2(-580, 85),  "scale": Vector2(0.44, 0.36), "rot": 0.10,  "mod": Color(1.10, 0.84, 0.78, 0.72)},
		{"pos": Vector2(-680, 75),  "scale": Vector2(0.48, 0.38), "rot": -0.08, "mod": Color(1.14, 0.80, 0.74, 0.82)},
		{"pos": Vector2(-780, 50),  "scale": Vector2(0.52, 0.40), "rot": 0.12,  "mod": Color(1.18, 0.76, 0.70, 0.88)},
		{"pos": Vector2(-880, 20),  "scale": Vector2(0.54, 0.42), "rot": -0.10, "mod": Color(1.22, 0.72, 0.68, 0.92)},
		{"pos": Vector2(-980, -20), "scale": Vector2(0.56, 0.44), "rot": 0.08,  "mod": Color(1.24, 0.70, 0.66, 0.94)},
		{"pos": Vector2(-1080, -70),"scale": Vector2(0.58, 0.46), "rot": -0.12, "mod": Color(1.24, 0.70, 0.66, 0.92)},
		{"pos": Vector2(-1180, -130),"scale": Vector2(0.58, 0.46), "rot": 0.15, "mod": Color(1.20, 0.72, 0.68, 0.85)}
	]

	for data in red_soil_coords:
		var patch := Sprite2D.new()
		patch.texture = load(RED_SOIL_PATCH) as Texture2D
		patch.position = data["pos"]
		patch.scale = data["scale"]
		patch.rotation = data["rot"]
		patch.modulate = data["mod"]
		soil_group.add_child(patch)

	# Faixa 2: Terra Amarelada Costeira (X: -1200 até X: -2600 no litoral aberto)
	var yellow_soil_coords: Array[Dictionary] = [
		# Transição inicial onde a terra vermelha se mistura com a terra amarelada
		{"pos": Vector2(-1250, -150), "scale": Vector2(0.55, 0.45), "rot": 0.05,  "mod": Color(1.05, 0.96, 0.85, 0.65)},
		{"pos": Vector2(-1380, -220), "scale": Vector2(0.58, 0.46), "rot": -0.08, "mod": Color(1.08, 0.98, 0.88, 0.78)},
		{"pos": Vector2(-1500, -280), "scale": Vector2(0.60, 0.48), "rot": 0.12,  "mod": Color(1.10, 1.00, 0.90, 0.85)},
		{"pos": Vector2(-1630, -330), "scale": Vector2(0.62, 0.50), "rot": -0.06, "mod": Color(1.12, 1.00, 0.90, 0.90)},
		
		# Litoral marítimo profundo com pura terra amarelada/areia compactada
		{"pos": Vector2(-1780, -380), "scale": Vector2(0.64, 0.52), "rot": 0.10,  "mod": Color(1.12, 1.00, 0.88, 0.95)},
		{"pos": Vector2(-1920, -420), "scale": Vector2(0.65, 0.52), "rot": -0.12, "mod": Color(1.14, 1.02, 0.88, 0.95)},
		{"pos": Vector2(-2080, -450), "scale": Vector2(0.66, 0.54), "rot": 0.08,  "mod": Color(1.14, 1.02, 0.88, 0.95)},
		{"pos": Vector2(-2240, -490), "scale": Vector2(0.68, 0.55), "rot": -0.05, "mod": Color(1.14, 1.02, 0.88, 0.95)},
		{"pos": Vector2(-2400, -530), "scale": Vector2(0.68, 0.55), "rot": 0.14,  "mod": Color(1.15, 1.02, 0.88, 0.95)},
		{"pos": Vector2(-2550, -570), "scale": Vector2(0.70, 0.56), "rot": -0.08, "mod": Color(1.15, 1.02, 0.88, 0.95)},
		
		# Faixa mais interna da trilha costeira
		{"pos": Vector2(-1450, -180), "scale": Vector2(0.55, 0.44), "rot": 0.18,  "mod": Color(1.08, 0.98, 0.88, 0.75)},
		{"pos": Vector2(-1700, -260), "scale": Vector2(0.58, 0.46), "rot": -0.14, "mod": Color(1.12, 1.00, 0.90, 0.85)},
		{"pos": Vector2(-2000, -330), "scale": Vector2(0.62, 0.48), "rot": 0.06,  "mod": Color(1.14, 1.02, 0.88, 0.92)},
		{"pos": Vector2(-2300, -400), "scale": Vector2(0.64, 0.50), "rot": -0.10, "mod": Color(1.14, 1.02, 0.88, 0.92)}
	]

	for data in yellow_soil_coords:
		var patch := Sprite2D.new()
		patch.texture = load(YELLOW_SOIL_PATCH) as Texture2D
		patch.position = data["pos"]
		patch.scale = data["scale"]
		patch.rotation = data["rot"]
		patch.modulate = data["mod"]
		soil_group.add_child(patch)

	# -------------------------------------------------------------------------
	# 2. CONTINUIDADE DO CAIS URBANO ATÉ A TRANSIÇÃO (X=-125 até X=-720)
	# -------------------------------------------------------------------------
	var pier_segments: Array[Vector2] = [
		Vector2(-125, 120), Vector2(-180, 120), Vector2(-245, 120),
		Vector2(-310, 120), Vector2(-375, 120), Vector2(-440, 120),
		Vector2(-505, 122), Vector2(-570, 122), Vector2(-635, 120),
		Vector2(-695, 118)
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

	for lamp_x in [-200, -380, -560, -680]:
		_build_cais_lamp(root, Vector2(lamp_x, 112))

	# -------------------------------------------------------------------------
	# 3. TRANSIÇÃO: QUEBRA-MAR EM RUÍNA E PRIMEIROS ROCHEDOS VERMELHOS (X=-720 a -950)
	# -------------------------------------------------------------------------
	var trans_rocks: Array[Dictionary] = [
		{"pos": Vector2(-735, 115), "scale": Vector2(0.26, 0.26), "rot": 0.08},
		{"pos": Vector2(-795, 108), "scale": Vector2(0.32, 0.30), "rot": -0.10},
		{"pos": Vector2(-860, 96),  "scale": Vector2(0.36, 0.34), "rot": 0.12},
		{"pos": Vector2(-925, 78),  "scale": Vector2(0.40, 0.36), "rot": -0.06}
	]

	for data in trans_rocks:
		var rock := Sprite2D.new()
		rock.texture = load(RED_ROCKS_CLUSTER) as Texture2D
		rock.position = data["pos"]
		rock.scale = data["scale"]
		rock.rotation = data["rot"]
		cliffs_group.add_child(rock)
		_build_rock_collision(root, data["pos"], Vector2(90, 40) * data["scale"].x)

	# -------------------------------------------------------------------------
	# 4. FALÉSIAS E ROCHAS VERMELHAS (X=-950 a X=-1500)
	# -------------------------------------------------------------------------
	var red_cliff_segments: Array[Dictionary] = [
		{"pos": Vector2(-990, 50),    "scale": Vector2(0.42, 0.38), "rot": 0.20},
		{"pos": Vector2(-1070, -5),   "scale": Vector2(0.44, 0.40), "rot": 0.32},
		{"pos": Vector2(-1145, -75),  "scale": Vector2(0.46, 0.42), "rot": 0.38},
		{"pos": Vector2(-1225, -155), "scale": Vector2(0.48, 0.44), "rot": 0.40},
		{"pos": Vector2(-1310, -240), "scale": Vector2(0.50, 0.45), "rot": 0.42},
		{"pos": Vector2(-1400, -320), "scale": Vector2(0.52, 0.46), "rot": 0.36},
		{"pos": Vector2(-1485, -390), "scale": Vector2(0.50, 0.45), "rot": 0.30}
	]

	for seg in red_cliff_segments:
		var cliff := Sprite2D.new()
		cliff.texture = load(RED_CLIFF_EDGE) as Texture2D
		cliff.position = seg["pos"]
		cliff.scale = seg["scale"]
		cliff.rotation = seg["rot"]
		cliffs_group.add_child(cliff)

		var cluster := Sprite2D.new()
		cluster.texture = load(RED_ROCKS_CLUSTER) as Texture2D
		cluster.position = seg["pos"] + Vector2(-25, 20)
		cluster.scale = seg["scale"] * 0.75
		cluster.rotation = seg["rot"] + 0.12
		cliffs_group.add_child(cluster)

		_build_rock_collision(root, seg["pos"] + Vector2(-15, 10), Vector2(130, 45) * seg["scale"].x)

	# -------------------------------------------------------------------------
	# 5. LITORAL MARÍTIMO ABERTO: FALÉSIAS AMARELADAS E ESCARPAS OCRE (X=-1500 a -2700)
	# -------------------------------------------------------------------------
	var yellow_cliff_segments: Array[Dictionary] = [
		# Parede norte da falésia costeira que acompanha a orla
		{"pos": Vector2(-1580, -470), "scale": Vector2(0.48, 0.44), "rot": 0.22},
		{"pos": Vector2(-1720, -520), "scale": Vector2(0.52, 0.46), "rot": 0.15},
		{"pos": Vector2(-1880, -560), "scale": Vector2(0.54, 0.48), "rot": 0.10},
		{"pos": Vector2(-2040, -590), "scale": Vector2(0.55, 0.48), "rot": 0.05},
		{"pos": Vector2(-2200, -620), "scale": Vector2(0.56, 0.50), "rot": 0.08},
		{"pos": Vector2(-2360, -650), "scale": Vector2(0.58, 0.50), "rot": 0.12},
		{"pos": Vector2(-2520, -680), "scale": Vector2(0.60, 0.52), "rot": 0.05},
		{"pos": Vector2(-2660, -710), "scale": Vector2(0.58, 0.50), "rot": -0.05}
	]

	for seg in yellow_cliff_segments:
		var shd := Sprite2D.new()
		shd.texture = load(YELLOW_CLIFF_SHD) as Texture2D
		shd.position = seg["pos"] + Vector2(12, 18)
		shd.scale = seg["scale"]
		shd.rotation = seg["rot"]
		shd.z_index = -1
		cliffs_group.add_child(shd)

		var cliff := Sprite2D.new()
		cliff.texture = load(YELLOW_CLIFF) as Texture2D
		cliff.position = seg["pos"]
		cliff.scale = seg["scale"]
		cliff.rotation = seg["rot"]
		cliffs_group.add_child(cliff)

		# Colisão da falésia para barrar subida ao norte
		_build_rock_collision(root, seg["pos"] + Vector2(0, 15), Vector2(280, 70) * seg["scale"].x)

	# -------------------------------------------------------------------------
	# 6. RECIFES COSTEIROS E ROCHAS MARÍTIMAS NA ÁGUA AZUL (Orla marítima sul)
	# -------------------------------------------------------------------------
	var marine_reefs: Array[Dictionary] = [
		# Recife intermediário (início da água azulada)
		{"pos": Vector2(-1350, -120), "scale": Vector2(0.38, 0.32), "rot": -0.12, "water_depth": 0.75},
		{"pos": Vector2(-1520, -180), "scale": Vector2(0.42, 0.35), "rot": 0.15,  "water_depth": 0.85},
		{"pos": Vector2(-1700, -220), "scale": Vector2(0.45, 0.38), "rot": -0.08, "water_depth": 0.90},
		
		# Grandes recifes e quebra-mares naturais na costa oeste
		{"pos": Vector2(-1880, -260), "scale": Vector2(0.48, 0.40), "rot": 0.10,  "water_depth": 0.95},
		{"pos": Vector2(-2080, -290), "scale": Vector2(0.50, 0.42), "rot": -0.15, "water_depth": 1.00},
		{"pos": Vector2(-2280, -320), "scale": Vector2(0.52, 0.42), "rot": 0.18,  "water_depth": 1.00},
		{"pos": Vector2(-2480, -350), "scale": Vector2(0.54, 0.44), "rot": -0.10, "water_depth": 1.00},
		{"pos": Vector2(-2680, -380), "scale": Vector2(0.56, 0.45), "rot": 0.05,  "water_depth": 1.00},
		
		# Pequenos arrecifes de marola externa (imersos nas águas azuis)
		{"pos": Vector2(-1600, -70),  "scale": Vector2(0.32, 0.28), "rot": 0.25,  "water_depth": 1.00},
		{"pos": Vector2(-1980, -130), "scale": Vector2(0.35, 0.30), "rot": -0.20, "water_depth": 1.00},
		{"pos": Vector2(-2380, -180), "scale": Vector2(0.38, 0.32), "rot": 0.15,  "water_depth": 1.00}
	]

	for reef in marine_reefs:
		var shd := Sprite2D.new()
		shd.texture = load(COASTAL_REEF_SHD) as Texture2D
		shd.position = reef["pos"] + Vector2(8, 14)
		shd.scale = reef["scale"]
		shd.rotation = reef["rot"]
		shd.z_index = -14
		water_shallows.add_child(shd)

		var rock := Sprite2D.new()
		rock.texture = load(COASTAL_REEF) as Texture2D
		rock.position = reef["pos"]
		rock.scale = reef["scale"]
		rock.rotation = reef["rot"]
		rock.z_index = -12
		water_shallows.add_child(rock)

		# Colisão da orla rochosa marítima para impedir que o player caia no mar
		_build_rock_collision(root, reef["pos"] + Vector2(0, -10), Vector2(240, 55) * reef["scale"].x)

	# -------------------------------------------------------------------------
	# 7. EXPANSÃO DO POLÍGONO DE ÁGUA MARÍTIMA (WestWaterline) E BARREIRAS
	# -------------------------------------------------------------------------
	_update_waterline_and_barrier(world)

func _build_cais_lamp(parent: Node2D, pos: Vector2) -> void:
	var node := Node2D.new()
	node.position = pos
	parent.add_child(node)

	var lamp := Sprite2D.new()
	lamp.texture = load(LANTERN_TEX) as Texture2D
	lamp.position = Vector2(0, -18)
	lamp.scale = Vector2(0.18, 0.18)
	node.add_child(lamp)

	var light := PointLight2D.new()
	light.texture = load(LIGHT_TEX) as Texture2D
	light.position = Vector2(0, -18)
	light.color = Color(1.0, 0.78, 0.45, 1.0)
	light.energy = 0.55
	light.texture_scale = 0.65
	node.add_child(light)

func _build_rock_collision(parent: Node2D, pos: Vector2, size: Vector2) -> void:
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

func _update_waterline_and_barrier(world: Node2D) -> void:
	# Linha costeira contínua e expandida para o oeste até X=-2850
	var coast_points: PackedVector2Array = [
		Vector2(-2850, -680),
		Vector2(-2700, -650),
		Vector2(-2500, -600),
		Vector2(-2300, -550),
		Vector2(-2100, -500),
		Vector2(-1900, -450),
		Vector2(-1700, -380),
		Vector2(-1500, -300),
		Vector2(-1380, -220),
		Vector2(-1280, -140),
		Vector2(-1180, -60),
		Vector2(-1080, 0),
		Vector2(-980, 50),
		Vector2(-915, 75),
		Vector2(-850, 95),
		Vector2(-790, 110),
		Vector2(-735, 115),
		Vector2(-695, 118),
		Vector2(-635, 120),
		Vector2(-570, 122),
		Vector2(-505, 122),
		Vector2(-440, 120),
		Vector2(-375, 120),
		Vector2(-310, 120),
		Vector2(-245, 120),
		Vector2(-180, 120),
		Vector2(-125, 120),
		Vector2(-73, 166),
		Vector2(-18, 198),
		Vector2(38, 238),
		Vector2(94, 284),
		Vector2(138, 335),
		Vector2(146, 385),
		Vector2(148, 428),
		Vector2(148, 520),
		Vector2(130, 610),
		Vector2(143, 790),
		Vector2(159, 880),
		Vector2(145, 1050),
		Vector2(120, 1160),
		Vector2(200, 1250),
		Vector2(260, 1350),
		Vector2(290, 1415),
		Vector2(360, 1485),
		Vector2(395, 1535)
	]

	# Polígono de água expandido até X=-3600 (sem corte preto!)
	var waterline: Polygon2D = world.get_node_or_null("WestWaterline")
	if waterline:
		var poly := PackedVector2Array()
		for pt in coast_points:
			poly.append(pt)
		poly.append(Vector2(-3600, 2600))
		poly.append(Vector2(-3600, -1200))
		poly.append(Vector2(-2850, -1200))
		waterline.polygon = poly

	var barrier: StaticBody2D = world.get_node_or_null("WestCoastalBarrier")
	if barrier:
		for child in barrier.get_children():
			if child is CollisionPolygon2D:
				var poly := PackedVector2Array()
				for pt in coast_points:
					poly.append(pt)
				poly.append(Vector2(-3600, 2600))
				poly.append(Vector2(-3600, -1200))
				poly.append(Vector2(-2850, -1200))
				child.polygon = poly

	# Polígono de caminhabilidade do litoral estendido
	var cais: Node2D = world.get_node_or_null("AltoLixoCais")
	if cais:
		var land_poly: PackedVector2Array = [
			Vector2(-2800, -750),
			Vector2(-2600, -700),
			Vector2(-2400, -650),
			Vector2(-2200, -600),
			Vector2(-2000, -550),
			Vector2(-1800, -500),
			Vector2(-1600, -420),
			Vector2(-1400, -320),
			Vector2(-1200, -180),
			Vector2(-1050, -50),
			Vector2(-900, 40),
			Vector2(-765, 115),
			Vector2(-700, 118),
			Vector2(-635, 120),
			Vector2(-570, 122),
			Vector2(-505, 122),
			Vector2(-440, 120),
			Vector2(-375, 120),
			Vector2(-310, 120),
			Vector2(-245, 120),
			Vector2(-180, 120),
			Vector2(-125, 120),
			Vector2(-73, 166),
			Vector2(-18, 198),
			Vector2(38, 238),
			Vector2(94, 284),
			Vector2(138, 335),
			Vector2(146, 385),
			Vector2(148, 435),
			Vector2(360, 435),
			Vector2(360, -750),
			Vector2(-2800, -750)
		]
		cais.set_meta("land_polygon", land_poly)
'''

with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
    f.write(code)

print("scripts/world/alto_west_cais.gd escrito com sucesso!")
