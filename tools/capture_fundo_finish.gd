extends SceneTree

const CAPTURE_DIR := "res://tools/fundo_finish_captures"
const CAPTURE_IDS := ["full", "PocoVelho", "Bombas", "Descarte", "Maquinas", "Reservatorio", "Ruinas", "Valvulas"]

func _sha256(path: String) -> String:
	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		return ""
	var hash := HashingContext.new()
	hash.start(HashingContext.HASH_SHA256)
	hash.update(file.get_buffer(file.get_length()))
	return hash.finish().hex_encode()

func _initialize() -> void:
	call_deferred("_capture_all")

func _capture_all() -> void:
	get_root().size = Vector2i(1600, 900)
	DirAccess.make_dir_recursive_absolute(ProjectSettings.globalize_path(CAPTURE_DIR))
	var packed: PackedScene = load("res://maps/fundo_ferro/fundo_ferro.tscn")
	var world: Node2D = packed.instantiate()
	get_root().add_child(world)
	current_scene = world
	var hud := world.get_node_or_null("HUD")
	for _frame in range(20):
		await process_frame
	await RenderingServer.frame_post_draw
	await physics_frame
	if hud is CanvasLayer:
		hud.visible = false # Capture-only: keep the approved gameplay HUD out of reference screenshots.
	print("CAPTURE harness ready size=", get_root().size)
	var player: Node2D = world.get_node("Structures/Player")
	var camera: Camera2D = world.get_node("Structures/Player/Camera")
	camera.position_smoothing_enabled = false
	camera.enabled = true
	camera.make_current()
	var manifest: Dictionary = {
		"engine": Engine.get_version_info(),
		"requested_window": [1600, 900],
		"scene_tree_window_size": [get_root().size.x, get_root().size.y],
		"capture_pass": "20 process frames plus RenderingServer.frame_post_draw per shot",
		"shots": []
	}
	for shot_id: String in CAPTURE_IDS:
		if shot_id == "full":
			player.position = Vector2(2210, 1400)
			camera.zoom = Vector2(0.34, 0.34)
			camera.limit_left = 200
			camera.limit_right = 4200
			camera.limit_top = -300
			camera.limit_bottom = 3000
		else:
			var room: Node2D = world.get_node("Rooms/" + shot_id)
			player.position = room.position
			camera.zoom = Vector2(0.9, 0.9)
		for _frame in range(20):
			await process_frame
		await RenderingServer.frame_post_draw
		var image: Image = get_root().get_texture().get_image()
		var path := CAPTURE_DIR + "/fundo_" + shot_id + ".png"
		var error := image.save_png(path)
		print("CAPTURE fundo_", shot_id, " size=", image.get_size(), " sha256=", _sha256(path), " error=", error)
		if error != OK:
			quit(error)
			return
		if manifest.get("actual_capture_size", []).is_empty():
			manifest["actual_capture_size"] = [image.get_width(), image.get_height()]
		manifest["shots"].append({"id": shot_id, "file": "fundo_" + shot_id + ".png", "width": image.get_width(), "height": image.get_height(), "sha256": _sha256(path)})
	var manifest_file := FileAccess.open(CAPTURE_DIR + "/manifest.json", FileAccess.WRITE)
	manifest_file.store_string(JSON.stringify(manifest, "\t"))
	world.queue_free()
	await process_frame
	quit(0)
