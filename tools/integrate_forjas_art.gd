extends SceneTree
var world: Node2D
var detail: Node2D
var modules: Node2D
func _initialize() -> void:call_deferred("run")
func art(file: String,point: Vector2,size: Vector2,parent: Node) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://"+file);sprite.position=point
	var dimensions := Vector2(sprite.texture.get_size());sprite.scale=Vector2.ONE*minf(size.x/dimensions.x,size.y/dimensions.y);parent.add_child(sprite);return sprite
func module(label: String,file: String,point: Vector2,size: Vector2,base: Vector2,offset: float) -> void:
	if modules.has_node(label):
		var existing: Node=modules.get_node(label)
		for sprite in existing.get_children():
			if sprite is Sprite2D and sprite.texture and sprite.texture.resource_path=="res://"+file:return
		modules.remove_child(existing);existing.free()
		for sprite in detail.get_children():
			if sprite is Sprite2D and sprite.position in [point-Vector2(0,12),point+Vector2(5,5),point+Vector2(0,9)]:
				detail.remove_child(sprite);sprite.free()
	var node := Node2D.new();node.name=label;node.position=point;node.set_meta("footprint_center",point+Vector2(0,-28));modules.add_child(node)
	art("assets/terrain/foundation.png",point-Vector2(0,12),Vector2(base.x*1.22,base.y*1.65),detail).modulate=Color(.47,.46,.39,.90)
	art("assets/fx/light.svg",point+Vector2(5,5),Vector2(size.x*.8,65),detail).modulate=Color(0,0,0,.62)
	art("assets/terrain/market_dirt.png",point+Vector2(0,9),Vector2(size.x*.90,105),detail).modulate=Color(.30,.23,.15,.42)
	art(file,Vector2(0,offset),size,node)
	var body := StaticBody2D.new();body.position=Vector2(0,-28);var collision := CollisionShape2D.new();var shape := RectangleShape2D.new();shape.size=base;collision.shape=shape;body.add_child(collision);node.add_child(body)
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	detail=world.get_node("ForjasRasasDistrict/IndustrialGroundFinish")
	modules=world.get_node_or_null("Structures/ForjasFunctionalModules")
	if not modules:modules=Node2D.new();modules.name="ForjasFunctionalModules";modules.y_sort_enabled=true;world.get_node("Structures").add_child(modules)
	var requests := OS.get_cmdline_user_args()
	var files := {"landmark":"great_furnace_chimney.png","smithy":"open_smithy.png","stock":"ore_storage_cart.png","crane":"compact_loading_crane.png","service":"service_pipe_boiler.png"}
	for request in requests:
		if request in files and not ResourceLoader.exists("res://assets/reconstruction/forjas_parallel/"+files[request]):
			push_error("Parallel asset is not imported; current scene not saved: "+request);world.queue_free();await process_frame;quit(1);return
	if "landmark" in requests:
		module("FornalhaDaEntrada","assets/reconstruction/forjas_parallel/great_furnace_chimney.png",Vector2(2050,-275),Vector2(340,345),Vector2(200,58),-127)
		var district: Node2D=world.get_node("ForjasRasasDistrict");district.set_meta("market_viewpoint",Vector2(1600,-275));district.set_meta("entry_landmark",NodePath("../Structures/ForjasFunctionalModules/FornalhaDaEntrada"))
	if "smithy" in requests:module("FerreiroDaRua","assets/reconstruction/forjas_parallel/open_smithy.png",Vector2(1850,-8),Vector2(189,157),Vector2(99,44),-58)
	if "stock" in requests:module("MinerioDaCarga","assets/reconstruction/forjas_parallel/ore_storage_cart.png",Vector2(2490,30),Vector2(227,153),Vector2(185,62),-54)
	if "crane" in requests:module("GuindasteDaFundicao","assets/reconstruction/forjas_parallel/compact_loading_crane.png",Vector2(2945,-925),Vector2(216,226),Vector2(75,49),-91)
	if "service" in requests:
		module("VasoDeServico","assets/reconstruction/forjas_parallel/service_pipe_boiler.png",Vector2(2840,-1390),Vector2(189,138),Vector2(112,47),-51)
		if not detail.has_node("LigacaoVasoCaldeiras"):
			var connection := Node2D.new();connection.name="LigacaoVasoCaldeiras";detail.add_child(connection)
			art("assets/generated/props/pipe.png",Vector2(2875,-1382),Vector2(86,24),connection)
			connection.set_meta("connected_points",PackedVector2Array([Vector2(2832,-1382),Vector2(2918,-1382)]))
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS new modules integrated=",modules.get_child_count()," saved=",error)
	world.queue_free();detail=null;modules=null;world=null;packed=null
	await process_frame;await process_frame;quit(error)
