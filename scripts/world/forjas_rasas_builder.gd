extends RefCounted
var m
var world: Node2D
var paths: Array[PackedVector2Array]=[]
var waters: Array[PackedVector2Array]=[]
var outline := PackedVector2Array([Vector2(1640,315),Vector2(1770,270),Vector2(2050,315),Vector2(2440,300),Vector2(2820,310),Vector2(3370,280),Vector2(3670,190),Vector2(3750,-190),Vector2(3650,-600),Vector2(3730,-1050),Vector2(3490,-1440),Vector2(3150,-1640),Vector2(2630,-1690),Vector2(2110,-1490),Vector2(1770,-1120),Vector2(1640,-570)])
var drain := PackedVector2Array([Vector2(2260,145),Vector2(2440,125),Vector2(2560,150),Vector2(2680,135),Vector2(2920,180),Vector2(3120,150),Vector2(3340,160),Vector2(3560,120)])
func path_distance(point: Vector2) -> float:
	var distance := INF
	for path in paths:
		for i in range(path.size()-1):distance=minf(distance,point.distance_to(Geometry2D.get_closest_point_to_segment(point,path[i],path[i+1])))
	return distance
func add_route(label: String, points: PackedVector2Array, width: float, parent: Node) -> void:
	paths.append(points);var marker := Marker2D.new();marker.name=label;marker.set_meta("points",points);marker.set_meta("clear_width",width);parent.add_child(marker)
	m.route(points,width,.32 if width>100 else .23)
func building(label: String, point: Vector2, file: String, size: Vector2, machine: bool=false) -> void:
	var node: Node2D=m.group(label,m.commerce);node.position=point
	m.shadow(point,size.x*.91)
	m.art("terrain/foundation.png",point-Vector2(0,12),Vector2(size.x*.94,86),m.detail).modulate=Color(.57,.57,.48,.82)
	var sprite: Sprite2D=m.art(file,Vector2(0,-size.y*.40),size,node)
	if label.begins_with("Oficina"):
		var index := int(label.trim_prefix("Oficina"))
		sprite.modulate=[Color(1,1,1),Color(.90,.94,.89),Color(1,.94,.83)][index%3]
	m.solid(Vector2(0,-28 if not machine else -43),Vector2(size.x*.63,65 if not machine else 78),node)
	m.art("terrain/oil_hatch.png",point+Vector2(size.x*.20,22),Vector2(65,51),m.detail,.11).modulate=Color(.69,.68,.52,.72)
	m.art("generated/props/pipe.png",Vector2(size.x*.34,-7),Vector2(87,28),node,.11)
	m.lamp(point+Vector2(-size.x*.39,23),m.commerce,machine)
	node.set_meta("function",label)
func drain_y(x: float) -> float:
	for i in range(drain.size()-1):
		if x>=drain[i].x and x<=drain[i+1].x:return lerpf(drain[i].y,drain[i+1].y,inverse_lerp(drain[i].x,drain[i+1].x,x))
	return drain[0].y
