extends "res://tools/build_amarras_geography.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("PassagemAmarrasDistrict")
	outline=district.get_meta("land_polygon");var floor: TileMapLayer=district.get_node("AmarrasFloor");floor.clear()
	# Boundary cells cover the physical polygon. The shader clips exact edges, preventing dry/wet tile slivers.
	for y in range(-8,24):
		for x in range(80,120):
			var a := Vector2(x*48,y*48);var tile := rect(a,a+Vector2(48,48))
			if not Geometry2D.intersect_polygons(outline,tile).is_empty():floor.set_cell(Vector2i(x,y),0,Vector2i(posmod(x,16),posmod(y,16)))
	var segments: Array[Vector4]=[]
	for label in ["EntradaDasForjas","ViaDeTransferencia"]:
		var points: PackedVector2Array=district.get_node("Routes/"+label).get_meta("points")
		for i in range(points.size()-1):segments.append(Vector4(points[i].x,points[i].y,points[i+1].x,points[i+1].y))
	floor.material.set_shader_parameter("cargo_count",segments.size());floor.material.set_shader_parameter("cargo_segments",segments)
	# Fade the new sea overlay before approved Forjas coastline; its original water/shore material stays visible.
	district.get_node("AguaIndustrialContinua").material.shader=load("res://assets/reconstruction/amarras_sea.gdshader")
	district.set_meta("surface_finish","polygon-clipped boundary tiles; dominant worn cargo lane and quieter inspection circuit; approved coast protected by water fade")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("AMARRAS surface saved=",error," coverage cells=",floor.get_used_cells().size()," cargo segments=",segments.size()," no land contour or route changes")
	world.queue_free();world=null;district=null;floor=null;packed=null;await process_frame;await process_frame;quit(error)
