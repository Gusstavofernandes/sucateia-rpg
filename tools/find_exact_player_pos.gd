extends SceneTree

var world: Node2D

func _init() -> void:
	world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	# Procurar nós em MarketDistrict e estruturas
	# Imprimir posição de todas as casas que têm telhado gótico / escada
	print("Procurando casinhas próximas...")
	for child in world.get_node("Structures").get_children():
		if child.name.begins_with("house_") or "@Node2D@" in child.name:
			print(child.name, " pos=", child.position)
			
	quit(0)
