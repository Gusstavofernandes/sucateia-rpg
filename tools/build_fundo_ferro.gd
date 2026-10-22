extends SceneTree
var world: Node2D
var floor: TileMapLayer
var structures: Node2D
var detail: Node2D
var routes: Array[PackedVector2Array]=[]
var room_shapes: Array[PackedVector2Array]=[]
var waters: Array[PackedVector2Array]=[]
var water_samples := PackedVector2Array()
const ACCESS := [["PocoVelho",Vector2(1296,1572),Vector2(1296,1572)],["DocaLeste",Vector2(2210,1668),Vector2(2250,2200)],["ForjasManutencao",Vector2(3000,260),Vector2(3000,480)]]
func _initialize() -> void:call_deferred("run")
func group(label: String, parent: Node, z: int=0) -> Node2D:
	var node := Node2D.new();node.name=label;node.z_index=z;parent.add_child(node);return node
func art(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://assets/"+file);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func solid(point: Vector2, size: Vector2, parent: Node) -> void:
	var body := StaticBody2D.new();body.position=point;var collision := CollisionShape2D.new();var shape := RectangleShape2D.new();shape.size=size;collision.shape=shape;body.add_child(collision);parent.add_child(body)
func own(node: Node, owner_node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=owner_node;own(child,owner_node)
func save(node: Node, path: String) -> Error:
	own(node,node);var packed := PackedScene.new();var error := packed.pack(node)
	if error==OK:error=ResourceSaver.save(packed,path)
	return error
func marker(label: String, point: Vector2, parent: Node) -> void:
	var node := Marker2D.new();node.name=label;node.position=point;parent.add_child(node)
func add_accesses(target: Node2D, surface: bool) -> void:
	var entries := group("LayerEntrances",target);var arrivals := group("LayerArrivals",target)
	for data in ACCESS:
		var point: Vector2=data[1 if surface else 2]
		marker(data[0],point,arrivals)
		var entry := Area2D.new();entry.name=data[0];entry.position=point;entry.collision_layer=0;entry.collision_mask=2;entry.set_script(load("res://scripts/world/layer_access.gd"));entries.add_child(entry)
		var collider := CollisionShape2D.new();var circle := CircleShape2D.new();circle.radius=47;collider.shape=circle;entry.add_child(collider)
		var prompt := Label.new();prompt.name="Prompt";prompt.text="F — "+("descer" if surface else "subir")+" · "+("Poço Velho" if data[0]=="PocoVelho" else "Doca Leste" if data[0]=="DocaLeste" else "Forjas / manutenção");prompt.position=Vector2(-138,38);prompt.size=Vector2(276,28);prompt.horizontal_alignment=HORIZONTAL_ALIGNMENT_CENTER;prompt.z_index=25;prompt.visible=false;prompt.add_theme_color_override("font_color",Color("e8ca8d"));prompt.add_theme_color_override("font_shadow_color",Color.BLACK);prompt.add_theme_constant_override("shadow_offset_x",2);prompt.add_theme_constant_override("shadow_offset_y",2);entry.add_child(prompt)
		if surface:
			if data[0]=="ForjasManutencao":art("infrastructure/stairs.png",point-Vector2(0,25),Vector2(99,87),entries).z_index=-12
			elif data[0]=="DocaLeste":art("terrain/oil_hatch.png",point,Vector2(80,63),entries).z_index=-12
			else:art("terrain/metal_repair.png",point+Vector2(43,9),Vector2(64,37),entries,.12).z_index=-12
		else:
			art("infrastructure/stairs.png",point-Vector2(0,18),Vector2(102,105),entries).z_index=-12
		entry.set_meta("function","physical vertical access; F in proximity only")
func route(label: String, points: PackedVector2Array) -> void:
	routes.append(points);var node := Marker2D.new();node.name=label;node.set_meta("points",points);world.get_node("Routes").add_child(node)
func room(label: String, center: Vector2, size: Vector2, arrival: Vector2=Vector2.INF) -> void:
	var a := center-size/2;var b := center+size/2
	var polygon := PackedVector2Array([a+Vector2(60,0),Vector2(b.x-40,a.y),Vector2(b.x,a.y+60),b-Vector2(0,45),b-Vector2(70,0),Vector2(a.x+45,b.y),Vector2(a.x,b.y-70),Vector2(a.x,a.y+45)])
	room_shapes.append(polygon);marker(label,center if arrival==Vector2.INF else arrival,world.get_node("Rooms"))
func in_layout(point: Vector2) -> bool:
	for polygon in room_shapes:
		if Geometry2D.is_point_in_polygon(point,polygon):return true
	for path in routes:
		for i in range(path.size()-1):
			if point.distance_to(Geometry2D.get_closest_point_to_segment(point,path[i],path[i+1]))<91:return true
	return false
func lamp(point: Vector2, cyan: bool=false) -> void:
	art("infrastructure/lantern.png",point-Vector2(0,23),Vector2(24,37),structures)
	var light := PointLight2D.new();light.position=point;light.texture=load("res://assets/fx/light.svg");light.texture_scale=.57;light.energy=.48;light.color=Color("78aaac" if cyan else "d7a065");world.add_child(light)
func machine(label: String, point: Vector2, file: String, size: Vector2) -> void:
	var node := group(label,structures);node.position=point
	art("terrain/foundation.png",point,Vector2(size.x*.95,95),detail).modulate=Color(.52,.60,.53,.82)
	art("fx/light.svg",point+Vector2(8,6),Vector2(size.x,73),detail).modulate=Color(0,0,0,.65)
	art(file,Vector2(0,-size.y*.4),size,node)
	solid(Vector2(0,-32),Vector2(size.x*.59,70),node);node.set_meta("blocked_base",point-Vector2(0,32))
	art("terrain/oil_hatch.png",point+Vector2(-63,28),Vector2(76,57),detail,.09).modulate=Color(.42,.50,.43,.8)
func water_rect(rect: Rect2) -> void:
	var a := rect.position;var b := rect.end
	var polygon := PackedVector2Array([a,Vector2(b.x,a.y),b,Vector2(a.x,b.y)])
	waters.append(polygon);water_samples.append(rect.get_center())
	var water := Polygon2D.new();water.polygon=polygon;water.z_index=-18;var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/forjas_drain.gdshader");material.set_shader_parameter("grime",load("res://assets/infrastructure/channel.png"));water.material=material;world.add_child(water)
	var body := StaticBody2D.new();var collision := CollisionPolygon2D.new();collision.polygon=polygon;body.add_child(collision);world.add_child(body)
	for y in [a.y,b.y]:art("infrastructure/retaining_edge.png",Vector2(rect.get_center().x,y),Vector2(rect.size.x+12,33),detail)
func build() -> void:
	world=Node2D.new();world.name="FundoFerro";root.add_child(world);world.set_meta("world_layer","underground")
	structures=group("Structures",world);structures.y_sort_enabled=true;detail=group("GroundIntegration",world,-14)
	group("Rooms",world);group("Routes",world)
	room("PocoVelho",Vector2(1296,1572),Vector2(470,355))
	room("Bombas",Vector2(1750,2000),Vector2(505,365))
	room("Descarte",Vector2(2300,2180),Vector2(600,365))
	room("Maquinas",Vector2(2900,1770),Vector2(620,450))
	room("Reservatorio",Vector2(2700,1160),Vector2(570,365),Vector2(2700,1240))
	room("Ruinas",Vector2(1750,1050),Vector2(465,395))
	room("Valvulas",Vector2(3100,640),Vector2(530,450),Vector2(3000,570))
	route("PocoBombas",PackedVector2Array([Vector2(1296,1572),Vector2(1450,1700),Vector2(1750,2000)]))
	route("BombasDescarte",PackedVector2Array([Vector2(1750,2000),Vector2(1820,2030),Vector2(1820,2160),Vector2(2300,2180)]))
	route("DescarteMaquinas",PackedVector2Array([Vector2(2300,2180),Vector2(2600,2120),Vector2(2900,1770)]))
	route("MaquinasReservatorio",PackedVector2Array([Vector2(2900,1770),Vector2(2850,1440),Vector2(2700,1240)]))
	route("ReservatorioRuinas",PackedVector2Array([Vector2(2700,1240),Vector2(2480,1260),Vector2(2300,1190),Vector2(1950,1150),Vector2(1750,1050)]))
	route("RuinasPoco",PackedVector2Array([Vector2(1750,1050),Vector2(1510,1090),Vector2(1280,1240),Vector2(1296,1572)]))
	route("TravessaDosDrenos",PackedVector2Array([Vector2(2300,2180),Vector2(2210,1840),Vector2(2100,1470),Vector2(1970,1250),Vector2(1750,1050)]))
	route("GaleriaDasValvulas",PackedVector2Array([Vector2(2700,1240),Vector2(2660,1250),Vector2(2660,1030),Vector2(3000,940),Vector2(3000,570),Vector2(3000,480)]))
	floor=TileMapLayer.new();floor.name="GroundFloor";floor.z_index=-30;floor.tile_set=load("res://assets/terrain/sucateia_terrain.tres");var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/fundo_ground.gdshader");floor.material=material;world.add_child(floor)
	for y in range(7,53):
		for x in range(19,74):
			var cell := Vector2i(x,y);var at := Vector2(x*48+24,y*48+24)
			if in_layout(at):floor.set_cell(cell,0,Vector2i(posmod(x,16),posmod(y,16)))
	var walls := group("Walls",structures);walls.y_sort_enabled=true
	for cell in floor.get_used_cells():
		for side in [Vector2i.LEFT,Vector2i.RIGHT,Vector2i.UP,Vector2i.DOWN]:
			if floor.get_cell_source_id(cell+side)!=-1:continue
			var at := floor.map_to_local(cell)+Vector2(side)*24
			art("reconstruction/fundo_wall.png",at,Vector2(61,32),walls,PI/2 if side.x!=0 else 0).modulate=Color(.80,.86,.77,1)
			solid(at+Vector2(side)*12,Vector2(26,48) if side.x!=0 else Vector2(48,26),walls)
	machine("MotorAbandonado",Vector2(3050,1680),"reconstruction/fundo_abandoned_engine.png",Vector2(350,239))
	machine("BombasDeRefluxo",Vector2(1595,1975),"region/pump_station.png",Vector2(205,210))
	machine("ValvulasAntigas",Vector2(3180,700),"generated/structures/reactor.png",Vector2(165,172))
	machine("TornoDesativado",Vector2(2400,2290),"reconstruction/forjas_recycler.png",Vector2(209,149))
	water_rect(Rect2(1680,2070,96,62));water_rect(Rect2(1864,2070,96,62))
	water_rect(Rect2(2540,1090,77,72));water_rect(Rect2(2703,1090,115,72))
	for entry in [[Vector2(1820,2100),Vector2(97,139)],[Vector2(2660,1127),Vector2(97,148)]]:
		art("infrastructure/walkway.png",entry[0],entry[1],detail)
	var props := group("SalvageAndRuins",structures);props.y_sort_enabled=true
	for point in [Vector2(1175,1655),Vector2(1400,1500),Vector2(1810,1910),Vector2(2130,2260),Vector2(2450,2100),Vector2(2870,1910),Vector2(3120,1820),Vector2(2510,1220),Vector2(2870,1020),Vector2(1580,975),Vector2(1840,945),Vector2(3250,530)]:
		art("infrastructure/scrap.png",point,Vector2(85,44),props,.10);solid(point,Vector2(43,24),props)
		art("terrain/metal_repair.png",point+Vector2(13,21),Vector2(71,47),detail,.13).modulate=Color(.72,.76,.62,.7)
	for path in routes:
		for i in range(path.size()-1):
			var delta := path[i+1]-path[i];var count := ceili(delta.length()/96)
			for j in range(count):
				var at := path[i].lerp(path[i+1],(j+.5)/count)
				art("terrain/market_dirt.png",at,Vector2(101,88),detail,delta.angle()).modulate=Color(.52,.64,.50,.33)
				if j%2==0:art("generated/props/pipe.png",at+delta.normalized().orthogonal()*68,Vector2(91,25),detail,delta.angle()).modulate=Color(.70,.80,.73,.91)
	for point in [Vector2(1390,1595),Vector2(1800,1990),Vector2(2190,2160),Vector2(2910,1780),Vector2(2760,1220),Vector2(1800,1070),Vector2(3100,595),Vector2(2090,1470)]:lamp(point,point.x>2600)
	for point in [Vector2(1670,1060),Vector2(1850,1140),Vector2(2280,1800)]:art("reconstruction/fundo_wall.png",point,Vector2(143,66),props,.1);solid(point,Vector2(81,31),props)
	world.set_meta("water_polygons",waters);world.set_meta("water_samples",water_samples)
	add_accesses(world,false)
	var surface: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();surface.set_script(null)
	var player: CharacterBody2D=surface.get_node("Structures/Player").duplicate();player.position=Vector2(1296,1572);structures.add_child(player);surface.free()
	var camera: Camera2D=player.get_node("Camera");camera.limit_left=800;camera.limit_right=3600;camera.limit_top=250;camera.limit_bottom=2580;camera.zoom=Vector2(.9,.9)
	var modulation := CanvasModulate.new();modulation.color=Color(.85,.90,.87);world.add_child(modulation)
	var hud := CanvasLayer.new();hud.name="HUD";world.add_child(hud);var label := Label.new();label.text="FUNDO-FERRO · WASD / Shift · F nos acessos · R retornar à chegada";label.position=Vector2(18,15);hud.add_child(label)
	world.set_meta("status","first underground stage built; validation pending");world.set_script(load("res://scripts/world/fundo_ferro.gd"))
	var error := save(world,"res://maps/fundo_ferro/fundo_ferro.tscn");print("FUNDO layer saved=",error," floor=",floor.get_used_cells().size()," rooms=7 routes=8");assert(error==OK)
func run() -> void:
	var check: Node=load("res://maps/sucateia/sucateia.tscn").instantiate()
	var already_built := check.has_node("LayerEntrances");check.free()
	if already_built:push_error("Layer already built; use the current scene for further refinement, not this initial generator");quit(1);return
	build()
	var surface: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();surface.set_script(null);root.add_child(surface)
	if surface.has_node("LayerEntrances"):push_error("Surface layer access already exists; do not replay generator");quit(1);return
	add_accesses(surface,true);surface.set_meta("world_layer","surface")
	surface.get_node("ForjasRasasDistrict/FutureExits/ManutencaoFundoFerro").set_meta("status","connected underground service access; F in proximity")
	surface.set_script(load("res://scripts/world/sucateia.gd"));var error := save(surface,"res://maps/sucateia/sucateia.tscn");print("FUNDO surface accesses saved=",error);quit(error)
