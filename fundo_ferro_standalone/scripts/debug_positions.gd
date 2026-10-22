extends SceneTree

func _init():
	var scene = load("res://scenes/fundo_ferro_master.tscn").instantiate()
	root.add_child(scene)
	
	var tunel = scene.get_node("RedeFerroviariaMina/TunelMinaEntrada")
	var tunel_sprite = tunel.get_node("TunelSprite")
	var estacao = scene.get_node("RedeFerroviariaMina/EstacaoCarga")
	var estacao_sprite = estacao.get_node("PlataformaSprite")
	
	print("--- POSIÇÕES NO GODOT ---")
	print("Tunel global_position: ", tunel.global_position)
	print("TunelSprite global_position: ", tunel_sprite.global_position)
	print("TunelSprite scale: ", tunel_sprite.scale)
	print("TunelSprite texture size: ", tunel_sprite.texture.get_size())
	
	var tunel_h_world = tunel_sprite.texture.get_size().y * tunel_sprite.scale.y
	var tunel_bottom_world = tunel_sprite.global_position.y + tunel_h_world / 2.0
	print("Tunel bottom Y no mundo: ", tunel_bottom_world)
	
	print("\nEstacao global_position: ", estacao.global_position)
	print("PlataformaSprite global_position: ", estacao_sprite.global_position)
	print("PlataformaSprite scale: ", estacao_sprite.scale)
	print("PlataformaSprite texture size: ", estacao_sprite.texture.get_size())
	
	var estacao_h_world = estacao_sprite.texture.get_size().y * estacao_sprite.scale.y
	var estacao_top_world = estacao_sprite.global_position.y - estacao_h_world / 2.0
	print("Estacao top Y no mundo: ", estacao_top_world)
	
	print("\nDIFERENÇA (GAP) NO MUNDO: ", estacao_top_world - tunel_bottom_world)
	
	quit(0)
