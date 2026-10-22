extends SceneTree

## Script de validação visual do layout 100% desobstruído e sem sobreposição com o Coliseu

func _init() -> void:
	print("--- INICIANDO CAPTURA DO LAYOUT LIMPO E DESOBSTRUÍDO ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var player = scene.get_node("Player")
	var cam: Camera2D = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# 1. CAPTURA 1: VISÃO GERAL PANORÂMICA (Mostrando a grandiosidade da arena e a organização espacial)
	player.position = Vector2(4800, 1350)
	cam.position = Vector2(0, 0)
	cam.zoom = Vector2(0.32, 0.32)
	
	for i in range(50):
		await process_frame
		
	var tex = root.get_viewport().get_texture()
	if tex != null:
		var img = tex.get_image()
		if img != null:
			img.save_png("res://captura_layout_limpo_visao_geral.png")
			print("Captura 1 (Visao Geral Panoramica) salva com sucesso!")

	# 2. CAPTURA 2: FACHADA SUL E PRAÇA DO COLISEU 100% DESOBSTRUÍDAS
	player.position = Vector2(4940, 1100)
	cam.zoom = Vector2(0.60, 0.60)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img2 = tex.get_image()
		if img2 != null:
			img2.save_png("res://captura_coliseu_praca_desobstruida.png")
			print("Captura 2 (Praca Coliseu Desobstruida) salva com sucesso!")

	# 3. CAPTURA 3: FEIRA DO ROLO OESTE ESPAÇOSA E SEM SOBREPOSIÇÕES
	player.position = Vector2(3650, 1200)
	cam.zoom = Vector2(0.55, 0.55)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img3 = tex.get_image()
		if img3 != null:
			img3.save_png("res://captura_feira_do_rolo_espacosa.png")
			print("Captura 3 (Feira do Rolo Espacosa) salva com sucesso!")

	# 4. CAPTURA 4: DISTRITO MECÂNICO E OFICINAS LESTE BEM ESPAÇADO
	player.position = Vector2(5400, 1450)
	cam.zoom = Vector2(0.52, 0.52)
	
	for i in range(30):
		await process_frame
		
	tex = root.get_viewport().get_texture()
	if tex != null:
		var img4 = tex.get_image()
		if img4 != null:
			img4.save_png("res://captura_distrito_mecanico_espacoso.png")
			print("Captura 4 (Distrito Mecanico Espacoso) salva com sucesso!")

	quit(0)
