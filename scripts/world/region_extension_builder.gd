extends RefCounted
var b
var rooms: Array[Rect2] = []
func floor_cell(cell: Vector2i) -> bool:
	var point := Vector2(cell)*48+Vector2(24,24)
	for room in rooms:
		if room.has_point(point): return true
	return false
func gallery_floor(builder) -> void:
	b = builder
	for entry in b.config.rooms: rooms.append(Rect2(entry[0],entry[1],entry[2],entry[3]))
	var back := Polygon2D.new()
	back.polygon = PackedVector2Array([Vector2(-500,-400),Vector2(2600,-400),Vector2(2600,2100),Vector2(-500,2100)])
	back.z_index = -40
	var mat := ShaderMaterial.new()
	mat.shader = load("res://assets/region/interior.gdshader")
	mat.set_shader_parameter("stone",load("res://assets/terrain/floor_atlas.png"))
	back.material = mat
	b.add(back,b.world)
	var floor_layer := TileMapLayer.new()
	floor_layer.name = "DistrictFloor"
	floor_layer.z_index = -30
	floor_layer.tile_set = load("res://assets/terrain/sucateia_terrain.tres")
	var floor_mat := ShaderMaterial.new()
	floor_mat.shader = load("res://assets/region/ground.gdshader")
	floor_mat.set_shader_parameter("district_tint",Color("607b78"))
	floor_layer.material = floor_mat
	b.add(floor_layer,b.world)
	# Blocked runs exactly match the cutaway rock around the room/corridor union.
	for y in range(32):
		var start := -1
		for x in range(45):
			var walk: bool = x<44 and floor_cell(Vector2i(x,y))
			if walk:
				floor_layer.set_cell(Vector2i(x,y),0,Vector2i(x%16,y%16))
			if not walk and x<44 and start == -1: start = x
			if (walk or x==44) and start!=-1:
				b.solid(Vector2((start+x)*24,(y+.5)*48),Vector2((x-start)*48,48),b.world)
				start = -1
	# Paint all exposed room boundaries, merging short edges into modules.
	for y in range(32):
		for direction in [-1,1]:
			var start := -1
			for x in range(45):
				var boundary: bool = x<44 and floor_cell(Vector2i(x,y)) and not floor_cell(Vector2i(x,y+direction))
				if boundary and start==-1: start=x
				if (not boundary or x==44) and start!=-1:
					wall(Vector2(start*48,(y+(1 if direction==1 else 0))*48),Vector2(x*48,(y+(1 if direction==1 else 0))*48))
					start=-1
	for x in range(44):
		for direction in [-1,1]:
			var start := -1
			for y in range(33):
				var boundary: bool = y<32 and floor_cell(Vector2i(x,y)) and not floor_cell(Vector2i(x+direction,y))
				if boundary and start==-1: start=y
				if (not boundary or y==32) and start!=-1:
					wall(Vector2((x+(1 if direction==1 else 0))*48,start*48),Vector2((x+(1 if direction==1 else 0))*48,y*48))
					start=-1
func wall(a: Vector2, end: Vector2) -> void:
	var delta := end-a
	var count := maxi(1,ceili(delta.length()/151.0))
	for j in range(count):
		var at := a.lerp(end,(j+.5)/count)
		b.shadow(at+Vector2(6,16),Vector2(122,79),.69)
		var sprite: Sprite2D = b.art("infrastructure/retaining_edge.png",at,Vector2(delta.length()/count+11,71),null,delta.angle())
		sprite.modulate = Color(.63,.77,.71)
