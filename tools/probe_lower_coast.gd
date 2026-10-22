extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);await physics_frame;await physics_frame
	var q := PhysicsShapeQueryParameters2D.new();var s := CircleShape2D.new();s.radius=11;q.shape=s;q.collision_mask=1
	for at in [Vector2(1116,1632),Vector2(1128,1632),Vector2(1140,1632)]:
		q.transform=Transform2D(0,at);var hits := world.get_world_2d().direct_space_state.intersect_shape(q)
		var names: Array[String]=[]
		for hit in hits:names.append(str(hit.collider.get_path()))
		print("PUMP approach ",at," blockers=",names)
	quit(0)
