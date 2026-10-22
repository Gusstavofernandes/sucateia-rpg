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
	# 1. TRANSIÇÃO LONGA E EXPANSIVA DE SOLO: TERRA VERMELHA PARA TERRA AMARELADA
	# -------------------------------------------------------------------------
	# Faixa 1: Terra Vermelha Intensa (Alto-Lixo urbano até o litoral de ferro, X: -380 a -1900)
	for x in range(-380, -1950, -90):
		var factor: float = clampf(float(-x - 380) / 1500.0, 0.0, 1.0)
		var y_base: float = 110.0 - factor * 220.0
		var patch := Sprite2D.new()
		patch.texture = load(RED_SOIL_PATCH) as Texture2D
		patch.position = Vector2(float(x), y_base + sin(float(x) * 0.01) * 20.0)
		patch.scale = Vector2(0.45 + factor * 0.15, 0.35 + factor * 0.12)
		patch.rotation = sin(float(x) * 0.02) * 0.15
		patch.modulate = Color(1.0 + factor * 0.25, 0.95 - factor * 0.25, 0.90 - factor * 0.25, 0.50 + factor * 0.40)
		soil_group.add_child(patch)
		
		# Patch secundário mais interno
		var patch_in := Sprite2D.new()
		patch_in.texture = load(RED_SOIL_PATCH) as Texture2D
		patch_in.position = Vector2(float(x) + 30.0, y_base - 70.0)
		patch_in.scale = Vector2(0.40, 0.32)
		patch_in.rotation = -0.10
		patch_in.modulate = Color(1.05 + factor * 0.2, 0.90 - factor * 0.2, 0.85 - factor * 0.2, 0.45 + factor * 0.35)
		soil_group.add_child(patch_in)

	# Faixa 2: Transição Mista / Mesclagem (X: -1800 a -3600)
	# Aqui a terra vermelha se mescla gradualmente com a terra amarelada
	for x in range(-1800, -3650, -110):
		var t: float = clampf(float(-x - 1800) / 1800.0, 0.0, 1.0)
		var y_base: float = -110.0 - t * 240.0
		
		# Patch vermelho atenuando
		var patch_red := Sprite2D.new()
		patch_red.texture = load(RED_SOIL_PATCH) as Texture2D
		patch_red.position = Vector2(float(x) + 25.0, y_base - 15.0)
		patch_red.scale = Vector2(0.55, 0.45)
		patch_red.rotation = 0.08
		patch_red.modulate = Color(1.20 - t * 0.25, 0.75 + t * 0.15, 0.70 + t * 0.15, 0.85 * (1.0 - t * 0.75))
		soil_group.add_child(patch_red)

		# Patch amarelo emergindo e ganhando força
		var patch_yel := Sprite2D.new()
		patch_yel.texture = load(YELLOW_SOIL_PATCH) as Texture2D
		patch_yel.position = Vector2(float(x), y_base + 10.0)
		patch_yel.scale = Vector2(0.55 + t * 0.1, 0.45 + t * 0.08)
		patch_yel.rotation = -0.06
		patch_yel.modulate = Color(1.05 + t * 0.1, 0.95 + t * 0.05, 0.85 + t * 0.05, 0.35 + t * 0.60)
		soil_group.add_child(patch_yel)

	# Faixa 3: O Grande Litoral de Terra Amarelada (X: -3500 a -5800)
	# Pura terra amarelada costeira e areia compactada ao longo de mais de 2.300px
	for x in range(-3500, -5850, -120):
		var t: float = clampf(float(-x - 3500) / 2300.0, 0.0, 1.0)
		var y_base: float = -350.0 - t * 220.0
		
		var patch := Sprite2D.new()
		patch.texture = load(YELLOW_SOIL_PATCH) as Texture2D
		patch.position = Vector2(float(x), y_base + sin(float(x) * 0.012) * 25.0)
		patch.scale = Vector2(0.65, 0.52)
		patch.rotation = sin(float(x) * 0.02) * 0.12
		patch.modulate = Color(1.15, 1.02, 0.88, 0.95)
		soil_group.add_child(patch)

		# Patch secundário interno na base das falésias
		var patch_in := Sprite2D.new()
		patch_in.texture = load(YELLOW_SOIL_PATCH) as Texture2D
		patch_in.position = Vector2(float(x) + 35.0, y_base - 80.0)
		patch_in.scale = Vector2(0.58, 0.46)
		patch_in.rotation = -0.08
		patch_in.modulate = Color(1.12, 1.00, 0.88, 0.90)
		soil_group.add_child(patch_in)

	# -------------------------------------------------------------------------
	# 2. CONTINUIDADE DO CAIS URBANO ATÉ A TRANSIÇÃO (X=-125 até X=-750)
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
	# 3. TRANSIÇÃO: RUÍNA DO CAIS E QUEBRA-MAR ROCHOSO (X=-750 a -1100)
	# -------------------------------------------------------------------------
	var ruined_cais_rocks: Array[Dictionary] = [
		{"pos": Vector2(-770, 112), "scale": Vector2(0.28, 0.28), "rot": 0.08},
		{"pos": Vector2(-835, 102), "scale": Vector2(0.34, 0.30), "rot": -0.10},
		{"pos": Vector2(-905, 88),  "scale": Vector2(0.38, 0.34), "rot": 0.12},
		{"pos": Vector2(-980, 68),  "scale": Vector2(0.42, 0.36), "rot": -0.06},
		{"pos": Vector2(-1055, 42), "scale": Vector2(0.44, 0.38), "rot": 0.15}
	]

	for data in ruined_cais_rocks:
		var rock := Sprite2D.new()
		rock.texture = load(RED_ROCKS_CLUSTER) as Texture2D
		rock.position = data["pos"]
		rock.scale = data["scale"]
		rock.rotation = data["rot"]
		cliffs_group.add_child(rock)
		_build_rock_collision(root, data["pos"], Vector2(95, 42) * data["scale"].x)

	# -------------------------------------------------------------------------
	# 4. FALÉSIAS E ROCHAS VERMELHAS (X=-1100 a X=-2200)
	# -------------------------------------------------------------------------
	var red_cliff_positions: Array[Vector2] = [
		Vector2(-1120, 15), Vector2(-1220, -40), Vector2(-1330, -95),
		Vector2(-1450, -150), Vector2(-1580, -200), Vector2(-1720, -250),
		Vector2(-1860, -290), Vector2(-2010, -330), Vector2(-2160, -370)
	]

	for i in range(red_cliff_positions.size()):
		var pos: Vector2 = red_cliff_positions[i]
		var cliff := Sprite2D.new()
		cliff.texture = load(RED_CLIFF_EDGE) as Texture2D
		cliff.position = pos
		cliff.scale = Vector2(0.48, 0.44)
		cliff.rotation = 0.25 + sin(float(i)) * 0.1
		cliffs_group.add_child(cliff)

		var cluster := Sprite2D.new()
		cluster.texture = load(RED_ROCKS_CLUSTER) as Texture2D
		cluster.position = pos + Vector2(-25, 25)
		cluster.scale = Vector2(0.38, 0.34)
		cluster.rotation = -0.15
		cliffs_group.add_child(cluster)

		_build_rock_collision(root, pos + Vector2(-10, 12), Vector2(135, 48) * 0.48)

	# -------------------------------------------------------------------------
	# 5. TRANSIÇÃO DE FALÉSIAS: MISTURA DE ROCHA VERMELHA E ARENITO AMARELADO (X=-2200 a -3600)
	# -------------------------------------------------------------------------
	for x in range(-2250, -3650, -180):
		var t: float = clampf(float(-x - 2250) / 1400.0, 0.0, 1.0)
		var y_pos: float = -380.0 - t * 140.0
		
		# Falésia amarelada crescendo em dominância
		var shd := Sprite2D.new()
		shd.texture = load(YELLOW_CLIFF_SHD) as Texture2D
		shd.position = Vector2(float(x), y_pos) + Vector2(10, 18)
		shd.scale = Vector2(0.50, 0.45)
		shd.rotation = 0.12 - t * 0.06
		shd.z_index = -1
		cliffs_group.add_child(shd)

		var yel_cliff := Sprite2D.new()
		yel_cliff.texture = load(YELLOW_CLIFF) as Texture2D
		yel_cliff.position = Vector2(float(x), y_pos)
		yel_cliff.scale = Vector2(0.50, 0.45)
		yel_cliff.rotation = 0.12 - t * 0.06
		cliffs_group.add_child(yel_cliff)

		_build_rock_collision(root, Vector2(float(x), y_pos + 15.0), Vector2(260, 65) * 0.50)

	# -------------------------------------------------------------------------
	# 6. O GRANDE LITORAL DE FALÉSIAS AMARELADAS (X=-3600 a -5800)
	# -------------------------------------------------------------------------
	for x in range(-3700, -5850, -210):
		var t: float = clampf(float(-x - 3700) / 2150.0, 0.0, 1.0)
		var y_pos: float = -520.0 - t * 150.0
		
		var shd := Sprite2D.new()
		shd.texture = load(YELLOW_CLIFF_SHD) as Texture2D
		shd.position = Vector2(float(x), y_pos) + Vector2(12, 20)
		shd.scale = Vector2(0.56, 0.50)
		shd.rotation = 0.05 + sin(float(x) * 0.01) * 0.08
		shd.z_index = -1
		cliffs_group.add_child(shd)

		var cliff := Sprite2D.new()
		cliff.texture = load(YELLOW_CLIFF) as Texture2D
		cliff.position = Vector2(float(x), y_pos)
		cliff.scale = Vector2(0.56, 0.50)
		cliff.rotation = 0.05 + sin(float(x) * 0.01) * 0.08
		cliffs_group.add_child(cliff)

		_build_rock_collision(root, Vector2(float(x), y_pos + 18.0), Vector2(280, 70) * 0.56)

	# -------------------------------------------------------------------------
	# 7. RECIFES COSTEIROS E ROCHAS MARÍTIMAS NA ÁGUA AZUL (Orla marítima sul)
	# -------------------------------------------------------------------------
	# Linha contínua de recifes e quebra-mares naturais acompanhando todo o litoral
	for x in range(-1200, -5850, -160):
		var t: float = clampf(float(-x - 1200) / 4600.0, 0.0, 1.0)
		var y_reef: float = 60.0 - t * 620.0 + sin(float(x) * 0.015) * 35.0
		
		var shd := Sprite2D.new()
		shd.texture = load(COASTAL_REEF_SHD) as Texture2D
		shd.position = Vector2(float(x), y_reef) + Vector2(8, 14)
		shd.scale = Vector2(0.44 + t * 0.12, 0.36 + t * 0.08)
		shd.rotation = sin(float(x) * 0.02) * 0.18
		shd.z_index = -14
		water_shallows.add_child(shd)

		var rock := Sprite2D.new()
		rock.texture = load(COASTAL_REEF) as Texture2D
		rock.position = Vector2(float(x), y_reef)
		rock.scale = Vector2(0.44 + t * 0.12, 0.36 + t * 0.08)
		rock.rotation = sin(float(x) * 0.02) * 0.18
		rock.z_index = -12
		water_shallows.add_child(rock)

		# Colisão da orla marítima (impede cair no oceano)
		_build_rock_collision(root, Vector2(float(x), y_reef - 12.0), Vector2(240, 50) * (0.44 + t * 0.12))

		# Ilhotas e rochedos externos ocasionais no oceano azul
		if (x % 320 == 0):
			var islet := Sprite2D.new()
			islet.texture = load(COASTAL_REEF) as Texture2D
			islet.position = Vector2(float(x) + 40.0, y_reef + 90.0)
			islet.scale = Vector2(0.35, 0.28)
			islet.rotation = -0.15
			islet.z_index = -13
			water_shallows.add_child(islet)

	# -------------------------------------------------------------------------
	# 8. EXPANSÃO MASSIVA DO POLÍGONO DE ÁGUA MARÍTIMA E BARREIRAS (Até X=-7500)
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
	# Linha costeira de alta resolução estendida de X=395 até X=-5900
	var coast_points: PackedVector2Array = []
	
	# Ponto extremo do promontório ocidental
	coast_points.append(Vector2(-5900, -780))
	
	# Pontos ao longo do litoral oeste
	for x in range(-5800, -750, 150):
		var t: float = clampf(float(-x - 1200) / 4600.0, 0.0, 1.0)
		var y_reef: float = 60.0 - t * 620.0
		coast_points.append(Vector2(float(x), y_reef))
	
	# Transição e cais urbano a leste
	var east_coast: Array[Vector2] = [
		Vector2(-735, 115), Vector2(-695, 118), Vector2(-635, 120),
		Vector2(-570, 122), Vector2(-505, 122), Vector2(-440, 120),
		Vector2(-375, 120), Vector2(-310, 120), Vector2(-245, 120),
		Vector2(-180, 120), Vector2(-125, 120), Vector2(-73, 166),
		Vector2(-18, 198),  Vector2(38, 238),   Vector2(94, 284),
		Vector2(138, 335),  Vector2(146, 385),  Vector2(148, 428),
		Vector2(148, 520),  Vector2(130, 610),  Vector2(143, 790),
		Vector2(159, 880),  Vector2(145, 1050), Vector2(120, 1160),
		Vector2(200, 1250), Vector2(260, 1350), Vector2(290, 1415),
		Vector2(360, 1485), Vector2(395, 1535)
	]
	for pt in east_coast:
		coast_points.append(pt)

	# Expansão massiva do oceano para cobrir todo o horizonte oeste até X=-7500
	var waterline: Polygon2D = world.get_node_or_null("WestWaterline")
	if waterline:
		var poly := PackedVector2Array()
		for pt in coast_points:
			poly.append(pt)
		poly.append(Vector2(-7500, 3200))
		poly.append(Vector2(-7500, -1800))
		poly.append(Vector2(-5900, -1800))
		waterline.polygon = poly

	var barrier: StaticBody2D = world.get_node_or_null("WestCoastalBarrier")
	if barrier:
		for child in barrier.get_children():
			if child is CollisionPolygon2D:
				var poly := PackedVector2Array()
				for pt in coast_points:
					poly.append(pt)
				poly.append(Vector2(-7500, 3200))
				poly.append(Vector2(-7500, -1800))
				poly.append(Vector2(-5900, -1800))
				child.polygon = poly

	# Polígono de caminhabilidade contínuo de X=360 até X=-5850
	var cais: Node2D = world.get_node_or_null("AltoLixoCais")
	if cais:
		var land_poly: PackedVector2Array = [
			Vector2(-5850, -850),
			Vector2(-4800, -750),
			Vector2(-3800, -620),
			Vector2(-2800, -480),
			Vector2(-1800, -320),
			Vector2(-1200, -180),
			Vector2(-900, 40),
			Vector2(-750, 115),
			Vector2(-635, 120),
			Vector2(-505, 122),
			Vector2(-375, 120),
			Vector2(-245, 120),
			Vector2(-125, 120),
			Vector2(-73, 166),
			Vector2(38, 238),
			Vector2(148, 435),
			Vector2(360, 435),
			Vector2(360, -850),
			Vector2(-5850, -850)
		]
		cais.set_meta("land_polygon", land_poly)
'''

with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
    f.write(code)

print("scripts/world/alto_west_cais.gd grandioso atualizado!")
