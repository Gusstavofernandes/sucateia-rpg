extends SceneTree

func _init() -> void:
	var world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var floor_layer: TileMapLayer = world.get_node("MarketDistrict/MarketFloor")
	var used = floor_layer.get_used_cells()
	var min_p = Vector2(999999, 999999)
	var max_p = Vector2(-999999, -999999)
	for c in used:
		var lp = floor_layer.map_to_local(c)
		min_p.x = min(min_p.x, lp.x)
		min_p.y = min(min_p.y, lp.y)
		max_p.x = max(max_p.x, lp.x)
		max_p.y = max(max_p.y, lp.y)
		
	print("MarketFloor bounds: ", min_p, " to ", max_p)
	
	_scan_for_bench(world)
	quit(0)

func _scan_for_bench(node: Node) -> void:
	if node is Sprite2D and node.texture:
		var path = node.texture.resource_path
		if "bench" in path.to_lower() or "workshop" in path.to_lower() or "table" in path.to_lower() or "craft" in path.to_lower() or "salvage" in path.to_lower():
			print("FOUND: ", node.get_parent().name, "/", node.name, " @ pos=", node.global_position, " tex=", path.get_file())
	for c in node.get_children():
		_scan_for_bench(c)
