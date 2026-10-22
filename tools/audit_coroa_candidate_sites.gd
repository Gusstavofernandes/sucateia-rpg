extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func _run_free(node: Node) -> void:
	if node:
		node.queue_free()

func _bounds(sprite: Sprite2D) -> Rect2:
	var half: Vector2 = Vector2(sprite.texture.get_size()) * sprite.global_scale.abs() * 0.5
	var min_pt := Vector2(INF, INF)
	var max_pt := Vector2(-INF, -INF)
	for corner in [Vector2(-half.x,-half.y), Vector2(half.x,-half.y), Vector2(half.x,half.y), Vector2(-half.x,half.y)]:
		var point: Vector2 = sprite.global_position + corner.rotated(sprite.global_rotation)
		min_pt = min_pt.min(point)
		max_pt = max_pt.max(point)
	return Rect2(min_pt, max_pt-min_pt)

func _has_floor(point: Vector2, floors: Array[TileMapLayer]) -> bool:
	for floor: TileMapLayer in floors:
		if floor.get_cell_source_id(floor.local_to_map(floor.to_local(point))) != -1:
			return true
	return false

func run() -> void:
	var world: Node2D = (load("res://maps/sucateia/sucateia.tscn") as PackedScene).instantiate()
	root.add_child(world)
	await process_frame
	world.get_node("CoroaDistrict").queue_free()
	await process_frame
	await physics_frame
	var player: CharacterBody2D = world.get_node("Structures/Player")
	var floors: Array[TileMapLayer] = [world.get_node("Ground/TerraceFloor"), world.get_node_or_null("MarketDistrict/MarketFloor"), world.get_node_or_null("AltoLixoDistrict/AltoFloor"), world.get_node_or_null("ForjasRasasDistrict/ForjasFloor")]
	floors = floors.filter(func(layer: TileMapLayer) -> bool: return layer != null)
	var blockers: Array[Dictionary] = []
	var scenery: Array[Dictionary] = []
	for node in world.find_children("*", "Sprite2D", true, false):
		var sprite := node as Sprite2D
		if not sprite.texture:
			continue
		var file: String = sprite.texture.resource_path.get_file()
		var box := _bounds(sprite)
		if file in ["house.png", "house_stack.png", "market_stall.png", "tenement.png", "cable_tower.png", "scrap_colossus.png"]:
			blockers.append({"box":box,"name":sprite.get_path(),"asset":file})
		elif file not in ["market_dirt.png", "foundation.png", "metal_repair.png", "light.svg", "floor_atlas.png"]:
			scenery.append({"box":box,"name":sprite.get_path(),"asset":file})
	var query := PhysicsShapeQueryParameters2D.new()
	var circle := CircleShape2D.new()
	circle.radius = 40.0
	query.shape = circle
	query.collision_mask = 1
	var space: PhysicsDirectSpaceState2D = world.get_world_2d().direct_space_state
	var sites: Array[Dictionary] = []
	for center_y in range(180, 721, 20):
		for center_x in range(900, 2201, 20):
			var center := Vector2(center_x,center_y)
			var visual_box := Rect2(center-Vector2(72,82),Vector2(144,164))
			var blocked := false
			for old in blockers:
				if visual_box.intersects(old["box"]):
					blocked = true
					break
			if blocked:
				continue
			var body_contact := center+Vector2(0,62)
			var grounded := true
			for point in [body_contact, body_contact+Vector2(-37,0), body_contact+Vector2(37,0)]:
				if not world.is_surface_walkable(point) or not _has_floor(point,floors):
					grounded=false
					break
				query.transform=Transform2D(0.0,point)
				query.exclude=[player.get_rid()]
				var docks: Node2D=world.get_node_or_null("DocasDistrict")
				if docks:query.exclude.append_array(docks.water_exclusions(point))
				if not space.intersect_shape(query,1).is_empty():
					grounded=false
					break
			if not grounded:
				continue
			var props: Array[String]=[]
			for item in scenery:
				var bounds: Rect2=item["box"]
				if not visual_box.intersects(bounds):
					continue
				var ratio: float=visual_box.intersection(bounds).get_area()/maxf(1.0,bounds.get_area())
				if ratio >= 0.08:
					props.append("%s:%0.0f" % [item["asset"],ratio*100.0])
			sites.append({"center":center,"props":props,"score":props.size()})
	sites.sort_custom(func(a: Dictionary,b: Dictionary) -> bool:
		if a["score"]==b["score"]:return a["center"].y<b["center"].y
		return a["score"]<b["score"])
	print("SUPPORTED_CROWN_SITES=",sites.size())
	for i in mini(60,sites.size()):
		print(sites[i]["center"]," significant_existing_props=",sites[i]["props"])
	world.queue_free()
	await process_frame
	quit(0)
