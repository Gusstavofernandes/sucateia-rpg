extends SceneTree

func _init() -> void:
	var root_scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(root_scene)
	
	# Aguardar 5 physics frames para o PhysicsServer2D conectar todos os corpos e espaços
	for i in range(5):
		await physics_frame
		
	var player = root_scene.get_node("Player") as CharacterBody2D
	print("Physics Server inicializado com sucesso.")
	
	# TESTE 1: TENTAR CRUZAR O CANO FORA DA PASSARELA (X = 750)
	print("\n--- TESTE 1: Cano fora da passarela (X = 750) ---")
	player.position = Vector2(750, 600)
	player.velocity = Vector2(0, 150)
	for f in range(30):
		player.velocity = Vector2(0, 150)
		player.move_and_slide()
		await physics_frame
	print("Posicao apos tentar descer pelo cano: ", player.position)
	if player.position.y < 638:
		print(">> SUCESSO: O cano bloqueia o jogador fora da passarela!")
	else:
		print(">> FALHA: O jogador atravessou o cano!")

	# TESTE 2: CRUZAR PELA PASSARELA 1 (X = 1000)
	print("\n--- TESTE 2: Travessia pela Passarela 1 (X = 1000) ---")
	player.position = Vector2(1000, 570)
	var max_elevation_reached = false
	var goblin_head = player.get_node("GoblinHead")
	
	for f in range(60):
		player.velocity = Vector2(0, 150)
		player.move_and_slide()
		await physics_frame
		if goblin_head.has_meta("orig_y"):
			var diff = goblin_head.position.y - goblin_head.get_meta("orig_y")
			if diff <= -3.0:
				max_elevation_reached = true
				
	print("Posicao apos travessia na Passarela 1: ", player.position)
	if player.position.y >= 700:
		print(">> SUCESSO: Jogador cruzou a Passarela 1 com perfeicao de Norte a Sul!")
	else:
		print(">> FALHA: Jogador foi bloqueado na Passarela 1!")
		for i in player.get_slide_collision_count():
			var col = player.get_slide_collision(i)
			print("   Colidiu com: ", col.get_collider().name, " em: ", col.get_position())

	if max_elevation_reached:
		print(">> SUCESSO: Elevacao suave do sprite do goblin ativada com sucesso!")
	else:
		print(">> AVISO: Elevacao visual nao detectada.")

	# TESTE 3: CRUZAR PELA PASSARELA 2 (X = 2240)
	print("\n--- TESTE 3: Travessia pela Passarela 2 (X = 2240) ---")
	player.position = Vector2(2240, 570)
	for f in range(60):
		player.velocity = Vector2(0, 150)
		player.move_and_slide()
		await physics_frame
	print("Posicao apos travessia na Passarela 2: ", player.position)
	if player.position.y >= 700:
		print(">> SUCESSO: Jogador cruzou a Passarela 2 com perfeicao de Norte a Sul!")
	else:
		print(">> FALHA: Jogador foi bloqueado na Passarela 2!")

	# TESTE 4: CRUZAR PELA PASSARELA 3 (X = 3000)
	print("\n--- TESTE 4: Travessia pela Passarela 3 (X = 3000) ---")
	player.position = Vector2(3000, 570)
	for f in range(60):
		player.velocity = Vector2(0, 150)
		player.move_and_slide()
		await physics_frame
	print("Posicao apos travessia na Passarela 3: ", player.position)
	if player.position.y >= 700:
		print(">> SUCESSO: Jogador cruzou a Passarela 3 com perfeicao de Norte a Sul!")
	else:
		print(">> FALHA: Jogador foi bloqueado na Passarela 3!")

	print("\n--- TODOS OS TESTES FÍSICOS CONCLUÍDOS ---")
	quit(0)
