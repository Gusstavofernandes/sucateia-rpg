extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var area := world.get_node("PassagemAmarrasDistrict")
	if not area.has_node("ArtIntegration"):push_error("Amarras selected production art not integrated");quit(1);return
	var manifest: Array=JSON.parse_string(FileAccess.get_file_as_string("res://assets/reconstruction/amarras_parallel/manifest.json"));var selected: Dictionary={}
	for entry in manifest:
		assert(FileAccess.get_sha256("res://"+entry.path)==entry.sha256,"Selected art changed after integration")
		selected["res://"+entry.path]=entry.sha256
	var used: Dictionary={};var nodes: Array[Node]=[world]
	while not nodes.is_empty():
		var node: Node=nodes.pop_back();nodes.append_array(node.get_children())
		if node is Sprite2D and node.texture and selected.has(node.texture.resource_path):
			assert(node.scale.x==node.scale.y and node.scale.x>0,"Generated art was deformed or mirrored")
			assert(node.get_meta("selection_sha256","")==selected[node.texture.resource_path],"Wrong asset selection")
			used[node.texture.resource_path]=true
	assert(used.size()==8,"Missing a selected production asset")
	var query := PhysicsShapeQueryParameters2D.new();var probe := CircleShape2D.new();probe.radius=4;query.shape=probe;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state;var structures := world.get_node("Structures/AmarrasInfrastructure")
	for machine in structures.get_children():
		if not machine.has_node("PhysicalBase"):continue
		var point: Vector2=machine.position+machine.get_meta("base_center");query.transform=Transform2D(0,point)
		assert(not space.intersect_shape(query,1).is_empty(),"Walkable solid machine base "+str(machine.name))
		assert(world.is_walkable(machine.position),"Ground support outside land "+str(machine.name))
	for chain in area.get_node("FunctionalChains").get_children():
		var endpoints: PackedVector2Array=chain.get_meta("endpoints")
		for i in range(2):
			var node_name: String=chain.get_meta("from_node" if i==0 else "to_node");var terminal: String=chain.get_meta("from_port" if i==0 else "to_port")
			var port: Marker2D=structures.get_node(node_name+"/Ports/"+terminal)
			assert(endpoints[i].distance_to(port.global_position)<.1,"Detached chain endpoint")
		assert(chain.get_child_count()>=6,"Missing visible forged links")
		for index in [0,chain.get_child_count()-3]:
			var visible: Line2D=chain.get_child(index);var bounds := Rect2(visible.points[0],Vector2.ZERO)
			for point in visible.points:bounds=bounds.expand(point)
			var endpoint: Vector2=endpoints[0] if index==0 else endpoints[1]
			assert(bounds.get_center().distance_to(endpoint)<2.5,"Visible chain does not reach its terminal")
	query.shape.radius=11
	for arrival in area.get_node("SafeArrivals").get_children():
		query.transform=Transform2D(0,arrival.position);assert(space.intersect_shape(query,1).is_empty(),"Unsafe Amarras arrival")
	var kiosk: Node2D=structures.get_node("PostoDeControle");var doorway: Vector2=kiosk.get_node("Ports/door_s").global_position+Vector2(0,35)
	query.transform=Transform2D(0,doorway);assert(space.intersect_shape(query,1).is_empty() and world.is_walkable(doorway),"Kiosk south access blocked")
	var platform: Node2D=structures.get_node("PlataformaDeTransferencia");var center: Vector2=platform.get_node("Ports/step_s").global_position+Vector2(0,12)
	query.transform=Transform2D(0,center);assert(space.intersect_shape(query,1).is_empty() and world.is_walkable(center),"Cargo platform access blocked")
	var outline: PackedVector2Array=area.get_meta("land_polygon");var surface := 0.
	for i in range(outline.size()):surface+=outline[i].cross(outline[(i+1)%outline.size()])*.5
	assert(outline.size()==32 and absf(surface)<1400000.,"Oversized rounded Amarras footprint")
	var floor: TileMapLayer=area.get_node("AmarrasFloor")
	for y in range(-180,961,12):
		for x in range(3912,5581,12):
			var sample := Vector2(x,y)
			if Geometry2D.is_point_in_polygon(sample,outline):assert(floor.get_cell_source_id(floor.local_to_map(sample))!=-1,"Physical land missing visual floor coverage")
	assert("bool inside=false" in floor.material.shader.code,"No polygon clipping on boundary tiles")
	assert(not world.has_node("EngrenopolisDistrict"),"Unapproved next district")
	print("PASS: eight hashed art selections, coherent scale, physical machine bases, connected chains, safe arrivals and kiosk/platform approaches; only Amarras")
	world.queue_free();await process_frame;quit(0)
