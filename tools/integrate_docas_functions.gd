extends "res://tools/build_docas_navigation.gd"
var architecture: Node2D
var contacts: Node2D
var rigging: Node2D
func object(label: String,file: String,center: Vector2,ratio: float,feet: Array) -> Sprite2D:
	var node := group(label,architecture);var texture: Texture2D=load("res://assets/"+file);var canvas := Vector2(texture.get_size());var origin := center+Vector2(0,50);node.position=origin
	var sprite := place(file,center-origin,ratio,node,"Artwork");node.set_meta("asset_scale",ratio)
	for native in feet:
		var bounds: Rect2=native;var foot := center+(bounds.get_center()-canvas*.5)*ratio
		var body := StaticBody2D.new();body.position=foot-origin;body.collision_mask=2;node.add_child(body);var shape := CollisionShape2D.new();var rectangle := RectangleShape2D.new();rectangle.size=bounds.size*ratio;shape.shape=rectangle;body.add_child(shape)
		var shadow := place("fx/light.svg",foot,1.,contacts,label+"Contact");shadow.scale=Vector2(bounds.size.x*ratio+14,23)/Vector2(shadow.texture.get_size());shadow.modulate=Color(0,0,0,.36)
	node.set_meta("contact_rectangles_native",feet);return sprite
func line(label: String,points: PackedVector2Array,width: float=2.5) -> void:
	var node := Line2D.new();node.name=label;node.points=points;node.width=width;node.default_color=Color("564935");node.antialiased=true;rigging.add_child(node);node.set_meta("real_endpoints",PackedVector2Array([points[0],points[-1]]))
	var strand := Line2D.new();strand.points=points;strand.width=.75;strand.default_color=Color("ad9470");strand.antialiased=true;node.add_child(strand)
