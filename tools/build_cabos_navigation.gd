extends "res://tools/build_amarras_geography.gd"
var decks: Array[PackedVector2Array]=[]
func walkway(label: String,a: Vector2,b: Vector2,width: float) -> void:
	var side := (b-a).normalized().orthogonal()*width*.5;decks.append(PackedVector2Array([a-side,b-side,b+side,a+side]))
	var node := marker(label,Vector2.ZERO,district.get_node("Routes"));node.set_meta("points",PackedVector2Array([a,b]));node.set_meta("clear_width",width)
func landing(label: String,point: Vector2) -> void:
	decks.append(rect(point-Vector2(54,50),point+Vector2(54,50)));marker(label,point,district.get_node("Landings"))
func access(label: String,ground: Vector2,upper: Vector2) -> void:
	var node := group(label,district.get_node("Accesses"));node.set_script(load("res://scripts/world/cabos_access.gd"));node.set_meta("surface_arrival",ground);node.set_meta("elevated_arrival",upper)
	var prompt := Label.new();prompt.name="Prompt";prompt.visible=false;prompt.z_index=15;prompt.add_theme_font_size_override("font_size",14);node.add_child(prompt);landing(label,upper)
	# Two visible original flights, with a landing; no stretched ladder or public access via maintenance tower.
	var upper_port := Vector2(140,31);var lower_port := Vector2(141,189);var dimensions := Vector2(288,220);var scale := .65
	for i in range(2):
		var bottom := ground+Vector2(0,-102.7*i);var center := bottom-(lower_port-dimensions*.5)*scale
		art("infrastructure/stairs.png",center,dimensions*scale,district.get_node("ElevatedDecks"))
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	if world.has_node("CabosDistrict"):world.queue_free();await process_frame;print("CABOS navigation retained");quit(0);return
	district=group("CabosDistrict",world);district.set_script(load("res://scripts/world/cabos_district.gd"));group("Routes",district);group("Landings",district);group("Accesses",district);group("ElevatedDecks",district,6)
	access("AltoLixo",Vector2(-400,-780),Vector2(-400,-992));access("Mercado",Vector2(744,-504),Vector2(744,-716));access("Forjas",Vector2(1900,108),Vector2(1900,-104))
	walkway("ViaOeste",Vector2(-400,-992),Vector2(220,-992),80);walkway("DescidaDeDistribuicao",Vector2(-151,-992),Vector2(-151,-420),80)
	walkway("ViaPrincipal",Vector2(-151,-420),Vector2(1640,-420),80);walkway("ColunaDasForjas",Vector2(1640,-420),Vector2(1640,-104),80);walkway("ChegadaDasForjas",Vector2(1640,-104),Vector2(1900,-104),80)
	walkway("RamalMercado",Vector2(744,-716),Vector2(744,-522.2),36);walkway("EncontroT",Vector2(469.64,-522.2),Vector2(1016.84,-522.2),32)
	walkway("LigacaoTOeste",Vector2(469.64,-522.2),Vector2(469.64,-420),74);walkway("LigacaoTLeste",Vector2(1016.84,-522.2),Vector2(1016.84,-420),74)
	# Secondary bridge follows its actual sag, leaving the broad main lane as an alternative.
	var bridge := PackedVector2Array([Vector2(220,-992),Vector2(310,-982),Vector2(410,-975),Vector2(510,-975),Vector2(650,-983),Vector2(751.7,-992)])
	for i in range(bridge.size()-1):walkway("PonteSecundaria%d"%i,bridge[i],bridge[i+1],28)
	walkway("InspecaoNorte",Vector2(751.7,-992),Vector2(744,-716),74)
	for point in [Vector2(-151,-992),Vector2(-151,-420),Vector2(220,-992),Vector2(751.7,-992),Vector2(469.64,-420),Vector2(1016.84,-420),Vector2(1640,-420),Vector2(1640,-104)]:landing("Patamar%d"%int(point.x+point.y),point)
	district.set_meta("walk_polygons",decks);district.set_meta("stage","navigation first; broad east-west deck art pending, no final visual claim")
	# Merge continuous floor sections; the outer boundary and hole boundaries block only elevated characters.
	var outline := decks[0]
	var pending: Array[PackedVector2Array]=decks.duplicate();pending.remove_at(0);var boundaries: Array[PackedVector2Array]=[]
	for iteration in range(40):
		var progress := false
		for i in range(pending.size()-1,-1,-1):
			var merged := Geometry2D.merge_polygons(outline,pending[i])
			if merged.size()==1:outline=merged[0];pending.remove_at(i);progress=true
		if not progress:break
	boundaries.append(outline);boundaries.append_array(pending)
	var guards := group("ElevatedGuards",district)
	for boundary in boundaries:
		var body := StaticBody2D.new();body.collision_layer=4;body.collision_mask=2;guards.add_child(body)
		var shape := CollisionPolygon2D.new();shape.build_mode=CollisionPolygon2D.BUILD_SEGMENTS;shape.polygon=boundary;body.add_child(shape)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("CABOS navigation saved=",error," routes=",district.get_node("Routes").get_child_count()," accesses=3; same city; surface unchanged")
	world.queue_free();world=null;district=null;packed=null;await process_frame;await process_frame;quit(error)
