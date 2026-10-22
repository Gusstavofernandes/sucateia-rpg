extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func run() -> void:
	var world: Node2D = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	await physics_frame
	await physics_frame
	
	if not world.has_node("AltoLixoCais"):
		push_error("FAIL: AltoLixoCais node missing in scene")
		quit(1)
		return
	
	var cais: Node2D = world.get_node("AltoLixoCais")
	if not cais.has_meta("land_polygon"):
		push_error("FAIL: AltoLixoCais missing land_polygon metadata")
		quit(1)
		return
		
	var space := world.get_world_2d().direct_space_state
	var circle := CircleShape2D.new()
	circle.radius = 11.0
	var query := PhysicsShapeQueryParameters2D.new()
	query.shape = circle
	query.collision_mask = 1
	
	# 1. Test that water in the ocean is blocked by collision and not walkable
	var water_points := [
		Vector2(-700, 200),
		Vector2(-400, 200),
		Vector2(-200, 250),
		Vector2(-100, 250),
		Vector2(0, 320),
		Vector2(50, 400),
		Vector2(-200, 300)
	]
	for wp in water_points:
		query.transform = Transform2D(0, wp)
		var hits = space.intersect_shape(query, 1)
		assert(not hits.is_empty(), "Water point must be blocked by WestCoastalBarrier: " + str(wp))
		assert(not world.is_walkable(wp), "Water point must not be walkable: " + str(wp))
	print("PASS: Ocean water is solid collision and not walkable.")
	
	# 2. Test that points along the entire unified Cais promenade are walkable and free of collision
	var cais_points := [
		Vector2(-800, 95),
		Vector2(-600, 105),
		Vector2(-440, 105),
		Vector2(-250, 115),
		Vector2(-150, 125),
		Vector2(-100, 140),
		Vector2(-50, 165),
		Vector2(0, 190),
		Vector2(55, 230),
		Vector2(115, 280),
		Vector2(160, 335),
		Vector2(180, 400)
	]
	for cp in cais_points:
		query.transform = Transform2D(0, cp)
		var hits = space.intersect_shape(query, 1)
		assert(hits.is_empty(), "Cais path point must not collide with obstacles: " + str(cp) + " hit: " + str(hits))
		assert(world.is_walkable(cp), "Cais path point must be marked as walkable: " + str(cp))
	print("PASS: All cais path points along the full promenade are walkable and free.")
	
	# 3. Test actual physical walking from far West Alto-Lixo all the way down to the Port
	var player: CharacterBody2D = world.get_node("Structures/Player")
	player.set_physics_process(false)
	player.position = cais_points[0]
	
	for cp in cais_points:
		var diff = cp - player.position
		var col = player.move_and_collide(diff)
		assert(col == null, "Player collision during walk from West Alto to Port at " + str(cp))
		player.position = cp
	print("PASS: Player walked smoothly from West Alto-Lixo all the way down to the Port!")
	
	# 4. Test walk back from Port to West Alto-Lixo
	cais_points.reverse()
	for cp in cais_points:
		var diff = cp - player.position
		var col = player.move_and_collide(diff)
		assert(col == null, "Player collision during walk from Port back to West Alto at " + str(cp))
		player.position = cp
	print("PASS: Player walked smoothly from Port back to West Alto-Lixo!")
	
	world.queue_free()
	await process_frame
	print("ALL UNIFIED ALTO-CAIS TESTS PASSED SUCCESSFULLY!")
	quit(0)
