extends "res://tests/test_docas_routes.gd"
func stitch_grid(world: Node2D,dock: Node2D) -> AStarGrid2D:
	var grid := AStarGrid2D.new();grid.cell_size=Vector2(12,12);grid.offset=Vector2(6,6);grid.region=Rect2i(90,-15,199,179);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	var query := PhysicsShapeQueryParameters2D.new();var circle := CircleShape2D.new();circle.radius=11;query.shape=circle;query.collision_mask=1;var space := world.get_world_2d().direct_space_state
	for y in range(grid.region.position.y,grid.region.end.y):
		for x in range(grid.region.position.x,grid.region.end.x):
			var at := Vector2i(x,y);var point := grid.get_point_position(at);query.transform=Transform2D(0,point);query.exclude=dock.water_exclusions(point)
			grid.set_point_solid(at,not world.is_surface_walkable(point) or not space.intersect_shape(query,1).is_empty())
	return grid
func sprites_under(node: Node) -> int:
	var total := 1 if node is Sprite2D and node.is_visible_in_tree() else 0
	for child in node.get_children():total+=sprites_under(child)
	return total
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	if not check(world.has_node("PortStitchInfrastructure/FunctionalStations"),"Port stitch economic stations missing"):return
	var port: Node2D=world.get_node("PortStitchInfrastructure");var dock: Node2D=world.get_node("DocasDistrict");var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false);var grid := stitch_grid(world,dock);var source: Vector2=dock.get_node("Connections/NucleoUrbano").position
	for role in ["ChegadaRasa","TriagemMolhada","Almoxarifado","BordaUrbana","BocasTecnicas"]:
		if not check(port.get_node("FunctionalStations").has_node(role),"Port economic role missing "+role):return
		var station: Node2D=port.get_node("FunctionalStations/"+role)
		var artwork_count := 0
		for path in station.get_meta("art_paths",[]):
			var art: Node=world.get_node_or_null(path)
			if art!=null:artwork_count+=sprites_under(art)
		if not check(artwork_count>0,"Visible service art missing "+role):return
		for target in station.get_meta("public_approaches",[]):
			if not dock_traverse(player,dock,grid.get_point_path(cell(grid,source),cell(grid,target)),role):return
	for landing in dock.get_node("SafeLandings").get_children():
		if not dock_traverse(player,dock,grid.get_point_path(cell(grid,source),cell(grid,landing.position)),"preserved respawn "+str(landing.name)):return
	for entrance in world.get_node("LayerEntrances").get_children():
		if not entrance is Area2D:continue
		if not dock_traverse(player,dock,grid.get_point_path(cell(grid,source),cell(grid,entrance.position)),"preserved F access "+str(entrance.name)):return
	var before: Node=load("res://tools/checkpoints/sucateia_before_port_stitch.tscn").instantiate();var current: Node=load("res://maps/sucateia/sucateia.tscn").instantiate();var preservation: SceneTree=load("res://tests/test_amarras_preservation.gd").new();var good: bool=preservation.compare(before,current,"Sucateia");before.free();current.free();preservation.free()
	if not check(good,"Approved city modified by stitch"):return
	print("PASS: five economic roles have real art; service aprons, all three F access pockets and six safe landings physically reached ida/volta; approved serialized city preserved")
	world.queue_free();await process_frame;quit(0)
