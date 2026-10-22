extends SceneTree

func _init():
	print("--- RENDERIZANDO CENA SEM O TÚNEL PARA MEDIÇÃO DO RECORTE VAZIO ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	# Ocultar o túnel antigo para expor o recorte vazio original
	var tunel = scene.get_node("RedeFerroviariaMina/TunelMinaEntrada")
	tunel.visible = false
	
	var player = scene.get_node("Player")
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# Focar no canto superior esquerdo (recorte vazio)
	# Coordenadas de mundo: centro da câmera em X = -190, Y = 180
	player.position = Vector2(-20, 380)
	cam.position = Vector2(-190 - player.position.x, 180 - player.position.y)
	cam.zoom = Vector2(1.5, 1.5)
	
	for i in range(20):
		await process_frame
		
	var img = root.get_viewport().get_texture().get_image()
	img.save_png("res://medicao_recorte_sem_tunel.png")
	print("Imagem medicao_recorte_sem_tunel.png salva com sucesso!")
	quit(0)
