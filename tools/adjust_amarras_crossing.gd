extends SceneTree
func _initialize() -> void:call_deferred("run")
func own(node: Node,world: Node) -> void:
	for child in node.get_children():child.scene_file_path="";child.owner=world;own(child,world)
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world)
	var bridge: Node2D=world.get_node("PassagemAmarrasDistrict/Bridges/PonteDasCorrentes")
	for child in bridge.get_children():
		if child is Sprite2D and child.texture.resource_path.ends_with("suspension_bridge_ew.png"):child.position.y=275
		if child is StaticBody2D:
			for collision in child.get_children():
				if collision is CollisionShape2D:collision.shape.size.x=500;collision.position.x=3685
	var route: Marker2D=world.get_node("PassagemAmarrasDistrict/Routes/CircuitoInferior")
	route.set_meta("points",PackedVector2Array([Vector2(4240,730),Vector2(4560,835),Vector2(4950,900),Vector2(5230,850),Vector2(5440,830),Vector2(5480,565)]))
	var segments: Array[Vector4]=[]
	for node in world.get_node("PassagemAmarrasDistrict/Routes").get_children():
		var points: PackedVector2Array=node.get_meta("points")
		for i in range(points.size()-1):segments.append(Vector4(points[i].x,points[i].y,points[i+1].x,points[i+1].y))
	var floor: TileMapLayer=world.get_node("PassagemAmarrasDistrict/AmarrasFloor");floor.material.set_shader_parameter("route_count",segments.size());while segments.size()<32:segments.append(Vector4.ZERO)
	floor.material.set_shader_parameter("route_segments",segments)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world,world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("AMARRAS crossing adjustment saved=",error," approved approach kept clear; lower route follows canal end")
	world.queue_free();world=null;packed=null;await process_frame;await process_frame;quit(error)
