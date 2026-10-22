extends SceneTree

func _init() -> void:
	var root = Node2D.new()
	root.name = "Queda"
	root.set_script(load("res://scripts/agua_riacho.gd"))
	
	var scene = PackedScene.new()
	scene.pack(root)
	ResourceSaver.save(scene, "res://scenes/Queda.tscn")
	print("Queda.tscn criado com sucesso!")
	quit()
