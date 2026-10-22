extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	var floor: TileMapLayer = world.get_node("Ground/TerraceFloor")
	var used = floor.get_used_cells()
	var min_x = 999999
	var max_x = -999999
	var min_y = 999999
	var max_y = -999999
	for c in used:
		if c.x < min_x: min_x = c.x
		if c.x > max_x: max_x = c.x
		if c.y < min_y: min_y = c.y
		if c.y > max_y: max_y = c.y
		
	print("TerraceFloor cells count: ", used.size())
	print("Cell bounds: X=[", min_x, ", ", max_x, "] Y=[", min_y, ", ", max_y, "]")
	var tile_size = floor.tile_set.tile_size if floor.tile_set else Vector2i(32, 32)
	print("Tile size: ", tile_size)
	print("World bounds approx: X=[", min_x * tile_size.x, ", ", max_x * tile_size.x, "] Y=[", min_y * tile_size.y, ", ", max_y * tile_size.y, "]")
	
	# Verificar se há outros TileMapLayers na cena
	_find_all_tilemaps(world)
	quit()

func _find_all_tilemaps(n: Node) -> void:
	if n is TileMapLayer:
		print("Found TileMapLayer: ", n.get_path(), " with ", n.get_used_cells().size(), " cells")
	for c in n.get_children():
		_find_all_tilemaps(c)
