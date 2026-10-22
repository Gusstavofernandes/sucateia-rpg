extends SceneTree
func _initialize() -> void:call_deferred("run")
func cell(point: Vector2) -> Vector2i:return Vector2i(floori(point.x/24),floori(point.y/24))
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	if not world.has_node("ForjasRasasDistrict"):
		push_error("Forjas Rasas missing from the continuous current city");quit(1);return
	var district: Node2D=world.get_node("ForjasRasasDistrict")
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var start := player.position
	var grid := AStarGrid2D.new();grid.region=Rect2i(-68,-80,232,162);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for y in range(-80,82):
		for x in range(-68,164):
			var at := Vector2i(x,y);var point := grid.get_point_position(at);query.transform=Transform2D(0,point)
			grid.set_point_solid(at,not world.is_walkable(point) or not space.intersect_shape(query,1).is_empty())
	for group in ["Frontiers","WorkYards","FutureExits"]:
		for marker in district.get_node(group).get_children():
			var passage := grid.get_point_path(cell(start),cell(marker.position))
			if passage.is_empty():push_error("No continuous Forjas route to "+str(marker.name));quit(1);return
			player.position=start
			for point in passage:
				if player.move_and_collide(point-player.position):push_error("Blocked ida "+str(marker.name));quit(1);return
			passage.reverse()
			for point in passage:
				if player.move_and_collide(point-player.position):push_error("Blocked volta "+str(marker.name));quit(1);return
			print("FORJAS destination ",marker.name," ida/volta cells=",passage.size())
	for route in district.get_node("Routes").get_children():
		var points: PackedVector2Array=route.get_meta("points")
		for i in range(points.size()-1):
			var passage := grid.get_point_path(cell(points[i]),cell(points[i+1]))
			if passage.is_empty():push_error("Closed Forjas route "+str(route.name)+" section "+str(i));quit(1);return
			player.position=passage[0]
			for point in passage:
				if point.distance_to(Geometry2D.get_closest_point_to_segment(point,points[i],points[i+1]))>135:
					push_error("Forjas route requires distant detour "+str(route.name));quit(1);return
				if player.move_and_collide(point-player.position):push_error("Blocked Forjas route "+str(route.name));quit(1);return
		print("FORJAS route ",route.name," all sections physically traversed")
	for bridge in district.get_node("Bridges").get_children():
		var a: Vector2=bridge.get_meta("approach");var b: Vector2=bridge.get_meta("departure");player.position=a
		assert(world.is_walkable(a) and world.is_walkable(b))
		if player.move_and_collide(b-a) or player.move_and_collide(a-b):push_error("Blocked Forjas bridge "+str(bridge.name));quit(1);return
		print("FORJAS bridge ",bridge.name," ida/volta")
	for point in district.get_meta("water_samples"):
		query.transform=Transform2D(0,point)
		assert(not world.is_walkable(point) and not space.intersect_shape(query,1).is_empty(),"Unblocked drainage")
	assert(world.get_node("Structures/ForjasIndustrialArchitecture").get_child_count()>=12)
	assert(get_nodes_in_group("player").size()==1 and not world.has_node("RegionalSectors"))
	print("PASS: Forjas continuous access, industrial yards, routes, bridges, blocked drainage and one player")
	world.queue_free();await process_frame;quit(0)
