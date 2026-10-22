extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var shape := CircleShape2D.new();shape.radius=11;var query := PhysicsShapeQueryParameters2D.new();query.shape=shape;query.collision_mask=1;var space := world.get_world_2d().direct_space_state
	for route in world.get_node("MarketDistrict/UrbanRoutes").get_children():
		for point in route.get_meta("points"):
			var cell := Vector2i(point/24);var actual := Vector2(cell)*24+Vector2(12,12);query.transform=Transform2D(0,actual)
			for hit in space.intersect_shape(query,10):print("SURFACE ",route.name," waypoint=",point," grid=",actual," collider=",hit.collider.get_path()," at=",hit.collider.global_position)
	world.queue_free();await process_frame;quit(0)
