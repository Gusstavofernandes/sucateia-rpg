extends SceneTree
var world: Node2D
var structures: Node2D
var ground: Node2D
var decor: Node2D
var lighting: Node2D
var foreground: Node2D
var rng := RandomNumberGenerator.new()
var obstacles: Array[Rect2] = []
var patina := ShaderMaterial.new()
const SIZE := Vector2(2400,1800)
const GENERATED := {
	"structures/house_0.svg":"generated/structures/house.png",
	"structures/house_1.svg":"generated/structures/house_stack.png",
	"structures/house_2.svg":"generated/structures/house.png",
	"structures/house_3.svg":"generated/structures/house_stack.png",
	"structures/workshop.svg":"generated/structures/workshop.png",
	"structures/reactor.svg":"generated/structures/reactor.png",
	"props/stall_0.svg":"generated/props/market_stall.png",
	"props/stall_1.svg":"generated/props/market_stall.png",
	"props/stall_2.svg":"generated/props/market_stall.png",
	"props/scrap.svg":"infrastructure/scrap.png"
}
func texture_for(file: String) -> Texture2D:
	return load("res://assets/"+str(GENERATED.get(file,file)))
func _initialize() -> void:
	call_deferred("build")
func own(node: Node, parent: Node) -> void:
	parent.add_child(node)
	node.owner = world
func container(label: String, z: int, sort: bool = false) -> Node2D:
	var node := Node2D.new()
	node.name = label
	node.z_index = z
	node.y_sort_enabled = sort
	own(node,world)
	return node
func box(parent: Node, at: Vector2, size: Vector2, color: Color) -> Polygon2D:
	return polygon(parent,PackedVector2Array([at,at+Vector2(size.x,0),at+size,at+Vector2(0,size.y)]),color)
func polygon(parent: Node, points: PackedVector2Array, color: Color) -> Polygon2D:
	var n := Polygon2D.new()
	n.polygon = points
	n.color = color
	own(n,parent)
	return n
func wire(parent: Node, points: PackedVector2Array, color: Color, width: float) -> Line2D:
	var n := Line2D.new()
	n.points = points
	n.default_color = color
	n.width = width
	n.antialiased = true
	n.joint_mode = Line2D.LINE_JOINT_ROUND
	n.begin_cap_mode = Line2D.LINE_CAP_ROUND
	n.end_cap_mode = Line2D.LINE_CAP_ROUND
	own(n,parent)
	return n
func art(parent: Node, file: String, pos: Vector2, scale_factor: float = 1.0) -> Sprite2D:
	var n := Sprite2D.new()
	n.texture = texture_for(file)
	n.position = pos
	n.scale = Vector2.ONE * scale_factor
	n.material = patina
	if GENERATED.has(file) or file.begins_with("generated/"):
		n.scale *= .5
		n.material = null
	own(n,parent)
	return n
func solid(parent: Node, at: Vector2, size: Vector2, label: String = "Solid") -> void:
	var n := StaticBody2D.new()
	n.name = label
	n.position = at
	own(n,parent)
	var collision := CollisionShape2D.new()
	var shape := RectangleShape2D.new()
	shape.size = size
	collision.shape = shape
	own(collision,n)
	obstacles.append(Rect2(at-size/2,size))
func building(file: String, base: Vector2, size: Vector2, factor: float = 1.0) -> void:
	var packed: PackedScene = load("res://scenes/props/reclaimed_structure.tscn")
	var n: Node2D = packed.instantiate(PackedScene.GEN_EDIT_STATE_INSTANCE)
	n.position = base
	n.scale = Vector2.ONE*factor
	n.name = file.get_basename().get_file()
	own(n,structures)
	world.set_editable_instance(n,true)

	var sprite: Sprite2D = n.get_node("Architecture")
	sprite.texture = texture_for("structures/"+file)
	sprite.scale = Vector2(.5,.5)
	sprite.material = null
	var shadow := art(n,"fx/light.svg",Vector2(0,-8))
	shadow.scale = Vector2(size.x*.83/256.0,55.0/256.0)
	shadow.modulate = Color(0,0,0,.55)
	shadow.material = null
	shadow.z_index = -1
	sprite.position = Vector2(0,-size.y/2+16/factor)
	var shape: RectangleShape2D = n.get_node("BuildingFootprint/Shape").shape
	shape.size = Vector2(size.x*.70,116)

