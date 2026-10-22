extends SceneTree
func _initialize() -> void:call_deferred("run")
func own(node: Node,world: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child,world)
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	var sea: Polygon2D=world.get_node("ForjasRasasDistrict/RegionalEdgeContext/CostaIndustrialLeste")
	var polygon: PackedVector2Array=sea.polygon;polygon[6].y=4000;polygon[7].y=4000;sea.polygon=polygon
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world,world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS sea context ends beyond camera saved=",error," no playable geometry change")
	world.queue_free();world=null;packed=null;await process_frame;await process_frame;quit(error)
