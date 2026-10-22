extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	if world.has_method("_ready"):
		world._ready()
		
	var wl: Polygon2D = world.get_node_or_null("WestWaterline")
	if wl:
		print("WestWaterline point count: ", wl.polygon.size())
		print("WestWaterline sample points around Y=750..950:")
		for pt in wl.polygon:
			if pt.y >= 700 and pt.y <= 1000:
				print("  Waterline pt: ", pt)
				
	quit(0)
