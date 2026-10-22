extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var player=world.get_node("Structures/Player");player.navigation_layer="cabos";player.collision_mask=4
	var query := PhysicsShapeQueryParameters2D.new();var shape := CircleShape2D.new();shape.radius=11;query.shape=shape;query.collision_mask=4
	for point in [Vector2(1641,-417),Vector2(1641,-105),Vector2(1905,-105),Vector2(1640,-104)]:
		query.transform=Transform2D(0,point);print(point," walk=",world.is_walkable(point))
		for hit in world.get_world_2d().direct_space_state.intersect_shape(query):
			print(" block=",hit.collider.get_path()," shape=",hit.shape)
			var index: int=hit.shape;var owner_id: int=hit.collider.shape_find_owner(index);var shape_node: CollisionShape2D=hit.collider.shape_owner_get_owner(owner_id);print(shape_node.shape.a," -> ",shape_node.shape.b)
	world.queue_free();await process_frame;quit(0)
