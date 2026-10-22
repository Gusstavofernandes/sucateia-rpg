extends SceneTree
var world: Node2D
var district: Node2D
var detail: Node2D
func _initialize() -> void:call_deferred("run")
func art(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> Sprite2D:
	var sprite := Sprite2D.new();sprite.texture=load("res://assets/"+file);sprite.position=point;sprite.scale=size/Vector2(sprite.texture.get_size());sprite.rotation=angle;parent.add_child(sprite);return sprite
func pipe(label: String, points: PackedVector2Array, width: float=23) -> void:
	var network := Node2D.new();network.name=label;network.set_meta("connected_points",points);network.set_meta("function","low service conduit between named production equipment");detail.add_child(network)
	for i in range(points.size()-1):
		var delta := points[i+1]-points[i];var count := maxi(1,ceili(delta.length()/79))
		for j in range(count):
			art("generated/props/pipe.png",points[i].lerp(points[i+1],(j+.5)/count),Vector2(delta.length()/count+6,width),network,delta.angle()).modulate=Color(.82,.85,.71)
	for point in points:art("generated/props/pipe.png",point,Vector2(width+4,width),network).modulate=Color(.75,.77,.61)
func apron(label: String, point: Vector2, size: Vector2, hot: bool=false) -> void:
	var node := Node2D.new();node.name=label;node.position=point;detail.add_child(node)
	art("terrain/market_dirt.png",Vector2(0,5),size*1.20,node,.06).modulate=Color(.26,.20,.12,.58) if hot else Color(.36,.33,.23,.45)
	art("terrain/foundation.png",Vector2.ZERO,size,node).modulate=Color(.49,.48,.39,.87)
	for i in range(3):art("terrain/metal_repair.png",Vector2((i-1)*size.x*.25,7+(i%2)*6),Vector2(size.x*.36,size.y*.64),node,.025*(i-1)).modulate=Color(.67,.58,.43,.86) if hot else Color(.71,.69,.55,.8)
func warmth(point: Vector2, size: float, energy: float) -> void:
	var light := PointLight2D.new();light.position=point;light.texture=load("res://assets/fx/light.svg");light.texture_scale=size/256.;light.energy=energy;light.color=Color("d98538");district.add_child(light)
	art("fx/light.svg",point,Vector2(size,size*.56),detail).modulate=Color(.74,.27,.05,.11)
func own(node: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("ForjasRasasDistrict")
	if district.has_node("IndustrialGroundFinish"):
		world.queue_free();await process_frame;print("FORJAS current finishing preserved; no generator replay");quit(0);return
	# Only isolated ground pipes within Forjas are replaced. Attached architecture pipes remain.
	for path in ["GroundIntegration","Drainage"]:
		var parent: Node=district.get_node(path)
		for sprite in parent.get_children():
			if sprite is Sprite2D and sprite.texture and sprite.texture.resource_path.ends_with("/pipe.png"):
				parent.remove_child(sprite);sprite.free()
	detail=Node2D.new();detail.name="IndustrialGroundFinish";detail.z_index=-13;district.add_child(detail)
	# Main pressure spine links boiler district, both foundries, machinery and drain outlets.
	pipe("CaldeirasFundicao",PackedVector2Array([Vector2(3050,-1382),Vector2(2910,-1382),Vector2(2910,-1140),Vector2(2700,-1140),Vector2(2700,-1040)]),28)
	pipe("CircuitoDosFornos",PackedVector2Array([Vector2(2700,-1040),Vector2(2700,-960),Vector2(2880,-960),Vector2(2880,-1020),Vector2(3170,-1020),Vector2(3170,-945)]),25)
	pipe("RecuperacaoTriagem",PackedVector2Array([Vector2(3170,-945),Vector2(3240,-945),Vector2(3240,-800),Vector2(3320,-800),Vector2(3320,-710),Vector2(3400,-710),Vector2(3400,-510),Vector2(3330,-510)]),22)
	pipe("ServicoFabricacao",PackedVector2Array([Vector2(2700,-960),Vector2(2600,-960),Vector2(2600,-582),Vector2(2530,-582),Vector2(2530,-440),Vector2(2950,-440),Vector2(2950,-350)]),23)
	pipe("DrenagemDasCaldeiras",PackedVector2Array([Vector2(2950,-350),Vector2(3020,-350),Vector2(3020,-45),Vector2(2860,-45),Vector2(2860,127)]),21)
	pipe("EntradaOficinas",PackedVector2Array([Vector2(2050,-275),Vector2(2050,-218),Vector2(1950,-218),Vector2(1950,-173),Vector2(1900,-173)]),24)
	pipe("ReparosEntrada",PackedVector2Array([Vector2(2050,-275),Vector2(2120,-275),Vector2(2120,-515),Vector2(2030,-515)]),19)
	pipe("ReparosCarga",PackedVector2Array([Vector2(2120,-515),Vector2(2250,-515),Vector2(2250,-345),Vector2(2450,-345),Vector2(2450,-190),Vector2(2520,-190),Vector2(2520,28)]),18)
	# Distinct uses: old street repairs, unloading/stock, fabrication, hot casting, sorting.
	apron("PatioDeCarga",Vector2(2500,-5),Vector2(323,169))
	apron("PisoDeForja",Vector2(2720,-916),Vector2(407,181),true)
	apron("PisoDeRecuperacao",Vector2(3170,-895),Vector2(290,128),true)
	apron("OficinaDeFabricacao",Vector2(2760,-495),Vector2(327,125))
	apron("TriagemDosRetalhos",Vector2(3420,-700),Vector2(237,117))
	apron("ReparosDaRua",Vector2(2040,-320),Vector2(213,111))
	for point in [Vector2(2600,-780),Vector2(3020,-150),Vector2(2250,-380),Vector2(2520,-110)]:
		art("terrain/metal_repair.png",point,Vector2(82,74),detail).modulate=Color(.78,.71,.53)
	# Strong heat remains near casting, a quieter glow marks entry and industrial service.
	warmth(Vector2(2700,-1030),292,.56);warmth(Vector2(3170,-975),202,.42);warmth(Vector2(2050,-290),168,.27)
	var floor: TileMapLayer=district.get_node("ForjasFloor");var material: ShaderMaterial=floor.material.duplicate()
	material.shader=load("res://assets/reconstruction/forjas_refined_ground.gdshader")
	material.set_shader_parameter("metal",load("res://assets/terrain/metal_repair.png"));material.set_shader_parameter("dirt",load("res://assets/terrain/market_dirt.png"));floor.material=material
	var anchors := Node2D.new();anchors.name="ArtIntegrationAnchors";district.add_child(anchors)
	for data in [["LandmarkMercado",Vector2(2050,-275)],["ForjaArtesanal",Vector2(1850,-8)],["EstoqueDeCarga",Vector2(2490,30)],["GuindasteFundicao",Vector2(2945,-925)],["CaldeiraDeServico",Vector2(2840,-1390)]]:
		var marker := Marker2D.new();marker.name=data[0];marker.position=data[1];anchors.add_child(marker)
	var exit := Marker2D.new();exit.name="CorredorParaOsCabos";exit.position=Vector2(3370,240);exit.set_meta("status","reserved approach only; Os Cabos not rebuilt");district.get_node("FutureExits").add_child(exit)
	district.set_meta("refinement","urban/industrial terrain progression; connected pressure and drain networks; work aprons; parallel art integration pending")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS refinement saved=",error," eight networks; five art anchors; four regional approaches; existing floor/architecture retained");quit(error)
