extends RefCounted
var m
var plan: Dictionary
var paths: Array[PackedVector2Array]=[]
var outline: PackedVector2Array
var homes: Node2D
func packed(values: Array) -> PackedVector2Array:
	var result := PackedVector2Array()
	for at in values:result.append(Vector2(at[0],at[1]))
	return result
func path_distance(point: Vector2) -> float:
	var distance := INF
	for path in paths:
		for i in range(path.size()-1):distance=minf(distance,point.distance_to(Geometry2D.get_closest_point_to_segment(point,path[i],path[i+1])))
	return distance
func residence(point: Vector2, stack: bool, index: int) -> void:
	var node: Node2D=m.group("Moradia%02d"%index,homes);node.position=point
	m.shadow(point,188)
	m.art("terrain/foundation.png",point-Vector2(0,10),Vector2(205,76),m.detail).modulate=Color(.63,.60,.47,.78)
	m.art("generated/structures/house_stack.png" if stack else "generated/structures/house.png",Vector2(0,-130),Vector2(228,266),node)
	m.solid(Vector2(0,-30),Vector2(146,61),node)
	# Small reused roofs, side tanks and raised landings make each frontage a residential cluster.
	var side := -1.0 if index%2==0 else 1.0
	var addon := point+Vector2(side*98,-6)
	if path_distance(addon)>85:
		m.art("generated/structures/house.png",Vector2(side*99,-53),Vector2(101,119),node).modulate=Color(.92,.89,.77,1)
		m.art("generated/props/pipe.png",Vector2(side*103,13),Vector2(89,25),node,.06*side)
		m.solid(Vector2(side*99,-9),Vector2(48,28),node)
	if index%3==0:
		m.art("infrastructure/walkway.png",point+Vector2(5,7),Vector2(113,49),m.detail,-.04)
		m.art("infrastructure/stairs.png",point+Vector2(4,39),Vector2(63,43),m.detail)
	if index%2==0:m.lamp(point+Vector2(93,17),m.commerce,index%8==0)
	if index%4==0:m.art("terrain/oil_hatch.png",point+Vector2(-76,29),Vector2(58,46),m.detail,.12)
