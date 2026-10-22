extends SceneTree
func _initialize() -> void:call_deferred("run")
func settle() -> void:
	for i in range(10):await process_frame
	await physics_frame;await physics_frame
func press(code: Key) -> void:
	var event := InputEventKey.new();event.keycode=code;event.physical_keycode=code;event.pressed=true;Input.parse_input_event(event);Input.flush_buffered_events();await settle()
	event=InputEventKey.new();event.keycode=code;event.physical_keycode=code;event.pressed=false;Input.parse_input_event(event);Input.flush_buffered_events();await settle()
func safe(world: Node2D, player: CharacterBody2D) -> bool:
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1;query.transform=Transform2D(0,player.global_position)
	return world.is_walkable(player.global_position) and player.get_world_2d().direct_space_state.intersect_shape(query,1).is_empty()
func run() -> void:
	var travel := root.get_node_or_null("LayerTravel")
	if not travel:push_error("Physical underground layer access unavailable");quit(1);return
	change_scene_to_file("res://maps/sucateia/sucateia.tscn");await settle()
	var player: CharacterBody2D=current_scene.get_node("Structures/Player");player.set_physics_process(false)
	await press(KEY_F);await press(KEY_E)
	assert(travel.current_layer=="surface" and current_scene.name=="Sucateia","Remote/global key changed layer")
	for id in ["PocoVelho","DocaLeste","ForjasManutencao"]:
		var entry: Area2D=current_scene.get_node("LayerEntrances/"+id);player=current_scene.get_node("Structures/Player");player.set_physics_process(false);player.global_position=entry.global_position;await settle()
		assert(entry.nearby and safe(current_scene,player))
		if not current_scene.get_node("MapInfo/Panel/District").text.contains("SUPERFÍCIE"):
			push_error("Access HUD incorrectly claims player is underground");quit(1);return
		await press(KEY_F)
		assert(travel.current_layer=="underground" and current_scene.name=="FundoFerro")
		player=current_scene.get_node("Structures/Player");player.set_physics_process(false)
		assert(get_nodes_in_group("player").size()==1 and safe(current_scene,player))
		var expected: Vector2=current_scene.get_node("LayerArrivals/"+id).position
		assert(player.position.distance_to(expected)<1 and player.spawn_point.distance_to(expected)<1)
		player.position+=Vector2(24,0);await press(KEY_R);assert(player.position.distance_to(expected)<1)
		await press(KEY_E);assert(travel.current_layer=="underground","Legacy E transition reintroduced")
		await press(KEY_F)
		assert(travel.current_layer=="surface" and current_scene.name=="Sucateia")
		player=current_scene.get_node("Structures/Player");player.set_physics_process(false)
		assert(get_nodes_in_group("player").size()==1 and safe(current_scene,player))
		assert(player.position.distance_to(current_scene.get_node("LayerArrivals/"+id).position)<1)
		print("FUNDO access ",id," F ida/volta, one player, safe spawn and R")
	assert(travel.transition_count==6)
	print("PASS: three physical underground accesses entered and returned with F; E inactive, spawns/R safe and one player")
	quit(0)
