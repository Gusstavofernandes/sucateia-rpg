extends "res://tools/integrate_cabos_art.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("CabosDistrict");render=district.get_node("ElevatedDecks")
	if render.has_node("AcessoCasaDeck01"):
		print("CABOS painted porch retained; no replay");world.queue_free();world=null;district=null;render=null;await process_frame;await process_frame;quit(0);return
	var route_node: Node=district.get_node("Routes/AcessoCasa");var points: PackedVector2Array=route_node.get_meta("points");var center := points[0].lerp(points[1],.75)+Vector2(.6,3.6)
	var floor_node: Sprite2D
	if not render.has_node("AcessoCasaDeck01"):
		floor_node=sprite("infrastructure/walkway.png",center,.6,render,"AcessoCasaDeck01")
	root.remove_child(world)
	var copy: Node2D=world.duplicate(7)
	world.free();world=copy;root.add_child(world);world.set_script(null);district=world.get_node("CabosDistrict");render=district.get_node("ElevatedDecks");floor_node=render.get_node("AcessoCasaDeck01")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	var state := packed.get_state();var found := false
	for i in range(state.get_node_count()):
		if String(state.get_node_name(i))=="AcessoCasaDeck01":found=true
	if not found:push_error("Porch packing failed");error=FAILED
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("CABOS painted porch saved=",error," packed=",found,"; restore_cabos_scene_paths.py must restore generated paths after duplicate");world.queue_free();world=null;copy=null;district=null;render=null;route_node=null;floor_node=null;packed=null;state=null;await process_frame;await process_frame;quit(error)
