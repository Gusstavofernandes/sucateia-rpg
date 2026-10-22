extends SceneTree
func _initialize() -> void:call_deferred("run")
func cell(point: Vector2) -> Vector2i:return Vector2i(floori(point.x/24),floori(point.y/24))
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	if not world.has_node("PassagemAmarrasDistrict"):
		push_error("Passagem das Amarras missing from the continuous current city");quit(1);return
	var district: Node2D=world.get_node("PassagemAmarrasDistrict")
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var start := player.position
	var grid := AStarGrid2D.new();grid.region=Rect2i(-68,-80,322,162);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for y in range(-80,82):
		for x in range(-68,254):
			var at := Vector2i(x,y);var point := grid.get_point_position(at);query.transform=Transform2D(0,point)
			grid.set_point_solid(at,not world.is_walkable(point) or not space.intersect_shape(query,1).is_empty())
	for group in ["Frontiers","WorkYards","FutureExits","SafeArrivals"]:
		for marker in district.get_node(group).get_children():
			var passage := grid.get_point_path(cell(start),cell(marker.position))
			if passage.is_empty():push_error("No continuous city route to "+str(marker.name));quit(1);return
			player.position=start
			for point in passage:
				if player.move_and_collide(point-player.position):push_error("Blocked ida "+str(marker.name));quit(1);return
			passage.reverse()
			for point in passage:
				if player.move_and_collide(point-player.position):push_error("Blocked volta "+str(marker.name));quit(1);return
			print("AMARRAS destination ",marker.name," ida/volta cells=",passage.size())
	for route in district.get_node("Routes").get_children():
		var points: PackedVector2Array=route.get_meta("points")
		for i in range(points.size()-1):
			var passage := grid.get_point_path(cell(points[i]),cell(points[i+1]))
			if passage.is_empty():push_error("Closed Amarras route "+str(route.name)+" section "+str(i));quit(1);return
			player.position=passage[0]
			for point in passage:
				if point.distance_to(Geometry2D.get_closest_point_to_segment(point,points[i],points[i+1]))>135:
					push_error("Amarras route requires distant detour "+str(route.name)+" section="+str(i)+" at="+str(point));quit(1);return
				if player.move_and_collide(point-player.position):push_error("Blocked Amarras route "+str(route.name));quit(1);return
		print("AMARRAS route ",route.name," all sections physically traversed")
	for bridge in district.get_node("Bridges").get_children():
		var a: Vector2=bridge.get_meta("approach");var b: Vector2=bridge.get_meta("departure");player.position=a
		assert(world.is_walkable(a) and world.is_walkable(b))
		if player.move_and_collide(b-a) or player.move_and_collide(a-b):push_error("Blocked Amarras bridge "+str(bridge.name));quit(1);return
		print("AMARRAS bridge ",bridge.name," ida/volta")
	for point in district.get_meta("water_samples"):
		query.transform=Transform2D(0,point)
		assert(not world.is_walkable(point) and not space.intersect_shape(query,1).is_empty(),"Unblocked drainage")
	assert(district.get_node("Bridges").get_child_count()==4)
	assert(get_nodes_in_group("player").size()==1 and not world.has_node("RegionalSectors"))
	player.position=world.get_node("PassagemAmarrasDistrict/SafeArrivals/ChegadaDeCarga").position
	var reset := InputEventKey.new();reset.keycode=KEY_R;reset.pressed=true;player._unhandled_input(reset)
	assert(player.position==player.spawn_point and world.is_walkable(player.position),"Unsafe existing reset")
	print("PASS: Amarras continuous same-scene access, routes ida/volta, four bridges, blocked canal, safe arrivals and R; one player")
	world.queue_free();await process_frame;quit(0)