func drainage() -> void:
	var group: Node2D=m.group("Drainage",m.district,-17)
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/forjas_drain.gdshader");material.set_shader_parameter("grime",load("res://assets/infrastructure/channel.png"))
	var samples := PackedVector2Array()
	for interval in [Vector2(2260,2580),Vector2(2660,3240),Vector2(3320,3560)]:
		var mid := PackedVector2Array([Vector2(interval.x,drain_y(interval.x))])
		for at in drain:
			if at.x>interval.x and at.x<interval.y:mid.append(at)
		mid.append(Vector2(interval.y,drain_y(interval.y)))
		var polygon := PackedVector2Array()
		for at in mid:polygon.append(at-Vector2(0,33))
		for i in range(mid.size()-1,-1,-1):polygon.append(mid[i]+Vector2(0,33))
		waters.append(polygon)
		var water := Polygon2D.new();water.polygon=polygon;water.material=material;group.add_child(water)
		var body := StaticBody2D.new();var shape := CollisionPolygon2D.new();shape.polygon=polygon;body.add_child(shape);group.add_child(body)
		samples.append(Vector2((interval.x+interval.y)/2,drain_y((interval.x+interval.y)/2)))
		for i in range(mid.size()-1):
			var delta := mid[i+1]-mid[i];var count := ceili(delta.length()/91)
			for j in range(count):
				var at := mid[i].lerp(mid[i+1],(j+.5)/count)
				for side in [-1,1]:
					m.art("infrastructure/retaining_edge.png",at+Vector2(0,side*43),Vector2(delta.length()/count+19,45),group,delta.angle()).modulate=Color(.74,.78,.68,1)
	var bridges: Node2D=m.group("Bridges",m.district,-12)
	for x in [2620,3280]:
		var node: Node2D=m.group("Travessia%d"%x,bridges);var y := drain_y(x)
		node.set_meta("approach",Vector2(x,y-95));node.set_meta("departure",Vector2(x,y+95))
		m.art("infrastructure/walkway.png",Vector2(x,y),Vector2(118,174),node)
		m.art("infrastructure/stairs.png",Vector2(x,y+77),Vector2(78,43),node)
		for side in [-1,1]:m.art("infrastructure/retaining_edge.png",Vector2(x+side*47,y),Vector2(125,34),node,PI/2)
		m.lamp(Vector2(x+56,y-74),m.commerce)
	for point in [Vector2(2350,83),Vector2(2860,121),Vector2(3450,90)]:
		m.art("generated/props/pipe.png",point,Vector2(99,31),group,.9)
		m.art("terrain/market_dirt.png",point+Vector2(6,44),Vector2(114,59),group).modulate=Color(.10,.19,.10,.7)
	for end in [drain[0],drain[drain.size()-1]]:
		m.art("infrastructure/coastal_wall.png",end,Vector2(91,55),group,PI/2).modulate=Color(.76,.81,.69,1)
		m.art("generated/props/pipe.png",end+Vector2(-12,0),Vector2(82,35),group,.08)
	m.district.set_meta("water_polygons",waters);m.district.set_meta("water_samples",samples)
func markers(label: String, data: Array) -> void:
	var parent: Node2D=m.group(label,m.district)
	for entry in data:
		var marker := Marker2D.new();marker.name=entry[0];marker.position=entry[1];parent.add_child(marker)
		if label=="FutureExits":marker.set_meta("status","reserved approach only; destination not built")
