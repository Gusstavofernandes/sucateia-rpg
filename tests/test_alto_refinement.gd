extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	if not world.has_node("AltoLixoDistrict/ResidentialFinish"):
		push_error("Alto-Lixo still lacks residential finishing and coherent terraces");quit(1);return
	var before: Node2D=load("res://tools/checkpoints/sucateia_before_alto_refinement.tscn").instantiate()
	for path in ["MarketDistrict/MarketFloor","AltoLixoDistrict/AltoFloor","Ground/TerraceFloor"]:
		var old: TileMapLayer=before.get_node(path);var current: TileMapLayer=world.get_node(path)
		assert(old.get_used_cells().size()==current.get_used_cells().size(),"Terrain extent changed "+path)
		for cell in old.get_used_cells():assert(old.get_cell_source_id(cell)==current.get_cell_source_id(cell) and old.get_cell_atlas_coords(cell)==current.get_cell_atlas_coords(cell))
	assert(before.get_node("LowerCoastReworked").get_meta("land_polygon")==world.get_node("LowerCoastReworked").get_meta("land_polygon"),"Approved coast altered")
	for name in ["WestCoastalBarrier","EastCoastalBarrier","SouthCoastalBarrier"]:
		assert(before.get_node(name).get_child(0).polygon==world.get_node(name).get_child(0).polygon)
	for home in before.get_node("AltoLixoDistrict/Residences").get_children():
		assert(world.get_node("AltoLixoDistrict/Residences/"+str(home.name)).transform==home.transform,"Existing home moved")
	var finish: Node2D=world.get_node("AltoLixoDistrict/ResidentialFinish")
	assert(finish.get_node("TerraceLandings").get_child_count()==4)
	assert(finish.get_meta("additional_houses")>=5)
	assert(get_nodes_in_group("player").size()==1)
	print("PASS: Alto residential finishing, four terrace landings, old homes retained, three floors and approved coast unchanged")
	before.free();world.queue_free();await process_frame;quit(0)
