extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func run() -> void:
	var world: Node2D = (load("res://maps/sucateia/sucateia.tscn") as PackedScene).instantiate()
	root.add_child(world)
	await process_frame
	var district := world.get_node("CoroaDistrict")
	district.queue_free()
	await process_frame
	var occupied: Array[Dictionary] = []
	for node in world.find_children("*", "Sprite2D", true, false):
		var sprite := node as Sprite2D
		if not sprite.texture:
			continue
		var asset: String = sprite.texture.resource_path.get_file()
		if asset not in ["house.png", "house_stack.png", "market_stall.png", "tenement.png", "cable_tower.png", "scrap_colossus.png"]:
			continue
		var half: Vector2 = Vector2(sprite.texture.get_size()) * sprite.global_scale.abs() * 0.5
		var radians: float = sprite.global_rotation
		var corners: Array[Vector2] = [Vector2(-half.x,-half.y), Vector2(half.x,-half.y), Vector2(half.x,half.y), Vector2(-half.x,half.y)]
		var minimum := Vector2(INF,INF)
		var maximum := Vector2(-INF,-INF)
		for corner in corners:
			var point: Vector2 = sprite.global_position + corner.rotated(radians)
			minimum = minimum.min(point)
			maximum = maximum.max(point)
		var rect := Rect2(minimum, maximum-minimum)
		occupied.append({"rect":rect,"path":str(sprite.get_path()),"asset":asset,"position":sprite.global_position})
	var sites: Array[String] = []
	for center_y in range(160, 761, 40):
		for center_x in range(900, 2241, 40):
			var target := Rect2(Vector2(center_x - 124, center_y - 126), Vector2(248, 252))
			var hits: Array[String] = []
			for old: Dictionary in occupied:
				if target.intersects(old["rect"]):
					hits.append(old["asset"] + "@" + str(old["position"]))
			if hits.is_empty():
				sites.append("%s free AABB %s" % [str(Vector2(center_x,center_y)), str(target)])
	print("CROWN_ARCHITECTURE_FREE_AABB_SITES=", sites.size())
	for i in mini(30,sites.size()):
		print(sites[i])
	var candidate := Rect2(Vector2(1416,274), Vector2(248,252))
	print("CANDIDATE_SOUTH_OF_MARKET ", candidate)
	var environmental: Array[String] = []
	for node in world.find_children("*", "Sprite2D", true, false):
		var sprite := node as Sprite2D
		if not sprite.texture:
			continue
		var asset: String = sprite.texture.resource_path.get_file()
		if asset in ["market_dirt.png", "foundation.png", "light.svg"]:
			continue
		var half: Vector2 = Vector2(sprite.texture.get_size()) * sprite.global_scale.abs() * 0.5
		var corners: Array[Vector2] = [Vector2(-half.x,-half.y), Vector2(half.x,-half.y), Vector2(half.x,half.y), Vector2(-half.x,half.y)]
		var minimum := Vector2(INF,INF)
		var maximum := Vector2(-INF,-INF)
		for corner in corners:
			var point: Vector2 = sprite.global_position + corner.rotated(sprite.global_rotation)
			minimum = minimum.min(point)
			maximum = maximum.max(point)
		var rect := Rect2(minimum, maximum-minimum)
		if candidate.intersects(rect):
			var intersection := candidate.intersection(rect)
			var ratio := intersection.get_area()/maxf(1.0,rect.get_area())
			if ratio>=0.05:
				environmental.append("%0.1f%% %s %s at %s" % [ratio*100,asset,str(sprite.get_path()),str(sprite.global_position)])
	for item in environmental:
		print(item)
	print("SIGNIFICANT_NON_GROUND_PROPS ",environmental.size())
	world.queue_free()
	await process_frame
	quit(0)