func lamp(at: Vector2, color: Color, size: float = 1.0, parent: Node = null) -> void:
	var target: Node = lighting if parent == null else parent
	var n := PointLight2D.new()
	n.position = at
	n.texture = load("res://assets/fx/light.svg")
	n.color = color
	n.energy = 1.15
	n.texture_scale = size
	own(n,target)
func prop(file: String, pos: Vector2, scale_factor: float = 1.0, collision_size: Vector2 = Vector2.ZERO) -> void:
	var n := Node2D.new()
	n.position = pos
	n.name = file.get_basename()
	own(n,structures)
	var sprite := art(n,"props/"+file,Vector2(0,-22*scale_factor),scale_factor)
	if file.begins_with("stall_"): sprite.position.y = (-152.0/2.0+16)*scale_factor
	if collision_size != Vector2.ZERO: solid(n,Vector2(0,-10),collision_size)
func smoke(pos: Vector2, tint: Color, count: int = 10) -> void:
	var n := CPUParticles2D.new()
	n.name = "Vapor"
	n.position = pos
	n.texture = load("res://assets/fx/smoke_01.png")
	n.amount = count
	n.lifetime = 5.0
	n.preprocess = 3.0
	n.direction = Vector2(-.3,-1)
	n.spread = 15
	n.gravity = Vector2(-3,-5)
	n.initial_velocity_min = 16
	n.initial_velocity_max = 25
	n.scale_amount_min = .035
	n.scale_amount_max = .09
	var gradient := Gradient.new()
	gradient.set_color(0,Color(tint,0))
	gradient.add_point(.25,Color(tint,.19))
	gradient.add_point(.7,Color(tint,.11))
	gradient.set_color(gradient.get_point_count()-1,Color(tint,0))
	n.color_ramp = gradient
	own(n,foreground)
func marker(label: String, at: Vector2) -> void:
	var n := Marker2D.new()
	n.name = label
	n.position = at
	own(n,world.get_node("RouteMarkers"))
func text_at(words: String, at: Vector2, parent: Node, font_size: int = 15) -> void:
	var n := Label.new()
	n.text = words
	n.position = at
	n.add_theme_color_override("font_color",Color("b7b18e"))
	n.add_theme_font_size_override("font_size",font_size)
	own(n,parent)
