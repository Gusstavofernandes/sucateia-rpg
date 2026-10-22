extends SceneTree
func _initialize() -> void:call_deferred("run")
func same_material(a: Material,b: Material) -> bool:
	if a==null or b==null:return a==b
	if a.get_class()!=b.get_class():return false
	if a is ShaderMaterial:
		if a.shader.resource_path!=b.shader.resource_path:return false
		for uniform in a.shader.get_shader_uniform_list():
			var old_value: Variant=a.get_shader_parameter(uniform.name);var new_value: Variant=b.get_shader_parameter(uniform.name)
			if old_value is Resource:
				if not new_value is Resource or old_value.resource_path!=new_value.resource_path:return false
			elif old_value!=new_value:return false
	return true
func compare(old: Node,current: Node,path: String) -> bool:
	if current==null or old.get_class()!=current.get_class():push_error("Missing approved node "+path);return false
	if old is Node2D and old.transform!=current.transform:push_error("Approved transform changed "+path);return false
	if old is CanvasItem and (old.z_index!=current.z_index or old.y_sort_enabled!=current.y_sort_enabled):push_error("Approved ordering changed "+path);return false
	if old is CanvasItem and not same_material(old.material,current.material):push_error("Approved material/parameters changed "+path);return false
	if old is Sprite2D and (old.texture.resource_path!=current.texture.resource_path or old.modulate!=current.modulate):push_error("Approved sprite changed "+path);return false
	if old is Polygon2D and old.polygon!=current.polygon:push_error("Approved contour changed "+path);return false
	if old is CollisionPolygon2D and old.polygon!=current.polygon:push_error("Approved collision changed "+path);return false
	if old is CollisionShape2D and var_to_str(old.shape)!=var_to_str(current.shape):push_error("Approved footprint changed "+path);return false
	if old is TileMapLayer:
		if old.get_used_cells()!=current.get_used_cells():push_error("Approved floor territory changed "+path);return false
		for cell in old.get_used_cells():
			if old.get_cell_source_id(cell)!=current.get_cell_source_id(cell) or old.get_cell_atlas_coords(cell)!=current.get_cell_atlas_coords(cell):push_error("Approved floor cell changed "+path);return false
	for child in old.get_children():
		if not compare(child,current.get_node_or_null(str(child.name)),path+"/"+str(child.name)):return false
	return true
func run() -> void:
	var old: Node=load("res://tools/checkpoints/sucateia_before_amarras.tscn").instantiate();var current: Node=load("res://maps/sucateia/sucateia.tscn").instantiate()
	var good := compare(old,current,"Sucateia");old.free();current.free()
	if good:print("PASS: all existing city floors, contours, approved sprites, Forjas network, physics and access placements preserved")
	quit(0 if good else 1)
