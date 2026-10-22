extends SceneTree

func _init() -> void:
	var root_scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(root_scene)
	
	var player = root_scene.get_node("Player")
	var cam = player.get_node("Camera2D")
	
	var shots = [
		{"name": "industrial_manifold_oeste.png", "pos": Vector2(750, 830)},
		{"name": "industrial_decantador_norte.png", "pos": Vector2(1150, 440)},
		{"name": "industrial_bomba_succao.png", "pos": Vector2(1750, 830)},
		{"name": "industrial_tubo_travessia.png", "pos": Vector2(2200, 830)},
		{"name": "industrial_caldeira_leste.png", "pos": Vector2(2650, 830)},
		{"name": "industrial_tubo_leste_parede.png", "pos": Vector2(3200, 830)}
	]
	
	for shot in shots:
		player.position = shot["pos"]
		cam.position = Vector2.ZERO
		
		for f in range(12):
			await process_frame
			
		var img = root.get_viewport().get_texture().get_image()
		img.save_png("res://" + shot["name"])
		print("Screenshot capturado: " + shot["name"])
		
	quit(0)
