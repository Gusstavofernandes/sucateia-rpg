extends SceneTree

func _init():
	print("--- TESTE DE CAPTURA: VALVULAS REMOVIDAS E FIACAO CONTINUA ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	# Focar a câmera exatamente onde ficavam as válvulas (X=750, Y=640)
	var player = scene.get_node("Player")
	player.position = Vector2(750, 520)
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	cam.position = Vector2.ZERO
	
	# Aguardar renderização
	for i in range(15):
		await process_frame
		
	var img = root.get_viewport().get_texture().get_image()
	img.save_png("res://valvulas_removidas_fiacao_continua.png")
	print("Captura salva em res://valvulas_removidas_fiacao_continua.png com sucesso!")
	quit(0)
