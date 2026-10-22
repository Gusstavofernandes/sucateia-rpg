extends Node

var step = 0
var positions = [Vector2(300, 380), Vector2(1500, 400), Vector2(2700, 680)]
var names = ["sewer_west.png", "sewer_center.png", "sewer_east.png"]


func _ready() -> void:
	await get_tree().process_frame
	await get_tree().process_frame
	_capture_loop()


func _capture_loop() -> void:
	var player = get_node_or_null("../Player")
	for i in range(positions.size()):
		if player:
			player.global_position = positions[i]
		await get_tree().create_timer(0.35).timeout
		var img = get_viewport().get_texture().get_image()
		var p = ProjectSettings.globalize_path("res://" + names[i])
		img.save_png(p)
		print("Capturado: ", names[i], " em ", positions[i])
	get_tree().quit()
