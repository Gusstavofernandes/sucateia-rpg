extends SceneTree

func _init() -> void:
	var installer = load("res://scripts/world/sucateia_west_ground.gd").new()
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	var count = 0
	for cx in range(-18, 4):
		for cy in range(7, 31):
			var src = floor_node.get_cell_source_id(Vector2i(cx, cy))
			if src != -1:
				count += 1
	print("Cells in range [-18..3, 7..30] with tile: ", count)
	
	quit(0)
