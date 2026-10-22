extends SceneTree

func _init() -> void:
	call_deferred("_test_run")

func _test_run() -> void:
	print("--- TESTE DE INICIALIZACAO COMPLETA DE SUCATEIA.TSCN ---")
	var scene = load("res://maps/sucateia/sucateia.tscn")
	var world = scene.instantiate()
	root.add_child(world)
	
	# Aguardar ready
	await process_frame
	
	var exp_node = world.get_node_or_null("AltoWestCaisExpansion")
	if exp_node:
		print("Sucesso! AltoWestCaisExpansion encontrado na arvore com ", exp_node.get_child_count(), " filhos!")
		print("--- SUCATEIA + KHEMET-RA TESTADO E APROVADO! ---")
		quit(0)
	else:
		push_error("ERRO: AltoWestCaisExpansion nao encontrado em Sucateia apos ready!")
		quit(1)
