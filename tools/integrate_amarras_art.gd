extends "res://tools/build_amarras_geography.gd"
var catalog: Dictionary={}
var machines: Dictionary={}
var connections: Node2D
func selected(label: String,parent: Node,point: Vector2,opacity: float=1.) -> Sprite2D:
	var entry: Dictionary=catalog[label];var sprite := Sprite2D.new();sprite.name=label;sprite.texture=load("res://"+entry.path);sprite.scale=Vector2.ONE*float(entry.recommended_scale_from_canvas);sprite.position=point;sprite.modulate.a=opacity;parent.add_child(sprite);sprite.set_meta("selection_sha256",entry.sha256);return sprite
func machine(label: String,asset: String,point: Vector2,solid: bool=true) -> Node2D:
	var node := group(label,structures);node.position=point;node.set_meta("asset",asset)
	var entry: Dictionary=catalog[asset];var box: Array=entry.footprint_native_floor_bbox_estimated;var scale: float=entry.recommended_scale_from_canvas
	var sprite := selected(asset,node,Vector2.ZERO);sprite.position.y=-(float(box[3])-sprite.texture.get_height()*.5)*scale
	var base := Rect2(Vector2(float(box[0]),float(box[1])),Vector2(float(box[2])-float(box[0]),float(box[3])-float(box[1])))
	var center := (base.get_center()-Vector2(sprite.texture.get_size())*.5)*scale+sprite.position
	node.set_meta("base_center",center);node.set_meta("base_size",base.size*scale)
	if solid:
		var body := StaticBody2D.new();body.name="PhysicalBase";var shape := CollisionShape2D.new();var rectangle := RectangleShape2D.new();rectangle.size=base.size*scale*.90;shape.shape=rectangle;shape.position=center;body.add_child(shape);node.add_child(body)
	var ports := group("Ports",node)
	for data in entry.connections_native_pixels_estimated:marker(data.id,sprite.position+(Vector2(data.x,data.y)-Vector2(sprite.texture.get_size())*.5)*scale,ports)
	var foot := point+Vector2(center.x,0)
	for side in [-1,0,1]:
		art("terrain/metal_repair.png",foot+Vector2(side*base.size.x*scale*.29,-2),Vector2(base.size.x*scale*.32,22),detail).modulate=Color(.65,.56,.41,.70)
		art("fx/light.svg",foot+Vector2(side*base.size.x*scale*.29+3,4),Vector2(base.size.x*scale*.34,16),detail).modulate=Color(0,0,0,.60)
	selected("damp_anchor_runoff_decal_stains",detail,foot+Vector2(8,31),.19)
	machines[label]=node;return node
func port(label: String,terminal: String) -> Vector2:return machines[label].get_node("Ports/"+terminal).global_position
func link(label: String,a_name: String,a_port: String,b_name: String,b_port: String,sag: float=8.) -> void:
	var a := port(a_name,a_port);var b := port(b_name,b_port);var delta := b-a
	var node := group(label,connections);node.set_meta("from_node",a_name);node.set_meta("from_port",a_port);node.set_meta("to_node",b_name);node.set_meta("to_port",b_port);node.set_meta("endpoints",PackedVector2Array([a,b]));node.set_meta("sag",sag)
	# Small shaded forged links continue the generated shackles; no opaque technical bars.
	var count := ceili(delta.length()/8.)
	for i in range(count+1):
		var t: float=float(i)/count;var at := a.lerp(b,t)+Vector2(0,sin(t*PI)*sag)
		var angle := (delta+Vector2(0,cos(t*PI)*sag*PI)).angle()
		for layer in range(3):
			var line := Line2D.new();line.width=2.8 if layer==0 else 1.5;line.default_color=[Color(.035,.025,.016,.9),Color(.25,.15,.065),Color(.51,.36,.18)][layer];line.antialiased=true
			var points := PackedVector2Array()
			for j in range(13):
				var phase := float(j)*TAU/12.;var radius_y := 2.9 if i%2==0 else 1.15;points.append(at+Vector2(cos(phase)*5.1,sin(phase)*radius_y).rotated(angle)+Vector2(0,1.5 if layer==0 else (-.5 if layer==2 else 0.)))
			line.points=points;node.add_child(line)
