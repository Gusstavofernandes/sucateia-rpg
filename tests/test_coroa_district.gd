extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func run() -> void:
	var packed := load("res://maps/sucateia/sucateia.tscn") as PackedScene
	assert(packed != null, "canonical city scene must load")
	var world := packed.instantiate()
	root.add_child(world)
	await process_frame
	await physics_frame
	assert(world.has_node("CoroaDistrict"), "Coroa must be integrated into canonical Sucateia")
	var crown: Node2D = world.get_node("CoroaDistrict")
	assert(crown.get_meta("function", "") == "civic_administration_and_public_arbitration", "Coroa function must remain distinct from market and industry")
	assert(crown.has_node("PublicThreshold") and crown.has_node("Administration") and crown.has_node("Landmark"), "public, administrative and landmark layers must be legible")
	assert(crown.has_node("Landmark/PublicServicesPlaque/ServiceLegend") and crown.has_node("PublicThreshold/BulletinBoard/PublicHearingsAndRegisters"), "civic functions must be signposted at the public entry")
	assert(crown.has_node("Approaches/Market") and crown.has_node("Approaches/Cabos") and crown.has_node("Approaches/Core") and crown.has_node("Approaches/Forjas"), "live approaches need explicit physical endpoints")
	assert(crown.has_node("Utilities") and crown.get_node("Utilities").get_meta("external_cables", 0) == 0 and crown.get_node("Utilities").get_meta("external_pipes", 0) == 0, "do not invent a surface utility source or destination")
	assert(crown.get_node("Utilities").get_meta("local_fixture_maintenance", "") == "municipal_wick_lamplighter", "wick lanterns need a grounded maintenance function")
	for route_name in ["Market", "Cabos", "Core", "Forjas"]:
		var route: Marker2D = crown.get_node("CivicRoutes/" + route_name)
		var points: PackedVector2Array = route.get_meta("points", PackedVector2Array())
		assert(points.size() >= 2 and route.get_meta("clear_width", 0.0) >= 60.0, "each approach needs a wide, traceable public route")
	var player: CharacterBody2D = world.get_node("Structures/Player")
	player.set_physics_process(false)
	var space: PhysicsDirectSpaceState2D = world.get_world_2d().direct_space_state
	var probe := PhysicsShapeQueryParameters2D.new()
	var circle := CircleShape2D.new()
	circle.radius = 11.0
	probe.shape = circle
	probe.collision_mask = 1
	var floor_layers: Array[TileMapLayer] = [world.get_node("Ground/TerraceFloor"), world.get_node_or_null("MarketDistrict/MarketFloor"), world.get_node_or_null("AltoLixoDistrict/AltoFloor"), world.get_node_or_null("ForjasRasasDistrict/ForjasFloor")]
	floor_layers = floor_layers.filter(func(layer: TileMapLayer) -> bool: return layer != null)
	var safe_arrival: Vector2 = crown.get_node("Landmark/SafePublicArrival").global_position
	assert(_has_ground_and_contact_clear(world, floor_layers, space, probe, player, safe_arrival), "public entrance arrival must have grounded, collision-free clearance for the player body")
	for body_path in ["Administration/RegistroAndArbitrationContact", "PublicThreshold/BulletinBoard/BoardGroundContact", "Landmark/TowerFoundationContact", "PublicThreshold/CivicStepsGroundContact"]:
		var contact: StaticBody2D = crown.get_node(body_path)
		assert(contact.get_meta("contact", "") != "", "every civic structure needs an explicit supported ground contact")
		for home in [Vector2(971, 587), Vector2(1260, 591)]:
			assert(contact.global_position.distance_to(home) > 100.0, "new structure must preserve the two catalogued homes")
	var grid := AStarGrid2D.new()
	grid.region = Rect2i(40, 20, 53, 39)
	grid.cell_size = Vector2(24, 24)
	grid.offset = Vector2(12, 12)
	grid.diagonal_mode = AStarGrid2D.DIAGONAL_MODE_NEVER
	grid.update()
	for y in range(grid.region.position.y, grid.region.end.y):
		for x in range(grid.region.position.x, grid.region.end.x):
			var cell := Vector2i(x, y)
			var point := grid.get_point_position(cell)
			var clear: bool = _has_ground_and_contact_clear(world, floor_layers, space, probe, player, point)
			grid.set_point_solid(cell, not clear)
	var market_from: Vector2 = world.get_node("RouteMarkers/Market").global_position
	var cabos_from: Vector2 = world.get_node("RegionPortals/To_cabos").global_position
	var core_from: Vector2 = world.get_node("RouteMarkers/Spawn").global_position
	var forjas_from: Vector2 = world.get_node("RegionPortals/To_forjas").global_position
	var invalid_routes: Array[String] = []
	for link in [["Mercado", market_from, crown.get_node("Approaches/Market").global_position, "Market"], ["Os Cabos", cabos_from, crown.get_node("Approaches/Cabos").global_position, "Cabos"], ["Núcleo", core_from, crown.get_node("Approaches/Core").global_position, "Core"], ["Forjas", forjas_from, crown.get_node("Approaches/Forjas").global_position, "Forjas"]]:
		assert(link[2].distance_to(safe_arrival) <= 1.0, "each transition must land at the signed, collision-free public threshold")
		assert(_walk_both_ways(world, grid, player, link[1], link[2], link[0]), "blocked or one-way civic approach from " + link[0])
		var route: Marker2D = crown.get_node("CivicRoutes/" + link[3])
		var recorded_points: PackedVector2Array = route.get_meta("points")
		assert(recorded_points[-1].distance_to(link[2]) <= 1.0, "route line and named arrival marker must share the same destination")
		if not _recorded_route_has_ground(world, floor_layers, space, probe, player, recorded_points):
			invalid_routes.append(link[0])
	print("UNVERIFIED_RECORDED_APPROACHES ", invalid_routes)
	assert(invalid_routes.is_empty(), "recorded approach paths must remain on supported walkable land")
	assert(crown.get_node("Utilities").get_meta("wick_fixture_count") == 3, "every declared low-energy fixture must be present and maintained")
	print("COROA_DISTRICT PASS grounded_routes=4 bidirectional=4 homes_preserved=2 exposed_utility_lines=0")
	world.queue_free()
	await process_frame
	quit(0)

