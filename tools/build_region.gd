extends SceneTree
var world: Node2D
var floor_details: Node2D
var structures: Node2D
var upper: Node2D
var config: Dictionary
var catalog: Dictionary
var id := ""
func _initialize() -> void:
	call_deferred("run")
func add(n: Node, parent: Node) -> void:
	parent.add_child(n)
	n.owner = world
func group_node(label: String, z: int, sorted: bool = false) -> Node2D:
	var n := Node2D.new()
	n.name = label
	n.z_index = z
	n.y_sort_enabled = sorted
	add(n,world)
	return n
func art(file: String, at: Vector2, size: Vector2, parent: Node = null, angle: float = 0) -> Sprite2D:
	var n := Sprite2D.new()
	n.texture = load("res://assets/"+file)
	n.position = at
	n.scale = size/Vector2(n.texture.get_size())
	n.rotation = angle
	add(n,floor_details if parent == null else parent)
	return n
func shadow(at: Vector2, size: Vector2, opacity: float = .55) -> void:
	var n := art("fx/light.svg",at,size)
	n.modulate = Color(0,0,0,opacity)
func solid(at: Vector2, size: Vector2, parent: Node, angle: float = 0) -> void:
	var n := StaticBody2D.new()
	n.position = at
	n.rotation = angle
	add(n,parent)
	var collision := CollisionShape2D.new()
	var shape := RectangleShape2D.new()
	shape.size = size
	collision.shape = shape
	add(collision,n)
func light(at: Vector2, color: Color, size: float) -> void:
	var n := PointLight2D.new()
	n.position = at
	n.texture = load("res://assets/fx/light.svg")
	n.color = color
	n.texture_scale = size
	n.energy = .8
	add(n,world.get_node("Lighting"))
func cable(points: PackedVector2Array, parent: Node = null) -> void:
	for entry in [[Color("17251f"),4.0],[Color("86714d"),1.0]]:
		var n := Line2D.new()
		n.points = points
		n.width = entry[1]
		n.default_color = entry[0]
		n.antialiased = true
		n.joint_mode = Line2D.LINE_JOINT_ROUND
		add(n,upper if parent == null else parent)
func pipe_route(points: PackedVector2Array) -> void:
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i]
		var count := maxi(1,ceili(delta.length()/104.0))
		for j in range(count):
			var at := points[i].lerp(points[i+1],(j+.5)/count)
			art("generated/props/pipe.png",at,Vector2(delta.length()/count+6,30),null,delta.angle())
			if j%2 == 0: art("terrain/metal_repair.png",at+Vector2(0,9),Vector2(41,38),null,delta.angle())
func building(entry: Array) -> void:
	var name: String = entry[0]
	var base := Vector2(entry[1],entry[2])
	var size := Vector2(entry[3],entry[4])
	var file := "region/"+name+".png"
	if name in ["gothic_block","port_warehouse","twin_towers","arcane_station"]: file = "vhal/"+name+".png"
	if name in ["house","house_stack","workshop","reactor"]: file = "generated/structures/"+name+".png"
	var n := Node2D.new()
	n.name = name
	n.position = base
	add(n,structures)
	var sprite := art(file,Vector2(0,-size.y*.5+10),size,n)
	sprite.name = "Architecture"
	var width := size.x*.65
	if name == "cable_tower": width = size.x*.32
	var depth := minf(118,size.y*.24)
	solid(Vector2(0,-depth*.5),Vector2(width,depth),n)
	shadow(base+Vector2(8,5),Vector2(width*1.45,78),.63)
	if name == "cargo_barge":
		for offset in [-1,1]:
			art("infrastructure/walkway.png",base+Vector2(offset*width*.53,-42),Vector2(102,149),null,.06*offset)
			art("infrastructure/scrap.png",base+Vector2(offset*width*.36,15),Vector2(122,67),null,.1*offset)
	elif not config.style.begins_with("vhal_"):
		art("terrain/foundation.png",base+Vector2(0,-15),Vector2(width+20,74)).modulate = Color(.72,.75,.68,.86)
	art("terrain/market_dirt.png",base+Vector2(-width*.33,20),Vector2(116,60)).modulate.a = .48
