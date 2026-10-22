extends SceneTree

var frame_count := 0

func _init() -> void:
	var world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var player = world.get_node_or_null("Structures/Player")
	if player:
		player.position = Vector2(1882, 1063)

func _process(_delta: float) -> bool:
	frame_count += 1
	if frame_count > 15:
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/bridge_current_closeup.png"
		img.save_png(out_path)
		print("Screenshot salva em: ", out_path)
		quit(0)
		return true
	return false
