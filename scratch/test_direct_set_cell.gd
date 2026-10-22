extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	print("Initial cell (0, 15): ", floor_node.get_cell_source_id(Vector2i(0, 15)))
	floor_node.set_cell(Vector2i(0, 15), 0, Vector2i(0, 0), 0)
	print("After set_cell (0, 15): ", floor_node.get_cell_source_id(Vector2i(0, 15)))
	quit(0)
