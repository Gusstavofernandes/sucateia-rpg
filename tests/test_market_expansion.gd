extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	await physics_frame
	await physics_frame
	if not world.has_node("MarketDistrict"):
		push_error("Market still confined to initial map dimensions; functional subareas absent")
		quit(1);return
	var camera: Camera2D=world.get_node("Structures/Player/Camera")
	assert(camera.limit_top < -1000)
	assert(get_nodes_in_group("player").size()==1)
	var player: CharacterBody2D=world.get_node("Structures/Player")
	player.set_physics_process(false)
	var space := world.get_world_2d().direct_space_state
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var grid := AStarGrid2D.new();grid.region=Rect2i(0,-60,100,135);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	for y in range(-60,75):
		for x in range(100):
			var cell := Vector2i(x,y);var point := grid.get_point_position(cell)
			query.transform=Transform2D(0,point)
			var floor: TileMapLayer=world.get_node("Ground/TerraceFloor")
			var extension: TileMapLayer=world.get_node("MarketDistrict/MarketFloor")
			var terrain: bool=floor.get_cell_source_id(floor.local_to_map(point))!=-1 or extension.get_cell_source_id(extension.local_to_map(point))!=-1
			grid.set_point_solid(cell,not terrain or not space.intersect_shape(query,1).is_empty())
	var start: Vector2=player.position
	for marker in world.get_node("MarketDistrict/Subareas").get_children():
		var path := grid.get_point_path(Vector2i(start/24),Vector2i(marker.position/24))
		if path.is_empty():push_error("No built walking route to "+str(marker.name));quit(1);return
		player.position=start
		for point in path:
			if player.move_and_collide(point-player.position):push_error("Collision on route "+str(marker.name));quit(1);return
		path.reverse()
		for point in path:
			if player.move_and_collide(point-player.position):push_error("Collision on return "+str(marker.name));quit(1);return
		print("SUBAREA ",marker.name," physical cells=",path.size())
	assert(world.get_node("MarketDistrict/Subareas").get_child_count()==8)
	assert(world.get_node("MarketDistrict/UrbanRoutes").get_child_count()==3)
	for alley in world.get_node("MarketDistrict/UrbanRoutes").get_children():
		var points: PackedVector2Array=alley.get_meta("points")
		for i in range(points.size()-1):
			var passage := grid.get_point_path(Vector2i(points[i]/24),Vector2i(points[i+1]/24))
			if passage.is_empty():push_error("Closed alley section: "+str(alley.name));quit(1);return
			player.position=passage[0]
			for point in passage:
				if player.move_and_collide(point-player.position):push_error("Blocked alley: "+str(alley.name));quit(1);return
		print("ALLEY ",alley.name," all sections traversed")
	print("PASS: eight market destinations and three alleys; physical ida/volta, original territory and player retained")
	world.queue_free();await process_frame;quit(0)
