extends SceneTree

func _init() -> void:
	var packed: PackedScene = load("res://maps/sucateia/sucateia.tscn")
	var world: Node = packed.instantiate()
	root.add_child(world)
	
	print("--- ALL SPRITES IN REGION (1300..1650, 1400..1800) ---")
	_scan(world)
	quit()

func _scan(n: Node) -> void:
	if n is Sprite2D and n.texture:
		var gpos: Vector2 = n.global_position
		if gpos.x >= 1300 and gpos.x <= 1650 and gpos.y >= 1400 and gpos.y <= 1800:
			var tex_path: String = n.texture.resource_path
			print(n.name, " (parent: ", n.get_parent().name, ") -> pos=", gpos, " | rot=", n.global_rotation, " | scale=", n.global_scale, " | tex=", tex_path)
	for c in n.get_children():
		_scan(c)
