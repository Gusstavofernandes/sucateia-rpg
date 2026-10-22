extends SceneTree

func _init():
	print("--- TESTE DE ALINHAMENTO DO PILOTO DE TRILHOS E ANGULOS ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	# Criar nó temporário do Sistema de Mineração Ferroviária para teste visual
	var rede_ferroviaria = Node2D.new()
	rede_ferroviaria.name = "RedeFerroviariaMina_Teste"
	rede_ferroviaria.y_sort_enabled = true
	scene.add_child(rede_ferroviaria)
	
	# 1. Boca do Túnel da Mina (Parede Norte, X=220, Y=145)
	var tunel = Sprite2D.new()
	tunel.texture = load("res://assets/rails/tunel_mina_norte_v1.png")
	tunel.position = Vector2(220, 150)
	tunel.scale = Vector2(0.26, 0.26)
	tunel.z_index = -11 # Encaixado na muralha norte
	rede_ferroviaria.add_child(tunel)
	
	# Lanterna do Túnel
	var luz_tunel = PointLight2D.new()
	luz_tunel.position = Vector2(245, 130)
	luz_tunel.color = Color(1.0, 0.72, 0.35, 1.0)
	luz_tunel.energy = 1.6
	luz_tunel.texture = scene.get_node("Bueiro_1/LuzLanternaBueiro").texture
	luz_tunel.texture_scale = 3.2
	rede_ferroviaria.add_child(luz_tunel)
	
	# 2. Estação Plataforma com Guincho (Piso claro, X=220, Y=310)
	var estacao_sombra = Sprite2D.new()
	estacao_sombra.texture = load("res://assets/rails/estacao_guincho_vertical_v1_sombra.png")
	estacao_sombra.position = Vector2(220, 316)
	estacao_sombra.scale = Vector2(0.22, 0.22)
	estacao_sombra.z_index = -10
	rede_ferroviaria.add_child(estacao_sombra)
	
	var estacao = Sprite2D.new()
	estacao.texture = load("res://assets/rails/estacao_guincho_vertical_v1.png")
	estacao.position = Vector2(220, 310)
	estacao.scale = Vector2(0.22, 0.22)
	estacao.z_index = -5
	rede_ferroviaria.add_child(estacao)
	
	# Luz da Lanterna da Estação
	var luz_estacao = PointLight2D.new()
	luz_estacao.position = Vector2(175, 305)
	luz_estacao.color = Color(1.0, 0.75, 0.38, 1.0)
	luz_estacao.energy = 1.4
	luz_estacao.texture = scene.get_node("Bueiro_1/LuzLanternaBueiro").texture
	luz_estacao.texture_scale = 2.8
	rede_ferroviaria.add_child(luz_estacao)
	
	# 3. Cavalete Alto Transpondo o Canal e o Cano (X=220, Y=560)
	var cavalete_sombra = Sprite2D.new()
	cavalete_sombra.texture = load("res://assets/rails/cavalete_alto_v1_sombra.png")
	cavalete_sombra.position = Vector2(220, 568)
	cavalete_sombra.scale = Vector2(0.32, 0.32)
	cavalete_sombra.z_index = -6
	rede_ferroviaria.add_child(cavalete_sombra)
	
	var cavalete = Sprite2D.new()
	cavalete.texture = load("res://assets/rails/cavalete_alto_v1.png")
	cavalete.position = Vector2(220, 560)
	cavalete.scale = Vector2(0.32, 0.32)
	cavalete.z_index = 0
	rede_ferroviaria.add_child(cavalete)
	
	# 4. Trilhos Verticais sobre o Cavalete
	var trilho_cavalete = Sprite2D.new()
	trilho_cavalete.texture = load("res://assets/rails/trilho_reto_vertical_v1.png")
	trilho_cavalete.position = Vector2(220, 530)
	trilho_cavalete.scale = Vector2(0.20, 0.20)
	trilho_cavalete.z_index = 1
	rede_ferroviaria.add_child(trilho_cavalete)
	
	# 5. Carrinho Cheio de Minério Verde no Eixo Vertical
	var carrinho_sombra = Sprite2D.new()
	carrinho_sombra.texture = load("res://assets/rails/carrinho_mina_vertical_v1_sombra.png")
	carrinho_sombra.position = Vector2(220, 488)
	carrinho_sombra.scale = Vector2(0.12, 0.12)
	carrinho_sombra.z_index = 1
	rede_ferroviaria.add_child(carrinho_sombra)
	
	var carrinho = Sprite2D.new()
	carrinho.texture = load("res://assets/rails/carrinho_mina_vertical_v1.png")
	carrinho.position = Vector2(220, 480)
	carrinho.scale = Vector2(0.12, 0.12)
	carrinho.z_index = 2
	rede_ferroviaria.add_child(carrinho)
	
	# Luz verde luminescente do minério
	var luz_minerio = PointLight2D.new()
	luz_minerio.position = Vector2(220, 480)
	luz_minerio.color = Color(0.2, 0.95, 0.45, 1.0)
	luz_minerio.energy = 1.8
	luz_minerio.texture = scene.get_node("Bueiro_1/LuzLanternaBueiro").texture
	luz_minerio.texture_scale = 3.0
	rede_ferroviaria.add_child(luz_minerio)
	
	# Ajustar o Player para ficar ao lado da estação em piso livre
	var player = scene.get_node("Player")
	player.position = Vector2(360, 320)
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	cam.position = Vector2(-120, 80) # Olhar centrado na ferrovia
	
	for i in range(15):
		await process_frame
		
	var img = root.get_viewport().get_texture().get_image()
	img.save_png("res://piloto_trilhos_angulos_validados.png")
	print("Captura salva em res://piloto_trilhos_angulos_validados.png com sucesso!")
	quit(0)
