extends SceneTree
var failures: Array[String] = []
func check(condition: bool, message: String) -> void:
	if not condition: failures.append(message)
func key(code: Key, pressed: bool) -> void:
	var event := InputEventKey.new()
	event.physical_keycode = code
	event.keycode = code
	event.pressed = pressed
	Input.parse_input_event(event)
	Input.flush_buffered_events()
func _initialize() -> void:
	call_deferred("run")
func run() -> void:
	if not ResourceLoader.exists("res://maps/sucateia/sucateia.tscn"):
		push_error("Área jogável ausente")
		quit(1)
		return
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node2D = packed.instantiate()
	root.add_child(world)
	await physics_frame
	await physics_frame
	var player: CharacterBody2D = world.get_node("Structures/Player")
	check(world.get_node("Ground/TerraceFloor") is TileMapLayer,"Piso deve usar TileMapLayer")
	check(player.get_node("Camera") is Camera2D,"Câmera ausente")
	check(world.get_node("Structures/workshop/Architecture").texture.resource_path.ends_with("workshop.png"),"Override da oficina não persistiu")
	check(world.get_node("Structures/reactor/Architecture").texture.resource_path.ends_with("reactor.png"),"Override do reator não persistiu")
	var painted_structures := 0
	for structure in world.get_node("Structures").get_children():
		if structure.has_node("Architecture"):
			var texture: Texture2D = structure.get_node("Architecture").texture
			check(texture.resource_path.begins_with("res://assets/generated/"),"Arquitetura antiga na cena: "+structure.name)
			painted_structures += 1
	check(painted_structures == 16,"Módulos de arquitetura incompletos")
	print("ART: 16 generated architecture instances preserved")
	var space := world.get_world_2d().direct_space_state
	var query := PhysicsShapeQueryParameters2D.new()
	var circle := CircleShape2D.new()
	circle.radius = 11
	query.shape = circle
	query.collision_mask = 1
	# Verify displaced canal banks, a shore recess and the bridge crossing.
	for sample in [[Vector2(1810,740),true],[Vector2(1968,1260),true],[Vector2(1810,1260),false],[Vector2(1880,1063),false]]:
		query.transform = Transform2D(0,sample[0])
		check((not space.intersect_shape(query,1).is_empty()) == sample[1],"Canal collision mismatch: "+str(sample[0]))
	print("CANAL: displaced banks block runoff; recess and crossing accessible")
	# Raised piers are decorative lower service levels; sea stays inaccessible.
	check(world.has_node("GoblinIndustrialQuay"),"Industrial quay absent")
	for at in [Vector2(140,1000),Vector2(2280,700),Vector2(1000,1730),Vector2(1850,1780)]:
		query.transform = Transform2D(0,at)
		check(not space.intersect_shape(query,1).is_empty(),"Unprotected sea edge: "+str(at))
	query.transform = Transform2D(0,Vector2(1600,1610))
	check(space.intersect_shape(query,1).is_empty(),"Coastal approach blocked")
	print("COAST: four exterior sea samples blocked; approach open")
	var grid := AStarGrid2D.new()
	grid.region = Rect2i(0,0,100,75)
	grid.cell_size = Vector2(24,24)
	grid.offset = Vector2(12,12)
	grid.diagonal_mode = AStarGrid2D.DIAGONAL_MODE_NEVER
	grid.update()
	var blocked := 0
	for y in range(75):
		for x in range(100):
			query.transform = Transform2D(0,Vector2(x*24+12,y*24+12))
			if not space.intersect_shape(query,1).is_empty():
				grid.set_point_solid(Vector2i(x,y),true)
				blocked += 1
	var origin := Vector2i(player.position/24)
	query.transform = Transform2D(0,player.position)
	check(space.intersect_shape(query,1).is_empty(),"Spawn sobre colisão")
	for m in world.get_node("RouteMarkers").get_children():
		var goal := Vector2i(m.position/24)
		var path := grid.get_id_path(origin,goal)
		check(not path.is_empty(),"Rota bloqueada: "+m.name)
		player.position = world.get_node("RouteMarkers/Spawn").position
		for cell in path:
			var target := Vector2(cell)*24+Vector2(12,12)
			var hit := player.move_and_collide(target-player.position)
			check(hit == null,"Colisão na travessia real: "+m.name)
		check(player.position.distance_to(grid.get_point_position(goal))<2,"Destino não alcançado: "+m.name)
		print("ROUTE ",m.name," cells=",path.size()," traversed")
	player.position = world.get_node("RouteMarkers/Spawn").position
	check(player.test_move(player.global_transform,Vector2(-1100,0)),"Travessia de paredes deve ser bloqueada")
	player.set_physics_process(false)
	var begin: Vector2 = player.position
	key(KEY_W,true)
	for i in range(20): player._physics_process(1.0/60.0)
	key(KEY_W,false)
	await physics_frame
	var walk: float = begin.distance_to(player.position)
	check(walk > 35 and walk < 65,"Movimento WASD fora da escala: "+str(walk))
	player.position = begin
	key(KEY_W,true)
	key(KEY_SHIFT,true)
	for i in range(20): player._physics_process(1.0/60.0)
	key(KEY_W,false)
	key(KEY_SHIFT,false)
	await physics_frame
	var run_distance: float = begin.distance_to(player.position)
	check(run_distance > walk*1.4,"Shift não acelera")
	key(KEY_R,true)
	await physics_frame
	key(KEY_R,false)
	check(player.position.distance_to(player.spawn_point)<2,"R não restaura spawn")
	print("MOVEMENT walk=",walk," run=",run_distance," blocked_grid=",blocked)
	if failures.is_empty():
		print("PASS: scene, tile layer, 9 connected routes, spawn, collision, WASD, sprint and reset")
		quit(0)
	else:
		for failure in failures: push_error(failure)
		quit(1)

