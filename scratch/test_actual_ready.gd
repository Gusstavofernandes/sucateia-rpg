extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	# Forçar _ready caso necessário
	if world.has_method("_ready"):
		world._ready()
	
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	var count = 0
	for cx in range(-18, 4):
		for cy in range(7, 31):
			var src = floor_node.get_cell_source_id(Vector2i(cx, cy))
			if src != -1:
				count += 1
	print("After _ready, cells in west region: ", count)
	
	var expansion: Node2D = world.get_node_or_null("SucateiaWestGroundExpansion")
	print("SucateiaWestGroundExpansion exists: ", expansion != null)
	if expansion:
		print("Expansion child count: ", expansion.get_child_count())
		for c in expansion.get_children():
			print("  Child: ", c.name, " (", c.get_child_count(), " nodes)")
	
	quit(0)
