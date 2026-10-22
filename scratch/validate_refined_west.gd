extends SceneTree

func _init() -> void:
	print("--- VALIDATING REFINED WEST GROUND ---")
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	if world.has_method("_ready"):
		world._ready()
		
	# Checar se muretas antigas foram ocultadas
	var quay: Node2D = world.get_node_or_null("GoblinIndustrialQuay")
	var hidden_quay := 0
	if quay:
		for c in quay.get_children():
			if c is Sprite2D and not c.visible:
				hidden_quay += 1
	print("Hidden quay sprites (interior wall removed): ", hidden_quay)
	
	var lower: Node2D = world.get_node_or_null("LowerCoastReworked")
	var hidden_lower := 0
	if lower:
		for c in lower.get_children():
			if c is Sprite2D and not c.visible:
				hidden_lower += 1
	print("Hidden lower coast sprites (diagonal wall removed): ", hidden_lower)
	
	var expansion: Node2D = world.get_node_or_null("SucateiaWestGroundExpansion")
	print("SucateiaWestGroundExpansion exists: ", expansion != null)
	if expansion:
		for c in expansion.get_children():
			print("  Child: ", c.name, " (", c.get_child_count(), " nodes)")
			
	var pipe_dock = world.get_node_or_null("FinishedInfrastructure/@Sprite2D@507")
	print("Dock pipe 507 visible: ", pipe_dock.visible if pipe_dock else "null")
	
	quit(0)
