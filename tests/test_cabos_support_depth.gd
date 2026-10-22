extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func run() -> void:
	var world: Node2D = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	await process_frame
	var structures: Node2D = world.get_node("Structures")
	var district: Node2D = world.get_node("CabosDistrict")
	var grounded: Node2D = structures.get_node_or_null("CabosGroundSupports")
	if grounded == null or not structures.y_sort_enabled or not grounded.y_sort_enabled:
		push_error("Cabos pillars must share the buildings' ground depth sorting")
		quit(1)
		return
	var count := 0
	for source in district.get_node("StructuralSupports").get_children():
		if not source.has_meta("ground_contact"):
			continue
		var receiver: Node2D = grounded.get_node(String(source.name))
		var art: Sprite2D = receiver.get_node("Art")
		var foot: Vector2 = district.to_global(source.get_meta("ground_contact"))
		var expected: Transform2D = source.global_transform
		if receiver.global_position.distance_to(foot) > .01 or art.z_index != 0 or source.visible:
			push_error("Pillar is still forced over foreground roofs: " + str(source.name))
			quit(1)
			return
		if art.global_position.distance_to(expected.origin) > .01 or not art.global_transform.x.is_equal_approx(expected.x) or not art.global_transform.y.is_equal_approx(expected.y):
			push_error("Depth correction moved the pillar away from its deck socket")
			quit(1)
			return
		if art.material != district.occlusion or art.use_parent_material:
			push_error("Ground pillars lost their pedestrian visibility material")
			quit(1)
			return
		count += 1
	if count != 27:
		push_error("Expected all 27 pillars to join street depth sorting")
		quit(1)
		return
	print("PASS:27 pillars sorted at street feet; deck sockets, sprite transforms and pedestrian fade preserved")
	world.queue_free()
	await process_frame
	quit(0)
