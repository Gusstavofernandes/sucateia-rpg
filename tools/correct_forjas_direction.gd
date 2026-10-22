extends SceneTree
var world: Node2D
var district: Node2D
var detail: Node2D
var yards: Node2D
const ART := "res://assets/reconstruction/forjas_parallel/complement_v1/"
func _initialize() -> void:call_deferred("run")
func art(path: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load(path);sprite.position=point
	sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func extracted(file: String, bbox: Rect2, point: Vector2, size: Vector2, parent: Node) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load(ART+file)
	var ratio := minf(size.x/bbox.size.x,size.y/bbox.size.y)
	sprite.scale=Vector2.ONE*ratio;sprite.position=point+(Vector2(sprite.texture.get_size())*.5-bbox.get_center())*ratio
	parent.add_child(sprite);return sprite
func conduit(label: String, points: PackedVector2Array, width: float=22) -> void:
	var node := Node2D.new();node.name=label;node.set_meta("connected_points",points);detail.add_child(node)
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i];var count := maxi(1,ceili(delta.length()/79))
		for j in range(count):art("res://assets/generated/props/pipe.png",points[i].lerp(points[i+1],(j+.5)/count),Vector2(delta.length()/count+6,width),node,delta.angle()).modulate=Color(.88,.82,.68)