func build() -> void:
	rng.seed = 83
	patina.shader = load("res://assets/fx/patina.gdshader")
	world = Node2D.new()
	world.name = "Sucateia"
	world.set_script(load("res://scripts/world/sucateia.gd"))
	root.add_child(world)
	ground = container("Ground",-30)
	decor = container("GroundDetails",-15)
	structures = container("Structures",0,true)
	lighting = container("Lighting",8)
	foreground = container("Foreground",12)
	container("RouteMarkers",0)
	var background := container("DistantCity",-40)
	box(background,Vector2.ZERO,SIZE,Color("131f23"))
	# Outer silhouettes behind the playable terraces.
	for x in [600,1800]:
		var silhouette := art(background,"generated/structures/skyline.png",Vector2(x,170))
		silhouette.modulate = Color(.5,.64,.64,.9)
	# Modern TileMapLayer with four terrain materials and seeded variants.
	var tiles := TileSet.new()
	tiles.tile_size = Vector2i(48,48)
	var source := TileSetAtlasSource.new()
	source.texture = load("res://assets/tiles/sucateia_atlas.svg")
	source.texture_region_size = Vector2i(48,48)
	for y in range(4):
		for x in range(4): source.create_tile(Vector2i(x,y))
	tiles.add_source(source,0)
	ResourceSaver.save(tiles,"res://assets/tiles/sucateia_tileset.tres")
	var layer := TileMapLayer.new()
	layer.name = "TerraceFloor"
	layer.tile_set = tiles
	layer.material = patina
	own(layer,ground)
	for y in range(7,35):
		for x in range(3,47):
			var row := 0
			if y > 28: row = 3
			elif x > 35: row = 2
			elif abs(x-24) < 3 or abs(y-22) < 2: row = 1
			layer.set_cell(Vector2i(x,y),0,Vector2i(rng.randi_range(0,3),row))
	# Collision banks stay invisible; painted infrastructure is installed below.
	art(decor,"generated/props/bridge.png",Vector2(1882,1063))
	for y in [1020,1107]:

		for x in range(1735,2050,40):

			solid(ground,Vector2(x,y),Vector2(7,8),"BridgePost")
	# Keep the same lower-wall solids and continuous 144px staircase gap.
	for x in [144,1584]:
		var width := 1296.0 if x == 144 else 216.0
		solid(ground,Vector2(x+width/2,1418),Vector2(width,65),"LowerRetainingWall")
	# Compose tightly packed masses around the main pedestrian loop.
	for entry in [[Vector2(410,650),0,1.0],[Vector2(697,610),1,.95],[Vector2(971,587),2,.88],[Vector2(1260,591),3,.9],[Vector2(420,992),2,1.0],[Vector2(706,954),0,.90],[Vector2(376,1310),1,1.05],[Vector2(733,1280),3,.93],[Vector2(1430,1264),0,.75],[Vector2(1660,1290),2,.7],[Vector2(2120,641),3,.75],[Vector2(2100,972),1,.78],[Vector2(2150,1325),2,.82]]:
		building("house_%d.svg" % entry[1],entry[0],Vector2(320,320),entry[2])
	building("workshop.svg",Vector2(1530,879),Vector2(416,368),1.1)
	building("reactor.svg",Vector2(1134,937),Vector2(256,296),.95)
	lamp(Vector2(1134,775),Color("70c9c3"),2.1)
	lamp(Vector2(1415,807),Color("efa257"),2.3)
	# Intentionally clustered stalls leave plaza and crossings readable.
	for entry in [[Vector2(917,1036),0],[Vector2(961,1198),1],[Vector2(1264,1150),2],[Vector2(1227,701),1]]:
		prop("stall_%d.svg" % entry[1],entry[0],.83,Vector2(139,43))
	for entry in [[Vector2(536,661),"barrel"],[Vector2(560,683),"crate"],[Vector2(537,1012),"crate"],[Vector2(578,1040),"scrap"],[Vector2(829,589),"barrel"],[Vector2(847,613),"scrap"],[Vector2(1570,927),"crate"],[Vector2(1650,940),"scrap"],[Vector2(1333,1000),"barrel"],[Vector2(1620,1520),"scrap"],[Vector2(1640,1572),"barrel"],[Vector2(2086,1424),"crate"],[Vector2(2105,1460),"scrap"]]:
		prop(entry[1]+".svg",entry[0],.9,Vector2(38,27) if entry[1] != "scrap" else Vector2(82,22))
	# Lower machinery, pipes, reclaimed gothic arches.
	building("reactor.svg",Vector2(1060,1650),Vector2(256,296),.58)
	lamp(Vector2(1060,1555),Color("5798a5"),1.1)

	# Weathered offcuts accumulate along specific building edges.
	for anchor in [Vector2(565,689),Vector2(807,988),Vector2(1580,951),Vector2(1710,1320),Vector2(850,650)]:
		for i in range(19):
			var at: Vector2 = anchor + Vector2(rng.randf_range(-45,45),rng.randf_range(-13,23))
			wire(decor,PackedVector2Array([at,at+Vector2(rng.randf_range(3,13),rng.randf_range(-3,3))]),Color("8f7953"),rng.randf_range(1,3))
	# Main feeder pipe leads from the foundry to the pressure machine.
	for x in [1360,1474,1588,1663]:
		art(decor,"generated/props/pipe.png",Vector2(x,968))
	for y in [828,922]:
		var upright := art(decor,"generated/props/pipe.png",Vector2(1714,y),.83)
		upright.rotation = PI/2

	var terrain = load("res://scripts/world/terrain_builder.gd").new()
	terrain.install(world,ground,structures)
	var infrastructure = load("res://scripts/world/infrastructure_builder.gd").new()
	infrastructure.install(world,foreground)
	var coastal = load("res://scripts/world/coastal_builder.gd").new()
	coastal.install(world)
	# Overhead hanging cables: gentle catenaries, anchoring visible masses.
	for connection in [[Vector2(400,600),Vector2(1540,680)],[Vector2(620,520),Vector2(1300,530)],[Vector2(1300,900),Vector2(2100,960)],[Vector2(450,1150),Vector2(1240,1160)]]:
		var start: Vector2 = connection[0]
		var end: Vector2 = connection[1]
		var points := PackedVector2Array()
		for i in range(25):
			var t := i/24.0
			points.append(start.lerp(end,t)+Vector2(0,sin(t*PI)*65))
		wire(foreground,points,Color("152a28"),4)
		wire(foreground,points+PackedVector2Array(),Color("796f51"),1)
		for i in [5,12,19]:
			var p: Vector2 = points[i]
			wire(foreground,PackedVector2Array([p,p+Vector2(0,12)]),Color("716347"),1.3)
			var lantern := art(foreground,"infrastructure/lantern.png",p+Vector2(0,25),.33)
			lantern.material = null
			lamp(p+Vector2(0,25),Color("e0a55c"),.65)
	# Warm lights at human scale, sparks and drifting chimney vapor.
	for p in [Vector2(410,626),Vector2(693,924),Vector2(1263,1120),Vector2(2140,1278)]: lamp(p,Color("e3a963"),.8)
	smoke(Vector2(1377,520),Color("a7a58b"),14)
	smoke(Vector2(1630,497),Color("abb5a5"),12)
	smoke(Vector2(1140,700),Color("72a6a0"),7)
	smoke(Vector2(550,1410),Color("7d9784"),8)
	var sparks := CPUParticles2D.new()
	sparks.position = Vector2(1420,819)
	sparks.amount = 16
	sparks.lifetime = 1.2
	sparks.direction = Vector2(0,-1)
	sparks.spread = 55
	sparks.gravity = Vector2(0,32)
	sparks.initial_velocity_min = 18
	sparks.initial_velocity_max = 48
	sparks.scale_amount_min = .9
	sparks.scale_amount_max = 1.4
	sparks.color = Color("f7c481")
	own(sparks,foreground)
	var ambient := CanvasModulate.new()
	ambient.name = "Atmosphere"
	ambient.color = Color(.72,.79,.75)
	own(ambient,lighting)
	# Boundary bodies prevent walking into background space.
	solid(ground,Vector2(1200,340),Vector2(2160,32),"NorthBoundary")
	marker("Spawn",Vector2(1152,1248))
	marker("Market",Vector2(1120,1060))
	marker("Workshop",Vector2(1510,1000))
	marker("AltoLixo",Vector2(1140,450))
	marker("Bridge",Vector2(1870,1060))
	marker("OsCabos",Vector2(2110,1110))
	marker("LowerStairs",Vector2(1512,1470))
	marker("FundoFerro",Vector2(1296,1570))
	marker("CoastalQuay",Vector2(1600,1610))
	var player := CharacterBody2D.new()
	player.name = "Player"
	player.position = Vector2(1152,1248)
	player.collision_layer = 2
	player.collision_mask = 1
	player.set_script(load("res://scripts/world/test_player.gd"))
	player.add_to_group("player",true)
	own(player,structures)
	var sprite := art(player,"props/test_goblin.svg",Vector2(0,-22),.85)
	sprite.name = "Sprite"
	var collision := CollisionShape2D.new()
	var shape := CircleShape2D.new()
	shape.radius = 10
	collision.shape = shape
	own(collision,player)
	var camera := Camera2D.new()
	camera.name = "Camera"
	camera.zoom = Vector2(.95,.95)
	camera.position_smoothing_enabled = true
	camera.position_smoothing_speed = 6
	camera.limit_left = 0
	camera.limit_top = 0
	camera.limit_right = 2400
	camera.limit_bottom = 2020
	own(camera,player)

	var veil_layer := CanvasLayer.new()
	veil_layer.name = "AirAndVignette"
	veil_layer.layer = 20
	own(veil_layer,world)
	var veil := ColorRect.new()
	veil.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	veil.mouse_filter = Control.MOUSE_FILTER_IGNORE
	var veil_material := ShaderMaterial.new()
	veil_material.shader = load("res://assets/fx/atmosphere.gdshader")
	veil.material = veil_material
	own(veil,veil_layer)

	# Minimal map title and controls, no full game interface.
	var hud := CanvasLayer.new()
	hud.name = "MapInfo"
	hud.layer = 25
	hud.set_script(load("res://scripts/world/slice_hud.gd"))
	hud.add_to_group("slice_hud",true)
	own(hud,world)
	var panel := Control.new()
	panel.name = "Panel"
	panel.mouse_filter = Control.MOUSE_FILTER_IGNORE
	own(panel,hud)
	text_at("F E R R U G E M  B A I X A",Vector2(35,25),panel,12)
	text_at("Sucateia",Vector2(32,43),panel,34)
	var district := Label.new()
	district.name = "District"
	district.position = Vector2(35,86)
	district.add_theme_font_size_override("font_size",12)
	district.add_theme_color_override("font_color",Color("b3b59b"))
	own(district,panel)
	text_at("WASD / SETAS   mover     SHIFT   correr     RODA   zoom     R   voltar     F1   ocultar",Vector2(34,757),panel,13)
	var packed := PackedScene.new()
	var err := packed.pack(world)
	if err == OK: err = ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("SCENE SAVED ",err," / ",obstacles.size()," collision bodies")
	quit(err)







