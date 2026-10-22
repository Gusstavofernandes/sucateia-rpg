extends SceneTree

var world: Node2D
var cam: Camera2D

func _init() -> void:
	world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var pcam = world.get_node_or_null("Structures/Player/Camera")
	if pcam:
		pcam.enabled = false
		
	cam = Camera2D.new()
	cam.enabled = true
	cam.zoom = Vector2(1.0, 1.0)
	world.add_child(cam)
	
	# Mover o castelo para o ponto exato onde a entrada fica sobre a posição do personagem na foto
	var castle = world.get_node("Structures/house_3")
	castle.position = Vector2(1050, -1500)
	
	# Testar 3 enquadramentos:
	# 1. Player parado na soleira onde estava na foto (y = -1500)
	# 2. Player um pouco à frente (y = -1420) olhando para a entrada
	# 3. Visão panorâmica (zoom 0.5) mostrando o castelo inteiro e a integração com a cidade
	
	_run_captures(castle)

func _run_captures(castle: Node2D) -> void:
	var player = world.get_node("Structures/Player")
	
	# 1. Posição da foto com a entrada ali
	player.position = Vector2(1050, -1450)
	cam.position = Vector2(1050, -1500)
	cam.zoom = Vector2(1.0, 1.0)
	await process_frame
	await process_frame
	await process_frame
	var img1 = root.get_viewport().get_texture().get_image()
	var path1 = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_entry_at_player_photo.png"
	img1.save_png(path1)
	print("Salvo: ", path1)
	
	# 2. Visão panorâmica (zoom 0.6) mostrando o castelo erguido ao norte e a praça na frente
	cam.position = Vector2(1050, -1800)
	cam.zoom = Vector2(0.6, 0.6)
	await process_frame
	await process_frame
	await process_frame
	var img2 = root.get_viewport().get_texture().get_image()
	var path2 = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_panoramic_north.png"
	img2.save_png(path2)
	print("Salvo: ", path2)
	
	quit(0)
