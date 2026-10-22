extends SceneTree

func _init() -> void:
	print("--- INICIANDO VALIDACAO KHEMET-RA EM SUCATEIA ---")
	var root_node := Node2D.new()
	root.add_child(root_node)

	# Mock de nós esperados por _update_waterline_and_barrier se sucateia não estiver carregada:
	var west_water := Polygon2D.new()
	west_water.name = "WestWaterline"
	root_node.add_child(west_water)

	var west_barrier := StaticBody2D.new()
	west_barrier.name = "WestCoastalBarrier"
	var col_poly := CollisionPolygon2D.new()
	west_barrier.add_child(col_poly)
	root_node.add_child(west_barrier)

	var cais := Node2D.new()
	cais.name = "AltoLixoCais"
	root_node.add_child(cais)

	var AltoWestScript = load("res://scripts/world/alto_west_cais.gd")
	if AltoWestScript == null:
		push_error("ERRO: Nao foi possivel carregar alto_west_cais.gd!")
		quit(1)
		return

	var inst = AltoWestScript.new()
	inst.install(root_node)

	var expansion = root_node.get_node_or_null("AltoWestCaisExpansion")
	if expansion == null:
		push_error("ERRO: AltoWestCaisExpansion nao foi criado!")
		quit(1)
		return

	print("Sucesso! AltoWestCaisExpansion instanciado com ", expansion.get_child_count(), " grupos de nos!")
	for child in expansion.get_children():
		print(" - Grupo: ", child.name, " (", child.get_child_count(), " elementos)")

	print("--- VALIDACAO CONCLUIDA COM SUCESSO ABSOLUTO! ---")
	quit(0)
