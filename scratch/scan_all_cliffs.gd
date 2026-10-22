extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	if world.has_method("_ready"):
		world._ready()
		
	print("--- SCANNING ALL CLIFF SPRITES IN WORLD ---")
	_scan(world)
	quit(0)

func _scan(n: Node) -> void:
	if n is Sprite2D and n.texture:
		var p: String = n.texture.resource_path
		if any_match(p):
			print(n.name, " (parent: ", n.get_parent().name, ") -> pos=", n.global_position, " | sc=", n.global_scale, " | rot=", n.global_rotation, " | tex=", p.get_file())
	for c in n.get_children():
		_scan(c)

func any_match(path: String) -> bool:
	var f := path.to_lower()
	return f.find("falesia") != -1 or f.find("cliff") != -1 or f.find("rock") != -1