func install(builder) -> void:
	b = builder
	if b.id in ["eng_nucleo","eng_corredor"]: return
	var style: String = b.config.style
	if style == "gallery":
		for at in [Vector2(365,1160),Vector2(650,1025),Vector2(1060,830),Vector2(1250,570),Vector2(1490,1030),Vector2(355,475)]:
			b.art("terrain/market_dirt.png",at,Vector2(188,93),null,.13).modulate = Color(.62,.7,.61,.47)
		b.pipe_route(PackedVector2Array([Vector2(1100,1008),Vector2(913,1008),Vector2(913,725),Vector2(833,725),Vector2(833,558),Vector2(370,558)]))
		b.pipe_route(PackedVector2Array([Vector2(1160,1010),Vector2(1290,936),Vector2(1430,936),Vector2(1430,1160),Vector2(1550,1160)]))
		b.pipe_route(PackedVector2Array([Vector2(1470,520),Vector2(1600,520),Vector2(1600,827),Vector2(1550,827),Vector2(1550,1130)]))
		for at in [Vector2(350,720),Vector2(795,605),Vector2(1267,799),Vector2(1570,685)]:
			b.art("infrastructure/service_arch.png",at,Vector2(113,92))
			b.art("infrastructure/stairs.png",at+Vector2(0,32),Vector2(74,63))
		for at in [Vector2(1000,916),Vector2(350,430),Vector2(1510,1030),Vector2(1250,440)]:
			b.art("terrain/oil_hatch.png",at,Vector2(89,75),null,.065)
			b.light(at,Color("62a4a4"),1.05)
		for at in [Vector2(450,1130),Vector2(865,843),Vector2(1440,845)]:
			b.art("infrastructure/lantern.png",at,Vector2(25,39))
			b.light(at,Color("b28d54"),.6)
		b.art("infrastructure/walkway.png",Vector2(850,1020),Vector2(223,127))
	elif style == "precision":
		b.pipe_route(PackedVector2Array([Vector2(475,714),Vector2(630,714),Vector2(630,810),Vector2(880,810)]))
		b.cable(PackedVector2Array([Vector2(980,734),Vector2(1050,892),Vector2(1370,940),Vector2(1470,1058)]),b.floor_details)
		for at in [Vector2(720,975),Vector2(980,964),Vector2(1220,936)]:
			b.art("terrain/metal_repair.png",at,Vector2(148,95),null,.03)
			b.art("infrastructure/walkway.png",at+Vector2(0,65),Vector2(93,59))
		b.light(Vector2(970,550),Color("78b9b4"),1.8)
		b.light(Vector2(1470,950),Color("caa45a"),.9)
		b.art("infrastructure/crane.png",Vector2(775,820),Vector2(98,146))
	elif style == "coastal_path":
		for at in [Vector2(360,1100),Vector2(850,940),Vector2(1510,724)]:
			b.art("infrastructure/walkway.png",at,Vector2(154,120),null,.08)
			b.art("terrain/metal_repair.png",at+Vector2(55,30),Vector2(68,47),null,-.1)
			b.light(at,Color("89aca3"),.9)
		b.art("infrastructure/crane.png",Vector2(1390,810),Vector2(113,167))
		b.art("region/cargo_barge.png",Vector2(1220,1135),Vector2(465,225),null,-.09)
		b.cable(PackedVector2Array([Vector2(373,995),Vector2(679,832),Vector2(900,805),Vector2(1200,653)]))
	elif style == "wreck_bank":
		for at in [Vector2(870,725),Vector2(950,913),Vector2(1240,904)]:
			b.art("terrain/metal_repair.png",at,Vector2(173,92),null,-.05)
		b.pipe_route(PackedVector2Array([Vector2(1315,875),Vector2(1390,875),Vector2(1390,962)]))
		for at in [Vector2(590,885),Vector2(1460,1070),Vector2(1150,1200)]:
			b.art("infrastructure/scrap.png",at,Vector2(201,109),null,.12)
			b.art("infrastructure/walkway.png",at+Vector2(-73,30),Vector2(134,80),null,-.08)
		b.art("region/cargo_barge.png",Vector2(715,410),Vector2(390,194),null,.15)
		b.art("infrastructure/crane.png",Vector2(1440,870),Vector2(119,181))
		b.art("terrain/metal_repair.png",Vector2(1050,1020),Vector2(194,110),null,-.08)
		b.light(Vector2(1220,749),Color("859f9b"),1)
	elif style == "freight_path":
		for at in [Vector2(450,1010),Vector2(900,906),Vector2(1420,836)]:
			b.art("terrain/metal_repair.png",at,Vector2(135,79),null,-.11)
			b.art("infrastructure/lantern.png",at+Vector2(12,-28),Vector2(25,39))
			b.light(at,Color("c6a16d"),.6)
		b.art("infrastructure/scrap.png",Vector2(480,1170),Vector2(144,79))
		b.pipe_route(PackedVector2Array([Vector2(1400,740),Vector2(1520,740),Vector2(1520,815)]))
		b.art("infrastructure/walkway.png",Vector2(1650,662),Vector2(170,113),null,.13)