func yard(label: String, file: String, bbox: Rect2, point: Vector2, size: Vector2, base: Vector2) -> void:
	var node := Node2D.new();node.name=label;node.position=point;node.set_meta("footprint_center",point+Vector2(0,-28));node.set_meta("function",label);yards.add_child(node)
	extracted(file,bbox,Vector2(0,-size.y*.37),size,node)
	var body := StaticBody2D.new();body.position=Vector2(0,-28);var collision := CollisionShape2D.new();var shape := RectangleShape2D.new();shape.size=base;collision.shape=shape;body.add_child(collision);node.add_child(body)
	art("res://assets/terrain/foundation.png",point-Vector2(0,15),Vector2(size.x*1.14,base.y*1.75),detail).modulate=Color(.46,.42,.33,.85)
	art("res://assets/terrain/market_dirt.png",point+Vector2(0,6),Vector2(size.x*1.45,size.y*1.4),detail).modulate=Color(.24,.20,.14,.67)
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	for file in ["coal_feed_cluster.png","slag_discharge_cluster.png","cooling_trough_cluster_complete.png","maintenance_bench_cluster.png","transition_soot_decal.png","slag_spill_decal.png","exhaust_tower_addon.png","supported_pipe_connector.png","short_service_catwalk.png"]:
		if not ResourceLoader.exists(ART+file):push_error("Unimported production asset: "+file);quit(1);return
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("ForjasRasasDistrict")
	if district.has_node("ProductionDirectionFinish"):world.queue_free();await process_frame;print("FORJAS direction preserved; no replay");quit(0);return
	detail=Node2D.new();detail.name="ProductionDirectionFinish";detail.z_index=-12;district.add_child(detail)
	yards=Node2D.new();yards.name="ForjasProductionYards";yards.y_sort_enabled=true;world.get_node("Structures").add_child(yards)
	yard("BaiaDeCarvao","coal_feed_cluster.png",Rect2(205,126,1259,716),Vector2(2500,-1170),Vector2(225,125),Vector2(154,54))
	yard("DescarteDeEscoria","slag_discharge_cluster.png",Rect2(113,105,1287,832),Vector2(3545,-875),Vector2(230,135),Vector2(154,56))
	yard("TanqueDeResfriamento","cooling_trough_cluster_complete.png",Rect2(85,201,1460,587),Vector2(2730,-290),Vector2(195,115),Vector2(140,46))
	yard("BancadaDeManutencao","maintenance_bench_cluster.png",Rect2(90,82,1376,752),Vector2(2780,-475),Vector2(182,105),Vector2(126,42))
	# Feeding, cooling and discharge terminate at actual production equipment.
	conduit("AlimentacaoCarvao",PackedVector2Array([Vector2(2595,-1200),Vector2(2635,-1200),Vector2(2635,-1115),Vector2(2700,-1115)]),26)
	conduit("AlimentacaoResfriamento",PackedVector2Array([Vector2(2730,-315),Vector2(2730,-440),Vector2(2790,-440)]),23)
	conduit("RetornoResfriamento",PackedVector2Array([Vector2(2815,-300),Vector2(2860,-300),Vector2(2860,-45)]),20)
	conduit("DescargaRecuperacao",PackedVector2Array([Vector2(3320,-800),Vector2(3400,-800),Vector2(3400,-900),Vector2(3480,-900)]),24)
	conduit("ValvulaCanal",PackedVector2Array([Vector2(2860,110),Vector2(2860,155)]),29)
	# Supported sections replace open joins on continuous low service networks.
	for point in [Vector2(2660,-1115),Vector2(2780,-440),Vector2(3440,-900),Vector2(2860,-45),Vector2(2875,-1382),Vector2(2770,135)]:
		extracted("supported_pipe_connector.png",Rect2(247,171,1377,490),point,Vector2(86,34),detail)
	# Maintenance grates attach beside equipment and beside the drain, not across streets.
	for data in [[Vector2(2780,-535),Vector2(150,42)],[Vector2(2960,-1080),Vector2(150,42)],[Vector2(3045,95),Vector2(155,42)]]:
		extracted("short_service_catwalk.png",Rect2(84,273,1606,406),data[0],data[1],detail)
	# The existing central furnace retains its footprint and original sprite.
	var foundry: Node2D=world.get_node("Structures/ForjasIndustrialArchitecture/FundicaoDasCaldeiras")
	var tower := Node2D.new();tower.name="ExaustaoDaFundicao";foundry.add_child(tower)
	extracted("exhaust_tower_addon.png",Rect2(110,43,828,1443),Vector2(30,-425),Vector2(253,440),tower)
	var exhaust := CPUParticles2D.new();exhaust.name="ExaustaoAtiva";exhaust.position=Vector2(25,-643);exhaust.texture=load("res://assets/fx/smoke_01.png")
	exhaust.amount=14;exhaust.lifetime=4.;exhaust.preprocess=4.;exhaust.direction=Vector2(-.28,-1);exhaust.spread=19.;exhaust.gravity=Vector2(-3,-7);exhaust.initial_velocity_min=13;exhaust.initial_velocity_max=20
	exhaust.scale_amount_min=.12;exhaust.scale_amount_max=.26;exhaust.color=Color(.26,.24,.22,.20);tower.add_child(exhaust)
	var heat := PointLight2D.new();heat.name="ReflexoDaFundicao";heat.position=Vector2(2710,-910);heat.texture=load("res://assets/fx/light.svg");heat.texture_scale=1.5;heat.energy=.72;heat.color=Color("ed963f");district.add_child(heat)
	# Drain receives the real cooling return; peripheral service reinforces the coastline.
	conduit("ServicoDaBordaLeste",PackedVector2Array([Vector2(3480,-900),Vector2(3600,-900),Vector2(3600,-680)]),23)
	conduit("ServicoDaBordaSul",PackedVector2Array([Vector2(3330,-510),Vector2(3480,-510),Vector2(3480,-210),Vector2(3500,-210)]),22)
	for point in [Vector2(3570,-680),Vector2(3470,-210),Vector2(2910,115),Vector2(3110,95)]:
		art("res://assets/infrastructure/retaining_edge.png",point,Vector2(92,46),detail).modulate=Color(.68,.65,.51)
	for point in [Vector2(3600,-680),Vector2(3500,-210)]:
		extracted("supported_pipe_connector.png",Rect2(247,171,1377,490),point,Vector2(96,38),detail)
	# Decals form functional wear patches; no baked floor replaces the existing tile.
	for point in [Vector2(1880,-760),Vector2(2030,-325),Vector2(2075,24)]:
		extracted("transition_soot_decal.png",Rect2(113,184,1747,477),point,Vector2(330,100),detail).modulate=Color(1,1,1,.48)
	extracted("slag_spill_decal.png",Rect2(133,177,1357,684),Vector2(3540,-805),Vector2(285,155),detail).modulate=Color(.8,.7,.6,.65)
	# Cargo wheel wear follows the real diagonal street, leaving its center clear.
	var cargo := PackedVector2Array([Vector2(1800,-1040),Vector2(1990,-1280),Vector2(2310,-1280),Vector2(2420,-1130)])
	for i in range(cargo.size()-1):
		var delta := cargo[i+1]-cargo[i];var count := maxi(1,ceili(delta.length()/85))
		for j in range(count):
			var center := cargo[i].lerp(cargo[i+1],(j+.5)/count)
			for side in [-1,1]:art("res://assets/terrain/market_dirt.png",center+delta.orthogonal().normalized()*22*side,Vector2(94,16),detail,delta.angle()).modulate=Color(.18,.15,.10,.45)
	district.set_meta("direction_status","five productive functions, central exhaust add-on, supported service and coastal drainage; pending capture and navigation QA")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS production direction saved=",error," four yards, feeding/cooling/discharge and logistics wear; no territory change")
	world.queue_free();world=null;detail=null;yards=null;district=null;packed=null;await process_frame;await process_frame;quit(error)
