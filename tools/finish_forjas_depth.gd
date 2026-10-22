extends SceneTree
var world: Node2D
func _initialize() -> void:call_deferred("run")
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	var district: Node2D=world.get_node("ForjasRasasDistrict")
	var structures: Node2D=world.get_node("Structures")
	for pair in [["IndustrialArchitecture","ForjasIndustrialArchitecture"],["StockAndService","ForjasStockAndService"]]:
		var group: Node2D=district.get_node_or_null(pair[0])
		if group:group.reparent(structures,true);group.name=pair[1]
	district.set_meta("architecture_path",NodePath("../Structures/ForjasIndustrialArchitecture"))
	assert(structures.y_sort_enabled and structures.get_node("ForjasIndustrialArchitecture").y_sort_enabled)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world)
	var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS localized depth fix saved=",error);quit(error)
