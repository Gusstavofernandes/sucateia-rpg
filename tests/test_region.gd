extends SceneTree
func _initialize() -> void:
	call_deferred("run")
func run() -> void:
	if not FileAccess.file_exists("res://maps/ferrugem_baixa/region.json"):
		push_error("Region manifest missing")
		quit(1)
		return
	var data: Dictionary = JSON.parse_string(FileAccess.get_file_as_string("res://maps/ferrugem_baixa/region.json"))
	var failures: Array[String] = []
	for required in ["galeria","banco","engrenopolis","via_cais","via_engrenagens","eng_nucleo","eng_corredor"]:
		if not data.has(required): failures.append("Required region missing: "+required)
	for id in data:
		var config: Dictionary = data[id]
		var packed: PackedScene = load(config.scene)
		if not packed:
			failures.append("Missing scene "+id)
			continue
		var world: Node2D = packed.instantiate()
		if id == "galeria":
			for room in ["CamaraDeValvulas","BombasInferiores","ColetorNorte"]:
				if not world.has_node("RouteMarkers/"+room): failures.append("Gallery room missing: "+room)
		root.add_child(world)
		await physics_frame
		await physics_frame
		var player: CharacterBody2D = world.get_node("Structures/Player")
		player.set_physics_process(false)
		var space := world.get_world_2d().direct_space_state
		var query := PhysicsShapeQueryParameters2D.new()
		var shape := CircleShape2D.new()
		shape.radius = 11
		query.shape = shape
		query.collision_mask = 1
		var grid := AStarGrid2D.new()
		grid.region = Rect2i(0,0,100,80)
		grid.cell_size = Vector2(24,24)
		grid.offset = Vector2(12,12)
		grid.diagonal_mode = AStarGrid2D.DIAGONAL_MODE_NEVER
		grid.update()
		for y in range(80):
			for x in range(100):
				query.transform = Transform2D(0,Vector2(x*24+12,y*24+12))
				grid.set_point_solid(Vector2i(x,y),not space.intersect_shape(query,1).is_empty())
		var start := player.position
		query.transform = Transform2D(0,start)
		if not space.intersect_shape(query,1).is_empty(): failures.append(id+" spawn blocked")
		var targets: Array[Node] = []
		if world.has_node("RegionPortals"): targets.append_array(world.get_node("RegionPortals").get_children())
		if world.has_node("RouteMarkers"): targets.append_array(world.get_node("RouteMarkers").get_children())
		for target in targets:
			var path := grid.get_id_path(Vector2i(start/24),Vector2i(target.global_position/24))
			if path.is_empty():
				failures.append(id+" inaccessible "+target.name)
				continue
			player.position = start
			for cell in path:
				var hit := player.move_and_collide(grid.get_point_position(cell)-player.position)
				if hit: failures.append(id+" collision to "+target.name);break
			if target.has_meta("destination"):
				query.transform = Transform2D(0,target.position+target.get_meta("arrival_offset",Vector2(0,58)))
				if not space.intersect_shape(query,1).is_empty(): failures.append(id+" unsafe arrival "+target.name)

				var dest: String = target.get_meta("destination")
				if not data.has(dest): failures.append(id+" invalid destination "+dest)
				elif not data[dest].links.has(id): failures.append(id+" no return from "+dest)
		print("REGION ",id," routes=",targets.size()," nodes=",world.get_child_count())
		world.queue_free()
		await process_frame
	if failures.is_empty():
		print("PASS: all district scenes, local traversal, safe spawns and bidirectional graph")
		quit(0)
	else:
		for failure in failures: push_error(failure)
		quit(1)
