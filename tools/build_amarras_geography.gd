extends SceneTree
var world: Node2D
var district: Node2D
var detail: Node2D
var structures: Node2D
var paths: Array[PackedVector2Array]=[]
var bridges: Array[PackedVector2Array]=[]
var waters: Array[PackedVector2Array]=[]
var outline := PackedVector2Array([Vector2(3980,-140),Vector2(4350,-340),Vector2(4780,-300),Vector2(5120,-70),Vector2(5240,230),Vector2(5590,380),Vector2(5670,660),Vector2(5430,940),Vector2(5030,1050),Vector2(4760,875),Vector2(4580,1110),Vector2(4240,1060),Vector2(4090,790),Vector2(3920,665),Vector2(3990,425),Vector2(3910,245)])
func _initialize() -> void:call_deferred("run")
func group(label: String,parent: Node,z: int=0) -> Node2D:
	var node := Node2D.new();node.name=label;node.z_index=z;parent.add_child(node);return node
func art(file: String,point: Vector2,size: Vector2,parent: Node,angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://assets/"+file);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func marker(label: String,point: Vector2,parent: Node) -> Marker2D:
	var node := Marker2D.new();node.name=label;node.position=point;parent.add_child(node);return node
func route(label: String,points: PackedVector2Array,parent: Node) -> void:
	paths.append(points);var node := marker(label,Vector2.ZERO,parent);node.set_meta("points",points);node.set_meta("clear_width",100)
func rect(a: Vector2,b: Vector2) -> PackedVector2Array:return PackedVector2Array([a,Vector2(b.x,a.y),b,Vector2(a.x,b.y)])
func bridge(label: String,a: Vector2,b: Vector2,width: float,suspension: bool=false) -> void:
	var node := group(label,district.get_node("Bridges"),-12);node.set_meta("approach",a);node.set_meta("departure",b)
	var delta := b-a;var side := delta.normalized().orthogonal()*width*.5
	var polygon := PackedVector2Array([a-side,b-side,b+side,a+side]);bridges.append(polygon)
	if suspension:
		var sprite := art("reconstruction/cabos_parallel/suspension_bridge_ew.png",a.lerp(b,.5),Vector2(580,193),node)
		sprite.scale=Vector2.ONE*(580./sprite.texture.get_width())
	else:
		var count := maxi(1,ceili(delta.length()/152))
		for i in range(count):
			var at := a.lerp(b,(i+.5)/count)
			var size := Vector2(width+24,delta.length()/count+10)
			art("infrastructure/walkway.png",at,size,node,delta.angle()-PI/2)
			for direction in [-1,1]:art("infrastructure/coastal_wall.png",at+side*direction,Vector2(50,69),detail).modulate=Color(.72,.71,.59)
	for at in [a,b]:
		art("terrain/foundation.png",at,Vector2(93,73),detail).modulate=Color(.48,.48,.38,.85)
		for direction in [-1,1]:art("infrastructure/retaining_edge.png",at+side*direction,Vector2(62,54),node).modulate=Color(.77,.75,.58)
	for direction in [-1,1]:
		var edge := PackedVector2Array([a+side*direction,b+side*direction])
		var body := StaticBody2D.new();var shape := CollisionShape2D.new();var rectangle := RectangleShape2D.new();var setback := 80. if suspension else 0.;rectangle.size=Vector2(delta.length()-setback,8);shape.shape=rectangle;shape.position=a.lerp(b,.5)+side*direction+delta.normalized()*setback*.5;shape.rotation=delta.angle();body.add_child(shape);node.add_child(body)
func canal_y(x: float) -> float:
	var points := PackedVector2Array([Vector2(4530,700),Vector2(4750,705),Vector2(4950,760),Vector2(5150,715),Vector2(5380,745)])
	for i in range(points.size()-1):
		if x>=points[i].x and x<=points[i+1].x:return lerpf(points[i].y,points[i+1].y,inverse_lerp(points[i].x,points[i+1].x,x))
	return 700
func drainage() -> void:
	var parent := group("Drainage",district,-17);var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/forjas_drain.gdshader");material.set_shader_parameter("grime",load("res://assets/infrastructure/channel.png"))
	for interval in [Vector2(4530,4705),Vector2(4795,5105),Vector2(5195,5380)]:
		var upper := PackedVector2Array([Vector2(interval.x,canal_y(interval.x)-26)])
		for x in [4750,4950,5150]:
			if x>interval.x and x<interval.y:upper.append(Vector2(x,canal_y(x)-26))
		upper.append(Vector2(interval.y,canal_y(interval.y)-26));var polygon := upper.duplicate()
		for i in range(upper.size()-1,-1,-1):polygon.append(upper[i]+Vector2(0,52))
		waters.append(polygon);var water := Polygon2D.new();water.polygon=polygon;water.material=material;parent.add_child(water)
		var body := StaticBody2D.new();var collision := CollisionPolygon2D.new();collision.polygon=polygon;body.add_child(collision);parent.add_child(body)
		for i in range(upper.size()-1):
			var a: Vector2=upper[i];var b: Vector2=upper[i+1];var delta := b-a;var count := ceili(delta.length()/95)
			for j in range(count):
				for side in [0,1]:art("infrastructure/retaining_edge.png",a.lerp(b,(j+.5)/count)+Vector2(0,-6+side*64),Vector2(delta.length()/count+9,39),parent,delta.angle()).modulate=Color(.74,.75,.64)
	for x in [4750,5150]:bridge("Travessia%d"%x,Vector2(x,canal_y(x)-89),Vector2(x,canal_y(x)+89),76)
func module(label: String,file: String,point: Vector2,size: Vector2,base: Vector2) -> void:
	var node := group(label,structures);node.position=point
	var texture: Texture2D=load("res://assets/"+file);var dimensions := Vector2(texture.get_size());var ratio := minf(size.x/dimensions.x,size.y/dimensions.y)
	var sprite := art(file,Vector2(0,-size.y*.35),dimensions*ratio,node)
	var body := StaticBody2D.new();body.position=Vector2(0,-28);var shape := CollisionShape2D.new();var rectangle := RectangleShape2D.new();rectangle.size=base;shape.shape=rectangle;body.add_child(shape);node.add_child(body)
	art("terrain/metal_repair.png",point+Vector2(0,4),Vector2(base.x*1.14,44),detail).modulate=Color(.58,.58,.48,.77)
	art("fx/light.svg",point+Vector2(4,5),Vector2(base.x*1.13,29),detail).modulate=Color(0,0,0,.57)
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	if world.has_node("PassagemAmarrasDistrict"):world.queue_free();await process_frame;print("AMARRAS geography retained; no replay");quit(0);return
	district=group("PassagemAmarrasDistrict",world);detail=group("GroundIntegration",district,-13)
	structures=group("AmarrasInfrastructure",world.get_node("Structures"));structures.y_sort_enabled=true
	group("Bridges",district);var routes := group("Routes",district)
	route("EntradaDasForjas",PackedVector2Array([Vector2(3550,0),Vector2(3690,0),Vector2(3990,0),Vector2(4290,30)]),routes)
	route("ViaDeTransferencia",PackedVector2Array([Vector2(4290,30),Vector2(4480,260),Vector2(4820,290),Vector2(5110,440),Vector2(5480,565),Vector2(5520,565)]),routes)
	route("CorrentesDeManutencao",PackedVector2Array([Vector2(3280,240),Vector2(3360,275),Vector2(3935,275),Vector2(4120,360),Vector2(4240,730)]),routes)
	route("CircuitoInferior",PackedVector2Array([Vector2(4240,730),Vector2(4560,835),Vector2(4950,900),Vector2(5230,850),Vector2(5440,830),Vector2(5480,565)]),routes)
	route("TravessaDeInspecao",PackedVector2Array([Vector2(4480,260),Vector2(4480,550),Vector2(4750,616),Vector2(4750,794),Vector2(4950,900)]),routes)
	route("ManutencaoDoCanal",PackedVector2Array([Vector2(5110,440),Vector2(5150,626),Vector2(5150,804),Vector2(5230,850)]),routes)
	route("RamalDeCarga",PackedVector2Array([Vector2(4700,420),Vector2(4750,550),Vector2(4950,550),Vector2(5110,440)]),routes)
	var floor := TileMapLayer.new();floor.name="AmarrasFloor";floor.z_index=-30;floor.tile_set=load("res://assets/terrain/sucateia_terrain.tres");district.add_child(floor)
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/amarras_ground.gdshader");material.set_shader_parameter("outline_points",outline);material.set_shader_parameter("grime",load("res://assets/region/salvage_ground.png"));material.set_shader_parameter("metal",load("res://assets/terrain/metal_repair.png"))
	var segments: Array[Vector4]=[]
	for path in paths:
		for i in range(path.size()-1):segments.append(Vector4(path[i].x,path[i].y,path[i+1].x,path[i+1].y))
	material.set_shader_parameter("route_count",segments.size());while segments.size()<32:segments.append(Vector4.ZERO)
	material.set_shader_parameter("route_segments",segments);floor.material=material
	for y in range(-8,24):
		for x in range(80,120):
			var cell := Vector2i(x,y);var at := Vector2(x*48+24,y*48+24)
			if Geometry2D.is_point_in_polygon(at,outline):floor.set_cell(cell,0,Vector2i(posmod(x,16),posmod(y,16)))
	bridge("PonteDeTransferencia",Vector2(3690,0),Vector2(3990,0),92)
	bridge("PonteDasCorrentes",Vector2(3355,275),Vector2(3935,275),48,true)
	drainage()
	var sea := Polygon2D.new();sea.name="AguaIndustrialContinua";sea.z_index=-35;sea.polygon=rect(Vector2(3890,-390),Vector2(7600,4000));var sea_material := ShaderMaterial.new();sea_material.shader=load("res://assets/reconstruction/lower_sea.gdshader");sea_material.set_shader_parameter("grime",load("res://assets/region/salvage_ground.png"));var sea_edges: Array[Vector4]=[]
	for i in range(outline.size()):sea_edges.append(Vector4(outline[i].x,outline[i].y,outline[(i+1)%outline.size()].x,outline[(i+1)%outline.size()].y))
	sea_material.set_shader_parameter("edge_count",sea_edges.size());while sea_edges.size()<64:sea_edges.append(Vector4.ZERO)
	sea_material.set_shader_parameter("coast_edges",sea_edges);sea.material=sea_material;district.add_child(sea)
	for i in range(outline.size()):
		var a: Vector2=outline[i];var b: Vector2=outline[(i+1)%outline.size()];var delta := b-a;var count := ceili(delta.length()/132)
		for j in range(count):
			var at := a.lerp(b,(j+.5)/count)
			if at.distance_to(Vector2(3990,0))<100 or at.distance_to(Vector2(3935,275))<80 or at.distance_to(Vector2(5520,565))<135:continue
			art("infrastructure/retaining_edge.png",at,Vector2(delta.length()/count+15,51),detail,delta.angle()).modulate=Color(.72,.76,.64)
	module("ReparosDaEntrada","reconstruction/forjas_workshop.png",Vector2(4330,-80),Vector2(270,190),Vector2(156,55))
	module("DepositoDeTransferencia","reconstruction/forjas_workshop.png",Vector2(5410,790),Vector2(255,180),Vector2(149,53))
	module("GuindasteDaPlataforma","reconstruction/forjas_parallel/compact_loading_crane.png",Vector2(4870,430),Vector2(180,170),Vector2(63,45))
	for point in [Vector2(4610,470),Vector2(4870,540)]:module("Carro%d"%int(point.x),"reconstruction/market_salvage_cart.png",point,Vector2(80,90),Vector2(42,30))
	var frontiers := group("Frontiers",district);marker("ViaDasForjas",Vector2(3550,0),frontiers);marker("ManutencaoDasForjas",Vector2(3280,240),frontiers)
	var yards := group("WorkYards",district)
	for data in [["Transferencia",Vector2(4660,380)],["Amarracao",Vector2(4400,180)],["Servico",Vector2(4210,620)],["Inspecao",Vector2(5130,330)],["Distribuicao",Vector2(4950,550)]]:marker(data[0],data[1],yards)
	var exits := group("FutureExits",district);var future := marker("Engrenopolis",Vector2(5520,565),exits);future.set_meta("status","reserved continuation only; Engrenopolis not built")
	var arrivals := group("SafeArrivals",district);marker("ChegadaDeCarga",Vector2(4070,20),arrivals);marker("ChegadaDeManutencao",Vector2(4030,330),arrivals)
	district.set_meta("land_polygon",outline);district.set_meta("walk_polygons",bridges);district.set_meta("water_polygons",waters);district.set_meta("water_samples",PackedVector2Array([Vector2(4590,canal_y(4590)),Vector2(4940,canal_y(4940)),Vector2(5320,canal_y(5320))]));district.set_meta("stage","geography/connected routes; parallel art integration pending")
	var camera: Camera2D=world.get_node("Structures/Player/Camera");camera.limit_right=6650;camera.limit_bottom=2900
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("AMARRAS geography saved=",error," cells=",floor.get_used_cells().size()," routes=",paths.size()," bridges=",bridges.size()," same scene; approved districts untouched")
	world.queue_free();world=null;district=null;detail=null;structures=null;packed=null;await process_frame;await process_frame;quit(error)
