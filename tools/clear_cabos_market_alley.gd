extends "res://tools/integrate_cabos_art.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("CabosDistrict");supports=district.get_node("StructuralSupports");links=district.get_node("TensionAndMessages")
	if district.has_meta("market_alley_clear"):print("CABOS alley retained");world.queue_free();await process_frame;quit(0);return
	var tower: Sprite2D=supports.get_node("InspecaoNorteDeck02Tower");var old_foot: Vector2=tower.get_meta("ground_contact");var displacement := Vector2(110,95);var old_crown := tower.position+(Vector2(370,138)-Vector2(384,384))*.4
	tower.position+=displacement;tower.set_meta("ground_contact",old_foot+displacement)
	for child in supports.get_children():
		if child is StaticBody2D and child.position.distance_to(old_foot)<.1:child.position+=displacement
	district.get_node("ContactShadows/InspecaoNorteDeck02TowerContact").position+=displacement
	for line in links.get_children():
		if not line is Line2D:continue
		var points: PackedVector2Array=line.points;var moved := false
		if points[0].distance_to(old_crown)<.2:points[0]+=displacement;moved=true
		if points[-1].distance_to(old_crown)<.2:points[-1]+=displacement;moved=true
		if moved:
			points[1]=points[0].lerp(points[-1],.5)+Vector2(0,6);line.points=points;line.set_meta("anchored_endpoints",PackedVector2Array([points[0],points[-1]]))
			for child in line.get_children():if child is Line2D:child.points=points
	district.set_meta("market_alley_clear",true)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("CABOS alley saved=",error," new inspection support moved clear of BecoDasFerragens")
	world.queue_free();world=null;district=null;supports=null;links=null;tower=null;packed=null;await process_frame;await process_frame;quit(error)
