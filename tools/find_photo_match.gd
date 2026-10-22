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
	cam.zoom = Vector2(1.0, 1.0) # Zoom padrão de jogo
	world.add_child(cam)
	
	# Vamos testar o player e a câmera em várias posições e salvar
	var test_positions = [
		Vector2(1130, 620),
		Vector2(1100, 750),
		Vector2(850, 650),
		Vector2(600, 700),
		Vector2(550, 600),
		Vector2(1050, 850),
		Vector2(1150, 950),
		Vector2(1120, 1060)
	]
	
	# Vamos rodar em background frame a frame
	_run_tests(test_positions)

func _run_tests(positions: Array) -> void:
	for i in range(positions.size()):
		var pos = positions[i]
		cam.position = pos
		var player = world.get_node("Structures/Player")
		player.position = pos
		await process_frame
		await process_frame
		await process_frame
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/photo_match_%d_%d.png" % [int(pos.x), int(pos.y)]
		img.save_png(out_path)
		print("Salvo: ", out_path)
	quit(0)