func portal(destination: String, at: Vector2) -> void:
	if config.get("style","").begins_with("vhal_"):
		load("res://scripts/world/vhal_builder.gd").new().portal(self,destination,at)
		return
	var n := Area2D.new()
	n.name = "To_"+destination
	n.position = at
	n.collision_layer = 0
	n.collision_mask = 2
	n.set_script(load("res://scripts/world/region_portal.gd"))
	n.set("destination",destination)
	n.set_meta("destination",destination)
	if config.get("continuity",{}).get(destination,{}).get("opening",false):
		var direction: Array = config.continuity[destination].direction
		n.set_meta("arrival_offset",-Vector2(direction[0],direction[1])*58)
	add(n,world.get_node("RegionPortals"))
	var shape := CollisionShape2D.new()
	var radius := CircleShape2D.new()
	radius.radius = 78
	shape.shape = radius
	add(shape,n)
	art("infrastructure/retaining_edge.png",Vector2(0,-52),Vector2(181,81),n)
	art("infrastructure/service_arch.png",Vector2(0,-22),Vector2(113,91),n)
	art("infrastructure/stairs.png",Vector2(0,23),Vector2(72,58),n)
	var label := Label.new()
	label.name = "Prompt"
	label.text = "E — "+str(catalog[destination].name)
	label.position = Vector2(-90,16)
	label.visible = false
	label.add_theme_font_size_override("font_size",14)
	label.add_theme_color_override("font_color",Color("e1c38b"))
	add(label,n)
	art("terrain/metal_repair.png",Vector2(76,-63),Vector2(114,61),n,.04)
	var sign := Label.new()
	sign.name = "Sign"
	sign.text = str(catalog[destination].name).split(" — ")[0]
	sign.position = Vector2(28,-82)
	sign.size = Vector2(106,44)
	sign.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	sign.add_theme_font_size_override("font_size",10)
	sign.add_theme_color_override("font_color",Color("d2ba81"))
	add(sign,n)
	if destination == "galeria": art("terrain/oil_hatch.png",Vector2(0,3),Vector2(129,111),n)
func perimeter(outline: PackedVector2Array) -> void:
	for i in range(outline.size()):
		var a := outline[i]
		var b := outline[(i+1)%outline.size()]
		var delta := b-a
		load("res://scripts/world/regional_continuity_builder.gd").new().wall(self,a,b)
		var count := maxi(1,ceili(delta.length()/171.0))
		for j in range(count):
			var at := a.lerp(b,(j+.5)/count)
			if load("res://scripts/world/regional_continuity_builder.gd").new().near_opening(self,at): continue
			if config.style.begins_with("vhal_") and config.style != "vhal_edge":
				art("vhal/stone_quay.png",at,Vector2(delta.length()/count+12,93),null,delta.angle())
				continue
			var coastal: bool = config.style in ["harbor","coastal_path","wreck_bank"] and at.y > 950 and abs(delta.x) > abs(delta.y)
			var file := "infrastructure/coastal_wall.png" if coastal else "infrastructure/retaining_edge.png"
			var outdoor: bool = config.style in ["salvage","ruins","freight_path"]
			var height := 98.0 if coastal else (26.0 if outdoor else 51.0)
			shadow(at+Vector2(7,20),Vector2(delta.length()/count+32,77))
			art(file,at,Vector2(delta.length()/count+11,height),null,delta.angle())
			if outdoor and j%2 == i%2: art("infrastructure/scrap.png",at+Vector2(10,0),Vector2(151,72),null,delta.angle()*.15)
