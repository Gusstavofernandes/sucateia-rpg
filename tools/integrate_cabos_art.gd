extends "res://tools/build_amarras_geography.gd"
var deck_polygons: Array[PackedVector2Array]=[]
var render: Node2D
var supports: Node2D
var links: Node2D
var deck_count := 0
var support_count := 0
func sprite(file: String,point: Vector2,ratio: float,parent: Node,label: String) -> Sprite2D:
	var texture: Texture2D=load("res://assets/"+file)
	var node := art(file,point,Vector2(texture.get_size())*ratio,parent);node.name=label;return node
func cable(label: String,a: Vector2,b: Vector2,heavy: bool=false) -> void:
	var node := Line2D.new();node.name=label;node.points=PackedVector2Array([a,a.lerp(b,.5)+Vector2(0,6),b]);node.width=3.5 if heavy else 2.;node.default_color=Color("29221a");node.antialiased=true;links.add_child(node)
	var inner := Line2D.new();inner.points=node.points;inner.width=1.2 if heavy else .7;inner.default_color=Color("77634a");inner.antialiased=true;node.add_child(inner)
	node.set_meta("anchored_endpoints",PackedVector2Array([a,b]))
func support(label: String,at: Vector2) -> Vector2:
	# The existing intermediate platform receives the under-deck socket.
	# Crown carries tension cables; its masonry foot reaches the street below.
	var center := at-(Vector2(370,338)-Vector2(384,384))*.4
	var tower := sprite("region/cable_tower.png",center,.4,supports,label)
	tower.set_meta("socket_world",at);var foot := center+(Vector2(371,711)-Vector2(384,384))*.4
	tower.set_meta("ground_contact",foot);support_count+=1
	var shadow := sprite("fx/light.svg",foot+Vector2(0,3),.4,district.get_node("ContactShadows"),label+"Contact")
	shadow.scale=Vector2(105,34)/Vector2(shadow.texture.get_size());shadow.modulate=Color(0,0,0,.44)
	return center+(Vector2(370,138)-Vector2(384,384))*.4
func route_floor(route: Node,width: float) -> void:
	var points: PackedVector2Array=route.get_meta("points");var side := (points[1]-points[0]).normalized().orthogonal()*width*.5
	deck_polygons.append(PackedVector2Array([points[0]-side,points[1]-side,points[1]+side,points[0]+side]));route.set_meta("clear_width",width)
func ew_decks(route: Node) -> void:
	var points: PackedVector2Array=route.get_meta("points");var length := points[0].distance_to(points[1]);var count := ceili(length/173.)
	# Uniform original scale; overlap only the open terminal bands, no rotated camera.
	var centers: Array[Vector2]=[]
	for i in range(count):
		var walking := points[0].lerp(points[1],(i+.5)/count)
		var center := walking+Vector2(.0705,9.949);var label := "%sDeck%02d"%[route.name,i]
		var node := sprite("reconstruction/cabos_parallel/main_deck_ew_wide.png",center,.14111610006414368,render,label)
		node.set_meta("walking_center",walking);node.set_meta("clear_rect",Rect2(walking-Vector2(86.78,37.74),Vector2(173.56,75.48)));deck_count+=1;centers.append(center)
		# Each socket has a real load receiver; pairs share tension along the rail.
		if i%2==0 or i==count-1:
			var socket := center+Vector2(-56.164,62.444);var crown := support(label+"Tower",socket)
			for lug in [Vector2(-100.757,-40.571),Vector2(100.475,-40.571)]:cable(label+"Stay",crown,center+lug,true)
	for i in range(centers.size()-1):
		cable("%sRailCable%02d"%[route.name,i],centers[i]+Vector2(0,-40.571),centers[i+1]+Vector2(0,-40.571))
