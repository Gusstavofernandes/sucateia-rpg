extends SceneTree
var world: Node2D
func _initialize() -> void:call_deferred("run")
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	if FileAccess.get_file_as_string("res://maps/sucateia/sucateia.tscn").contains('[node name="ResidentialFinish"'):
		push_error("Coastal replay snapshot predates Alto-Lixo finishing. Preserve current scene and create a new scoped baseline before another coastal edit.");quit(1);return
	var script: Script=load("res://scripts/world/lower_coast_builder.gd")
	if not script or not script.can_instantiate():push_error("Lower coast builder failed validation");quit(1);return
	world=load("res://tools/checkpoints/sucateia_before_lower_coast.tscn").instantiate();world.set_script(null);root.add_child(world)
	script.new().install(world)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world)
	var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("LOWER COAST saved=",error);quit(error)
