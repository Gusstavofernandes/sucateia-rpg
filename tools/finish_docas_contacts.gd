extends "res://tools/refine_docas_finish.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);district=world.get_node("DocasDistrict");architecture=world.get_node("Structures/DocasPortFunctions");contacts=district.get_node("PhysicalContacts");rigging=district.get_node("WorkingRopes");painted=district.get_node("WorkingDecks");receivers=district.get_node("WetSupports")
	if district.has_meta("working_contacts_finished"):world.free();quit(0);return
	var capstan: Sprite2D=architecture.get_node("Cabrestante/Artwork");var spool := capstan.to_global(Vector2(600,580)-Vector2(capstan.texture.get_size())*.5)
	var rope: Line2D=rigging.get_node("AmarraProa");var revised: PackedVector2Array=rope.points;revised.append(spool);rope.points=revised;rope.get_child(0).points=revised;rope.set_meta("real_endpoints",PackedVector2Array([revised[0],spool]));rope.set_meta("drum_native",Vector2(600,580))
	# Technical arrival now reads as a maintained pumping station, not an empty landing.
	object("BombaDaMargem","region/pump_station.png",Vector2(3280,415),.10,[Rect2(95,505,600,118)])
	var services := group("DocasServicePipes",district,-8);var utilities: RefCounted=load("res://scripts/world/connected_utilities.gd").new()
	utilities.straight(services,"EntradaDaBomba",Vector2(3243.5,417.8),Vector2(3243.5,295))
	utilities.elbow(services,"CotoveloNaMargem",Vector2(3243.5,295),Vector2(3268,275),true)
	var boat: Sprite2D=architecture.get_node("BarcacaAncorada/Artwork")
	var waterline := PackedVector2Array([Vector2(105,435),Vector2(330,640),Vector2(800,730),Vector2(1400,730),Vector2(1630,620)])
	for i in range(waterline.size()):waterline[i]=boat.to_global(waterline[i]-Vector2(boat.texture.get_size())*.5)+Vector2(0,2)
	var contact := Line2D.new();contact.name="CascoNaAgua";contact.points=waterline;contact.width=5;contact.default_color=Color(.015,.027,.024,.42);contact.antialiased=true;contacts.add_child(contact)
	var ripple := Line2D.new();ripple.name="MarolaIndustrial";ripple.points=waterline;ripple.position.y=4;ripple.width=1.3;ripple.default_color=Color(.25,.31,.25,.22);ripple.antialiased=true;contacts.add_child(ripple)
	# Cropped technical joints gain a real, asymmetric piled underside.
	for pair in [["Junta3890",Vector2(3280,610)],["Junta4015",Vector2(3090,925)],["Junta4120",Vector2(2840,1280)]]:
		clean_prefix(painted,pair[0]+"Interior");clean_prefix(receivers,pair[0]+"Estaca")
		place(YARD,pair[1]+Vector2(0,-6),.16,painted,pair[0]+"ApoioRemendado")
	district.set_meta("working_contacts_finished",true);district.set_meta("stage","Docas final contact finish integrated; physical regressions, stable captures and consultant review pending")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if packed.get_state().get_node_count()!=count_nodes(world):push_error("Dock contact nodes omitted");error=FAILED
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("DOCAS final contacts saved=",error," pump/feeder, true drum traction, hull waterline, piled technical joints")
	world.free();world=null;district=null;painted=null;receivers=null;architecture=null;contacts=null;rigging=null;packed=null;boat=null;capstan=null;rope=null;utilities=null;quit(error)