func existing_details(builder) -> void:
	b = builder
	refinement_details()
	if b.id == "docas":
		b.art("region/cargo_barge.png",Vector2(1320,1250),Vector2(435,210),null,-.05)
		b.art("region/cargo_barge.png",Vector2(575,1230),Vector2(405,196),null,.07)
		for at in [Vector2(755,568),Vector2(1120,490),Vector2(1540,784)]:
			b.art("infrastructure/walkway.png",at,Vector2(188,139),null,.06)
			b.art("infrastructure/scrap.png",at+Vector2(42,17),Vector2(118,63),null,-.1)
			b.art("terrain/metal_repair.png",at+Vector2(-35,55),Vector2(79,53))
		b.cable(PackedVector2Array([Vector2(540,730),Vector2(845,867),Vector2(1220,789),Vector2(1370,704)]),b.floor_details)
	if b.id == "fundo":
		for x in [330,500,670,1370,1540,1710]:
			b.art("infrastructure/retaining_edge.png",Vector2(x,633),Vector2(181,89))
		b.art("infrastructure/stairs.png",Vector2(970,654),Vector2(155,120))
		b.art("terrain/oil_hatch.png",Vector2(1000,968),Vector2(139,113))
		b.pipe_route(PackedVector2Array([Vector2(1200,782),Vector2(1200,900),Vector2(1060,900)]))
	if b.id == "chamines":
		for at in [Vector2(1470,395),Vector2(1570,329),Vector2(590,500)]:
			var smoke := CPUParticles2D.new()
			smoke.position = at
			smoke.texture = load("res://assets/fx/smoke_01.png")
			smoke.amount = 9
			smoke.lifetime = 5
			smoke.preprocess = 4
			smoke.direction = Vector2(-.2,-1)
			smoke.gravity = Vector2(-1,-3)
			smoke.initial_velocity_min = 8
			smoke.initial_velocity_max = 15
			smoke.scale_amount_min = .035
			smoke.scale_amount_max = .10
			smoke.color = Color(.35,.38,.32,.2)
			b.add(smoke,b.upper)
func worn_route(points: PackedVector2Array, width: float = 98) -> void:
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i]
		var count := maxi(1,ceili(delta.length()/110.0))
		for j in range(count):
			var at := points[i].lerp(points[i+1],(j+.5)/count)
			var outline := PackedVector2Array()
			for point in b.config.outline: outline.append(Vector2(point[0],point[1]))
			var fits := true
			for corner in [Vector2(-70,-width*.5),Vector2(70,-width*.5),Vector2(-70,width*.5),Vector2(70,width*.5)]:
				if not Geometry2D.is_point_in_polygon(at+corner.rotated(delta.angle()),outline): fits = false
			if not fits: continue
			var stamp: Sprite2D = b.art("terrain/market_dirt.png",at,Vector2(139,width),null,delta.angle())
			stamp.modulate = Color(.87,.83,.7,.24)
func workpad(at: Vector2, size: Vector2, angle: float = 0) -> void:
	b.art("terrain/metal_repair.png",at,size,null,angle)
	b.art("infrastructure/walkway.png",at+Vector2(size.x*.35,9),size*Vector2(.44,.73),null,angle+.04)
	b.shadow(at+Vector2(12,15),size*.8,.24)
