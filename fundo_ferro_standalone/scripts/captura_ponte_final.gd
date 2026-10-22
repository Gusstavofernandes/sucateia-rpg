extends SceneTree

func _init():
	print("--- GERANDO CAPTURAS IN-ENGINE DA PONTE CALIBRADA SEM CARRINHO ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var player = scene.get_node("Player")
	var player_cam = player.get_node_or_null("Camera2D")
	if player_cam:
		player_cam.enabled = false
		
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
	
	# 1. Visão Geral da Ferrovia Completa (Túnel -> Estação -> Ponte limpa sem carrinho)
	cam.zoom = Vector2(1.0, 1.0)
	cam.global_position = Vector2(-190, 420)
	for i in range(25):
		await process_frame
	var img1 = root.get_viewport().get_texture().get_image()
	img1.save_png("res://captura_ponte_sem_carrinho_completo.png")
	print("Captura 1 (Ferrovia Completa sem Carrinho) salva!")
	
	# 2. Close-up Cirúrgico na Junção Estação -> Ponte (Y = 406.0, X = -190.0)
	cam.zoom = Vector2(2.5, 2.5)
	cam.global_position = Vector2(-190, 410)
	for i in range(15):
		await process_frame
	var img2 = root.get_viewport().get_texture().get_image()
	img2.save_png("res://captura_ponte_emenda_closeup.png")
	print("Captura 2 (Close-up Junção Estação-Ponte) salva!")
	
	# 3. Vista da Ponte Atravessando o Canal de Esgoto
	cam.zoom = Vector2(1.3, 1.3)
	cam.global_position = Vector2(-190, 560)
	for i in range(15):
		await process_frame
	var img3 = root.get_viewport().get_texture().get_image()
	img3.save_png("res://captura_ponte_canal_travessia.png")
	print("Captura 3 (Travessia do Canal) salva!")
	
	quit(0)