func terrain(outline: PackedVector2Array) -> void:
	if config.style == "gallery":
		load("res://scripts/world/region_extension_builder.gd").new().gallery_floor(self)
		return
	var background := Polygon2D.new()
	background.polygon = PackedVector2Array([Vector2(-500,-500),Vector2(2800,-500),Vector2(2800,2100),Vector2(-500,2100)])
	background.z_index = -40
	background.color = Color("17211f")
	if config.style in ["harbor","suspended","coastal_path","wreck_bank"]:
		var shader := ShaderMaterial.new()
		shader.shader = load("res://assets/infrastructure/sea.gdshader")
		shader.set_shader_parameter("grime",load("res://assets/infrastructure/channel.png"))
		background.material = shader
	if config.style in ["vhal_river","vhal_port"]:
		var water := ShaderMaterial.new()
		water.shader = load("res://assets/vhal/river.gdshader")
		background.material = water
	if config.style in ["salvage","ruins","freight_path"]:
		var material := ShaderMaterial.new()
		material.shader = load("res://assets/region/outskirts.gdshader")
		material.set_shader_parameter("soil",load("res://assets/region/salvage_ground.png"))
		background.material = material
	add(background,world)
	var layer := TileMapLayer.new()
	layer.name = "DistrictFloor"
	layer.z_index = -30
	layer.tile_set = load("res://assets/terrain/sucateia_terrain.tres")
	if config.has("floor_texture") or config.style in ["salvage","ruins","freight_path","wreck_bank"]:
		var tiles := TileSet.new()
		tiles.tile_size = Vector2i(48,48)
		var source := TileSetAtlasSource.new()
		source.texture = load("res://assets/"+config.get("floor_texture","region/salvage_ground.png"))
		source.texture_region_size = Vector2i(48,48)
		for y in range(16):
			for x in range(16): source.create_tile(Vector2i(x,y))
		tiles.add_source(source,0)
		layer.tile_set = tiles
	var material := ShaderMaterial.new()
	material.shader = load("res://assets/region/ground.gdshader")
	material.set_shader_parameter("district_tint",Color(config.tint))
	if config.style in ["freight_path","vhal_edge"]:
		material.shader = load("res://assets/region/transition.gdshader")
		material.set_shader_parameter("dirt",load("res://assets/region/salvage_ground.png"))
		material.set_shader_parameter("stone",load("res://assets/vhal/stone_ground.png" if config.style == "vhal_edge" else "res://assets/terrain/floor_atlas.png"))
	layer.material = material
	add(layer,world)
	for y in range(3,29):
		for x in range(2,41):
			var at := Vector2(x*48+24,y*48+24)
			if Geometry2D.is_point_in_polygon(at,outline): layer.set_cell(Vector2i(x,y),0,Vector2i((x+int(id.hash()%13))%16,(y+int(id.hash()%7))%16))
	perimeter(outline)
	# Deliberate worn junctions and micro-courts; sparse, no global debris noise.
	for at in [Vector2(980,1130),Vector2(1060,905),Vector2(900,600),Vector2(1310,1070),Vector2(460,1050)]:
		if config.style == "suspended" or not Geometry2D.is_point_in_polygon(at,outline): continue
		art("terrain/market_dirt.png",at,Vector2(155,102),null,.11).modulate.a = .36
