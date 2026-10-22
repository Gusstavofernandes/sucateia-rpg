extends SceneTree

func _init():
	print("--- TESTE COM X = -190 ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var rede = scene.get_node("RedeFerroviariaMina")
	
	# Mover conjunto para X = -190
	var delta_x = -190.0 - 220.0
	for child in rede.get_children():
		child.position.x += delta_x
		
	# Mover Sucata_1 para X = -360
	var sucata_1 = scene.get_node_or_null("EntulhoESucataNoChao/Sucata_1")
	if sucata_1:
		sucata_1.position.x = -360.0
		
	# Spawn do jogador: no piso claro entre a estação e o duto da parede (X = 30, Y = 320)
	var player = scene.get_node("Player")
	player.position = Vector2(20, 320)
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	cam.position = Vector2(-120, 40)
	
	for i in range(20):
		await process_frame
		
	var img = root.get_viewport().get_texture().get_image()
	img.save_png("res://teste_conjunto_x_minus_190.png")
	print("Captura salva em res://teste_conjunto_x_minus_190.png!")
	quit(0)
