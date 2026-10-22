extends "res://tests/test_cabos_art_contacts.gd"
func dock_painted(point: Vector2,artworks: Array) -> bool:
	for entry in artworks:
		var sprite: Node2D=entry[0];var source: Image=entry[1]
		if not sprite.is_visible_in_tree():continue
		if sprite is Polygon2D:
			var local := sprite.to_local(point)
			if not Geometry2D.is_point_in_polygon(local,sprite.polygon):continue
			var shape := Transform2D(sprite.polygon[1]-sprite.polygon[0],sprite.polygon[2]-sprite.polygon[0],sprite.polygon[0])
			var uv := Transform2D(sprite.uv[1]-sprite.uv[0],sprite.uv[2]-sprite.uv[0],sprite.uv[0])
			var pixel: Vector2=uv*(shape.affine_inverse()*local)
			if Rect2(Vector2.ZERO,source.get_size()).has_point(pixel) and source.get_pixelv(Vector2i(pixel)).a>.7:return true
			continue
		var region: Rect2=sprite.region_rect if sprite.region_enabled else Rect2(Vector2.ZERO,source.get_size())
		var pixel := sprite.to_local(point)+region.size*.5+region.position
		if not region.has_point(pixel):continue
		if source.get_pixelv(Vector2i(pixel)).a>.7:return true
	return false
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	var district: Node2D=world.get_node("DocasDistrict");var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false);district.set_physics_process(false)
	var artworks: Array=[];var images: Dictionary={}
	for sprite in district.get_node("WorkingDecks").get_children():
		if not sprite is Sprite2D or String(sprite.name)=="RampaNavalLeste":continue
		var path: String=sprite.texture.resource_path
		if not images.has(path):
			var source: Image=sprite.texture.get_image();if source.is_compressed():source.decompress()
			images[path]=source
		artworks.append([sprite,images[path]])
	# Concurrent approach finish may hide old deck art: audit the actually visible seam.
	if world.has_node("PortApproachFinish"):
		for sprite in world.get_node("PortApproachFinish").get_children():
			if not (sprite is Sprite2D or sprite is Polygon2D) or not sprite.texture:continue
			var source: Image=sprite.texture.get_image();if source.is_compressed():source.decompress()
			artworks.append([sprite,source])
	var query := PhysicsShapeQueryParameters2D.new();var circle := CircleShape2D.new();circle.radius=11;query.shape=circle;query.collision_mask=1;var space := world.get_world_2d().direct_space_state;var sampled := 0
	for y in range(280,1950,10):
		for x in range(2240,3320,10):
			var point := Vector2(x,y)
			if not district.is_walkable(point):continue
			query.transform=Transform2D(0,point);query.exclude=district.water_exclusions(point)
			if not space.intersect_shape(query,1).is_empty():continue
			if not check(dock_painted(point,artworks),"Docas navigable center lacks floor paint "+str(point)):return
			sampled+=1
	for object in world.get_node("Structures/DocasPortFunctions").get_children():
		if not object.has_meta("contact_rectangles_native"):continue
		var sprite: Sprite2D=object.get_node("Artwork")
		for bounds in object.get_meta("contact_rectangles_native"):
			for native in [bounds.get_center(),bounds.position+Vector2(3,3),bounds.end-Vector2(3,3)]:
				var foot := sprite.to_global(native-Vector2(sprite.texture.get_size())*.5)
				if not check(district.is_walkable(foot) and dock_painted(foot,artworks),"Port equipment foot lacks dry floor "+str(object.name)+" "+str(foot)):return
	var barge: Sprite2D=world.get_node("Structures/DocasPortFunctions/BarcacaAncorada/Artwork")
	for pair in [["AmarraProa",Vector2(232,420)],["AmarraPopa",Vector2(1372,650)]]:
		var rope: Line2D=district.get_node("WorkingRopes/"+pair[0]);var socket := barge.to_global(pair[1]-Vector2(barge.texture.get_size())*.5)
		if not check(rope.points[0].distance_to(socket)<.1,"Mooring floats off boat socket"):return
	var slip: Sprite2D=district.get_node("WorkingDecks/RampaNavalLeste");var socket := slip.to_global(slip.get_meta("dry_socket_native")-Vector2(slip.texture.get_size())*.5);var tip := slip.to_global(slip.get_meta("water_tip_native")-Vector2(slip.texture.get_size())*.5)
	if not check(district.is_walkable(socket) and not world.is_walkable(tip),"Naval launch does not reach from dry platform to actual water"):return
	for point in [Vector2(2735,1910),Vector2(2500,1575),Vector2(1800,1100)]:
		player.position=point;district.update_player_water();var exceptions: Array=player.get_collision_exceptions()
		for body in district.water_bodies:
			if not check(exceptions.has(body)==district.is_walkable(point),"Water exclusions leak outside dock floors"):return
	player.position=Vector2(3170,1810);district.update_player_water()
	if not check(player.move_and_collide(Vector2(120,0))!=null,"Local guard permits stepping into harbor when old water excluded"):return
	# R must be safe when returning from inland, not only while already in docks.
	player.spawn_point=Vector2(2735,1910);player.position=Vector2(1800,1100);district.update_player_water()
	var reset := InputEventKey.new();reset.keycode=KEY_R;reset.pressed=true;player._unhandled_input(reset)
	if not check(district.process_physics_priority<player.process_physics_priority,"Water exceptions refresh after first respawn movement"):return
	district.set_physics_process(true);player.set_physics_process(true);await physics_frame;await physics_frame
	if not check(player.position.distance_to(player.spawn_point)<.1,"Inland R displaced player from dry dock landing"):return
	for body in district.water_bodies:
		if not check(player.get_collision_exceptions().has(body),"Inland R water body still active"):return
	if not check(sampled>2000,"Incomplete dock paint audit"):return
	print("PASS: ",sampled," safe navigable centers have PNG floor paint; equipment dry contacts; mooring sockets; launch reaches water; exceptions limited and local harbor guard solid")
	world.queue_free();await process_frame;quit(0)
