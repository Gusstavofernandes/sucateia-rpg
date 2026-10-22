extends "res://tools/integrate_docas_functions.gd"
const YARD = "reconstruction/docas_finish/workyard_platform.png"
func yard(label: String,center: Vector2,ratio: float,index: int) -> void:
	clean_prefix(painted,label+"Interior");clean_prefix(receivers,label+"Estaca")
	place(YARD,center,ratio,painted,label+"PatioRemendado")
	# Conservative floor contour follows the planks, excluding projecting piles.
	var contour := PackedVector2Array([Vector2(210,165),Vector2(465,165),Vector2(480,225),Vector2(745,225),Vector2(760,185),Vector2(1060,180),Vector2(1210,220),Vector2(1250,365),Vector2(1360,410),Vector2(1350,515),Vector2(1260,560),Vector2(1290,720),Vector2(1170,805),Vector2(415,805),Vector2(210,790),Vector2(170,650),Vector2(75,515),Vector2(90,395),Vector2(185,365)])
	for i in range(contour.size()):contour[i]=center+(contour[i]-Vector2(716,549))*ratio
	floors[index]=contour
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);district=world.get_node("DocasDistrict");floors.assign(district.get_meta("walk_polygons"));painted=district.get_node("WorkingDecks");receivers=district.get_node("WetSupports");architecture=world.get_node("Structures/DocasPortFunctions");contacts=district.get_node("PhysicalContacts");rigging=district.get_node("WorkingRopes")
	if district.has_meta("finish_refined"):world.free();quit(0);return
	yard("Triagem",Vector2(2510,1505),.30,18);yard("Reparo",Vector2(3030,1535),.28,19)
	# New dock corridors use clear planking, without cloned crates/rail ends at every join.
	for sprite in painted.get_children():
		if not sprite is Sprite2D:continue
		if sprite.texture.resource_path.ends_with("/main_deck_ew_wide.png"):
			var old_position: Vector2=sprite.position
			var was_pad: bool=sprite.region_enabled
			sprite.texture=load("res://assets/"+YARD);sprite.region_enabled=true
			sprite.region_rect=Rect2(400+int(old_position.x)%3*18,280,720,320);sprite.scale=Vector2.ONE*.235
			if not was_pad:sprite.position-=Vector2(.0705,9.949)
			sprite.modulate=Color(.83,.85,.80,1)
	# Ship-launch rails reach from the repair platform into the water; machinery, not a footbridge.
	var slip := place("reconstruction/docas_finish/naval_slipway.png",Vector2(3246.44,1567.60),.16,painted,"RampaNavalLeste")
	slip.set_meta("dry_socket_native",Vector2(75,300));slip.set_meta("dry_socket_world",Vector2(3105,1550));slip.set_meta("water_tip_native",Vector2(1810,440));slip.set_meta("use","launch rails for repair cradle; machinery apron, no pedestrian water shortcut")
	# Wet wood stays on wood; remove narrow-corridor spill and move the rest inward.
	for sprite in contacts.get_children():
		if sprite is Sprite2D and String(sprite.name).begins_with("Umidade"):
			match String(sprite.name):
				"Umidade3090":sprite.free()
				"Umidade2675":sprite.position=Vector2(2682,1923)
				"Umidade2885":sprite.position=Vector2(2890,1924)
				"Umidade3030":sprite.position=Vector2(3030,1640)
				"Umidade2500":sprite.position=Vector2(2510,1545)
	district.get_node("DeckBoundaries").free();district.set_meta("walk_polygons",floors);district.set_meta("boundary_segments",make_guards());district.set_meta("finish_refined",true);district.set_meta("stage","handcrafted dock yards and naval slipway integrated; final visual/physical review pending")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if packed.get_state().get_node_count()!=count_nodes(world):push_error("Dock finish omitted nodes");error=FAILED
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("DOCAS finish saved=",error," two new image-generated assets; contours follow floor; sources untouched")
	world.free();world=null;district=null;painted=null;receivers=null;architecture=null;contacts=null;rigging=null;packed=null;slip=null;quit(error)
