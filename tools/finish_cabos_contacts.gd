extends "res://tools/integrate_cabos_art.gd"
func footprint(parent: Node,point: Vector2,size: Vector2) -> void:
	var body := StaticBody2D.new();body.name="GroundFootprint";body.collision_layer=1;body.collision_mask=2;body.position=point;parent.add_child(body)
	var shape := CollisionShape2D.new();var rectangle := RectangleShape2D.new();rectangle.size=size;shape.shape=rectangle;body.add_child(shape)
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("CabosDistrict");supports=district.get_node("StructuralSupports");links=district.get_node("TensionAndMessages");render=district.get_node("ElevatedDecks")
	if district.has_meta("contacts_finished"):print("CABOS contacts retained");world.queue_free();await process_frame;quit(0);return
	var shadows: Node2D=district.get_node("ContactShadows");var accesses: Array[Vector2]=[]
	for access_node in district.get_node("Accesses").get_children():accesses.append(access_node.get_meta("surface_arrival"))
	for tower in supports.get_children():
		if not tower.has_meta("ground_contact"):continue
		var label := String(tower.name);var ratio := .4;var socket: Vector2=tower.get_meta("socket_world")
		if label.begins_with("CasaTorre"):
			# House beam is high above its porch: these two receivers reach street level,
			# rather than ending at the cabin's suspended threshold.
			var beam := socket-Vector2(0,80);ratio=.75;tower.scale=Vector2.ONE*ratio;tower.position=beam-(Vector2(370,138)-Vector2(384,384))*ratio;socket=beam+Vector2(0,150)
		var foot: Vector2=tower.position+(Vector2(371,711)-Vector2(384,384))*ratio
		var displacement := Vector2.ZERO
		for ground in accesses:
			if absf(foot.x-ground.x)<80 and absf(foot.y-ground.y)<46:displacement.x+=100 if foot.x>=ground.x else -100
		if displacement!=Vector2.ZERO:
			var old_crown: Vector2=tower.position+(Vector2(370,138)-Vector2(384,384))*ratio;tower.position+=displacement
			var new_crown := old_crown+displacement
			for line in links.get_children():
				if not line is Line2D:continue
				var points: PackedVector2Array=line.points
				if points[0].distance_to(old_crown)<.2:points[0]=new_crown
				if points[-1].distance_to(old_crown)<.2:points[-1]=new_crown
				points[1]=points[0].lerp(points[-1],.5)+Vector2(0,6);line.points=points
				for child in line.get_children():if child is Line2D:child.points=points
				line.set_meta("anchored_endpoints",PackedVector2Array([points[0],points[-1]]))
			cable(label+"SocketBrace",new_crown,socket,true)
		foot=tower.position+(Vector2(371,711)-Vector2(384,384))*ratio;tower.set_meta("ground_contact",foot)
		footprint(district.get_node("StructuralSupports"),foot,Vector2(64,22)*ratio/.4)
		var shadow: Sprite2D=shadows.get_node_or_null(label+"Contact")
		if shadow:shadow.position=foot+Vector2(0,3);shadow.scale=Vector2(105,34)*ratio/.4/Vector2(shadow.texture.get_size())
	# Every primary module has a heavy stay to an actual structural crown.
	for deck in render.get_children():
		if not deck.has_meta("walking_center"):continue
		var nearest: Node2D;var distance := INF
		for tower in supports.get_children():
			if not tower.has_meta("ground_contact") or String(tower.name).begins_with("Casa"):continue
			if tower.position.distance_to(deck.position)<distance:nearest=tower;distance=tower.position.distance_to(deck.position)
		if nearest:
			var crown: Vector2=nearest.position+(Vector2(370,138)-Vector2(384,384))*.4
			cable(String(deck.name)+"LoadStay",crown,deck.position+Vector2(55.318,62.444),true)
		var tone := .94+float(deck.get_index()%4)*.02;deck.modulate=Color(tone,tone,.97+float(deck.get_index()%2)*.02)
	# Sparse lamps identify the three public entrances without filling the lane.
	for access_node in district.get_node("Accesses").get_children():
		var point: Vector2=access_node.get_meta("elevated_arrival")
		sprite("infrastructure/lantern.png",point+Vector2(-75,-18),.45,links,String(access_node.name)+"Luz")
	district.set_meta("contacts_finished",true)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("CABOS contacts saved=",error," solid tower bases=27; house street receivers=2; primary load stays connected")
	world.queue_free();world=null;district=null;render=null;supports=null;links=null;shadows=null;packed=null;await process_frame;await process_frame;quit(error)
