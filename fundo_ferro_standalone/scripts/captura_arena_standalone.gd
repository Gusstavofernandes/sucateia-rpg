extends SceneTree

## Script de captura in-engine da Feira Clandestina, Barracas de Apostas e Tráfico de Humanoides

func _init() -> void:
	print("--- INICIANDO CAPTURA DA FEIRA CLANDESTINA E APOSTAS ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var player = scene.get_node("Player")
	var cam: Camera2D = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# 1. CAPTURA 1: VISÃO GERAL DA FEIRA CLANDESTINA (Mostrando todo o pátio sul preenchido)
	player.position = Vector2(3750, 1020)
	cam.position = Vector2(0, 0)
	cam.zoom = Vector2(0.48, 0.48)
	
	for i in range(50):
		await process_frame
		
	var tex = root.get_viewport().get_texture()
	if tex != null:
		var img = tex.get_image()
		if img != null:
			img.save_png("res://captura_feira_clandestina_visao_geral.png")
			print("Captura 1 (Visao Geral Feira Clandestina) salva com sucesso!")

	# 2. CAPTURA 2: CLOSE NAS BARRACAS DE APOSTAS E PEÇAS RARAS (FEIRA DO ROLO)
	player.position = Vector2(3680, 860)
	cam.zoom = Vector2(0.68, 0.68)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img2 = tex.get_image()
		if img2 != null:
			img2.save_png("res://captura_barracas_apostas_pecas_close.png")
			print("Captura 2 (Barracas Apostas e Pecas Raras Close) salva com sucesso!")

	# 3. CAPTURA 3: CLOSE NA JAULA DE MERCADORIA DE HUMANOIDES E TAPETE DE TROCAS
	player.position = Vector2(3750, 1150)
	cam.zoom = Vector2(0.68, 0.68)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img3 = tex.get_image()
		if img3 != null:
			img3.save_png("res://captura_jaula_humanoides_close.png")
			print("Captura 3 (Jaula de Humanoides Close) salva com sucesso!")
	
	quit(0)
