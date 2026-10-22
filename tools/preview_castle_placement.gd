extends SceneTree

var frame_count := 0
var cam: Camera2D

func _init() -> void:
	var world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var pcam = world.get_node_or_null("Structures/Player/Camera")
	if pcam:
		pcam.enabled = false
	
	var tex = load("res://assets/generated/structures/monumental_clock_castle.png")
	
	var h3 = world.get_node("Structures/house_3")
	# Encravado na montanha norte exatamente no fim da avenida de saída da cidade
	h3.position = Vector2(1060, 360)
	var arch: Sprite2D = h3.get_node("Architecture")
	arch.texture = tex
	var scale_factor := 1.5
	arch.scale = Vector2(scale_factor, scale_factor)
	arch.position = Vector2(0, -1264.0 * scale_factor * 0.5)
	arch.z_as_relative = false
	arch.z_index = 3
	
	var shadow: Sprite2D = h3.get_node_or_null("@Sprite2D@43")
	if shadow:
		shadow.scale = Vector2(8.0, 2.0)
		shadow.position = Vector2(0, -10)
		shadow.z_as_relative = false
		shadow.z_index = 2
	
	var player = world.get_node_or_null("Structures/Player")
	if player:
		# Player no fim da estrada de pedra, pronto para subir os degraus
		player.position = Vector2(1060, 375)
		player.z_as_relative = false
		player.z_index = 4
	
	cam = Camera2D.new()
	cam.enabled = true
	cam.position = Vector2(1060, 100)
	cam.zoom = Vector2(0.55, 0.55)
	world.add_child(cam)

func _process(_delta: float) -> bool:
	frame_count += 1
	if frame_count == 2:
		cam.make_current()
	if frame_count > 15:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_road_exit_perfect.png"
		img.save_png(out_path)
		print("Screenshot salva em: ", out_path)
		quit(0)
		return true
	return false
