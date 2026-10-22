extends SceneTree
func _initialize() -> void:call_deferred("run")
func cell(point: Vector2) -> Vector2i:return Vector2i(floori(point.x/24),floori(point.y/24))
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var modules: Node2D=world.get_node_or_null("Structures/ForjasProductionYards")
	if not modules:push_error("Production yards not integrated");quit(1);return
	if modules.get_parent()!=player.get_parent() or not modules.y_sort_enabled or modules.get_child_count()!=4:push_error("Production art or shared player sorting missing");quit(1);return
	var foundry: Node2D=world.get_node("Structures/ForjasIndustrialArchitecture/FundicaoDasCaldeiras")
	if not foundry.has_node("ExaustaoDaFundicao/ExaustaoAtiva"):push_error("Central foundry exhaust not attached");quit(1);return
	var detail: Node=world.get_node("ForjasRasasDistrict/ProductionDirectionFinish")
	var contacts: Node=world.get_node_or_null("ForjasRasasDistrict/PhysicalGroundContact")
	if not contacts:push_error("Final physical contact pass missing");quit(1);return
	for label in ["FundicaoDasCaldeiras","FornoDeRecuperacao","PrensaDeTriagem","PrensaDosRetalhos","BobinasDeRecuperacao","BaiaDeCarvao","TanqueDeResfriamento"]:
		if not contacts.has_node(label) or not contacts.get_node(label).has_meta("actual_sprite_foot"):push_error("Missing visible-base contact: "+label);quit(1);return
	for point in [Vector2(4100,-900),Vector2(3100,-1900)]:
		if world.is_walkable(point):push_error("Visual context incorrectly expands playable territory");quit(1);return
	for data in [["BaiaDeCarvao",Vector2(1440,517),"AlimentacaoCarvao"],["TanqueDeResfriamento",Vector2(1514,414),"AlimentacaoResfriamento"],["TanqueDeResfriamento",Vector2(155,693),"RetornoResfriamento"],["DescarteDeEscoria",Vector2(142,177),"DescargaRecuperacao"]]:
		var sprite: Sprite2D=modules.get_node(data[0]).get_child(0)
		var port: Vector2=sprite.to_global(data[1]-Vector2(sprite.texture.get_size())*.5)
		var points: PackedVector2Array=detail.get_node(data[2]).get_meta("connected_points")
		if port.distance_to(points[0])>8:push_error("Unaligned functional port: "+str(data[2]));quit(1);return
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for module in modules.get_children():
		query.transform=Transform2D(0,module.get_meta("footprint_center"))
		if space.intersect_shape(query,1).is_empty():push_error("Unblocked industrial module "+str(module.name));quit(1);return
	var grid := AStarGrid2D.new();grid.region=Rect2i(55,-70,100,100);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12);grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	for y in range(-70,30):
		for x in range(55,155):
			var at := Vector2i(x,y);var point := grid.get_point_position(at);query.transform=Transform2D(0,point)
			grid.set_point_solid(at,not world.is_walkable(point) or not space.intersect_shape(query,1).is_empty())
	for point in [Vector2(2500,-1090),Vector2(3545,-795),Vector2(2730,-220),Vector2(2780,-400),Vector2(2490,85),Vector2(1416,-756)]:
		var path := grid.get_point_path(cell(Vector2(1668,132)),cell(point))
		if path.is_empty():push_error("New working frontage inaccessible "+str(point));quit(1);return
		player.position=path[0]
		for at in path:
			if player.move_and_collide(at-player.position):push_error("Blocked new working frontage");quit(1);return
		path.reverse()
		for at in path:
			if player.move_and_collide(at-player.position):push_error("Blocked working frontage return");quit(1);return
	print("PASS: four production bases blocked; coal/slag/cooling/maintenance/ore and Market viewpoint reached ida/volta; shared player y-sort; exhaust attached to original foundry")
	world.queue_free();await process_frame;quit(0)
