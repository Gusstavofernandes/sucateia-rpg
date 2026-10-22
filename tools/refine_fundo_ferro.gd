extends SceneTree
var world: Node2D
var structures: Node2D
var detail: Node2D
func art(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://assets/"+file);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func machine(label: String, point: Vector2, file: String, size: Vector2) -> void:
	var node := Node2D.new();node.name=label;node.position=point;structures.add_child(node)
	art("terrain/foundation.png",point,Vector2(size.x*.95,95),detail).modulate=Color(.52,.60,.53,.82)
	art("fx/light.svg",point+Vector2(8,6),Vector2(size.x,73),detail).modulate=Color(0,0,0,.65)
	art(file,Vector2(0,-size.y*.4),size,node)
	var body := StaticBody2D.new();body.position=Vector2(0,-32);var collision := CollisionShape2D.new();var shape := RectangleShape2D.new();shape.size=Vector2(size.x*.59,70);collision.shape=shape;body.add_child(collision);node.add_child(body);node.set_meta("blocked_base",point-Vector2(0,32))
func _initialize() -> void:call_deferred("run")
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	world=load("res://maps/fundo_ferro/fundo_ferro.tscn").instantiate();world.set_script(null);root.add_child(world)
	if world.has_node("BedrockMass"):
		world.queue_free();await process_frame;print("FUNDO finishing already present; current scene preserved");quit(0);return
	structures=world.get_node("Structures");detail=world.get_node("GroundIntegration");var builder=self
	for sprite in world.get_node("Structures/Walls").get_children():
		if not sprite is Sprite2D:continue
		sprite.scale=Vector2(87,48)/Vector2(sprite.texture.get_size())
		var index := posmod(int(sprite.position.x+sprite.position.y),3)
		sprite.modulate=[Color(.80,.86,.77),Color(.73,.82,.74),Color(.86,.82,.71)][index]
	var bedrock := Polygon2D.new();bedrock.name="BedrockMass";bedrock.z_index=-50;bedrock.polygon=PackedVector2Array([Vector2(-5000,-5000),Vector2(7000,-5000),Vector2(7000,7000),Vector2(-5000,7000)])
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/fundo_bedrock.gdshader");material.set_shader_parameter("rock",load("res://assets/region/salvage_ground.png"));bedrock.material=material;world.add_child(bedrock)
	builder.machine("CisternaDeRecalque",Vector2(1420,1480),"reconstruction/alto_cistern.png",Vector2(170,181))
	builder.machine("RestosDaFundacao",Vector2(1880,990),"region/ruined_engine.png",Vector2(194,199))
	for point in [Vector2(1155,1510),Vector2(1370,1680),Vector2(1630,2080),Vector2(2200,2310),Vector2(2460,2230),Vector2(2750,1830),Vector2(3020,1950),Vector2(2860,1270),Vector2(2580,1000),Vector2(3140,495)]:
		builder.art("terrain/metal_repair.png",point,Vector2(114,75),builder.detail,.08).modulate=Color(.68,.77,.64,.7)
		builder.art("terrain/market_dirt.png",point+Vector2(10,8),Vector2(136,96),builder.detail,-.13).modulate=Color(.33,.42,.30,.40)
		builder.art("generated/props/pipe.png",point+Vector2(-31,21),Vector2(88,26),builder.detail,.13).modulate=Color(.68,.76,.67,.92)
	world.set_script(load("res://scripts/world/fundo_ferro.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/fundo_ferro/fundo_ferro.tscn")
	print("FUNDO localized finishing saved=",error);quit(error)
