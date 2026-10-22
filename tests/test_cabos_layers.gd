extends SceneTree
func _initialize() -> void:call_deferred("run")
func check(condition: bool,message: String) -> bool:
	if not condition:push_error(message);quit(1)
	return condition
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	if not check(world.has_node("CabosDistrict"),"Cabos elevated continuous layer missing"):return
	var district: Node2D=world.get_node("CabosDistrict");var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	if not check(district.get_node("Accesses").get_child_count()==3 and get_nodes_in_group("player").size()==1,"Cabos needs three accesses and one player"):return
	var event := InputEventKey.new();event.keycode=KEY_F;event.pressed=true
	var probe := CircleShape2D.new();probe.radius=11;var query := PhysicsShapeQueryParameters2D.new();query.shape=probe;query.collision_mask=4
	var space := world.get_world_2d().direct_space_state
	for access in district.get_node("Accesses").get_children():
		var ground: Vector2=access.get_meta("surface_arrival");var elevated: Vector2=access.get_meta("elevated_arrival");player.position=ground
		district._process(0.)
		if not check(district.surface_avatar.visible and district.surface_avatar.global_position==player.get_node("Sprite").global_position,"Surface avatar unreadable under access structure"):return
		access._unhandled_input(event)
		if not check(player.get("navigation_layer")=="cabos" and player.position==elevated and player.collision_mask==4 and player.z_index==8,"Cabos ascent failed "+str(access.name)):return
		district._process(0.)
		if not check(not district.surface_avatar.visible,"Lower avatar readout remains visible on upper layer"):return
		query.transform=Transform2D(0,elevated)
		if not check(world.is_walkable(elevated) and space.intersect_shape(query,1).is_empty(),"Unsafe elevated arrival "+str(access.name)):return
		player.position=elevated+Vector2(12,0);var reset := InputEventKey.new();reset.keycode=KEY_R;reset.pressed=true;player._unhandled_input(reset)
		if not check(player.position==elevated and player.get("navigation_layer")=="cabos","R lost safe elevated spawn"):return
		access._unhandled_input(event)
		if not check(player.get("navigation_layer")=="surface" and player.position==ground and player.collision_mask==1 and player.z_index==0,"Cabos descent failed "+str(access.name)):return
		print("CABOS access ",access.name," F ida/volta, safe layer spawn/R")
	if not check(not district.change_layer(district.get_node("Accesses/Mercado")),"Remote elevation change was accepted"):return
	print("PASS: three same-scene Cabos accesses F ida/volta, per-layer collision/depth, safe R spawns and one player")
	world.queue_free();await process_frame;quit(0)
