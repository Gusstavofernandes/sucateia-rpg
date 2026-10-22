extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world)
	await physics_frame;await physics_frame
	if not world.has_node("LowerCoastReworked"):
		push_error("Lower city still has old rectangular coast");quit(1);return
	var coast: Node2D=world.get_node("LowerCoastReworked")
	var previous: Node2D=load("res://tools/checkpoints/sucateia_before_lower_coast.tscn").instantiate()
	for path in ["MarketDistrict/MarketFloor","AltoLixoDistrict/AltoFloor","Ground/TerraceFloor"]:
		var before: TileMapLayer=previous.get_node(path);var after: TileMapLayer=world.get_node(path)
		var before_count := 0;var after_count := 0
		for at in before.get_used_cells():
			if path=="Ground/TerraceFloor" and before.map_to_local(at).y>=1170:continue
			before_count+=1
			assert(before.get_cell_source_id(at)==after.get_cell_source_id(at) and before.get_cell_atlas_coords(at)==after.get_cell_atlas_coords(at),"Protected terrain changed "+path)
		for at in after.get_used_cells():
			if path=="Ground/TerraceFloor" and after.map_to_local(at).y>=1170:continue
			after_count+=1
		assert(before_count==after_count,"Protected terrain area changed "+path)
	for structure in previous.get_node("Structures").get_children():
		if not structure.has_node("Architecture"):continue
		var retained: Node2D=world.get_node("Structures/"+str(structure.name))
		assert(retained.transform==structure.transform,"Approved structure moved: "+str(structure.name))
		assert(retained.get_node("Architecture").texture.resource_path==structure.get_node("Architecture").texture.resource_path)
	previous.free()
	print("PROTECTED: MarketFloor, AltoFloor, upper original terrain and 16 approved architecture placements unchanged")
	var query := PhysicsShapeQueryParameters2D.new();var circle := CircleShape2D.new();circle.radius=11;query.shape=circle;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for point in [Vector2(205,1490),Vector2(870,1580),Vector2(1395,1630),Vector2(2215,1450),Vector2(800,1840)]:
		query.transform=Transform2D(0,point)
		assert(not space.intersect_shape(query,1).is_empty(),"Water recess must block walking: "+str(point))
		assert(not world.is_walkable(point),"Water recess must not be ground: "+str(point))
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var start := player.position
	var grid := AStarGrid2D.new();grid.region=Rect2i(0,0,100,88);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	for y in range(88):
		for x in range(100):
			var cell := Vector2i(x,y);var point := grid.get_point_position(cell);query.transform=Transform2D(0,point)
			grid.set_point_solid(cell,not world.is_walkable(point) or not space.intersect_shape(query,1).is_empty())
	for marker in coast.get_node("Destinations").get_children():
		var path := grid.get_point_path(Vector2i(start/24),Vector2i(marker.position/24))
		if path.is_empty():push_error("Coastal destination isolated: "+str(marker.name));quit(1);return
		player.position=start
		for point in path:
			if player.move_and_collide(point-player.position):push_error("Blocked coastal ida "+str(marker.name));quit(1);return
		path.reverse()
		for point in path:
			if player.move_and_collide(point-player.position):push_error("Blocked coastal volta "+str(marker.name));quit(1);return
		print("LOWER COAST ",marker.name," ida/volta cells=",path.size())
	assert(coast.get_meta("recess_count")==4)
	print("PASS: irregular lower coast, five protected water samples, maintained lower circulation and connected maintenance decks")
	world.queue_free();await process_frame;quit(0)
