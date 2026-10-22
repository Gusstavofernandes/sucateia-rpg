extends SceneTree

func _init() -> void:
	var root_scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(root_scene)
	
	var player = root_scene.get_node("Player") as CharacterBody2D
	var cam = player.get_node("Camera2D") as Camera2D
	cam.position_smoothing_enabled = false
	
	# Shot 1: Canto Noroeste (Passagem parede oeste, margem norte livre de sucatas na rota, sem ponta solta)
	player.position = Vector2(250, 520)
	cam.position = Vector2.ZERO
	for f in range(15):
		await process_frame
	var img1 = root.get_viewport().get_texture().get_image()
	img1.save_png("res://fase0_canto_noroeste.png")
	print("Capturado: fase0_canto_noroeste.png")
	
	# Shot 2: Passarela 1 (Sem duto grosso pendurado no teto sobre a ponte do canal)
	player.position = Vector2(1000, 550)
	cam.position = Vector2.ZERO
	for f in range(15):
		await process_frame
	var img2 = root.get_viewport().get_texture().get_image()
	img2.save_png("res://fase0_passarela1_sem_duto.png")
	print("Capturado: fase0_passarela1_sem_duto.png")

	quit(0)
