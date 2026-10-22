extends SceneTree

func _init():
	print("--- GERANDO CAPTURAS PRECISAS COM CAMERA DEDICADA ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	# Desativar a câmera interna do player
	var player = scene.get_node("Player")
	var player_cam = player.get_node_or_null("Camera2D")
	if player_cam:
		player_cam.enabled = false
		
	# Criar câmera de captura independente filha da cena após entrar na árvore
	var cam = Camera2D.new()
	cam.anchor_mode = Camera2D.ANCHOR_MODE_DRAG_CENTER
	cam.position_smoothing_enabled = false
	cam.limit_left = -10000
	cam.limit_right = 10000
	cam.limit_top = -10000
	cam.limit_bottom = 10000
	scene.add_child(cam)
	
	await process_frame
	cam.enabled = true
	cam.make_current()
	
	# Posicionar player na área livre ao lado da estação (X = -40, Y = 320)
	player.position = Vector2(-40, 320)
	
	# 1. Visão Completa da Ferrovia (Túnel V2 -> Estação V2 -> Ponte -> Carrinho)
	cam.zoom = Vector2(1.0, 1.0)
	cam.global_position = Vector2(-190, 340)
	for i in range(20):
		await process_frame
	var img1 = root.get_viewport().get_texture().get_image()
	img1.save_png("res://captura_boca_tunel_v2_completo.png")
	print("Captura 1 (Completo) salva com sucesso!")
	
	# 2. Close-up Cirúrgico na Emenda Túnel -> Estação (Y = 244.0, X = -190.0)
	cam.zoom = Vector2(2.5, 2.5)
	cam.global_position = Vector2(-190, 244)
	for i in range(15):
		await process_frame
	var img2 = root.get_viewport().get_texture().get_image()
	img2.save_png("res://captura_boca_tunel_v2_closeup_emenda.png")
	print("Captura 2 (Close-up Emenda) salva com sucesso!")
	
	# 3. Vista do Encaixe do Portal e Asas na Parede Norte
	cam.zoom = Vector2(1.4, 1.4)
	cam.global_position = Vector2(-190, 140)
	for i in range(15):
		await process_frame
	var img3 = root.get_viewport().get_texture().get_image()
	img3.save_png("res://captura_boca_tunel_v2_recorte_parede.png")
	print("Captura 3 (Encaixe Parede Norte) salva com sucesso!")
	
	quit(0)
