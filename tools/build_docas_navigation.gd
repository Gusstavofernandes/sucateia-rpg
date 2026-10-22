extends "res://tools/repair_cabos_navigation.gd"
var floors: Array[PackedVector2Array]=[]
var painted: Node2D
var receivers: Node2D
var route_count := 0
func inside(point: Vector2,polygons: Array) -> bool:
	var industrial: TileMapLayer=world.get_node("ForjasRasasDistrict/ForjasFloor")
	if industrial.get_cell_source_id(industrial.local_to_map(industrial.to_local(point)))!=-1:return true
	return super.inside(point,polygons)
func place(file: String,point: Vector2,ratio: float,parent: Node,label: String) -> Sprite2D:
	var node := Sprite2D.new();node.name=label;node.texture=load("res://assets/"+file);node.position=point;node.scale=Vector2.ONE*ratio;parent.add_child(node);return node
func strip(label: String,a: Vector2,b: Vector2,width: float) -> void:
	var side := (b-a).normalized().orthogonal()*width*.5;floors.append(PackedVector2Array([a-side,b-side,b+side,a+side]));var node := marker(label,Vector2.ZERO,district.get_node("Routes"));node.set_meta("points",PackedVector2Array([a,b]));node.set_meta("clear_width",width);route_count+=1
	var ew := absf(a.y-b.y)<1;var count := ceili(a.distance_to(b)/(165. if ew else 118.))
	for i in range(count):
		var point := a.lerp(b,(i+.5)/count)
		if ew:
			place("reconstruction/cabos_parallel/main_deck_ew_wide.png",point+Vector2(.0705,9.949),.14111610006414368,painted,"%s%02d"%[label,i])
		else:place("infrastructure/walkway.png",point+Vector2(.6,3.6),.6,painted,"%s%02d"%[label,i])
		# Wet, low stone/metal receivers below the deck, not tall aerial towers.
		if i%2==0 or i==count-1:place("infrastructure/coastal_wall.png",point+Vector2(0,51),.18,receivers,"%sContencao%02d"%[label,i])
func platform(label: String,bounds: Rect2,safe: Vector2=Vector2.INF) -> void:
	floors.append(rect(bounds.position,bounds.end));var columns := ceili(bounds.size.x/166.);var rows := ceili(bounds.size.y/68.)
	for row in range(rows):
		for col in range(columns):
			var point := bounds.position+Vector2((col+.5)*bounds.size.x/columns,(row+.5)*bounds.size.y/rows)
			var plank := place("reconstruction/cabos_parallel/main_deck_ew_wide.png",point,.14111610006414368,painted,"%sInterior%d_%d"%[label,col,row]);plank.region_enabled=true;plank.region_rect=Rect2(180,155,1230,535)
			plank.modulate=Color(.94+row*.015,.95+col*.015,.92+row*.015)
	for x in range(int(bounds.position.x)+45,int(bounds.end.x),88):place("infrastructure/coastal_wall.png",Vector2(x,bounds.end.y+20),.18,receivers,"%sEstaca%d"%[label,x])
	if safe!=Vector2.INF:marker(label,safe,district.get_node("SafeLandings"))
func make_guards() -> int:
	var polygons: Array=floors.duplicate();polygons.append(world.get_node("LowerCoastReworked").get_meta("land_polygon"));var guards := group("DeckBoundaries",district);var body := StaticBody2D.new();body.name="OuterWaterGuards";body.collision_mask=2;guards.add_child(body);var count := 0
	for polygon in floors:
		for i in range(polygon.size()):
			var a: Vector2=polygon[i];var b: Vector2=polygon[(i+1)%polygon.size()];var delta := b-a;var cuts: Array[float]=[0.,1.]
			for other in polygons:
				for j in range(other.size()):
					var crossing: Variant=Geometry2D.segment_intersects_segment(a,b,other[j],other[(j+1)%other.size()])
					if crossing!=null:cuts.append(clampf((crossing-a).dot(delta)/delta.length_squared(),0.,1.))
			cuts.sort()
			for j in range(cuts.size()-1):
				if cuts[j+1]-cuts[j]<.0001:continue
				var p: Vector2=a+delta*cuts[j];var q: Vector2=a+delta*cuts[j+1];var middle := p.lerp(q,.5);var normal := delta.normalized().orthogonal()*.25
				if inside(middle+normal,polygons)==inside(middle-normal,polygons):continue
				var collision := CollisionShape2D.new();var segment := SegmentShape2D.new();segment.a=p;segment.b=q;collision.shape=segment;body.add_child(collision);count+=1
	return count
