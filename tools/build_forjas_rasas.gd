extends SceneTree
var world: Node2D
func _initialize() -> void:call_deferred("run")
func art(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://assets/"+file);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	var current: Node=load("res://maps/sucateia/sucateia.tscn").instantiate()
	var district: Node=current.get_node_or_null("ForjasRasasDistrict")
	var validated: bool=district!=null and str(district.get_meta("status","")).begins_with("exterior first stage validated")
	current.free()
	if validated:push_error("Forjas stage sealed; refine the current scene or establish a fresh checkpoint instead of replaying construction");quit(1);return
	var script: Script=load("res://scripts/world/forjas_rasas_builder.gd")
	if not script or not script.can_instantiate():push_error("Forjas builder failed validation");quit(1);return
	world=load("res://tools/checkpoints/sucateia_before_forjas.tscn").instantiate();world.set_script(null);root.add_child(world)
	if not world.has_node("AltoLixoDistrict/ResidentialFinish") or not world.has_node("LowerCoastReworked"):push_error("Forjas requires the currently approved city checkpoint");quit(1);return
	script.new().install(self)
	if not world.has_node("ForjasRasasDistrict"):push_error("Forjas missing after build");quit(1);return
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world)
	var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS scene saved=",error);quit(error)
