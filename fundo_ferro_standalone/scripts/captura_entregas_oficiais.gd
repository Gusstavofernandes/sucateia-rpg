extends SceneTree

func _init():
	print("--- GERANDO CAPTURAS OFICIAIS DE ENTREGA ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var player = scene.get_node("Player")
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# 1. Captura da Nova Posição à Esquerda (Boca de túnel, estação, cavalete e spawn livre)
	player.position = Vector2(20, 320)
	cam.position = Vector2(-120, 40)
	
	for i in range(20):
		await process_frame
		
	var img1 = root.get_viewport().get_texture().get_image()
	img1.save_png("res://captura_nova_posicao_esquerda.png")
	print("Captura 1 salva em res://captura_nova_posicao_esquerda.png!")
	
	# 2. Captura do Centro da Galeria Restaurado (Paredes de arcos, canal verde e bueiro intactos)
	player.position = Vector2(450, 400)
	cam.position = Vector2(0, 0)
	
	for i in range(15):
		await process_frame
		
	var img2 = root.get_viewport().get_texture().get_image()
	img2.save_png("res://captura_centro_galeria_restaurado.png")
	print("Captura 2 salva em res://captura_centro_galeria_restaurado.png!")
	
	quit(0)
