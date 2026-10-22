extends RefCounted
var world: Node2D
var infrastructure: Node2D
func add(node: Node, parent: Node) -> void:
	parent.add_child(node)
	node.owner = world
func art(file: String, at: Vector2, size: Vector2, angle: float = 0, parent: Node = null) -> Sprite2D:
	var sprite := Sprite2D.new()
	sprite.name = file.get_basename()
	sprite.texture = load("res://assets/infrastructure/"+file+".png")
	sprite.position = at
	sprite.scale = size/Vector2(sprite.texture.get_size())
	sprite.rotation = angle
	add(sprite,infrastructure if parent == null else parent)
	return sprite
func shadow(at: Vector2, size: Vector2, opacity: float = .46) -> void:
	var sprite := Sprite2D.new()
	sprite.texture = load("res://assets/fx/light.svg")
	sprite.position = at
	sprite.scale = size/256.0
	sprite.modulate = Color(0,0,0,opacity)
	add(sprite,infrastructure)
func edge_row(start: float, finish: float, y: float) -> void:
	var count := maxi(1,roundi((finish-start)/184.0))
	var step := (finish-start)/count
	for i in range(count):
		var x := start+step*(i+.5)
		var offset: float = [-2.0,2.5,0.0,3.0][i%4]
		shadow(Vector2(x+6,y+23),Vector2(step+25,75),.46)
		var module := art("retaining_edge",Vector2(x,y+offset),Vector2(step+10,80),.006 if i%2 else -.005)
		module.modulate = Color(.97,1,.96) if i%3 == 0 else Color(1,1,1)
func edge_column(x: float, start: float, finish: float) -> void:
	var count := maxi(1,roundi((finish-start)/174.0))
	var step := (finish-start)/count
	for i in range(count):
		art("retaining_edge",Vector2(x+(-2 if i%2 else 1),start+step*(i+.5)),Vector2(step+8,46),PI/2)
func pipe(at: Vector2, angle: float = 0) -> void:
	var sprite := Sprite2D.new()
	sprite.texture = load("res://assets/generated/props/pipe.png")
	sprite.position = at
	sprite.scale = Vector2(.50,.42)
	sprite.rotation = angle
	add(sprite,infrastructure)
