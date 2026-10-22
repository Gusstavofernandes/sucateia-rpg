extends RefCounted

const RED_ROCKS_CLUSTER := "res://assets/reconstruction/red_iron_rocks_cluster.png"
const RED_CLIFF_EDGE    := "res://assets/reconstruction/red_rock_cliff_edge.png"
const RED_SOIL_PATCH    := "res://assets/reconstruction/red_soil_transition_patch.png"

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

	var soil_group := Node2D.new()
	soil_group.name = "RedSoilTransition"
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
	cliffs_group.name = "RedCliffsAndRocks"
	cliffs_group.y_sort_enabled = true
	cliffs_group.z_index = 1
	root.add_child(cliffs_group)

	# -------------------------------------------------------------------------
	# 1. TRANSIÇÃO GRADUAL DE TERRA VERMELHA (À medida que se afasta da cidade)
	# -------------------------------------------------------------------------
	# Dégradé suave: sutil perto das casas a leste, intensificando para o oeste
	var soil_coords: Array[Dictionary] = [
		# Transição suave inicial (mais próxima da cidade)
		{"pos": Vector2(-380, 110), "scale": Vector2(0.32, 0.28), "rot": 0.05,  "mod": Color(1.0, 0.95, 0.90, 0.40)},
		{"pos": Vector2(-460, 95),  "scale": Vector2(0.38, 0.32), "rot": -0.06, "mod": Color(1.04, 0.90, 0.84, 0.55)},
		{"pos": Vector2(-540, 80),  "scale": Vector2(0.42, 0.35), "rot": 0.10,  "mod": Color(1.08, 0.86, 0.80, 0.68)},
		{"pos": Vector2(-620, 65),  "scale": Vector2(0.46, 0.38), "rot": -0.08, "mod": Color(1.12, 0.82, 0.76, 0.78)},
		
		# Solo intermediário (zona da abertura rochosa)
		{"pos": Vector2(-720, 45),  "scale": Vector2(0.50, 0.40), "rot": 0.15,  "mod": Color(1.16, 0.78, 0.72, 0.85)},
		{"pos": Vector2(-820, 20),  "scale": Vector2(0.54, 0.42), "rot": -0.10, "mod": Color(1.20, 0.75, 0.70, 0.90)},
		{"pos": Vector2(-920, -20), "scale": Vector2(0.56, 0.44), "rot": 0.08,  "mod": Color(1.24, 0.72, 0.68, 0.92)},

		# Solo profundo avermelhado de óxido e minério (oeste/noroeste extremo)
		{"pos": Vector2(-1020, -70),  "scale": Vector2(0.58, 0.46), "rot": -0.12, "mod": Color(1.26, 0.70, 0.66, 0.95)},
		{"pos": Vector2(-1120, -140), "scale": Vector2(0.60, 0.48), "rot": 0.18,  "mod": Color(1.28, 0.68, 0.65, 0.95)},
		{"pos": Vector2(-1220, -230), "scale": Vector2(0.62, 0.50), "rot": -0.05, "mod": Color(1.30, 0.66, 0.64, 0.95)},
		{"pos": Vector2(-1320, -340), "scale": Vector2(0.64, 0.52), "rot": 0.10,  "mod": Color(1.30, 0.66, 0.64, 0.95)},

		# Viela e terra entre as casas de Alto-Lixo
		{"pos": Vector2(-480, -20),  "scale": Vector2(0.36, 0.30), "rot": 0.20,  "mod": Color(1.06, 0.88, 0.82, 0.50)},
		{"pos": Vector2(-650, -40),  "scale": Vector2(0.44, 0.36), "rot": -0.15, "mod": Color(1.12, 0.82, 0.76, 0.70)},
		{"pos": Vector2(-800, -80),  "scale": Vector2(0.48, 0.38), "rot": 0.05,  "mod": Color(1.18, 0.76, 0.70, 0.80)},
		{"pos": Vector2(-960, -160), "scale": Vector2(0.52, 0.40), "rot": -0.08, "mod": Color(1.24, 0.72, 0.68, 0.88)}
	]

	for data in soil_coords:
		var patch := Sprite2D.new()
		patch.texture = load(RED_SOIL_PATCH) as Texture2D
		patch.position = data["pos"]
		patch.scale = data["scale"]
		patch.rotation = data["rot"]
		patch.modulate = data["mod"]
		soil_group.add_child(patch)

	# -------------------------------------------------------------------------
	# 2. CONTINUIDADE DO CAIS DE PEDRA COMPACTADA (De X=-100 até X=-710)
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

	# Lampiões do cais urbano
	for lamp_x in [-200, -380, -560, -680]:
		_build_cais_lamp(root, Vector2(lamp_x, 112))

	# -------------------------------------------------------------------------
	# 3. TRANSIÇÃO: A PEDRA COMPACTADA DÁ ABERTURA A ROCHAS VERMELHAS (X=-710 a X=-920)
	# -------------------------------------------------------------------------
	# Quebra-mar com pedras vermelhas e mureta que se dissolve
	var trans_points: Array[Dictionary] = [
		{"pos": Vector2(-735, 115), "scale": Vector2(0.24, 0.24), "rot": 0.08},
		{"pos": Vector2(-790, 110), "scale": Vector2(0.30, 0.28), "rot": -0.10},
		{"pos": Vector2(-850, 98),  "scale": Vector2(0.35, 0.32), "rot": 0.12},
		{"pos": Vector2(-915, 80),  "scale": Vector2(0.40, 0.36), "rot": -0.06}
	]

	for data in trans_points:
		var rock := Sprite2D.new()
		rock.texture = load(RED_ROCKS_CLUSTER) as Texture2D
		rock.position = data["pos"]
		rock.scale = data["scale"]
		rock.rotation = data["rot"]
		cliffs_group.add_child(rock)

		_build_rock_collision(root, data["pos"], Vector2(90, 40) * data["scale"].x)

	# -------------------------------------------------------------------------
	# 4. FALÉSIAS E ESCARPAS DE ROCHAS VERMELHAS (X=-920 até X=-1420, noroeste)
	# -------------------------------------------------------------------------
	var cliff_segments: Array[Dictionary] = [
		{"pos": Vector2(-990, 55),    "scale": Vector2(0.40, 0.38), "rot": 0.20},
		{"pos": Vector2(-1070, 0),    "scale": Vector2(0.44, 0.40), "rot": 0.32},
		{"pos": Vector2(-1145, -70),  "scale": Vector2(0.46, 0.42), "rot": 0.38},
		{"pos": Vector2(-1220, -155), "scale": Vector2(0.48, 0.44), "rot": 0.42},
		{"pos": Vector2(-1290, -250), "scale": Vector2(0.50, 0.45), "rot": 0.45},
		{"pos": Vector2(-1355, -355), "scale": Vector2(0.52, 0.46), "rot": 0.40},
		{"pos": Vector2(-1400, -470), "scale": Vector2(0.50, 0.45), "rot": 0.18}
	]

	for seg in cliff_segments:
		var cliff := Sprite2D.new()
		cliff.texture = load(RED_CLIFF_EDGE) as Texture2D
		cliff.position = seg["pos"]
		cliff.scale = seg["scale"]
		cliff.rotation = seg["rot"]
		cliffs_group.add_child(cliff)

		var cluster := Sprite2D.new()
		cluster.texture = load(RED_ROCKS_CLUSTER) as Texture2D
		cluster.position = seg["pos"] + Vector2(-30, 20)
		cluster.scale = seg["scale"] * 0.75
		cluster.rotation = seg["rot"] + 0.12
		cliffs_group.add_child(cluster)

		_build_rock_collision(root, seg["pos"] + Vector2(-18, 8), Vector2(130, 45) * seg["scale"].x)

	# -------------------------------------------------------------------------
	# 5. AJUSTE DO POLÍGONO DE ÁGUA (WestWaterline) E BARREIRAS
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
	var coast_points: PackedVector2Array = [
		Vector2(-1440, -520),
		Vector2(-1400, -470),
		Vector2(-1355, -355),
		Vector2(-1290, -250),
		Vector2(-1220, -155),
		Vector2(-1145, -70),
		Vector2(-1070, 0),
		Vector2(-990, 55),
		Vector2(-915, 80),
		Vector2(-850, 98),
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

	var waterline: Polygon2D = world.get_node_or_null("WestWaterline")
	if waterline:
		var poly := PackedVector2Array()
		for pt in coast_points:
			poly.append(pt)
		poly.append(Vector2(-1800, 2600))
		poly.append(Vector2(-1800, -800))
		poly.append(Vector2(-1440, -800))
		waterline.polygon = poly

	var barrier: StaticBody2D = world.get_node_or_null("WestCoastalBarrier")
	if barrier:
		for child in barrier.get_children():
			if child is CollisionPolygon2D:
				var poly := PackedVector2Array()
				for pt in coast_points:
					poly.append(pt)
				poly.append(Vector2(-1800, 2600))
				poly.append(Vector2(-1800, -800))
				poly.append(Vector2(-1440, -800))
				child.polygon = poly

	var cais: Node2D = world.get_node_or_null("AltoLixoCais")
	if cais:
		var land_poly: PackedVector2Array = [
			Vector2(-1400, -500),
			Vector2(-1300, -250),
			Vector2(-1150, -30),
			Vector2(-980, 50),
			Vector2(-880, 95),
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
			Vector2(360, -500),
			Vector2(-1400, -500)
		]
		cais.set_meta("land_polygon", land_poly)
