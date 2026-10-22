extends SceneTree

func _init() -> void:
	var noise_a = FastNoiseLite.new()
	noise_a.noise_type = FastNoiseLite.TYPE_SIMPLEX_SMOOTH
	noise_a.seed = 1337
	noise_a.frequency = 0.015
	
	var tex_a = NoiseTexture2D.new()
	tex_a.width = 256
	tex_a.height = 256
	tex_a.seamless = true
	tex_a.noise = noise_a
	ResourceSaver.save(tex_a, "res://resources/ruido_a.tres")
	
	var noise_b = FastNoiseLite.new()
	noise_b.noise_type = FastNoiseLite.TYPE_SIMPLEX_SMOOTH
	noise_b.seed = 9999
	noise_b.frequency = 0.02
	
	var tex_b = NoiseTexture2D.new()
	tex_b.width = 256
	tex_b.height = 256
	tex_b.seamless = true
	tex_b.noise = noise_b
	ResourceSaver.save(tex_b, "res://resources/ruido_b.tres")
	
	print("Ruídos gerados com sucesso pelo Godot!")
	quit()
