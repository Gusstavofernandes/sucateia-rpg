extends SceneTree

func _init() -> void:
	var root_scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(root_scene)
	
	var player = root_scene.get_node("Player") as CharacterBody2D
	var cam = player.get_node("Camera2D") as Camera2D
	cam.position_smoothing_enabled = false
	
	print("--- INICIANDO CAPTURA DAS PASSARELAS IN-ENGINE ---")
	
	# Capturas de visualização
	var shots = [
		{"name": "passarela_1_oeste_x1000.png", "pos": Vector2(1000, 642), "player_hide": true},
		{"name": "passarela_2_centro_x2240.png", "pos": Vector2(2240, 642), "player_hide": true},
		{"name": "passarela_3_leste_x3000.png", "pos": Vector2(3000, 642), "player_hide": true},
		{"name": "passarela_1_com_jogador.png", "pos": Vector2(1000, 642), "player_hide": false}
	]
	
	for shot in shots:
		if shot["player_hide"]:
			player.position = Vector2(shot["pos"].x, shot["pos"].y + 250) # afasta o player da foto
			cam.position = Vector2(0, -250) # centraliza a câmera na passarela
		else:
			player.position = shot["pos"] # player exatamente em cima da grade da passarela
			cam.position = Vector2.ZERO
			
		for f in range(15):
			await process_frame
			
		var img = root.get_viewport().get_texture().get_image()
		var save_path = "res://" + shot["name"]
		img.save_png(save_path)
		print("Screenshot gravado: " + shot["name"])
	
	print("--- INICIANDO TESTES FÍSICOS E DE TRAVESSIA ---")
	
	# TESTE 1: TENTAR CRUZAR O CANO FORA DA PASSARELA (X = 750)
	print("[TESTE 1] Tentativa de atravessar o cano fora da passarela (X = 750)...")
	player.position = Vector2(750, 580)
	player.velocity = Vector2(0, 150)
	for f in range(60):
		player.move_and_slide()
		await process_frame
		
	var final_y_blocked = player.position.y
	print("  Posição final após tentar descer: Y = " + str(final_y_blocked))
	if final_y_blocked < 638:
		print("  -> SUCESSO: Cano bloqueou fisicamente o jogador! (Bloqueado em Y < 638)")
	else:
		print("  -> FALHA: Jogador atravessou o cano fora da passarela!")

	# TESTE 2: CRUZAR A PASSARELA 1 (X = 1000) DE NORTE A SUL
	print("[TESTE 2] Cruzando a Passarela 1 (X = 1000) de Norte a Sul...")
	player.position = Vector2(1000, 560)
	player.velocity = Vector2(0, 120)
	var max_elevation_reached = false
	var goblin_head = player.get_node("GoblinHead")
	
	for f in range(90):
		player.move_and_slide()
		await process_frame
		var orig_y = goblin_head.get_meta("orig_y") if goblin_head.has_meta("orig_y") else 0.0
		var diff = goblin_head.position.y - orig_y
		if diff <= -4.0:
			max_elevation_reached = true
			
	var final_y_crossed = player.position.y
	print("  Posição final após travessia: Y = " + str(final_y_crossed))
	if final_y_crossed >= 700:
		print("  -> SUCESSO: Jogador cruzou a passarela perfeitamente para o sul!")
	else:
		print("  -> FALHA: Jogador não conseguiu cruzar a passarela!")
	
	if max_elevation_reached:
		print("  -> SUCESSO: Elevação suave no sprite do goblin foi ativada com sucesso!")
	else:
		print("  -> AVISO: Elevação visual não registrada no intervalo.")

	# TESTE 3: CRUZAR A PASSARELA 3 (X = 3000) DE NORTE A SUL
	print("[TESTE 3] Cruzando a Passarela 3 (X = 3000) de Norte a Sul...")
	player.position = Vector2(3000, 560)
	player.velocity = Vector2(0, 120)
	for f in range(90):
		player.move_and_slide()
		await process_frame
		
	var final_y_p3 = player.position.y
	print("  Posição final após travessia na Passarela 3: Y = " + str(final_y_p3))
	if final_y_p3 >= 700:
		print("  -> SUCESSO: Passarela 3 cruzada perfeitamente!")
	else:
		print("  -> FALHA: Passarela 3 não permitiu travessia!")

	print("--- TODOS OS TESTES CONCLUÍDOS ---")
	quit(0)
