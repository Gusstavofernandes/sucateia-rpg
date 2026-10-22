extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=1
	for point in [Vector2(4476,252),Vector2(4476,552),Vector2(4480,260),Vector2(4480,550)]:
		query.transform=Transform2D(0,point);print(point," walkable=",world.is_walkable(point))
		for hit in world.get_world_2d().direct_space_state.intersect_shape(query):print(" blocker=",hit.collider.get_path())
	world.queue_free();await process_frame;quit(0)
