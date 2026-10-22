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
	world.add_child(cam)
	
	_take_screenshots()

func _take_screenshots() -> void:
	var player = world.get_node("Structures/Player")
	
	# 1. Posição idêntica à foto do usuário: personagem na soleira da escada (y = -1500)
	player.position = Vector2(1060, -1500)
	cam.position = Vector2(1060, -1520)
	cam.zoom = Vector2(1.0, 1.0)
	await process_frame
	await process_frame
	await process_frame
	var img1 = root.get_viewport().get_texture().get_image()
	var path1 = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/final_castle_at_player_photo.png"
	img1.save_png(path1)
	print("Salvo 1: ", path1)
	
	# 2. Visão ampla mostrando o castelo monumental completo e as casas da cidade abaixo
	cam.position = Vector2(1100, -1850)
	cam.zoom = Vector2(0.55, 0.55)
	await process_frame
	await process_frame
	await process_frame
	var img2 = root.get_viewport().get_texture().get_image()
	var path2 = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/final_castle_panoramic.png"
	img2.save_png(path2)
	print("Salvo 2: ", path2)
	
	quit(0)
