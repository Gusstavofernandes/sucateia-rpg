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
	
	var castle = world.get_node_or_null("Structures/house_3")
	if castle:
		castle.visible = false
		
	var positions = [
		Vector2(1140, 240),
		Vector2(1100, 200),
		Vector2(1060, 180),
		Vector2(1060, 220),
		Vector2(1060, 260),
		Vector2(1060, 300),
		Vector2(1000, 200),
		Vector2(1000, 250),
		Vector2(1120, 180),
		Vector2(1140, 150)
	]
	
	_run_calib(positions)

func _run_calib(positions: Array) -> void:
	var player = world.get_node("Structures/Player")
	for i in range(positions.size()):
		var p = positions[i]
		cam.position = p
		player.position = p
		await process_frame
		await process_frame
		await process_frame
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/calib_%d_%d.png" % [int(p.x), int(p.y)]
		img.save_png(out_path)
		print("Salvo: ", out_path)
	quit(0)