func _nearest_open_cell(grid: AStarGrid2D, world_point: Vector2) -> Vector2i:
	var origin := Vector2i(roundi((world_point.x - 12.0) / 24.0), roundi((world_point.y - 12.0) / 24.0))
	for radius in range(0, 7):
		for dx in range(-radius, radius + 1):
			for dy in range(-radius, radius + 1):
				if maxi(absi(dx), absi(dy)) != radius:
					continue
				var cell := origin + Vector2i(dx, dy)
				if grid.is_in_boundsv(cell) and not grid.is_point_solid(cell):
					return cell
	return Vector2i(-1, -1)

func _has_ground_and_contact_clear(world: Node2D, floors: Array[TileMapLayer], space: PhysicsDirectSpaceState2D, probe: PhysicsShapeQueryParameters2D, player: CharacterBody2D, point: Vector2) -> bool:
	if not world.is_surface_walkable(point):
		return false
	var supported := false
	for floor: TileMapLayer in floors:
		if floor.get_cell_source_id(floor.local_to_map(floor.to_local(point))) != -1:
			supported = true
			break
	if not supported:
		for district_name in ["CabosDistrict", "DocasDistrict", "PassagemAmarrasDistrict"]:
			var district: Node2D = world.get_node_or_null(district_name)
			if not district:
				continue
			for polygon in district.get_meta("walk_polygons", []):
				if Geometry2D.is_point_in_polygon(point, polygon):
					supported = true
					break
			if supported:
				break
	if not supported:
		return false
	probe.transform = Transform2D(0.0, point)
	probe.exclude = [player.get_rid()]
	var docks: Node2D = world.get_node_or_null("DocasDistrict")
	if docks:
		probe.exclude.append_array(docks.water_exclusions(point))
	return space.intersect_shape(probe, 1).is_empty()

func _recorded_route_has_ground(world: Node2D, floors: Array[TileMapLayer], space: PhysicsDirectSpaceState2D, probe: PhysicsShapeQueryParameters2D, player: CharacterBody2D, points: PackedVector2Array) -> bool:
	for i in range(points.size() - 1):
		var count := maxi(1, ceili(points[i].distance_to(points[i + 1]) / 24.0))
		for step in range(count + 1):
			var point := points[i].lerp(points[i + 1], float(step) / count)
			if not _has_ground_and_contact_clear(world, floors, space, probe, player, point):
				print("UNSUPPORTED_ROUTE_POINT ", point)
				return false
	return true

func _walk_both_ways(world: Node2D, grid: AStarGrid2D, player: CharacterBody2D, start: Vector2, finish: Vector2, label: String) -> bool:
	var a := _nearest_open_cell(grid, start)
	var b := _nearest_open_cell(grid, finish)
	if a.x < 0 or b.x < 0:
		return false
	var path: Array[Vector2i] = grid.get_id_path(a, b)
	if path.is_empty():
		return false
	var cell_points: Array[Vector2] = []
	for cell in path:
		cell_points.append(grid.get_point_position(cell))
	var compressed: PackedVector2Array = _compress_path(cell_points)
	print("SURVEY_ROUTE ", label, " ", compressed)
	player.global_position = cell_points[0]
	for i in range(1, cell_points.size()):
		if player.move_and_collide(cell_points[i] - player.global_position):
			return false
	cell_points.reverse()
	for i in range(1, cell_points.size()):
		if player.move_and_collide(cell_points[i] - player.global_position):
			return false
	return player.global_position.distance_to(grid.get_point_position(a)) < 1.0

func _compress_path(points: Array[Vector2]) -> PackedVector2Array:
	var result := PackedVector2Array()
	if points.is_empty():
		return result
	result.append(points[0])
	var previous_direction := Vector2i.ZERO
	for i in range(1, points.size()):
		var direction := Vector2i(signf(points[i].x - points[i - 1].x), signf(points[i].y - points[i - 1].y))
		if previous_direction != Vector2i.ZERO and direction != previous_direction:
			result.append(points[i - 1])
		previous_direction = direction
	result.append(points[points.size() - 1])
	return result
