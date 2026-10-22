extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func fail(message: String) -> void:
	push_error(message)
	quit(1)

func run() -> void:
	var world: Node2D = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	current_scene = world
	await physics_frame
	await physics_frame
	var flights := world.find_children("*","Sprite2D",true,false).filter(func(n):return n.has_meta("fitted_stair"))
	if flights.size()!=4:
		fail("Three deck accesses and coastal wall need four fitted flights using two purpose-built assets")
		return
	var player: CharacterBody2D = world.get_node("Structures/Player")
	player.set_physics_process(false)
	var query := PhysicsShapeQueryParameters2D.new()
	var circle := CircleShape2D.new()
	circle.radius=11
	query.shape=circle
	var deck: Node2D=world.get_node("CabosDistrict")
	for flight in flights:
		var ports: PackedVector2Array = flight.get_meta("ports_pixels")
		var targets: PackedVector2Array = flight.get_meta("ports_world")
		var image: Image = flight.texture.get_image()
		if image.is_compressed():image.decompress()
		for i in range(2):
			var actual: Vector2=flight.to_global(ports[i]-Vector2(image.get_size())*.5)
			if actual.distance_to(targets[i])>.01 or image.get_pixelv(Vector2i(ports[i])).a<.9:
				fail("Docking seam mismatch or transparent end tread: "+str(flight.name))
				return
		if String(flight.name).begins_with("Deck"):
			var access: Node=deck.get_node("Accesses/"+String(flight.name).trim_prefix("Deck"))
			var upper: Vector2=access.get_meta("elevated_arrival")
			var ground: Vector2=access.get_meta("surface_arrival")
			if targets[1].distance_to(ground)>.01 or not deck.is_walkable(upper) or absf(targets[0].x-upper.x)>.01:
				fail("Stair deviates from its existing F access")
				return
			for pair in [[ground,1],[upper,4]]:
				query.collision_mask=pair[1]
				query.transform=Transform2D(0,pair[0])
				if not world.get_world_2d().direct_space_state.intersect_shape(query,1).is_empty():
					fail("Blocked stair arrival: "+str(flight.name))
					return
		else:
			player.navigation_layer="surface"
			player.collision_mask=1
			for x in [1490.,1512.,1534.]:
				player.position=Vector2(x,targets[0].y-12)
				for y in range(int(targets[0].y)-12,int(targets[1].y)+13,2):
					var point:=Vector2(x,y)
					if not world.is_surface_walkable(point) or player.move_and_collide(point-player.position)!=null:
						fail("Coastal stair physically blocked at "+str(point))
						return
				for y in range(int(targets[1].y)+12,int(targets[0].y)-13,-2):
					if player.move_and_collide(Vector2(x,y)-player.position)!=null:
						fail("Coastal stair return blocked")
						return
	print("PASS:4 fitted stairflights, 8 opaque docking ports within0.01px,3 safe F access pairs,coast crossed in3 lanes ida/volta")
	world.queue_free()
	await process_frame
	quit(0)
