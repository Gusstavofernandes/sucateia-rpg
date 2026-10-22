extends "res://tools/build_amarras_geography.gd"
func inside(point: Vector2,polygons: Array) -> bool:
	for polygon in polygons:
		if Geometry2D.is_point_in_polygon(point,polygon):return true
	return false
func run() -> void:
	world=load("res://maps/sucateia/sucateia.tscn").instantiate();world.set_script(null);root.add_child(world);district=world.get_node("CabosDistrict")
	district.set_script(load("res://scripts/world/cabos_district.gd"))
	for access in district.get_node("Accesses").get_children():access.set_script(load("res://scripts/world/cabos_access.gd"))
	if not district.has_node("Landings/Patamar1536"):
		marker("Patamar1536",Vector2(1640,-104),district.get_node("Landings"));var revised: Array=district.get_meta("walk_polygons");revised.append(rect(Vector2(1586,-154),Vector2(1694,-54)));district.set_meta("walk_polygons",revised)
	for point in [Vector2(469.64,-522.2),Vector2(1016.84,-522.2)]:
		var label := "PatamarT%d"%int(point.x)
		if not district.has_node("Landings/"+label):
			marker(label,point,district.get_node("Landings"));var revised: Array=district.get_meta("walk_polygons");revised.append(rect(point-Vector2(40,37),point+Vector2(40,37)));district.set_meta("walk_polygons",revised)
	if not district.has_meta("secondary_joint_caps"):
		var revised: Array=district.get_meta("walk_polygons")
		for point in [Vector2(310,-982),Vector2(410,-975),Vector2(510,-975),Vector2(650,-983)]:revised.append(rect(point-Vector2(14,14),point+Vector2(14,14)))
		district.set_meta("walk_polygons",revised);district.set_meta("secondary_joint_caps",true)
	var guards: Node2D=district.get_node("ElevatedGuards");for child in guards.get_children():child.free()
	var polygons: Array=district.get_meta("walk_polygons");var body := StaticBody2D.new();body.collision_layer=4;body.collision_mask=2;guards.add_child(body);var count := 0
	# Only true boundaries of the UNION are solid; crossings and alternate routes remain open.
	for polygon in polygons:
		for i in range(polygon.size()):
			var a: Vector2=polygon[i];var b: Vector2=polygon[(i+1)%polygon.size()];var delta := b-a;var cuts: Array[float]=[0.,1.]
			for other in polygons:
				for j in range(other.size()):
					var crossing: Variant=Geometry2D.segment_intersects_segment(a,b,other[j],other[(j+1)%other.size()])
					if crossing!=null:cuts.append(clampf((crossing-a).dot(delta)/delta.length_squared(),0.,1.))
			cuts.sort()
			for j in range(cuts.size()-1):
				if cuts[j+1]-cuts[j]<.0001:continue
				var p: Vector2=a+delta*cuts[j];var q: Vector2=a+delta*cuts[j+1];var middle := p.lerp(q,.5);var normal := delta.normalized().orthogonal()*.25
				if inside(middle+normal,polygons)==inside(middle-normal,polygons):continue
				var collision := CollisionShape2D.new();var segment := SegmentShape2D.new();segment.a=p;segment.b=q;collision.shape=segment;body.add_child(collision);count+=1
	district.set_meta("boundary_segments",count)
	world.set_script(load("res://scripts/world/sucateia.gd"));own(world);var packed := PackedScene.new();var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("CABOS layer scripts/boundaries saved=",error," boundary segments=",count)
	world.queue_free();world=null;district=null;guards=null;body=null;packed=null;await process_frame;await process_frame;quit(error)
