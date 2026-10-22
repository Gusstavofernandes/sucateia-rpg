extends SceneTree
var world: Node2D
var ground: Node2D
func _initialize() -> void:call_deferred("run")
func own(node: Node) -> void:
	for child in node.get_children():
		child.scene_file_path=""
		child.owner=world
		own(child)
func art(file: String, at: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new()
	sprite.texture=load("res://assets/"+file)
	sprite.position=at;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle
	parent.add_child(sprite)
	return sprite
func contact(at: Vector2, size: Vector2) -> void:
	art("fx/light.svg",at+Vector2(4,8),size,ground).modulate=Color(0,0,0,.60)
	art("terrain/market_dirt.png",at+Vector2(8,15),size*Vector2(1.3,1.5),ground,.12).modulate=Color(.72,.69,.53,.56)
func cargo(at: Vector2, crate: bool, angle: float) -> void:
	contact(at,Vector2(46,22))
	art("infrastructure/scrap.png",at-Vector2(0,10),Vector2(58,37),world.get_node("Structures"),angle).modulate=Color(.88,.84,.70)
	var body := StaticBody2D.new();body.position=at-Vector2(0,7)
	var collision := CollisionShape2D.new();var shape := RectangleShape2D.new();shape.size=Vector2(30,20);collision.shape=shape
	body.add_child(collision);world.get_node("Structures").add_child(body)
func run() -> void:
	if FileAccess.get_file_as_string("res://maps/sucateia/sucateia.tscn").contains('[node name="LowerCoastReworked"'):
		push_error("Current coastal shape is preserved. Use tools/rework_lower_coast.gd for scoped coast changes; do not regenerate from the historical rectangle.");quit(1);return
	var expansion_script: Script=load("res://scripts/world/market_expansion_builder.gd")
	if not expansion_script or not expansion_script.can_instantiate():
		push_error("Market expansion script failed validation");quit(1);return
	world=load("res://tools/checkpoints/sucateia_before_world_extension.tscn").instantiate()
	world.set_script(null)
	root.add_child(world)
	# Keep direction signs and their finished architectural art, remove scene-switch behaviour.
	for portal in world.get_node("RegionPortals").get_children():
		portal.set_script(null)
		for child in portal.get_children():
			if child.name=="Prompt":child.visible=false
			if child is CollisionShape2D:
				portal.remove_child(child);child.free()
		portal.collision_mask=0
	ground=Node2D.new();ground.name="MarketIntegration";ground.z_index=-14;world.add_child(ground)
	var market := Node2D.new();market.name="MercadoReconstruido";world.get_node("Structures").add_child(market)
	market.position=Vector2(1032,1310)
	contact(market.position,Vector2(138,48))
	art("terrain/metal_repair.png",market.position+Vector2(12,6),Vector2(95,63),ground,-.1).modulate=Color(.73,.70,.57,.70)
	art("reconstruction/market_salvage_cart.png",Vector2(0,-54),Vector2(156,164),market)
	var body := StaticBody2D.new();body.name="CartCollision";body.position=Vector2(0,-20)
	var collision := CollisionShape2D.new();var shape := RectangleShape2D.new();shape.size=Vector2(78,49);collision.shape=shape
	body.add_child(collision);market.add_child(body)
	for entry in [[Vector2(837,1030),true,-.09],[Vector2(863,1045),false,.07],[Vector2(893,1188),true,.08],[Vector2(904,1214),false,-.04],[Vector2(1350,1133),true,-.08],[Vector2(1371,1154),true,.06]]:
		cargo(entry[0],entry[1],entry[2])
	for at in [Vector2(902,1050),Vector2(980,1220),Vector2(1290,1172),Vector2(1036,1343)]:
		art("terrain/market_dirt.png",at,Vector2(112,54),ground,.09).modulate=Color(.90,.83,.63,.26)
	for at in [Vector2(864,1070),Vector2(1368,1184)]:
		art("infrastructure/lantern.png",at-Vector2(0,25),Vector2(25,43),world.get_node("Structures"))
		var light := PointLight2D.new();light.position=at;light.texture=load("res://assets/fx/light.svg");light.color=Color("d2a04d");light.energy=.32;light.texture_scale=.32
		world.get_node("Lighting").add_child(light)
	for label in world.find_children("*","Label",true,false):label.text=label.text.replace("E passagem    ","")
	expansion_script.new().install(self)
	var alto_script: Script=load("res://scripts/world/alto_lixo_builder.gd")
	if not alto_script or not alto_script.can_instantiate():push_error("Alto-Lixo builder failed validation");quit(1);return
	alto_script.new().install(self)
	world.set_script(load("res://scripts/world/sucateia.gd"))
	own(world)
	var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("REBUILT Mercado directly in original Sucateia; save=",error)
	quit(error)
