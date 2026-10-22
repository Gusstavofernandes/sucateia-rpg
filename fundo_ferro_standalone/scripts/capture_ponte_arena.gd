extends SceneTree

func _init() -> void:
	var root_scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(root_scene)
	
	var player = root_scene.get_node("Player") as CharacterBody2D
	var cam = player.get_node("Camera2D") as Camera2D
	cam.position_smoothing_enabled = false
	cam.zoom = Vector2(1.15, 1.15)
	
	print("--- INICIANDO CAPTURA DA PONTE DA ARENA ---")
	
	# 1. Foto vazia da ponte unificada
	player.position = Vector2(3680, 850)
	cam.position = Vector2(0, -285) # foca na ponte (Y=565)
	for f in range(20):
		await process_frame
	var img = root.get_viewport().get_texture().get_image()
	img.save_png("res://captura_ponte_arena_vazia.png")
	print("Screenshot salvo: captura_ponte_arena_vazia.png")
	
	# 2. Foto com o jogador no meio da ponte (onde estava no print do usuário)
	player.position = Vector2(3680, 595)
	cam.position = Vector2.ZERO
	for f in range(20):
		await process_frame
	img = root.get_viewport().get_texture().get_image()
	img.save_png("res://captura_ponte_arena_com_jogador.png")
	print("Screenshot salvo: captura_ponte_arena_com_jogador.png")
	
	# 3. Foto com o jogador cruzando o cano ao sul
	player.position = Vector2(3680, 642)
	cam.position = Vector2.ZERO
	for f in range(20):
		await process_frame
	img = root.get_viewport().get_texture().get_image()
	img.save_png("res://captura_ponte_arena_cruzando_cano.png")
	print("Screenshot salvo: captura_ponte_arena_cruzando_cano.png")
	
	print("--- CAPTURAS FINALIZADAS COM SUCESSO ---")
	quit(0)
