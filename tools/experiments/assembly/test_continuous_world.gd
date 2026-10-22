extends SceneTree
func _initialize() -> void:
	call_deferred("run")
func run() -> void:
	var world: Node2D = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	await physics_frame
	await physics_frame
	if not world.has_node("ContinuousRoutes"):
		push_error("Sucateia still consists of separate scenes, no physical regional routes")
		quit(1)
		return
	var players := get_nodes_in_group("player")
	assert(players.size()==1,"Only one player in expanded map")
	var player: CharacterBody2D = players[0]
	player.set_physics_process(false)
	var identity := player.get_instance_id()
	var count := 0
	for route in world.get_node("ContinuousRoutes").get_children():
		var points: PackedVector2Array = route.get_meta("path")
		player.global_position=points[0]
		for point in points:
			assert(world.is_walkable(point),"Every crossing has constructed ground")
			var hit := player.move_and_collide(point-player.global_position)
			if hit:
				push_error("Blocked continuous crossing: "+str(route.name)+" at "+str(point))
				quit(1)
				return
		points.reverse()
		for point in points:
			if player.move_and_collide(point-player.global_position):
				push_error("Blocked physical return: "+str(route.name))
				quit(1)
				return
		assert(player.get_instance_id()==identity,"No player replacement")
		count+=1
	assert(count==27,"All regional links are physically present")
	assert(world.get_node("RegionalSectors").get_child_count()==15)
	print("PASS: existing Sucateia extended; 16 sectors, one player, 27 physical crossings without loading")
	world.queue_free()
	await process_frame
	quit(0)
