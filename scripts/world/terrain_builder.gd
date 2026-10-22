extends RefCounted
# All additions are ground-level decoration, outside the collision/navigation layers.
var world: Node2D
var details: Node2D
func add(node: Node, parent: Node) -> void:
	parent.add_child(node)
	node.owner = world
func stamp(file: String, at: Vector2, size: Vector2, alpha: float = 1.0, angle: float = 0.0) -> Sprite2D:
	var sprite := Sprite2D.new()
	sprite.texture = load("res://assets/terrain/"+file+".png")
	sprite.position = at
	sprite.scale = size/Vector2(sprite.texture.get_size())
	sprite.modulate = Color(1,1,1,alpha)
	sprite.rotation = angle
	add(sprite,details)
	return sprite
func stain(at: Vector2, size: Vector2, color: Color) -> void:
	var sprite := Sprite2D.new()
	sprite.texture = load("res://assets/fx/light.svg")
	sprite.position = at
	sprite.scale = size/256.0
	sprite.modulate = color
	add(sprite,details)
func line(points: PackedVector2Array, color: Color, width: float) -> void:
	var n := Line2D.new()
	n.points = points
	n.default_color = color
	n.width = width
	n.antialiased = true
	n.joint_mode = Line2D.LINE_JOINT_ROUND
	n.begin_cap_mode = Line2D.LINE_CAP_ROUND
	n.end_cap_mode = Line2D.LINE_CAP_ROUND
	add(n,details)
func install(target: Node2D, ground: Node2D, structures: Node2D) -> void:
	world = target
	details = Node2D.new()
	details.name = "TerrainIntegration"
	details.z_index = -20
	add(details,world)
	var floor_layer: TileMapLayer = ground.get_node("TerraceFloor")
	var tiles := TileSet.new()
	tiles.tile_size = Vector2i(48,48)
	var source := TileSetAtlasSource.new()
	source.texture = load("res://assets/terrain/floor_atlas.png")
	source.texture_region_size = Vector2i(48,48)
	for y in range(16):
		for x in range(16): source.create_tile(Vector2i(x,y))
	tiles.add_source(source,0)
	floor_layer.clear()
	floor_layer.tile_set = tiles
	var material := ShaderMaterial.new()
	material.shader = load("res://assets/terrain/terrain.gdshader")
	floor_layer.material = material
	for y in range(7,35):
		for x in range(3,47): floor_layer.set_cell(Vector2i(x,y),0,Vector2i((x-3)%16,(y-7)%16))
	ResourceSaver.save(tiles,"res://assets/terrain/sucateia_terrain.tres")
	# Foundations and dirt gather at structural feet instead of blank tile underneath.
	var index := 0
	for building in structures.get_children():
		if not building.has_node("Architecture"): continue
		var shape: RectangleShape2D = building.get_node("BuildingFootprint/Shape").shape
		var width: float = shape.size.x * building.scale.x
		var base: Vector2 = building.position
		stain(base+Vector2(10,1),Vector2(width*1.5,92),Color(.07,.09,.07,.65))
		stain(base+Vector2(-width*.38,9),Vector2(88,70),Color(.30,.21,.12,.35))
		stamp("foundation",base+Vector2(0,-25),Vector2(width+35,103),.86,.015 if index%2 else -.015)
		# Reclaimed door tread and metallic shims are unique to alternating modules.
		if index%3 == 1: stamp("metal_repair",base+Vector2(width*.20,20),Vector2(55,36),.78,.08)
		if index%3 == 2: stamp("market_dirt",base+Vector2(-width*.36,19),Vector2(95,61),.55,-.15)
		index += 1
	# Small market clearings: compressed dirt without hiding the pedestrian loop.
	for entry in [[Vector2(920,1048),Vector2(195,92),-.08],[Vector2(964,1217),Vector2(208,104),.12],[Vector2(1260,1170),Vector2(207,98),-.07]]:
		stamp("market_dirt",entry[0],entry[1],.71,entry[2])
		stain(entry[0]+Vector2(9,9),entry[1]*1.25,Color(.31,.24,.13,.24))
	# Forge forecourt: soot, repairs, flush inspection cover and embedded short rails.
	stain(Vector2(1510,950),Vector2(460,235),Color(.035,.045,.04,.70))
	stamp("oil_hatch",Vector2(1557,966),Vector2(132,118),.88,.17)
	stamp("metal_repair",Vector2(1440,905),Vector2(159,80),.88,-.04)
	stamp("metal_repair",Vector2(1668,1020),Vector2(94,71),.76,.08)
	stamp("metal_repair",Vector2(1460,1013),Vector2(174,54),.74,-.02)
	stamp("metal_repair",Vector2(1630,1005),Vector2(132,51),.72,-.04)
	# Cracked residential repairs, attached to door approaches rather than scattered.
	for at in [Vector2(536,737),Vector2(797,680),Vector2(548,1092),Vector2(833,1350)]:
		line(PackedVector2Array([at,at+Vector2(13,-15),at+Vector2(9,-28),at+Vector2(29,-36)]),Color(.10,.13,.11,.62),2)
		line(PackedVector2Array([at+Vector2(9,-28),at+Vector2(-10,-34)]),Color(.10,.13,.11,.46),1.4)
	# Salvaged plates at the bridge landings and lower service routes.
	stamp("metal_repair",Vector2(1715,1062),Vector2(118,87),.85,-.02)
	stamp("metal_repair",Vector2(2040,1065),Vector2(124,86),.85,.03)
	stamp("oil_hatch",Vector2(1318,1548),Vector2(125,100),.74,.1)
	stamp("metal_repair",Vector2(1513,1510),Vector2(133,73),.8,-.01)
	# Flush ground cables connect maintenance patches to architectural bases.
	for connection in [[Vector2(1320,1280),Vector2(1414,1280),Vector2(1445,1305)],[Vector2(2025,1070),Vector2(2025,1160),Vector2(2070,1176)]]:
		var path := PackedVector2Array(connection)
		line(path,Color("28342f"),4)
		line(path,Color("7a6747"),1.3)
	# Compressed foot traffic appears at connections, with breaks rather than a road stripe.
	for entry in [[Vector2(1139,1217),Vector2(73,102),.10],[Vector2(1115,1138),Vector2(83,98),-.12],[Vector2(1161,1059),Vector2(115,67),-.06],[Vector2(1285,1068),Vector2(104,74),.08],[Vector2(1409,1053),Vector2(119,68),-.1],[Vector2(1533,1067),Vector2(99,75),.08],[Vector2(1676,1060),Vector2(91,61),-.06],[Vector2(1210,1301),Vector2(105,63),.13],[Vector2(1345,1320),Vector2(108,66),-.06],[Vector2(1483,1351),Vector2(98,69),.12],[Vector2(1509,1542),Vector2(78,105),-.07],[Vector2(913,1097),Vector2(102,60),.09],[Vector2(773,1098),Vector2(89,57),-.1],[Vector2(729,722),Vector2(112,57),-.08],[Vector2(1056,736),Vector2(115,54),.07]]:
		stamp("market_dirt",entry[0],entry[1],.34,entry[2])
	# Light reflected on dust at thresholds anchors luminous facades to their street.
	for at in [Vector2(410,663),Vector2(706,967),Vector2(1430,1270)]:
		stain(at,Vector2(105,73),Color(.63,.35,.11,.18))
	print("TERRAIN: seamless atlas, 16 foundations, 3 market courts, forge service yard")
