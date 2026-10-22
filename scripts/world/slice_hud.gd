extends CanvasLayer
func toggle() -> void:
	$Panel.visible = not $Panel.visible
func on_floor(world: Node, path: String, point: Vector2) -> bool:
	var floor: TileMapLayer=world.get_node_or_null(path)
	return floor!=null and floor.get_cell_source_id(floor.local_to_map(floor.to_local(point)))!=-1
func on_amarras_bridge(world: Node,point: Vector2) -> bool:
	var area := world.get_node_or_null("PassagemAmarrasDistrict")
	if area:
		for polygon in area.get_meta("walk_polygons",[]):
			if Geometry2D.is_point_in_polygon(point,polygon):return true
	return false
func _process(_delta: float) -> void:
	var player: Node2D = get_tree().get_first_node_in_group("player")
	if not player: return
	var district := "NÚCLEO DE SUCATEIA"
	var world := get_tree().current_scene
	if world:
		if player.get("navigation_layer")=="cabos":district="OS CABOS / CAMADA ELEVADA"
		elif world.has_node("DocasDistrict") and world.get_node("DocasDistrict").is_walkable(player.position):district="DOCAS / CAIS DE SUCATEIA"
		elif on_floor(world,"PassagemAmarrasDistrict/AmarrasFloor",player.global_position):district="PASSAGEM DAS AMARRAS"
		elif on_floor(world,"ForjasRasasDistrict/ForjasFloor",player.global_position):district="FORJAS RASAS"
		elif on_amarras_bridge(world,player.global_position):district="PASSAGEM DAS AMARRAS"
		elif on_floor(world,"AltoLixoDistrict/AltoFloor",player.global_position):district="ALTO-LIXO"
		elif on_floor(world,"MarketDistrict/MarketFloor",player.global_position):district="MERCADO DOS RESTOS"
		elif player.position.y>1170:district="COSTA / MANUTENÇÃO"
		elif player.position.x>1950:district="OS CABOS / PASSARELA"
		var entries: Node=world.get_node_or_null("LayerEntrances")
		if entries:
			for entry in entries.get_children():
				if entry is Area2D and player.global_position.distance_to(entry.global_position)<=52:
					district="ACESSO FUNDO-FERRO / SUPERFÍCIE";break
	$Panel/District.text = district
