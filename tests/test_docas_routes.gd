extends "res://tests/test_cabos_routes.gd"
func docas_grid(world: Node2D,district: Node2D) -> AStarGrid2D:
	var grid := AStarGrid2D.new();grid.cell_size=Vector2(12,12);grid.offset=Vector2(6,6);grid.region=Rect2i(170,15,118,158);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	var query := PhysicsShapeQueryParameters2D.new();var circle := CircleShape2D.new();circle.radius=11;query.shape=circle;query.collision_mask=1;var space := world.get_world_2d().direct_space_state
	for y in range(grid.region.position.y,grid.region.end.y):
		for x in range(grid.region.position.x,grid.region.end.x):
			var at := Vector2i(x,y);var point := grid.get_point_position(at);query.transform=Transform2D(0,point);query.exclude=district.water_exclusions(point)
			grid.set_point_solid(at,not world.is_walkable(point) or not space.intersect_shape(query,1).is_empty())
	return grid
func dock_traverse(player: CharacterBody2D,district: Node2D,points: PackedVector2Array,label: String) -> bool:
	if not check(not points.is_empty(),"Closed Docas path "+label):return false
	player.position=points[0]
	for direction in range(2):
		for point in points:
			district.update_player_water();if not check(player.move_and_collide(point-player.position)==null,"Blocked dock path "+label+" at "+str(point)):return false
		points.reverse()
	return true
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	if not check(world.has_node("DocasDistrict"),"Docas continuous district missing"):return
	var district: Node2D=world.get_node("DocasDistrict");var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false);var origin := player.position;var old_grid := grid_for(world,1,false)
	for entrance in district.get_node("Connections").get_children():
		if not traverse(player,old_grid.get_point_path(cell(old_grid,origin),cell(old_grid,entrance.position)),"existing city arrival "+str(entrance.name)):return
	var grid := docas_grid(world,district);var source: Vector2=district.get_node("Connections/NucleoUrbano").position
	for destination in district.get_node("SafeLandings").get_children():
		if not dock_traverse(player,district,grid.get_point_path(cell(grid,source),cell(grid,destination.position)),str(destination.name)):return
		player.position=destination.position;district.update_player_water();district.update_safe_spawn();var reset := InputEventKey.new();reset.keycode=KEY_R;reset.pressed=true;player.position+=Vector2(12,0);player._unhandled_input(reset)
		if not check(player.position==destination.position and world.is_walkable(player.position),"Unsafe Docas respawn "+str(destination.name)):return
	for route in district.get_node("Routes").get_children():
		var points: PackedVector2Array=route.get_meta("points")
		if not dock_traverse(player,district,grid.get_point_path(cell(grid,points[0]),cell(grid,points[1])),str(route.name)):return
		print("DOCAS ",route.name," physically crossed ida/volta")
	for point in district.get_meta("water_samples"):
		if not check(not world.is_walkable(point),"Docas walking through harbor water"):return
	if not check(get_nodes_in_group("player").size()==1,"Docas duplicated player"):return
	print("PASS: three continuous dock arrivals; all cargo/coastal/technical/work routes ida/volta; safe R landings; harbor water blocked; one city/player")
	world.queue_free();await process_frame;quit(0)
