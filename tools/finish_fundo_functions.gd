extends SceneTree
var world: Node2D
var detail: Node2D
var architecture: Node2D
func _initialize() -> void:call_deferred("run")
func art(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://assets/"+file);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func foundation(point: Vector2, size: Vector2, dirty: bool=false) -> void:
	art("terrain/foundation.png",point,size,detail).modulate=Color(.57,.62,.56,.85)
	art("terrain/market_dirt.png",point+Vector2(5,8),size*1.17,detail).modulate=Color(.26,.32,.23,.52) if dirty else Color(.24,.30,.29,.30)
func pipe(label: String, points: PackedVector2Array, width: float=21) -> void:
	var network := Node2D.new();network.name=label;network.set_meta("connected_points",points);network.set_meta("low_floor_conduit",true);detail.add_child(network)
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i];var count := maxi(1,ceili(delta.length()/75))
		for j in range(count):
			var point := points[i].lerp(points[i+1],(j+.5)/count)
			art("generated/props/pipe.png",point,Vector2(delta.length()/count+5,width),network,delta.angle()).modulate=Color(.77,.87,.80)
	for point in points:
		art("generated/props/pipe.png",point,Vector2(width+5,width),network).modulate=Color(.61,.76,.68)
func remains(label: String, point: Vector2, file: String, size: Vector2, solid_size: Vector2) -> void:
	var node := Node2D.new();node.name=label;node.position=point;architecture.add_child(node)
	foundation(point+Vector2(0,12),Vector2(size.x*.90,size.y*.77),true)
	art("fx/light.svg",point+Vector2(0,17),Vector2(size.x,size.y*.6),detail).modulate=Color(0,0,0,.65)
	art(file,Vector2(0,-size.y*.26),size,node)
	var body := StaticBody2D.new();body.position=Vector2(0,-size.y*.26);var collision := CollisionShape2D.new();var shape := RectangleShape2D.new();shape.size=solid_size;collision.shape=shape;body.add_child(collision);node.add_child(body)
