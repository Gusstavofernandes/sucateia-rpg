extends SceneTree
func _initialize() -> void:call_deferred("run")
func compare_nodes(old: Node, current: Node, path: String) -> void:
	assert(current!=null,"Missing approved node "+path)
	assert(old.get_class()==current.get_class(),"Approved node type changed "+path)
	if old is Node2D:assert(old.transform==current.transform,"Approved transform changed "+path)
	if old is Sprite2D:
		assert(old.texture.resource_path==current.texture.resource_path and old.modulate==current.modulate and old.z_index==current.z_index,"Approved sprite altered "+path)
	if old is CollisionPolygon2D:assert(old.polygon==current.polygon,"Approved collision coast changed "+path)
	if old is CollisionShape2D:
		assert(var_to_str(old.shape)==var_to_str(current.shape),"Approved shape changed "+path)
	if old is TileMapLayer:
		assert(old.get_used_cells()==current.get_used_cells(),"Approved floor cells changed "+path)
		for cell in old.get_used_cells():assert(old.get_cell_source_id(cell)==current.get_cell_source_id(cell) and old.get_cell_atlas_coords(cell)==current.get_cell_atlas_coords(cell))
	for child in old.get_children():
		if child is Camera2D:continue
		compare_nodes(child,current.get_node_or_null(str(child.name)),path+"/"+str(child.name))
func run() -> void:
	var old: Node2D=load("res://tools/checkpoints/sucateia_before_forjas.tscn").instantiate()
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate()
	assert(world.has_node("ForjasRasasDistrict"),"Forjas absent")
	compare_nodes(old,world,"Sucateia")
	assert(old.get_node("LowerCoastReworked").get_meta("land_polygon")==world.get_node("LowerCoastReworked").get_meta("land_polygon"))
	root.add_child(world);await physics_frame;await physics_frame
	var space := world.get_world_2d().direct_space_state
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	var tested := 0
	for building in world.get_node("Structures/ForjasIndustrialArchitecture").get_children():
		if not building is Node2D or not building.has_meta("function"):continue
		var bodies := building.find_children("*","StaticBody2D",true,false)
		assert(not bodies.is_empty())
		query.transform=Transform2D(0,bodies[0].global_position)
		assert(not space.intersect_shape(query,1).is_empty(),"Unblocked industrial base")
		tested+=1
	assert(tested==19)
	assert(not world.is_walkable(Vector2(3950,-1300)))
	print("PASS: all approved scene nodes, three floors, coast and artwork preserved; 19 industrial bases blocked")
	old.free();world.queue_free();await process_frame;quit(0)
