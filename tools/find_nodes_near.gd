extends SceneTree

func _init() -> void:
	var world = load(res://maps/sucateia/sucateia.tscn).instantiate()
	root.add_child(world)
	call_deferred(_go, world)

func _go(world: Node) -> void:
	print(--- LISTING NODES ---)
	_scan(world)
	print(--- DONE ---)
	quit(0)

func _scan(n: Node) -> void:
	if n is Sprite2D and n.texture:
		var gp = n.global_position
		var fn = n.texture.resource_path.get_file()
		if gp.x > 400 and gp.x < 1600 and gp.y > -400 and gp.y < 1200:
			print(n.get_parent().name, /, n.name,  pos=, gp,  tex=, fn)
	for c in n.get_children():
		_scan(c)
