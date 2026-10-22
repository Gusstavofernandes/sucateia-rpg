extends SceneTree
var world: Node2D
func _initialize() -> void:call_deferred("run")
func art(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://assets/"+file);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	var current: Node=load("res://maps/sucateia/sucateia.tscn").instantiate()
	var later_stage := current.has_node("ForjasRasasDistrict");current.free()
	if later_stage:push_error("Historical Alto checkpoint predates Forjas; establish a fresh baseline before further refinement");quit(1);return
	var script: Script=load("res://scripts/world/alto_residential_finish.gd")
	if not script or not script.can_instantiate():push_error("Alto finishing script failed validation");quit(1);return
	world=load("res://tools/checkpoints/sucateia_before_alto_refinement.tscn").instantiate();world.set_script(null);root.add_child(world)
	script.new().install(self)
	if not world.has_node("AltoLixoDistrict/ResidentialFinish") or world.get_node("AltoLixoDistrict/ResidentialFinish").get_meta("additional_houses",0)<5:push_error("Residential finishing incomplete");quit(1);return
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world)
	var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("ALTO refinement saved=",error);quit(error)
