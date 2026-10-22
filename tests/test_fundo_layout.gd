extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	if not ResourceLoader.exists("res://maps/fundo_ferro/fundo_ferro.tscn"):
		push_error("Fundo-Ferro underground layer missing");quit(1);return
	var world: Node2D=load("res://maps/fundo_ferro/fundo_ferro.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var grid := AStarGrid2D.new();grid.region=Rect2i(38,13,150,92);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for y in range(13,105):
		for x in range(38,188):
			var cell := Vector2i(x,y);var point := grid.get_point_position(cell);query.transform=Transform2D(0,point)
			grid.set_point_solid(cell,not world.is_walkable(point) or not space.intersect_shape(query,1).is_empty())
	for marker in world.get_node("Rooms").get_children():
		var path := grid.get_point_path(Vector2i(1296/24,1572/24),Vector2i(marker.position/24))
		if path.is_empty():push_error("Unreachable underground room "+str(marker.name));quit(1);return
		player.position=path[0]
		for point in path:
			if player.move_and_collide(point-player.position):push_error("Blocked underground room route");quit(1);return
		path.reverse()
		for point in path:
			if player.move_and_collide(point-player.position):push_error("Blocked underground return");quit(1);return
		print("FUNDO room ",marker.name," ida/volta ",path.size())
	for route in world.get_node("Routes").get_children():
		var points: PackedVector2Array=route.get_meta("points")
		for i in range(points.size()-1):
			var path := grid.get_point_path(Vector2i(points[i]/24),Vector2i(points[i+1]/24))
			if path.is_empty():push_error("Closed underground route "+str(route.name));quit(1);return
			player.position=path[0]
			for point in path:
				if point.distance_to(Geometry2D.get_closest_point_to_segment(point,points[i],points[i+1]))>115:push_error("Distant underground detour");quit(1);return
				if player.move_and_collide(point-player.position):push_error("Blocked underground circuit");quit(1);return
		print("FUNDO route ",route.name," all sections")
	for point in world.get_meta("water_samples"):
		query.transform=Transform2D(0,point);assert(not world.is_walkable(point) and not space.intersect_shape(query,1).is_empty())
	for span in [[Vector2(1820,2025),Vector2(1820,2170)],[Vector2(2660,1030),Vector2(2660,1220)]]:
		player.position=span[0]
		assert(world.is_walkable(span[0]) and world.is_walkable(span[1]))
		if player.move_and_collide(span[1]-span[0]) or player.move_and_collide(span[0]-span[1]):push_error("Blocked underground bridge ida/volta");quit(1);return
		print("FUNDO bridge ",span[0]," ida/volta")
	var bases := 0
	for node in world.get_node("Structures").get_children():
		if not node.has_meta("blocked_base"):continue
		query.transform=Transform2D(0,node.get_meta("blocked_base"));assert(not space.intersect_shape(query,1).is_empty());bases+=1
	assert(bases==6 and not world.is_walkable(Vector2(2400,1770)))
	assert(world.get_node("Rooms").get_child_count()==8 and get_nodes_in_group("player").size()==1)
	print("PASS: eight underground rooms, return circuit, nine routes, two bridges ida/volta, six blocked machines, water and one player")
	world.queue_free();await process_frame;quit(0)
