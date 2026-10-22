extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	print("--- INSPECTING RUNTIME PIPES IN CHANNEL SOUTH ---")
	_scan(world)
	quit()

func _scan(n: Node) -> void:
	if n is Sprite2D and n.texture:
		var tex_path: String = n.texture.resource_path
		if tex_path.to_lower().find("pipe") != -1:
			var gpos: Vector2 = n.global_position
			if gpos.x >= 1200 and gpos.x <= 2100 and gpos.y >= 1200 and gpos.y <= 1900:
				print("FOUND PIPE: ", n.get_path(), " | global_pos=", gpos, " | rot=", n.global_rotation, " | scale=", n.global_scale, " | tex=", tex_path)
	for c in n.get_children():
		_scan(c)