func ns_decks(route: Node) -> void:
	var points: PackedVector2Array=route.get_meta("points");var length := points[0].distance_to(points[1]);var count := ceili(length/120.)
	for i in range(count):
		var walking := points[0].lerp(points[1],(i+.5)/count);var label := "%sDeck%02d"%[route.name,i]
		sprite("infrastructure/walkway.png",walking+Vector2(.6,3.6),.6,render,label);deck_count+=1
		if i%3==0 or i==count-1:
			var crown := support(label+"Tower",walking+Vector2(45,42))
			cable(label+"Brace",crown,walking+Vector2(43,-50),true)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("CabosDistrict")
	if district.has_meta("art_integrated"):print("CABOS art retained; no replay");world.queue_free();await process_frame;quit(0);return
	render=district.get_node("ElevatedDecks");supports=group("StructuralSupports",district,5);links=group("TensionAndMessages",district,7);group("ContactShadows",district,-3)
	var bridge := PackedVector2Array([Vector2(220,-992),Vector2(310,-988),Vector2(410,-985),Vector2(510,-985),Vector2(650,-988),Vector2(751.7,-992)])
	for route_node in district.get_node("Routes").get_children():
		var label := String(route_node.name)
		if label.begins_with("PonteSecundaria"):
			var index := int(label.trim_prefix("PonteSecundaria"));route_node.set_meta("points",PackedVector2Array([bridge[index],bridge[index+1]]));route_floor(route_node,28)
		elif label=="EncontroT":route_floor(route_node,32)
		elif label=="RamalMercado":route_floor(route_node,36)
		elif label in ["ViaOeste","ViaPrincipal","ChegadaDasForjas"]:route_floor(route_node,72);ew_decks(route_node)
		else:route_floor(route_node,60);ns_decks(route_node)
	for landing_node in district.get_node("Landings").get_children():
		var point: Vector2=landing_node.position;var half := Vector2(54,36)
		if String(landing_node.name).begins_with("PatamarT"):half=Vector2(36,22)
		deck_polygons.append(rect(point-half,point+half))
		# Broad painted landings at public spawns and main turns. T ends join N-S floor.
		if not String(landing_node.name).begins_with("PatamarT"):
			sprite("reconstruction/cabos_parallel/main_deck_ew_wide.png",point+Vector2(.0705,9.949),.14111610006414368,render,String(landing_node.name)+"Landing")
	for i in range(1,bridge.size()-1):deck_polygons.append(rect(bridge[i]-Vector2(14,14),bridge[i]+Vector2(14,14)))
	var bridge_center := Vector2(486.76,-995.38)
	sprite("reconstruction/cabos_parallel/suspension_bridge_ew.png",bridge_center,.26,render,"PonteSecundariaFinal")
	for socket in [Vector2(251.46,-1036.2),Vector2(719.2,-1036.2)]:
		var crown := support("PonteAncora%d"%int(socket.x),socket+Vector2(0,80));cable("PonteTirante",crown,socket,true)
	var junction_center := Vector2(742.48,-586.04)
	sprite("reconstruction/cabos_parallel/walkway_t_junction_clean.png",junction_center,.38,render,"EncontroTFinal")
	var t_socket := junction_center+Vector2(2.28,86.64);var t_crown := support("ApoioCentralDoT",t_socket)
	for socket in [Vector2(469.64,-522.2),Vector2(1016.84,-522.2),Vector2(744,-716)]:cable("TDistribuicao",t_crown,socket+Vector2(0,-20),true)
	# House is attached to a pair of independent structural receivers, off the circulation lane.
	var house_center := Vector2(305,-712);var house := sprite("reconstruction/cabos_parallel/hanging_house.png",house_center,.28,supports,"CasaSuspensa")
	var beams := PackedVector2Array([house_center+(Vector2(210,112)-Vector2(687,572.5))*.28,house_center+(Vector2(1160,112)-Vector2(687,572.5))*.28])
	house.set_meta("beam_connections",beams)
	for i in range(2):
		var crown := support("CasaTorre%d"%i,beams[i]+Vector2(0,80));cable("CasaTravessa%d"%i,crown,beams[i],true)
	var door := house_center+(Vector2(565,931)-Vector2(687,572.5))*.28
	# Exterior porch reaches the broad main lane; the hanging cabin is visual, not an interior portal.
	var porch_end := Vector2(door.x,-420);var porch_route := marker("AcessoCasa",Vector2.ZERO,district.get_node("Routes"));porch_route.set_meta("points",PackedVector2Array([door,porch_end]));route_floor(porch_route,60);ns_decks(porch_route)
	deck_polygons.append(rect(door-Vector2(32,27),door+Vector2(32,27)));marker("SoleiraCasa",door,district.get_node("Landings"))
	var house_shadow := sprite("fx/light.svg",door+Vector2(0,205),1.,district.get_node("ContactShadows"),"CasaShadow");house_shadow.scale=Vector2(206,85)/Vector2(house_shadow.texture.get_size());house_shadow.modulate=Color(0,0,0,.32)
	for point in [Vector2(-400,-992),Vector2(744,-716),Vector2(1900,-104)]:
		var center: Vector2=point+Vector2(65,35);var mast := sprite("reconstruction/cabos_parallel/power_messenger_anchor.png",center,.16,supports,"Mastro%d"%int(point.x));mast.set_meta("function","messages and power, not heavy structural support")
		var socket: Vector2=center+(Vector2(385,51)-Vector2(697,564))*.16;cable("Mensagens%d"%int(point.x),socket,point+Vector2(0,-35))
	district.set_meta("walk_polygons",deck_polygons);district.set_meta("art_integrated",true);district.set_meta("stage","visual integration pending capture and physical revalidation");district.set_meta("deck_modules",deck_count);district.set_meta("structural_supports",support_count)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("CABOS art saved=",error," deck modules=",deck_count," supports=",support_count," new terrain=0; approved architecture unchanged")
	world.queue_free();world=null;district=null;render=null;supports=null;links=null;packed=null;await process_frame;await process_frame;quit(error)