func count_nodes(node: Node) -> int:
	var count := 1
	for child in node.get_children():count+=count_nodes(child)
	return count
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null)
	if world.has_node("DocasDistrict"):print("DOCAS navigation retained; no replay");world.free();world=null;quit(0);return
	district=group("DocasDistrict",world);district.set_script(load("res://scripts/world/docas_district.gd"));group("Routes",district);group("Connections",district);group("SafeLandings",district);painted=group("WorkingDecks",district,-11);receivers=group("WetSupports",district,-12)
	for entry in [["NucleoUrbano",Vector2(2240,1330)],["RotaCosteira",Vector2(2210,1700)],["EixoTecnico",Vector2(3280,275)]]:marker(entry[0],entry[1],district.get_node("Connections"))
	strip("ChegadaUrbana",Vector2(2240,1330),Vector2(2350,1330),72);strip("ViaDosFardos",Vector2(2350,1330),Vector2(2350,1640),60);strip("CargaPrincipal",Vector2(2350,1640),Vector2(2920,1640),72)
	strip("RetornoCosteiro",Vector2(2210,1700),Vector2(2450,1700),72);strip("CostaInterna",Vector2(2450,1700),Vector2(2450,1910),60);strip("ChegadaDeEmbarque",Vector2(2450,1910),Vector2(2670,1910),72)
	strip("PierDeCarga",Vector2(2920,1640),Vector2(2920,1910),60);strip("CaisDeCarga",Vector2(2670,1910),Vector2(2920,1910),72)
	strip("TecnicoForjas",Vector2(3280,275),Vector2(3280,610),60);strip("RecuperacaoLeste",Vector2(3090,610),Vector2(3280,610),72);strip("TecnicoDrenagem",Vector2(3090,610),Vector2(3090,925),60);strip("DesvioDeSucata",Vector2(2840,925),Vector2(3090,925),72);strip("MargemDeServicos",Vector2(2840,925),Vector2(2840,1280),60);strip("ConexaoComTriagem",Vector2(2700,1280),Vector2(2840,1280),72);strip("ServicosPortuarios",Vector2(2700,1280),Vector2(2700,1640),60)
	strip("OficinaNaval",Vector2(2920,1640),Vector2(3030,1640),72);strip("PatioDeTriagem",Vector2(2500,1575),Vector2(2500,1640),60)
	platform("Entrada",Rect2(2275,1294,166,72),Vector2(2350,1330));platform("Triagem",Rect2(2360,1370,300,240),Vector2(2500,1575));platform("Reparo",Rect2(2880,1430,280,235),Vector2(3030,1640));platform("Embarque",Rect2(2530,1860,260,150),Vector2(2670,1910));platform("Tecnico",Rect2(3220,408,120,100),Vector2(3280,458))
	for point in [Vector2(2350,1640),Vector2(2920,1640),Vector2(2450,1700),Vector2(2450,1910),Vector2(2920,1910),Vector2(3280,610),Vector2(3090,610),Vector2(3090,925),Vector2(2840,925),Vector2(2840,1280),Vector2(2700,1280),Vector2(2700,1640)]:
		platform("Junta%d"%int(point.x+point.y),Rect2(point-Vector2(45,36),Vector2(90,72)))
	district.set_meta("walk_polygons",floors);district.set_meta("water_samples",PackedVector2Array([Vector2(2700,1780),Vector2(2800,1460),Vector2(3190,1200),Vector2(2380,1800),Vector2(2980,1970)]));district.set_meta("boundary_segments",make_guards());district.set_meta("stage","Docas circulation prototype; professional art finish pending")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if packed.get_state().get_node_count()!=count_nodes(world):push_error("Dock nodes omitted during packing");error=FAILED
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("DOCAS navigation saved=",error," route sections=",route_count," connections=3; approved water/coast nodes unchanged")
	world.free();world=null;district=null;painted=null;receivers=null;packed=null;quit(error)
