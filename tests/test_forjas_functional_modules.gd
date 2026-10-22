extends SceneTree
func _initialize() -> void:call_deferred("run")
func cell(point: Vector2) -> Vector2i:return Vector2i(floori(point.x/24),floori(point.y/24))
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var modules: Node2D=world.get_node("Structures/ForjasFunctionalModules")
	if modules.get_parent()!=player.get_parent() or not modules.y_sort_enabled or modules.get_child_count()!=5:push_error("Functional art or shared player sorting missing");quit(1);return
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for module in modules.get_children():
		query.transform=Transform2D(0,module.get_meta("footprint_center"))
		if space.intersect_shape(query,1).is_empty():push_error("Unblocked industrial module "+str(module.name));quit(1);return
	var grid := AStarGrid2D.new();grid.region=Rect2i(60,-70,95,100);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	for y in range(-70,30):
		for x in range(60,155):
			var at := Vector2i(x,y);var point := grid.get_point_position(at);query.transform=Transform2D(0,point)
			grid.set_point_solid(at,not world.is_walkable(point) or not space.intersect_shape(query,1).is_empty())
	for point in [Vector2(2050,-198),Vector2(1850,60),Vector2(2490,85),Vector2(2945,-848),Vector2(2840,-1295)]:
		var path := grid.get_point_path(cell(Vector2(1668,132)),cell(point))
		if path.is_empty():push_error("New working frontage inaccessible "+str(point));quit(1);return
		player.position=path[0]
		for at in path:
			if player.move_and_collide(at-player.position):push_error("Blocked new working frontage");quit(1);return
		path.reverse()
		for at in path:
			if player.move_and_collide(at-player.position):push_error("Blocked working frontage return");quit(1);return
	print("PASS: five functional bases blocked and five service frontages physically reached ida/volta from Market; shared player y-sort")
	world.queue_free();await process_frame;quit(0)
