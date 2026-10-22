extends RefCounted

const RED_SOIL_PATCH    := "res://assets/reconstruction/red_soil_transition_patch.png"
const RED_ROCKS_CLUSTER := "res://assets/reconstruction/red_iron_rocks_cluster.png"
const RED_CLIFF_EDGE    := "res://assets/reconstruction/red_rock_cliff_edge.png"
const MARKET_DIRT       := "res://assets/terrain/market_dirt.png"
const FOUNDATION_TEX    := "res://assets/terrain/foundation.png"
const METAL_REPAIR      := "res://assets/terrain/metal_repair.png"
const COASTAL_WALL      := "res://assets/infrastructure/coastal_wall.png"
const RETAINING_EDGE    := "res://assets/infrastructure/retaining_edge.png"

# Linha costeira externa que contorna o continente e as rochas pelo mar
const UNIFIED_WEST_COAST: Array[Vector2] = [
	Vector2(-750, 80),
	Vector2(-800, 150),
	Vector2(-850, 260),
	Vector2(-880, 400),
	Vector2(-890, 560),
	Vector2(-890, 720),
	Vector2(-880, 860),
	Vector2(-870, 980),
	Vector2(-850, 1100),
	Vector2(-820, 1220),
	Vector2(-780, 1350),
	Vector2(-720, 1480),
	Vector2(-600, 1580),
	Vector2(-450, 1640),
	Vector2(-200, 1670),
	Vector2(50, 1670),
	Vector2(250, 1630),
	Vector2(395, 1535)
]

func install(world: Node2D) -> void:
	if world.has_node("SucateiaWestGroundExpansion"):
		world.get_node("SucateiaWestGroundExpansion").free()

	# 1. REMOVER MURETAS OBSOLETAS QUE CORTAM O INTERIOR
	_hide_obsolete_interior_walls(world)

	# 2. EXPANDIR CÉLULAS DO TILEMAP DE CHÃO (TerraceFloor) ATÉ AS ROCHAS
	_expand_terrace_floor(world)

	# 3. CRIAR NÓ RAIZ DA EXPANSÃO DO TERRENO
	var root := Node2D.new()
	root.name = "SucateiaWestGroundExpansion"
	root.z_index = -12
	world.add_child(root)

	var ground_layer := Node2D.new()
	ground_layer.name = "RedSoilAndDetails"
	ground_layer.z_index = -11
	root.add_child(ground_layer)

	var edges_layer := Node2D.new()
	edges_layer.name = "CoastalEdgesAndRocks"
	edges_layer.y_sort_enabled = true
	edges_layer.z_index = 0
	root.add_child(edges_layer)

	# 4. PREENCHIMENTO COMPLETO E DENSO DE TERRA VERMELHA ATÉ AS ROCHAS
	_build_dense_red_soil_cover(ground_layer)

	# 5. CONTENÇÃO COSTEIRA EXTERNA E FALÉSIAS APENAS NO LIMITE DO MAR
	_build_outer_coastal_cliffs(edges_layer)

	# 6. BARREIRA FÍSICA EXTERNA
	_build_collision_boundary(root)


# ------------------------------------------------------------------------------
# 1. REMOÇÃO DE MURETAS OBSOLETAS INTERNAS
# ------------------------------------------------------------------------------
func _hide_obsolete_interior_walls(world: Node2D) -> void:
	var quay: Node2D = world.get_node_or_null("GoblinIndustrialQuay")
	if quay:
		for child in quay.get_children():
			if child is Sprite2D:
				if child.position.x >= 95.0 and child.position.x <= 185.0 and child.position.y >= 400.0 and child.position.y <= 1200.0:
					child.visible = false

	var lower: Node2D = world.get_node_or_null("LowerCoastReworked")
	if lower:
		for child in lower.get_children():
			if child is Sprite2D:
				if child.position.x >= 140.0 and child.position.x <= 350.0 and child.position.y >= 1180.0 and child.position.y <= 1500.0:
					child.visible = false