func refinement_details() -> void:
	if b.id == "eng_nucleo":
		worn_route(PackedVector2Array([Vector2(1000,1170),Vector2(1070,1020),Vector2(1230,905),Vector2(1250,690),Vector2(910,690),Vector2(485,690),Vector2(485,995)]),83)
		worn_route(PackedVector2Array([Vector2(1230,905),Vector2(1715,890)]),75)
		b.cable(PackedVector2Array([Vector2(410,410),Vector2(740,440),Vector2(1150,360),Vector2(1560,410)]))
		b.pipe_route(PackedVector2Array([Vector2(1450,1000),Vector2(1450,1060),Vector2(1190,1060),Vector2(1190,865)]))
		for at in [Vector2(600,650),Vector2(1250,750),Vector2(1020,1030),Vector2(1510,1100)]:
			b.art("infrastructure/lantern.png",at,Vector2(29,46))
			b.light(at,Color("c7a56e"),.8)
		workpad(Vector2(950,905),Vector2(191,107),-.04)
		workpad(Vector2(750,1210),Vector2(157,79),.08)
		b.art("infrastructure/stairs.png",Vector2(1650,633),Vector2(86,69))
		b.art("infrastructure/scrap.png",Vector2(780,840),Vector2(90,54))
	elif b.id == "eng_corredor":
		worn_route(PackedVector2Array([Vector2(330,1080),Vector2(820,1110),Vector2(1110,990),Vector2(1460,845),Vector2(1700,535)]),110)
		b.pipe_route(PackedVector2Array([Vector2(900,720),Vector2(1010,720),Vector2(1010,845),Vector2(1420,845),Vector2(1420,760),Vector2(1610,760)]))
		b.cable(PackedVector2Array([Vector2(690,985),Vector2(970,860),Vector2(1290,590),Vector2(1620,690)]))
		workpad(Vector2(1170,940),Vector2(245,143),-.06)
		workpad(Vector2(685,1040),Vector2(226,111),.03)
		for at in [Vector2(520,1120),Vector2(960,1000),Vector2(1480,910)]:
			b.art("infrastructure/lantern.png",at,Vector2(28,45))
			b.light(at,Color("74aaa4"),.9)
	elif b.id == "engrenopolis":
		worn_route(PackedVector2Array([Vector2(770,355),Vector2(750,490),Vector2(585,775),Vector2(710,880),Vector2(1040,1000),Vector2(1680,1130),Vector2(1750,860)]))
		workpad(Vector2(1135,1135),Vector2(180,99),.04)
		b.cable(PackedVector2Array([Vector2(630,390),Vector2(810,442),Vector2(980,585)]))
	elif b.id == "banco":
		worn_route(PackedVector2Array([Vector2(270,1120),Vector2(700,1150),Vector2(910,1060),Vector2(1200,920),Vector2(1500,730),Vector2(1550,525),Vector2(1720,460)]),119)
		workpad(Vector2(1180,860),Vector2(420,162),.03)
		workpad(Vector2(600,1110),Vector2(232,119),-.05)
		workpad(Vector2(1570,1170),Vector2(189,113),.06)
		b.art("infrastructure/crane.png",Vector2(1070,540),Vector2(142,214))
		b.art("infrastructure/walkway.png",Vector2(1110,480),Vector2(200,170),null,-.42)
		b.art("region/wreck_cradle.png",Vector2(1490,455),Vector2(370,215),null,.12)
		b.cable(PackedVector2Array([Vector2(1190,780),Vector2(1230,694),Vector2(1070,540)]))
	elif b.id == "docas":
		worn_route(PackedVector2Array([Vector2(950,300),Vector2(920,530),Vector2(750,670),Vector2(840,870),Vector2(1070,1050),Vector2(1380,1140),Vector2(1600,1200)]),120)
		worn_route(PackedVector2Array([Vector2(920,530),Vector2(1400,550),Vector2(1640,695)]),90)
		workpad(Vector2(695,445),Vector2(225,115),-.04)
		workpad(Vector2(1425,475),Vector2(213,112),.07)
		workpad(Vector2(1110,1010),Vector2(192,95),-.08)
	elif b.id == "fundo":
		worn_route(PackedVector2Array([Vector2(420,370),Vector2(700,525),Vector2(970,654),Vector2(1000,990),Vector2(1000,1160)]),90)
		worn_route(PackedVector2Array([Vector2(1620,380),Vector2(1500,640),Vector2(1300,850),Vector2(1050,965)]),85)
		for entry in [[Vector2(340,740),Vector2(180,85)],[Vector2(565,765),Vector2(175,85)],[Vector2(745,815),Vector2(175,85)]]:
			var at: Vector2 = entry[0]
			var size: Vector2 = entry[1]
			b.art("infrastructure/channel.png",at,size,null,.08)
			b.solid(at,Vector2(size.x*.78,29),b.world,.08)
			b.art("infrastructure/retaining_edge.png",at+Vector2(0,30),Vector2(size.x,49),null,.08)
		b.art("infrastructure/walkway.png",Vector2(470,790),Vector2(100,143),null,.09)
		b.pipe_route(PackedVector2Array([Vector2(530,525),Vector2(530,690),Vector2(350,690),Vector2(350,730)]))
		b.pipe_route(PackedVector2Array([Vector2(1550,545),Vector2(1450,545),Vector2(1450,640),Vector2(1210,720)]))
		for at in [Vector2(400,775),Vector2(565,800),Vector2(790,850)]:
			b.art("terrain/oil_hatch.png",at,Vector2(105,79),null,.10).modulate=Color(.47,.65,.52,.7)
