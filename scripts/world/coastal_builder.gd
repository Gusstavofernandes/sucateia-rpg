extends RefCounted
# Coastal construction is independent of approved buildings and circulation.
var world: Node2D
var coast: Node2D
var water_material: ShaderMaterial
func add(node: Node, parent: Node) -> void:
	parent.add_child(node)
	node.owner = world
func sprite(file: String, at: Vector2, size: Vector2, angle: float = 0) -> Sprite2D:
	var n := Sprite2D.new()
	n.texture = load("res://assets/"+file)
	n.position = at
	n.scale = size/Vector2(n.texture.get_size())
	n.rotation = angle
	add(n,coast)
	return n
func water(points: PackedVector2Array, z: int, label: String) -> void:
	var n := Polygon2D.new()
	n.name = label
	n.polygon = points
	n.material = water_material
	n.z_index = z
	add(n,world)
func barrier(points: PackedVector2Array, label: String) -> void:
	var body := StaticBody2D.new()
	body.name = label
	add(body,world)
	var shape := CollisionPolygon2D.new()
	shape.polygon = points
	add(shape,body)
func stain(at: Vector2, size: Vector2, color: Color) -> void:
	var n := sprite("fx/light.svg",at,size)
	n.modulate = color
func line(points: PackedVector2Array, color: Color, width: float) -> void:
	var n := Line2D.new()
	n.points = points
	n.width = width
	n.default_color = color
	n.antialiased = true
	n.joint_mode = Line2D.LINE_JOINT_ROUND
	add(n,coast)
func side(points: PackedVector2Array, west: bool) -> void:
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i]
		var at := (points[i+1]+points[i])*.5
		stain(at+Vector2(-10 if west else 13,8),Vector2(95,delta.length()+24),Color(0,0,0,.60))
		var wall := sprite("infrastructure/retaining_edge.png",at,Vector2(delta.length()+13,70+(i%3)*9),delta.angle())
		wall.modulate = Color(.80,.87,.73) if i%3 == 1 else Color(.91,.93,.84)
		# Unequal transverse buttresses project from the coping into the water.
		if i%2 == 0:
			var end := points[i]+Vector2(-24 if west else 25,19)
			sprite("infrastructure/retaining_edge.png",end,Vector2(89,47),-.08 if west else .07)
			stain(end+Vector2(0,18),Vector2(85,43),Color(.13,.20,.10,.42))
			sprite("terrain/metal_repair.png",points[i]+Vector2(12 if west else -14,0),Vector2(58,52),.1)
