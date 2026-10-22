extends SceneTree

func _init() -> void:
	print("--- VALIDATING TERRAIN FILL UNTIL ROCKS ---")
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	if world.has_method("_ready"):
		world._ready()
		
	var wl: Polygon2D = world.get_node_or_null("WestWaterline")
	print("WestWaterline exists: ", wl != null)
	if wl:
		print("Waterline point count: ", wl.polygon.size())
		# Verificar se o ponto antigo (120, 1160) ainda existe no WestWaterline
		var has_old_cut := false
		for pt in wl.polygon:
			if absf(pt.x - 120.0) < 5.0 and absf(pt.y - 1160.0) < 5.0:
				has_old_cut = true
				break
		print("Has old water cut at (120, 1160): ", has_old_cut)
		
	var expansion: Node2D = world.get_node_or_null("SucateiaWestGroundExpansion")
	print("SucateiaWestGroundExpansion exists: ", expansion != null)
	if expansion:
		var soil_layer: Node2D = expansion.get_node_or_null("RedSoilAndDetails")
		if soil_layer:
			print("RedSoilAndDetails child count: ", soil_layer.get_child_count())
			
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	if floor_node:
		var cells_near_rocks := 0
		for cx in range(-10, 8):
			for cy in range(15, 33):
				if floor_node.get_cell_source_id(Vector2i(cx, cy)) != -1:
					cells_near_rocks += 1
		print("Cells near rocks (y: 15..32, x: -10..7): ", cells_near_rocks)
		
	quit(0)
