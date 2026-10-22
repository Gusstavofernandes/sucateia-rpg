extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	var ts: TileSet = floor_node.tile_set
	print("TileSet source count: ", ts.get_source_count())
	var source: TileSetAtlasSource = ts.get_source(0)
	print("Atlas source: ", source)
	if source:
		print("Source tiles count: ", source.get_tiles_count())
		for i in range(min(20, source.get_tiles_count())):
			print("Tile ", i, ": ", source.get_tile_id(i))
			
	quit(0)
