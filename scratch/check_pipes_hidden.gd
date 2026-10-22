extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	if world.has_method("_ready"):
		world._ready()
		
	var pipe1 = world.get_node_or_null("LowerCoastReworked/@Sprite2D@183")
	var pipe2 = world.get_node_or_null("FinishedInfrastructure/@Sprite2D@421")
	var pipe3 = world.get_node_or_null("FinishedInfrastructure/@Sprite2D@438")
	
	print("Pipe 1 (1770, 1510) visible: ", pipe1.visible if pipe1 else "null")
	print("Pipe 2 (1703, 1448) visible: ", pipe2.visible if pipe2 else "null")
	print("Pipe 3 (1945, 1480) visible: ", pipe3.visible if pipe3 else "null")
	quit(0)
