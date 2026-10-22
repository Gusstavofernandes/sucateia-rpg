extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	var floor: TileMapLayer = world.get_node("Ground/TerraceFloor")
	print("TileSet: ", floor.tile_set)
	print("Material: ", floor.material)
	if floor.material is ShaderMaterial:
		var sm: ShaderMaterial = floor.material
		print("Shader: ", sm.shader.resource_path)
	
	# Ver os tiles das primeiras colunas (x=3, x=4, etc.)
	for x in range(3, 8):
		for y in range(12, 18):
			var source_id = floor.get_cell_source_id(Vector2i(x, y))
			var atlas_coords = floor.get_cell_atlas_coords(Vector2i(x, y))
			var alt = floor.get_cell_alternative_tile(Vector2i(x, y))
			print("Cell (", x, ", ", y, "): source=", source_id, " atlas=", atlas_coords, " alt=", alt)
			
	quit()
