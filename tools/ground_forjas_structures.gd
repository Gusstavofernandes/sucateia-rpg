extends "res://tools/correct_forjas_direction.gd"
func contact(node: Node2D, parent: Node) -> void:
	var sprite: Sprite2D
	for child in node.get_children():
		if child is Sprite2D:sprite=child;break
	if not sprite:return
	var pixels: Image=sprite.texture.get_image();pixels.resize(192,192,Image.INTERPOLATE_LANCZOS)
	var left := 192;var right := 0;var bottom := 0
	for y in range(192):
		for x in range(192):
			if pixels.get_pixel(x,y).a>.35:left=mini(left,x);right=maxi(right,x);bottom=maxi(bottom,y)
	var dimensions := Vector2(sprite.texture.get_size())
	var foot: Vector2=sprite.to_global(Vector2((left+right)*.5,bottom)*dimensions/192.-dimensions*.5)
	var width := (right-left)*dimensions.x/192.*sprite.scale.x
	var group := Node2D.new();group.name=node.name;group.set_meta("actual_sprite_foot",foot);parent.add_child(group)
	# Two/three small bearing surfaces follow the visible base, instead of a broad halo.
	for side in [-1,0,1]:
		var at := foot+Vector2(side*width*.31,2)
		art("res://assets/terrain/metal_repair.png",at-Vector2(0,4),Vector2(clampf(width*.25,26,84),24),group,.025*side).modulate=Color(.60,.53,.40,.78)
		art("res://assets/fx/light.svg",at+Vector2(3,5),Vector2(clampf(width*.29,28,94),19),group).modulate=Color(0,0,0,.54)
	art("res://assets/terrain/market_dirt.png",foot+Vector2(8,15),Vector2(width*.79,36),group,.08).modulate=Color(.25,.20,.13,.38)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("ForjasRasasDistrict")
	if district.has_node("PhysicalGroundContact"):world.queue_free();await process_frame;print("FORJAS physical grounding preserved");quit(0);return
	if not ResourceLoader.exists(ART+"pipe_saddle_support_single_ns.png"):push_error("Final saddle support not imported");quit(1);return
	detail=Node2D.new();detail.name="PhysicalGroundContact";detail.z_index=-13;district.add_child(detail)
	for path in ["ForjasIndustrialArchitecture","ForjasFunctionalModules","ForjasProductionYards"]:
		for node in world.get_node("Structures/"+path).get_children():contact(node,detail)
	# NS collars sit beneath the existing vertical conduits; horizontal connectors have feet built in.
	for point in [Vector2(2910,-1280),Vector2(2910,-1175),Vector2(2600,-800),Vector2(2600,-650),Vector2(3020,-240),Vector2(3020,-100),Vector2(2860,-150),Vector2(3380,-920),Vector2(3480,-385),Vector2(3600,-785)]:
		extracted("pipe_saddle_support_single_ns.png",Rect2(292,400,614,611),point+Vector2(3,10),Vector2(42,42),detail)
	# Bearing blocks attach bridge corners to real banks without occupying the walking deck.
	for x in [2620,3280]:
		var bridge: Node2D=district.get_node("Bridges/Travessia%d"%x)
		var center: Vector2=(bridge.get_meta("approach")+bridge.get_meta("departure"))*.5
		for side in [-1,1]:
			for end in [-1,1]:
				var at := center+Vector2(side*48,end*69)
				art("res://assets/infrastructure/retaining_edge.png",at,Vector2(45,37),detail,PI/2).modulate=Color(.70,.63,.49)
				art("res://assets/terrain/metal_repair.png",at+Vector2(0,end*13),Vector2(35,29),detail).modulate=Color(.65,.59,.44,.8)
	detail.set_meta("scope","localized sprite-foot plates/contact shadows, conduit saddles and bridge bank anchors; original art and collisions retained")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS physical grounding saved=",error," real sprite feet and supported pipes/bridges; approved geometry untouched")
	world.queue_free();world=null;district=null;detail=null;packed=null;await process_frame;await process_frame;quit(error)
