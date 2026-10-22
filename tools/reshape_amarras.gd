extends "res://tools/build_amarras_geography.gd"
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	district=world.get_node("PassagemAmarrasDistrict");detail=district.get_node("GroundIntegration")
	if district.has_meta("passage_shape"):world.queue_free();await process_frame;print("AMARRAS shape retained");quit(0);return
	outline=PackedVector2Array([Vector2(3980,-85),Vector2(4140,-115),Vector2(4400,-180),Vector2(4550,-150),Vector2(4660,95),Vector2(4900,90),Vector2(5140,60),Vector2(5270,250),Vector2(5180,335),Vector2(5420,455),Vector2(5570,510),Vector2(5570,635),Vector2(5515,635),Vector2(5520,830),Vector2(5390,910),Vector2(5140,960),Vector2(4950,970),Vector2(4810,870),Vector2(4720,945),Vector2(4550,910),Vector2(4300,855),Vector2(4150,820),Vector2(4100,700),Vector2(4180,605),Vector2(4070,550),Vector2(4090,430),Vector2(3990,380),Vector2(3910,285),Vector2(3970,240),Vector2(4010,140),Vector2(3930,80),Vector2(3980,40)])
	var floor: TileMapLayer=district.get_node("AmarrasFloor");floor.clear();floor.material.set_shader_parameter("outline_points",outline)
	for y in range(-8,24):
		for x in range(80,120):
			if Geometry2D.is_point_in_polygon(Vector2(x*48+24,y*48+24),outline):floor.set_cell(Vector2i(x,y),0,Vector2i(posmod(x,16),posmod(y,16)))
	# Only new Amarras retaining sprites are replaced; approved Forjas geometry is untouched.
	for child in detail.get_children():
		if child is Sprite2D and child.texture.resource_path.ends_with("retaining_edge.png"):child.free()
	for i in range(outline.size()):
		var a: Vector2=outline[i];var b: Vector2=outline[(i+1)%outline.size()];var delta := b-a;var count := ceili(delta.length()/106)
		for j in range(count):
			var at := a.lerp(b,(j+.5)/count)
			if at.distance_to(Vector2(3990,0))<90 or at.distance_to(Vector2(3935,275))<65 or at.distance_to(Vector2(5520,565))<115:continue
			art("infrastructure/retaining_edge.png",at,Vector2(delta.length()/count+10,47),detail,delta.angle()).modulate=Color(.72,.76,.64)
	var sea: Polygon2D=district.get_node("AguaIndustrialContinua");sea.polygon=rect(Vector2(3000,-3400),Vector2(8500,4300))
	var edges: Array[Vector4]=[]
	for i in range(outline.size()):edges.append(Vector4(outline[i].x,outline[i].y,outline[(i+1)%outline.size()].x,outline[(i+1)%outline.size()].y))
	sea.material.set_shader_parameter("edge_count",edges.size());while edges.size()<64:edges.append(Vector4.ZERO)
	sea.material.set_shader_parameter("coast_edges",edges);district.set_meta("land_polygon",outline);district.set_meta("passage_shape","narrow technical arrivals, central transfer yard, narrow southeast continuation; lower inspection circuit preserved")
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("AMARRAS passage contour saved=",error," cells=",floor.get_used_cells().size()," all existing route endpoints retained")
	world.queue_free();world=null;district=null;detail=null;packed=null;await process_frame;await process_frame;quit(error)
