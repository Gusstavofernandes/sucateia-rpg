extends SceneTree

func _init() -> void:
	var world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	print("--- SCANNING FOR NODES WITH Y < -1400 ---")
	_scan_north(world)
	print("--- SCAN COMPLETE ---")
	quit(0)

func _scan_north(n: Node) -> void:
	if n is Node2D:
		var gp = n.global_position
		if gp.y < -1400:
			if n is Sprite2D and n.texture:
				print("%-30s | pos=(%6.1f, %6.1f) | parent=%s" % [n.texture.resource_path.get_file(), gp.x, gp.y, n.get_parent().name])
	for c in n.get_children():
		_scan_north(c)
