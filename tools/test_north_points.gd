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
	
	# Testar posições na faixa norte do MarketFloor (onde Y é bem negativo)
	var test_points = [
		Vector2(1050, -1300),
		Vector2(1050, -1400),
		Vector2(1050, -1500),
		Vector2(1050, -1600),
		Vector2(1100, -1350),
		Vector2(1100, -1450),
		Vector2(1100, -1550),
		Vector2(1000, -1350),
		Vector2(1000, -1450),
		Vector2(1000, -1550)
	]
	
	_run_captures(test_points)

func _run_captures(points: Array) -> void:
	var player = world.get_node("Structures/Player")
	for i in range(points.size()):
		var p = points[i]
		cam.position = p
		player.position = p
		await process_frame
		await process_frame
		await process_frame
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/north_match_%d_%d.png" % [int(p.x), int(p.y)]
		img.save_png(out_path)
		print("Salvo: ", out_path)
	quit(0)