func install(target: Node2D) -> void:
	world = target
	coast = Node2D.new()
	coast.name = "GoblinIndustrialQuay"
	coast.z_index = -12
	add(coast,world)
	water_material = ShaderMaterial.new()
	water_material.shader = load("res://assets/infrastructure/sea.gdshader")
	water_material.set_shader_parameter("grime",load("res://assets/infrastructure/channel.png"))
	water(PackedVector2Array([Vector2(-900,335),Vector2(3300,335),Vector2(3300,2600),Vector2(-900,2600)]),-35,"IndustrialSea")
	var west := PackedVector2Array([Vector2(148,335),Vector2(148,520),Vector2(130,610),Vector2(143,790),Vector2(159,880),Vector2(145,1050),Vector2(120,1160),Vector2(141,1300),Vector2(151,1460),Vector2(133,1580),Vector2(144,1670)])
	var east := PackedVector2Array([Vector2(2248,335),Vector2(2248,518),Vector2(2270,606),Vector2(2253,782),Vector2(2240,880),Vector2(2260,1030),Vector2(2278,1170),Vector2(2250,1285),Vector2(2238,1460),Vector2(2256,1568),Vector2(2256,1676)])
	var west_sea := west.duplicate()
	west_sea.append(Vector2(-900,1900));west_sea.append(Vector2(-900,335))
	var east_sea := east.duplicate()
	east_sea.append(Vector2(3300,1900));east_sea.append(Vector2(3300,335))
	water(west_sea,-16,"WestWaterline")
	water(east_sea,-16,"EastWaterline")
	barrier(west_sea,"WestCoastalBarrier")
	barrier(east_sea,"EastCoastalBarrier")
	side(west,true)
	side(east,false)
	# Uneven coping heights and buttress widths break the south terrace silhouette.
	var shore := PackedVector2Array([Vector2(144,1670),Vector2(371,1670),Vector2(581,1689),Vector2(817,1676),Vector2(1032,1682),Vector2(1247,1669),Vector2(1464,1686),Vector2(1702,1675),Vector2(1800,1670),Vector2(1955,1670),Vector2(2058,1688),Vector2(2256,1676)])
	var south_sea := shore.duplicate()
	south_sea.append(Vector2(3000,2600));south_sea.append(Vector2(-800,2600))
	water(south_sea,-16,"SouthWaterline")
	barrier(south_sea,"SouthCoastalBarrier")
	for i in range(shore.size()-1):
		if i == 8: continue # The industrial runoff empties through an open outfall.
		var delta := shore[i+1]-shore[i]
		var at := (shore[i+1]+shore[i])*.5
		stain(at+Vector2(3,42),Vector2(delta.length()+52,100),Color(0,0,0,.59))
		var section := sprite("infrastructure/coastal_wall.png",at+Vector2(0,4),Vector2(delta.length()+13,106+(i%3)*7),delta.angle())
		section.modulate = Color(.93,.96,.86) if i%3 == 1 else Color(1,1,1)
		stain(at+Vector2(0,54),Vector2(delta.length()*.86,38),Color(.12,.22,.12,.31))
	# A tiny chained timber-and-grate landing sits below the coast's retaining level.
	for entry in [[Vector2(635,1752),Vector2(126,137),-.04],[Vector2(2180,1740),Vector2(126,128),.06],[Vector2(2300,1128),Vector2(121,91),-.03]]:
		var at: Vector2 = entry[0]
		stain(at+Vector2(7,17),entry[1]*1.22,Color(0,0,0,.64))
		sprite("infrastructure/walkway.png",at,entry[1],entry[2])
		sprite("infrastructure/stairs.png",at+Vector2(0,-57),Vector2(66,82),entry[2])
		for offset in [Vector2(-44,37),Vector2(46,22)]:
			sprite("infrastructure/retaining_edge.png",at+offset,Vector2(42,60),PI/2)
		line(PackedVector2Array([at+Vector2(-45,-43),at+Vector2(-47,10),at+Vector2(-43,35)]),Color("554b35"),2)
	# Rusty outfalls, fouled water and damp repair plates explain the coastal function.
	for at in [Vector2(382,1690),Vector2(1379,1698),Vector2(2247,803),Vector2(142,1205)]:
		var south: bool = at.y > 1600
		sprite("generated/props/pipe.png",at,Vector2(109,32),PI/2 if south else 0)
		var discharge: Vector2 = at+Vector2(0,47) if south else at+Vector2(37,12)
		stain(discharge,Vector2(112,81),Color(.19,.23,.10,.29))
		stain(discharge+Vector2(9,14),Vector2(117,96),Color(.02,.035,.023,.44))
		var spray := CPUParticles2D.new()
		spray.name = "OutfallSpray"
		spray.position = discharge
		spray.texture = load("res://assets/fx/smoke_01.png")
		spray.amount = 7
		spray.lifetime = 2.2
		spray.preprocess = 2.2
		spray.direction = Vector2(.3,1)
		spray.spread = 26
		spray.gravity = Vector2(0,4)
		spray.initial_velocity_min = 4
		spray.initial_velocity_max = 11
		spray.scale_amount_min = .015
		spray.scale_amount_max = .035
		spray.color = Color(.44,.47,.32,.12)
		add(spray,coast)
	# Mooring-service corners use the existing painted crane and repaired grate family.
	sprite("infrastructure/crane.png",Vector2(2155,1640),Vector2(101,151))
	for at in [Vector2(652,1688),Vector2(2185,1662),Vector2(2246,1130)]:
		sprite("terrain/metal_repair.png",at+Vector2(-26,-23),Vector2(91,60),.08)
		sprite("infrastructure/lantern.png",at+Vector2(18,-37),Vector2(25,39))
		stain(at,Vector2(95,58),Color(.63,.35,.10,.14))
	print("COAST: industrial sea, reinforced shores, three service landings and four outfalls")