func clean_prefix(parent: Node,prefix: String) -> void:
	for child in parent.get_children():
		if String(child.name).begins_with(prefix):child.free()
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);district=world.get_node("DocasDistrict");floors.assign(district.get_meta("walk_polygons"));painted=district.get_node("WorkingDecks");receivers=district.get_node("WetSupports")
	if district.has_meta("functions_integrated"):print("DOCAS functions retained");world.free();world=null;quit(0);return
	architecture=group("DocasPortFunctions",world.get_node("Structures"));architecture.y_sort_enabled=true;contacts=group("PhysicalContacts",district,-10);rigging=group("WorkingRopes",district,-9)
	# Two proper piled heads create enough space for crane, staged cargo and capstan.
	clean_prefix(painted,"EmbarqueInterior");clean_prefix(receivers,"EmbarqueEstaca");floors[20]=rect(Vector2(2566,1864),Vector2(2772,1950));floors.append(rect(Vector2(2796.56,1864),Vector2(3002.56,1950)))
	for point in [Vector2(2670,1927.593),Vector2(2900.56,1927.593)]:place("reconstruction/docas_parallel/complement_v1/pier_head_deep.png",point,.18518518518518517,painted,"Cabeceira%d"%int(point.x))
	district.get_node("SafeLandings/Embarque").position=Vector2(2735,1910);marker("CargaPreparada",Vector2(2974,1933),district.get_node("SafeLandings"))
	# Move only the new access pier east: approach through the head's open side,
	# never through its painted north guardrail or loaded boat.
	for i in range(floors[6].size()):floors[6][i].x+=250
	district.get_node("Routes/PierDeCarga").set_meta("points",PackedVector2Array([Vector2(3170,1640),Vector2(3170,1910)]))
	for parent in [painted,receivers]:
		for child in parent.get_children():
			if String(child.name).begins_with("PierDeCarga"):child.position.x+=250
	clean_prefix(painted,"CargaPrincipal");clean_prefix(receivers,"CargaPrincipal");clean_prefix(painted,"CaisDeCarga");clean_prefix(receivers,"CaisDeCarga")
	district.get_node("Routes/CargaPrincipal").free();district.get_node("Routes/CaisDeCarga").free()
	floors[2]=rect(Vector2(2350,1604),Vector2(3170,1676));floors[7]=rect(Vector2(2670,1874),Vector2(3170,1946))
	var original_count := floors.size();strip("CargaPrincipal",Vector2(2350,1640),Vector2(3170,1640),72);strip("CaisDeCarga",Vector2(2670,1910),Vector2(3170,1910),72);floors.resize(original_count)
	platform("JuntaDoPier",Rect2(3125,1604,90,72));platform("JuntaInferiorDoPier",Rect2(3125,1874,90,72))
	object("AbrigoDeTriagem","reconstruction/docas_parallel/cargo_sorting_shelter.png",Vector2(2490,1440),.20785219399538107,[Rect2(110,825,1210,155)])
	object("BercoDeReparo","reconstruction/docas_parallel/naval_repair_cradle.png",Vector2(3030,1510),.134886572654813,[Rect2(360,600,1100,234)])
	object("Cabrestante","reconstruction/docas_parallel/mooring_capstan.png",Vector2(2640,1914),.10550113036925395,[Rect2(133,710,347,80),Rect2(510,735,500,97),Rect2(1080,704,350,86)])
	object("CargaComSling","reconstruction/docas_parallel/complement_v1/port_cargo_sling_cluster.png",Vector2(2940,1876),.09322033898305085,[Rect2(181,529,1177,446)])
	var barge := object("BarcacaAncorada","reconstruction/docas_parallel/cargo_barge.png",Vector2(2820,1780),.20535158680771623,[])
	var bow := barge.to_global(Vector2(232,420)-Vector2(barge.texture.get_size())*.5);var aft := barge.to_global(Vector2(1372,650)-Vector2(barge.texture.get_size())*.5)
	line("AmarraProa",PackedVector2Array([bow,Vector2(2580,1844),Vector2(2590.52,1923.50)]))
	line("AmarraPopa",PackedVector2Array([aft,Vector2(3025,1850),Vector2(3030.56,1934.445)]))
	var ring := Vector2(2939.72,1835.542);var crane_texture: Texture2D=load("res://assets/infrastructure/crane.png");var crane_canvas := Vector2(crane_texture.get_size());var crane_center := ring-(Vector2(272,296)-crane_canvas*.5)*.55
	var crane := object("GuindasteDeTransbordo","infrastructure/crane.png",crane_center,.55,[Rect2(20,352,160,47)])
	line("GanchoNoAnel",PackedVector2Array([crane.to_global(Vector2(272,296)-crane_canvas*.5),ring]),2.)
	for point in [Vector2(2675,1940),Vector2(2885,1941),Vector2(2500,1585),Vector2(3030,1650),Vector2(3090,805)]:
		var decal := place("reconstruction/docas_parallel/complement_v1/wet_wood_saltwear_decal.png",point,.10864197530864197,contacts,"Umidade%d"%int(point.x));decal.modulate.a=.25
	for point in [Vector2(2310,1360),Vector2(2550,1600),Vector2(2995,1610),Vector2(3170,1820),Vector2(2690,1925)]:place("infrastructure/lantern.png",point,.45,architecture,"Lanterna%d"%int(point.x))
	district.get_node("DeckBoundaries").free();district.set_meta("walk_polygons",floors);district.set_meta("boundary_segments",make_guards());district.set_meta("functions_integrated",true);district.set_meta("stage","seven selected PNGs integrated; contact/geography/capture refinement pending")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if packed.get_state().get_node_count()!=count_nodes(world):push_error("Dock art nodes omitted during packing");error=FAILED
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("DOCAS art saved=",error," four original functions + piled heads/cargo/saltwear; professional finish still under visual review")
	world.free();world=null;district=null;painted=null;receivers=null;architecture=null;contacts=null;rigging=null;barge=null;crane=null;packed=null;quit(error)
