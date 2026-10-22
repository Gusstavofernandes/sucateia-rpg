extends SceneTree

var frame_count := 0
var cam: Camera2D
var world: Node2D

func _init() -> void:
	world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var pcam = world.get_node_or_null("Structures/Player/Camera")
	if pcam:
		pcam.enabled = false
	
	# Esconder house_3 temporariamente para ver exatamente o cenário original da foto
	var h3 = world.get_node("Structures/house_3")
	h3.visible = false
	
	# Testar player em (1060, -20)
	var player = world.get_node_or_null("Structures/Player")
	if player:
		player.position = Vector2(1060, -20)
		player.z_as_relative = false
		player.z_index = 10
	
	cam = Camera2D.new()
	cam.enabled = true
	# A câmera do player no jogo normal segue o player em zoom (1.0, 1.0) ou zoom normal
	cam.position = Vector2(1060, -20)
	cam.zoom = Vector2(1.0, 1.0)
	world.add_child(cam)

func _process(_delta: float) -> bool:
	frame_count += 1
	if frame_count == 2:
		cam.make_current()
	if frame_count > 15:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/match_user_photo.png"
		img.save_png(out_path)
		print("Salvo match_user_photo")
		quit(0)
		return true
	return false
