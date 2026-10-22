extends RefCounted
var b
func portal(builder, destination: String, at: Vector2) -> void:
	b = builder
	var n := Area2D.new()
	n.name = "To_"+destination
	n.position = at
	n.collision_layer = 0
	n.collision_mask = 2
	n.set_script(load("res://scripts/world/region_portal.gd"))
	n.set("destination",destination)
	n.set_meta("destination",destination)
	b.add(n,b.world.get_node("RegionPortals"))
	var collision := CollisionShape2D.new()
	var circle := CircleShape2D.new()
	circle.radius = 78
	collision.shape = circle
	b.add(collision,n)
	b.art("vhal/stone_quay.png",Vector2(0,-24),Vector2(195,116),n)
	b.art("vhal/river_crossing.png",Vector2(0,-37),Vector2(170,113),n)
	var prompt := Label.new()
	prompt.name = "Prompt"
	prompt.position = Vector2(-90,25)
	prompt.text = "E — "+str(b.catalog[destination].name)
	prompt.visible = false
	prompt.add_theme_font_size_override("font_size",14)
	b.add(prompt,n)
	var sign := Label.new()
	sign.name = "Sign"
	sign.text = str(b.catalog[destination].name).split(" — ")[0]
	sign.position = Vector2(-78,-100)
	sign.add_theme_font_size_override("font_size",11)
	sign.add_theme_color_override("font_color",Color("c3b996"))
	b.add(sign,n)
func route(points: PackedVector2Array, width: float = 85) -> void:
	var outline := PackedVector2Array()
	for point in b.config.outline: outline.append(Vector2(point[0],point[1]))
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i]
		var count := maxi(1,ceili(delta.length()/110.0))
		for j in range(count):
			var at := points[i].lerp(points[i+1],(j+.5)/count)
			var fits := true
			for corner in [Vector2(-65,-width*.5),Vector2(65,-width*.5),Vector2(-65,width*.5),Vector2(65,width*.5)]:
				var point := at+corner.rotated(delta.angle())
				if not Geometry2D.is_point_in_polygon(point,outline): fits = false
				if b.id == "river_route" and Rect2(912,432,192,576).has_point(point) and not Rect2(912,720,192,48).has_point(point): fits = false
			if not fits: continue
			b.art("terrain/market_dirt.png",at,Vector2(132,width),null,delta.angle()).modulate = Color(.57,.65,.59,.23)
func quay(at: Vector2, size: Vector2) -> void:
	b.art("vhal/stone_quay.png",at,size)
	b.shadow(at+Vector2(0,26),size*Vector2(1,.4),.45)
func details(builder) -> void:
	b = builder
	for entry in b.config.buildings:
		var at := Vector2(entry[1],entry[2])
		b.light(at+Vector2(0,-50),Color("b9a475"),.6)
		if entry[0] == "arcane_station": b.light(at+Vector2(0,-125),Color("72bec6"),1.2)
	if b.id == "north_expedition":
		route(PackedVector2Array([Vector2(290,1100),Vector2(780,990),Vector2(1050,830),Vector2(1470,650),Vector2(1690,410)]),110)
		b.art("infrastructure/walkway.png",Vector2(660,1110),Vector2(184,111))
		b.pipe_route(PackedVector2Array([Vector2(620,765),Vector2(770,765),Vector2(770,905)]))
		b.art("infrastructure/scrap.png",Vector2(490,850),Vector2(144,83))
		quay(Vector2(1410,645),Vector2(223,139))
	elif b.id == "river_route":
		var floor_layer: TileMapLayer = b.world.get_node("DistrictFloor")
		for y in range(9,21):
			for x in range(19,23):
				if y != 15: floor_layer.erase_cell(Vector2i(x,y))
		b.solid(Vector2(1008,576),Vector2(192,288),b.world)
		b.solid(Vector2(1008,888),Vector2(192,240),b.world)
		b.art("vhal/river_crossing.png",Vector2(1030,760),Vector2(485,280))
		route(PackedVector2Array([Vector2(285,1080),Vector2(735,950),Vector2(825,795),Vector2(1060,744),Vector2(1210,720),Vector2(1460,390)]),73)
		quay(Vector2(800,815),Vector2(152,117))
		b.art("region/cargo_barge.png",Vector2(1020,1110),Vector2(375,175),null,-.10)
	elif b.id == "caelporto":
		route(PackedVector2Array([Vector2(300,1050),Vector2(790,865),Vector2(1010,900),Vector2(1220,895),Vector2(1700,650)]),120)
		route(PackedVector2Array([Vector2(1010,900),Vector2(850,635),Vector2(1000,300)]),105)
		for at in [Vector2(400,1190),Vector2(1000,1300),Vector2(1560,1250)]:
			quay(at,Vector2(180,138))
		b.art("region/cargo_barge.png",Vector2(690,1230),Vector2(340,157),null,.03)
		b.art("region/cargo_barge.png",Vector2(1260,1280),Vector2(370,165),null,-.04)
		b.cable(PackedVector2Array([Vector2(1090,650),Vector2(1240,722),Vector2(1430,725)]))
	elif b.id == "vhal_lower":
		route(PackedVector2Array([Vector2(1010,1210),Vector2(1030,1020),Vector2(760,850),Vector2(725,690),Vector2(1420,645),Vector2(1760,890)]),95)
		route(PackedVector2Array([Vector2(760,850),Vector2(270,1030)]),75)
		b.art("vhal/river_crossing.png",Vector2(1175,615),Vector2(430,185),b.upper)
		b.cable(PackedVector2Array([Vector2(400,420),Vector2(960,584),Vector2(1650,430)]))
		b.cable(PackedVector2Array([Vector2(950,730),Vector2(730,810),Vector2(760,1075)]),b.floor_details)
		for at in [Vector2(730,785),Vector2(1100,1050),Vector2(1570,840)]:
			b.art("vhal/stone_quay.png",at,Vector2(114,79)).modulate=Color(.78,.85,.88)
			b.light(at,Color("99a8b3"),.55)
	elif b.id == "twin_plaza":
		route(PackedVector2Array([Vector2(320,1110),Vector2(780,1180),Vector2(1030,1080),Vector2(1400,1190),Vector2(1720,1110)]),120)
		quay(Vector2(1030,1105),Vector2(318,161))
		b.cable(PackedVector2Array([Vector2(585,980),Vector2(780,1020),Vector2(1010,835)]))
		b.light(Vector2(1030,855),Color("82bbd0"),2)
		b.light(Vector2(585,950),Color("73a7bd"),1)
	if b.id in ["vhal_lower","twin_plaza"]:
		# Urban masses beyond the playable frontage prevent a detached courtyard silhouette.
		for at in [Vector2(360,210),Vector2(1050,200),Vector2(1690,220)]:
			var distant: Sprite2D = b.art("vhal/gothic_block.png",at,Vector2(590,430),b.upper)
			distant.z_as_relative = false
			distant.z_index = -35
			distant.modulate = Color(.45,.55,.61,.64)
