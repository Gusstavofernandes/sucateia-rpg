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
	
	var castle = world.get_node("Structures/house_3")
	var player = world.get_node("Structures/Player")
	player.position = Vector2(1050, -1500)
	
	# Testar 2 posições refinadas:
	# Opção A: Vector2(1080, -1550)
	# Opção B: Vector2(1100, -1560)
	
	_test_refined(castle, player)

func _test_refined(castle: Node2D, player: Node2D) -> void:
	var opts = [
		Vector2(1080, -1540),
		Vector2(1090, -1550),
		Vector2(1100, -1560)
	]
	
	for i in range(opts.size()):
		var cp = opts[i]
		castle.position = cp
		cam.position = Vector2(cp.x, -1500)
		cam.zoom = Vector2(1.0, 1.0)
		await process_frame
		await process_frame
		await process_frame
		var img = root.get_viewport().get_texture().get_image()
		var p1 = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_opt_%d_%d_zoom1.png" % [int(cp.x), int(cp.y)]
		img.save_png(p1)
		
		# Visão aberta
		cam.position = Vector2(cp.x, -1800)
		cam.zoom = Vector2(0.65, 0.65)
		await process_frame
		await process_frame
		await process_frame
		var img_wide = root.get_viewport().get_texture().get_image()
		var p2 = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_opt_%d_%d_wide.png" % [int(cp.x), int(cp.y)]
		img_wide.save_png(p2)
		print("Salvo opções para: ", cp)
		
	quit(0)
