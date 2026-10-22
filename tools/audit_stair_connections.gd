extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func run() -> void:
	var world: Node2D = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	current_scene = world
	await physics_frame
	await physics_frame
	var rows: Array = []
	var query := PhysicsShapeQueryParameters2D.new()
	var circle := CircleShape2D.new()
	circle.radius = 11
	query.shape = circle
	query.collision_mask = 1
	for sprite in world.find_children("*", "Sprite2D", true, false):
		if not sprite.texture or not sprite.texture.resource_path.ends_with("/stairs.png"):
			continue
		var top: Vector2 = sprite.to_global(Vector2(-4,-79))
		var bottom: Vector2 = sprite.to_global(Vector2(-3,79))
		var blocked: Array = []
		for point in [top,bottom]:
			query.transform = Transform2D(0,point)
			blocked.append(not world.get_world_2d().direct_space_state.intersect_shape(query,1).is_empty())
		rows.append({"path":str(world.get_path_to(sprite)), "visible":sprite.is_visible_in_tree(), "top":[top.x,top.y], "bottom":[bottom.x,bottom.y], "blocked_surface":blocked, "surface_floor":[world.is_surface_walkable(top),world.is_surface_walkable(bottom)]})
	var deck: Node2D = world.get_node("CabosDistrict")
	var connections: Array = []
	for access in deck.get_node("Accesses").get_children():
		var ground: Vector2 = access.get_meta("surface_arrival")
		var upper: Vector2 = access.get_meta("elevated_arrival")
		query.transform = Transform2D(0,ground)
		query.collision_mask = 1
		var ground_free := world.get_world_2d().direct_space_state.intersect_shape(query,1).is_empty()
		query.transform = Transform2D(0,upper)
		query.collision_mask = 4
		var upper_free := world.get_world_2d().direct_space_state.intersect_shape(query,1).is_empty()
		connections.append({"access":str(access.name),"ground":[ground.x,ground.y],"upper":[upper.x,upper.y],"ground_free":ground_free,"upper_free":upper_free,"upper_painted_navigation":deck.is_walkable(upper)})
	var report := {"player_radius":11,"old_stair_sprites":rows,"cabos_accesses":connections,"coast_opening":{"left":1440,"right":1584,"center_x":1512,"wall_y":1418,"top":[1512,1378],"bottom":[1512,1472]}}
	var file := FileAccess.open("res://tools/stair_physical_audit.json",FileAccess.WRITE)
	file.store_string(JSON.stringify(report,"\t"))
	print("PASS:physical stair inventory saved;",rows.size()," existing sprites;3 elevated access pairs;coastal opening144px")
	world.queue_free()
	await process_frame
	quit(0)
