extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame;var floor: TileMapLayer=world.get_node("ForjasRasasDistrict/ForjasFloor")
	for y in range(65,290,10):
		var good := true
		for delta in [Vector2(-31,20),Vector2(31,30),Vector2(-19,26)]:
			var point: Vector2=Vector2(3122,y)+delta
			if not world.is_surface_walkable(point) or floor.get_cell_source_id(floor.local_to_map(point))==-1:good=false
		if good:print("DRAIN dry tile center ",Vector2(3122,y))
	world.queue_free();await process_frame;quit(0)
