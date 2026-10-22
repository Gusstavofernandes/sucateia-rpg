extends SceneTree

## Script de captura in-engine do Setor Sul da Arena povoado com assets de reconstrução refinados

func _init() -> void:
	print("--- INICIANDO CAPTURA REFINADA DO SETOR SUL DA ARENA ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var player = scene.get_node("Player")
	var cam: Camera2D = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# 1. CAPTURA 1: VISÃO GERAL PANORÂMICA DO SETOR SUL DA ARENA E MERCADO (X=4500, Y=1220)
	player.position = Vector2(4500, 1220)
	cam.position = Vector2(0, 0)
	cam.zoom = Vector2(0.38, 0.38)
	
	for i in range(50):
		await process_frame
		
	var tex = root.get_viewport().get_texture()
	if tex != null:
		var img = tex.get_image()
		if img != null:
			img.save_png("res://captura_setor_sul_arena_geral.png")
			print("Captura 1 (Visao Geral Setor Sul Refinada) salva com sucesso!")

	# 2. CAPTURA 2: CLOSE NO RECICLADOR DE SUCATA, BARRACA DE PANOS E CARROÇÃO
	player.position = Vector2(4150, 1150)
	cam.zoom = Vector2(0.65, 0.65)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img2 = tex.get_image()
		if img2 != null:
			img2.save_png("res://captura_reciclador_e_mercado_close.png")
			print("Captura 2 (Reciclador e Mercado Close) salva com sucesso!")

	# 3. CAPTURA 3: CLOSE NO PAVILHÃO DE CÂMBIO, OFICINA DE ARMEIROS E PORTÃO SUL DO COLISEU
	player.position = Vector2(4700, 1150)
	cam.zoom = Vector2(0.65, 0.65)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img3 = tex.get_image()
		if img3 != null:
			img3.save_png("res://captura_cambio_e_oficina_coliseu_close.png")
			print("Captura 3 (Cambio e Oficina Coliseu Close) salva com sucesso!")

	# 4. CAPTURA 4: CLOSE NA ARCADA ATACADISTA, BANCADA DE TRIAGEM E OFICINA
	player.position = Vector2(3600, 1420)
	cam.zoom = Vector2(0.65, 0.65)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img4 = tex.get_image()
		if img4 != null:
			img4.save_png("res://captura_arcada_triagem_close.png")
			print("Captura 4 (Arcada e Triagem Close) salva com sucesso!")
	
	# 5. CAPTURA 5: CLOSE NO MOTOR SUBTERRÂNEO, SALA DE CALDEIRAS E CISTERNA ELEVADA (LADO LESTE)
	player.position = Vector2(5600, 1300)
	cam.zoom = Vector2(0.60, 0.60)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img5 = tex.get_image()
		if img5 != null:
			img5.save_png("res://captura_motor_cisterna_leste_close.png")
			print("Captura 5 (Motor, Caldeiras e Cisterna Leste Close) salva com sucesso!")

	quit(0)