func install(builder) -> void:
	world=builder.world
	m=load("res://scripts/world/market_expansion_builder.gd").new();m.b=builder
	m.district=m.group("ForjasRasasDistrict",world);m.detail=m.group("GroundIntegration",m.district,-14);m.commerce=m.group("ForjasIndustrialArchitecture",world.get_node("Structures"));m.commerce.y_sort_enabled=true
	var routes: Node2D=m.group("Routes",m.district)
	add_route("ViaDosRebitadores",PackedVector2Array([Vector2(1668,132),Vector2(1900,108),Vector2(2170,-70),Vector2(2470,-120),Vector2(2780,-150),Vector2(3200,-150),Vector2(3550,0)]),132,routes)
	add_route("CircuitoDasFornalhas",PackedVector2Array([Vector2(2170,-70),Vector2(2210,-650),Vector2(2310,-800),Vector2(2700,-800),Vector2(2970,-680),Vector2(3270,-600),Vector2(3550,-630)]),115,routes)
	add_route("CargaDoMercado",PackedVector2Array([Vector2(1416,-756),Vector2(1490,-925),Vector2(1620,-920),Vector2(1800,-1040),Vector2(1990,-1280),Vector2(2310,-1280),Vector2(2420,-1130),Vector2(2700,-800)]),90,routes)
	add_route("PassagemDasCaldeiras",PackedVector2Array([Vector2(2310,-800),Vector2(2310,-1280),Vector2(2870,-1250),Vector2(3100,-1550)]),82,routes)
	add_route("BecoDosReparos",PackedVector2Array([Vector2(2210,-650),Vector2(2150,-340),Vector2(2470,-120)]),75,routes)
	add_route("BecoDaFabricacao",PackedVector2Array([Vector2(2470,-120),Vector2(2800,-610),Vector2(2970,-680)]),82,routes)
	add_route("RotaDaTriagem",PackedVector2Array([Vector2(3270,-600),Vector2(3550,-630),Vector2(3650,-760)]),95,routes)
	add_route("ManutencaoDaDrenagem",PackedVector2Array([Vector2(2470,-120),Vector2(2620,-80),Vector2(2620,260),Vector2(3000,260),Vector2(3280,240),Vector2(3280,-150),Vector2(3200,-150)]),72,routes)
	var floor := TileMapLayer.new();floor.name="ForjasFloor";floor.z_index=-30;floor.tile_set=load("res://assets/terrain/sucateia_terrain.tres")
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/forjas_ground.gdshader");material.set_shader_parameter("outline_points",outline);material.set_shader_parameter("grime",load("res://assets/region/salvage_ground.png"));floor.material=material;m.district.add_child(floor)
	var segments: Array[Vector4]=[]
	for path in paths:
		for i in range(path.size()-1):segments.append(Vector4(path[i].x,path[i].y,path[i+1].x,path[i+1].y))
	material.set_shader_parameter("segment_count",segments.size());while segments.size()<48:segments.append(Vector4.ZERO)
	material.set_shader_parameter("segments",segments)
	for y in range(-37,7):
		for x in range(28,81):
			var cell := Vector2i(x,y);var at := Vector2(x*48+24,y*48+24)
			var occupied := false
			for path in ["Ground/TerraceFloor","MarketDistrict/MarketFloor","AltoLixoDistrict/AltoFloor"]:
				if world.get_node(path).get_cell_source_id(cell)!=-1:occupied=true
			if not occupied and (Geometry2D.is_point_in_polygon(at,outline) or path_distance(at)<86):floor.set_cell(cell,0,Vector2i(posmod(x,16),posmod(y,16)))
	markers("Frontiers",[["EntradaComercial",Vector2(1668,132)],["CargaDoMercado",Vector2(1620,-920)]])
	markers("WorkYards",[["Reparos",Vector2(2150,-340)],["Fabricacao",Vector2(2800,-610)],["Fundicao",Vector2(2700,-800)],["Carga",Vector2(2470,-120)],["Reciclagem",Vector2(3270,-600)]])
	markers("FutureExits",[["ChaminesVelhas",Vector2(3100,-1550)],["GrandeFerrugem",Vector2(3650,-760)],["ManutencaoFundoFerro",Vector2(3000,260)]])
	for i in range(12):
		var points := [Vector2(1900,-140),Vector2(2030,-485),Vector2(2020,-990),Vector2(2175,-1130),Vector2(2450,-315),Vector2(2530,-550),Vector2(2950,-320),Vector2(3330,-480),Vector2(3440,-1090),Vector2(3050,-1380),Vector2(2670,-1380),Vector2(3550,-150)]
		var file := "reconstruction/forjas_boiler_hall.png" if i in [2,4,8,9] else "reconstruction/forjas_workshop.png"
		building("Oficina%02d"%i,points[i],file,Vector2(350+(i%3)*13,255))
	building("GalpaoDeMontagem",Vector2(3090,-430),"reconstruction/forjas_boiler_hall.png",Vector2(370,275))
	building("ReparosDaEntrada",Vector2(1870,-605),"generated/structures/workshop.png",Vector2(275,297))
	building("FundicaoDasCaldeiras",Vector2(2700,-1000),"region/foundry.png",Vector2(470,470))
	building("FornoDeRecuperacao",Vector2(3170,-950),"region/foundry.png",Vector2(340,340))
	for entry in [["PrensaDeTriagem",Vector2(3320,-760),Vector2(285,205)],["PrensaDosRetalhos",Vector2(2440,-945),Vector2(219,156)],["BobinasDeRecuperacao",Vector2(3530,-1200),Vector2(235,166)]]:
		building(entry[0],entry[1],"reconstruction/forjas_recycler.png",entry[2],true)
	# Grouped stock and side-work plots; deterministic offsets avoid a uniform grid.
	var stock: Node2D=m.group("ForjasStockAndService",world.get_node("Structures"));stock.y_sort_enabled=true
	# Aprons and grouped working plots make equipment belong to a yard, leaving the through lanes open.
	for entry in [[Vector2(2095,-205),Vector2(235,113),-.06],[Vector2(2740,-745),Vector2(319,125),.025],[Vector2(3380,-595),Vector2(280,113),-.05],[Vector2(2490,-173),Vector2(303,139),.045]]:
		var at: Vector2=entry[0];var size: Vector2=entry[1]
		m.shadow(at,size.x)
		m.art("reconstruction/alto_residential_landing.png",at,size,m.detail,entry[2]).modulate=Color(.79,.83,.72,1)
		m.art("terrain/metal_repair.png",at+Vector2(-size.x*.40,14),Vector2(91,53),m.detail,.12)
	for point in [Vector2(2390,-30),Vector2(2870,-710),Vector2(3470,-535)]:
		m.art("infrastructure/crane.png",point-Vector2(0,66),Vector2(94,172),stock)
		m.solid(point-Vector2(0,9),Vector2(35,29),stock)
		m.art("infrastructure/scrap.png",point+Vector2(58,13),Vector2(114,53),stock,.05)
	var bins := [Vector2(1940,-310),Vector2(2100,-890),Vector2(2470,-730),Vector2(2600,-280),Vector2(2920,-1080),Vector2(3030,-485),Vector2(3380,-940),Vector2(3500,-360),Vector2(3480,-1370),Vector2(2760,-1530)]
	for i in range(bins.size()):
		var point: Vector2=bins[i]
		if path_distance(point)<90:continue
		m.shadow(point,91);m.art("infrastructure/scrap.png",point,Vector2(107+(i%3)*11,59),stock,.05*(i%3-1));m.solid(point,Vector2(63,27),stock)
		m.art("terrain/metal_repair.png",point+Vector2(-30,22),Vector2(76,53),m.detail,.12).modulate=Color(.72,.70,.58,.8)
	for point in [Vector2(2350,-170),Vector2(2480,-240),Vector2(2860,-60),Vector2(3100,-90),Vector2(3400,-550)]:
		m.art("reconstruction/market_salvage_cart.png",point,Vector2(81,91),stock)
	for i in range(paths.size()):
		var path := paths[i]
		for j in range(1,path.size()-1):
			var at: Vector2=path[j];var delta := (path[j+1]-at).normalized();var side := delta.orthogonal()
			m.art("terrain/metal_repair.png",at+side*32,Vector2(75,41),m.detail,delta.angle()+.04*(j%3-1)).modulate=Color(.75,.73,.56,.60)
			if i<4:m.art("generated/props/pipe.png",at+side*88,Vector2(111,27),m.detail,delta.angle())
	drainage()
	for data in [[PackedVector2Array([Vector2(1710,90),Vector2(2060,-60),Vector2(2510,-140),Vector2(3010,-200),Vector2(3530,-150)]),false],[PackedVector2Array([Vector2(1650,-930),Vector2(1910,-1090),Vector2(2370,-1110),Vector2(2750,-1060),Vector2(3210,-1030)]),true]]:
		var cable := Line2D.new();cable.points=data[0];cable.width=2;cable.default_color=Color("615039");cable.z_index=8;m.district.add_child(cable)
		for at in data[0]:m.lamp(at,m.commerce,data[1])
	# Border service structures follow the contour, interrupted at reserved exits.
	for i in range(5,14):
		var a: Vector2=outline[i];var b: Vector2=outline[i+1];var delta := b-a
		for j in range(ceili(delta.length()/150)):
			var at := a.lerp(b,(j+.5)/ceili(delta.length()/150))
			if path_distance(at)<96:continue
			m.art("infrastructure/retaining_edge.png",at,Vector2(162,53),m.detail,delta.angle()).modulate=Color(.79,.80,.67,.91)
			if j%2==0:m.art("generated/props/pipe.png",at+Vector2(0,-28),Vector2(122,29),m.detail,delta.angle())
	var camera: Camera2D=world.get_node("Structures/Player/Camera");camera.limit_right=4020;camera.limit_top=-2070
	m.district.set_meta("function","repair, fabrication, foundry, recycling and industrial distribution")
	m.district.set_meta("architecture_path",NodePath("../Structures/ForjasIndustrialArchitecture"))
	m.district.set_meta("status","built; pending current physical and visual validation")
	m.district.set_meta("boundary",outline);m.district.set_meta("territory_cells",floor.get_used_cells().size())
	print("FORJAS built: workshops/halls=14 foundries=2 recycling=3 routes=8 bridges=2 cells=",floor.get_used_cells().size())
