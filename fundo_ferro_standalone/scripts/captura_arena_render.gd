extends Node2D

var frames := 0

func _ready() -> void:
	print("--- CAPTURA ARENA STANDALONE INICIADA ---")
	var player = $Player
	var cam = player.get_node("Camera2D")
	cam.position_smoothing_enabled = false
	
	# Posiciona o jogador no meio da Arena
	player.position = Vector2(3860, 1100)
	cam.zoom = Vector2(0.95, 0.95)
	
	$HUDCanvas.visible = false

func _process(_delta: float) -> void:
	frames += 1
	if frames == 50:
		await RenderingServer.frame_post_draw
		var img = get_viewport().get_texture().get_image()
		var err = img.save_png("res://captura_arena_standalone_oficial.png")
		print("CAPTURA ARENA STANDALONE SALVA COM SUCESSO: err=", err)
		get_tree().quit(err)
