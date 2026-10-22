extends SceneTree

var frame_count := 0
var cam: Camera2D
var test_y_values = [280, 220, 160]
var current_test_idx = 0
var world: Node2D

func _init() -> void:
	world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var pcam = world.get_node_or_null("Structures/Player/Camera")
	if pcam:
		pcam.enabled = false
	
	cam = Camera2D.new()
	cam.enabled = true
	cam.position = Vector2(1060, 0)
	cam.zoom = Vector2(0.55, 0.55)
	world.add_child(cam)
	
	_apply_y(test_y_values[0])

func _apply_y(target_y: float) -> void:
	var h3 = world.get_node("Structures/house_3")
	h3.position = Vector2(1060, target_y)

func _process(_delta: float) -> bool:
	frame_count += 1
	if frame_count == 2:
		cam.make_current()
	
	# A cada 10 frames após estabilização, salva e troca
	if frame_count == 15:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_test_y280.png"
		img.save_png(out_path)
		print("Salvo y=280")
		_apply_y(220)
	elif frame_count == 30:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_test_y220.png"
		img.save_png(out_path)
		print("Salvo y=220")
		_apply_y(160)
	elif frame_count == 45:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_test_y160.png"
		img.save_png(out_path)
		print("Salvo y=160")
		_apply_y(100)
	elif frame_count == 60:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_test_y100.png"
		img.save_png(out_path)
		print("Salvo y=100")
		quit(0)
		return true
	return false