func details() -> void:
	var style: String = config.style
	if style.begins_with("vhal_"):
		load("res://scripts/world/vhal_builder.gd").new().details(self)
		return
	if style in ["gallery","precision","coastal_path","wreck_bank","freight_path"]:
		load("res://scripts/world/region_extension_builder.gd").new().install(self)
		return
	if style == "residential":
		for at in [Vector2(510,710),Vector2(1455,745),Vector2(594,1090),Vector2(1230,1110)]:
			art("infrastructure/stairs.png",at+Vector2(30,25),Vector2(92,74),null,.04)
			art("infrastructure/walkway.png",at+Vector2(-36,4),Vector2(86,62))
			light(at+Vector2(0,-30),Color("d8a257"),.8)
		cable(PackedVector2Array([Vector2(450,465),Vector2(700,535),Vector2(1040,565),Vector2(1450,480)]))
		art("terrain/oil_hatch.png",Vector2(1650,1120),Vector2(146,124))
	elif style == "forge":
		pipe_route(PackedVector2Array([Vector2(635,771),Vector2(635,868),Vector2(951,868),Vector2(951,996)]))
		pipe_route(PackedVector2Array([Vector2(1000,985),Vector2(1185,985),Vector2(1185,752),Vector2(1480,752)]))
		for at in [Vector2(620,470),Vector2(1480,485)]: light(at,Color("ee873d"),2)
		light(Vector2(960,870),Color("57bdd0"),1.4)
		for at in [Vector2(1160,1020),Vector2(550,850),Vector2(1680,1080)]:
			art("terrain/oil_hatch.png",at,Vector2(132,105),null,.1)
			art("infrastructure/scrap.png",at+Vector2(62,54),Vector2(131,71))
		for at in [Vector2(480,807),Vector2(1500,803),Vector2(322,1138)]:
			for offset in [Vector2(-53,0),Vector2(61,7),Vector2(8,58)]:
				art("terrain/metal_repair.png",at+offset,Vector2(131,78),null,.065)
			art("infrastructure/crane.png",at+Vector2(105,-37),Vector2(77,112))
	elif style == "suspended":
		for y in range(300,1250,153): art("infrastructure/walkway.png",Vector2(985+(y%4)*5,y),Vector2(239,177),null,.014 if y%2 else -.012)
		for x in range(315,1730,173): art("infrastructure/walkway.png",Vector2(x,829+(x%3)*9),Vector2(200,184),null,PI/2)
		art("generated/props/bridge.png",Vector2(1000,840),Vector2(650,190))
		cable(PackedVector2Array([Vector2(470,265),Vector2(745,403),Vector2(1040,459),Vector2(1470,275)]))
		cable(PackedVector2Array([Vector2(470,310),Vector2(900,495),Vector2(1470,319)]))
		for at in [Vector2(470,375),Vector2(1470,380),Vector2(985,1170)]: light(at,Color("69a1b0"),1.2)
	elif style == "undercity":
		for x in [335,590,1580,1770]:
			art("infrastructure/retaining_edge.png",Vector2(x,540),Vector2(211,78))
			art("infrastructure/service_arch.png",Vector2(x,594),Vector2(141,133))
		pipe_route(PackedVector2Array([Vector2(650,1040),Vector2(400,1040),Vector2(400,657),Vector2(570,657)]))
		pipe_route(PackedVector2Array([Vector2(720,1050),Vector2(1180,1050),Vector2(1180,790)]))
		art("infrastructure/walkway.png",Vector2(660,1060),Vector2(255,181))
		for at in [Vector2(405,679),Vector2(1770,671),Vector2(1330,875)]:
			art("infrastructure/walkway.png",at,Vector2(119,91))
			art("infrastructure/stairs.png",at+Vector2(15,48),Vector2(63,57))
			light(at,Color("4a8c8a"),.6)
		art("terrain/oil_hatch.png",Vector2(1000,915),Vector2(166,139))
		light(Vector2(650,924),Color("479ea5"),1.5)
		light(Vector2(1200,584),Color("43858e"),.7)
	elif style == "crown":
		for at in [Vector2(725,985),Vector2(1265,990),Vector2(1000,1080)]:
			art("terrain/metal_repair.png",at,Vector2(169,111),null,-.035)
			light(at,Color("d1a46b"),1)
		light(Vector2(1000,535),Color("71c6cb"),2.3)
		art("infrastructure/stairs.png",Vector2(1000,955),Vector2(179,123))
		cable(PackedVector2Array([Vector2(805,960),Vector2(830,1050),Vector2(728,1097)]),floor_details)
	elif style == "harbor":
		for at in [Vector2(950,1160),Vector2(345,1160),Vector2(1630,1220)]:
			art("infrastructure/walkway.png",at,Vector2(160,188),null,.035)
			art("infrastructure/crane.png",at+Vector2(76,-80),Vector2(100,150))
			light(at,Color("7eacaa"),1.2)
		pipe_route(PackedVector2Array([Vector2(280,845),Vector2(680,845),Vector2(680,961)]))
		for at in [Vector2(510,800),Vector2(1450,760)]: art("infrastructure/scrap.png",at,Vector2(123,66))
	else:
		# External sectors have larger quiet clearings and restrained salvage clusters.
		for entry in [[Vector2(590,586),.14],[Vector2(1490,960),-.1],[Vector2(425,1150),.06],[Vector2(1550,460),-.2]]:
			art("terrain/market_dirt.png",entry[0],Vector2(225,134),null,entry[1]).modulate.a = .45
			art("infrastructure/scrap.png",entry[0],Vector2(166,90),null,entry[1])
			art("infrastructure/scrap.png",entry[0]+Vector2(72,36),Vector2(75,42),null,-entry[1])
		if style == "ruins":
			pipe_route(PackedVector2Array([Vector2(390,710),Vector2(390,805),Vector2(725,805),Vector2(725,755)]))
			light(Vector2(1000,485),Color("5b9da2"),1)
			art("infrastructure/service_arch.png",Vector2(1650,1160),Vector2(192,148))
	# Working clusters attach to selected facades and routes instead of filling every void.
	var work_sites := [Vector2(690,1120),Vector2(1460,1090),Vector2(1190,430)]
	if style == "harbor": work_sites = [Vector2(345,1110),Vector2(1020,1140),Vector2(1630,1155)]
	for at in work_sites:
		if style == "suspended": continue
		art("terrain/metal_repair.png",at,Vector2(76,48),null,.12)
		art("infrastructure/scrap.png",at+Vector2(43,5),Vector2(87,47),null,-.08)
		art("infrastructure/lantern.png",at+Vector2(-30,-21),Vector2(26,39))
		light(at,Color("cc9a60"),.6)
