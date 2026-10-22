extends SceneTree

func _initialize() -> void:
	call_deferred("run")

func run() -> void:
	# Restore from bak
	var dir := DirAccess.open("res://maps/fundo_ferro")
	dir.copy("res://maps/fundo_ferro/fundo_ferro.tscn.bak", "res://maps/fundo_ferro/fundo_ferro.tscn")
	
	var scene: PackedScene = load("res://maps/fundo_ferro/fundo_ferro.tscn")
	var world: Node2D = scene.instantiate()
	
	var rooms = world.get_node("Rooms")
	var routes = world.get_node("Routes")
	var floor: TileMapLayer = world.get_node("GroundFloor")
	var structures = world.get_node("Structures")
	var walls = structures.get_node("Walls")

	# 1. Add Room Arena
	if not rooms.has_node("Arena"):
		var marker := Marker2D.new()
		marker.name = "Arena"
		marker.position = Vector2(3900, 1100)
		rooms.add_child(marker)
		marker.owner = world

	# 2. Add Route GaleriaArena strictly orthogonal with 2 curves
	var arena_points := PackedVector2Array([
		Vector2(3480, 750),
		Vector2(3480, 960),
		Vector2(3580, 960),
		Vector2(3900, 960),
		Vector2(3900, 1100)
	])
	if not routes.has_node("GaleriaArena"):
		var route_marker := Marker2D.new()
		route_marker.name = "GaleriaArena"
		route_marker.set_meta("points", arena_points)
		routes.add_child(route_marker)
		route_marker.owner = world

	# 3. Add floor tiles
	# Inside Valvulas navigation corridor: from X=2950 to 3480 along Y=750 (free floor, south of pipe Y=620-655)
	for y in range(14, 18): # Y: ~672 to 864
		for x in range(60, 73): # X: ~2880 to 3504
			var cell := Vector2i(x, y)
			floor.set_cell(cell, 0, Vector2i(posmod(x, 16), posmod(y, 16)))

	# Tunnel Trecho 1: X=3480, Y from 750 to 960
	for y in range(15, 22): # Y: ~720 to 1056
		for x in range(71, 74): # X: ~3408 to 3552
			var cell := Vector2i(x, y)
			floor.set_cell(cell, 0, Vector2i(posmod(x, 16), posmod(y, 16)))

	# Tunnel Trecho 2: Y=960, X from 3480 to 3580 (and entering Arena)
	for y in range(19, 22): # Y: ~912 to 1056
		for x in range(72, 76): # X: ~3456 to 3648
			var cell := Vector2i(x, y)
			floor.set_cell(cell, 0, Vector2i(posmod(x, 16), posmod(y, 16)))

	# Arena polygon: center 3900, 1100, size 640x520
	var a := Vector2(3900, 1100) - Vector2(640, 520) / 2.0
	var b := Vector2(3900, 1100) + Vector2(640, 520) / 2.0
	var arena_polygon := PackedVector2Array([
		a + Vector2(60, 0), Vector2(b.x - 40, a.y), Vector2(b.x, a.y + 60),
		b - Vector2(0, 45), b - Vector2(70, 0), Vector2(a.x + 45, b.y),
		Vector2(a.x, b.y - 70), Vector2(a.x, a.y + 45)
	])

	for y in range(17, 30):
		for x in range(74, 89):
			var cell := Vector2i(x, y)
			var at := Vector2(x * 48 + 24, y * 48 + 24)
			if Geometry2D.is_point_in_polygon(at, arena_polygon):
				floor.set_cell(cell, 0, Vector2i(posmod(x, 16), posmod(y, 16)))

	# 4. Remove any existing wall sitting on newly opened floor
	var walls_to_remove = []
	for child in walls.get_children():
		var cell = floor.local_to_map(child.position)
		if floor.get_cell_source_id(cell) != -1:
			walls_to_remove.append(child)
	for w in walls_to_remove:
		walls.remove_child(w)
		w.queue_free()

	# 5. Add new walls for edges in the new region (x >= 65)
	for cell in floor.get_used_cells():
		if cell.x < 65:
			continue
		for side in [Vector2i.LEFT, Vector2i.RIGHT, Vector2i.UP, Vector2i.DOWN]:
			if floor.get_cell_source_id(cell + side) != -1:
				continue
			var at := floor.map_to_local(cell) + Vector2(side) * 24
			var exists = false
			for c in walls.get_children():
				if c.position.distance_to(at) < 10:
					exists = true
					break
			if exists:
				continue

			var sprite := Sprite2D.new()
			sprite.texture = load("res://assets/reconstruction/fundo_wall.png")
			sprite.position = at
			sprite.scale = Vector2(61, 32) / Vector2(sprite.texture.get_size())
			sprite.rotation = PI/2 if side.x != 0 else 0
			sprite.modulate = Color(0.80, 0.86, 0.77, 1)
			walls.add_child(sprite)
			sprite.owner = world

			var body := StaticBody2D.new()
			body.position = at + Vector2(side) * 12
			walls.add_child(body)
			body.owner = world
			var collision := CollisionShape2D.new()
			var shape := RectangleShape2D.new()
			shape.size = Vector2(26, 48) if side.x != 0 else Vector2(48, 26)
			collision.shape = shape
			body.add_child(collision)
			collision.owner = world

	# 6. Update Camera limits
	var player = structures.get_node_or_null("Player")
	if player:
		var cam = player.get_node_or_null("Camera")
		if cam:
			cam.limit_right = 4400

	# 7. Save packed scene
	var packed := PackedScene.new()
	var err := packed.pack(world)
	if err == OK:
		err = ResourceSaver.save(packed, "res://maps/fundo_ferro/fundo_ferro.tscn")
		print("Successfully patched scene with orthogonal route! err=", err)
	quit(err)