func install(target: Node2D, foreground: Node2D) -> void:
	world = target
	infrastructure = Node2D.new()
	infrastructure.name = "FinishedInfrastructure"
	infrastructure.z_index = -14
	add(infrastructure,world)
	# Both the painted bank and collision follow the same stepped canal profile.
	var left := PackedVector2Array([Vector2(1802,380),Vector2(1802,475),Vector2(1830,530),Vector2(1827,620),Vector2(1778,690),Vector2(1768,800),Vector2(1794,878),Vector2(1794,965),Vector2(1789,1026),Vector2(1789,1100),Vector2(1795,1170),Vector2(1830,1232),Vector2(1821,1320),Vector2(1772,1410),Vector2(1776,1510),Vector2(1800,1590),Vector2(1800,1670)])
	var right := PackedVector2Array([Vector2(1956,380),Vector2(1956,475),Vector2(1972,530),Vector2(1965,620),Vector2(1926,690),Vector2(1929,800),Vector2(1944,878),Vector2(1951,965),Vector2(1963,1026),Vector2(1963,1100),Vector2(1969,1170),Vector2(1987,1232),Vector2(1978,1320),Vector2(1940,1410),Vector2(1936,1510),Vector2(1955,1590),Vector2(1955,1670)])
	var outline := left.duplicate()
	for i in range(right.size()-1,-1,-1): outline.append(right[i])
	var channel := Polygon2D.new()
	channel.name = "IndustrialRunoff"
	channel.z_index = -18
	channel.polygon = outline
	var material := ShaderMaterial.new()
	material.shader = load("res://assets/infrastructure/channel.gdshader")
	material.set_shader_parameter("channel_surface",load("res://assets/infrastructure/channel.png"))
	channel.material = material
	add(channel,world)
	channel_collision(left.slice(0,9),right.slice(0,9),"ChannelNorth")
	channel_collision(left.slice(9),right.slice(9),"ChannelSouth")
	bank(left)
	bank(right)
	# The eastern deck has narrow links, widened landings and visibly repaired bays.
	for bay in [[2020,455,178,205,-.016],[2170,463,170,214,.014],[2029,662,157,201,.009],[2180,682,195,206,-.012],[2010,843,183,184,-.018],[2176,876,166,224,.005],[2021,1064,204,162,0.0],[2190,1080,176,178,-.021],[2040,1234,183,217,.012],[2198,1280,153,173,-.018],[2014,1441,158,214,.018],[2160,1496,204,191,-.009],[2037,1630,194,145,-.013],[2190,1640,157,148,.022]]:
		var deck := art("walkway",Vector2(bay[0],bay[1]),Vector2(bay[2],bay[3]),bay[4])
		deck.modulate = Color(.90,.93,.86) if bay[1] < 900 else Color(.98,.93,.84)
	# Cantilever maintenance pockets remain on the safe bank side of the canal.
	for pocket in [[Vector2(1735,754),-.11],[Vector2(1998,578),.09],[Vector2(1740,1466),-.05],[Vector2(2010,1366),.07]]:
		shadow(pocket[0]+Vector2(5,15),Vector2(125,92),.65)
		art("walkway",pocket[0],Vector2(115,97),pocket[1])
		art("stairs",pocket[0]+Vector2(-12,69),Vector2(66,62),pocket[1])
		pipe(pocket[0]+Vector2(-37,-18),PI/2)
		art("retaining_edge",pocket[0]+Vector2(3,-45),Vector2(104,34),pocket[1])
	for outlet in [[Vector2(1812,581),0.0],[Vector2(1945,1480),PI]]:
		pipe(outlet[0],outlet[1])
		decal("market_dirt",outlet[0]+Vector2(-28,29),Vector2(117,64),.58,.18)
		shadow(outlet[0]+Vector2(26,24),Vector2(65,102),.54)
		decal("oil_hatch",outlet[0]+Vector2(-65,12),Vector2(67,55),.59,-.1)
		var leak := Sprite2D.new()
		leak.texture = load("res://assets/fx/light.svg")
		leak.position = outlet[0]+Vector2(36,28)
		leak.scale = Vector2(.20,.38)
		leak.modulate = Color(.19,.37,.29,.23)
		add(leak,infrastructure)
	# Distinct deck repairs and cable loops break the repeated grate rhythm.
	for repair in [[Vector2(2050,555),Vector2(91,76),.14],[Vector2(2112,787),Vector2(118,84),-.13],[Vector2(2050,1170),Vector2(94,66),.06],[Vector2(2125,1392),Vector2(126,79),-.07],[Vector2(2150,1600),Vector2(88,63),.11]]:
		decal("metal_repair",repair[0],repair[1],.95,repair[2])
		pipe(repair[0]+Vector2(-46,28),PI/2)
	cable(PackedVector2Array([Vector2(1998,590),Vector2(2010,718),Vector2(2058,770),Vector2(2104,766)]))
	cable(PackedVector2Array([Vector2(2175,1168),Vector2(2218,1195),Vector2(2208,1370),Vector2(2140,1403)]))
	# Perimeter and lower terrace lip, including the staircase opening.
	edge_row(144,2256,335)
	edge_row(144,1440,1418)
	edge_row(1584,1800,1418)
	# Real treads and chain handrails link the unchanged pedestrian levels.
	shadow(Vector2(1517,1437),Vector2(170,136),.5)
	art("stairs",Vector2(1512,1428),Vector2(144,110))
	# Service portals belong to the lower retaining wall instead of free-standing boxes.
	for x in [395,655,915,1175]:
		shadow(Vector2(x,1459),Vector2(136,55),.42)
		art("service_arch",Vector2(x,1435),Vector2(160,132))
	# The lower feeder is assembled from the same textured pipe family as the forge.
	for x in range(285,967,111): pipe(Vector2(x,1550))
	for y in [1388,1497]: pipe(Vector2(246,y),PI/2)
	# Small fully textured service gratings replace blank geometric grate blocks.
	for at in [Vector2(851,1012),Vector2(1690,978),Vector2(1300,1298)]:
		art("walkway",at,Vector2(65,54))
	# Foreground support, anchored to the western wall with an actual chain and hook.
	art("crane",Vector2(255,663),Vector2(195,286),0,foreground)
	# Textured joints tie the pressure machine to its existing copper feeder.
	pipe(Vector2(1263,879))
	pipe(Vector2(1300,924),PI/2)
	street_life()
	print("INFRA: painted terrace edges, grate decks, stairs, portals, runoff and gantry")


