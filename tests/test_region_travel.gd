extends SceneTree
var failures: Array[String] = []
var travel: Node
func _initialize() -> void:
	call_deferred("run")
func settle() -> void:
	for i in range(5): await process_frame
	await physics_frame
	await physics_frame
func press_e() -> void:
	var event := InputEventKey.new()
	event.keycode = KEY_E
	event.physical_keycode = KEY_E
	event.pressed = true
	Input.parse_input_event(event)
	Input.flush_buffered_events()
	await settle()
	event = InputEventKey.new()
	event.keycode = KEY_E
	event.pressed = false
	Input.parse_input_event(event)
	Input.flush_buffered_events()
func run() -> void:
	travel = root.get_node_or_null("RegionTravel")
	if not travel:
		travel = load("res://scripts/world/region_travel.gd").new()
		travel.name = "RegionTravel"
		root.add_child(travel)
	var data: Dictionary = travel.catalog
	var tested := 0
	for source in data:
		for dest in data[source].links:
			travel.pending_from = ""
			travel.changing = false
			change_scene_to_file(data[source].scene)
			await settle()
			var player: CharacterBody2D = current_scene.get_node("Structures/Player")
			player.set_physics_process(false)
			var portal: Area2D = current_scene.get_node("RegionPortals/To_"+dest)
			player.position = portal.position
			await settle()
			if not portal.nearby:
				failures.append(source+" missing proximity "+dest)
				continue
			await press_e()
			if travel.current_region != dest:
				failures.append(source+" E did not reach "+dest)
				continue
			player = current_scene.get_node("Structures/Player")
			player.set_physics_process(false)
			var return_portal: Area2D = current_scene.get_node("RegionPortals/To_"+source)
			if player.position.distance_to(return_portal.position+return_portal.get_meta("arrival_offset",Vector2(0,58))) > 1:
				failures.append(dest+" incorrect arrival from "+source)
			var query := PhysicsShapeQueryParameters2D.new()
			var shape := CircleShape2D.new()
			shape.radius = 11
			query.shape = shape
			query.collision_mask = 1
			query.transform = Transform2D(0,player.position)
			if not player.get_world_2d().direct_space_state.intersect_shape(query,1).is_empty(): failures.append(dest+" arrival blocked")
			await press_e()
			if travel.current_region != source: failures.append(dest+" E did not return "+source)
			tested += 1
		print("TRAVEL tested ",source)
	if failures.is_empty():
		print("PASS: ",tested," directed connections entered with E and returned; safe arrivals")
		quit(0)
	else:
		for failure in failures: push_error(failure)
		quit(1)
