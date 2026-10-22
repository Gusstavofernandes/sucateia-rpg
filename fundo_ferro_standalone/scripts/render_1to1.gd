extends SceneTree

func _init():
	print("--- RENDERIZANDO MUNDO 1:1 EM TORNO DA FERROVIA ---")
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	# Desativar player cam
	var player = scene.get_node("Player")
	var player_cam = player.get_node_or_null("Camera2D")
	if player_cam:
		player_cam.enabled = false
		
	var cam = Camera2D.new()
	cam.anchor_mode = Camera2D.ANCHOR_MODE_DRAG_CENTER
	cam.zoom = Vector2(1.0, 1.0) # 1:1 sem zoom!
	# Vamos posicionar a camera no eixo dos trilhos: X = -190, Y = 500
	cam.global_position = Vector2(-190, 500)
	scene.add_child(cam)
	
	await process_frame
	cam.enabled = true
	cam.make_current()
	
	for i in range(15):
		await process_frame
		
	var img = root.get_viewport().get_texture().get_image()
	img.save_png("res://debug_mundo_1to1.png")
	print("Imagem 1:1 salva com sucesso!")
	quit(0)