func residue(point: Vector2, size: Vector2, angle: float=0) -> void:
	art("terrain/market_dirt.png",point,size*1.3,detail,angle).modulate=Color(.33,.27,.15,.61)
	art("infrastructure/scrap.png",point,size,detail,angle).modulate=Color(.72,.71,.61)
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	world=load("res://maps/fundo_ferro/fundo_ferro.tscn").instantiate();world.set_script(null);root.add_child(world)
	if world.has_node("FunctionalGroundFinish"):
		world.queue_free();await process_frame;print("FUNDO functional finish already present; no historical replay");quit(0);return
	# Old short, unconnected pipes are removed; foundations and approved architecture remain.
	var old_detail: Node2D=world.get_node("GroundIntegration")
	for node in old_detail.get_children():
		if node is Sprite2D and node.texture and node.texture.resource_path.ends_with("/pipe.png"):
			old_detail.remove_child(node);node.free()
	detail=Node2D.new();detail.name="FunctionalGroundFinish";detail.z_index=-13;world.add_child(detail)
	architecture=Node2D.new();architecture.name="FunctionalRoomMargins";architecture.y_sort_enabled=true;world.get_node("Structures").add_child(architecture)
	# Wet intake starts at cistern, feeds pumps, then discharges into both blocked basins.
	pipe("CisternaBombas",PackedVector2Array([Vector2(1420,1438),Vector2(1505,1438),Vector2(1505,1905),Vector2(1595,1905)]),23)
	pipe("BombaBaciaOeste",PackedVector2Array([Vector2(1595,1905),Vector2(1728,1905),Vector2(1728,2092)]),25)
	pipe("BombaBaciaLeste",PackedVector2Array([Vector2(1595,1950),Vector2(1660,1950),Vector2(1660,2024),Vector2(1912,2024),Vector2(1912,2092)]),19)
	# Service conduit continues across the sorting room to the abandoned engine.
	pipe("BombasTriagemMotor",PackedVector2Array([Vector2(1912,2024),Vector2(2030,2024),Vector2(2030,2270),Vector2(2400,2270),Vector2(2570,2270),Vector2(2570,2100),Vector2(2810,2100),Vector2(2810,1605),Vector2(3050,1605)]),17)
	pipe("MotorReservatorio",PackedVector2Array([Vector2(3050,1605),Vector2(3110,1605),Vector2(3110,1520),Vector2(2800,1520),Vector2(2800,1195),Vector2(2748,1195),Vector2(2748,1128)]),22)
	pipe("ReservatorioEntrada",PackedVector2Array([Vector2(2576,1128),Vector2(2576,1008),Vector2(2660,1008),Vector2(2660,970),Vector2(3120,970),Vector2(3120,650),Vector2(3180,650)]),22)
	pipe("ValvulasDistribuicao",PackedVector2Array([Vector2(3180,650),Vector2(3290,650),Vector2(3290,500),Vector2(3140,500)]),16)
	pipe("RecalquePoco",PackedVector2Array([Vector2(1420,1438),Vector2(1380,1438),Vector2(1380,1405),Vector2(1170,1405),Vector2(1170,1515)]),16)
	# Rock masonry and iron containment visibly frame the water, with wet aprons.
	for entry in [[Vector2(1728,2058),96],[Vector2(1912,2058),96],[Vector2(2578,1078),77],[Vector2(2760,1078),115]]:
		art("infrastructure/retaining_edge.png",entry[0],Vector2(entry[1]+18,62),detail)
		art("terrain/market_dirt.png",entry[0]+Vector2(0,43),Vector2(entry[1]+38,80),detail).modulate=Color(.20,.38,.28,.65)
	# Metal working aprons stop the machinery looking like a loose sprite on stone.
	for entry in [[Vector2(1595,1985),Vector2(236,145)],[Vector2(3050,1680),Vector2(349,166)],[Vector2(3180,700),Vector2(189,121)],[Vector2(1420,1480),Vector2(185,113)]]:
		foundation(entry[0],entry[1]);art("terrain/metal_repair.png",entry[0]+Vector2(0,45),Vector2(entry[1].x*.75,86),detail).modulate=Color(.77,.78,.66,.83)
	for point in [Vector2(2930,1668),Vector2(3170,1668)]:art("infrastructure/retaining_edge.png",point,Vector2(64,55),detail)
	# Triage hugs the lower perimeter. A worn working aisle passes in front of bins.
	remains("BancadaDeTriagem",Vector2(2190,2318),"reconstruction/fundo_sorting_bank.png",Vector2(278,111),Vector2(250,51))
	for entry in [[Vector2(2075,2265),Vector2(101,52),-.11],[Vector2(2050,2310),Vector2(125,61),.2],[Vector2(2490,2315),Vector2(112,51),.1]]:residue(entry[0],entry[1],entry[2])
	for point in [Vector2(2160,2255),Vector2(2280,2245),Vector2(2390,2225)]:
		art("terrain/metal_repair.png",point,Vector2(113,71),detail,.04).modulate=Color(.87,.75,.55,.79)
	# Broken foundation remnants frame a real route between collapsed margins.
	remains("FundacaoDesabadaOeste",Vector2(1600,963),"reconstruction/fundo_collapsed_corner.png",Vector2(211,126),Vector2(146,53))
	remains("FundacaoDesabadaSul",Vector2(1888,1185),"reconstruction/fundo_collapsed_corner.png",Vector2(167,103),Vector2(118,42))
	for entry in [[Vector2(1590,1005),Vector2(93,43),.14],[Vector2(1840,1203),Vector2(114,48),-.14],[Vector2(1880,892),Vector2(104,41),.18]]:residue(entry[0],entry[1],entry[2])
	# Reinforced wall groups break uniform trim at meaningful corners/service zones.
	for entry in [[Vector2(1080,1480),Vector2(110,57),PI/2],[Vector2(1770,1806),Vector2(126,60),0],[Vector2(2280,2365),Vector2(159,68),0],[Vector2(3140,1992),Vector2(132,70),0],[Vector2(2900,1342),Vector2(115,57),0],[Vector2(3260,431),Vector2(124,65),0]]:
		art("infrastructure/retaining_edge.png",entry[0],entry[1],detail,entry[2]).modulate=Color(.71,.80,.73)
	# Low, flush service plates allow safe crossing over floor conduits.
	for point in [Vector2(1505,1738),Vector2(1820,2024),Vector2(2660,1008),Vector2(2810,1850),Vector2(3000,970)]:
		art("terrain/metal_repair.png",point,Vector2(73,62),detail).modulate=Color(.73,.77,.65)
	var material := ShaderMaterial.new();material.shader=load("res://assets/reconstruction/fundo_functional_ground.gdshader")
	material.set_shader_parameter("metal",load("res://assets/terrain/metal_repair.png"));material.set_shader_parameter("dirt",load("res://assets/terrain/market_dirt.png"));world.get_node("GroundFloor").material=material
	world.set_meta("functional_finish","connected wet/industrial networks; triage and ruined foundation margins; seven differentiated rooms; validation pending")
	world.set_script(load("res://scripts/world/fundo_ferro.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/fundo_ferro/fundo_ferro.tscn")
	print("FUNDO functional finish saved=",error," networks=8; no floor or surface expansion");quit(error)
