extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	current_scene=world
	await physics_frame
	await physics_frame
	var finish: Node2D=world.get_node_or_null("PortApproachFinish")
	if finish==null:
		push_error("Port approach needs a clear grounded quay and stone/timber connection")
		quit(1)
		return
	var removed: Array=finish.get_meta("hidden_legacy_art")
	if removed.size()<8:
		push_error("Buried approach still has stacked grate and pipe overlays")
		quit(1)
		return
	for path in removed:
		if world.get_node(path).visible:
			push_error("Legacy overlap remains visible")
			quit(1)
			return
	var apron: Polygon2D=finish.get_node("StoneQuay")
	for y in range(1130,1540,12):
		for x in range(1980,2290,12):
			var point:=Vector2(x,y)
			if Geometry2D.is_point_in_polygon(point,apron.polygon) and not world.is_surface_walkable(point):
				push_error("Quay art invents land over water: "+str(point))
				quit(1)
				return
	var district: Node2D=world.get_node("DocasDistrict")
	var threshold: Sprite2D=finish.get_node("StoneToTimberThreshold")
	var image: Image=threshold.texture.get_image()
	if image.is_compressed():image.decompress()
	var player: CharacterBody2D=world.get_node("Structures/Player")
	player.set_physics_process(false)
	for y in [1360.,1370.,1380.]:
		player.position=Vector2(2240,y)
		for x in range(2240,2351,2):
			var pixel:=Vector2i(threshold.to_local(Vector2(x,y))+Vector2(image.get_size())*.5)
			if pixel.x<0 or pixel.x>=image.get_width() or pixel.y<0 or pixel.y>=image.get_height() or image.get_pixelv(pixel).a<.9:
				push_error("Port entry lacks actual painted surface")
				quit(1)
				return
			district.update_player_water()
			if not world.is_walkable(Vector2(x,y)) or player.move_and_collide(Vector2(x,y)-player.position)!=null:
				push_error("Entry to port blocked at "+str(player.position))
				quit(1)
				return
		for x in range(2350,2239,-2):
			district.update_player_water()
			if player.move_and_collide(Vector2(x,y)-player.position)!=null:
				push_error("Return from port blocked")
				quit(1)
				return
	print("PASS:cleared legacy overlays;quay clipped to existing land;three entry lanes crossed ida/volta")
	world.queue_free()
	await process_frame
	quit(0)
