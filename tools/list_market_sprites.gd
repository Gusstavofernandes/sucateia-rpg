extends SceneTree

func _init() -> void:
	var world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	print("--- SCANNING MARKET FLOOR AREA (x: 400..1600, y: -1400..400) ---")
	_scan(world)
	print("--- SCAN COMPLETE ---")
	quit(0)

func _scan(n: Node) -> void:
	if n is Sprite2D and n.texture:
		var gp = n.global_position
		if gp.x >= 350 and gp.x <= 1650 and gp.y >= -1450 and gp.y <= 450:
			var fn = n.texture.resource_path.get_file()
			# ignorar terreno/luz simples
			if not ("floor" in fn or "light" in fn or "shadow" in fn or "dirt" in fn or "patch" in fn):
				print("%-30s | pos=(%6.1f, %6.1f) | parent=%s" % [fn, gp.x, gp.y, n.get_parent().name])
	for c in n.get_children():
		_scan(c)
