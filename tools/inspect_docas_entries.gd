extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var shape := CircleShape2D.new();shape.radius=11;var query := PhysicsShapeQueryParameters2D.new();query.shape=shape;query.collision_mask=1;var space := world.get_world_2d().direct_space_state
	for marker in world.get_node("DocasDistrict/Connections").get_children():
		var center := Vector2(Vector2i(marker.position/24))*24+Vector2(12,12)
		for point in [marker.position,center]:
			query.transform=Transform2D(0,point);print("DOCAS entry ",marker.name," point=",point," walk=",world.is_surface_walkable(point))
			for hit in space.intersect_shape(query,10):print("DOCAS blocking=",hit.collider.get_path()," at=",hit.collider.global_position)
	world.queue_free();await process_frame;quit(0)
