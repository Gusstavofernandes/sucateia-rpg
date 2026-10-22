extends SceneTree
func _initialize() -> void:call_deferred("run")
func permitted_pipe(node: Node,path: String) -> bool:
	return node is Sprite2D and node.texture.resource_path.ends_with("/pipe.png") and (path.begins_with("Sucateia/ForjasRasasDistrict/GroundIntegration/") or path.begins_with("Sucateia/ForjasRasasDistrict/Drainage/"))
func compare(old: Node,current: Node,path: String) -> bool:
	if permitted_pipe(old,path):return true
	if current==null or old.get_class()!=current.get_class():push_error("Missing preserved node "+path);return false
	if old is Node2D and old.transform!=current.transform:push_error("Preserved transform changed "+path);return false
	if old is CanvasItem and (old.z_index!=current.z_index or old.y_sort_enabled!=current.y_sort_enabled):push_error("Preserved ordering changed "+path);return false
	if old is Sprite2D and (old.texture.resource_path!=current.texture.resource_path or old.modulate!=current.modulate):push_error("Preserved artwork changed "+path);return false
	if old is CollisionPolygon2D and old.polygon!=current.polygon:push_error("Preserved collision changed "+path);return false
	if old is CollisionShape2D and var_to_str(old.shape)!=var_to_str(current.shape):push_error("Preserved footprint changed "+path);return false
	if old is TileMapLayer:
		if old.get_used_cells()!=current.get_used_cells():push_error("Floor territory changed "+path);return false
		for cell in old.get_used_cells():
			if old.get_cell_source_id(cell)!=current.get_cell_source_id(cell) or old.get_cell_atlas_coords(cell)!=current.get_cell_atlas_coords(cell):push_error("Floor cells changed "+path);return false
	for child in old.get_children():
		if not compare(child,current.get_node_or_null(str(child.name)),path+"/"+str(child.name)):return false
	return true
func run() -> void:
	var old: Node=load("res://tools/checkpoints/sucateia_before_forjas_refinement.tscn").instantiate();var current: Node=load("res://maps/sucateia/sucateia.tscn").instantiate()
	var good := compare(old,current,"Sucateia")
	old.free();current.free()
	if good:print("PASS: current city, 19 Forjas buildings, four floor territories, coastal contour and underground access placements preserved; only named Forjas ground pipes replaced")
	quit(0 if good else 1)