func player_and_hud() -> void:
	var packed: PackedScene = load("res://scenes/player/map_player.tscn")
	var player: CharacterBody2D = packed.instantiate(PackedScene.GEN_EDIT_STATE_INSTANCE)
	player.position = Vector2(config.spawn[0],config.spawn[1])
	add(player,structures)
	world.set_editable_instance(player,true)
	var cam: Camera2D = player.get_node("Camera")
	cam.limit_left = -100
	cam.limit_top = 0
	cam.limit_right = 2100
	cam.limit_bottom = 1600
	var hud := CanvasLayer.new()
	hud.name = "MapInfo"
	hud.layer = 25
	hud.set_script(load("res://scripts/world/region_hud.gd"))
	hud.add_to_group("slice_hud",true)
	add(hud,world)
	var panel := Control.new()
	panel.name = "Panel"
	panel.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add(panel,hud)
	for entry in [[config.get("region","FERRUGEM BAIXA"),Vector2(34,25),13],[config.name,Vector2(32,48),26],["WASD / SETAS mover    SHIFT correr    RODA zoom    E passagem    R voltar    F1 ocultar",Vector2(32,757),13]]:
		var label := Label.new()
		label.text = entry[0]
		label.position = entry[1]
		label.add_theme_font_size_override("font_size",entry[2])
		label.add_theme_color_override("font_color",Color("c7ba94"))
		add(label,panel)
	var veil := CanvasLayer.new()
	veil.layer = 20
	add(veil,world)
	var rect := ColorRect.new()
	rect.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	rect.mouse_filter = Control.MOUSE_FILTER_IGNORE
	var material := ShaderMaterial.new()
	material.shader = load("res://assets/fx/atmosphere.gdshader")
	rect.material = material
	add(rect,veil)
func save_scene(path: String) -> void:
	var packed := PackedScene.new()
	var err := packed.pack(world)
	if err == OK: err = ResourceSaver.save(packed,path)
	print("BUILT ",id," ",err," nodes=",world.get_child_count())
	world.queue_free()
func extract_player() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var slice: Node2D = packed.instantiate()
	var player := slice.get_node("Structures/Player").duplicate()
	player.owner = null
	for child in player.find_children("*","",true,false): child.owner = player
	var scene := PackedScene.new()
	scene.pack(player)
	ResourceSaver.save(scene,"res://scenes/player/map_player.tscn")
	player.free()
	slice.free()
