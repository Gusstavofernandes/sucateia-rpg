extends SceneTree

const X0 := 700
const X1 := 2020
const Y0 := -100
const Y1 := 700
const STEP := 40


func _initialize() -> void:
	call_deferred("_run")


func _run() -> void:
	var packed := load("res://maps/sucateia/sucateia.tscn") as PackedScene
	assert(packed != null, "canonical Sucateia scene must load")
	var world := packed.instantiate()
	root.add_child(world)
	await process_frame
	var current_crown := world.get_node_or_null("CoroaDistrict")
	if current_crown:
		current_crown.queue_free()
		await process_frame
	await physics_frame

	var player := world.get_node_or_null("Structures/Player") as CollisionObject2D
	var floor_layers: Array[TileMapLayer] = [
		world.get_node("Ground/TerraceFloor"),
		world.get_node_or_null("MarketDistrict/MarketFloor"),
		world.get_node_or_null("AltoLixoDistrict/AltoFloor"),
		world.get_node_or_null("ForjasRasasDistrict/ForjasFloor"),
	]
	floor_layers = floor_layers.filter(func(layer: TileMapLayer) -> bool: return layer != null)
	var space: PhysicsDirectSpaceState2D = world.get_world_2d().direct_space_state
	var query: PhysicsPointQueryParameters2D = PhysicsPointQueryParameters2D.new()
	query.collide_with_areas = false
	query.collide_with_bodies = true
	query.collision_mask = 0x7fffffff
	if player:
		query.exclude = [player.get_rid()]

	print("COROA_STUDY_ENVELOPE x=", X0, "..", X1, " y=", Y0, "..", Y1, " step=", STEP)
	for y in range(Y0, Y1 + 1, STEP):
		var row := ""
		for x in range(X0, X1 + 1, STEP):
			var point := Vector2(x, y)
			var has_floor := false
			for floor: TileMapLayer in floor_layers:
				if floor.get_cell_source_id(floor.local_to_map(floor.to_local(point))) != -1:
					has_floor = true
					break
			if not has_floor:
				row += " "
				continue
			query.position = point
			var collisions: Array[Dictionary] = space.intersect_point(query, 8)
			if collisions.is_empty() and world.is_surface_walkable(point):
				row += "."
			else:
				row += "#"
		print("Y=", y, " ", row)

	print("CROWN_GROUP_PRESENT=", world.has_node("CoroaDistrict"))
	print("PLAYER=", player.global_position if player else Vector2.INF)
	print("ROOT_ROUTES=", world.get_node_or_null("RouteMarkers").get_child_count() if world.has_node("RouteMarkers") else -1)
	world.queue_free()
	await process_frame
	quit(0)
