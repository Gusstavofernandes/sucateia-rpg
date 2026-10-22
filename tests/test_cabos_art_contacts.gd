extends SceneTree
func _initialize() -> void:call_deferred("run")
func check(condition: bool,message: String) -> bool:
	if not condition:push_error(message);quit(1)
	return condition
func painted(point: Vector2,artworks: Array) -> bool:
	for entry in artworks:
		var node: Sprite2D=entry[0];var image: Image=entry[1];var pixel := node.to_local(point)+Vector2(image.get_size())*.5
		var bounds: Rect2=entry[2]
		if not bounds.has_point(pixel):continue
		var at := Vector2i(pixel)
		# Grates deliberately have transparent holes. A 3-native-pixel metal neighbor
		# is within the painted grate, not a larger invisible navigation platform.
		for offset in [Vector2i.ZERO,Vector2i(3,0),Vector2i(-3,0),Vector2i(0,3),Vector2i(0,-3)]:
			if bounds.has_point(Vector2(at+offset)) and image.get_pixelv(at+offset).a>.7:return true
	return false
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	var district: Node2D=world.get_node("CabosDistrict");var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var query := PhysicsShapeQueryParameters2D.new();var circle := CircleShape2D.new();circle.radius=11;query.shape=circle;query.collision_mask=1;var space := world.get_world_2d().direct_space_state;var count := 0
	for tower in district.get_node("StructuralSupports").get_children():
		if not tower.has_meta("ground_contact"):continue
		var foot: Vector2=tower.get_meta("ground_contact");query.transform=Transform2D(0,foot)
		if not check(not space.intersect_shape(query,1).is_empty(),"Solid support has no surface collision "+str(tower.name)):return
		count+=1
		if String(tower.name).begins_with("CasaTorre"):
			var door: Vector2=district.get_node("Landings/SoleiraCasa").position
			if not check(foot.y>door.y+175,"House support stops at elevated cabin instead of street"):return
	var artworks: Array=[]
	for node in district.get_node("ElevatedDecks").get_children():
		if not node is Sprite2D:continue
		var image: Image=node.texture.get_image();if image.is_compressed():image.decompress()
		var path: String=node.texture.resource_path;var bounds: Rect2
		if path.ends_with("main_deck_ew_wide.png"):bounds=Rect2(155,155,1285,535)
		elif path.ends_with("walkway.png"):bounds=Rect2(80,30,130,216)
		elif path.ends_with("walkway_t_junction_clean.png"):
			artworks.append([node,image,Rect2(50,640,1440,87)]);bounds=Rect2(725,170,94,550)
		elif path.ends_with("suspension_bridge_ew.png"):bounds=Rect2(60,320,2045,150)
		else:continue
		artworks.append([node,image,bounds])
	query.collision_mask=4;var sampled := 0
	for y in range(-1040,-60,8):
		for x in range(-454,1954,8):
			var point := Vector2(x,y)
			if not district.is_walkable(point):continue
			query.transform=Transform2D(0,point)
			if not space.intersect_shape(query,1).is_empty():continue
			if not check(painted(point,artworks),"Navigable player center lacks painted deck at "+str(point)):return
			sampled+=1
	if not check(count==27 and sampled>1500,"Incomplete support/paint audit"):return
	print("PASS:27 solid surface support bases; house supports reach street;",sampled," safe elevated centers backed by actual PNG floor paint")
	world.queue_free();await process_frame;quit(0)
