extends SceneTree
func _initialize() -> void:call_deferred("run")
func cell(point: Vector2) -> Vector2i:return Vector2i(floori(point.x/24),floori(point.y/24))
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world)
	await physics_frame;await physics_frame
	if not world.has_node("AltoLixoDistrict"):
		push_error("Alto-Lixo west/northwest not built in the current scene");quit(1);return
	var district: Node2D=world.get_node("AltoLixoDistrict")
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var start := player.position
	var grid := AStarGrid2D.new();grid.region=Rect2i(-68,-68,174,150);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for y in range(-68,82):
		for x in range(-68,106):
			var at := Vector2i(x,y);var point := grid.get_point_position(at);query.transform=Transform2D(0,point)
			var built := false
			for path in ["Ground/TerraceFloor","MarketDistrict/MarketFloor","AltoLixoDistrict/AltoFloor"]:
				var floor: TileMapLayer=world.get_node(path)
				if floor.get_cell_source_id(floor.local_to_map(point))!=-1:built=true
			grid.set_point_solid(at,not built or not space.intersect_shape(query,1).is_empty())
	for group in ["Frontiers","Terraces","FutureExits"]:
		for marker in district.get_node(group).get_children():
			var passage := grid.get_point_path(cell(start),cell(marker.position))
			if passage.is_empty():push_error("No continuous route to "+str(marker.name));quit(1);return
			player.position=start
			for point in passage:
				if player.move_and_collide(point-player.position):push_error("Blocked ida "+str(marker.name));quit(1);return
			passage.reverse()
			for point in passage:
				if player.move_and_collide(point-player.position):push_error("Blocked volta "+str(marker.name));quit(1);return
			print("ALTO destination ",marker.name," ida/volta cells=",passage.size())
	for route in district.get_node("Routes").get_children():
		var points: PackedVector2Array=route.get_meta("points")
		for i in range(points.size()-1):
			var passage := grid.get_point_path(cell(points[i]),cell(points[i+1]))
			if passage.is_empty():push_error("Closed route section "+str(route.name)+" "+str(i));quit(1);return
			player.position=passage[0]
			for point in passage:
				if point.distance_to(Geometry2D.get_closest_point_to_segment(point,points[i],points[i+1]))>115:
					push_error("Route requires distant detour "+str(route.name)+" section "+str(i));quit(1);return
				if player.move_and_collide(point-player.position):push_error("Blocked route "+str(route.name));quit(1);return
		print("ALTO route ",route.name," all sections physically traversed")
	for stair in district.get_node("Stairs").get_children():
		var approach: Vector2=stair.get_meta("approach");var departure: Vector2=stair.get_meta("departure")
		player.position=approach
		if player.move_and_collide(departure-approach):push_error("Blocked stair "+str(stair.name));quit(1);return
		if player.move_and_collide(approach-departure):push_error("Blocked stair return "+str(stair.name));quit(1);return
		assert(world.is_walkable(approach) and world.is_walkable(departure))
		print("ALTO stair ",stair.name," crossed ida/volta")
	assert(district.get_node("Residences").get_child_count()>=22)
	assert(get_nodes_in_group("player").size()==1)
	assert(not world.has_node("RegionalSectors"))
	assert(not world.is_walkable(Vector2(-1600,-850)))
	print("PASS: continuous western Alto-Lixo, three frontiers, four terraces, six routes, four stairs, reserved exits and original scene retained")
	world.queue_free();await process_frame;quit(0)
