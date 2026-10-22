extends SceneTree

func _init() -> void:
	var world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	print("--- Buscando nós ao redor da área do mercado ---")
	_inspect_node(world)
	quit(0)

func _inspect_node(node: Node) -> void:
	if node is Sprite2D and node.texture:
		var gpos = node.global_position
		if gpos.x >= 700 and gpos.x <= 1500 and gpos.y >= -800 and gpos.y <= 600:
			var tex_path = node.texture.resource_path
			if not "decal" in tex_path and not "light" in tex_path and not "shadow" in tex_path and not "dirt" in tex_path:
				print(node.name, " (", node.get_parent().name, ") at ", gpos, " tex: ", tex_path.get_file())
	for c in node.get_children():
		_inspect_node(c)