func run() -> void:
	if FileAccess.get_file_as_string("res://maps/sucateia/sucateia.tscn").contains("MercadoReconstruido"):
		push_error("Night maps are layout drafts. Reconstruct one sector directly in the original using tools/rebuild_original.gd.")
		quit(1)
		return
	if FileAccess.get_file_as_string("res://maps/sucateia/sucateia.tscn").contains("ContinuousRoutes"):
		push_error("Sucateia is now an expanded continuous world. Use tools/extend_existing_world.gd; do not replace it with isolated sectors.")
		quit(1)
		return
	catalog = JSON.parse_string(FileAccess.get_file_as_string("res://maps/ferrugem_baixa/region.json"))
	for sector in catalog:
		var planned: Dictionary = catalog[sector]
		if not planned.has("function") or not planned.has("continuity"):
			push_error("Plan regional neighbours and continuity before rebuilding: "+sector)
			quit(1)
			return
		for destination in planned.links:
			if not planned.continuity.has(destination):
				push_error("Unplanned regional boundary: "+sector+" → "+destination)
				quit(1)
				return
	extract_player()
	for key in catalog:
		id = key
		config = catalog[id]
		if id == "centre":
			var packed: PackedScene = load(config.scene)
			world = packed.instantiate(PackedScene.GEN_EDIT_STATE_INSTANCE)
			root.add_child(world)
			if world.has_node("RegionPortals"): world.get_node("RegionPortals").free()
			if world.has_node("RegionalContinuity"): world.get_node("RegionalContinuity").free()
			var node := group_node("RegionPortals",1)
			floor_details = world.get_node("GroundDetails")
			for dest in config.links: portal(dest,Vector2(config.links[dest][0],config.links[dest][1]))
			await physics_frame
			load("res://scripts/world/regional_continuity_builder.gd").new().install(self)
			save_scene(config.scene)
			await process_frame
			continue
		world = Node2D.new()
		world.name = id.capitalize()
		world.set_script(load("res://scripts/world/region_world.gd"))
		world.set("region_id",id)
		floor_details = group_node("GroundDetails",-15)
		structures = group_node("Structures",0,true)
		upper = group_node("UpperDetails",8)
		group_node("Lighting",7)
		group_node("RegionPortals",1)
		group_node("RouteMarkers",0)
		var outline := PackedVector2Array()
		for point in config.outline: outline.append(Vector2(point[0],point[1]))
		terrain(outline)
		for entry in config.buildings: building(entry)
		details()
		load("res://scripts/world/region_extension_builder.gd").new().existing_details(self)
		for dest in config.links: portal(dest,Vector2(config.links[dest][0],config.links[dest][1]))
		var mark := Marker2D.new()
		mark.name = "Landmark"
		mark.position = Vector2(config.landmark[0],config.landmark[1])
		add(mark,world.get_node("RouteMarkers"))
		if config.has("markers"):
			for label in config.markers:
				var extra := Marker2D.new()
				extra.name = label
				extra.position = Vector2(config.markers[label][0],config.markers[label][1])
				add(extra,world.get_node("RouteMarkers"))
		backdrop()
		player_and_hud()
		root.add_child(world)
		await physics_frame
		await physics_frame
		load("res://scripts/world/regional_continuity_builder.gd").new().install(self)
		save_scene(config.scene)
		await process_frame
	quit(0)

func backdrop() -> void:
	if config.style in ["residential","crown"]:
		var skyline := art("generated/structures/skyline.png",Vector2(1040,104),Vector2(2150,360),upper)
		skyline.z_as_relative = false
		skyline.z_index = -35
		skyline.modulate = Color(.45,.51,.49,.8)
	elif config.style in ["forge","ruins"]:
		for at in [Vector2(305,245),Vector2(1770,322)]:
			var distant := art("region/foundry.png",at,Vector2(385,290),upper)
			distant.z_as_relative = false
			distant.z_index = -35
			distant.modulate = Color(.45,.47,.40,.72)