# ------------------------------------------------------------------------------
# 2. EXPANSÃO DO TILEMAP DE CHÃO
# ------------------------------------------------------------------------------
func _expand_terrace_floor(world: Node2D) -> void:
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	if not floor_node:
		return

	# Preenche as células a oeste de x=5 até x=-19 (~ -912 px), e de y=4 até y=34 (~ 1632 px)
	for cx in range(-19, 7):
		for cy in range(4, 35):
			var world_x: float = float(cx * 48 + 24)
			var world_y: float = float(cy * 48 + 24)

			if _is_inside_land(world_x, world_y):
				var atlas_x: int = posmod(cx, 16)
				var atlas_y: int = posmod(cy, 16)
				floor_node.set_cell(Vector2i(cx, cy), 0, Vector2i(atlas_x, atlas_y), 0)


func _is_inside_land(wx: float, wy: float) -> bool:
	if wy < UNIFIED_WEST_COAST[0].y:
		return wx >= -750.0
	if wy > UNIFIED_WEST_COAST[-1].y:
		return wx >= 395.0

	for i in range(UNIFIED_WEST_COAST.size() - 1):
		var p0 := UNIFIED_WEST_COAST[i]
		var p1 := UNIFIED_WEST_COAST[i + 1]
		if (wy >= p0.y and wy <= p1.y) or (wy >= p1.y and wy <= p0.y):
			var dy: float = p1.y - p0.y
			if absf(dy) > 0.001:
				var t: float = (wy - p0.y) / dy
				var coast_x: float = lerpf(p0.x, p1.x, t)
				return wx >= (coast_x - 35.0)
	return wx >= -850.0


# ------------------------------------------------------------------------------
# 3. PREENCHIMENTO DENSO E TOTAL DE TERRA VERMELHADA ATÉ AS ROCHAS
# ------------------------------------------------------------------------------
func _build_dense_red_soil_cover(parent: Node2D) -> void:
	var red_tex := load(RED_SOIL_PATCH) as Texture2D
	var dirt_tex := load(MARKET_DIRT) as Texture2D
	var found_tex := load(FOUNDATION_TEX) as Texture2D
	var metal_tex := load(METAL_REPAIR) as Texture2D

	# Grade ultra-densa (passos de 60px) cobrindo todo o platô até as rochas do sul (Y até 1640)
	for y in range(80, 1640, 60):
		for x in range(-870, 320, 65):
			var pos := Vector2(
				float(x) + sin(float(y) * 0.04 + float(x) * 0.03) * 16.0,
				float(y) + cos(float(x) * 0.04) * 14.0
			)
			if not _is_inside_land(pos.x, pos.y):
				continue

			# Patch primário de terra vermelha densa
			var patch := Sprite2D.new()
			patch.texture = red_tex
			patch.position = pos
			var s: float = 0.58 + sin(float(x * 2 + y) * 0.015) * 0.12
			patch.scale = Vector2(s, s * 0.88)
			patch.rotation = sin(float(x * 3 + y * 2) * 0.02) * 0.28
			# Cor rica de óxido de ferro avermelhado
			patch.modulate = Color(1.06, 0.92, 0.86, 0.88)
			parent.add_child(patch)

			# Na área crítica entre as casas e as rochas (X: -400..300, Y: 800..1580),
			# adicionamos um reforço extra de solo para garantir 100% de preenchimento até a pedra
			if x >= -400 and x <= 300 and y >= 800 and y <= 1580:
				if (x + y) % 90 == 0:
					var patch_extra := Sprite2D.new()
					patch_extra.texture = red_tex
					patch_extra.position = pos + Vector2(25, 20)
					patch_extra.scale = Vector2(s * 1.1, s * 0.95)
					patch_extra.rotation = -patch.rotation
					patch_extra.modulate = Color(1.08, 0.90, 0.84, 0.85)
					parent.add_child(patch_extra)

			# Mesclagem orgânica com poeira e terra de mercado
			if (x + y) % 150 == 0 and dirt_tex:
				var dirt := Sprite2D.new()
				dirt.texture = dirt_tex
				dirt.position = pos + Vector2(18, -12)
				dirt.scale = Vector2(0.62, 0.48)
				dirt.rotation = -0.10
				dirt.modulate = Color(0.96, 0.88, 0.80, 0.52)
				parent.add_child(dirt)

			# Fundações e chapas de reparo de sucata espalhadas de forma natural
			if (x * 7 + y * 11) % 380 < 30 and found_tex:
				var foundation := Sprite2D.new()
				foundation.texture = found_tex
				foundation.position = pos + Vector2(-12, 8)
				foundation.scale = Vector2(0.40, 0.30)
				foundation.modulate = Color(0.86, 0.83, 0.77, 0.65)
				parent.add_child(foundation)

			if (x * 13 + y * 7) % 360 < 28 and metal_tex:
				var metal := Sprite2D.new()
				metal.texture = metal_tex
				metal.position = pos + Vector2(14, 14)
				metal.scale = Vector2(0.35, 0.26)
				metal.rotation = 0.08
				metal.modulate = Color(0.90, 0.88, 0.82, 0.72)
				parent.add_child(metal)


