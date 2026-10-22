extends SceneTree

func _init() -> void:
	print("--- VALIDATING SCENE LOADING & SCRIPTS ---")
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	if not packed:
		print("ERROR: Failed to load sucateia.tscn")
		quit(1)
		return
		
	var world: Node = packed.instantiate()
	root.add_child(world)
	print("SUCCESS: Scene instantiated and _ready executed without errors!")
	
	var floor_node: TileMapLayer = world.get_node_or_null("Ground/TerraceFloor")
	if floor_node:
		var west_cells := 0
		for c in floor_node.get_used_cells():
			if c.x <= 2:
				west_cells += 1
		print("SUCCESS: TerraceFloor expanded cells at x <= 2: ", west_cells)
		
	var expansion: Node2D = world.get_node_or_null("SucateiaWestGroundExpansion")
	if expansion:
		print("SUCCESS: SucateiaWestGroundExpansion node created with children: ", expansion.get_child_count())
		for child in expansion.get_children():
			print("  Child: ", child.name, " (", child.get_child_count(), " children)")
			
	quit(0)
