extends "res://tools/correct_forjas_direction.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("ForjasRasasDistrict")
	if district.has_node("LoadingStopsFinish"):world.queue_free();await process_frame;print("FORJAS local logistics finish preserved");quit(0);return
	detail=Node2D.new();detail.name="LoadingStopsFinish";detail.z_index=-12;district.add_child(detail)
	# Small stopping aprons connect existing ore stock and foundry hoist to their lanes.
	# The gaps between plates remain open; there are no new collision obstacles.
	for data in [[Vector2(2490,92),Vector2(2490,145)],[Vector2(2945,-805),Vector2(2970,-715)]]:
		var at: Vector2=data[0];var lane: Vector2=data[1];var delta := lane-at
		for side in [-1,1]:
			art("res://assets/terrain/metal_repair.png",at+Vector2(side*38,0),Vector2(49,26),detail,.035*side).modulate=Color(.68,.59,.43,.77)
			art("res://assets/terrain/market_dirt.png",at.lerp(lane,.5)+Vector2(side*19,0),Vector2(delta.length()+20,13),detail,delta.angle()).modulate=Color(.24,.21,.14,.48)
	art("res://assets/terrain/oil_hatch.png",Vector2(2787,-399),Vector2(64,39),detail,.07).modulate=Color(.46,.45,.32,.46)
	art("res://assets/terrain/market_dirt.png",Vector2(2642,-299),Vector2(72,37),detail).modulate=Color(.18,.25,.22,.38)
	detail.set_meta("scope","two unloading stops, localized maintenance oil and cooling moisture; no new buildings or territory")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("FORJAS short local finish saved=",error," existing foundations kept; two loading stops and localized residue")
	world.queue_free();world=null;district=null;detail=null;packed=null;await process_frame;await process_frame;quit(error)
