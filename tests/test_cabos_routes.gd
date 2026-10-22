extends SceneTree
func _initialize() -> void:call_deferred("run")
func check(condition: bool,message: String) -> bool:
	if not condition:push_error(message);quit(1)
	return condition
func grid_for(world: Node2D,mask: int,upper: bool) -> AStarGrid2D:
	var grid := AStarGrid2D.new();grid.cell_size=Vector2(6,6) if upper else Vector2(24,24);grid.offset=grid.cell_size*.5;grid.region=Rect2i(-80,-200,430,230) if upper else Rect2i(-68,-80,322,162);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_ALWAYS if upper else AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	var query := PhysicsShapeQueryParameters2D.new();var circle := CircleShape2D.new();circle.radius=11;query.shape=circle;query.collision_mask=mask;var space := world.get_world_2d().direct_space_state
	for y in range(grid.region.position.y,grid.region.end.y):
		for x in range(grid.region.position.x,grid.region.end.x):
			var at := Vector2i(x,y);var point := grid.get_point_position(at)
			if not world.is_walkable(point):grid.set_point_solid(at,true);continue
			query.transform=Transform2D(0,point);grid.set_point_solid(at,not space.intersect_shape(query,1).is_empty())
	return grid
func cell(grid: AStarGrid2D,point: Vector2) -> Vector2i:return Vector2i(floori(point.x/grid.cell_size.x),floori(point.y/grid.cell_size.y))
func traverse(player: CharacterBody2D,points: PackedVector2Array,label: String) -> bool:
	if not check(not points.is_empty(),"Closed physical Cabos path "+label):return false
	player.position=points[0]
	for point in points:
		if not check(player.move_and_collide(point-player.position)==null,"Blocked Cabos movement "+label+" at "+str(point)):return false
	points.reverse()
	for point in points:
		if not check(player.move_and_collide(point-player.position)==null,"Blocked return Cabos "+label):return false
	return true
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	if not check(world.has_node("CabosDistrict"),"Cabos network missing"):return
	var district: Node2D=world.get_node("CabosDistrict");var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false);var original := player.position
	var ground_grid := grid_for(world,1,false)
	for access in district.get_node("Accesses").get_children():
		var point: Vector2=access.get_meta("surface_arrival")
		if not traverse(player,ground_grid.get_point_path(cell(ground_grid,original),cell(ground_grid,point)),"surface arrival "+str(access.name)):return
		print("CABOS ground arrival ",access.name," physical ida/volta")
	var access: Node=district.get_node("Accesses/Mercado");player.position=access.get_meta("surface_arrival")
	if not check(district.change_layer(access),"Could not enter Cabos for route test"):return
	var upper_grid := grid_for(world,4,true);var source: Vector2=access.get_meta("elevated_arrival")
	for landing in district.get_node("Landings").get_children():
		if not traverse(player,upper_grid.get_point_path(cell(upper_grid,source),cell(upper_grid,landing.position)),"upper landing "+str(landing.name)):return
		print("CABOS upper landing ",landing.name," physical ida/volta")
	for route in district.get_node("Routes").get_children():
		var points: PackedVector2Array=route.get_meta("points");var path := upper_grid.get_point_path(cell(upper_grid,points[0]),cell(upper_grid,points[1]))
		for point in path:
			if not check(point.distance_to(Geometry2D.get_closest_point_to_segment(point,points[0],points[1]))<70,"Upper route detours away from its deck "+str(route.name)):return
		if not traverse(player,path,str(route.name)):return
		print("CABOS route ",route.name," physically traversed ida/volta")
	var before := player.position;player.position=Vector2(980,-750)
	if not check(not world.is_walkable(player.position),"Upper player can walk through gap"):return
	player.position=before
	print("PASS: three surface arrivals, all elevated landings, main/alternate/T routes physically crossed ida/volta; upper gaps blocked")
	world.queue_free();await process_frame;quit(0)