func channel_collision(left: PackedVector2Array, right: PackedVector2Array, label: String) -> void:
	var outline := left.duplicate()
	for i in range(right.size()-1,-1,-1): outline.append(right[i])
	var body := StaticBody2D.new()
	body.name = label
	add(body,world)
	var shape := CollisionPolygon2D.new()
	shape.polygon = outline
	add(shape,body)
func bank(points: PackedVector2Array) -> void:
	for i in range(points.size()-1):
		var a := points[i]
		var b := points[i+1]
		if a.y >= 1026 and b.y <= 1100: continue
		var delta := b-a
		var length := delta.length()
		var midpoint := (a+b)*.5
		shadow(midpoint+Vector2(4,9),Vector2(61,length+29),.51)
		var ledge := art("retaining_edge",midpoint,Vector2(length+12,43+(i%3)*3),delta.angle())
		ledge.modulate = Color(.92,.95,.88) if i%3 == 0 else Color(1,1,1)
		if i in [2,5,10,13]:
			decal("metal_repair",a,Vector2(58,65),.84,-.09)
			art("retaining_edge",a+Vector2(0,7),Vector2(51,52),PI/2)
func decal(file: String, at: Vector2, size: Vector2, alpha: float, angle: float = 0) -> void:
	var sprite := Sprite2D.new()
	sprite.texture = load("res://assets/terrain/"+file+".png")
	sprite.position = at
	sprite.scale = size/Vector2(sprite.texture.get_size())
	sprite.modulate.a = alpha
	sprite.rotation = angle
	add(sprite,infrastructure)
func cable(points: PackedVector2Array) -> void:
	for entry in [[Color("17211d"),5.0],[Color("726045"),1.25]]:
		var wire := Line2D.new()
		wire.points = points
		wire.width = entry[1]
		wire.default_color = entry[0]
		wire.joint_mode = Line2D.LINE_JOINT_ROUND
		wire.begin_cap_mode = Line2D.LINE_CAP_ROUND
		wire.end_cap_mode = Line2D.LINE_CAP_ROUND
		wire.antialiased = true
		add(wire,infrastructure)
func street_life() -> void:
	# Sparse work sites sit beside the routes, never across a crossing or doorway.
	for entry in [[Vector2(817,820),-.15],[Vector2(1012,1338),.13],[Vector2(1610,1172),-.09],[Vector2(1439,540),.18]]:
		var at: Vector2 = entry[0]
		decal("market_dirt",at,Vector2(167,99),.47,entry[1])
		shadow(at+Vector2(12,9),Vector2(109,49),.52)
		art("scrap",at+Vector2(-26,0),Vector2(84,45),entry[1])
		art("walkway",at+Vector2(44,6),Vector2(47,54),entry[1])
		pipe(at+Vector2(9,-29),entry[1])
		decal("metal_repair",at+Vector2(22,43),Vector2(51,32),.8,-entry[1])
	# Each selected home gets a purposeful utility annex rather than a sprite recolor.
	for entry in [[Vector2(530,615),Vector2(79,68),-.08],[Vector2(804,594),Vector2(64,76),.04],[Vector2(1094,565),Vector2(81,60),-.06],[Vector2(526,966),Vector2(65,74),.09],[Vector2(836,1260),Vector2(94,70),-.07],[Vector2(2010,917),Vector2(64,91),.06]]:
		var at: Vector2 = entry[0]
		shadow(at+Vector2(8,31),Vector2(113,64),.60)
		art("service_arch",at+Vector2(0,26),Vector2(entry[1].x,65))
		art("walkway",at,entry[1],entry[2])
		pipe(at+Vector2(-30,7),PI/2)
		decal("foundation",at+Vector2(0,44),Vector2(102,56),.68)
	# Small amber service lanterns punctuate bends and repair sites.
	for at in [Vector2(835,851),Vector2(1601,1199),Vector2(1740,800),Vector2(2010,1398)]:
		pipe(at+Vector2(0,-29),PI/2)
		art("lantern",at+Vector2(2,-44),Vector2(28,42))
		var glow := Sprite2D.new()
		glow.texture = load("res://assets/fx/light.svg")
		glow.position = at
		glow.scale = Vector2(.45,.26)
		glow.modulate = Color(.63,.35,.11,.17)
		add(glow,infrastructure)
	cable(PackedVector2Array([Vector2(819,832),Vector2(879,844),Vector2(910,884),Vector2(943,902)]))
	cable(PackedVector2Array([Vector2(1550,1160),Vector2(1603,1180),Vector2(1640,1230)]))
