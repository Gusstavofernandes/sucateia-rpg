extends "res://tools/integrate_docas_functions.gd"
var port: Node2D
var stations: Node2D
var opened: Array[NodePath]=[]
var new_floor: PackedVector2Array
func station(label: String,approaches: Array) -> Node2D:
	var node := group(label,stations);node.set_meta("public_approaches",approaches);node.set_meta("art_paths",[]);return node
func asset(station_node: Node2D,label: String,file: String,center: Vector2,ratio: float,feet: Array) -> Sprite2D:
	var sprite := object(label,file,center,ratio,feet);var node: Node2D=sprite.get_parent();var bottom := 0.
	for bounds in feet:bottom=maxf(bottom,bounds.end.y)
	var wanted := center+Vector2(0,(bottom-sprite.texture.get_height()*.5)*ratio);var shift := wanted-node.position
	for child in node.get_children():if child is Node2D:child.position-=shift
	node.position=wanted
	var paths: Array=station_node.get_meta("art_paths");paths.append(world.get_path_to(sprite));station_node.set_meta("art_paths",paths);return sprite
func native_feet(data: Dictionary) -> Array:
	var result: Array=[]
	for box in data.footboxes_native_estimated:result.append(Rect2(box[0],box[1],box[2]-box[0],box[3]-box[1]))
	return result
func cut_line(a: Vector2,b: Vector2,polys: Array) -> Array:
	var delta := b-a;var cuts: Array[float]=[0.,1.]
	for polygon in polys:
		for i in range(polygon.size()):
			var hit: Variant=Geometry2D.segment_intersects_segment(a,b,polygon[i],polygon[(i+1)%polygon.size()])
			if hit!=null:cuts.append(clampf((hit-a).dot(delta)/delta.length_squared(),0.,1.))
	cuts.sort();var result: Array=[]
	for i in range(cuts.size()-1):
		if cuts[i+1]-cuts[i]>.0001:result.append(PackedVector2Array([a+delta*cuts[i],a+delta*cuts[i+1]]))
	return result
func guard(a: Vector2,b: Vector2,parent: Node) -> void:
	var shape := CollisionShape2D.new();var segment := SegmentShape2D.new();segment.a=a;segment.b=b;shape.shape=segment;parent.add_child(shape)
func branch_pipe(label: String,a: Vector2,b: Vector2) -> void:
	var utility: RefCounted=load("res://scripts/world/connected_utilities.gd").new();var delta := b-a;var count := maxi(1,ceili(delta.length()/100.))
	for i in range(count):
		var start := a.lerp(b,float(i)/count);var finish := a.lerp(b,float(i+1)/count)
		utility.piece(rigging,label+str(i),utility.PIPE,PackedVector2Array([Vector2(-114,0),Vector2(114,0)]),PackedVector2Array([start,finish]),(finish-start)/228.,delta.normalized().orthogonal()*.17)