func wear_path(points: PackedVector2Array) -> void:
	for i in range(points.size()-1):
		var a: Vector2=points[i];var b: Vector2=points[i+1];var count := maxi(1,ceili(a.distance_to(b)/190.))
		for j in range(count):
			var sprite := selected("chain_drag_wear_decal_marks",detail,a.lerp(b,(j+.5)/count),.26);sprite.rotation=(b-a).angle()
func align_reused() -> void:
	for node in structures.get_children():
		if node.has_meta("asset"):continue
		for sprite in node.get_children():
			if not sprite is Sprite2D:continue
			var pixels: Image=sprite.texture.get_image();pixels.resize(128,128,Image.INTERPOLATE_LANCZOS);var bottom := 0
			for y in range(128):
				for x in range(128):
					if pixels.get_pixel(x,y).a>.35:bottom=maxi(bottom,y)
			sprite.position.y=-(float(bottom)/128.-.5)*sprite.texture.get_height()*sprite.scale.y
			art("fx/light.svg",node.position+Vector2(3,4),Vector2(95,21),detail).modulate=Color(0,0,0,.5)
func run() -> void:
	var data: Array=JSON.parse_string(FileAccess.get_file_as_string("res://assets/reconstruction/amarras_parallel/manifest.json"))
	for entry in data:
		if FileAccess.get_sha256("res://"+entry.path)!=entry.sha256:push_error("Amarras selection hash mismatch "+entry.name);quit(1);return
		catalog[entry.name]=entry
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("PassagemAmarrasDistrict");structures=world.get_node("Structures/AmarrasInfrastructure")
	if district.has_node("ArtIntegration"):
		if not "--revise-amarras-art" in OS.get_cmdline_user_args():world.queue_free();await process_frame;print("AMARRAS selected art retained");quit(0);return
		district.get_node("ArtIntegration").free();district.get_node("FunctionalChains").free()
		for node in structures.get_children():
			if node.has_meta("asset") or node.has_meta("amarras_finish"):node.free()
	detail=group("ArtIntegration",district,-13);connections=group("FunctionalChains",district,-10)
	machine("TorreDeTensao","tension_anchor_tower_margin",Vector2(4470,100))
	machine("GuinchoDeTracao","chain_winch_station",Vector2(4210,540))
	machine("DistribuidorMecanico","chain_routing_hub",Vector2(4520,510))
	machine("PostoDeControle","technical_control_kiosk_complete",Vector2(5130,235))
	var platform := machine("PlataformaDeTransferencia","cargo_tiedown_platform",Vector2(4700,465),false);platform.z_index=-11
	for data_point in [["AncoragemDaCarga",Vector2(4060,-10)],["AncoragemDaPonte",Vector2(4025,295)],["ContraforteDeTensao",Vector2(4310,-60)],["ContraforteDeRetorno",Vector2(4570,130)],["RetencaoDoGuincho",Vector2(4110,545)],["ApoioDoCanal",Vector2(5030,868)],["ApoioDaInspecao",Vector2(5300,838)],["AmarraDaSaida",Vector2(5390,610)],["RetencaoDaCarga",Vector2(4930,335)]]:machine(data_point[0],"edge_anchor_buttress",data_point[1])
	link("TensaoOeste","ContraforteDeTensao","chain_e_upper","TorreDeTensao","chain_w",9.)
	link("TensaoLeste","TorreDeTensao","chain_e","ContraforteDeRetorno","chain_e_lower",5.)
	link("GuinchoRetido","RetencaoDoGuincho","chain_e_lower","GuinchoDeTracao","chain_in_w",2.)
	link("GuinchoDistribuidor","GuinchoDeTracao","chain_out_e","DistribuidorMecanico","chain_w",4.)
	link("DistribuidorCarga","DistribuidorMecanico","chain_e","PlataformaDeTransferencia","tie_sw",6.)
	link("CargaRetida","PlataformaDeTransferencia","tie_ne","RetencaoDaCarga","chain_e_lower",6.)
	# Quays contain niches and inspection supports rather than a smooth enclosing ring.
	for label in ["AncoragemDaCarga","AncoragemDaPonte","ContraforteDeTensao","ApoioDoCanal","ApoioDaInspecao"]:
		var join := port(label,"wall_join_n");art("infrastructure/retaining_edge.png",join+Vector2(0,8),Vector2(77,38),detail).modulate=Color(.69,.72,.61)
	for point in [Vector2(3980,-55),Vector2(3975,327),Vector2(5145,758),Vector2(5380,792)]:
		art("infrastructure/walkway.png",point,Vector2(110,71),detail,PI/2).modulate=Color(.76,.80,.70)
		for side in [-1,1]:art("infrastructure/coastal_wall.png",point+Vector2(side*39,21),Vector2(33,51),detail).modulate=Color(.65,.70,.59)
	for label in ["EntradaDasForjas","ViaDeTransferencia","RamalDeCarga"]:wear_path(district.get_node("Routes/"+label).get_meta("points"))
	for point in [Vector2(4220,23),Vector2(4410,158),Vector2(4600,270),Vector2(4965,365),Vector2(5230,480),Vector2(5470,565)]:
		art("terrain/metal_repair.png",point,Vector2(126,66),detail,.10 if int(point.x)%3==0 else -.07).modulate=Color(.74,.67,.53,.69)
	for point in [Vector2(4030,325),Vector2(4250,713),Vector2(4800,829),Vector2(5180,812)]:selected("damp_anchor_runoff_decal_stains",detail,point,.23)
	var soot := art("reconstruction/forjas_parallel/complement_v1/transition_soot_decal.png",Vector2(4010,0),Vector2(260,128),detail);soot.modulate.a=.13
	# Reused small cargo, lamps and reinforced margins establish functions without a new building family.
	for point in [Vector2(4670,414),Vector2(4725,417)]:art("props/crate.svg",point-platform.position,Vector2(27,27),platform).z_index=1
	art("props/crate.svg",Vector2(5360,772),Vector2(27,27),detail)
	for point in [Vector2(4650,497),Vector2(4760,502)]:selected("chain_drag_wear_decal_marks",detail,point,.34)
	for point in [Vector2(4160,130),Vector2(4590,242),Vector2(5000,410),Vector2(5330,640)]:
		art("infrastructure/lantern.png",point,Vector2(38,65),detail)
		art("fx/light.svg",point+Vector2(0,22),Vector2(92,62),detail).modulate=Color(.80,.47,.15,.10)
	for data_point in [["BancadaDeInspecao",Vector2(4580,652)],["ReparosDeTransito",Vector2(5240,418)]]:
		module(data_point[0],"reconstruction/forjas_parallel/complement_v1/maintenance_bench_cluster.png",data_point[1],Vector2(160,93),Vector2(105,28));structures.get_node(data_point[0]).set_meta("amarras_finish",true)
	module("ReservaDeCarga","reconstruction/forjas_parallel/ore_storage_cart.png",Vector2(5340,660),Vector2(148,99),Vector2(119,35));structures.get_node("ReservaDeCarga").set_meta("amarras_finish",true)
	align_reused()
	district.set_meta("stage","eight selected assets integrated; route and visual QA pending");district.set_meta("selected_asset_count",catalog.size());detail.set_meta("scope","measured contact footprints, tension/transfer nodes, wear and industrial margin inspection")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("AMARRAS final selections saved=",error," assets=",catalog.size()," chains=",connections.get_child_count()," approved city unchanged")
	world.queue_free();world=null;district=null;detail=null;structures=null;connections=null;machines.clear();packed=null;await process_frame;await process_frame;quit(error)