# ------------------------------------------------------------------------------
# 4. CONTENÇÃO COSTEIRA EXTERNA (APENAS NA LINHA DO MAR, SEM CORTAR O CHÃO)
# ------------------------------------------------------------------------------
func _build_outer_coastal_cliffs(parent: Node2D) -> void:
	var wall_tex := load(COASTAL_WALL) as Texture2D
	var edge_tex := load(RETAINING_EDGE) as Texture2D
	var rocks_tex := load(RED_ROCKS_CLUSTER) as Texture2D
	var cliff_tex := load(RED_CLIFF_EDGE) as Texture2D

	for i in range(UNIFIED_WEST_COAST.size() - 1):
		var p0 := UNIFIED_WEST_COAST[i]
		var p1 := UNIFIED_WEST_COAST[i + 1]
		var delta := p1 - p0
		var seg_len := delta.length()
		var seg_angle := delta.angle()
		var steps: int = maxi(1, int(ceil(seg_len / 135.0)))

		for s in range(steps):
			var t: float = (float(s) + 0.5) / float(steps)
			var at := p0.lerp(p1, t)

			# Mureta de contenção contornando a borda externa
			var wall := Sprite2D.new()
			wall.texture = wall_tex
			wall.position = at + Vector2(0, 16)
			wall.scale = Vector2(seg_len / float(steps) / 384.0 * 1.06, 0.40)
			wall.rotation = seg_angle
			wall.modulate = Color(0.92, 0.88, 0.82, 1.0)
			parent.add_child(wall)

			var edge := Sprite2D.new()
			edge.texture = edge_tex
			edge.position = at + Vector2(0, -6)
			edge.scale = Vector2(seg_len / float(steps) / 384.0 * 1.04, 0.32)
			edge.rotation = seg_angle
			edge.modulate = Color(0.96, 0.94, 0.90, 1.0)
			parent.add_child(edge)

			# Rochas na linha da água / base da falésia externa
			if s % 2 == 0 and rocks_tex:
				var rock := Sprite2D.new()
				rock.texture = rocks_tex
				rock.position = at + Vector2(-28, 44)
				var rs: float = 0.42 + sin(float(i + s) * 1.6) * 0.08
				rock.scale = Vector2(rs, rs * 0.88)
				rock.rotation = sin(float(i * 3 + s) * 1.1) * 0.22
				rock.modulate = Color(1.05, 0.92, 0.88, 0.95)
				parent.add_child(rock)

			if s % 3 == 1 and cliff_tex:
				var cliff := Sprite2D.new()
				cliff.texture = cliff_tex
				cliff.position = at + Vector2(-36, 30)
				cliff.scale = Vector2(0.38, 0.32)
				cliff.rotation = seg_angle
				cliff.modulate = Color(1.02, 0.90, 0.85, 0.90)
				parent.add_child(cliff)


# ------------------------------------------------------------------------------
# 5. BARREIRA FÍSICA AO REDOR DA BORDA DO MAR
# ------------------------------------------------------------------------------
func _build_collision_boundary(parent: Node2D) -> void:
	var body := StaticBody2D.new()
	body.name = "SucateiaWestCoastPhysicalBarrier"
	body.collision_layer = 1
	body.collision_mask = 0
	parent.add_child(body)

	for i in range(UNIFIED_WEST_COAST.size() - 1):
		var p0 := UNIFIED_WEST_COAST[i]
		var p1 := UNIFIED_WEST_COAST[i + 1]
		var col := CollisionShape2D.new()
		var seg := SegmentShape2D.new()
		seg.a = p0 + Vector2(-8, 0)
		seg.b = p1 + Vector2(-8, 0)
		col.shape = seg
		body.add_child(col)