func supported_bay() -> void:
	# No room for a139px dry shed base outside existing60/72px strips: one compact anchored side bay.
	var center := Vector2(2983,874);var ratio := .18
	place("reconstruction/docas_finish/workyard_platform.png",center,ratio,painted,"StitchAlmoxarifadoApoiado")
	new_floor=PackedVector2Array([Vector2(210,165),Vector2(465,165),Vector2(480,225),Vector2(745,225),Vector2(760,185),Vector2(1060,180),Vector2(1210,220),Vector2(1250,365),Vector2(1360,410),Vector2(1350,515),Vector2(1260,560),Vector2(1290,720),Vector2(1170,805),Vector2(415,805),Vector2(210,790),Vector2(170,650),Vector2(75,515),Vector2(90,395),Vector2(185,365)])
	for i in range(new_floor.size()):new_floor[i]=center+(new_floor[i]-Vector2(716,549))*ratio
	var union: Array=floors.duplicate();union.append(new_floor);union.append(world.get_node("LowerCoastReworked").get_meta("land_polygon"));var edges := group("SupportedBayGuards",port);var body := StaticBody2D.new();body.name="BayWaterContainment";body.collision_mask=2;edges.add_child(body)
	# Retain approved shape nodes intact, replace only their covered portions at runtime.
	for shape in district.get_node("DeckBoundaries/OuterWaterGuards").get_children():
		if not shape is CollisionShape2D or not shape.shape is SegmentShape2D:continue
		var pieces := cut_line(shape.shape.a,shape.shape.b,[new_floor]);var removed := false
		for pair in pieces:
			if Geometry2D.is_point_in_polygon(pair[0].lerp(pair[1],.5),new_floor):removed=true
		if not removed:continue
		opened.append(world.get_path_to(shape))
		for pair in pieces:
			if not Geometry2D.is_point_in_polygon(pair[0].lerp(pair[1],.5),new_floor):guard(pair[0],pair[1],body)
	for i in range(new_floor.size()):
		for pair in cut_line(new_floor[i],new_floor[(i+1)%new_floor.size()],union):
			var middle: Vector2=pair[0].lerp(pair[1],.5);var normal: Vector2=(pair[1]-pair[0]).normalized().orthogonal()*.25
			if inside(middle+normal,union)!=inside(middle-normal,union):guard(pair[0],pair[1],body)
	floors.append(new_floor);district.set_meta("walk_polygons",floors);port.set_meta("opened_seam_shapes",opened);port.set_meta("supported_bay",new_floor)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null)
	if world.has_node("PortStitchInfrastructure"):
		if not "--revise-port-stitch" in OS.get_cmdline_user_args():world.free();quit(0);return
		var old_floors: Array=world.get_node("DocasDistrict").get_meta("walk_polygons");var old_bay: PackedVector2Array=world.get_node("PortStitchInfrastructure").get_meta("supported_bay")
		if old_floors[-1]!=old_bay:push_error("Unexpected floor appended by another task; no stitch replay");world.free();quit(1);return
		old_floors.pop_back();world.get_node("DocasDistrict").set_meta("walk_polygons",old_floors);world.get_node("PortStitchInfrastructure").free();world.get_node("Structures/PortStitchArchitecture").free();world.get_node("DocasDistrict/WorkingDecks/StitchAlmoxarifadoApoiado").free()
	district=world.get_node("DocasDistrict");floors.assign(district.get_meta("walk_polygons"));painted=district.get_node("WorkingDecks");receivers=district.get_node("WetSupports")
	port=group("PortStitchInfrastructure",world);port.set_script(load("res://scripts/world/port_stitch.gd"));stations=group("FunctionalStations",port);architecture=group("PortStitchArchitecture",world.get_node("Structures"));architecture.y_sort_enabled=true;contacts=group("ContactWear",port,-10);rigging=group("ServiceRigging",port,-9)
	var manifest: Dictionary=JSON.parse_string(FileAccess.get_file_as_string("res://assets/reconstruction/port_stitch/manifest.json"));var catalog := {};for entry in manifest.assets:catalog[entry.name]=entry
	supported_bay()
	var entry := station("ChegadaRasa",[Vector2(2350,1455),Vector2(2500,1540)])
	asset(entry,"CarrinhoDeEspera","reconstruction/market_salvage_cart.png",Vector2(2415,1528),.08,[Rect2(224,872,73,102),Rect2(936,872,72,102),Rect2(321,1120,75,59),Rect2(843,1120,77,59)])
	var sorting := station("TriagemMolhada",[Vector2(2500,1540),Vector2(2540,1560)]);var data: Dictionary=catalog.wet_sorting_lot
	asset(sorting,"CobreEMadeiraSeparados","reconstruction/port_stitch/wet_sorting_lot.png",Vector2(2594,1552),data.scale_uniform,native_feet(data))
	var service := station("Almoxarifado",[Vector2(2983,887),Vector2(3090,925)]);data=catalog.rope_oil_service_shed
	asset(service,"OficinaDeCordasEOleo","reconstruction/port_stitch/rope_oil_service_shed.png",Vector2(2983,832),data.scale_uniform,native_feet(data))
	var urban := station("BordaUrbana",[Vector2(3175,70)]);data=catalog.drain_inspection_module
	var drain := asset(urban,"InspecaoNaMargemIndustrial","reconstruction/port_stitch/drain_inspection_module.png",Vector2(3122,85),data.scale_uniform,native_feet(data))
	var feed := drain.to_global(Vector2(125,180)-Vector2(drain.texture.get_size())*.5);var outlet := drain.to_global(Vector2(1298,606)-Vector2(drain.texture.get_size())*.5)
	var utility: RefCounted=load("res://scripts/world/connected_utilities.gd").new()
	# Small branch enters the center of an existing larger collector junction.
	utility.elbow(rigging,"CurvaDoRamalN",Vector2(3020,-45),Vector2(3051,-19),false);branch_pipe("DescidaDoRamal",Vector2(3051,-19),Vector2(3051,feed.y-26));utility.elbow(rigging,"CurvaDoRamalS",Vector2(3051,feed.y-26),feed,true)
	branch_pipe("SaidaDaInspecao",outlet,Vector2(3198,outlet.y));utility.elbow(rigging,"DescargaNoCanal",Vector2(3198,outlet.y),Vector2(3222,outlet.y+26),false);branch_pipe("BocaSobreAgua",Vector2(3222,outlet.y+26),Vector2(3222,138))
	port.set_meta("drain_sockets",PackedVector2Array([feed,outlet]));port.set_meta("drain_destination",Vector2(3222,138));port.set_meta("collector_source",Vector2(3020,-45))
	var mouths := station("BocasTecnicas",[Vector2(1296,1572),Vector2(2210,1668),Vector2(3000,260)])
	var winch := asset(mouths,"TracaoDoPocoVelho","reconstruction/amarras_parallel/chain_winch_station.png",Vector2(1408,1480),.107341,[Rect2(320,551,880,253)])
	var socket := winch.to_global(Vector2(97,434)-Vector2(winch.texture.get_size())*.5);line("GuiaAtePoco",PackedVector2Array([socket,Vector2(1336,1492),Vector2(1336,1514)]),2.)
	# Ends at the masonry jamb of the existing Poço mouth; input pocket stays clear.
	port.set_meta("winch_socket",socket);port.set_meta("winch_wall_lug",Vector2(1336,1514))
	# Low, restrained wear follows the service economy; never replace the existing floor.
	for pair in [[Vector2(2983,892),.055],[Vector2(2490,1540),.06]]:
		var wear := place("reconstruction/docas_parallel/complement_v1/wet_wood_saltwear_decal.png",pair[0],pair[1],contacts,"UsoPortuario%d"%int(pair[0].x));wear.modulate.a=.22
	port.set_meta("brief","CONSULTANT_PORT_STITCH_BRIEF");port.set_meta("stage","integrated; physical and visual verification pending")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if packed.get_state().get_node_count()!=count_nodes(world):push_error("Stitch nodes omitted during packing");error=FAILED
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("STITCH integrated=",error," five functions; one compact supported side bay; old routes and scene nodes preserved; seam openings=",opened.size())
	world.free();world=null;district=null;architecture=null;port=null;stations=null;contacts=null;rigging=null;painted=null;receivers=null;packed=null;quit(error)
