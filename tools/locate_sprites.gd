extends SceneTree

var world: Node2D

func _init() -> void:
	world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	# Procurar todos os Sprite2D que têm visibilidade e posição
	print("Listing nodes in world...")
	_search(world)
	quit(0)

func _search(node: Node) -> void:
	if node is Sprite2D and node.texture:
		var name_low = node.name.to_lower()
		var p_name = node.get_parent().name.to_lower()
		var res = node.texture.resource_path.get_file().to_lower()
		# Procurar qualquer coisa relacionada a bench, gothic, tenem, market, stall
		if "stall" in res or "bench" in res or "crown" in res or "tenement" in res or "gate" in res:
			print(node.get_parent().name, "/", node.name, " pos=", node.global_position, " tex=", res)
	for c in node.get_children():
		_search(c)
