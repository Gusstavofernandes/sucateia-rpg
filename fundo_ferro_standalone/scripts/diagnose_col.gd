extends SceneTree

func _init() -> void:
	var root_scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(root_scene)
	var player = root_scene.get_node("Player") as CharacterBody2D
	player.position = Vector2(1000, 560)
	player.velocity = Vector2(0, 120)
	for f in range(5):
		player.move_and_slide()
		await process_frame
		for i in player.get_slide_collision_count():
			var col = player.get_slide_collision(i)
			var collider = col.get_collider()
			print("COLIDIU COM: ", collider.name, " (", collider.get_parent().name, ") na pos: ", col.get_position(), " normal: ", col.get_normal())
	quit(0)
