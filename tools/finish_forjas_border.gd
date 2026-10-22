extends SceneTree
var world: Node2D
func _initialize() -> void:call_deferred("run")
func art(path: String,point: Vector2,size: Vector2,parent: Node,angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load(path);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	var district: Node2D=world.get_node("ForjasRasasDistrict")
	if district.has_node("RegionalEdgeContext"):world.queue_free();await process_frame;print("FORJAS edge context preserved");quit(0);return
	var context := Node2D.new();context.name="RegionalEdgeContext";context.set_meta("scope","non-playable water and distant scrap embankment; no floor cells, destinations or access expansion");district.add_child(context)
	var sea := Polygon2D.new();sea.name="CostaIndustrialLeste";sea.z_index=-35
	sea.polygon=PackedVector2Array([Vector2(3670,190),Vector2(3750,-190),Vector2(3650,-600),Vector2(3730,-1050),Vector2(4150,-1450),Vector2(4900,-1400),Vector2(4900,4000),Vector2(3300,4000),Vector2(3300,335),Vector2(3370,280)])
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/lower_sea.gdshader");material.set_shader_parameter("grime",load("res://assets/region/salvage_ground.png"))
	var edges: Array[Vector4]=[Vector4(3670,190,3750,-190),Vector4(3750,-190,3650,-600),Vector4(3650,-600,3730,-1050)]
	material.set_shader_parameter("edge_count",edges.size());while edges.size()<64:edges.append(Vector4.ZERO)
	material.set_shader_parameter("coast_edges",edges);sea.material=material;context.add_child(sea)
	# The district's upper retaining works now sit against a distant scrap embankment,
	# rather than a void. This is visual context, not another playable sector.
	var bank := Polygon2D.new();bank.name="TaludeDeSucataAoFundo";bank.z_index=-34
	bank.polygon=PackedVector2Array([Vector2(1770,-1120),Vector2(2110,-1490),Vector2(2630,-1690),Vector2(3150,-1640),Vector2(3490,-1440),Vector2(3730,-1050),Vector2(4150,-1450),Vector2(4280,-1970),Vector2(4200,-2310),Vector2(1770,-2310)])
	var ground := ShaderMaterial.new();ground.shader=load("res://assets/reconstruction/forjas_outer_context.gdshader");ground.set_shader_parameter("ground_texture",load("res://assets/region/salvage_ground.png"));bank.material=ground;context.add_child(bank)
	var edge := Node2D.new();edge.name="ApoiosDaMargem";edge.z_index=-12;context.add_child(edge)
	for data in [[Vector2(3690,-320),.24],[Vector2(3690,-730),-.16],[Vector2(3640,-1120),.3],[Vector2(3430,-1490),-.24],[Vector2(3270,300),.08]]:
		art("res://assets/infrastructure/retaining_edge.png",data[0],Vector2(110,76),edge,data[1]).modulate=Color(.68,.62,.49)
		art("res://assets/infrastructure/scrap.png",data[0]+Vector2(22,22),Vector2(116,70),edge,data[1]).modulate=Color(.59,.53,.41)
	for point in [Vector2(3180,-1695),Vector2(3440,-1510),Vector2(3650,-1180)]:
		art("res://assets/infrastructure/scrap.png",point,Vector2(146,94),edge,.13).modulate=Color(.51,.46,.37)
	# Short attached decks provide visible maintenance function at the wet edge.
	for point in [Vector2(3690,-355),Vector2(3660,-1150)]:
		art("res://assets/infrastructure/walkway.png",point,Vector2(78,74),edge).modulate=Color(.72,.67,.51)
		art("res://assets/generated/props/pipe.png",point-Vector2(28,0),Vector2(85,26),edge).modulate=Color(.81,.74,.56)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS coastal/background context saved=",error," no playable territory expansion")
	world.queue_free();world=null;packed=null;await process_frame;await process_frame;quit(error)
