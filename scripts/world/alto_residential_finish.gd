extends RefCounted
var m
var paths: Array[PackedVector2Array]=[]
func distance(point: Vector2) -> float:
	var result := INF
	for path in paths:
		for i in range(path.size()-1):result=minf(result,point.distance_to(Geometry2D.get_closest_point_to_segment(point,path[i],path[i+1])))
	return result
func packed(values: Array) -> PackedVector2Array:
	var result := PackedVector2Array()
	for point in values:result.append(Vector2(point[0],point[1]))
	return result
func install(builder) -> void:
	var world: Node2D=builder.world
	var district: Node2D=world.get_node("AltoLixoDistrict")
	m=load("res://scripts/world/market_expansion_builder.gd").new();m.b=builder;m.district=district;m.detail=district.get_node("GroundIntegration");m.commerce=district.get_node("UrbanArchitecture")
	var finish: Node2D=m.group("ResidentialFinish",district)
	var floors: TileMapLayer=district.get_node("AltoFloor")
	var homes: Node2D=district.get_node("Residences")
	var plan: Dictionary=JSON.parse_string(FileAccess.get_file_as_string("res://tools/alto_lixo_spatial_plan.json"))
	for route in district.get_node("Routes").get_children():paths.append(route.get_meta("points"))
	paths.append(PackedVector2Array([Vector2(-760,-1130),Vector2(-900,-1170)]))
	for exit_ in plan.future_exits:paths.append(PackedVector2Array([Vector2(exit_.from[0],exit_.from[1]),Vector2(exit_.point[0],exit_.point[1])]))
	var plots: Array[Vector2]=[]
	for home in homes.get_children():plots.append(home.position)
	var candidates := PackedVector2Array([Vector2(-360,-650),Vector2(-480,-420),Vector2(-615,-205),Vector2(-930,-245),Vector2(-1040,-710),Vector2(-350,-1125),Vector2(5,-770),Vector2(80,-1140)])
	for index in range(6):
		var path := paths[index]
		for j in range(path.size()-1):
			var delta := path[j+1]-path[j];var count := maxi(1,ceili(delta.length()/160))
			for k in range(count):
				var center := path[j].lerp(path[j+1],(k+.5)/count)
				if center.x>300:continue
				for side in [-1,1]:candidates.append(center+delta.normalized().orthogonal()*(163+posmod(j*29+index*19,54))*side)
	var housing_script: Script=load("res://scripts/world/alto_lixo_builder.gd")
	if not housing_script.can_instantiate():push_error("Residential helper failed validation");return
	var housing=housing_script.new();housing.m=m;housing.paths=paths;housing.homes=homes
	var extra := 0;var outline := packed(plan.boundary)
	for candidate in candidates:
		if extra>=12:break
		for offset in [Vector2.ZERO,Vector2(0,40),Vector2(0,-40),Vector2(40,0),Vector2(-40,0)]:
			var at: Vector2=candidate+offset
			if not Geometry2D.is_point_in_polygon(at,outline) or at.x>380 or floors.get_cell_source_id(floors.local_to_map(at))==-1:continue
			if distance(at-Vector2(0,30))<128 or at.distance_to(Vector2(-650,-965))<175:continue
			var free_plot := true
			for other in plots:
				# Tighter staggered rows overlap their roofs but leave 79 px between physical frontages.
				if absf(at.x-other.x)<155 and absf(at.y-other.y)<140:free_plot=false
			if not free_plot:continue
			housing.residence(at,extra%4!=0,22+extra);plots.append(at);extra+=1;break
	# Four distinct communal landings reinforce the progression from market threshold to upper residences.
	var landings: Node2D=m.group("TerraceLandings",finish)
	for data in [["Soleira",Vector2(310,-577),Vector2(237,137)],["Remendos",Vector2(-100,-717),Vector2(251,145)],["Patio",Vector2(-650,-985),Vector2(293,164)],["Cume",Vector2(-917,-1206),Vector2(244,139)]]:
		var landing: Node2D=m.group(data[0],landings);landing.position=data[1];landing.z_index=-13
		m.shadow(data[1],data[2].x)
		m.art("reconstruction/alto_residential_landing.png",Vector2.ZERO,data[2],landing)
		m.art("terrain/foundation.png",data[1]+Vector2(0,31),Vector2(data[2].x+18,85),m.detail).modulate=Color(.59,.57,.45,.72)
	# Stone/metal banks beside stairs provide a readable level change without obstructing the treads.
	for stair in district.get_node("Stairs").get_children():
		var at: Vector2=stair.position
		for side in [-1,1]:
			var bank := at+Vector2(side*102,-12)
			m.art("infrastructure/retaining_edge.png",bank,Vector2(91,67),m.detail)
			m.art("generated/props/pipe.png",bank+Vector2(12,22),Vector2(75,22),m.detail,.08)
		m.lamp(at+Vector2(66,34),m.commerce)
	# Residential fronts: gutters, damp foundations, short door courts and private equipment.
	var index := 0
	for home in homes.get_children():
		if not str(home.name).begins_with("Moradia"):continue
		var at: Vector2=home.position
		m.art("terrain/metal_repair.png",at+Vector2(18,21),Vector2(73,43),m.detail,.08 if index%2==0 else -.07).modulate=Color(.82,.76,.58,.72)
		if index%3==0:
			m.art("infrastructure/retaining_edge.png",at+Vector2(-10,9),Vector2(143,53),m.detail)
			m.art("generated/props/pipe.png",at+Vector2(-65,33),Vector2(81,23),m.detail,.04)
		if index%4==1 and distance(at+Vector2(95,19))>67:
			m.art("infrastructure/scrap.png",at+Vector2(95,12),Vector2(70,37),m.commerce,.05)
		index+=1
	# Route joints are readable wear/metal repairs rather than new terrain or debug markers.
	for path in paths.slice(0,3):
		for i in range(1,path.size()-1):
			if path[i].x>430:continue
			m.art("terrain/metal_repair.png",path[i],Vector2(69,44),m.detail,.11).modulate=Color(.79,.74,.57,.45)
	for points in [PackedVector2Array([Vector2(330,-265),Vector2(62,-372),Vector2(-480,-420),Vector2(-960,-460)]),PackedVector2Array([Vector2(245,-790),Vector2(-190,-900),Vector2(-650,-965),Vector2(-1090,-1128)])]:
		var cable := Line2D.new();cable.points=points;cable.width=1.8;cable.default_color=Color("705838");cable.z_index=8;finish.add_child(cable)
	for at in [Vector2(-100,-658),Vector2(-600,-850),Vector2(-877,-1117),Vector2(425,-485)]:m.lamp(at,m.commerce)
	finish.set_meta("additional_houses",extra);finish.set_meta("landings",4);finish.set_meta("scope","residential details within existing western floor; preserved coast and market")
	district.set_meta("residence_count",22+extra);district.set_meta("status","residential finishing built; pending current physical/visual validation")
	print("ALTO refinement: additional homes=",extra," total=",22+extra," four landings, existing floors and coast retained")
