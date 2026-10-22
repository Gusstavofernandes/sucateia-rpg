extends SceneTree

var frame_count := 0
var cam: Camera2D

func _init() -> void:
	var world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var pcam = world.get_node_or_null("Structures/Player/Camera")
	if pcam:
		pcam.enabled = false
	
	var player = world.get_node_or_null("Structures/Player")
	if player:
		# Player no fim da estrada de pedra, pronto para subir os degraus em frente ao Castelo
		player.position = Vector2(1060, 370)
		player.z_as_relative = false
		player.z_index = 4
	
	cam = Camera2D.new()
	cam.enabled = true
	# Enquadramento mostrando a base, os degraus, a saída da cidade e a majestosa torre do relógio
	cam.position = Vector2(1060, 0)
	cam.zoom = Vector2(0.5, 0.5)
	world.add_child(cam)

func _process(_delta: float) -> bool:
	frame_count += 1
	if frame_count == 2:
		cam.make_current()
	if frame_count > 15:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_ingame_final.png"
		img.save_png(out_path)
		print("Screenshot final salva em: ", out_path)
		quit(0)
		return true
	return false
