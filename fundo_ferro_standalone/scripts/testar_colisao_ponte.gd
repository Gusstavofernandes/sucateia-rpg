extends SceneTree

func _init():
	print("--- TESTANDO FÍSICA E COLISÃO DA PONTE NO GODOT ---")
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
	
	# Teste 1: Posicionar player tentando entrar no canal / ponte pelo norte
	# Posição inicial: Vector2(-188, 450)
	player.position = Vector2(-188, 450)
	print("Posição inicial do player: ", player.position)
	
	# Simular tentativa de andar para o sul (em direção ao canal / ponte) por 30 frames de física
	for i in range(30):
		player.velocity = Vector2(0, 200) # tentando descer
		player.move_and_slide()
		await process_frame
		
	print("Posição do player após tentar atravessar para o sul: ", player.position)
	print("Bloqueado com sucesso antes do canal? ", player.position.y < 485)
	
	# Captura do player encostado na colisão da ponte sem passar por baixo
	cam.zoom = Vector2(2.0, 2.0)
	cam.global_position = Vector2(-188, 480)
	for i in range(15):
		await process_frame
		
	var img = root.get_viewport().get_texture().get_image()
	img.save_png("res://captura_colisao_ponte_bloqueada.png")
	print("Captura da colisão funcionando salva com sucesso!")
	
	quit(0)
