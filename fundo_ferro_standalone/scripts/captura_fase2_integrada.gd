extends SceneTree

func _init():
	print("--- TESTE E CAPTURA IN-ENGINE: FASE 2 INTEGRADA NA CENA MASTER ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var player = scene.get_node("Player")
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# Captura 1: Visão da Mina, Estação e Cavalete a partir do spawn do Goblin
	player.position = Vector2(380, 320)
	cam.position = Vector2(-100, 60)
	
	for i in range(20):
		await process_frame
		
	var img1 = root.get_viewport().get_texture().get_image()
	img1.save_png("res://fase2_mina_estacao_cavalete.png")
	print("Captura 1 salva em res://fase2_mina_estacao_cavalete.png!")
	
	# Captura 2: Close-up no Cavalete e Carrinho com Minério Verde transpondo Canal e Cano
	player.position = Vector2(360, 560)
	cam.position = Vector2(-120, 0)
	
	for i in range(15):
		await process_frame
		
	var img2 = root.get_viewport().get_texture().get_image()
	img2.save_png("res://fase2_cavalete_carrinho_transposicao.png")
	print("Captura 2 salva em res://fase2_cavalete_carrinho_transposicao.png!")
	
	quit(0)
