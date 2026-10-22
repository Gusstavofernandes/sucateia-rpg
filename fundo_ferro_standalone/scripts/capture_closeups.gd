extends SceneTree

func _init() -> void:
	var root_scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(root_scene)
	
	var player = root_scene.get_node("Player") as CharacterBody2D
	var cam = player.get_node("Camera2D") as Camera2D
	cam.position_smoothing_enabled = false
	cam.zoom = Vector2(1.85, 1.85)
	
	# Shot 1: Goblin no meio da Passarela 1 sobre a grade e o cano
	player.position = Vector2(1000, 642)
	cam.position = Vector2.ZERO
	for f in range(15):
		await process_frame
	var img1 = root.get_viewport().get_texture().get_image()
	img1.save_png("res://closeup_passarela_1_goblin.png")
	print("Gravado: closeup_passarela_1_goblin.png")
	
	# Shot 2: Detalhes dos pilares, parafusos e tubulação sob a Passarela 2
	player.position = Vector2(2240, 850) # afasta o player
	cam.position = Vector2(0, -208) # foca na passarela em 642
	for f in range(15):
		await process_frame
	var img2 = root.get_viewport().get_texture().get_image()
	img2.save_png("res://closeup_passarela_2_grade.png")
	print("Gravado: closeup_passarela_2_grade.png")

	# Shot 3: Goblin subindo a rampa da Passarela 3
	player.position = Vector2(3000, 620)
	cam.position = Vector2.ZERO
	for f in range(15):
		await process_frame
	var img3 = root.get_viewport().get_texture().get_image()
	img3.save_png("res://closeup_passarela_3_goblin.png")
	print("Gravado: closeup_passarela_3_goblin.png")
	
	quit(0)
