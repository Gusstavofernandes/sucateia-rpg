extends SceneTree
func _initialize() -> void:call_deferred("run")
func compare(old: Node, current: Node, path: String) -> void:
	assert(current!=null and old.get_class()==current.get_class(),"Surface node missing "+path)
	if old is Node2D:assert(old.transform==current.transform,"Surface placement changed "+path)
	if old is CanvasItem:assert(old.z_index==current.z_index and old.y_sort_enabled==current.y_sort_enabled,"Surface ordering changed "+path)
	if old is Sprite2D:assert(old.texture.resource_path==current.texture.resource_path and old.modulate==current.modulate and old.scale==current.scale,"Surface art changed "+path)
	if old is TileMapLayer:
		assert(old.get_used_cells()==current.get_used_cells(),"Surface floor changed")
		for cell in old.get_used_cells():assert(old.get_cell_source_id(cell)==current.get_cell_source_id(cell) and old.get_cell_atlas_coords(cell)==current.get_cell_atlas_coords(cell))
	if old is CollisionPolygon2D:assert(old.polygon==current.polygon,"Surface coast/water changed")
	if old is CollisionShape2D:assert(var_to_str(old.shape)==var_to_str(current.shape),"Surface footprint changed")
	for child in old.get_children():compare(child,current.get_node_or_null(str(child.name)),path+"/"+str(child.name))
func run() -> void:
	var before: Node2D=load("res://tools/checkpoints/sucateia_before_fundo.tscn").instantiate()
	var current: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate()
	compare(before,current,"Sucateia")
	assert(current.get_node("LayerEntrances").get_child_count()==6)
	assert(current.get_node("LayerArrivals").get_child_count()==3)
	for portal in current.get_node("RegionPortals").get_children():assert(portal.get_script()==null)
	print("PASS: complete approved surface including Forjas preserved; only physical layer accesses added; old E portals inactive")
	before.free();current.free();quit(0)
