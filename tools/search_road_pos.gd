extends SceneTree

var frame_count := 0
var cam: Camera2D
var world: Node2D
var test_points = [
	Vector2(1100, 400),
	Vector2(1100, 600),
	Vector2(1100, 800),
	Vector2(1100, 1000),
	Vector2(1100, 1200),
	Vector2(1100, 1400)
]
var idx = 0

func _init() -> void:
	world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var pcam = world.get_node_or_null("Structures/Player/Camera")
	if pcam:
		pcam.enabled = false
	
	cam = Camera2D.new()
	cam.enabled = true
	cam.zoom = Vector2(1.0, 1.0) # Zoom nativo do jogo
	world.add_child(cam)
	
	_next_cam()

func _next_cam() -> void:
	if idx < test_points.size():
		cam.position = test_points[idx]
		print("Testando cam em: ", test_points[idx])
	else:
		quit(0)

func _process(_delta: float) -> bool:
	frame_count += 1
	if frame_count == 2:
		cam.make_current()
	if frame_count % 10 == 0:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/search_road_%d.png" % int(test_points[idx].y)
		img.save_png(out_path)
		print("Salvo: ", out_path)
		idx += 1
		if idx >= test_points.size():
			quit(0)
			return true
		else:
			cam.position = test_points[idx]
	return false
