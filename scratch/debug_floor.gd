extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	print("floor_node: ", floor_node)
	if floor_node:
		var count = 0
		for cx in range(-18, 4):
			for cy in range(7, 31):
				var src = floor_node.get_cell_source_id(Vector2i(cx, cy))
				if src != -1:
					count += 1
		print("Cells with src != -1 in west region: ", count)
		
	quit(0)
