extends SceneTree

func _init():
	print("--- GERANDO CAPTURAS IN-ENGINE DO ALINHAMENTO FINAL V2 ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var player = scene.get_node("Player")
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# 1. Foco no conjunto completo da Mina alinhado (Túnel V2 -> Estação V2 -> Ponte -> Carrinho)
	player.position = Vector2(-20, 380)
	cam.position = Vector2(-190 - player.position.x, 380 - player.position.y)
	
	for i in range(25):
		await process_frame
		
	var img1 = root.get_viewport().get_texture().get_image()
	img1.save_png("res://captura_estacao_v2_inengine_completo.png")
	print("Captura 1 (Conjunto Completo) salva com sucesso!")
	
	# 2. Close-up de alta precisão nas emendas do trilho (Túnel -> Estação e Estação -> Ponte)
	cam.zoom = Vector2(2.0, 2.0)
	cam.position = Vector2(-190 - player.position.x, 330 - player.position.y)
	
	for i in range(15):
		await process_frame
		
	var img2 = root.get_viewport().get_texture().get_image()
	img2.save_png("res://captura_estacao_v2_inengine_closeup.png")
	print("Captura 2 (Close-up Emendas) salva com sucesso!")
	
	# 3. Visão do jogador caminhando na área livre ao lado da estação
	cam.zoom = Vector2(1.0, 1.0)
	player.position = Vector2(30, 320)
	cam.position = Vector2(-80, 20)
	
	for i in range(15):
		await process_frame
		
	var img3 = root.get_viewport().get_texture().get_image()
	img3.save_png("res://captura_estacao_v2_inengine_gameplay.png")
	print("Captura 3 (Gameplay / Spawn livre) salva com sucesso!")
	
	quit(0)