func install(builder) -> void:
	plan=JSON.parse_string(FileAccess.get_file_as_string("res://tools/alto_lixo_spatial_plan.json"))
	m=load("res://scripts/world/market_expansion_builder.gd").new();m.b=builder
	m.district=m.group("AltoLixoDistrict",builder.world)
	m.detail=m.group("GroundIntegration",m.district,-14)
	m.commerce=m.group("UrbanArchitecture",m.district);m.commerce.y_sort_enabled=true
	homes=m.group("Residences",m.commerce)
	# Flat root container allows physical tests and editing to find every residence directly.
	homes.name="Residences";m.commerce.remove_child(homes);m.district.add_child(homes);homes.y_sort_enabled=true
	outline=packed(plan.boundary)
	var route_group: Node2D=m.group("Routes",m.district)
	for route in plan.routes:
		var path := packed(route.points);paths.append(path)
		var marker := Marker2D.new();marker.name=String(route.name).replace(" ","");marker.set_meta("points",path);marker.set_meta("clear_width",route.clear_width);route_group.add_child(marker)
	# Extra built approach to the upper terrace; future exits remain reserved stubs only.
	paths.append(PackedVector2Array([Vector2(-760,-1130),Vector2(-900,-1170)]))
	for entry in plan.future_exits:paths.append(PackedVector2Array([Vector2(entry.from[0],entry.from[1]),Vector2(entry.point[0],entry.point[1])]))
	var floor := TileMapLayer.new();floor.name="AltoFloor";floor.z_index=-30;floor.tile_set=load("res://assets/terrain/sucateia_terrain.tres")
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/alto_ground.gdshader");material.set_shader_parameter("mud",load("res://assets/region/salvage_ground.png"));floor.material=material;m.district.add_child(floor)
	material.set_shader_parameter("outline_points",outline)
	var segments: Array[Vector4]=[]
	for path in paths:
		for i in range(path.size()-1):segments.append(Vector4(path[i].x,path[i].y,path[i+1].x,path[i+1].y))
	material.set_shader_parameter("segment_count",segments.size())
	while segments.size()<40:segments.append(Vector4.ZERO)
	material.set_shader_parameter("segments",segments)
	var market: TileMapLayer=builder.world.get_node("MarketDistrict/MarketFloor")
	for y in range(-34,6):
		for x in range(-32,23):
			var at := Vector2(x*48+24,y*48+24)
			if market.get_cell_source_id(Vector2i(x,y))!=-1:continue
			if Geometry2D.is_point_in_polygon(at,outline) or path_distance(at)<108:
				floor.set_cell(Vector2i(x,y),0,Vector2i(posmod(x,16),posmod(y,16)))
	for i in range(paths.size()):m.route(paths[i],float(plan.routes[i].clear_width) if i<6 else 60.0,.32 if i<3 else .23)
	for data in [["Frontiers",plan.frontiers],["Terraces",plan.terraces],["FutureExits",plan.future_exits]]:
		var parent: Node2D=m.group(data[0],m.district)
		for entry in data[1]:
			var marker := Marker2D.new();marker.name=String(entry.name).replace(" ","").replace("—","");marker.position=Vector2(entry.point[0],entry.point[1]);parent.add_child(marker)
			if data[0]=="Terraces":marker.set_meta("visual_height_m",entry.visual_height_m)
			if data[0]=="FutureExits":marker.set_meta("status","reserved; no scene portal or destination built")
	var stairs: Node2D=m.group("Stairs",m.district)
	for i in range(plan.stairs.size()):
		var entry: Dictionary=plan.stairs[i];var at := Vector2(entry.point[0],entry.point[1])
		var node: Node2D=m.group("Escada%02d"%i,stairs);node.position=at
		var heading := Vector2(0,-1);var nearest := INF
		for path in paths:
			for j in range(path.size()-1):
				var distance := at.distance_to(Geometry2D.get_closest_point_to_segment(at,path[j],path[j+1]))
				if distance<nearest:nearest=distance;heading=(path[j+1]-path[j]).normalized()
		node.rotation=heading.angle()+PI/2
		m.shadow(at,132);m.art("infrastructure/walkway.png",at,Vector2(139,86),m.detail,-.04)
		m.art("infrastructure/stairs.png",Vector2.ZERO,Vector2(102,76),node)
		m.art("terrain/foundation.png",at+heading*38,Vector2(170,101),m.detail).modulate=Color(.65,.61,.48,.8)
		var cross := heading.orthogonal()
		for side in [-1,1]:
			var bank: Vector2=at+cross*108*side+heading*11
			m.art("infrastructure/retaining_edge.png",bank,Vector2(96,64),m.detail)
			m.solid(bank,Vector2(44,38),m.commerce)
		# Walkable visual steps span the path, without fake height teleportation.
		node.set_meta("levels",entry.levels);node.set_meta("approach",at-heading*30);node.set_meta("departure",at+heading*30)
	# Asymmetric manually authored blocks; positions near a circulation line are shifted away.
	var candidates := PackedVector2Array([Vector2(330,-265),Vector2(245,-790),Vector2(450,-1020),Vector2(205,-1130),Vector2(62,-372),Vector2(-150,-462),Vector2(-350,-225),Vector2(-520,-125),Vector2(-795,-95),Vector2(-1085,-155),Vector2(-1210,-340),Vector2(-960,-460),Vector2(-685,-455),Vector2(-565,-620),Vector2(-755,-735),Vector2(-1020,-770),Vector2(-1235,-925),Vector2(-1090,-1080),Vector2(-960,-1270),Vector2(-690,-1300),Vector2(-400,-1330),Vector2(-180,-1210),Vector2(-190,-900),Vector2(200,-170),Vector2(-445,-995),Vector2(-890,-1010),Vector2(-1160,-570),Vector2(310,20),Vector2(-440,75),Vector2(-1260,-540),Vector2(-1120,-300),Vector2(-860,-220),Vector2(-620,-240),Vector2(-100,-200),Vector2(80,40),Vector2(-1250,-720),Vector2(-1090,-1210),Vector2(-380,-1170),Vector2(360,-410),Vector2(40,-1120),Vector2(-420,-470),Vector2(40,-770)])
	var placed: Array[Vector2]=[]
	# Additional street-front plots follow the irregular circulation, with staggered setbacks.
	for path_index in range(6):
		var path := paths[path_index]
		for j in range(path.size()-1):
			var delta := path[j+1]-path[j];var count := maxi(1,floori(delta.length()/190))
			for k in range(count):
				var center := path[j].lerp(path[j+1],(k+.5)/count)
				if center.x>350:continue
				for side in [-1,1]:candidates.append(center+delta.normalized().orthogonal()*(167+posmod(j*37+path_index*23,51))*side)
	for candidate in candidates:
		var chosen := candidate
		var clear := false
		for offset in [Vector2.ZERO,Vector2(0,48),Vector2(0,-48),Vector2(48,0),Vector2(-48,0),Vector2(0,96),Vector2(0,-96),Vector2(96,0),Vector2(-96,0)]:
			var point: Vector2=candidate+offset
			if not Geometry2D.is_point_in_polygon(point,outline) or path_distance(point-Vector2(0,30))<128:continue
			if point.distance_to(Vector2(-650,-965))<160:continue
			var separated := true
			for other in placed:
				if absf(point.x-other.x)<155 and absf(point.y-other.y)<183:separated=false
			if separated:chosen=point;clear=true;break
		if clear:residence(chosen,placed.size()%3!=0,placed.size());placed.append(chosen)
	# Functional upper courtyard landmark, used only here; no substitution of approved assets.
	var cistern: Node2D=m.group("CisternaComunitaria",homes);cistern.position=Vector2(-650,-965)
	m.shadow(cistern.position,206);m.art("terrain/foundation.png",cistern.position+Vector2(0,7),Vector2(235,101),m.detail).modulate=Color(.66,.62,.49,.9);m.art("reconstruction/alto_cistern.png",Vector2(0,-97),Vector2(233,217),cistern);m.solid(Vector2(0,-30),Vector2(139,54),cistern)
	m.art("terrain/oil_hatch.png",cistern.position+Vector2(70,28),Vector2(109,62),m.detail).modulate=Color(.54,.65,.57,.75)
	m.lamp(Vector2(-531,-948),m.commerce,true)
	# Short retaining walls describe terrace fronts; leave the circulation and stairs open.
	for at in [Vector2(-300,-780),Vector2(-660,-650),Vector2(-1100,-950),Vector2(-1030,-1190),Vector2(195,-760),Vector2(-510,-1330)]:
		if path_distance(at)<80:continue
		m.shadow(at,130);m.art("infrastructure/retaining_edge.png",at,Vector2(161,77),m.detail,.04)
		m.art("generated/props/pipe.png",at+Vector2(43,27),Vector2(110,29),m.detail,.12)
	# A high maintenance gallery links the upper residences, beside the ground-level loop.
	for entry in [[Vector2(-975,-1210),Vector2(148,62)],[Vector2(-845,-1250),Vector2(146,62)],[Vector2(-730,-1290),Vector2(121,62)]]:
		m.shadow(entry[0],130);m.art("infrastructure/walkway.png",entry[0],entry[1],m.detail,-.13)
	for points in [PackedVector2Array([Vector2(729,-941),Vector2(205,-1130),Vector2(-400,-1330),Vector2(-960,-1270)]),PackedVector2Array([Vector2(613,-621),Vector2(245,-790),Vector2(-190,-900),Vector2(-650,-965),Vector2(-1090,-1080)]),PackedVector2Array([Vector2(565,277),Vector2(310,20),Vector2(-350,-225),Vector2(-1085,-155)])]:
		var cable := Line2D.new();cable.points=points;cable.width=2;cable.default_color=Color("5a4936");cable.z_index=8;m.district.add_child(cable)
	for at in [Vector2(315,-485),Vector2(95,-570),Vector2(-145,-625),Vector2(-445,-685),Vector2(-555,-1120),Vector2(-1020,-1140),Vector2(-870,-440),Vector2(-545,-190)]:
		m.art("generated/props/pipe.png",at,Vector2(107,28),m.detail,.17)
		m.art("terrain/oil_hatch.png",at+Vector2(22,20),Vector2(67,46),m.detail,-.1).modulate=Color(.81,.78,.63,.73)
	# Reserved external stubs end in the built terrain, with no invented destination.
	for entry in plan.future_exits:
		var from := Vector2(entry.from[0],entry.from[1]);var to := Vector2(entry.point[0],entry.point[1])
		m.route(PackedVector2Array([from,to]),58,.16)
	for at in [Vector2(-1350,-490),Vector2(-1135,-1410),Vector2(-850,75)]:
		m.art("infrastructure/scrap.png",at,Vector2(115,59),m.commerce,-.05)
	# Terrain fringe: irregular alpha, lower than the playable floor, not a rectangular district frame.
	var fringe := Polygon2D.new();fringe.z_index=-34;fringe.polygon=PackedVector2Array([Vector2(-1730,-1670),Vector2(1050,-1670),Vector2(1050,360),Vector2(-1730,360)])
	var edge_material := ShaderMaterial.new();edge_material.shader=load("res://assets/reconstruction/alto_fringe.gdshader");edge_material.set_shader_parameter("outline_points",outline);edge_material.set_shader_parameter("mud",load("res://assets/region/salvage_ground.png"));fringe.material=edge_material;m.district.add_child(fringe)
	for at in [Vector2(-1130,-90),Vector2(-975,15),Vector2(-790,104),Vector2(-610,130),Vector2(-420,115),Vector2(-190,92),Vector2(-1380,-410),Vector2(-1358,-760)]:
		m.shadow(at,141);m.art("infrastructure/coastal_wall.png",at,Vector2(180,95),m.detail,.05)
		m.art("infrastructure/scrap.png",at+Vector2(57,7),Vector2(74,40),m.detail,-.08)
	var camera: Camera2D=builder.world.get_node("Structures/Player/Camera");camera.limit_left=-1680
	m.district.set_meta("direction","west/northwest");m.district.set_meta("residence_count",placed.size());m.district.set_meta("elevation","visual terraces; no multilayer traversal implemented");m.district.set_meta("status","built; pending physical and visual verification")
	print("ALTO built western floor cells=",floor.get_used_cells().size()," residences=",placed.size())
