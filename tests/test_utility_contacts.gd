extends SceneTree

func _initialize() -> void:call_deferred("run")

func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	await physics_frame
	var utility: Node2D=world.get_node_or_null("ConnectedUtilities")
	if utility==null:
		push_error("Coastal drains and core feeder need an anchored connection layout")
		quit(1)
		return
	var count:=0
	for arch in utility.get_node("WallDrains").get_children():
		var wall_y: float=arch.get_meta("wall_y")
		var top: float=arch.get_meta("painted_top_y")
		if top>wall_y+16 or top<wall_y-20:
			push_error("Drain masonry is detached from retaining wall: "+str(arch.name))
			quit(1)
			return
		count+=1
	if count!=4:
		push_error("Expected four fitted wall drains")
		quit(1)
		return
	var sections: Array=utility.get_node("CoreFeeder").get_children()
	for i in range(sections.size()):
		var item: Sprite2D=sections[i]
		var ports: PackedVector2Array=item.get_meta("ports_local")
		var targets: PackedVector2Array=item.get_meta("ports_world")
		for j in range(2):
			if item.to_global(ports[j]).distance_to(targets[j])>.1:
				push_error("Pipe flange misses target")
				quit(1)
				return
		if i>0:
			var previous: PackedVector2Array=sections[i-1].get_meta("ports_world")
			if previous[1].distance_to(targets[0])>.1:
				push_error("Gap in core feeder junction")
				quit(1)
				return
	for name in ["DeckAltoLixo","DeckMercado","DeckForjas"]:
		var stair: Sprite2D=world.find_child(name,true,false)
		if stair.z_index!=0 or stair.get_parent().get_parent().get_parent()!=world.get_node("Structures"):
			push_error("Stair is still drawn over foreground house roofs")
			quit(1)
			return
	print("PASS:4 drains intersect retaining-wall face;feeder flanges continuous within0.1px;3 stairs share house depth")
	world.queue_free()
	await process_frame
	quit(0)
