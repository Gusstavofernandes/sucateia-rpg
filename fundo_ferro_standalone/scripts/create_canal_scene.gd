extends SceneTree

func _init() -> void:
	var root = Node2D.new()
	root.name = "Canal"
	root.set_script(load("res://scripts/canal.gd"))
	
	var agua = Sprite2D.new()
	agua.name = "Agua"
	agua.z_index = -8
	
	var placeholder = PlaceholderTexture2D.new()
	placeholder.size = Vector2(900, 80)
	agua.texture = placeholder
	agua.centered = true
	
	var mat = ShaderMaterial.new()
	mat.shader = load("res://shaders/agua_canal.gdshader")
	mat.set_shader_parameter("ruido_a", load("res://resources/ruido_a.tres"))
	mat.set_shader_parameter("ruido_b", load("res://resources/ruido_b.tres"))
	mat.set_shader_parameter("tile_px", 256.0)
	mat.set_shader_parameter("velocidade", 0.03)
	mat.set_shader_parameter("distorcao", 0.05)
	mat.set_shader_parameter("borda_largura", 0.14)
	mat.set_shader_parameter("cor_fundo", Color(0.03, 0.12, 0.09, 0.92))
	mat.set_shader_parameter("cor_raso", Color(0.10, 0.30, 0.22, 0.92))
	mat.set_shader_parameter("cor_brilho", Color(0.55, 0.80, 0.45, 1.0))
	mat.set_shader_parameter("cor_espuma", Color(0.45, 0.55, 0.35, 1.0))
	mat.set_shader_parameter("cor_luz", Color(1.0, 0.55, 0.20, 1.0))
	mat.set_shader_parameter("raio_luz", 110.0)
	
	agua.material = mat
	root.add_child(agua)
	agua.owner = root
	
	var scene = PackedScene.new()
	scene.pack(root)
	ResourceSaver.save(scene, "res://scenes/Canal.tscn")
	print("Canal.tscn criado com sucesso!")
	quit()
