extends RefCounted

const PIPE = "res://assets/generated/props/pipe.png"
const ELBOW = "res://assets/reconstruction/utility_fits/copper_elbow.png"

func group(parent: Node, label: String) -> Node2D:
	var node := Node2D.new()
	node.name=label
	parent.add_child(node)
	return node

func piece(parent: Node2D, label: String, texture: String, ports: PackedVector2Array, targets: PackedVector2Array, basis_x: Vector2, basis_y: Vector2) -> Sprite2D:
	var art := Sprite2D.new()
	art.name=label
	art.texture=load(texture)
	parent.add_child(art)
	var transform := Transform2D(basis_x,basis_y,Vector2.ZERO)
	transform.origin=targets[0]-transform.basis_xform(ports[0])
	art.global_transform=transform
	art.set_meta("ports_local",ports)
	art.set_meta("ports_world",targets)
	art.modulate=Color(.82,.80,.74,1) if texture==PIPE else Color(.54,.55,.50,1)
	return art

func straight(parent: Node2D, label: String, a: Vector2, b: Vector2) -> void:
	var delta:=b-a
	var count:=maxi(1,ceili(delta.length()/112.))
	for i in range(count):
		var start:=a.lerp(b,float(i)/count)
		var finish:=a.lerp(b,float(i+1)/count)
		piece(parent,label+str(i),PIPE,PackedVector2Array([Vector2(-114,0),Vector2(114,0)]),PackedVector2Array([start,finish]),(finish-start)/228.,delta.normalized().orthogonal()*.34)

func elbow(parent: Node2D, label: String, a: Vector2, b: Vector2, swapped: bool) -> void:
	var delta:=b-a
	var x_axis:=Vector2(0,delta.y/720.) if swapped else Vector2(delta.x/720.,0)
	var y_axis:=Vector2(delta.x/665.,0) if swapped else Vector2(0,delta.y/665.)
	piece(parent,label,ELBOW,PackedVector2Array([Vector2(180,365)-Vector2(627,627),Vector2(900,1030)-Vector2(627,627)]),PackedVector2Array([a,b]),x_axis,y_axis)

func wall_strip(parent: Node2D, label: String, a: Vector2, b: Vector2) -> void:
	if a.distance_to(b)<4:return
	var art:=Sprite2D.new()
	art.name=label
	art.texture=load("res://assets/infrastructure/retaining_edge.png")
	art.position=(a+b)*.5
	art.rotation=(b-a).angle()
	art.scale=Vector2((a.distance_to(b)+16)/384.,.38)
	parent.add_child(art)
	art.modulate=Color(.82,.84,.73,1)
	art.set_meta("wall_endpoints",PackedVector2Array([a,b]))

func nearest_shore(point: Vector2, shore: PackedVector2Array) -> Vector2:
	var nearest:=shore[0]
	var distance:=INF
	for i in range(shore.size()-1):
		var candidate:=Geometry2D.get_closest_point_to_segment(point,shore[i],shore[i+1])
		if point.distance_to(candidate)<distance:
			nearest=candidate
			distance=point.distance_to(candidate)
	return nearest

func install(world: Node2D) -> void:
	if not world.has_node("FinishedInfrastructure") or not world.has_node("LowerCoastReworked"):
		return
	var utility:=group(world,"ConnectedUtilities")
	utility.z_index=-12
	var drains:=group(utility,"WallDrains")
	var infrastructure: Node2D=world.get_node("FinishedInfrastructure")
	var target_drain_y := 1435.0
	for old in infrastructure.get_children():
		if not old is Sprite2D or not old.texture:continue
		if old.texture.resource_path.ends_with("/light.svg") and (absf(old.position.y-1498)<.1 or absf(old.position.y-1459)<.1):
			old.position.y = target_drain_y + 24.0
		elif "service_arch" in old.texture.resource_path and (absf(old.position.y-1484)<1.0 or absf(old.position.y-1435)<1.0):
			var arch:=Sprite2D.new()
			arch.name="Drain"+str(int(old.position.x))
			arch.texture=old.texture
			arch.scale=old.scale
			arch.position=Vector2(old.position.x,target_drain_y)
			drains.add_child(arch)
			arch.modulate=Color(.88,.88,.79,1)
			arch.set_meta("wall_y",1418.)
			arch.set_meta("painted_top_y",target_drain_y+(45.-95.)*old.scale.y)
			old.hide()
	# Entradas de portal com placas removidas conforme solicitado
	for label in ["To_fundo","To_docas"]:
		var portal: Node2D = world.get_node_or_null("RegionPortals/"+label)
		if portal:
			portal.queue_free()
	var cont := world.get_node_or_null("RegionalContinuity")
	if cont:
		for i in range(47, 58):
			var node := cont.get_node_or_null("@Sprite2D@" + str(i))
			if node: node.visible = false
			var line := cont.get_node_or_null("@Line2D@" + str(i))
			if line: line.visible = false
	# Remoção dos 3 canos no canal sul solicitados pelo usuário
	var lower_coast: Node2D = world.get_node_or_null("LowerCoastReworked")
	if lower_coast:
		for old in lower_coast.get_children():
			if old is Sprite2D and old.texture and old.texture.resource_path == PIPE:
				if old.position.distance_to(Vector2(1770, 1510)) < 25.0:
					old.hide()
	var infra: Node2D = world.get_node_or_null("FinishedInfrastructure")
	if infra:
		for old in infra.get_children():
			if old is Sprite2D and old.texture and old.texture.resource_path == PIPE:
				if old.position.distance_to(Vector2(1703, 1448)) < 25.0 or old.position.distance_to(Vector2(1945, 1480)) < 25.0 or (absf(old.position.y - 1550.0) < 15.0 and old.position.x >= 500.0 and old.position.x <= 1000.0):
					old.hide()

	var feeder:=group(utility,"CoreFeeder")
	for parent_name in ["GroundDetails","FinishedInfrastructure"]:
		for old in world.get_node(parent_name).get_children():
			if old is Sprite2D and old.texture and old.texture.resource_path==PIPE and Rect2(1200,750,550,250).has_point(old.position):
				old.hide()

	# Limpeza de props residuais em SVG plano (crate.svg / barrel.svg) no Núcleo de Sucateia
	var structures := world.get_node_or_null("Structures")
	if structures:
		for child in structures.get_children():
			for sub in child.get_children():
				if sub is Sprite2D and sub.texture:
					var res_path: String = sub.texture.resource_path
					if res_path.ends_with("/crate.svg") or res_path.ends_with("/barrel.svg"):
						if Rect2(1000, 750, 800, 450).has_point(child.position):
							child.hide()
							child.process_mode = Node.PROCESS_MODE_DISABLED

	# Ports sit inside the visible reactor outlet and the workshop's
	# right-hand receiver. Every flange joins its successor exactly.
	straight(feeder,"ReactorDrop",Vector2(1226,928),Vector2(1226,941))
	elbow(feeder,"ReactorTurn",Vector2(1226,941),Vector2(1254,968),true)
	straight(feeder,"MainFeed",Vector2(1254,968),Vector2(1686,968))
	elbow(feeder,"WorkshopTurn",Vector2(1686,968),Vector2(1714,940),false)
	straight(feeder,"WorkshopRise",Vector2(1714,940),Vector2(1714,810))
	utility.set_meta("scope","four wall drains, two coastal arch splices, one continuous reactor/workshop pipe and three ground-depth stairflights")
